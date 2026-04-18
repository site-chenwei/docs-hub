---
title: "密钥删除(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-arkts"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥删除"
  - "密钥删除(ArkTS)"
captured_at: "2026-04-17T01:35:51.643Z"
---

# 密钥删除(ArkTS)

为保证数据安全性，当不需要使用该密钥时，应该删除密钥。

从API 23开始支持[群组密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview)特性。

#### 开发步骤

以删除HKDF256密钥为例。

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  初始化密钥属性集。用于删除时指定密钥的属性，删除单个密钥或者非群组密钥，可传空。
    
3.  调用接口[deleteKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksdeletekeyitem9)，删除密钥。
    

/\*
 \* 以下以HKDF256密钥的Promise操作使用为例
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test\_Key';

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
  try {
    await generateKeyItem(keyAlias, huksOptions);
    console.info(\`promise: generateKeyItem success\`);
  } catch (error) {
    console.error(\`promise: generateKeyItem failed, ${JSON.stringify(error)}\`);
  }
}

/\* 2.删除密钥 \*/
let deleteHuksOptions: huks.HuksOptions = {
  properties: \[\]
}

function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.deleteKeyItem(keyAlias, huksOptions, (error, data) => {
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

async function deleteKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(\`enter promise deleteKeyItem\`);
  try {
    await deleteKeyItem(keyAlias, huksOptions);
    console.info(\`promise: deleteKeyItem success\`);
  } catch (error) {
    console.error(\`promise: deleteKeyItem failed, ${JSON.stringify(error)}\`);
  }
}

async function executeKeyLifecycle(): Promise<string> {
  try {
    /\* 1.生成密钥 \*/
    console.info('start generateKey...');
    await generateKey(keyAlias, generateHuksOptions);
    console.info('end generateKey...');

    /\* 2.删除密钥 \*/
    console.info('start deleteKey...');
    await deleteKey(keyAlias, deleteHuksOptions);
    console.info('end deleteKey...');

    console.info('Key lifecycle completed successfully');
    return 'Success';
  } catch (error) {
    console.error(\`Key lifecycle failed: ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}
