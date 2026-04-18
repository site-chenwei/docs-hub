---
title: "查询密钥是否存在(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-check-key-arkts"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "其他操作"
  - "查询密钥是否存在"
  - "查询密钥是否存在(ArkTS)"
captured_at: "2026-04-17T01:35:51.851Z"
---

# 查询密钥是否存在(ArkTS)

HUKS提供了接口供应用查询指定密钥是否存在。

从API 23开始支持[群组密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview)特性。

#### 开发步骤

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  初始化密钥属性集。用于查询时指定密钥的属性，查询单个密钥或者非群组密钥，可传空。
    
3.  调用接口[hasKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukshaskeyitem11)，查询密钥是否存在。
    

import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test\_key';
let isKeyExist: Boolean;

let generateProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_DH
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_AGREE
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_DH\_KEY\_SIZE\_2048
  }
\];

let generateHuksOptions: huks.HuksOptions = {
  properties: generateProperties,
  inData: new Uint8Array(\[\])
}

/\* 1.生成密钥 \*/
function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}

async function generateKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(\`enter promise generateKeyItem\`);
  await generateKeyItem(keyAlias, huksOptions);
  console.info(\`promise: generateKeyItem success\`);
}

/\* 2.检查密钥是否存在 \*/
let huksOptions: huks.HuksOptions = {
  properties: \[\]
}

function hasKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<boolean>((resolve, reject) => {
    try {
      huks.hasKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data.valueOf());
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}

async function checkKeyExistence(keyAlias: string, huksOptions: huks.HuksOptions): Promise<boolean> {
  console.info(\`enter promise hasKeyItem\`);
  const exists = await hasKeyItem(keyAlias, huksOptions);
  console.info(\`promise: hasKeyItem success, isKeyExist = ${exists}\`);
  return exists;
}

async function executeCheckKey(): Promise<string> {
  try {
    /\* 1.生成密钥 \*/
    await generateKey(keyAlias, generateHuksOptions);

    /\* 2.检查密钥是否存在 \*/
    isKeyExist = await checkKeyExistence(keyAlias, huksOptions);

    console.info(\`Key check completed, isKeyExist = ${isKeyExist}\`);
    return 'Success';
  } catch (error) {
    console.error(\`Key check failed: ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}
