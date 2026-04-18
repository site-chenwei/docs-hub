---
title: "使用AES"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用AES-WRAP算法对对称密钥加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.572Z"
---

# 使用AES-WRAP算法对对称密钥加解密(C/C++)

从API version 22开始，算法库支持使用该算法进行加密和解密操作。

请查看[AES-WRAP加解密算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#aes-wrap)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

如何生成AES对称密钥，请参考以下示例，并结合[对称密钥生成和转换规格：AES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#aes)和[随机生成对称密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk)理解，参考文档与当前示例可能存在入参差异，请注意区分。

**加密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'AES128-WRAP'，创建对称密钥类型为AES128-WRAP的Cipher实例，用于加密操作。
    
2.  调用[OH\_CryptoSymCipherParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_create)创建参数对象，并调用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置加密参数。
    
3.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
    
4.  加密内容较短时，可以直接调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，获取加密后的数据。
    

**解密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'AES128-WRAP'，创建对称密钥类型为AES128-WRAP的Cipher实例，用于解密操作。
    
2.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
    
3.  解密内容较短时，可直接调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，获取解密后的数据。
    

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_destroy)、[OH\_CryptoSymKey\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkey_destroy)、[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放申请的内存，销毁对象。

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_cipher.h"
#include <cstring>
#include "file.h"

// 加密函数
static OH\_Crypto\_ErrCode doAesWrapEncrypt(OH\_CryptoSymKey \*keyCtx, OH\_CryptoSymCipherParams \*params,
    Crypto\_DataBlob \*msgBlob, Crypto\_DataBlob \*encData)
{
    OH\_CryptoSymCipher \*encCtx = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymCipher\_Create("AES128-WRAP", &encCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(encCtx, CRYPTO\_ENCRYPT\_MODE, keyCtx, params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(encCtx, msgBlob, encData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

end:
    OH\_CryptoSymCipher\_Destroy(encCtx);
    return ret;
}

// 解密函数
static OH\_Crypto\_ErrCode doAesWrapDecrypt(OH\_CryptoSymKey \*keyCtx, OH\_CryptoSymCipherParams \*params,
    Crypto\_DataBlob \*encData, Crypto\_DataBlob \*decData)
{
    OH\_CryptoSymCipher \*decCtx = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymCipher\_Create("AES128-WRAP", &decCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(decCtx, CRYPTO\_DECRYPT\_MODE, keyCtx, params); // 解密使用的params与加密时相同。
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(decCtx, encData, decData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

end:
    OH\_CryptoSymCipher\_Destroy(decCtx);
    return ret;
}

OH\_Crypto\_ErrCode doTestAesWrap()
{
    OH\_CryptoSymKeyGenerator \*genCtx = nullptr;
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoSymCipherParams \*params = nullptr;
    Crypto\_DataBlob encData = {.data = nullptr, .len = 0};
    Crypto\_DataBlob decData = {.data = nullptr, .len = 0};
    uint8\_t keyData\[\] = {0xb7, 0x21, 0x3d, 0x4f, 0x63, 0x57, 0x9b, 0x97,
        0x09, 0xd9, 0x80, 0x6f, 0x9f, 0x3a, 0x6f, 0x64};
    Crypto\_DataBlob msgBlob = {.data = keyData, .len = sizeof(keyData)};
    uint8\_t iv\[8\] = {1, 2, 4, 12, 3, 4, 2, 3}; // 示例代码iv值，开发者可使用安全随机数生成。
    Crypto\_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
    // 生成对称密钥。
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create("AES128", &genCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymKeyGenerator\_Generate(genCtx, &keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 创建参数对象。
    ret = OH\_CryptoSymCipherParams\_Create(&params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    // 设置参数。
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_IV\_DATABLOB, &ivBlob); // aes-wrap只需要设置iv。
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 加密。
    ret = doAesWrapEncrypt(keyCtx, params, &msgBlob, &encData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 解密。
    ret = doAesWrapDecrypt(keyCtx, params, &encData, &decData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

end:
    OH\_CryptoSymCipherParams\_Destroy(params);
    OH\_CryptoSymKeyGenerator\_Destroy(genCtx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    OH\_Crypto\_FreeDataBlob(&encData);
    OH\_Crypto\_FreeDataBlob(&decData);
    return ret;
}
