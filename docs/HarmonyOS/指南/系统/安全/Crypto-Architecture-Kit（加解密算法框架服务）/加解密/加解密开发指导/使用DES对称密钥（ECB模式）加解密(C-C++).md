---
title: "使用DES对称密钥（ECB模式）加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-des-sym-encrypt-decrypt-ecb-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用DES对称密钥（ECB模式）加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.267Z"
---

# 使用DES对称密钥（ECB模式）加解密(C/C++)

对应的算法规格请查看[对称密钥加解密算法规格：DES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#des)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，生成密钥算法为DES、密钥长度为64位的对称密钥（OH\_CryptoSymKey）。

如何生成DES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：DES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#des)和[指定二进制数据转换对称密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key-ndk)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

**加密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'DES64|ECB|PKCS7'，创建对称密钥类型为DES64、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成加密操作。
    
2.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey），初始化加密Cipher实例。
    
    ECB模式无加密参数，params直接传入null。
    
3.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（明文）。
    
    -   当数据量较小时，可以在init完成后直接调用final。
    -   当数据量较大时，可以多次调用update，即分段加密。
4.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取加密后的数据。
    
    -   如果使用update接口传入数据，此处data传入null。如果使用final接口传入数据，此处data传入明文数据。
    -   final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**解密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'DES64|ECB|PKCS7'，创建对称密钥类型为DES64、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成解密操作。
    
2.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）初始化解密Cipher实例。ECB模式无加密参数，直接传入null。
    
3.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（密文）。
    
    -   当数据量较小时，可以在init完成后直接调用final。
    -   当数据量较大时，可以多次调用update，即分段解密。
    -   数据量大小可以使用者自行决定。比如大于20字节使用update。
4.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取解密后的数据。
    
    -   如果使用update接口传入数据，此处data传入null。如果使用final接口传入数据，此处data传入密文数据。
    -   final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_destroy)、[OH\_CryptoSymKey\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkey_destroy)、[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放申请的内存，销毁对象。

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_cipher.h"
#include <cstring>
#include "file.h"

OH\_Crypto\_ErrCode doTestDesEcb()
{
    OH\_CryptoSymKeyGenerator \*genCtx = nullptr;
    OH\_CryptoSymCipher \*encCtx = nullptr;
    OH\_CryptoSymCipher \*decCtx = nullptr;
    OH\_CryptoSymKey \*keyCtx = nullptr;
    char \*plainText = const\_cast<char \*>("this is test!");
    Crypto\_DataBlob input = {.data = (uint8\_t \*)(plainText), .len = strlen(plainText)};
    Crypto\_DataBlob encData = {.data = nullptr, .len = 0};
    Crypto\_DataBlob decData = {.data = nullptr, .len = 0};

    // 随机生成对称密钥。
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create("DES64", &genCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymKeyGenerator\_Generate(genCtx, &keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 加密操作。
    ret = OH\_CryptoSymCipher\_Create("DES64|ECB|PKCS7", &encCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(encCtx, CRYPTO\_ENCRYPT\_MODE, keyCtx, nullptr);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(encCtx, &input, &encData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 解密操作。
    ret = OH\_CryptoSymCipher\_Create("DES64|ECB|PKCS7", &decCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(decCtx, CRYPTO\_DECRYPT\_MODE, keyCtx, nullptr);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(decCtx, &encData, &decData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
end:
    OH\_CryptoSymCipher\_Destroy(encCtx);
    OH\_CryptoSymCipher\_Destroy(decCtx);
    OH\_CryptoSymKeyGenerator\_Destroy(genCtx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    OH\_Crypto\_FreeDataBlob(&encData);
    OH\_Crypto\_FreeDataBlob(&decData);
    return ret;
}
