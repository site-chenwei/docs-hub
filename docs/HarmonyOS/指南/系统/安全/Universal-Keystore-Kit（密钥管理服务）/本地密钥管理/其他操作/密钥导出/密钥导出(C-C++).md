---
title: "密钥导出(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "其他操作"
  - "密钥导出"
  - "密钥导出(C/C++)"
captured_at: "2026-04-17T01:35:51.976Z"
---

# 密钥导出(C/C++)

业务需要获取持久化存储的非对称密钥的公钥时使用，当前支持ECC/RSA/ED25519/X25519/SM2的公钥导出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/dNrUuL_sRfW69asm_SGglw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013554Z&HW-CC-Expire=86400&HW-CC-Sign=951AA0E1E5774D5E4D7DF71BCE5EF060A55F5810E9B9224F5D17EEB5E7B67357)

轻量级智能穿戴仅支持RSA公钥导出。

从API 23开始支持[群组密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview)特性。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

1.  构造对应参数。
    
    -   keyAlias：密钥别名，封装成[OH\_Huks\_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob)结构，密钥别名最大长度为128字节。
    -   paramSetIn：预留参数，暂不需要处理，传空即可。
    -   key：用于放置导出的公钥，为[OH\_Huks\_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob)类型对象，需要业务提前申请好内存，需申请足够容纳获取到的密钥属性集的内存大小。
2.  调用接口[OH\_Huks\_GetKeyItemParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_getkeyitemparamset)，传入上述参数。
    
3.  返回值为成功码/错误码，导出公钥以标准的X.509规范的DER格式封装在参数key中，具体请参考[公钥材料格式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-concepts#公钥材料格式)。
    

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
/\* 以下以生成ECC密钥为例 \*/
OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet, const struct OH\_Huks\_Param \*params,
                            uint32\_t paramCount)
{
    OH\_Huks\_Result ret = OH\_Huks\_InitParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_AddParams(\*paramSet, params, paramCount);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        return ret;
    }
    ret = OH\_Huks\_BuildParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        return ret;
    }
    return ret;
}

struct OH\_Huks\_Param g\_testGenerateKeyParam\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
                                                 {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
                                                 {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
                                                 {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};

static OH\_Huks\_Result GenerateKeyHelper(const char \*alias)
{
    struct OH\_Huks\_Blob aliasBlob = {.size = (uint32\_t)strlen(alias), .data = (uint8\_t \*)alias};
    struct OH\_Huks\_ParamSet \*testGenerateKeyParamSet = nullptr;
    struct OH\_Huks\_Result ohResult;
    do {
        /\* 1.初始化密钥属性集 \*/
        ohResult = InitParamSet(&testGenerateKeyParamSet, g\_testGenerateKeyParam,
                                sizeof(g\_testGenerateKeyParam) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2.生成密钥 \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
    } while (0);
    OH\_Huks\_FreeParamSet(&testGenerateKeyParamSet);
    return ohResult;
}

static napi\_value ExportKey(napi\_env env, napi\_callback\_info info)
{
    /\* 1. 参数构造：确定密钥别名 \*/
    const char \*alias = "test\_key";
    struct OH\_Huks\_Blob aliasBlob = { .size = (uint32\_t)strlen(alias), .data = (uint8\_t \*)alias };
    /\* 生成密钥 \*/
    OH\_Huks\_Result genResult = GenerateKeyHelper(alias);
    if (genResult.errorCode != OH\_HUKS\_SUCCESS) {
        napi\_value ret;
        napi\_create\_int32(env, genResult.errorCode, &ret);
        return ret;
    }
    /\* 构造参数：为待导出公钥申请内存 \*/
    uint8\_t \*pubKey = (uint8\_t \*)malloc(512); // 请业务按实际密钥大小评估申请
    if (pubKey == nullptr) {
        return nullptr;
    }
    struct OH\_Huks\_Blob keyBlob = { 256, pubKey };
    struct OH\_Huks\_Result ohResult;
    do {
        ohResult = OH\_Huks\_ExportPublicKeyItem(&aliasBlob, nullptr, &keyBlob);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);
    free(pubKey);
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
