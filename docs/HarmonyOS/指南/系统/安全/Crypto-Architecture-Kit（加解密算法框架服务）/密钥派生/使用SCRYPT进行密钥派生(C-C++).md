---
title: "使用SCRYPT进行密钥派生(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥派生"
  - "使用SCRYPT进行密钥派生(C/C++)"
captured_at: "2026-04-17T01:35:49.272Z"
---

# 使用SCRYPT进行密钥派生(C/C++)

对应的算法规格请查看[密钥派生算法规格：SCRYPT](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-overview#scrypt算法)。

#### 开发步骤

1.  调用[OH\_CryptoKdfParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_create)，指定字符串参数'SCRYPT'，创建密钥派生参数对象。
    
2.  调用[OH\_CryptoKdfParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_setparam)，设置Scrypt所需的参数。
    
    密钥派生失败原因：下列参数未设置。
    
    -   CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密码。
    -   CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
    -   CRYPTO\_KDF\_SCRYPT\_N\_UINT64：CPU/内存开销参数，必须是2的幂次方。
    -   CRYPTO\_KDF\_SCRYPT\_R\_UINT64：块大小参数，影响并行度。
    -   CRYPTO\_KDF\_SCRYPT\_P\_UINT64：并行化参数。
    -   CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64：最大内存限制（字节）。
3.  调用[OH\_CryptoKdf\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_create)，指定字符串参数'SCRYPT'，创建密钥派生函数对象。
    
4.  调用[OH\_CryptoKdf\_Derive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include "CryptoArchitectureKit/crypto\_kdf.h"
#include <cstdio>
#include <cstring>
#include "file.h"

static OH\_Crypto\_ErrCode doSetSaltAndPassword(OH\_CryptoKdfParams \*\*params)
{
    const char \*password = "123456";
    const char \*salt = "saltstring";
    Crypto\_DataBlob saltBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(salt)),
        .len = strlen(salt)
    };
    Crypto\_DataBlob passwordBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(password)),
        .len = strlen(password)
    };
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_KEY\_DATABLOB, &passwordBlob);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_SALT\_DATABLOB, &saltBlob);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    return CRYPTO\_SUCCESS;
}

// 设置参数函数
static OH\_Crypto\_ErrCode doScryptSetParams(OH\_CryptoKdfParams \*\*params)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_Create("SCRYPT", params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    uint64\_t n = 1024;  // CPU/内存开销参数。
    uint64\_t r = 8;     // 块大小参数。
    uint64\_t p = 16;    // 并行化参数。
    uint64\_t maxMem = 1067008;  // 最大内存限制（字节）。

    Crypto\_DataBlob nData = { .data = reinterpret\_cast<uint8\_t \*>(&n), .len = sizeof(uint64\_t) };
    Crypto\_DataBlob rData = { .data = reinterpret\_cast<uint8\_t \*>(&r), .len = sizeof(uint64\_t) };
    Crypto\_DataBlob pData = { .data = reinterpret\_cast<uint8\_t \*>(&p), .len = sizeof(uint64\_t) };
    Crypto\_DataBlob maxMemData = { .data = reinterpret\_cast<uint8\_t \*>(&maxMem), .len = sizeof(uint64\_t) };

    ret = doSetSaltAndPassword(params);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }

    ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_SCRYPT\_N\_UINT64, &nData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_SCRYPT\_R\_UINT64, &rData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_SCRYPT\_P\_UINT64, &pData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    ret = OH\_CryptoKdfParams\_SetParam(\*params, CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64, &maxMemData);
    if (ret != CRYPTO\_SUCCESS) {
        goto end;
    }
    return ret;

end:
    OH\_CryptoKdfParams\_Destroy(\*params);
    \*params = nullptr;
    return ret;
}

static OH\_Crypto\_ErrCode doScryptDerive(OH\_CryptoKdfParams \*params, uint32\_t keyLength, Crypto\_DataBlob \*out)
{
    // 创建密钥派生函数对象。
    OH\_CryptoKdf \*kdfCtx = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdf\_Create("SCRYPT", &kdfCtx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 派生密钥。
    ret = OH\_CryptoKdf\_Derive(kdfCtx, params, keyLength, out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdf\_Destroy(kdfCtx);
        return ret;
    }

    printf("Derived key length: %u\\n", out->len);

    OH\_CryptoKdf\_Destroy(kdfCtx);
    return ret;
}

OH\_Crypto\_ErrCode doTestScrypt()
{
    OH\_CryptoKdfParams \*params = nullptr;
    Crypto\_DataBlob out = {0};
    uint32\_t keyLength = 32; // 生成32字节的密钥。

    // 设置参数。
    OH\_Crypto\_ErrCode ret = doScryptSetParams(&params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 派生密钥。
    ret = doScryptDerive(params, keyLength, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // 清理资源。
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoKdfParams\_Destroy(params);
    return CRYPTO\_SUCCESS;
}
