---
title: "使用SM4对称密钥（CBC模式）加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-cbc-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用SM4对称密钥（CBC模式）加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.255Z"
---

# 使用SM4对称密钥（CBC模式）加解密(C/C++)

对应的算法规格请查看[对称密钥加解密算法规格：SM4](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#sm4)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

**加密**

1.  调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，生成密钥算法为SM4、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。
    
    如何生成SM4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：SM4](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#sm4)和[随机生成对称密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
    
2.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|CBC|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于完成加密操作。
    
3.  调用[OH\_CryptoSymCipherParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
    
4.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和CBC模式对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
    
5.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（明文）。
    
    -   当数据量较小时，可以在init完成后直接调用final。
    -   当数据量较大时，可以多次调用update，即分段加解密。
6.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取加密后的数据。
    
    -   由于已使用update传入数据，此处data传入null。
    -   final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
7.  调用[OH\_CryptoSymKeyGenerator\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_destroy)销毁各对象。
    

**解密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|CBC|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于完成解密操作。
    
2.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和CBC模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
    
3.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（密文）。
    
4.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取解密后的数据。
    

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_cipher.h"
#include <cstring>
// ...

OH\_Crypto\_ErrCode doTestSm4Cbc()
{
    OH\_CryptoSymKeyGenerator \*genCtx = nullptr;
    OH\_CryptoSymCipher \*encCtx = nullptr;
    OH\_CryptoSymCipher \*decCtx = nullptr;
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoSymCipherParams \*params = nullptr;
    Crypto\_DataBlob outUpdate = {.data = nullptr, .len = 0};
    Crypto\_DataBlob decUpdate = {.data = nullptr, .len = 0};

    char \*plainText = const\_cast<char \*>("this is test!");
    Crypto\_DataBlob msgBlob = {.data = (uint8\_t \*)(plainText), .len = strlen(plainText)};
    uint8\_t iv\[16\] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4, 3, 1, 0, 10}; // iv使用安全随机数生成
    Crypto\_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
    // 生成对称密钥
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create("SM4\_128", &genCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymKeyGenerator\_Generate(genCtx, &keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 设置参数
    ret = OH\_CryptoSymCipherParams\_Create(&params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_IV\_DATABLOB, &ivBlob);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 加密
    ret = OH\_CryptoSymCipher\_Create("SM4\_128|CBC|PKCS7", &encCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(encCtx, CRYPTO\_ENCRYPT\_MODE, keyCtx, params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(encCtx, &msgBlob, &outUpdate);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 解密
    ret = OH\_CryptoSymCipher\_Create("SM4\_128|CBC|PKCS7", &decCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(decCtx, CRYPTO\_DECRYPT\_MODE, keyCtx, params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(decCtx, &outUpdate, &decUpdate);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 资源释放
end:
    OH\_CryptoSymCipherParams\_Destroy(params);
    OH\_CryptoSymCipher\_Destroy(encCtx);
    OH\_CryptoSymCipher\_Destroy(decCtx);
    OH\_CryptoSymKeyGenerator\_Destroy(genCtx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    OH\_Crypto\_FreeDataBlob(&outUpdate);
    OH\_Crypto\_FreeDataBlob(&decUpdate);
    return ret;
}
