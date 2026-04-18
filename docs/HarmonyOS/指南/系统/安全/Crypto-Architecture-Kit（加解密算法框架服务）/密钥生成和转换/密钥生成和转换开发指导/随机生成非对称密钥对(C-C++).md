---
title: "随机生成非对称密钥对(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥生成和转换"
  - "密钥生成和转换开发指导"
  - "随机生成非对称密钥对(C/C++)"
captured_at: "2026-04-17T01:35:47.749Z"
---

# 随机生成非对称密钥对(C/C++)

以RSA和SM2为例，随机生成非对称密钥对（OH\_CryptoKeyPair），并获得二进制数据。

非对称密钥对可用于后续加解密等操作，二进制数据可用于存储或传输。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 随机生成RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#rsa)。

1.  调用[OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create)，指定字符串参数'RSA1024|PRIMES\_2'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。
    
2.  调用[OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate)，随机生成非对称密钥对象（OH\_CryptoKeyPair）。
    
3.  调用[OH\_CryptoPubKey\_Encode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptopubkey_encode)获取公钥密钥对象的二进制数据。
    

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_asym\_key.h"
#include "file.h"

OH\_Crypto\_ErrCode randomGenerateAsymKey()
{
    OH\_CryptoAsymKeyGenerator \*ctx = nullptr;
    OH\_CryptoKeyPair \*keyPair = nullptr;
    OH\_Crypto\_ErrCode ret;

    ret = OH\_CryptoAsymKeyGenerator\_Create("RSA1024|PRIMES\_2", &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
        return ret;
    }
    
    ret = OH\_CryptoAsymKeyGenerator\_Generate(ctx, &keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
        OH\_CryptoKeyPair\_Destroy(keyPair);
        return ret;
    }

    OH\_CryptoPubKey \*pubKey = OH\_CryptoKeyPair\_GetPubKey(keyPair);
    Crypto\_DataBlob retBlob = {.data = nullptr, .len = 0};
    ret = OH\_CryptoPubKey\_Encode(pubKey, CRYPTO\_PEM, "PKCS1", &retBlob);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
        OH\_CryptoKeyPair\_Destroy(keyPair);
        return ret;
    }

    OH\_Crypto\_FreeDataBlob(&retBlob);

    OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
    OH\_CryptoKeyPair\_Destroy(keyPair);
    return ret;
}

#### 随机生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#sm2)。

1.  调用[OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create)，指定字符串参数'SM2\_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。
    
2.  调用[OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate)，随机生成非对称密钥对象（OH\_CryptoKeyPair）。
    
3.  调用[OH\_CryptoPubKey\_Encode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptopubkey_encode)获取公钥密钥对象的二进制数据。
    

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_asym\_key.h"
#include "file.h"

OH\_Crypto\_ErrCode randomGenerateRSA()
{
    OH\_CryptoAsymKeyGenerator \*ctx = nullptr;
    OH\_CryptoKeyPair \*dupKeyPair = nullptr;
    OH\_Crypto\_ErrCode ret;

    ret = OH\_CryptoAsymKeyGenerator\_Create("SM2\_256", &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
        return ret;
    }

    ret = OH\_CryptoAsymKeyGenerator\_Generate(ctx, &dupKeyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
        OH\_CryptoKeyPair\_Destroy(dupKeyPair);
        return ret;
    }

    OH\_CryptoPubKey \*pubKey = OH\_CryptoKeyPair\_GetPubKey(dupKeyPair);
    Crypto\_DataBlob retBlob = { .data = nullptr, .len = 0 };
    ret = OH\_CryptoPubKey\_Encode(pubKey, CRYPTO\_DER, nullptr, &retBlob);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
        OH\_CryptoKeyPair\_Destroy(dupKeyPair);
        return ret;
    }

    OH\_CryptoAsymKeyGenerator\_Destroy(ctx);
    OH\_CryptoKeyPair\_Destroy(dupKeyPair);
    return ret;
}
