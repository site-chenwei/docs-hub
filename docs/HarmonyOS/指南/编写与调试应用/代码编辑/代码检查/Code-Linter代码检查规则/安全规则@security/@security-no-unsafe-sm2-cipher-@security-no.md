---
title: "@security/no"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm2-cipher"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "安全规则@security"
  - "@security/no-unsafe-sm2-cipher"
captured_at: "2026-04-17T01:36:46.587Z"
---

# @security/no-unsafe-sm2-cipher

此规则禁止在SM2算法中使用不安全的消息摘要算法MD5和SHA1。推荐使用SM2\_256|SHA256算法和RSA算法，算法详情参见：[非对称加解密算法](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453)和[非对称密钥加解密算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec#rsa)。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm2-cipher": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM2\_256|SHA256')

#### 反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM2\_256|SHA1')
cryptoFramework.createCipher('SM2\_256|MD5')

#### 规则集

plugin:@security/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
