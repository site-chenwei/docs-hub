---
title: "HMAC(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥使用"
  - "HMAC"
  - "HMAC(C/C++)"
captured_at: "2026-04-17T01:35:51.577Z"
---

# HMAC(C/C++)

HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code）。具体的场景介绍及支持的算法规格，请参考[HMAC介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-overview)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

**生成密钥**

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  初始化密钥属性集。
    
3.  调用[OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem)生成密钥，HMAC支持的规格请参考[密钥生成支持的算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview#支持的算法)。
    

除此之外，开发者也可以参考[密钥导入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview#支持的算法)的规格介绍，导入已有的密钥。

**执行HMAC**

1.  获取密钥别名。
    
2.  获取待运算的数据。
    
3.  调用[OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset)指定算法参数配置。
    
4.  调用[OH\_Huks\_InitSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
    
5.  调用[OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession)结束密钥会话，获取哈希后的数据。
    

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>

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

static struct OH\_Huks\_Param g\_genHmacParams\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_HMAC},
                                                 {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_MAC},
                                                 {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
                                                 {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA384}};

static const uint32\_t HMAC\_COMMON\_SIZE = 1024;
OH\_Huks\_Result HksHmacTest(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*hmacParamSet,
                           const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*hashText)
{
    uint8\_t handleE\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleE};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, hmacParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, hmacParamSet, inData, hashText);
    return ret;
}

static napi\_value HmacKey(napi\_env env, napi\_callback\_info info)
{
    char tmpKeyAlias\[\] = "test\_hmac";
    struct OH\_Huks\_Blob keyAlias = {(uint32\_t)strlen(tmpKeyAlias), (uint8\_t \*)tmpKeyAlias};
    struct OH\_Huks\_ParamSet \*hmacParamSet = nullptr;
    OH\_Huks\_Result ohResult;

    do {
        ohResult = InitParamSet(&hmacParamSet, g\_genHmacParams, sizeof(g\_genHmacParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = OH\_Huks\_GenerateKeyItem(&keyAlias, hmacParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        char tmpInData\[\] = "HMAC\_MAC\_INDATA\_1";
        struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(tmpInData), (uint8\_t \*)tmpInData};
        uint8\_t cipher\[HMAC\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob hashText = {HMAC\_COMMON\_SIZE, cipher};

        ohResult = HksHmacTest(&keyAlias, hmacParamSet, &inData, &hashText);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);

    OH\_Huks\_FreeParamSet(&hmacParamSet);
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
