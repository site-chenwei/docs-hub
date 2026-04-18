---
title: "密钥协商(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥使用"
  - "密钥协商"
  - "密钥协商(C/C++)"
captured_at: "2026-04-17T01:35:51.436Z"
---

# 密钥协商(C/C++)

以X25519、DH和ECDH协商密钥类型为例，在密钥由HUKS管理的情况下，完成密钥协商。具体的场景介绍及支持的算法规格，请参考[密钥协商支持的算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-overview#支持的算法)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)或[密钥导入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview)。

密钥生成时，可指定参数，OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识此步骤生成的密钥是否由HUKS管理。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-arkts)。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，可指定参数OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识协商得到的密钥是否由HUKS管理。

-   当TAG设置为OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS时，表示基于该密钥协商出的密钥，由HUKS管理，可保证协商密钥全生命周期不出安全环境。
    
-   当TAG设置为OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED时，表示基于该密钥协商出的密钥，返回给调用方管理，由业务自行保证密钥安全。
    
-   若业务未设置TAG的具体值，表示基于该密钥协商出的密钥，既可由HUKS管理，也可返回给调用方管理，业务可在后续协商时再选择使用何种方式保护密钥。
    

| 生成 | 协商 | 规格 |
| :-- | :-- | :-- |
| OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| 未指定TAG具体值 | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

注：协商时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-ndk)。

#### 开发案例

下面分别以X25519、DH和ECDH密钥为例，进行协商。

#### \[h2\]X25519非对称密钥协商用例

准备X25519密钥协商材料：

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

/\* 初始化参数 \*/
static OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet, const struct OH\_Huks\_Param \*params,
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
static struct OH\_Huks\_Blob g\_keyAliasFinal1001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_1\_final"),
                                                  (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_1\_final"};
/\* 集成密钥参数集 \*/
static struct OH\_Huks\_Param g\_genAgreeParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsInit01\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Blob g\_keyAliasFinal2001 = {(uint32\_t)strlen("HksX25519AgreeKeyAliasTest001\_2\_final"),
                                                  (uint8\_t \*)"HksX25519AgreeKeyAliasTest001\_2\_final"};
static struct OH\_Huks\_Param g\_agreeParamsInit02\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static const uint32\_t X25519\_COMMON\_SIZE = 256;
static struct OH\_Huks\_Blob g\_keyAlias01001 = {(uint32\_t)strlen("HksX25519AgreeKeyAliasTest001\_1"),
                                              (uint8\_t \*)"HksX25519AgreeKeyAliasTest001\_1"};
static struct OH\_Huks\_Blob g\_keyAlias02001 = {(uint32\_t)strlen("HksX25519AgreeKeyAliasTest001\_2"),
                                              (uint8\_t \*)"HksX25519AgreeKeyAliasTest001\_2"};

执行密钥协商：

/\* 导出密钥 \*/
OH\_Huks\_Result HksX25519AgreeExport(const struct OH\_Huks\_Blob \*keyAlias1, const struct OH\_Huks\_Blob \*keyAlias2,
    struct OH\_Huks\_Blob \*publicKey1, struct OH\_Huks\_Blob \*publicKey2,
    const struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ret = OH\_Huks\_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char \*IN\_DATA = "Hks\_X25519\_Agree\_Test";
/\* 协商密钥操作 \*/
OH\_Huks\_Result HksX25519AgreeFinish(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*publicKey,
    const struct OH\_Huks\_ParamSet \*initParamSet,
    const struct OH\_Huks\_ParamSet \*finishParamSet, struct OH\_Huks\_Blob \*outData)
{
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(IN\_DATA), (uint8\_t \*)IN\_DATA};
    uint8\_t handleU\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleU};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint8\_t outDataU\[X25519\_COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataUpdate = {X25519\_COMMON\_SIZE, outDataU};
    ret = OH\_Huks\_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH\_Huks\_Result InitializeAgreeParamSets(struct OH\_Huks\_ParamSet \*\*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet01,
    struct OH\_Huks\_ParamSet \*\*finishParamSet01,
    struct OH\_Huks\_ParamSet \*\*initParamSet02,
    struct OH\_Huks\_ParamSet \*\*finishParamSet02)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g\_genAgreeParams,
                            sizeof(g\_genAgreeParams) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g\_agreeParamsInit01,
                            sizeof(g\_agreeParamsInit01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g\_agreeParamsFinish01,
                            sizeof(g\_agreeParamsFinish01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g\_agreeParamsInit02,
                            sizeof(g\_agreeParamsInit02) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g\_agreeParamsFinish02,
                            sizeof(g\_agreeParamsFinish02) / sizeof(OH\_Huks\_Param));
    return ohResult;
}

static OH\_Huks\_Result GenerateKeyPair(struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ohResult;
    
    /\* 设备A生成密钥 \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    /\* 设备B生成密钥 \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH\_Huks\_Result KeyAgreement(struct OH\_Huks\_Blob \*g\_keyAlias,
    struct OH\_Huks\_Blob \*publicKey,
    struct OH\_Huks\_Blob \*outData,
    struct OH\_Huks\_ParamSet \*initParamSet,
    struct OH\_Huks\_ParamSet \*finishParamSet)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    /\* 协商密钥 \*/
    ohResult = HksX25519AgreeFinish(g\_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH\_Huks\_Blob \*genKeyAlias,
    struct OH\_Huks\_Blob \*genKeyAliasFinal,
    struct OH\_Huks\_ParamSet \*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet,
    struct OH\_Huks\_ParamSet \*\*finishParamSet)
{
    OH\_Huks\_DeleteKeyItem(genKeyAlias, genParamSet);
    OH\_Huks\_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH\_Huks\_FreeParamSet(initParamSet);
    OH\_Huks\_FreeParamSet(finishParamSet);
}

/\* 协商密钥整体流程 \*/
napi\_value X25519AgreeKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet02 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet02 = nullptr;
    struct OH\_Huks\_Blob publicKey01 = {.size = OH\_HUKS\_AES\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob publicKey02 = {.size = OH\_HUKS\_AES\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob outData01 = {.size = X25519\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData02 = {.size = X25519\_COMMON\_SIZE, .data = nullptr};
    OH\_Huks\_Result ohResult;
    do {
        /\* 1.确定密钥别名集成密钥参数集 \*/
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2.设备A和设备B生成密钥 \*/
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3.设备A、B导出公钥 \*/
        ohResult = HksX25519AgreeExport(&g\_keyAlias01001, &g\_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 4.设备A、B执行密钥协商 \*/
        ohResult = KeyAgreement(&g\_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g\_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /\* 5.设备A、B删除密钥 \*/
    CleanKey(&g\_keyAlias01001, &g\_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g\_keyAlias02001, &g\_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH\_Huks\_FreeParamSet(&genParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]DH密钥协商用例

准备DH密钥协商材料：

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

/\* 初始化参数 \*/
static OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet, const struct OH\_Huks\_Param \*params,
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
static struct OH\_Huks\_Blob g\_keyAliasFinal1001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_1\_final"),
                                                  (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_1\_final"};
/\* 集成密钥参数集 \*/
static struct OH\_Huks\_Param g\_genAgreeParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_DH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_DH\_KEY\_SIZE\_2048}};
static struct OH\_Huks\_Param g\_agreeParamsInit01\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_DH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_DH\_KEY\_SIZE\_2048}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\_2\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Blob g\_keyAliasFinal2001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_2\_final"),
                                                  (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_2\_final"};
static struct OH\_Huks\_Param g\_agreeParamsInit02\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_DH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_DH\_KEY\_SIZE\_2048}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\_2\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static const uint32\_t DH\_COMMON\_SIZE = 2048;
static struct OH\_Huks\_Blob g\_keyAlias01001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_1"),
                                              (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_1"};
static struct OH\_Huks\_Blob g\_keyAlias02001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_2"),
                                              (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_2"};

执行密钥协商：

static OH\_Huks\_Result MallocAndCheckBlobData(struct OH\_Huks\_Blob \*blob, const uint32\_t blobSize)
{
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    if (blobSize == 0 || blobSize > DH\_COMMON\_SIZE) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
        return ret;
    }
    blob->data = (uint8\_t \*)malloc(blobSize);
    if (blob->data == NULL) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
    }
    return ret;
}
/\* 导出密钥 \*/
OH\_Huks\_Result HksDHAgreeExport(const struct OH\_Huks\_Blob \*keyAlias1, const struct OH\_Huks\_Blob \*keyAlias2,
    struct OH\_Huks\_Blob \*publicKey1, struct OH\_Huks\_Blob \*publicKey2,
    const struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ret = OH\_Huks\_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char \*IN\_DATA = "Hks\_DH\_Agree\_Test";
/\* 协商密钥操作 \*/
OH\_Huks\_Result HksDHAgreeFinish(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*publicKey,
    const struct OH\_Huks\_ParamSet \*initParamSet,
    const struct OH\_Huks\_ParamSet \*finishParamSet, struct OH\_Huks\_Blob \*outData)
{
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(IN\_DATA), (uint8\_t \*)IN\_DATA};
    uint8\_t handleU\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleU};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint8\_t outDataU\[DH\_COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataUpdate = {DH\_COMMON\_SIZE, outDataU};
    ret = OH\_Huks\_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH\_Huks\_Result InitializeAgreeParamSets(struct OH\_Huks\_ParamSet \*\*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet01,
    struct OH\_Huks\_ParamSet \*\*finishParamSet01,
    struct OH\_Huks\_ParamSet \*\*initParamSet02,
    struct OH\_Huks\_ParamSet \*\*finishParamSet02)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g\_genAgreeParams,
                            sizeof(g\_genAgreeParams) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g\_agreeParamsInit01,
                            sizeof(g\_agreeParamsInit01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g\_agreeParamsFinish01,
                            sizeof(g\_agreeParamsFinish01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g\_agreeParamsInit02,
                            sizeof(g\_agreeParamsInit02) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g\_agreeParamsFinish02,
                            sizeof(g\_agreeParamsFinish02) / sizeof(OH\_Huks\_Param));
    return ohResult;
}

static OH\_Huks\_Result GenerateKeyPair(struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ohResult;
    
    /\* 设备A生成密钥 \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    /\* 设备B生成密钥 \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH\_Huks\_Result KeyAgreement(struct OH\_Huks\_Blob \*g\_keyAlias,
    struct OH\_Huks\_Blob \*publicKey,
    struct OH\_Huks\_Blob \*outData,
    struct OH\_Huks\_ParamSet \*initParamSet,
    struct OH\_Huks\_ParamSet \*finishParamSet)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    /\* 协商密钥 \*/
    ohResult = HksDHAgreeFinish(g\_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH\_Huks\_Blob \*genKeyAlias,
    struct OH\_Huks\_Blob \*genKeyAliasFinal,
    struct OH\_Huks\_ParamSet \*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet,
    struct OH\_Huks\_ParamSet \*\*finishParamSet)
{
    OH\_Huks\_DeleteKeyItem(genKeyAlias, genParamSet);
    OH\_Huks\_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH\_Huks\_FreeParamSet(initParamSet);
    OH\_Huks\_FreeParamSet(finishParamSet);
}

/\* 协商密钥整体流程 \*/
napi\_value DhAgreeKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet02 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet02 = nullptr;
    struct OH\_Huks\_Blob publicKey01 = {.size = DH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob publicKey02 = {.size = DH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData01 = {.size = DH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData02 = {.size = DH\_COMMON\_SIZE, .data = nullptr};

    OH\_Huks\_Result ohResult;
    do {
        /\* 1.确定密钥别名集成密钥参数集 \*/
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2.设备A和设备B生成密钥 \*/
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3.设备A、B导出公钥 \*/
        ohResult = HksDHAgreeExport(&g\_keyAlias01001, &g\_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 4.设备A、B执行密钥协商 \*/
        ohResult = KeyAgreement(&g\_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g\_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /\* 5.设备A、B删除密钥 \*/
    CleanKey(&g\_keyAlias01001, &g\_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g\_keyAlias02001, &g\_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH\_Huks\_FreeParamSet(&genParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]ECDH密钥协商用例

准备ECDH密钥协商材料：

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

/\* 初始化参数 \*/
static OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet, const struct OH\_Huks\_Param \*params,
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
static const uint32\_t IV\_SIZE = 16;
static uint8\_t IV\[IV\_SIZE\] = {0}; // this is a test value, for real use the iv should be different every time
static struct OH\_Huks\_Blob g\_keyAliasFinal1001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_1\_final"),
                                                  (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_1\_final"};
/\* 集成密钥参数集 \*/
static struct OH\_Huks\_Param g\_genAgreeParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsInit01\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECDH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_CBC}};
static struct OH\_Huks\_Blob g\_keyAliasFinal2001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_2\_final"),
                                                  (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_2\_final"};
static struct OH\_Huks\_Param g\_agreeParamsInit02\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECDH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_CBC}};
static const uint32\_t ECDH\_COMMON\_SIZE = 1024;
static struct OH\_Huks\_Blob g\_keyAlias01001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_1"),
                                              (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_1"};
static struct OH\_Huks\_Blob g\_keyAlias02001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_2"),
                                              (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_2"};

ECDH密钥协商的功能函数实现，包括内存分配、参数初始化、密钥生成、和资源清理等：

static OH\_Huks\_Result MallocAndCheckBlobData(struct OH\_Huks\_Blob \*blob, const uint32\_t blobSize)
{
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    if (blobSize == 0 || blobSize > ECDH\_COMMON\_SIZE) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
        return ret;
    }
    blob->data = (uint8\_t \*)malloc(blobSize);
    if (blob->data == NULL) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
    }
    return ret;
}

/\* 导出密钥 \*/
OH\_Huks\_Result HksEcdhAgreeExport(const struct OH\_Huks\_Blob \*keyAlias1, const struct OH\_Huks\_Blob \*keyAlias2,
                                  struct OH\_Huks\_Blob \*publicKey1, struct OH\_Huks\_Blob \*publicKey2,
                                  const struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ret = OH\_Huks\_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char \*IN\_DATA = "Hks\_ECDH\_Agree\_Test\_000000000000000000000000000000000000000000000000000000000000"
                              "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
                              "0000000000000000000000000000000000000000000000000000000000000000000000000\_string";
/\* 协商密钥操作 \*/
OH\_Huks\_Result HksEcdhAgreeFinish(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*publicKey,
                                  const struct OH\_Huks\_ParamSet \*initParamSet,
                                  const struct OH\_Huks\_ParamSet \*finishParamSet, struct OH\_Huks\_Blob \*outData)
{
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(IN\_DATA), (uint8\_t \*)IN\_DATA};
    uint8\_t handleU\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleU};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint8\_t outDataU\[ECDH\_COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataUpdate = {ECDH\_COMMON\_SIZE, outDataU};
    ret = OH\_Huks\_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH\_Huks\_Result InitializeAgreeParamSets(struct OH\_Huks\_ParamSet \*\*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet01,
    struct OH\_Huks\_ParamSet \*\*finishParamSet01,
    struct OH\_Huks\_ParamSet \*\*initParamSet02,
    struct OH\_Huks\_ParamSet \*\*finishParamSet02)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g\_genAgreeParams,
                            sizeof(g\_genAgreeParams) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g\_agreeParamsInit01,
                            sizeof(g\_agreeParamsInit01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g\_agreeParamsFinish01,
                            sizeof(g\_agreeParamsFinish01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g\_agreeParamsInit02,
                            sizeof(g\_agreeParamsInit02) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g\_agreeParamsFinish02,
                            sizeof(g\_agreeParamsFinish02) / sizeof(OH\_Huks\_Param));
    return ohResult;
}

static OH\_Huks\_Result GenerateKeyPair(struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ohResult;
    
    /\* 设备A生成密钥 \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    /\* 设备B生成密钥 \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH\_Huks\_Result KeyAgreement(struct OH\_Huks\_Blob \*g\_keyAlias,
    struct OH\_Huks\_Blob \*publicKey,
    struct OH\_Huks\_Blob \*outData,
    struct OH\_Huks\_ParamSet \*initParamSet,
    struct OH\_Huks\_ParamSet \*finishParamSet)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    /\* 协商密钥 \*/
    ohResult = HksEcdhAgreeFinish(g\_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH\_Huks\_Blob \*genKeyAlias,
    struct OH\_Huks\_Blob \*genKeyAliasFinal,
    struct OH\_Huks\_ParamSet \*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet,
    struct OH\_Huks\_ParamSet \*\*finishParamSet)
{
    OH\_Huks\_DeleteKeyItem(genKeyAlias, genParamSet);
    OH\_Huks\_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH\_Huks\_FreeParamSet(initParamSet);
    OH\_Huks\_FreeParamSet(finishParamSet);
}

ECDH密钥协商的完整流程实现：

/\* 协商密钥整体流程 \*/
napi\_value EcdhAgreeKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet02 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet02 = nullptr;
    struct OH\_Huks\_Blob publicKey01 = {.size = OH\_HUKS\_ECC\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob publicKey02 = {.size = OH\_HUKS\_ECC\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob outData01 = {.size = ECDH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData02 = {.size = ECDH\_COMMON\_SIZE, .data = nullptr};
    OH\_Huks\_Result ohResult;
    do {
        /\* 1.确定密钥别名集成密钥参数集 \*/
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2.设备A和设备B生成密钥 \*/
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3.设备A、B导出公钥 \*/
        ohResult = HksEcdhAgreeExport(&g\_keyAlias01001, &g\_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 4.设备A、B执行密钥协商 \*/
        ohResult = KeyAgreement(&g\_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g\_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /\* 5.设备A、B删除密钥 \*/
    CleanKey(&g\_keyAlias01001, &g\_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g\_keyAlias02001, &g\_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH\_Huks\_FreeParamSet(&genParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
