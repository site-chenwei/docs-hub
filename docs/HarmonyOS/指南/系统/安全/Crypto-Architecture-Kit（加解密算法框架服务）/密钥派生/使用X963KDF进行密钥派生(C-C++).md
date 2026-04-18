---
title: "使用X963KDF进行密钥派生(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥派生"
  - "使用X963KDF进行密钥派生(C/C++)"
captured_at: "2026-04-17T01:35:49.322Z"
---

# 使用X963KDF进行密钥派生(C/C++)

从API version 22开始，算法库支持使用该算法进行密钥派生操作。

对应算法规格请查看[密钥派生算法规格：X963KDF](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-overview#x963kdf算法)。

#### 开发步骤

1.  调用[OH\_CryptoKdfParams\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_create)，指定字符串参数'X963KDF'，创建密钥派生参数对象。
    
2.  调用[OH\_CryptoKdfParams\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_setparam)，设置X963KDF所需的参数。示例如下：
    
    -   CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密钥材料。
    -   CRYPTO\_KDF\_INFO\_DATABLOB：应用程序特定的信息（可选）。
3.  调用[OH\_CryptoKdf\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_create)，指定字符串参数'X963KDF|SHA256'，创建密钥派生函数对象。
    
4.  调用[OH\_CryptoKdf\_Derive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstdio>
#include <cstring>
#include "file.h"

OH\_Crypto\_ErrCode doTestX963Kdf()
{
    // 创建X963KDF参数对象。
    OH\_CryptoKdfParams \*params = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_Create("X963KDF", &params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 设置原始密钥材料。
    const char \*keyData = "012345678901234567890123456789";
    Crypto\_DataBlob key = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(keyData)),
        .len = strlen(keyData)
    };
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_KEY\_DATABLOB, &key);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // 设置应用程序特定信息。
    const char \*infoData = "infostring";
    Crypto\_DataBlob info = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(infoData)),
        .len = strlen(infoData)
    };
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_INFO\_DATABLOB, &info);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // 创建密钥派生函数对象。
    OH\_CryptoKdf \*kdfCtx = nullptr;
    ret = OH\_CryptoKdf\_Create("X963KDF|SHA256", &kdfCtx);
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
