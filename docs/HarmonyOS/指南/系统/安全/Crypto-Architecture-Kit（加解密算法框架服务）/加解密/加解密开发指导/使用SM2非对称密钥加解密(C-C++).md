---
title: "使用SM2非对称密钥加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用SM2非对称密钥加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.491Z"
---

# 使用SM2非对称密钥加解密(C/C++)

对应的算法规格请查看[非对称密钥加解密算法规格：SM2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec#sm2)。

**加密**

1.  调用[OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate)，生成SM2密钥类型为SM2\_256的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。
    
    如何生成SM2非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：SM2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#sm2)和[随机生成非对称密钥对](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
    
2.  调用[OH\_CryptoAsymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_create)，指定字符串参数'SM2\_256|SM3'，创建非对称密钥类型为SM2\_256、摘要算法为SM3的Cipher实例，用于完成加解密操作。
    
3.  调用[OH\_CryptoAsymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（keyPair），初始化加密Cipher实例。
    
4.  调用[OH\_CryptoAsymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_final)，传入明文，获取加密后的数据。
    
    OH\_CryptoAsymCipher\_Final输出结果可能为NULL，在访问具体数据前，需要先判断结果是否为NULL，避免产生异常。
    

**解密**

1.  由于SM2算法的Cipher实例不支持重复init操作，需要调用[OH\_CryptoAsymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_create)，重新生成Cipher实例。
    
2.  调用[OH\_CryptoAsymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（keyPair）初始化解密Cipher实例。
    
3.  调用[OH\_CryptoAsymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_final)，传入密文，获取解密后的数据。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <algorithm>
#include <vector>
#include <string>

static std::vector<uint8\_t> doTestSm2Enc(OH\_CryptoKeyPair \*keyPair, std::vector<uint8\_t> &plainText)
{
    std::vector<uint8\_t> cipherText;
    OH\_CryptoAsymCipher \*cipher = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymCipher\_Create("SM2\_256|SM3", &cipher);
    if (ret != CRYPTO\_SUCCESS) {
        return std::vector<uint8\_t>{};
    }

    ret = OH\_CryptoAsymCipher\_Init(cipher, CRYPTO\_ENCRYPT\_MODE, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        return std::vector<uint8\_t>{};
    }

    Crypto\_DataBlob in = {};
    in.data = plainText.data();
    in.len = plainText.size();
    Crypto\_DataBlob out = {};
    ret = OH\_CryptoAsymCipher\_Final(cipher, &in, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        return std::vector<uint8\_t>{};
    }
    cipherText.insert(cipherText.end(), out.data, out.data + out.len);
    OH\_Crypto\_FreeDataBlob(&out);

    OH\_CryptoAsymCipher\_Destroy(cipher);
    return cipherText;
}

static std::vector<uint8\_t> doTestSm2Dec(OH\_CryptoKeyPair \*keyPair, std::vector<uint8\_t> &encryptText)
{
    std::vector<uint8\_t> decryptText;
    OH\_CryptoAsymCipher \*cipher = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymCipher\_Create("SM2\_256|SM3", &cipher);
    if (ret != CRYPTO\_SUCCESS) {
        return std::vector<uint8\_t>{};
    }

    ret = OH\_CryptoAsymCipher\_Init(cipher, CRYPTO\_DECRYPT\_MODE, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        return std::vector<uint8\_t>{};
    }

    Crypto\_DataBlob in = {};
    in.data = encryptText.data();
    in.len = encryptText.size();
    Crypto\_DataBlob out = {};
    ret = OH\_CryptoAsymCipher\_Final(cipher, &in, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        return std::vector<uint8\_t>{};
    }
    decryptText.insert(decryptText.end(), out.data, out.data + out.len);
    OH\_Crypto\_FreeDataBlob(&out);

    OH\_CryptoAsymCipher\_Destroy(cipher);
    return decryptText;
}

OH\_Crypto\_ErrCode doTestSm2EncMessage()
{
    OH\_CryptoAsymKeyGenerator \*keyGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("SM2\_256", &keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    OH\_CryptoKeyPair \*keyPair = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Generate(keyGen, &keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(keyGen);
        return ret;
    }

    std::string message = "This is a test";
    std::vector<uint8\_t> plainText(message.begin(), message.end());
    std::vector<uint8\_t> cipherText = doTestSm2Enc(keyPair, plainText);
    std::vector<uint8\_t> decryptText = doTestSm2Dec(keyPair, cipherText);

    if ((plainText.size() != decryptText.size()) ||
        (!std::equal(plainText.begin(), plainText.end(), decryptText.begin()))) {
        OH\_CryptoKeyPair\_Destroy(keyPair);
        OH\_CryptoAsymKeyGenerator\_Destroy(keyGen);
        return CRYPTO\_OPERTION\_ERROR;
    }

    OH\_CryptoKeyPair\_Destroy(keyPair);
    OH\_CryptoAsymKeyGenerator\_Destroy(keyGen);
    return CRYPTO\_SUCCESS;
}
