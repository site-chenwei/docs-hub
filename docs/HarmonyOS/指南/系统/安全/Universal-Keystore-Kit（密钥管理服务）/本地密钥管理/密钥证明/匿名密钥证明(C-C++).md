---
title: "匿名密钥证明(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-anon-attestation-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥证明"
  - "匿名密钥证明(C/C++)"
captured_at: "2026-04-17T01:35:51.683Z"
---

# 匿名密钥证明(C/C++)

在使用本功能时，需确保网络通畅。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  初始化参数集：通过[OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset)、[OH\_Huks\_AddParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_addparams)、[OH\_Huks\_BuildParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_buildparamset)构造参数集paramSet，参数集中必须包含[OH\_Huks\_KeyAlg](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keyalg)，[OH\_Huks\_KeySize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keysize)，[OH\_Huks\_KeyPurpose](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keypurpose)属性。
    
3.  将密钥别名与参数集作为参数传入[OH\_Huks\_AnonAttestKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_anonattestkeyitem)方法中，即可证明密钥。
    

#### 开发案例

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

static uint32\_t g\_size = 4096;
static uint32\_t CERT\_COUNT = 4;
void FreeCertChain(struct OH\_Huks\_CertChain \*certChain, const uint32\_t pos)
{
    if (certChain == nullptr || certChain->certs == nullptr) {
        return;
    }
    for (uint32\_t j = 0; j < pos; j++) {
        if (certChain->certs\[j\].data != nullptr) {
            free(certChain->certs\[j\].data);
            certChain->certs\[j\].data = nullptr;
        }
    }
    if (certChain->certs != nullptr) {
        free(certChain->certs);
        certChain->certs = nullptr;
    }
}

int32\_t ConstructDataToCertChain(struct OH\_Huks\_CertChain \*certChain)
{
    if (certChain == nullptr) {
        return OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT;
    }
    certChain->certsCount = CERT\_COUNT;

    certChain->certs = (struct OH\_Huks\_Blob \*)malloc(sizeof(struct OH\_Huks\_Blob) \* (certChain->certsCount));
    if (certChain->certs == nullptr) {
        return OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
    }
    for (uint32\_t i = 0; i < certChain->certsCount; i++) {
        certChain->certs\[i\].size = g\_size;
        certChain->certs\[i\].data = (uint8\_t \*)malloc(certChain->certs\[i\].size);
        if (certChain->certs\[i\].data == nullptr) {
            FreeCertChain(certChain, i);
            return OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT;
        }
    }
    return 0;
}

static struct OH\_Huks\_Param g\_genAnonAttestParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_PSS},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
};

#define CHALLENGE\_DATA "hi\_challenge\_data"
static struct OH\_Huks\_Blob g\_challenge = {sizeof(CHALLENGE\_DATA), (uint8\_t \*)CHALLENGE\_DATA};
static napi\_value AnonAttestKey(napi\_env env, napi\_callback\_info info)
{
    /\* 1.确定密钥别名 \*/
    struct OH\_Huks\_Blob genAlias = {(uint32\_t)strlen("test\_anon\_attest"), (uint8\_t \*)"test\_anon\_attest"};
    static struct OH\_Huks\_Param g\_anonAttestParams\[\] = {
        {.tag = OH\_HUKS\_TAG\_ATTESTATION\_CHALLENGE, .blob = g\_challenge},
        {.tag = OH\_HUKS\_TAG\_ATTESTATION\_ID\_ALIAS, .blob = genAlias},
    };
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*anonAttestParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    OH\_Huks\_Blob certs = {0};
    OH\_Huks\_CertChain certChain = {&certs, 0};
    do {
        /\* 2.初始化密钥参数集 \*/
        ohResult =
            InitParamSet(&genParamSet, g\_genAnonAttestParams, sizeof(g\_genAnonAttestParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult =
            InitParamSet(&anonAttestParamSet, g\_anonAttestParams, sizeof(g\_anonAttestParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = OH\_Huks\_GenerateKeyItem(&genAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        (void)ConstructDataToCertChain(&certChain);
        /\* 3.证明密钥 \*/
        ohResult = OH\_Huks\_AnonAttestKeyItem(&genAlias, anonAttestParamSet, &certChain);
    } while (0);
    FreeCertChain(&certChain, CERT\_COUNT);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&anonAttestParamSet);
    (void)OH\_Huks\_DeleteKeyItem(&genAlias, NULL);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
