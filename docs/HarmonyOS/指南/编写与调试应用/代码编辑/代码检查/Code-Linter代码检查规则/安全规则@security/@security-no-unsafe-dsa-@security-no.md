---
title: "@security/no"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dsa"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "安全规则@security"
  - "@security/no-unsafe-dsa"
captured_at: "2026-04-17T01:36:46.392Z"
---

# @security/no-unsafe-dsa

该规则禁止使用不安全的DSA签名算法，如DSA模数长度小于2048bit、摘要中使用不安全的SHA1哈希算法。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dsa": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA3072|SHA256');
cryptoFramework.createVerify('DSA3072|SHA256');

#### 反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA1024|SHA256');
cryptoFramework.createVerify('DSA1024|SHA256');

#### 规则集

plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
