---
title: "使用RSA非对称密钥分段加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用RSA非对称密钥分段加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.489Z"
---

# 使用RSA非对称密钥分段加解密(C/C++)

对应的算法规格请查看[非对称密钥加解密算法规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec#rsa)。

**加密**

1.  调用[OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate)，生成RSA密钥类型为RSA1024、素数个数为2的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。
    
    如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#rsa)和[随机生成非对称密钥对](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
    
2.  调用[OH\_CryptoAsymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_create)，指定字符串参数'RSA1024|PKCS1'，创建非对称密钥类型为RSA1024、填充模式为PKCS1的Cipher实例，用于完成加解密操作。
    
3.  调用[OH\_CryptoAsymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（keyPair），初始化加密Cipher实例。
    
4.  多次调用[OH\_CryptoAsymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_final)，传入明文，获取加密后的数据。
    
    -   OH\_CryptoAsymCipher\_Final输出结果可能为NULL，在访问具体数据前，需要先判断结果是否为NULL，避免产生异常。
        
    -   此处将明文按64个字节一组拆分，多次加密。使用1024位密钥，每次将生成128字节密文。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-qGlVQUlTJWmPAnlxW2LXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013550Z&HW-CC-Expire=86400&HW-CC-Sign=2A24A912678D8350BAEA80969CB1B36F9C445C65ED8C44E8EC49EF7C0EB3C56F)
        
        非对称密钥的分段加解密是指当明文大于单次加解密支持的数据长度时，需要将待加解密数据分为合适长度的数据段，并对每个数据段执行加解密操作。详细介绍可见[非对称分段加解密介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-by-segment#非对称加解密)。
        

**解密**

1.  由于RSA算法的Cipher实例不支持重复init操作，需要调用[OH\_CryptoAsymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_create)，重新生成Cipher实例。
    
2.  调用[OH\_CryptoAsymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（keyPair）初始化解密Cipher实例。
    
3.  多次调用[OH\_CryptoAsymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_final)，传入密文，获取解密后的数据。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <algorithm>
#include <vector>
#include <string>

static std::vector<uint8\_t> doTestRsaEnc(OH\_CryptoKeyPair \*keyPair, std::vector<uint8\_t> &plainText)
{
    std::vector<uint8\_t> cipherText;
    OH\_CryptoAsymCipher \*cipher = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymCipher\_Create("RSA1024|PKCS1", &cipher);
    if (ret != CRYPTO\_SUCCESS) {
        return std::vector<uint8\_t>{};
    }

    ret = OH\_CryptoAsymCipher\_Init(cipher, CRYPTO\_ENCRYPT\_MODE, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        return std::vector<uint8\_t>{};
    }

    size\_t plainTextSplitLen = 64;
    for (size\_t i = 0; i < plainText.size(); i += plainTextSplitLen) {
        Crypto\_DataBlob in = {};
        in.data = plainText.data() + i;
        if (i + plainTextSplitLen > plainText.size()) {
            in.len = plainText.size() - i;
        } else {
            in.len = plainTextSplitLen;
        }
        Crypto\_DataBlob out = {};
        ret = OH\_CryptoAsymCipher\_Final(cipher, &in, &out);
        if (ret != CRYPTO\_SUCCESS) {
            OH\_CryptoAsymCipher\_Destroy(cipher);
            return std::vector<uint8\_t>{};
        }
        cipherText.insert(cipherText.end(), out.data, out.data + out.len);
        OH\_Crypto\_FreeDataBlob(&out);
    }

    OH\_CryptoAsymCipher\_Destroy(cipher);
    return cipherText;
}

static std::vector<uint8\_t> doTestRsaDec(OH\_CryptoKeyPair \*keyPair, std::vector<uint8\_t> &encryptText)
{
    std::vector<uint8\_t> decryptText;
    OH\_CryptoAsymCipher \*cipher = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymCipher\_Create("RSA1024|PKCS1", &cipher);
    if (ret != CRYPTO\_SUCCESS) {
        return std::vector<uint8\_t>{};
    }

    ret = OH\_CryptoAsymCipher\_Init(cipher, CRYPTO\_DECRYPT\_MODE, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymCipher\_Destroy(cipher);
        return std::vector<uint8\_t>{};
    }

    size\_t cipherTextSplitLen = 128; // RSA密钥每次加密生成的密文字节长度计算方式：密钥位数/8。
    for (size\_t i = 0; i < encryptText.size(); i += cipherTextSplitLen) {
        Crypto\_DataBlob in = {};
        in.data = encryptText.data() + i;
        if (i + cipherTextSplitLen > encryptText.size()) {
            in.len = encryptText.size() - i;
        } else {
            in.len = cipherTextSplitLen;
        }
        Crypto\_DataBlob out = {};
        ret = OH\_CryptoAsymCipher\_Final(cipher, &in, &out);
        if (ret != CRYPTO\_SUCCESS) {
            OH\_CryptoAsymCipher\_Destroy(cipher);
            return std::vector<uint8\_t>{};
        }
        decryptText.insert(decryptText.end(), out.data, out.data + out.len);
        OH\_Crypto\_FreeDataBlob(&out);
    }

    OH\_CryptoAsymCipher\_Destroy(cipher);
    return decryptText;
}

OH\_Crypto\_ErrCode doTestRsaEncLongMessage()
{
    OH\_CryptoAsymKeyGenerator \*keyGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("RSA1024", &keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    OH\_CryptoKeyPair \*keyPair = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Generate(keyGen, &keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(keyGen);
        return ret;
    }

    std::string message =
        "This is a long plainTest! This is a long plainTest! This is a long plainTest!"
        "This is a long plainTest! This is a long plainTest! This is a long plainTest! This is a long plainTest!"
        "This is a long plainTest! This is a long plainTest! This is a long plainTest! This is a long plainTest!"
        "This is a long plainTest! This is a long plainTest! This is a long plainTest! This is a long plainTest!"
        "This is a long plainTest! This is a long plainTest! This is a long plainTest! This is a long plainTest!"
        "This is a long plainTest! This is a long plainTest! This is a long plainTest! This is a long plainTest!"
        "This is a long plainTest! This is a long plainTest! This is a long plainTest! This is a long plainTest!"
        "This is a long plainTest! This is a long plainTest! This is a long plainTest! This is a long plainTest!";

    std::vector<uint8\_t> plainText(message.begin(), message.end());
    std::vector<uint8\_t> cipherText = doTestRsaEnc(keyPair, plainText);
    std::vector<uint8\_t> decryptText = doTestRsaDec(keyPair, cipherText);

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
