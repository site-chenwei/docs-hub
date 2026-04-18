---
title: "使用DH进行密钥协商(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥协商"
  - "密钥协商开发指导"
  - "使用DH进行密钥协商(C/C++)"
captured_at: "2026-04-17T01:35:48.912Z"
---

# 使用DH进行密钥协商(C/C++)

对应的算法规格请查看[密钥协商算法规格：DH](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-overview#dh)。

#### 开发步骤

1.  调用[OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate)生成密钥算法为DH\_modp1536的非对称密钥（keyPair）。
    
    如何生成DH非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：DH](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#dh)和[随机生成非对称密钥对](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
    
2.  调用[OH\_CryptoKeyAgreement\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_create)，指定字符串参数'DH\_modp1536'，创建密钥算法为DH\_modp1536的密钥协议生成器。
    
3.  调用[OH\_CryptoKeyAgreement\_GenerateSecret](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_generatesecret)，基于传入的私钥（keyPair.priKey）与公钥（keyPair.pubKey）进行密钥协商，返回共享密钥。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include "CryptoArchitectureKit/crypto\_key\_agreement.h"
#include "file.h"
#include <cstdio>
#include <cstring>

static OH\_Crypto\_ErrCode GenerateSecret(OH\_CryptoKeyAgreement \*dhKeyAgreement, OH\_CryptoKeyPair \*keyPairA,
    OH\_CryptoKeyPair \*keyPairB, Crypto\_DataBlob \*secret)
{
    OH\_CryptoPrivKey \*privKey = OH\_CryptoKeyPair\_GetPrivKey(keyPairA);
    OH\_CryptoPubKey \*pubKey = OH\_CryptoKeyPair\_GetPubKey(keyPairB);
    return OH\_CryptoKeyAgreement\_GenerateSecret(dhKeyAgreement, privKey, pubKey, secret);
}

static OH\_Crypto\_ErrCode compareSecrets(const Crypto\_DataBlob \*secret1, const Crypto\_DataBlob \*secret2)
{
    if ((secret1->len == secret2->len) &&
        (memcmp(secret1->data, secret2->data, secret1->len) == 0)) {
        return CRYPTO\_SUCCESS;
    }
    return CRYPTO\_OPERTION\_ERROR;
}

OH\_Crypto\_ErrCode doTestDHKeyAgreement()
{
    OH\_CryptoAsymKeyGenerator \*dhGen = nullptr;
    OH\_CryptoKeyPair \*keyPairA = nullptr;
    OH\_CryptoKeyPair \*keyPairB = nullptr;
    OH\_CryptoKeyAgreement \*dhKeyAgreement = nullptr;
    Crypto\_DataBlob secret1 = { 0 };
    Crypto\_DataBlob secret2 = { 0 };
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("DH\_modp1536", &dhGen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 生成公私钥对A 和 B。
    ret = OH\_CryptoAsymKeyGenerator\_Generate(dhGen, &keyPairA);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    ret = OH\_CryptoAsymKeyGenerator\_Generate(dhGen, &keyPairB);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    ret = OH\_CryptoKeyAgreement\_Create("DH\_modp1536", &dhKeyAgreement);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    // 使用A的公钥和B的私钥进行密钥协商。
    ret = GenerateSecret(dhKeyAgreement, keyPairB, keyPairA, &secret1);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    // 使用B的公钥和A的私钥进行密钥协商。
    ret = GenerateSecret(dhKeyAgreement, keyPairA, keyPairB, &secret2);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    // 比较两次协商的结果。
    ret = compareSecrets(&secret1, &secret2);
    if (ret != CRYPTO\_SUCCESS) {
        printf("dh result is not equal\\n");
        goto goto\_cleanup;
    }

goto\_cleanup:
    OH\_Crypto\_FreeDataBlob(&secret1);
    OH\_Crypto\_FreeDataBlob(&secret2);
    OH\_CryptoKeyAgreement\_Destroy(dhKeyAgreement);
    OH\_CryptoKeyPair\_Destroy(keyPairA);
    OH\_CryptoKeyPair\_Destroy(keyPairB);
    OH\_CryptoAsymKeyGenerator\_Destroy(dhGen);
    return ret;
}
