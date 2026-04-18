---
title: "签名/验签(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-signing-signature-verification-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥使用"
  - "签名/验签"
  - "签名/验签(C/C++)"
captured_at: "2026-04-17T01:35:51.360Z"
---

# 签名/验签(C/C++)

当前指导提供以下示例，供开发者参考完成签名、验签开发：

-   密钥算法为ECC256、摘要算法为SHA256，请见开发案例：[ECC256/SHA256](#ecc256sha256)
-   密钥算法为SM2、摘要算法为SM3，请见开发案例：[SM2/SM3](#sm2sm3)
-   密钥算法为SM2、摘要算法为NoDigest，请见开发案例：[SM2/NoDigest](#sm2nodigest)
-   密钥算法为RSA、摘要算法为SHA256、填充模式为PSS，请见开发案例：[RSA/SHA256/PSS](#rsasha256pss)
-   密钥算法为RSA、摘要算法为SHA256、填充模式为PKCS1\_V1\_5，请见开发案例：[RSA/SHA256/PKCS1\_V1\_5](#rsasha256pkcs1_v1_5)
-   密钥算法为RSA、摘要算法为SHA384、填充模式为PSS，请见开发案例：[RSA/SHA384/PSS](#rsasha384pss)

具体的场景介绍及支持的算法规格，请参考[签名/验签支持的算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-signing-signature-verification-overview#支持的算法)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

**生成密钥**

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  初始化密钥属性集。
    
3.  调用[OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    

除此之外，开发者也可以参考[密钥导入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview)，导入已有的密钥。

**签名**

1.  获取密钥别名。
    
2.  指定待签名的明文数据。
    
3.  调用[OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset)指定算法参数配置。
    
4.  调用[OH\_Huks\_InitSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
    
5.  调用[OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession)结束密钥会话，获取签名signature。
    

**验签**

1.  获取密钥别名。
    
2.  获取待验证的签名signature。
    
3.  调用[OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset)指定算法参数配置。
    
4.  调用[OH\_Huks\_InitSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
    
5.  调用[OH\_Huks\_UpdateSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_updatesession)更新密钥会话。
    
6.  调用[OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession)结束密钥会话，验证签名。
    

**删除密钥**

当密钥废弃不用时，需要调用[OH\_Huks\_DeleteKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_deletekeyitem)删除密钥，具体请参考[密钥删除](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-ndk)。

#### 开发案例

#### \[h2\]ECC256/SHA256

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

static struct OH\_Huks\_Param g\_genSignVerifyParamsTestECC\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN | OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
};

static struct OH\_Huks\_Param g\_signParamsTestECC\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256}};

static struct OH\_Huks\_Param g\_verifyParamsTestECC\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256}};

static const uint32\_t ECC\_COMMON\_SIZE = 256;
static const char \*DATA\_TO\_SIGN\_ECC = "Hks\_ECC\_Sign\_Verify\_Test\_0000000000000000000000000000000000000000000000000000000"
                                      "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
                                      "00000000000000000000000000000000000000000000000000"
                                      "00000000000000000000000\_string";

/\* 1. 生成密钥 \*/
static OH\_Huks\_Result GenerateKeyECC(const struct OH\_Huks\_Blob \*keyAlias,
                                     const struct OH\_Huks\_ParamSet \*genParamSet)
{
    return OH\_Huks\_GenerateKeyItem(keyAlias, genParamSet, nullptr);
}

/\* 2. 签名 \*/
static OH\_Huks\_Result SignDataECC(const struct OH\_Huks\_Blob \*keyAlias,
                                  const struct OH\_Huks\_ParamSet \*signParamSet,
                                  const struct OH\_Huks\_Blob \*inData,
                                  struct OH\_Huks\_Blob \*outDataSign)
{
    uint8\_t handleS\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleSign = {(uint32\_t)sizeof(uint64\_t), handleS};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    ohResult = OH\_Huks\_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    struct OH\_Huks\_Blob finishInData = {0, NULL};
    ohResult = OH\_Huks\_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);
    
    return ohResult;
}

/\* 3. 验签 \*/
static OH\_Huks\_Result VerifySignatureECC(const struct OH\_Huks\_Blob \*keyAlias,
                                         const struct OH\_Huks\_ParamSet \*verifyParamSet,
                                         const struct OH\_Huks\_Blob \*inData,
                                         const struct OH\_Huks\_Blob \*signature)
{
    uint8\_t handleV\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleVerify = {(uint32\_t)sizeof(uint64\_t), handleV};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    uint8\_t temp\[\] = "out";
    struct OH\_Huks\_Blob verifyOut = {(uint32\_t)sizeof(temp), temp};
    ohResult = OH\_Huks\_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    ohResult = OH\_Huks\_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);
    
    return ohResult;
}

napi\_value SignVerifyKeyECC(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob g\_keyAlias = {(uint32\_t)strlen("test\_signVerify\_ECC"), (uint8\_t \*)"test\_signVerify\_ECC"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(DATA\_TO\_SIGN\_ECC), (uint8\_t \*)DATA\_TO\_SIGN\_ECC};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*signParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*verifyParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    
    do {
        ohResult = InitParamSet(&genParamSet, g\_genSignVerifyParamsTestECC,
                                sizeof(g\_genSignVerifyParamsTestECC) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        ohResult = InitParamSet(&signParamSet, g\_signParamsTestECC,
                                sizeof(g\_signParamsTestECC) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        ohResult = InitParamSet(&verifyParamSet, g\_verifyParamsTestECC,
                                sizeof(g\_verifyParamsTestECC) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 1. 生成密钥 \*/
        ohResult = GenerateKeyECC(&g\_keyAlias, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 2. 签名 \*/
        uint8\_t outDataS\[ECC\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob outDataSign = {ECC\_COMMON\_SIZE, outDataS};
        ohResult = SignDataECC(&g\_keyAlias, signParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 3. 验签 \*/
        ohResult = VerifySignatureECC(&g\_keyAlias, verifyParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);
    
    (void)OH\_Huks\_DeleteKeyItem(&g\_keyAlias, genParamSet);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&signParamSet);
    OH\_Huks\_FreeParamSet(&verifyParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]SM2/SM3

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

static struct OH\_Huks\_Param g\_genSignVerifyParamsSM2\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_SM2},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_SM2\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN | OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SM3},
};

static struct OH\_Huks\_Param g\_signParamsSM2\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_SM2},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_SM2\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SM3}
};

static struct OH\_Huks\_Param g\_verifyParamsSM2\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_SM2},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_SM2\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SM3}
};

static const uint32\_t SM2\_COMMON\_SIZE = 256;
static const char \*DATA\_TO\_SIGN\_SM2 = "Hks\_SM2\_Sign\_Verify\_Test\_0000000000000000000000000000000000000000000000000000000"
                                      "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
                                      "0000000000000000000000000000000000000000000000000"
                                      "000000000000000000000000\_string";

/\* 1. 生成密钥 \*/
static OH\_Huks\_Result GenerateKeySM2(const struct OH\_Huks\_Blob \*keyAlias,
                                     const struct OH\_Huks\_ParamSet \*genParamSet)
{
    return OH\_Huks\_GenerateKeyItem(keyAlias, genParamSet, nullptr);
}

/\* 2. 签名 \*/
static OH\_Huks\_Result SignDataSM2(const struct OH\_Huks\_Blob \*keyAlias,
                                  const struct OH\_Huks\_ParamSet \*signParamSet,
                                  const struct OH\_Huks\_Blob \*inData,
                                  struct OH\_Huks\_Blob \*outDataSign)
{
    uint8\_t handleS\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleSign = {(uint32\_t)sizeof(uint64\_t), handleS};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    ohResult = OH\_Huks\_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    struct OH\_Huks\_Blob finishInData = {0, NULL};
    ohResult = OH\_Huks\_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);
    
    return ohResult;
}

/\* 3. 验签 \*/
static OH\_Huks\_Result VerifySignatureSM2(const struct OH\_Huks\_Blob \*keyAlias,
                                         const struct OH\_Huks\_ParamSet \*verifyParamSet,
                                         const struct OH\_Huks\_Blob \*inData,
                                         const struct OH\_Huks\_Blob \*signature)
{
    uint8\_t handleV\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleVerify = {(uint32\_t)sizeof(uint64\_t), handleV};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    uint8\_t temp\[\] = "out";
    struct OH\_Huks\_Blob verifyOut = {(uint32\_t)sizeof(temp), temp};
    ohResult = OH\_Huks\_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    ohResult = OH\_Huks\_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);
    
    return ohResult;
}

napi\_value SignVerifyKeySM2SM3(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob g\_keyAlias = {(uint32\_t)strlen("test\_signVerify\_SM2\_SM3"),
        (uint8\_t \*)"test\_signVerify\_SM2\_SM3"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(DATA\_TO\_SIGN\_SM2), (uint8\_t \*)DATA\_TO\_SIGN\_SM2};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*signParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*verifyParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    
    do {
        ohResult = InitParamSet(&genParamSet, g\_genSignVerifyParamsSM2,
                                sizeof(g\_genSignVerifyParamsSM2) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        ohResult = InitParamSet(&signParamSet, g\_signParamsSM2,
                                sizeof(g\_signParamsSM2) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        ohResult = InitParamSet(&verifyParamSet, g\_verifyParamsSM2,
                                sizeof(g\_verifyParamsSM2) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 1. 生成密钥 \*/
        ohResult = GenerateKeySM2(&g\_keyAlias, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 2. 签名 \*/
        uint8\_t outDataS\[SM2\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob outDataSign = {SM2\_COMMON\_SIZE, outDataS};
        ohResult = SignDataSM2(&g\_keyAlias, signParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 3. 验签 \*/
        ohResult = VerifySignatureSM2(&g\_keyAlias, verifyParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);
    
    (void)OH\_Huks\_DeleteKeyItem(&g\_keyAlias, genParamSet);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&signParamSet);
    OH\_Huks\_FreeParamSet(&verifyParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]SM2/NoDigest

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

static struct OH\_Huks\_Param g\_genSignVerifyParamsSM2NoDigest\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_SM2},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_SM2\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN | OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE},
};

static struct OH\_Huks\_Param g\_signParamsSM2NoDigest\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_SM2},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_SM2\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}
};

static struct OH\_Huks\_Param g\_verifyParamsSM2NoDigest\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_SM2},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_SM2\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}
};

static const uint32\_t SM2\_COMMON\_SIZE = 256;
static const char \*DATA\_TO\_SIGN\_SM2\_NODIGEST = "12345678901234567890123456789012";

/\* 1. 生成密钥 \*/
static OH\_Huks\_Result GenerateKeySM2(const struct OH\_Huks\_Blob \*keyAlias,
                                     const struct OH\_Huks\_ParamSet \*genParamSet)
{
    return OH\_Huks\_GenerateKeyItem(keyAlias, genParamSet, nullptr);
}

/\* 2. 签名 \*/
static OH\_Huks\_Result SignDataSM2NoDigest(const struct OH\_Huks\_Blob \*keyAlias,
                                          const struct OH\_Huks\_ParamSet \*signParamSet,
                                          const struct OH\_Huks\_Blob \*inData,
                                          struct OH\_Huks\_Blob \*outDataSign)
{
    uint8\_t handleS\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleSign = {(uint32\_t)sizeof(uint64\_t), handleS};

    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    ohResult = OH\_Huks\_FinishSession(&handleSign, signParamSet, inData, outDataSign);

    return ohResult;
}

/\* 3. 验签  \*/
static OH\_Huks\_Result VerifySignatureSM2NoDigest(const struct OH\_Huks\_Blob \*keyAlias,
                                                 const struct OH\_Huks\_ParamSet \*verifyParamSet,
                                                 const struct OH\_Huks\_Blob \*inData,
                                                 const struct OH\_Huks\_Blob \*signature)
{
    uint8\_t handleV\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleVerify = {(uint32\_t)sizeof(uint64\_t), handleV};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    uint8\_t temp\[\] = "out";
    struct OH\_Huks\_Blob verifyOut = {(uint32\_t)sizeof(temp), temp};
    ohResult = OH\_Huks\_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    ohResult = OH\_Huks\_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);
    
    return ohResult;
}

napi\_value SignVerifyKeySM2NoDigest(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob g\_keyAlias = {(uint32\_t)strlen("test\_signVerify\_SM2\_NoDigest"),
        (uint8\_t \*)"test\_signVerify\_SM2\_NoDigest"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(DATA\_TO\_SIGN\_SM2\_NODIGEST), (uint8\_t \*)DATA\_TO\_SIGN\_SM2\_NODIGEST};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*signParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*verifyParamSet = nullptr;
    OH\_Huks\_Result ohResult;

    do {
        ohResult = InitParamSet(&genParamSet, g\_genSignVerifyParamsSM2NoDigest,
                                sizeof(g\_genSignVerifyParamsSM2NoDigest) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&signParamSet, g\_signParamsSM2NoDigest,
                                sizeof(g\_signParamsSM2NoDigest) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&verifyParamSet, g\_verifyParamsSM2NoDigest,
                                sizeof(g\_verifyParamsSM2NoDigest) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 1. 生成密钥 \*/
        ohResult = GenerateKeySM2(&g\_keyAlias, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 2. 签名 \*/
        uint8\_t outDataS\[SM2\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob outDataSign = {SM2\_COMMON\_SIZE, outDataS};
        ohResult = SignDataSM2NoDigest(&g\_keyAlias, signParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 3. 验签 \*/
        ohResult = VerifySignatureSM2NoDigest(&g\_keyAlias, verifyParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);

    (void)OH\_Huks\_DeleteKeyItem(&g\_keyAlias, genParamSet);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&signParamSet);
    OH\_Huks\_FreeParamSet(&verifyParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]RSA/SHA256/PSS

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

static struct OH\_Huks\_Param g\_genSignVerifyParamsRsaPss\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN | OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PSS},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
};

static struct OH\_Huks\_Param g\_signParamsRsaPss\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PSS},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN}
};

static struct OH\_Huks\_Param g\_verifyParamsRsaPss\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PSS},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY}
};

static const uint32\_t RSA\_COMMON\_SIZE = 1024;
static const char \*DATA\_TO\_SIGN\_RSA\_PSS = "Hks\_RSA\_PSS\_Sign\_Verify\_Test\_0000000000000000000000000000000000000000000"
                                          "000000000000000000000000000000000000000000000000000000000000000000000000"
                                          "000000000000000000000000000000000000000000000000000000000000000\_string";

/\* 1. 生成密钥 \*/
static OH\_Huks\_Result GenerateKey(const struct OH\_Huks\_Blob \*keyAlias,
                                  const struct OH\_Huks\_ParamSet \*genParamSet)
{
    return OH\_Huks\_GenerateKeyItem(keyAlias, genParamSet, nullptr);
}

/\* 2. 签名 \*/
static OH\_Huks\_Result SignData(const struct OH\_Huks\_Blob \*keyAlias,
                               const struct OH\_Huks\_ParamSet \*signParamSet,
                               const struct OH\_Huks\_Blob \*inData,
                               struct OH\_Huks\_Blob \*outDataSign)
{
    uint8\_t handleS\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleSign = {(uint32\_t)sizeof(uint64\_t), handleS};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    ohResult = OH\_Huks\_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    struct OH\_Huks\_Blob finishInData = {0, nullptr};
    ohResult = OH\_Huks\_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);
    
    return ohResult;
}

/\* 3. 验签 \*/
static OH\_Huks\_Result VerifySignature(const struct OH\_Huks\_Blob \*keyAlias,
                                      const struct OH\_Huks\_ParamSet \*verifyParamSet,
                                      const struct OH\_Huks\_Blob \*inData,
                                      const struct OH\_Huks\_Blob \*signature)
{
    uint8\_t handleV\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleVerify = {(uint32\_t)sizeof(uint64\_t), handleV};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    uint8\_t temp\[\] = "out";
    struct OH\_Huks\_Blob verifyOut = {(uint32\_t)sizeof(temp), temp};
    ohResult = OH\_Huks\_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    ohResult = OH\_Huks\_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);
    
    return ohResult;
}

napi\_value SignVerifyKeyRsaSha256Pss(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob g\_keyAlias = {(uint32\_t)strlen("test\_signVerify\_RSA\_SHA256\_PSS"),
        (uint8\_t \*)"test\_signVerify\_RSA\_SHA256\_PSS"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(DATA\_TO\_SIGN\_RSA\_PSS), (uint8\_t \*)DATA\_TO\_SIGN\_RSA\_PSS};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*signParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*verifyParamSet = nullptr;
    OH\_Huks\_Result ohResult;

    do {
        ohResult = InitParamSet(&genParamSet, g\_genSignVerifyParamsRsaPss,
                                sizeof(g\_genSignVerifyParamsRsaPss) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&signParamSet, g\_signParamsRsaPss, sizeof(g\_signParamsRsaPss) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&verifyParamSet, g\_verifyParamsRsaPss,
                                sizeof(g\_verifyParamsRsaPss) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = GenerateKey(&g\_keyAlias, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        uint8\_t outDataS\[RSA\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob outDataSign = {RSA\_COMMON\_SIZE, outDataS};
        ohResult = SignData(&g\_keyAlias, signParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = VerifySignature(&g\_keyAlias, verifyParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);

    (void)OH\_Huks\_DeleteKeyItem(&g\_keyAlias, genParamSet);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&signParamSet);
    OH\_Huks\_FreeParamSet(&verifyParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]RSA/SHA256/PKCS1\_V1\_5

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

static struct OH\_Huks\_Param g\_genSignVerifyParamsRsaPkcs1\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN | OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PKCS1\_V1\_5},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
};

static struct OH\_Huks\_Param g\_signParamsRsaPkcs1\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PKCS1\_V1\_5},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256}
};

static struct OH\_Huks\_Param g\_verifyParamsRsaPkcs1\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PKCS1\_V1\_5},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256}
};

static const uint32\_t RSA\_COMMON\_SIZE = 1024;
static const char \*DATA\_TO\_SIGN\_RSA\_PKCS1 = "Hks\_RSA\_PKCS1\_V1\_5\_Sign\_Verify\_Test\_000000000000000000000000000000"
                                            "000000000000000000000000000000000000000000000000000000000000000000"
                                            "000000000000000000000000000000000000000000000000000000000000\_string";

/\* 1. 生成密钥 \*/
static OH\_Huks\_Result GenerateKey(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*genParamSet)
{
    return OH\_Huks\_GenerateKeyItem(keyAlias, genParamSet, nullptr);
}

/\* 2. 验签 \*/
static OH\_Huks\_Result SignData(const struct OH\_Huks\_Blob \*keyAlias,
                               const struct OH\_Huks\_ParamSet \*signParamSet,
                               const struct OH\_Huks\_Blob \*inData,
                               struct OH\_Huks\_Blob \*outDataSign)
{
    uint8\_t handleS\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleSign = {(uint32\_t)sizeof(uint64\_t), handleS};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    ohResult = OH\_Huks\_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    struct OH\_Huks\_Blob finishInData = {0, nullptr};
    ohResult = OH\_Huks\_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);
    
    return ohResult;
}

/\* 3. 验签 \*/
static OH\_Huks\_Result VerifySignature(const struct OH\_Huks\_Blob \*keyAlias,
                                      const struct OH\_Huks\_ParamSet \*verifyParamSet,
                                      const struct OH\_Huks\_Blob \*inData,
                                      const struct OH\_Huks\_Blob \*signature)
{
    uint8\_t handleV\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleVerify = {(uint32\_t)sizeof(uint64\_t), handleV};
    
    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    uint8\_t temp\[\] = "out";
    struct OH\_Huks\_Blob verifyOut = {(uint32\_t)sizeof(temp), temp};
    ohResult = OH\_Huks\_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    ohResult = OH\_Huks\_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);
    
    return ohResult;
}

napi\_value SignVerifyKeyRsaSha256Pkcs1V15(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob g\_keyAlias = {(uint32\_t)strlen("test\_signVerify\_RSA\_SHA256\_PKCS1"),
        (uint8\_t \*)"test\_signVerify\_RSA\_SHA256\_PKCS1"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(DATA\_TO\_SIGN\_RSA\_PKCS1), (uint8\_t \*)DATA\_TO\_SIGN\_RSA\_PKCS1};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*signParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*verifyParamSet = nullptr;
    OH\_Huks\_Result ohResult;

    do {
        ohResult = InitParamSet(&genParamSet, g\_genSignVerifyParamsRsaPkcs1,
                                sizeof(g\_genSignVerifyParamsRsaPkcs1) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&signParamSet, g\_signParamsRsaPkcs1,
                                sizeof(g\_signParamsRsaPkcs1) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&verifyParamSet, g\_verifyParamsRsaPkcs1,
                                sizeof(g\_verifyParamsRsaPkcs1) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        ohResult = GenerateKey(&g\_keyAlias, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        uint8\_t outDataS\[RSA\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob outDataSign = {RSA\_COMMON\_SIZE, outDataS};
        ohResult = SignData(&g\_keyAlias, signParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        ohResult = VerifySignature(&g\_keyAlias, verifyParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);

    (void)OH\_Huks\_DeleteKeyItem(&g\_keyAlias, genParamSet);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&signParamSet);
    OH\_Huks\_FreeParamSet(&verifyParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### \[h2\]RSA/SHA384/PSS

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

static struct OH\_Huks\_Param g\_genSignVerifyParamsRsaSha384Pss\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN | OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PSS},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA384},
};

static struct OH\_Huks\_Param g\_signParamsRsaSha384Pss\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PSS},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA384},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN}
};

static struct OH\_Huks\_Param g\_verifyParamsRsaSha384Pss\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PSS},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA384},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY}
};

static const uint32\_t RSA\_COMMON\_SIZE = 1024;
static const char \*DATA\_TO\_SIGN\_RSA\_SHA384\_PSS = "Hks\_RSA\_SHA384\_PSS\_Sign\_Verify\_Test\_000000000000000000000000000"
                                                  "000000000000000000000000000000000000000000000000000000000000"
                                                  "000000000000000000000000000000000000000000000000000000\_string";

/\* 1. 生成密钥 \*/
static OH\_Huks\_Result GenerateKeyRSA(const struct OH\_Huks\_Blob \*keyAlias,
                                     const struct OH\_Huks\_ParamSet \*genParamSet)
{
    return OH\_Huks\_GenerateKeyItem(keyAlias, genParamSet, nullptr);
}

/\* 2. 签名 \*/
static OH\_Huks\_Result SignDataRSA(const struct OH\_Huks\_Blob \*keyAlias,
                                  const struct OH\_Huks\_ParamSet \*signParamSet,
                                  const struct OH\_Huks\_Blob \*inData,
                                  struct OH\_Huks\_Blob \*outDataSign)
{
    uint8\_t handleS\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleSign = {(uint32\_t)sizeof(uint64\_t), handleS};

    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    ohResult = OH\_Huks\_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    struct OH\_Huks\_Blob finishInData = {0, NULL};
    ohResult = OH\_Huks\_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);
    
    return ohResult;
}

/\* 3. 验签  \*/
static OH\_Huks\_Result VerifySignatureRSA(const struct OH\_Huks\_Blob \*keyAlias,
                                         const struct OH\_Huks\_ParamSet \*verifyParamSet,
                                         const struct OH\_Huks\_Blob \*inData,
                                         const struct OH\_Huks\_Blob \*signature)
{
    uint8\_t handleV\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleVerify = {(uint32\_t)sizeof(uint64\_t), handleV};

    OH\_Huks\_Result ohResult = OH\_Huks\_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    uint8\_t temp\[\] = "out";
    struct OH\_Huks\_Blob verifyOut = {(uint32\_t)sizeof(temp), temp};
    ohResult = OH\_Huks\_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }

    ohResult = OH\_Huks\_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);

    return ohResult;
}

napi\_value SignVerifyKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob g\_keyAlias = {(uint32\_t)strlen("test\_signVerify\_RSA\_SHA384\_PSS"),
        (uint8\_t \*)"test\_signVerify\_RSA\_SHA384\_PSS"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(DATA\_TO\_SIGN\_RSA\_SHA384\_PSS),
        (uint8\_t \*)DATA\_TO\_SIGN\_RSA\_SHA384\_PSS};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*signParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*verifyParamSet = nullptr;
    OH\_Huks\_Result ohResult;

    do {
        ohResult = InitParamSet(&genParamSet, g\_genSignVerifyParamsRsaSha384Pss,
                                sizeof(g\_genSignVerifyParamsRsaSha384Pss) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&signParamSet, g\_signParamsRsaSha384Pss,
                                sizeof(g\_signParamsRsaSha384Pss) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&verifyParamSet, g\_verifyParamsRsaSha384Pss,
                                sizeof(g\_verifyParamsRsaSha384Pss) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 1. 生成密钥 \*/
        ohResult = GenerateKeyRSA(&g\_keyAlias, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 2. 签名 \*/
        uint8\_t outDataS\[RSA\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob outDataSign = {RSA\_COMMON\_SIZE, outDataS};
        ohResult = SignDataRSA(&g\_keyAlias, signParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        /\* 3. 验签 \*/
        ohResult = VerifySignatureRSA(&g\_keyAlias, verifyParamSet, &inData, &outDataSign);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);

    (void)OH\_Huks\_DeleteKeyItem(&g\_keyAlias, genParamSet);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&signParamSet);
    OH\_Huks\_FreeParamSet(&verifyParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
