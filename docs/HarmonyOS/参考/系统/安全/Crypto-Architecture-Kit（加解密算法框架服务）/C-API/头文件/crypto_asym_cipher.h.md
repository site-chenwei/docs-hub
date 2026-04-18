---
title: "crypto_asym_cipher.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "C API"
  - "头文件"
  - "crypto_asym_cipher.h"
captured_at: "2026-04-17T01:48:17.932Z"
---

# crypto\_asym\_cipher.h

#### 概述

定义非对称密钥加密API。

**引用文件：** <CryptoArchitectureKit/crypto\_asym\_cipher.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoAsymCipherApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_CryptoAsymCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher) | OH\_CryptoAsymCipher | 定义非对称加密结构。 |
| [OH\_CryptoSm2CiphertextSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec) | OH\_CryptoSm2CiphertextSpec | 定义SM2密文规格结构。 |

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [CryptoSm2CiphertextSpec\_item](#cryptosm2ciphertextspec_item) | CryptoSm2CiphertextSpec\_item | 定义SM2密文规格项类型。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Create(const char \*algoName, OH\_CryptoAsymCipher \*\*ctx)](#oh_cryptoasymcipher_create) | 
根据给定的算法名称创建非对称加密。

注意：创建的资源必须通过[OH\_CryptoAsymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_destroy)销毁。

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Init(OH\_CryptoAsymCipher \*ctx, Crypto\_CipherMode mode, OH\_CryptoKeyPair \*key)](#oh_cryptoasymcipher_init) | 初始化非对称加密。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Final(OH\_CryptoAsymCipher \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](#oh_cryptoasymcipher_final) | 

完成非对称加密。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。

 |
| [void OH\_CryptoAsymCipher\_Destroy(OH\_CryptoAsymCipher \*ctx)](#oh_cryptoasymcipher_destroy) | 销毁非对称加密上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Create(Crypto\_DataBlob \*sm2Ciphertext, OH\_CryptoSm2CiphertextSpec \*\*spec)](#oh_cryptosm2ciphertextspec_create) | 

创建SM2密文规格。

注意：创建的资源必须通过[OH\_CryptoSm2CiphertextSpec\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptosm2ciphertextspec_destroy)销毁。

 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_GetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*out)](#oh_cryptosm2ciphertextspec_getitem) | 

获取SM2密文规格中的指定项。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。

 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_SetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*in)](#oh_cryptosm2ciphertextspec_setitem) | 设置SM2密文规格中的指定项。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Encode(OH\_CryptoSm2CiphertextSpec \*spec, Crypto\_DataBlob \*out)](#oh_cryptosm2ciphertextspec_encode) | 

将SM2密文规格编码为DER格式密文。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。

 |
| [void OH\_CryptoSm2CiphertextSpec\_Destroy(OH\_CryptoSm2CiphertextSpec \*spec)](#oh_cryptosm2ciphertextspec_destroy) | 销毁SM2密文规格。 |

#### 枚举类型说明

#### \[h2\]CryptoSm2CiphertextSpec\_item

```c
enum CryptoSm2CiphertextSpec_item
```

**描述**

定义SM2密文规格项类型。

**起始版本：** 20

| 枚举项 | 描述 |
| :-- | :-- |
| CRYPTO\_SM2\_CIPHERTEXT\_C1\_X = 0 | 公钥x，也称为C1x。 |
| CRYPTO\_SM2\_CIPHERTEXT\_C1\_Y = 1 | 公钥y，也称为C1y。 |
| CRYPTO\_SM2\_CIPHERTEXT\_C2 = 2 | 哈希值，也称为C2。 |
| CRYPTO\_SM2\_CIPHERTEXT\_C3 = 3 | 密文数据，也称为C3。 |

#### 函数说明

#### \[h2\]OH\_CryptoAsymCipher\_Create()

```c
OH_Crypto_ErrCode OH_CryptoAsymCipher_Create(const char *algoName, OH_CryptoAsymCipher **ctx)
```

**描述**

根据给定的算法名称创建非对称加密。

注意：创建的资源必须通过[OH\_CryptoAsymCipher\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char \*algoName | 
用于生成加密的算法名称。

例如"RSA|PKCS1\_OAEP|SHA384|MGF1\_SHA384", "SM2|SM3"。

 |
| [OH\_CryptoAsymCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher) \*\*ctx | 指向非对称加密上下文的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_errcode) | 
CRYPTO\_SUCCESS：操作成功。

CRYPTO\_NOT\_SUPPORTED：操作不支持。

CRYPTO\_MEMORY\_ERROR：内存错误。

CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。

CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。

 |

#### \[h2\]OH\_CryptoAsymCipher\_Init()

```c
OH_Crypto_ErrCode OH_CryptoAsymCipher_Init(OH_CryptoAsymCipher *ctx, Crypto_CipherMode mode, OH_CryptoKeyPair *key)
```

**描述**

初始化非对称加密。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_CryptoAsymCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher) \*ctx | 非对称加密上下文。 |
| [Crypto\_CipherMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#crypto_ciphermode) mode | 加密模式是加密还是解密。 |
| [OH\_CryptoKeyPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptokeypair) \*key | 非对称密钥。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_errcode) | 
CRYPTO\_SUCCESS：操作成功。

CRYPTO\_NOT\_SUPPORTED：操作不支持。

CRYPTO\_MEMORY\_ERROR：内存错误。

CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。

CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。

 |

**参考：**

[OH\_CryptoAsymCipher\_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_final)

#### \[h2\]OH\_CryptoAsymCipher\_Final()

```c
OH_Crypto_ErrCode OH_CryptoAsymCipher_Final(OH_CryptoAsymCipher *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

完成非对称加密。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_CryptoAsymCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher) \*ctx | 非对称加密上下文。 |
| [const Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob) \*in | 要加密或解密的数据。 |
| [Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob) \*out | 最终加密或解密的数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_errcode) | 
CRYPTO\_SUCCESS：操作成功。

CRYPTO\_NOT\_SUPPORTED：操作不支持。

CRYPTO\_MEMORY\_ERROR：内存错误。

CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。

CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。

 |

**参考：**

[OH\_CryptoAsymCipher\_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptoasymcipher_init)

#### \[h2\]OH\_CryptoAsymCipher\_Destroy()

```c
void OH_CryptoAsymCipher_Destroy(OH_CryptoAsymCipher *ctx)
```

**描述**

销毁非对称加密上下文。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_CryptoAsymCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher) \*ctx | 非对称加密上下文。 |

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_Create()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Create(Crypto_DataBlob *sm2Ciphertext, OH_CryptoSm2CiphertextSpec **spec)
```

**描述**

创建SM2密文规格。

注意：创建的资源必须通过[OH\_CryptoSm2CiphertextSpec\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#oh_cryptosm2ciphertextspec_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob) \*sm2Ciphertext | SM2密文DER格式数据，如果为NULL则创建空的SM2密文规格。 |
| [OH\_CryptoSm2CiphertextSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec) \*\*spec | 输出的SM2密文规格。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_errcode) | 
CRYPTO\_SUCCESS：操作成功。

CRYPTO\_NOT\_SUPPORTED：操作不支持。

CRYPTO\_MEMORY\_ERROR：内存错误。

CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。

CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。

 |

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_GetItem()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_GetItem(OH_CryptoSm2CiphertextSpec *spec, CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *out)
```

**描述**

获取SM2密文规格中的指定项。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec) \*spec | SM2密文规格。 |
| [CryptoSm2CiphertextSpec\_item](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#cryptosm2ciphertextspec_item) item | SM2密文规格项。 |
| [Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob) \*out | 输出数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_errcode) | 
CRYPTO\_SUCCESS：操作成功。

CRYPTO\_NOT\_SUPPORTED：操作不支持。

CRYPTO\_MEMORY\_ERROR：内存错误。

CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。

CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。

 |

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_SetItem()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_SetItem(OH_CryptoSm2CiphertextSpec *spec, CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *in)
```

**描述**

设置SM2密文规格中的指定项。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec) \*spec | SM2密文规格。 |
| [CryptoSm2CiphertextSpec\_item](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h#cryptosm2ciphertextspec_item) item | SM2密文规格项。 |
| [Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob) \*in | 输入数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_errcode) | 
CRYPTO\_SUCCESS：操作成功。

CRYPTO\_NOT\_SUPPORTED：操作不支持。

CRYPTO\_MEMORY\_ERROR：内存错误。

CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。

CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。

 |

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_Encode()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Encode(OH_CryptoSm2CiphertextSpec *spec, Crypto_DataBlob *out)
```

**描述**

将SM2密文规格编码为DER格式密文。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec) \*spec | SM2密文规格。 |
| [Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob) \*out | 输出数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_errcode) | 
CRYPTO\_SUCCESS：操作成功。

CRYPTO\_NOT\_SUPPORTED：操作不支持。

CRYPTO\_MEMORY\_ERROR：内存错误。

CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。

CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。

 |

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_Destroy()

```c
void OH_CryptoSm2CiphertextSpec_Destroy(OH_CryptoSm2CiphertextSpec *spec)
```

**描述**

销毁SM2密文规格。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec) \*spec | SM2密文规格。 |
