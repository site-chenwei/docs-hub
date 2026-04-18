---
title: "消息认证码计算CMAC(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-cmac-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "消息认证码"
  - "消息认证码计算CMAC(C/C++)"
captured_at: "2026-04-17T01:35:49.138Z"
---

# 消息认证码计算CMAC(C/C++)

CMAC通过使用分组密码（如AES）和一个密钥来生成认证码，确保消息在传输过程中未被篡改。

#### 开发步骤

在调用update接口传入数据时，可以[一次性传入](#cmac一次性传入)，也可以把数据人工[分段传入](#cmac分段传入)。对于同一段数据而言，是否分段，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

#### \[h2\]CMAC（一次性传入）

1.  调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)生成密钥算法为AES128的对称密钥（symKey）。
    
2.  调用[OH\_CryptoMac\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_create)，指定字符串参数'CMAC'，创建MAC算法为CMAC的MAC生成器。
    
3.  调用[OH\_CryptoMac\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_setparam)，指定参数CRYPTO\_MAC\_CIPHER\_NAME\_STR，设置分组密码算法名称。
    
4.  调用[OH\_CryptoMac\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_init)，指定共享对称密钥（symKey），初始化MAC对象。
    
5.  调用[OH\_CryptoMac\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_update)，传入自定义消息，进行消息认证码计算。
    
6.  调用[OH\_CryptoMac\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_final)，获取MAC计算结果。
    
7.  调用[OH\_CryptoMac\_GetLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_getlength)，获取MAC消息认证码的长度，单位为字节。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstdio>
#include <cstring>

static OH\_CryptoSymKey \*GenerateAesKey(const char \*algoName)
{
    OH\_CryptoSymKeyGenerator \*keyGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create(algoName, &keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    OH\_CryptoSymKey \*keyCtx = nullptr;
    ret = OH\_CryptoSymKeyGenerator\_Generate(keyGen, &keyCtx);
    OH\_CryptoSymKeyGenerator\_Destroy(keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    return keyCtx;
}

static OH\_Crypto\_ErrCode CreateCmacContext(OH\_CryptoSymKey \*keyCtx, OH\_CryptoMac \*\*ctx)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Create("CMAC", ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 设置分组密码算法名称为AES128。
    const char \*cipherName = "AES128";
    Crypto\_DataBlob cipherNameData = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(cipherName)),
        .len = strlen(cipherName)
    };
    ret = OH\_CryptoMac\_SetParam(\*ctx, CRYPTO\_MAC\_CIPHER\_NAME\_STR, &cipherNameData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    // 初始化CMAC计算。
    ret = OH\_CryptoMac\_Init(\*ctx, keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode UpdateCmacData(OH\_CryptoMac \*ctx)
{
    // 一次性传入所有数据。
    const char \*message = "cmacTestMessage";
    Crypto\_DataBlob input = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(message)),
        .len = strlen(message)
    };
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Update(ctx, &input);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode FinalizeCmac(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out, uint32\_t \*macLen)
{
    // 完成CMAC计算并获取结果。
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Final(ctx, out);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 获取CMAC值的长度。
    ret = OH\_CryptoMac\_GetLength(ctx, macLen);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(out);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

OH\_Crypto\_ErrCode doTestCmacOnce()
{
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoMac \*ctx = nullptr;
    Crypto\_DataBlob out = {0};
    OH\_Crypto\_ErrCode ret = CRYPTO\_SUCCESS;
    uint32\_t macLen = 0;

    // 生成AES128密钥。
    keyCtx = GenerateAesKey("AES128");
    if (keyCtx == nullptr) {
        ret = CRYPTO\_OPERTION\_ERROR;
        goto cleanup;
    }

    // 创建CMAC上下文。
    ret = CreateCmacContext(keyCtx, &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 一次性传入所有数据。
    ret = UpdateCmacData(ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 完成CMAC计算。
    ret = FinalizeCmac(ctx, &out, &macLen);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    printf("CMAC calculation success, length: %u\\n", macLen);

cleanup:
    // 清理资源。
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoMac\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    return ret;
}

#### \[h2\]CMAC（分段传入）

与一次性传入的步骤基本相同，区别在于多次调用[OH\_CryptoMac\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_update)来处理分段数据。

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstdio>
#include <cstring>

static OH\_CryptoSymKey \*GenerateAesKey(const char \*algoName)
{
    OH\_CryptoSymKeyGenerator \*keyGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create(algoName, &keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    OH\_CryptoSymKey \*keyCtx = nullptr;
    ret = OH\_CryptoSymKeyGenerator\_Generate(keyGen, &keyCtx);
    OH\_CryptoSymKeyGenerator\_Destroy(keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    return keyCtx;
}

static OH\_Crypto\_ErrCode CreateCmacContext(OH\_CryptoSymKey \*keyCtx, OH\_CryptoMac \*\*ctx)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Create("CMAC", ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 设置分组密码算法名称为AES128。
    const char \*cipherName = "AES128";
    Crypto\_DataBlob cipherNameData = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(cipherName)),
        .len = strlen(cipherName)
    };
    ret = OH\_CryptoMac\_SetParam(\*ctx, CRYPTO\_MAC\_CIPHER\_NAME\_STR, &cipherNameData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    // 初始化CMAC计算。
    ret = OH\_CryptoMac\_Init(\*ctx, keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode ProcessCmacSegments(OH\_CryptoMac \*ctx)
{
    // 分段传入数据。
    const char \*message = "aaaaa.....bbbbb.....ccccc.....ddddd.....eee";
    size\_t messageLen = strlen(message);
    size\_t segmentSize = 20; // 每段20字节。

    for (size\_t i = 0; i < messageLen; i += segmentSize) {
        size\_t currentSize = (i + segmentSize <= messageLen) ? segmentSize : (messageLen - i);
        Crypto\_DataBlob segment = {
            .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(message + i)),
            .len = currentSize
        };
        OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Update(ctx, &segment);
        if (ret != CRYPTO\_SUCCESS) {
            return ret;
        }
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode FinalizeCmac(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out, uint32\_t \*macLen)
{
    // 完成CMAC计算并获取结果。
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Final(ctx, out);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 获取CMAC值的长度。
    ret = OH\_CryptoMac\_GetLength(ctx, macLen);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(out);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

OH\_Crypto\_ErrCode doTestCmacBySegments()
{
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoMac \*ctx = nullptr;
    Crypto\_DataBlob out = {0};
    OH\_Crypto\_ErrCode ret = CRYPTO\_SUCCESS;
    uint32\_t macLen = 0;

    // 生成AES128密钥。
    keyCtx = GenerateAesKey("AES128");
    if (keyCtx == nullptr) {
        ret = CRYPTO\_OPERTION\_ERROR;
        goto cleanup;
    }

    // 创建CMAC上下文。
    ret = CreateCmacContext(keyCtx, &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 分段处理数据。
    ret = ProcessCmacSegments(ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 完成CMAC计算。
    ret = FinalizeCmac(ctx, &out, &macLen);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    printf("CMAC calculation success, length: %u\\n", macLen);

cleanup:
    // 清理资源。
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoMac\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    return ret;
}
