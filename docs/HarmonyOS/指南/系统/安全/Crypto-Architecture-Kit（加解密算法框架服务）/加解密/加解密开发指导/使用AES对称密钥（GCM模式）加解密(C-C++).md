---
title: "使用AES对称密钥（GCM模式）加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用AES对称密钥（GCM模式）加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.012Z"
---

# 使用AES对称密钥（GCM模式）加解密(C/C++)

对应的算法规格请查看[对称密钥加解密算法规格：AES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#aes)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

生成AES对称密钥，参考以下示例，并结合[对称密钥生成和转换规格：AES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#aes)和[随机生成对称密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk)理解。注意，参考文档与示例可能有入参差异

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM|PKCS7'，创建对称密钥类型为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。
    
2.  调用[OH\_CryptoSymCipherParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
    
3.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定对称密钥（OH\_CryptoSymKey）和GCM模式对应的加密参数（OH\_CryptoSymCipherParams），以初始化加密Cipher实例。
    
4.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（明文）。
    
    当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
    
    -   当数据量较小时，可以在init完成后直接调用final。
    -   当数据量较大时，可以多次调用update，即[分段加解密](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment-ndk)。
5.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取加密后的数据。
    
    -   由于已使用update传入数据，此处data传入null。
    -   final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/qc3sPELhRsmOltGuXPGs8A/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=31ED634426FC2C79870B78E0CEB9EBE01450EFC12CF023B7D03E330CD11B6975)
    
    在GCM模式下，final会返回authTag，作为解密时初始化的认证信息，需要保存。GCM模式下，算法库当前只支持16字节的authTag。示例中authTag为16字节。
    

**解密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM|PKCS7'，创建对称密钥类型为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成解密操作。
    
2.  使用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置authTag，作为解密的认证信息。
    
3.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和GCM模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
    
4.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（密文）。
    
5.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取解密数据。
    

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_destroy)销毁对象。

-   AES GCM模式加解密示例如下：

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_cipher.h"
#include <cstring>
#include "file.h"

OH\_Crypto\_ErrCode doTestAesGcm()
{
    OH\_CryptoSymKeyGenerator \*genCtx = nullptr;
    OH\_CryptoSymCipher \*encCtx = nullptr;
    OH\_CryptoSymCipher \*decCtx = nullptr;
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoSymCipherParams \*params = nullptr;

    Crypto\_DataBlob outUpdate = {.data = nullptr, .len = 0};
    Crypto\_DataBlob decUpdate = {.data = nullptr, .len = 0};

    uint8\_t aad\[8\] = {1, 2, 3, 4, 5, 6, 7, 8};
    uint8\_t tag\[16\] = {0};
    uint8\_t iv\[12\] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4}; // iv使用安全随机数生成
    Crypto\_DataBlob ivData = {.data = iv, .len = sizeof(iv)};
    Crypto\_DataBlob aadData = {.data = aad, .len = sizeof(aad)};
    Crypto\_DataBlob tagData = {.data = tag, .len = sizeof(tag)};
    Crypto\_DataBlob tagOutPut = {.data = nullptr, .len = 0};
    char \*plainText = const\_cast<char \*>("this is test!");
    Crypto\_DataBlob msgBlob = {.data = (uint8\_t \*)(plainText), .len = strlen(plainText)};

    // 生成对称密钥
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create("AES128", &genCtx);
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
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_IV\_DATABLOB, &ivData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_AAD\_DATABLOB, &aadData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_TAG\_DATABLOB, &tagData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 加密
    ret = OH\_CryptoSymCipher\_Create("AES128|GCM|PKCS7", &encCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(encCtx, CRYPTO\_ENCRYPT\_MODE, keyCtx, params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Update(encCtx, &msgBlob, &outUpdate);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(encCtx, nullptr, &tagOutPut);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 解密
    ret = OH\_CryptoSymCipher\_Create("AES128|GCM|PKCS7", &decCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_TAG\_DATABLOB, &tagOutPut);
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

end:
    OH\_CryptoSymCipherParams\_Destroy(params);
    OH\_CryptoSymCipher\_Destroy(encCtx);
    OH\_CryptoSymCipher\_Destroy(decCtx);
    OH\_CryptoSymKeyGenerator\_Destroy(genCtx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    OH\_Crypto\_FreeDataBlob(&outUpdate);
    OH\_Crypto\_FreeDataBlob(&decUpdate);
    OH\_Crypto\_FreeDataBlob(&tagOutPut);
    return ret;
}
