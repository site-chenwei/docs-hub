---
title: "密钥派生(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥使用"
  - "密钥派生"
  - "密钥派生(C/C++)"
captured_at: "2026-04-17T01:35:51.482Z"
---

# 密钥派生(C/C++)

以HKDF256和PBKDF2密钥为例，完成密钥派生。具体的场景介绍及支持的算法规格，请参考[密钥派生支持的算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-overview#支持的算法)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

**生成密钥**

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  初始化密钥属性集，可指定参数，OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识基于该密钥派生出的密钥是否由HUKS管理。
    
    -   当TAG设置为OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS时，表示基于该密钥派生出的密钥，由HUKS管理，可保证派生密钥全生命周期不出安全环境。
        
    -   当TAG设置为OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED时，表示基于该密钥派生出的密钥，返回给调用方管理，由业务自行保证密钥安全。
        
    -   若业务未设置TAG的具体值，表示基于该密钥派生出的密钥，即可由HUKS管理，也可返回给调用方管理，业务可在后续派生时再选择使用何种方式保护密钥。
        
3.  调用[OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    

除此之外，开发者也可以参考[密钥导入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview)，导入已有的密钥。

**密钥派生**

1.  获取密钥别名，指定对应的属性参数HuksOptions。
    
    可指定参数OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识派生得到的密钥是否由HUKS管理。
    
    | 生成 | 派生 | 规格 |
    | :-- | :-- | :-- |
    | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
    | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
    | 未指定TAG具体值 | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
    | 未指定TAG具体值 | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
    | 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |
    
    注：派生时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。
    
2.  调用[OH\_Huks\_InitSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
    
3.  调用[OH\_Huks\_UpdateSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_updatesession)更新密钥会话。
    
4.  调用[OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession)结束密钥会话，完成派生。
    

**删除密钥**

当密钥废弃不用时，需要调用OH\_Huks\_DeleteKeyItem删除密钥，具体请参考[密钥删除](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-ndk)。

#### 开发案例

#### \[h2\]HKDF

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>

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

static const uint32\_t DERIVE\_KEY\_SIZE\_32 = 32;
static const uint32\_t DERIVE\_KEY\_SIZE\_256 = 256;
static struct OH\_Huks\_Blob g\_deriveKeyAlias = {(uint32\_t)strlen("test\_derive"), (uint8\_t \*)"test\_derive"};
static struct OH\_Huks\_Param g\_genDeriveParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_hkdfParams\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_HKDF},
                                              {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
                                              {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
                                              {.tag = OH\_HUKS\_TAG\_DERIVE\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_32}};
static struct OH\_Huks\_Param g\_hkdfFinishParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_deriveKeyAlias},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256}};
static const uint32\_t COMMON\_SIZE = 2048;
static const char \*G\_DERIVE\_IN\_DATA = "Hks\_HKDF\_Derive\_Test\_0\_string";
static OH\_Huks\_Result PerformHkdfDerivation(const struct OH\_Huks\_Blob \*genAlias,
    struct OH\_Huks\_ParamSet \*hkdfParamSet,
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet,
    const struct OH\_Huks\_Blob &inData)
{
    OH\_Huks\_Result ohResult;
    // Init
    uint8\_t handleD\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleDerive = {sizeof(uint64\_t), handleD};
    ohResult = OH\_Huks\_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Update
    uint8\_t tmpOut\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outData = {COMMON\_SIZE, tmpOut};
    ohResult = OH\_Huks\_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Finish
    uint8\_t outDataD\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataDerive = {COMMON\_SIZE, outDataD};
    ohResult = OH\_Huks\_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
    return ohResult;
}

napi\_value HkdfDeriveKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob genAlias = {(uint32\_t)strlen("test\_signVerify"), (uint8\_t \*)"test\_signVerify"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(G\_DERIVE\_IN\_DATA), (uint8\_t \*)G\_DERIVE\_IN\_DATA};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&genParamSet, g\_genDeriveParams, sizeof(g\_genDeriveParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&hkdfParamSet, g\_hkdfParams, sizeof(g\_hkdfParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        // finish paramset
        ohResult =
            InitParamSet(&hkdfFinishParamSet, g\_hkdfFinishParams, sizeof(g\_hkdfFinishParams) /
              sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 1. 生成密钥 \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&genAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. 派生密钥 \*/
        ohResult = PerformHkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
    } while (0);
    (void)OH\_Huks\_DeleteKeyItem(&genAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(&g\_deriveKeyAlias, nullptr);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&hkdfParamSet);
    OH\_Huks\_FreeParamSet(&hkdfFinishParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]PBKDF2

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

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
static const uint32\_t DERIVE\_KEY\_SIZE\_32 = 32;
static const uint32\_t DERIVE\_KEY\_SIZE\_256 = 256;
static const uint32\_t DERIVE\_KEY\_ITERATION = 10000;
static const uint32\_t SALT\_SIZE = 8;
static const char DERIVE\_KEY\_SALT\[SALT\_SIZE\] = "mysalt1";
static struct OH\_Huks\_Blob g\_deriveKeyAlias = {(uint32\_t)strlen("test\_derive"), (uint8\_t \*)"test\_derive"};
static struct OH\_Huks\_Param g\_genDeriveParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_hkdfParams\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_PBKDF2},
                                              {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
                                              {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
                                              {.tag = OH\_HUKS\_TAG\_DERIVE\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_32},
                                              {.tag = OH\_HUKS\_TAG\_ITERATION, .uint32Param = DERIVE\_KEY\_ITERATION},
                                              {.tag = OH\_HUKS\_TAG\_SALT,
                                               .blob = {
                                                   .size = SALT\_SIZE,
                                                   .data = (uint8\_t \*) DERIVE\_KEY\_SALT
                                               }}};
static struct OH\_Huks\_Param g\_hkdfFinishParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_deriveKeyAlias},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB}};
static const uint32\_t COMMON\_SIZE = 1024;
static const char \*G\_DERIVE\_IN\_DATA = "Hks\_PBKDF2\_Derive\_Test\_0\_string";
static OH\_Huks\_Result PerformPbkdfDerivation(const struct OH\_Huks\_Blob \*genAlias,
    struct OH\_Huks\_ParamSet \*hkdfParamSet,
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet,
    const struct OH\_Huks\_Blob &inData)
{
    OH\_Huks\_Result ohResult;
    // Init
    uint8\_t handleD\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleDerive = {sizeof(uint64\_t), handleD};
    ohResult = OH\_Huks\_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Update
    uint8\_t tmpOut\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outData = {COMMON\_SIZE, tmpOut};
    ohResult = OH\_Huks\_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Finish
    uint8\_t outDataD\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataDerive = {COMMON\_SIZE, outDataD};
    ohResult = OH\_Huks\_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
    return ohResult;
}

napi\_value PbkdfDeriveKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob genAlias = {(uint32\_t)strlen("test\_signVerify"), (uint8\_t \*)"test\_signVerify"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(G\_DERIVE\_IN\_DATA), (uint8\_t \*)G\_DERIVE\_IN\_DATA};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&genParamSet, g\_genDeriveParams, sizeof(g\_genDeriveParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = InitParamSet(&hkdfParamSet, g\_hkdfParams, sizeof(g\_hkdfParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult =InitParamSet(&hkdfFinishParamSet, g\_hkdfFinishParams, sizeof(g\_hkdfFinishParams) /
              sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 1. 生成密钥 \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&genAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. 派生密钥 \*/
        ohResult = PerformPbkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
    } while (0);
    (void)OH\_Huks\_DeleteKeyItem(&genAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(&g\_deriveKeyAlias, nullptr);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&hkdfParamSet);
    OH\_Huks\_FreeParamSet(&hkdfFinishParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
