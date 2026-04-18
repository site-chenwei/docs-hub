---
title: "使用AES对称密钥（GCM模式）分段加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用AES对称密钥（GCM模式）分段加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.094Z"
---

# 使用AES对称密钥（GCM模式）分段加解密(C/C++)

对应的算法规格请查看[对称密钥加解密算法规格：AES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#aes)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

如何生成AES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：AES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#aes)和[随机生成对称密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk)文档进行理解。参考文档与当前示例可能存在入参差异，请注意区分。

**加密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM|PKCS7'，创建对称密钥算法为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。
    
2.  调用[OH\_CryptoSymCipherParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
    
3.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定对称密钥（OH\_CryptoSymKey）和GCM模式的加密参数（OH\_CryptoSymCipherParams），以初始化加密 Cipher 实例。
    
4.  将一次传入数据量设置为20字节，多次调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（明文）。
    
    -   当前单次update没有长度限制，开发者可根据数据量判断如何调用update。
        
    -   建议开发者对每次update的结果都判断是否为null，并在结果不为null时取出其中的密文进行拼接，形成完整的密文。因为在不同的规格下，update的结果可能会受到不同影响。
        
        1）例如ECB和CBC模式，始终以分组为基本单位进行加密，并输出本次更新产生的加密分组结果。即当本次更新操作凑满一个分组时，输出密文；若未凑满，则本次更新输出null，将未加密的数据与下次输入的数据拼接后，再进行分组输出。最后进行doFinal操作时，将未加密的数据根据指定的填充模式进行填充，再输出剩余加密结果。解密过程中的update操作同理。
        
        2）对于流加密模式（比如CTR和OFB模式），通常密文长度和明文长度相等。
        
5.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取密文。
    
    -   由于已使用update传入数据，此处传入null。
    -   final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，以避免产生异常。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/7RnYsdCwTECyTG8kksK9TQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=D08904BDB7CEA1E2A47CF248238930410718718078145E1FE3EA6A6B762D52E4)
        
        在GCM模式下，final会返回authTag，作为解密操作时初始化的认证信息，需要保存。
        
        在GCM模式下，算法库当前只支持16字节的authTag，作为解密操作时初始化的认证信息。示例中authTag恰好为16字节。
        

**解密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定参数'AES128|GCM|PKCS7'，创建对称密钥类型为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，完成解密操作。
    
2.  调用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置authTag作为解密的认证信息。
    
    在GCM模式下，从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。示例中authTag恰好为16字节。
    
3.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和GCM模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
    
4.  将一次传入数据量设置为20字节，多次调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（密文）。
    
5.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)获取解密数据。
    

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_destroy)和[OH\_CryptoSymCipherParams\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_destroy)销毁各对象。

#include <cstring>
#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_cipher.h"
#include "file.h"

#define OH\_CRYPTO\_GCM\_TAG\_LEN 16
#define OH\_CRYPTO\_MAX\_TEST\_DATA\_LEN 128
OH\_Crypto\_ErrCode doTestAesGcmSeg()
{
    OH\_CryptoSymKeyGenerator \*genCtx = nullptr;
    OH\_CryptoSymCipher \*encCtx = nullptr;
    OH\_CryptoSymCipher \*decCtx = nullptr;
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoSymCipherParams \*params = nullptr;

    char \*plainText = const\_cast<char \*>("aaaaa.....bbbbb.....ccccc.....ddddd.....eee");
    Crypto\_DataBlob msgBlob = {.data = (uint8\_t \*)(plainText), .len = strlen(plainText)};

    uint8\_t aad\[8\] = {1, 2, 3, 4, 5, 6, 7, 8};
    uint8\_t tagArr\[16\] = {0};
    uint8\_t iv\[12\] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4}; // iv使用安全随机数生成
    Crypto\_DataBlob tag = {.data = nullptr, .len = 0};
    Crypto\_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
    Crypto\_DataBlob aadBlob = {.data = aad, .len = sizeof(aad)};
    Crypto\_DataBlob outUpdate = {.data = nullptr, .len = 0};
    Crypto\_DataBlob decUpdate = {.data = nullptr, .len = 0};
    Crypto\_DataBlob tagInit = {.data = tagArr, .len = sizeof(tagArr)};
    int32\_t cipherLen = 0;
    int blockSize = 20;
    int32\_t randomLen = strlen(plainText);
    int cnt = randomLen / blockSize;
    int rem = randomLen % blockSize;
    uint8\_t cipherText\[OH\_CRYPTO\_MAX\_TEST\_DATA\_LEN\] = {0};
    Crypto\_DataBlob cipherBlob;
    
    // 生成密钥
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
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_IV\_DATABLOB, &ivBlob);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_AAD\_DATABLOB, &aadBlob);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_TAG\_DATABLOB, &tagInit);
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
    
    for (int i = 0; i < cnt; i++) {
        msgBlob.len = blockSize;
        ret = OH\_CryptoSymCipher\_Update(encCtx, &msgBlob, &outUpdate);
        if (ret != CRYPTO\_SUCCESS) {
            goto end;
        }
        msgBlob.data += blockSize;
        memcpy(&cipherText\[cipherLen\], outUpdate.data, outUpdate.len);
        cipherLen += outUpdate.len;
        OH\_Crypto\_FreeDataBlob(&outUpdate);
    }
    if (rem > 0) {
        msgBlob.len = rem;
        ret = OH\_CryptoSymCipher\_Update(encCtx, (Crypto\_DataBlob \*)&msgBlob, &outUpdate);
        if (ret != CRYPTO\_SUCCESS) {
            goto end;
        }
        memcpy(&cipherText\[cipherLen\], outUpdate.data, outUpdate.len);
        cipherLen += outUpdate.len;
        OH\_Crypto\_FreeDataBlob(&outUpdate);
    }
    ret = OH\_CryptoSymCipher\_Final(encCtx, nullptr, &tag);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 解密
    cipherBlob = {.data = reinterpret\_cast<uint8\_t \*>(cipherText), .len = (size\_t)cipherLen};
    msgBlob.data -= strlen(plainText) - rem;
    msgBlob.len = strlen(plainText);
    ret = OH\_CryptoSymCipher\_Create("AES128|GCM|PKCS7", &decCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_TAG\_DATABLOB, &tag);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(decCtx, CRYPTO\_DECRYPT\_MODE, keyCtx, params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(decCtx, &cipherBlob, &decUpdate);
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
    OH\_Crypto\_FreeDataBlob(&tag);
    OH\_Crypto\_FreeDataBlob(&decUpdate);
    return ret;
}
