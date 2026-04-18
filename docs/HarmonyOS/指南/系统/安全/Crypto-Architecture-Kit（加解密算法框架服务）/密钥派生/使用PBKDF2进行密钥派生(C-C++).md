---
title: "使用PBKDF2进行密钥派生(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥派生"
  - "使用PBKDF2进行密钥派生(C/C++)"
captured_at: "2026-04-17T01:35:49.226Z"
---

# 使用PBKDF2进行密钥派生(C/C++)

对应的算法规格请查看[密钥派生算法规格：PBKDF2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-overview#pbkdf2算法)。

#### 开发步骤

1.  调用[OH\_CryptoKdfParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_create)，指定字符串参数'PBKDF2'，创建密钥派生参数对象。
    
2.  调用[OH\_CryptoKdfParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_setparam)，设置PBKDF2所需的参数。示例如下：
    
    -   CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密码。
    -   CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
    -   CRYPTO\_KDF\_ITER\_COUNT\_INT：重复运算的次数，需要为正整数。
3.  调用[OH\_CryptoKdf\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_create)，指定字符串参数'PBKDF2|SHA256'，创建密钥派生函数对象。
    
4.  调用[OH\_CryptoKdf\_Derive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstdio>
#include <cstring>
#include "file.h"

static OH\_Crypto\_ErrCode setParams(OH\_CryptoKdfParams \*\*params)
{
    // 设置密码。
    const char \*password = "123456";
    Crypto\_DataBlob passwordBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(password)),
        .len = strlen(password)
    };
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_KEY\_DATABLOB, &passwordBlob);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 设置盐值。
    const char \*salt = "saltstring";
    Crypto\_DataBlob saltBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(salt)),
        .len = strlen(salt)
    };
    ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_SALT\_DATABLOB, &saltBlob);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    // 设置迭代次数。
    int iterations = 10000;
    Crypto\_DataBlob iterationsBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(&iterations),
        .len = sizeof(int)
    };
    ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_ITER\_COUNT\_INT, &iterationsBlob);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
end:
    OH\_CryptoKdfParams\_Destroy(\*params);
    \*params = nullptr;
    return ret;
}

OH\_Crypto\_ErrCode doTestPbkdf2()
{
    // 创建PBKDF2参数对象。
    OH\_CryptoKdfParams \*params = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_Create("PBKDF2", &params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = setParams(&params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 创建密钥派生函数对象。
    OH\_CryptoKdf \*kdfCtx = nullptr;
    ret = OH\_CryptoKdf\_Create("PBKDF2|SHA256", &kdfCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // 派生密钥。
    Crypto\_DataBlob out = {0};
    uint32\_t keyLength = 32; // 生成32字节的密钥。
    ret = OH\_CryptoKdf\_Derive(kdfCtx, params, keyLength, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdf\_Destroy(kdfCtx);
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    printf("Derived key length: %u\\n", out.len);

    // 清理资源。
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoKdf\_Destroy(kdfCtx);
    OH\_CryptoKdfParams\_Destroy(params);
    return CRYPTO\_SUCCESS;
}
