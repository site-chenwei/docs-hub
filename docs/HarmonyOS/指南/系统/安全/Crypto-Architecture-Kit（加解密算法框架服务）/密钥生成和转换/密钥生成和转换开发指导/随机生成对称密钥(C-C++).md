---
title: "随机生成对称密钥(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥生成和转换"
  - "密钥生成和转换开发指导"
  - "随机生成对称密钥(C/C++)"
captured_at: "2026-04-17T01:35:47.663Z"
---

# 随机生成对称密钥(C/C++)

以AES和SM4为例，随机生成对称密钥（OH\_CryptoSymKey）。

对称密钥对象可用于后续加解密操作，二进制数据可用于存储或传输。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 随机生成AES密钥

对应的算法规格请查看[对称密钥生成和转换规格：AES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#aes)。

1.  调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)，指定字符串参数'AES256'，创建密钥算法为AES、密钥长度为256位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
    
2.  调用[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，随机生成对称密钥对象（OH\_CryptoSymKey）。
    
3.  调用[OH\_CryptoSymKey\_GetKeyData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。
    

```
#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_sym_key.h"
#include "file.h"

OH_Crypto_ErrCode testGenerateSymKey()
{
    OH_CryptoSymKeyGenerator *ctx = nullptr;
    OH_CryptoSymKey *keyCtx = nullptr;
    Crypto_DataBlob out = {.data = nullptr, .len = 0};
    OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES256", &ctx);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoSymKeyGenerator_Generate(ctx, &keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymKeyGenerator_Destroy(ctx);
        return ret;
    }
    ret = OH_CryptoSymKey_GetKeyData(keyCtx, &out);
    OH_CryptoSymKeyGenerator_Destroy(ctx);
    OH_CryptoSymKey_Destroy(keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    OH_Crypto_FreeDataBlob(&out);
    return ret;
}
```

#### 随机生成SM4密钥

对应的算法规格请查看[对称密钥生成和转换规格：SM4](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#sm4)。

1.  调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)，指定字符串参数'SM4\_128'，创建密钥算法为SM4、密钥长度为128位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
    
2.  调用[OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate)，随机生成对称密钥对象（OH\_CryptoSymKey）。
    
3.  调用[OH\_CryptoSymKey\_GetKeyData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。
    

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_key.h"
#include "file.h"

OH\_Crypto\_ErrCode testGenerateSM4Key()
{
    OH\_CryptoSymKeyGenerator \*ctx = nullptr;
    OH\_CryptoSymKey \*keyCtx = nullptr;
    Crypto\_DataBlob out = {.data = nullptr, .len = 0};
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create("SM4\_128", &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoSymKeyGenerator\_Generate(ctx, &keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoSymKeyGenerator\_Destroy(ctx);
        return ret;
    }
    ret = OH\_CryptoSymKey\_GetKeyData(keyCtx, &out);
    OH\_CryptoSymKeyGenerator\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    OH\_Crypto\_FreeDataBlob(&out);
    return ret;
}
