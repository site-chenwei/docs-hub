---
title: "消息认证码计算HMAC(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "消息认证码"
  - "消息认证码计算HMAC(C/C++)"
captured_at: "2026-04-17T01:35:49.116Z"
---

# 消息认证码计算HMAC(C/C++)

HMAC通过指定摘要算法，以通信双方共享密钥与消息作为输入，生成消息认证码用于检验传递报文的完整性。HMAC在消息摘要算法的基础上增加了密钥的输入，确保了信息的正确性。生成的消息认证码为固定长度。

#### 开发步骤

在调用update接口传入数据时，可以[一次性传入](#hmac一次性传入)，也可以把数据人工[分段传入](#hmac分段传入)。对于同一段数据而言，是否分段，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

#### \[h2\]HMAC（一次性传入）

1.  调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)生成密钥算法为HMAC的对称密钥（symKey）。
    
2.  调用[OH\_CryptoMac\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_create)，指定字符串参数'HMAC'，创建MAC算法为HMAC的MAC生成器。
    
3.  调用[OH\_CryptoMac\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_setparam)，指定参数CRYPTO\_MAC\_DIGEST\_NAME\_STR，设置摘要算法名称。
    
4.  调用[OH\_CryptoMac\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_init)，指定共享对称密钥（symKey），初始化MAC对象。
    
5.  调用[OH\_CryptoMac\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_update)，传入自定义消息，进行消息认证码计算。
    
6.  调用[OH\_CryptoMac\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_final)，获取MAC计算结果。
    
7.  调用[OH\_CryptoMac\_GetLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_getlength)，获取MAC消息认证码的长度，单位为字节。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstdio>
#include <cstring>

static OH\_CryptoSymKey \*GenerateHmacKey(const char \*algoName)
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

static OH\_Crypto\_ErrCode CreateHmacContext(OH\_CryptoSymKey \*keyCtx, OH\_CryptoMac \*\*ctx)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Create("HMAC", ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 设置摘要算法名称为SM3。
    const char \*digestName = "SM3";
    Crypto\_DataBlob digestNameData = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(digestName)),
        .len = strlen(digestName)
    };
    ret = OH\_CryptoMac\_SetParam(\*ctx, CRYPTO\_MAC\_DIGEST\_NAME\_STR, &digestNameData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    // 初始化HMAC计算。
    ret = OH\_CryptoMac\_Init(\*ctx, keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode UpdateHmacData(OH\_CryptoMac \*ctx)
{
    // 一次性传入所有数据。
    const char \*message = "hmacTestMessage";
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

static OH\_Crypto\_ErrCode FinalizeHmac(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out, uint32\_t \*macLen)
{
    // 完成HMAC计算并获取结果。
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Final(ctx, out);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 获取HMAC值的长度。
    ret = OH\_CryptoMac\_GetLength(ctx, macLen);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(out);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

OH\_Crypto\_ErrCode doTestHmacOnce()
{
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoMac \*ctx = nullptr;
    Crypto\_DataBlob out = {0};
    OH\_Crypto\_ErrCode ret = CRYPTO\_SUCCESS;
    uint32\_t macLen = 0;

    // 生成HMAC密钥，使用SM3作为摘要算法。
    keyCtx = GenerateHmacKey("HMAC|SM3");
    if (keyCtx == nullptr) {
        ret = CRYPTO\_OPERTION\_ERROR;
        goto cleanup;
    }

    // 创建HMAC上下文。
    ret = CreateHmacContext(keyCtx, &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 一次性传入所有数据。
    ret = UpdateHmacData(ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 完成HMAC计算。
    ret = FinalizeHmac(ctx, &out, &macLen);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    printf("HMAC calculation success, length: %u\\n", macLen);

cleanup:
    // 清理资源。
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoMac\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    return ret;
}

#### \[h2\]HMAC（分段传入）

与一次性传入的步骤基本相同，区别在于多次调用[OH\_CryptoMac\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_update)来处理分段数据。

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstdio>
#include <cstring>

static OH\_CryptoSymKey \*GenerateHmacKey(const char \*algoName)
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

static OH\_Crypto\_ErrCode CreateHmacContext(OH\_CryptoSymKey \*keyCtx, OH\_CryptoMac \*\*ctx)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Create("HMAC", ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 设置摘要算法名称为SM3。
    const char \*digestName = "SM3";
    Crypto\_DataBlob digestNameData = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(digestName)),
        .len = strlen(digestName)
    };
    ret = OH\_CryptoMac\_SetParam(\*ctx, CRYPTO\_MAC\_DIGEST\_NAME\_STR, &digestNameData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    // 初始化HMAC计算。
    ret = OH\_CryptoMac\_Init(\*ctx, keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(\*ctx);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode ProcessHmacSegments(OH\_CryptoMac \*ctx)
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

static OH\_Crypto\_ErrCode FinalizeHmac(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out, uint32\_t \*macLen)
{
    // 完成HMAC计算并获取结果。
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Final(ctx, out);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 获取HMAC值的长度。
    ret = OH\_CryptoMac\_GetLength(ctx, macLen);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(out);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

OH\_Crypto\_ErrCode doTestHmacBySegments()
{
    OH\_CryptoSymKey \*keyCtx = nullptr;
    OH\_CryptoMac \*ctx = nullptr;
    Crypto\_DataBlob out = {0};
    OH\_Crypto\_ErrCode ret = CRYPTO\_SUCCESS;
    uint32\_t macLen = 0;

    // 生成HMAC密钥，使用SM3作为摘要算法。
    keyCtx = GenerateHmacKey("HMAC|SM3");
    if (keyCtx == nullptr) {
        ret = CRYPTO\_OPERTION\_ERROR;
        goto cleanup;
    }

    // 创建HMAC上下文。
    ret = CreateHmacContext(keyCtx, &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 分段处理数据。
    ret = ProcessHmacSegments(ctx);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    // 完成HMAC计算。
    ret = FinalizeHmac(ctx, &out, &macLen);
    if (ret != CRYPTO\_SUCCESS) {
        goto cleanup;
    }

    printf("HMAC calculation success, length: %u\\n", macLen);

cleanup:
    // 清理资源。
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoMac\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    return ret;
}
