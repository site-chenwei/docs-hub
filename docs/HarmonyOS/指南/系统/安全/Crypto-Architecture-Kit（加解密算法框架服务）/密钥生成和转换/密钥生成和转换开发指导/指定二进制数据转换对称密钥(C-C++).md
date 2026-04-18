---
title: "指定二进制数据转换对称密钥(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥生成和转换"
  - "密钥生成和转换开发指导"
  - "指定二进制数据转换对称密钥(C/C++)"
captured_at: "2026-04-17T01:35:47.716Z"
---

# 指定二进制数据转换对称密钥(C/C++)

以3DES和HMAC为例，根据指定的对称密钥二进制数据生成密钥（OH\_CryptoSymKey），将外部或存储的二进制数据转换为算法库的密钥对象，该对象可用于后续的加解密操作。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

#### 指定二进制数据转换3DES密钥

查看[对称密钥生成和转换规格：3DES](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#section3des)。

1.  获取3DES二进制密钥数据，封装成[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)。
    
2.  调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)，指定字符串参数'3DES192'，创建密钥算法为3DES、密钥长度为192位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
    
3.  调用[OH\_CryptoSymKeyGenerator\_Convert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_convert)，根据指定的对称密钥二进制数据生成对称密钥对象（OH\_CryptoSymKey）。
    
4.  调用[OH\_CryptoSymKey\_GetKeyData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。
    

以下以生成3DES密钥为例：

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_key.h"
#include "file.h"

OH\_Crypto\_ErrCode doTestDataCovertSymKey()
{
    const char \*algName = "3DES192";
    OH\_CryptoSymKeyGenerator \*ctx = nullptr;
    OH\_CryptoSymKey \*convertKeyCtx = nullptr;
    Crypto\_DataBlob out = {.data = nullptr, .len = 0};
    OH\_Crypto\_ErrCode ret;
    uint8\_t arr\[\] = {0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56, 0xad, 0x47, 0xfc, 0x5a,
                     0x46, 0x39, 0xee, 0x7c, 0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72};
    Crypto\_DataBlob convertBlob = {.data = arr, .len = sizeof(arr)};
    ret = OH\_CryptoSymKeyGenerator\_Create(algName, &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoSymKeyGenerator\_Convert(ctx, &convertBlob, &convertKeyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoSymKeyGenerator\_Destroy(ctx);
        return ret;
    }
    ret = OH\_CryptoSymKey\_GetKeyData(convertKeyCtx, &out);
    OH\_CryptoSymKeyGenerator\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(convertKeyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    OH\_Crypto\_FreeDataBlob(&out);
    return ret;
}

#### 指定二进制数据转换HMAC密钥

查看[对称密钥生成和转换规格：HMAC](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#hmac)。

1.  获取HMAC二进制密钥，封装成[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)。
    
2.  调用[OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create)，指定字符串参数'HMAC'，创建密钥算法为HMAC、密钥长度为\[1, 32768\]位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
    
3.  调用[OH\_CryptoSymKeyGenerator\_Convert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_convert)，根据指定的对称密钥二进制数据生成对称密钥对象（OH\_CryptoSymKey）。
    
4.  调用[OH\_CryptoSymKey\_GetKeyData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。
    

以下以生成HMAC密钥为例：

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_sym\_key.h"
#include <cstring>
#include "file.h"

OH\_Crypto\_ErrCode testConvertHmacKey()
{
    const char \*algName = "HMAC";
    OH\_CryptoSymKeyGenerator \*ctx = nullptr;
    OH\_CryptoSymKey \*convertKeyCtx = nullptr;
    Crypto\_DataBlob out = {.data = nullptr, .len = 0};
    OH\_Crypto\_ErrCode ret;

    char \*arr = const\_cast<char \*>("12345678abcdefgh12345678abcdefgh12345678abcdefgh12345678abcdefgh");
    Crypto\_DataBlob convertBlob = {.data = (uint8\_t \*)(arr), .len = strlen(arr)};
    ret = OH\_CryptoSymKeyGenerator\_Create(algName, &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoSymKeyGenerator\_Convert(ctx, &convertBlob, &convertKeyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoSymKeyGenerator\_Destroy(ctx);
        return ret;
    }
    ret = OH\_CryptoSymKey\_GetKeyData(convertKeyCtx, &out);
    OH\_CryptoSymKeyGenerator\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(convertKeyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    OH\_Crypto\_FreeDataBlob(&out);
    return ret;
}
