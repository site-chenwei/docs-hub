---
title: "密钥派生(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-arkts"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥使用"
  - "密钥派生"
  - "密钥派生(ArkTS)"
captured_at: "2026-04-17T01:35:51.468Z"
---

# 密钥派生(ArkTS)

以PBKDF2和HKDF256密钥为例，完成密钥派生。具体的场景介绍及支持的算法规格，请参考[密钥派生支持的算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-overview#支持的算法)。

#### 开发步骤

**生成密钥**

1.  指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    
2.  初始化密钥属性集，可指定参数HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识基于该密钥派生出的密钥是否由HUKS管理。
    
    -   当TAG设置为HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS时，表示基于该密钥派生出的密钥，由HUKS管理，可保证派生密钥全生命周期不出安全环境。
        
    -   当TAG设置为HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED时，表示基于该密钥派生出的密钥，返回给调用方管理，由业务自行保证密钥安全。
        
    -   若业务未设置TAG的具体值，表示基于该密钥派生出的密钥，即可由HUKS管理，也可返回给调用方管理，业务可在后续派生时再选择使用何种方式保护密钥。
        
3.  调用[generateKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
    

除此之外，开发者也可以参考[密钥导入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview)，导入已有的密钥。

**密钥派生**

1.  获取密钥别名，指定对应的属性参数HuksOptions。
    
    可指定参数HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识派生得到的密钥是否由HUKS管理。
    
    | 生成 | 派生 | 规格 |
    | :-- | :-- | :-- |
    | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
    | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
    | 未指定TAG具体值 | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
    | 未指定TAG具体值 | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
    | 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |
    
    注：派生时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。
    
2.  调用[initSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
    
3.  调用[updateSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksupdatesession9)更新密钥会话。
    
4.  调用[finishSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksfinishsession9)结束密钥会话，完成派生。
    

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-arkts)。

#### 开发案例

#### \[h2\]HKDF

准备HKDF密钥派生材料

/\*
 \* 以下以HKDF密钥的Promise操作使用为例
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

/\*
 \* 确定密钥别名和封装密钥属性参数集
 \*/
let srcKeyAlias = 'hkdf\_Key';
let deriveHkdfInData = 'deriveHkdfTestIndata';
let handle: number;
let finishOutData: Uint8Array;
let huksKeyDeriveKeySize = 32;
/\* 集成生成密钥参数集 \*/
let properties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}\];

let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(\[\])
}
/\* 集成init时密钥参数集 \*/
let initProperties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_HKDF,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVE\_KEY\_SIZE,
  value: huksKeyDeriveKeySize,
}\];

let initOptions: huks.HuksOptions = {
  properties: initProperties,
  inData: new Uint8Array(\[\])
}
/\* 集成finish时密钥参数集 \*/
let finishProperties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_IS\_KEY\_ALIAS,
  value: true,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value:
  huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
  huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
  value: stringToUint8Array(srcKeyAlias),
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_ECB,
}\];
let finishOptions: huks.HuksOptions = {
  properties: finishProperties,
  inData: new Uint8Array(\[\])
}

function stringToUint8Array(str: String) {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

class ThrowObject {
  public isThrow = false;
}

执行密钥派生

function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
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
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise generateKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await generateKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: generateKeyItem success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: generateKeyItem failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function initSession(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
    try {
      huks.initSession(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicInitFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doInit\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await initSession(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doInit success, data = ${JSON.stringify(data)}\`);
        handle = data.handle;
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doInit failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doInit input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function updateSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksOptions>((resolve, reject) => {
    try {
      huks.updateSession(handle, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicUpdateFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doUpdate\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await updateSession(handle, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doUpdate success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doUpdate failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doUpdate input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function finishSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.finishSession(handle, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicFinishFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doFinish\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await finishSession(handle, huksOptions, throwObject)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(\`promise: doFinish success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doFinish failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doFinish input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
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
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicDeleteKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise deleteKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await deleteKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: deleteKeyItem failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: deleteKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

async function testDerive() {
  /\* 生成密钥 \*/
  await publicGenKeyFunc(srcKeyAlias, huksOptions);
  /\* 进行派生操作 \*/
  await publicInitFunc(srcKeyAlias, initOptions);
  initOptions.inData = stringToUint8Array(deriveHkdfInData);
  await publicUpdateFunc(handle, initOptions);
  await publicFinishFunc(handle, finishOptions);
  await publicDeleteKeyFunc(srcKeyAlias, huksOptions);
}

#### \[h2\]PBKDF2

准备PBKDF2密钥派生材料

/\*
 \* 以下以PBKDF2密钥的Promise操作使用为例
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

/\*
 \* 确定密钥别名和封装密钥属性参数集
 \*/
let srcKeyAlias = 'pbkdf2\_Key';
let salt = 'mySalt';
let iterationCount = 10000;
let derivedKeySize = 32;
let handle: number;
let finishOutData: Uint8Array;

/\* 集成生成密钥参数集 \*/
let properties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}
\];

let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(\[\])
}

/\* 集成init时密钥参数集 \*/
let initProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_PBKDF2,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVE\_KEY\_SIZE,
  value: derivedKeySize,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_ITERATION,
  value: iterationCount,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_SALT,
  value: stringToUint8Array(salt),
}
\];

let initOptions: huks.HuksOptions = {
  properties: initProperties,
  inData: new Uint8Array(\[\])
}

/\* 集成finish时密钥参数集 \*/
let finishProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
    value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_IS\_KEY\_ALIAS,
  value: true,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT | huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
  value: stringToUint8Array(srcKeyAlias),
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_ECB,
}
\];

let finishOptions: huks.HuksOptions = {
  properties: finishProperties,
  inData: new Uint8Array(\[\])
}

function stringToUint8Array(str: String) {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

class ThrowObject {
  public isThrow = false;
}

执行密钥派生

function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
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
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise generateKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await generateKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: generateKeyItem success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: generateKeyItem failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function initSession(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
    try {
      huks.initSession(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicInitFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doInit\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await initSession(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doInit success, data = ${JSON.stringify(data)}\`);
        handle = data.handle;
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doInit failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doInit input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function updateSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksOptions>((resolve, reject) => {
    try {
      huks.updateSession(handle, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicUpdateFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doUpdate\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await updateSession(handle, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doUpdate success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doUpdate failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doUpdate input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function finishSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.finishSession(handle, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicFinishFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doFinish\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await finishSession(handle, huksOptions, throwObject)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(\`promise: doFinish success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doFinish failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doFinish input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
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
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicDeleteKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise deleteKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await deleteKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: deleteKeyItem failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: deleteKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

async function testDerive() {
  /\* 生成密钥 \*/
  await publicGenKeyFunc(srcKeyAlias, huksOptions);
  /\* 进行派生操作 \*/
  await publicInitFunc(srcKeyAlias, initOptions);
  await publicUpdateFunc(handle, initOptions);
  await publicFinishFunc(handle, finishOptions);
  await publicDeleteKeyFunc(srcKeyAlias, huksOptions);
}
