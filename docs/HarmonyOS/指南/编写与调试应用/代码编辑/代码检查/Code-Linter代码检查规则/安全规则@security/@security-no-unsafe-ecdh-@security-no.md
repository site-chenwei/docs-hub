---
title: "@security/no"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-ecdh"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "安全规则@security"
  - "@security/no-unsafe-ecdh"
captured_at: "2026-04-17T01:36:46.591Z"
---

# @security/no-unsafe-ecdh

此规则禁止使用不安全的非对称密钥类型ECC。推荐使用ECC256算法，详情参见：[密钥生成算法](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-key-generation-0000001819355432)。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdh": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC256');

#### 反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC');

#### 规则集

plugin:@security/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
