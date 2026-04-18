---
title: "使用RSA非对称密钥（PKCS1模式）加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用RSA非对称密钥（PKCS1模式）加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.493Z"
---

# 使用RSA非对称密钥（PKCS1模式）加解密(C/C++)

对应的算法规格请查看[非对称密钥加解密算法规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec#rsa)。

**加密**

1.  调用[OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate)，生成RSA密钥类型为RSA1024、素数个数为2的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。
    
    如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#rsa)和[随机生成非对称密钥对](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
    
2.  调用[OH\_CryptoAsymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_create)，指定字符串参数'RSA1024|PKCS1'，创建非对称密钥类型为RSA1024、填充模式为PKCS1的Cipher实例，用于完成加解密操作。
    
3.  调用[OH\_CryptoAsymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（keyPair），初始化加密Cipher实例。
    
4.  调用[OH\_CryptoAsymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_final)，传入明文，获取加密后的数据。
    
    -   OH\_CryptoAsymCipher\_Final输出结果可能为NULL，在访问具体数据前，需要先判断结果是否为NULL，避免产生异常。
    -   当数据量较大时，可以多次调用OH\_CryptoAsymCipher\_Final，即[分段加解密](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment-ndk)。

**解密**

1.  由于RSA算法的Cipher实例不支持重复init操作，需要调用[OH\_CryptoAsymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_create)，重新生成Cipher实例。
    
2.  调用[OH\_CryptoAsymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（keyPair）初始化解密Cipher实例。
    
3.  调用[OH\_CryptoAsymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_final)，传入密文，获取解密后的数据。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstring>

static OH\_Crypto\_ErrCode doRsaEncrypt(const Crypto\_DataBlob \*plainData, OH\_CryptoKeyPair \*\*keyPair,
    OH\_CryptoAsymKeyGenerator \*\*keyGen, Crypto\_DataBlob \*encryptedData)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("RSA1024", keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = OH\_CryptoAsymKeyGenerator\_Generate(\*keyGen, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(\*keyGen);
        return ret;
    }

    OH\_CryptoAsymCipher \*cipher = nullptr;
    ret = OH\_CryptoAsymCipher\_Create("RSA1024|PKCS1", &cipher);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(\*keyPair);
        OH\_CryptoAsymKeyGenerator\_Destroy(\*keyGen);
        return ret;
    }

    ret = OH\_CryptoAsymCipher\_Init(cipher, CRYPTO\_ENCRYPT\_MODE, \*keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        OH\_CryptoKeyPair\_Destroy(\*keyPair);
        OH\_CryptoAsymKeyGenerator\_Destroy(\*keyGen);
        return ret;
    }

    ret = OH\_CryptoAsymCipher\_Final(cipher, plainData, encryptedData);
    OH\_CryptoAsymCipher\_Destroy(cipher);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(\*keyPair);
        OH\_CryptoAsymKeyGenerator\_Destroy(\*keyGen);
        return ret;
    }

    return ret;
}

static OH\_Crypto\_ErrCode doRsaDecrypt(const Crypto\_DataBlob \*encryptedData, OH\_CryptoKeyPair \*keyPair,
    const Crypto\_DataBlob \*expectedPlainData)
{
    OH\_CryptoAsymCipher \*cipher = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymCipher\_Create("RSA1024|PKCS1", &cipher);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = OH\_CryptoAsymCipher\_Init(cipher, CRYPTO\_DECRYPT\_MODE, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        return ret;
    }

    Crypto\_DataBlob decrypted = { 0 };
    ret = OH\_CryptoAsymCipher\_Final(cipher, encryptedData, &decrypted);
    OH\_CryptoAsymCipher\_Destroy(cipher);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    if ((decrypted.len != expectedPlainData->len) ||
        (memcmp(decrypted.data, expectedPlainData->data, decrypted.len) != 0)) {
        OH\_Crypto\_FreeDataBlob(&decrypted);
        return CRYPTO\_OPERTION\_ERROR;
    }

    OH\_Crypto\_FreeDataBlob(&decrypted);
    return ret;
}

OH\_Crypto\_ErrCode doTestRsaEncDec()
{
    const char \*testData = "Hello, RSA!";
    Crypto\_DataBlob plainData = {
        .data = (uint8\_t \*)testData,
        .len = strlen(testData)
    };

    OH\_CryptoKeyPair \*keyPair = nullptr;
    OH\_CryptoAsymKeyGenerator \*keyGen = nullptr;
    Crypto\_DataBlob encryptedData = { 0 };

    OH\_Crypto\_ErrCode ret = doRsaEncrypt(&plainData, &keyPair, &keyGen, &encryptedData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = doRsaDecrypt(&encryptedData, keyPair, &plainData);
    OH\_Crypto\_FreeDataBlob(&encryptedData);
    OH\_CryptoKeyPair\_Destroy(keyPair);
    OH\_CryptoAsymKeyGenerator\_Destroy(keyGen);
    return ret;
}
