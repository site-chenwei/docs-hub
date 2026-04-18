---
title: "使用ECDH进行密钥协商(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-ecdh-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥协商"
  - "密钥协商开发指导"
  - "使用ECDH进行密钥协商(C/C++)"
captured_at: "2026-04-17T01:35:48.861Z"
---

# 使用ECDH进行密钥协商(C/C++)

对应的算法规格请查看[密钥协商算法规格：ECDH](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-overview#ecdh)。

#### 开发步骤

1.  调用[OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate)、[OH\_CryptoAsymKeyGenerator\_Convert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_convert)生成密钥算法为ECC、密钥长度为256位的非对称密钥（keyPair）。
    
    如何生成ECC非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：ECC](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#ecc)和[随机生成非对称密钥对](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
    
2.  调用[OH\_CryptoKeyAgreement\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_create)，指定字符串参数'ECC256'，创建密钥算法为ECC、密钥长度为256位的密钥协议生成器。
    
3.  调用[OH\_CryptoKeyAgreement\_GenerateSecret](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_generatesecret)，基于传入的私钥（keyPair.priKey）与公钥（keyPair.pubKey）进行密钥协商，返回共享密钥。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include "CryptoArchitectureKit/crypto\_key\_agreement.h"
#include "file.h"
#include <cstdio>
#include <cstring>

static OH\_Crypto\_ErrCode GenerateSecret(OH\_CryptoKeyAgreement \*eccKeyAgreement, OH\_CryptoKeyPair \*keyPairA,
    OH\_CryptoKeyPair \*keyPairB, Crypto\_DataBlob \*secret)
{
    OH\_CryptoPrivKey \*privKey = OH\_CryptoKeyPair\_GetPrivKey(keyPairA);
    OH\_CryptoPubKey \*pubKey = OH\_CryptoKeyPair\_GetPubKey(keyPairB);
    return OH\_CryptoKeyAgreement\_GenerateSecret(eccKeyAgreement, privKey, pubKey, secret);
}

static OH\_Crypto\_ErrCode compareSecrets(const Crypto\_DataBlob \*secret1, const Crypto\_DataBlob \*secret2)
{
    if ((secret1->len == secret2->len) &&
        (memcmp(secret1->data, secret2->data, secret1->len) == 0)) {
        return CRYPTO\_SUCCESS;
    }
    return CRYPTO\_OPERTION\_ERROR;
}

static OH\_Crypto\_ErrCode CovertKeyPairByBlob(OH\_CryptoAsymKeyGenerator \*eccGen, OH\_CryptoKeyPair \*\*keyPair)
{
    uint8\_t pubKeyArray\[\] = {48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7,
        3, 66, 0, 4, 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246,
        162, 215, 71, 81, 58, 202, 121, 26, 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167,
        160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235, 215, 159, 239, 28, 106, 124,
        171, 34, 145, 124, 174, 57, 92};
    uint8\_t priKeyArray\[\] = {48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16,
        27, 4, 171, 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6,
        8, 42, 134, 72, 206, 61, 3, 1, 7};
    Crypto\_DataBlob pubKeyBlob = {pubKeyArray, sizeof(pubKeyArray)};
    Crypto\_DataBlob priKeyBlob = {priKeyArray, sizeof(priKeyArray)};
    return OH\_CryptoAsymKeyGenerator\_Convert(eccGen, CRYPTO\_DER, &pubKeyBlob, &priKeyBlob, keyPair);
}

OH\_Crypto\_ErrCode doTestEcdhKeyAgreement()
{
    OH\_CryptoAsymKeyGenerator \*eccGen = nullptr;
    OH\_CryptoKeyPair \*keyPairA = nullptr;
    OH\_CryptoKeyPair \*keyPairB = nullptr;
    OH\_CryptoKeyAgreement \*eccKeyAgreement = nullptr;
    Crypto\_DataBlob secret1 = { 0 };
    Crypto\_DataBlob secret2 = { 0 };

    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("ECC256", &eccGen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = CovertKeyPairByBlob(eccGen, &keyPairA);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    ret = OH\_CryptoAsymKeyGenerator\_Generate(eccGen, &keyPairB);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    ret = OH\_CryptoKeyAgreement\_Create("ECC256", &eccKeyAgreement);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    // 使用A的公钥和B的私钥进行密钥协商。
    ret = GenerateSecret(eccKeyAgreement, keyPairB, keyPairA, &secret1);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    // 使用A的私钥和B的公钥进行密钥协商。
    ret = GenerateSecret(eccKeyAgreement, keyPairA, keyPairB, &secret2);
    if (ret != CRYPTO\_SUCCESS) {
        goto goto\_cleanup;
    }

    // 比较两次协商的结果。
    ret = compareSecrets(&secret1, &secret2);
    if (ret != CRYPTO\_SUCCESS) {
        printf("ecdh result is not equal\\n");
        goto goto\_cleanup;
    }

goto\_cleanup:
    OH\_Crypto\_FreeDataBlob(&secret1);
    OH\_Crypto\_FreeDataBlob(&secret2);
    OH\_CryptoKeyAgreement\_Destroy(eccKeyAgreement);
    OH\_CryptoKeyPair\_Destroy(keyPairA);
    OH\_CryptoKeyPair\_Destroy(keyPairB);
    OH\_CryptoAsymKeyGenerator\_Destroy(eccGen);
    return ret;
}
