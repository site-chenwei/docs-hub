---
title: "@security/no"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-ecdsa"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "安全规则@security"
  - "@security/no-unsafe-ecdsa"
captured_at: "2026-04-17T01:36:46.456Z"
---

# @security/no-unsafe-ecdsa

该规则禁止在ECDSA签名算法中使用不安全的SHA1摘要算法。推荐使用Petal Aegis SDK中的安全ECDSA接口，详情参见： [ECDSA签名验签](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-signature-verification-0000001866035345)。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdsa": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC256|SHA256');
cryptoFramework.createVerify('ECC256|SHA256');

#### 反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC224|SHA1');
cryptoFramework.createVerify('ECC224|SHA1');

#### 规则集

plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
