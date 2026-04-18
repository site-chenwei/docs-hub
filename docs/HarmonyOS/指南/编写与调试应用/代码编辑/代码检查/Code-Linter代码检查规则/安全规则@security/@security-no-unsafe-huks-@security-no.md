---
title: "@security/no"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-huks"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "安全规则@security"
  - "@security/no-unsafe-huks"
captured_at: "2026-04-17T01:36:46.630Z"
---

# @security/no-unsafe-huks

此规则禁止在HUKS中使用不安全的加密模式ECB，不安全的摘要算法MD5、SHA1，填充算法NONE、PKCS1-V1\_5。推荐使用HUKS的AES-GCM算法，详情参见：[对称加解密算法](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-encryption-and-decryption-symmetry-0000001861247310)。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-huks": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import {huks} from '@kit.UniversalKeystoreKit';  
let keyAlias: string = 'keyAlias'; 
let properties: Array<huks.HuksParam> = \[
  { 
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_ECC
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_ECC\_KEY\_SIZE\_256
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value:
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_SIGN |
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC
  }, 
  {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST, 
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256
  },
  {
   tag: huks.HuksTag.HUKS\_TAG\_PADDING,
   value: huks.HuksKeyPadding.HUKS\_PADDING\_PKCS7
  }
\]; 
let options: huks.HuksOptions = {
    properties: properties
}; 
huks.generateKeyItem(keyAlias, options);

#### 反例

import {huks} from '@kit.UniversalKeystoreKit';  
let keyAlias: string = 'keyAlias'; 
let properties: Array<huks.HuksParam> = \[
  { 
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_ECC
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_ECC\_KEY\_SIZE\_256
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value:
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_SIGN |
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_ECB
  }, 
  {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST, 
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA1
  },
  {
   tag: huks.HuksTag.HUKS\_TAG\_PADDING,
   value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE
  }
\]; 
let options: huks.HuksOptions = {
    properties: properties
}; 
huks.generateKeyItem(keyAlias, options);

#### 规则集

plugin:@security/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
