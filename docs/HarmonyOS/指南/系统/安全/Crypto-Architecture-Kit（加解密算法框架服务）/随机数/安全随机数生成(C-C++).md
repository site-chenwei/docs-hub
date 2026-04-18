---
title: "安全随机数生成(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "随机数"
  - "安全随机数生成(C/C++)"
captured_at: "2026-04-17T01:35:49.152Z"
---

# 安全随机数生成(C/C++)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/E0Df3NhlRyasM6okOckJ7A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=7B6632E20471F9C553B07ADCA993CB4D32817139FE582DF149D2723E01CB3C42)

从API version 12开始，轻量级智能穿戴设备支持获取随机数相关操作。

随机数主要用于临时会话密钥生成和非对称加密算法密钥生成等场景。在加解密场景中，安全随机数生成器需要具备随机性、不可预测性与不可重现性。当前系统生成的随机数满足密码学安全伪随机性要求。

开发者可以调用接口，完成以下功能：

-   生成指定长度的安全随机数，并将其用于生成对应的密钥。
    
-   指定随机种子，生成一系列的随机序列。
    

在开发前，开发者应该先对加解密基础知识有一定了解，并熟知以下随机数相关的基本概念：

-   **内部状态**
    
    代表随机数生成器内存中的数值，当内部状态相同时，随机数生成器会生成固定的随机数序列。
    
-   **随机种子**
    
    一个用来对伪随机数的内部状态进行初始化的数据，随机数生成器通过种子来生成一系列的随机序列。
    
    当前OpenSSL实现方式，随机数生成器内部状态是不断变化的，即使设置相同的种子，生成的随机数序列也不会相同。
    

#### 支持的算法与规格

随机数生成算法使用OpenSSL的RAND\_priv\_bytes接口生成安全随机数。

| 算法 | 长度（Byte） |
| :-- | :-- |
| CTR\_DRBG | \[1, INT\_MAX\] |

#### 开发步骤

1.  调用[OH\_CryptoRand\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_create)，创建随机数生成器。
    
2.  （可选）调用[OH\_CryptoRand\_SetSeed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_setseed)，为随机数生成器设置种子。
    
3.  调用[OH\_CryptoRand\_GenerateRandom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_generaterandom)，生成指定长度的安全随机数。指定字节长度范围为1~INT\_MAX。
    
4.  调用[OH\_CryptoRand\_GetAlgoName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_getalgoname)，获取随机数生成器使用的算法名称。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <cstdio>
#include "file.h"

OH\_Crypto\_ErrCode doTestRandomNumber()
{
    // 创建随机数生成器。
    OH\_CryptoRand \*rand = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoRand\_Create(&rand);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // 设置随机种子（可选）。
    uint8\_t seedData\[12\] = {0x25, 0x65, 0x58, 0x89, 0x85, 0x55, 0x66, 0x77, 0x88, 0x99, 0x11, 0x22};
    Crypto\_DataBlob seed = {
        .data = seedData,
        .len = sizeof(seedData)
    };
    ret = OH\_CryptoRand\_SetSeed(rand, &seed);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoRand\_Destroy(rand);
        return ret;
    }

    // 生成指定长度的随机数。
    Crypto\_DataBlob out = {0};
    uint32\_t randomLength = 24; // 生成24字节的随机数。
    ret = OH\_CryptoRand\_GenerateRandom(rand, randomLength, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoRand\_Destroy(rand);
        return ret;
    }

    // 获取并打印随机数生成器的算法名称。
    const char \*algoName = OH\_CryptoRand\_GetAlgoName(rand);
    if (algoName != nullptr) {
        printf("Random number generator algorithm: %s\\n", algoName);
    }

    printf("Generated random number length: %u\\n", out.len);

    // 清理资源。
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoRand\_Destroy(rand);
    return CRYPTO\_SUCCESS;
}
