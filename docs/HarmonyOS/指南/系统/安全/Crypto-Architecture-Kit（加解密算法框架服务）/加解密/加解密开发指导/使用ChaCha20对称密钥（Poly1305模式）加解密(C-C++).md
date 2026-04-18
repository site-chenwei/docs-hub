---
title: "使用ChaCha20对称密钥（Poly1305模式）加解密(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "加解密"
  - "加解密开发指导"
  - "使用ChaCha20对称密钥（Poly1305模式）加解密(C/C++)"
captured_at: "2026-04-17T01:35:48.388Z"
---

# 使用ChaCha20对称密钥（Poly1305模式）加解密(C/C++)

从API22开始，算法库支持该算法。

对应的算法规格请查看[对称密钥加解密算法规格：ChaCha20](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#chacha20)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，生成密钥算法为ChaCha20的对称密钥（OH\_CryptoSymKey）。

如何生成ChaCha20对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：ChaCha20](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#chacha20)和[随机生成对称密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk)理解。参考文档与示例可能存在入参差异，请注意区分。

**加密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成加密操作。
    
2.  调用[OH\_CryptoSymCipherParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
    
3.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和Poly1305模式对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
    
4.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（明文）。
    
5.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取加密后的数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/cWCzNL0ASMylq-DJv8DZ6Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013550Z&HW-CC-Expire=86400&HW-CC-Sign=30D33D92E2B3A6910615A41FA9F5DCEFF0E0F8CA503FD9978E748CAE59B95774)
    
    由于已使用update传入数据，此处data传入null。
    
    doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
    
6.  使用[OH\_CryptoSymCipherParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_create)创建Params，使用[OH\_CryptoSymCipherParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_setparam)设置authTag，作为解密的认证信息。在Poly1305模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。
    
7.  调用[OH\_CryptoSymKeyGenerator\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipherparams_destroy)销毁各对象。
    

**解密**

1.  调用[OH\_CryptoSymCipher\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_create)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成解密操作。
    
2.  调用[OH\_CryptoSymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和Poly1305模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
    
3.  调用[OH\_CryptoSymCipher\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_update)，更新数据（密文）。
    
4.  调用[OH\_CryptoSymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h#oh_cryptosymcipher_final)，获取解密后的数据。
    

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_cipher.h"
#include <cstring>
#include "file.h"

// 参数赋值函数
static OH\_Crypto\_ErrCode doChaCha20Poly1305SetParams(Crypto\_DataBlob \*ivData, Crypto\_DataBlob \*aadData,
    Crypto\_DataBlob \*tagData, OH\_CryptoSymCipherParams \*\*params)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymCipherParams\_Create(params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(\*params, CRYPTO\_IV\_DATABLOB, ivData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(\*params, CRYPTO\_AAD\_DATABLOB, aadData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipherParams\_SetParam(\*params, CRYPTO\_TAG\_DATABLOB, tagData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    return ret;

end:
    OH\_CryptoSymCipherParams\_Destroy(\*params);
    \*params = nullptr;
    return ret;
}

// 加密函数
static OH\_Crypto\_ErrCode doChaCha20Poly1305Encrypt(OH\_CryptoSymKey \*keyCtx, OH\_CryptoSymCipherParams \*params,
    Crypto\_DataBlob \*msgBlob, Crypto\_DataBlob \*outUpdate, Crypto\_DataBlob \*tagOutPut)
{
    OH\_CryptoSymCipher \*encCtx = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymCipher\_Create("ChaCha20|Poly1305", &encCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(encCtx, CRYPTO\_ENCRYPT\_MODE, keyCtx, params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Update(encCtx, msgBlob, outUpdate);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(encCtx, nullptr, tagOutPut);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

end:
    OH\_CryptoSymCipher\_Destroy(encCtx);
    return ret;
}

// 解密函数
static OH\_Crypto\_ErrCode doChaCha20Poly1305Decrypt(OH\_CryptoSymKey \*keyCtx, OH\_CryptoSymCipherParams \*params,
    Crypto\_DataBlob \*tagOutPut, Crypto\_DataBlob \*outUpdate, Crypto\_DataBlob \*decUpdate)
{
    OH\_CryptoSymCipher \*decCtx = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymCipherParams\_SetParam(params, CRYPTO\_TAG\_DATABLOB, tagOutPut);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoSymCipher\_Create("ChaCha20|Poly1305", &decCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Init(decCtx, CRYPTO\_DECRYPT\_MODE, keyCtx, params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymCipher\_Final(decCtx, outUpdate, decUpdate);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

end:
    OH\_CryptoSymCipher\_Destroy(decCtx);
    return ret;
}

OH\_Crypto\_ErrCode doTestChaCha20Poly1305()
{
    OH\_CryptoSymKeyGenerator \*genCtx = nullptr;
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoSymCipherParams \*params = nullptr;

    Crypto\_DataBlob outUpdate = {.data = nullptr, .len = 0};
    Crypto\_DataBlob decUpdate = {.data = nullptr, .len = 0};

    uint8\_t aad\[8\] = {1, 2, 3, 4, 5, 6, 7, 8};
    uint8\_t tag\[16\] = {0};
    uint8\_t iv\[12\] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4}; // iv使用安全随机数生成。
    Crypto\_DataBlob ivData = {.data = iv, .len = sizeof(iv)};
    Crypto\_DataBlob aadData = {.data = aad, .len = sizeof(aad)};
    Crypto\_DataBlob tagData = {.data = tag, .len = sizeof(tag)};
    Crypto\_DataBlob tagOutPut = {.data = nullptr, .len = 0};
    char \*plainText = const\_cast<char \*>("this is test!");
    Crypto\_DataBlob msgBlob = {.data = (uint8\_t \*)(plainText), .len = strlen(plainText)};
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create("ChaCha20", &genCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoSymKeyGenerator\_Generate(genCtx, &keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 参数赋值。
    ret = doChaCha20Poly1305SetParams(&ivData, &aadData, &tagData, &params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 加密。
    ret = doChaCha20Poly1305Encrypt(keyCtx, params, &msgBlob, &outUpdate, &tagOutPut);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 解密。
    ret = doChaCha20Poly1305Decrypt(keyCtx, params, &tagOutPut, &outUpdate, &decUpdate);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 释放资源。
end:
    OH\_CryptoSymCipherParams\_Destroy(params);
    OH\_CryptoSymKeyGenerator\_Destroy(genCtx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    OH\_Crypto\_FreeDataBlob(&outUpdate);
    OH\_Crypto\_FreeDataBlob(&decUpdate);
    OH\_Crypto\_FreeDataBlob(&tagOutPut);
    return ret;
}
