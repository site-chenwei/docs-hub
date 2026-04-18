---
title: "获取密钥属性(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-obtain-key-properties-arkts"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "其他操作"
  - "获取密钥属性"
  - "获取密钥属性(ArkTS)"
captured_at: "2026-04-17T01:35:51.878Z"
---

# 获取密钥属性(ArkTS)

HUKS提供了接口供业务获取指定密钥的相关属性。在获取指定密钥属性前，需要确保已在HUKS中生成或导入持久化存储的密钥。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/ln7WP7AuSB6EK2JN8qHkkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013554Z&HW-CC-Expire=86400&HW-CC-Sign=B19863AEE9B4A82A59A2051C6B248AEBB21AE7A9346AD6855EE154567880741C)

轻量级智能穿戴不支持获取密钥属性功能。

从API 23开始支持[群组密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview)特性。

#### 开发步骤

1.  指定待查询的密钥别名keyAlias，密钥别名最大长度为128字节。
    
2.  调用接口[getKeyItemProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksgetkeyitemproperties9)，传入参数keyAlias和options。options为预留参数，当前可传入空。
    
3.  返回值为[HuksReturnResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksreturnresult9)类型对象，获取的属性集在properties字段中。
    

import { huks } from '@kit.UniversalKeystoreKit';

/\* 1. 设置密钥别名 \*/
let keyAlias = 'keyAlias';
/\* option对象传空 \*/
let emptyOptions: huks.HuksOptions = {
  properties: \[\]
};
let properties1: huks.HuksParam\[\] = \[
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

let huksOptions: huks.HuksOptions = {
  properties: properties1,
  inData: new Uint8Array(\[\])
}

/\* 3.生成密钥 \*/
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

async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
  console.info(\`enter promise generateKeyItem\`);
  try {
    await generateKeyItem(keyAlias, huksOptions)
      .then((data) => {
        console.info(\`promise: generateKeyItem success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        console.error(\`promise: generateKeyItem failed, ${JSON.stringify(error)}\`);
      });
    return 'Success';
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}

async function testGenKey(): Promise<string> {
  let ret = await publicGenKeyFunc(keyAlias, huksOptions);
  return ret;
}

function check(): string {
  try {
    /\* 1. 生成密钥 \*/
    testGenKey();
    /\* 2. 获取密钥属性 \*/
    huks.getKeyItemProperties(keyAlias, emptyOptions, (error, data) => {
      if (error) {
        console.error(\`callback: getKeyItemProperties failed, ${JSON.stringify(error)}\`);
      } else {
        console.info(\`callback: getKeyItemProperties success, data = ${JSON.stringify(data)}\`);
      }
    });
    return 'Success';
  } catch (error) {
    console.error(\`callback: getKeyItemProperties input arg invalid, ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}
