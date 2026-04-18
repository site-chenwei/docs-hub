---
title: "消息摘要计算SHA256(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "消息摘要计算"
  - "消息摘要计算开发指导"
  - "消息摘要计算SHA256(C/C++)"
captured_at: "2026-04-17T01:35:49.009Z"
---

# 消息摘要计算SHA256(C/C++)

对应的算法规格请查看[消息摘要计算算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-overview#支持的算法与规格)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 开发步骤

在调用update接口传入数据时，可以[一次性传入所有数据](#摘要算法一次性传入)，也可以把数据人工分段，然后[分段update](#分段摘要算法)。对于同一段数据而言，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

#### \[h2\]摘要算法（一次性传入）

1.  调用[OH\_CryptoDigest\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_create)，指定摘要算法SHA256，生成摘要实例（OH\_CryptoDigest）。
    
2.  调用[OH\_CryptoDigest\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_update)，传入自定义消息，进行摘要更新计算。单次update长度没有限制。
    
3.  调用[OH\_CryptoDigest\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_final)，获取摘要计算结果。
    
4.  调用[OH\_CryptoDigest\_GetLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_getlength)，获取摘要计算长度，单位为字节。
    
5.  调用[OH\_DigestCrypto\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_digestcrypto_destroy)，销毁摘要实例（OH\_CryptoDigest）。
    

-   以下使用单次传入数据，获取摘要计算结果为例：
    
    #include "CryptoArchitectureKit/crypto\_common.h"
    #include "CryptoArchitectureKit/crypto\_digest.h"
    #include <cstring>
    
    OH\_Crypto\_ErrCode doTestSha256Md()
    {
        OH\_Crypto\_ErrCode ret;
        OH\_CryptoDigest \*ctx = nullptr;
        char \*testData = const\_cast<char \*>("0123456789");
        Crypto\_DataBlob in = {.data = (uint8\_t \*)(testData), .len = strlen(testData)};
        Crypto\_DataBlob out = {.data = nullptr, .len = 0};
        int mdLen = 0;
        ret = OH\_CryptoDigest\_Create("SHA256", &ctx);
        if (ret != CRYPTO\_SUCCESS) {
            return ret;
        }
        do {
            ret = OH\_CryptoDigest\_Update(ctx, &in);
            if (ret != CRYPTO\_SUCCESS) {
                break;
            }
            ret = OH\_CryptoDigest\_Final(ctx, &out);
            if (ret != CRYPTO\_SUCCESS) {
                break;
            }
            mdLen = OH\_CryptoDigest\_GetLength(ctx);
        } while (0);
        OH\_Crypto\_FreeDataBlob(&out);
        OH\_DigestCrypto\_Destroy(ctx);
        return ret;
    }
    

#### \[h2\]分段摘要算法

1.  调用[OH\_CryptoDigest\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_create)，指定摘要算法SHA256，生成摘要实例（OH\_CryptoDigest）。
    
2.  传入自定义消息，将一次传入数据量设置为20字节，多次调用[OH\_CryptoDigest\_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_update)，进行摘要更新计算。
    
3.  调用[OH\_CryptoDigest\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_final)，获取摘要计算结果。
    
4.  调用[OH\_CryptoDigest\_GetLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_getlength)，获取摘要计算长度，单位为字节。
    
5.  调用[OH\_DigestCrypto\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h#oh_digestcrypto_destroy)，销毁摘要实例（OH\_CryptoDigest）。
    

-   以下使用分段传入数据，获取摘要计算结果为例：
    
    #include <cstdlib>
    #include "CryptoArchitectureKit/crypto\_common.h"
    #include "CryptoArchitectureKit/crypto\_digest.h"
    #define OH\_CRYPTO\_DIGEST\_DATA\_MAX (1024 \* 1024 \* 100)
    
    static constexpr int INT\_640 = 640;
    
    OH\_Crypto\_ErrCode doLoopSha256Md()
    {
        OH\_Crypto\_ErrCode ret;
        OH\_CryptoDigest \*ctx = nullptr;
        uint8\_t \*testData = (uint8\_t \*)malloc(OH\_CRYPTO\_DIGEST\_DATA\_MAX);
        if (testData == nullptr) {
            return CRYPTO\_MEMORY\_ERROR;
        }
        Crypto\_DataBlob out = {.data = nullptr, .len = 0};
        int mdLen = 0;
        int isBlockSize = 20;
        int offset = 0;
    
        ret = OH\_CryptoDigest\_Create("SHA256", &ctx);
        if (ret != CRYPTO\_SUCCESS) {
            return ret;
        }
        do {
            for (int i = 0; i < INT\_640 / isBlockSize; i++) {
                Crypto\_DataBlob in = {
                    .data = reinterpret\_cast<uint8\_t \*>(testData + offset),
                    .len = static\_cast<size\_t>(isBlockSize)};
                ret = OH\_CryptoDigest\_Update(ctx, &in);
                if (ret != CRYPTO\_SUCCESS) {
                    break;
                }
                offset += isBlockSize;
            }
            ret = OH\_CryptoDigest\_Final(ctx, &out);
            if (ret != CRYPTO\_SUCCESS) {
                break;
            }
            mdLen = OH\_CryptoDigest\_GetLength(ctx);
        } while (0);
        OH\_Crypto\_FreeDataBlob(&out);
        OH\_DigestCrypto\_Destroy(ctx);
        return ret;
    }
