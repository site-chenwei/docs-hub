---
title: "Crypto_DataBlob"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "C API"
  - "结构体"
  - "Crypto_DataBlob"
captured_at: "2026-04-17T01:48:18.082Z"
---

# Crypto\_DataBlob

```c
typedef struct Crypto_DataBlob {...} Crypto_DataBlob
```

#### 概述

加解密数据结构体。

**起始版本：** 12

**相关模块：** [CryptoCommonApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi)

**所在头文件：** [crypto\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t\* data | 数据Blob的内容。 |
| size\_t len | 数据Blob的长度。 |
