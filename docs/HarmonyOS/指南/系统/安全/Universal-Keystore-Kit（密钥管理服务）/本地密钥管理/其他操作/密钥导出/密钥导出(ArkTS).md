---
title: "密钥导出(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-arkts"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "其他操作"
  - "密钥导出"
  - "密钥导出(ArkTS)"
captured_at: "2026-04-17T01:35:51.966Z"
---

# 密钥导出(ArkTS)

业务需要获取持久化存储的非对称密钥的公钥时使用，当前支持ECC/RSA/ED25519/X25519/SM2的公钥导出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/DEvzbrsdQnKT7fmjBs1dpA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013554Z&HW-CC-Expire=86400&HW-CC-Sign=8C5F3BF12CB2BB45495EE2D4E4DAFC7D7B840BB5BDA351F9DECE2AF2CC340C2B)

轻量级智能穿戴仅支持RSA公钥导出。

从API 23开始支持[群组密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview)特性。

#### 开发步骤

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  调用接口[exportKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksexportkeyitem9)，传入参数keyAlias和options。options为预留参数，当前可传入空。
    
3.  返回值为[HuksReturnResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksreturnresult9)类型对象，获取的公钥明文在outData字段中，以标准的X.509规范的DER格式封装，具体请参考[公钥材料格式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-concepts#公钥材料格式)。
    

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
    testGenKey()
    /\* 2. 导出密钥 \*/
    huks.exportKeyItem(keyAlias, emptyOptions, (error, data) => {
      if (error) {
        console.error(\`callback: exportKeyItem failed, \` + error);
      } else {
        console.info(\`callback: exportKeyItem success, data = ${JSON.stringify(data)}\`);
      }
    });
    return 'Success';
  } catch (error) {
    console.error(\`callback: exportKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}
