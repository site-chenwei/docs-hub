---
title: "E类加密数据库的使用 (ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/encrypted-estore-guidelines"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "数据可靠性与安全性"
  - "E类加密数据库的使用 (ArkTS)"
captured_at: "2026-04-17T01:35:33.803Z"
---

# E类加密数据库的使用 (ArkTS)

#### 场景介绍

从安全角度考虑，为满足部分敏感数据的安全特性，提供了E类加密数据库的方案以提高锁屏下数据的安全性。存有敏感信息的应用在申请ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA权限后会在[EL5](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant#areamode)路径下创建一个E类数据库。在锁屏的情况下（未调用Access接口获取保留文件密钥）会触发文件密钥的销毁，此时E类数据库不可读写。当锁屏解锁后，密钥会恢复，E类数据库恢复正常读写操作。这样的设计可以有效防止用户数据的泄露。

在锁屏的情况下，应用程序仍然可以继续写入数据。由于此时E类数据库不可读写，这可能会导致数据丢失。为了解决这个问题，当前提供了一种方案：在锁屏的情况下，将数据存储在[EL2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant#areamode)路径下的C类数据库中。当解锁后，再将数据迁移到E类数据库中。这样可以确保数据在锁屏期间的安全性和完整性。

键值型数据库和关系型数据库均支持E类加密数据库。

#### 实现机制

通过封装Mover类、Store类、SecretKeyObserver类和ECStoreManager类实现应用数据库密钥加锁和解锁状态下E类数据库和C类数据库的切换和操作。

Mover类：提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中有数据，使用该接口将数据迁移到E类数据库。

Store类：提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。

SecretKeyObserver类：提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。

ECStoreManager类：用于管理应用的E类数据库和C类数据库。

#### 配置权限

使用EL5路径下的数据库，需要配置ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA权限。

```ts
// module.json5
"requestPermissions": [
      {
        "name": "ohos.permission.PROTECT_SCREEN_LOCK_DATA"
      }
    ]
```

#### 键值型数据库E类加密

本章节提供键值型数据库的E类加密数据库使用方式，提供[Mover](#mover)类、[Store](#store)类、[SecretKeyObserver](#secretkeyobserver)类和[ECStoreManager](#ecstoremanager)类的具体实现，并在[EntryAbility](#entryability)和[index按键事件](#index按键事件)中展示这几个类的使用方式。

#### \[h2\]Mover

提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中存在数据，使用该接口将数据迁移到E类数据库。

import { distributedKVStore } from '@kit.ArkData';
// Logger为hilog封装后实现的打印功能
import Logger from '../common/Logger';

export class Mover {
  async move(eStore: distributedKVStore.SingleKVStore, cStore: distributedKVStore.SingleKVStore): Promise<void> {
    if (eStore != null && cStore != null) {
      let entries: distributedKVStore.Entry\[\] = await cStore.getEntries('key\_test\_string');
      await eStore.putBatch(entries);
      Logger.info(\`ECDB\_Encry move success\`);
    }
  }
}

#### \[h2\]Store

提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。

import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
// Logger为hilog封装后实现的打印功能
import Logger from '../common/Logger';

let kvManager: distributedKVStore.KVManager;

export class StoreInfo {
  kvManagerConfig: distributedKVStore.KVManagerConfig;
  storeId: string;
  option: distributedKVStore.Options;
}

export class Store {
  async getECStore(storeInfo: StoreInfo): Promise<distributedKVStore.SingleKVStore> {
    try {
      kvManager = distributedKVStore.createKVManager(storeInfo.kvManagerConfig);
      Logger.info('Succeeded in creating KVManager');
    } catch (e) {
      let error = e as BusinessError;
      Logger.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
    if (kvManager !== undefined) {
      let kvStore: distributedKVStore.SingleKVStore | null;
      try {
        kvStore = await kvManager.getKVStore<distributedKVStore.SingleKVStore>(storeInfo.storeId, storeInfo.option);
        if (kvStore != undefined) {
          Logger.info(\`ECDB\_Encry succeeded in getting store : ${storeInfo.storeId}\`);
          return kvStore;
        }
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
      }
    }
  }

  putOnedata(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string' + String(Date.now());
      const VALUE\_TEST\_STRING\_ELEMENT = 'value\_test\_string' + String(Date.now());
      try {
        kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, (err) => {
          if (err !== undefined) {
            Logger.error(\`Failed to put data. Code:${err.code},message:${err.message}\`);
            return;
          }
          Logger.info(\`ECDB\_Encry Succeeded in putting data.${KEY\_TEST\_STRING\_ELEMENT}\`);
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  getDataNum(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      let resultSet: distributedKVStore.KVStoreResultSet;
      kvStore.getResultSet('key\_test\_string').then((result: distributedKVStore.KVStoreResultSet) => {
        Logger.info(\`ECDB\_Encry Succeeded in getting result set num ${result.getCount()}\`);
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet).then(() => {
            Logger.info('Succeeded in closing result set');
          }).catch((err: BusinessError) => {
            Logger.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
          });
        }
      }).catch((err: BusinessError) => {
        Logger.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
      });
    }
  }

  deleteOnedata(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      kvStore.getEntries('key\_test\_string', (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          Logger.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        if (kvStore != null && entries.length != 0) {
          kvStore.delete(entries\[0\].key, (err: BusinessError) => {
            if (err != undefined) {
              Logger.error(\`Failed to delete.code is ${err.code},message is ${err.message}\`);
              return;
            }
            Logger.info('ECDB\_Encry Succeeded in deleting');
          });
        }
      });
    }
  }

  updateOnedata(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      kvStore.getEntries('key\_test\_string', async (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          Logger.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        if (kvStore != null && entries.length != 0) {
          Logger.info(\`ECDB\_Encry old data:${entries\[0\].key},value :${entries\[0\].value.value.toString()}\`);
          await kvStore.put(entries\[0\].key, 'new value\_test\_string' + String(Date.now()) + 'new').then(() => {
          }).catch((err: BusinessError) => {
            Logger.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
          });
          Logger.info(\`ECDB\_Encry update success\`);
        }
      });
    }
  }
}

#### \[h2\]SecretKeyObserver

该类提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。

import { ECStoreManager } from './ECStoreManager';

export enum SecretStatus {
  Lock,
  UnLock
}

export class SecretKeyObserver {
  onLock(): void {
    this.lockStatus = SecretStatus.Lock;
    this.storeManager.closeEStore();
  }

  onUnLock(): void {
    this.lockStatus = SecretStatus.UnLock;
  }

  getCurrentStatus(): number {
    return this.lockStatus;
  }

  initialize(storeManager: ECStoreManager): void {
    this.storeManager = storeManager;
  }

  updateLockStatus(code: number) {
    if (code === SecretStatus.Lock) {
      this.onLock();
    } else {
      this.lockStatus = code;
    }
  }

  // 初始获取锁屏状态
  private lockStatus: number = SecretStatus.UnLock;
  private storeManager: ECStoreManager;
}

export let lockObserve = new SecretKeyObserver();

#### \[h2\]ECStoreManager

ECStoreManager类用于管理应用的E类数据库和C类数据库。支持配置数据库信息、配置迁移函数的信息，可根据密钥状态为应用提供相应的数据库句柄，并提供了关闭E类数据库、数据迁移完成后销毁C类数据库等接口。

import { distributedKVStore } from '@kit.ArkData';
import { Mover } from './Mover';
import { BusinessError } from '@kit.BasicServicesKit';
import { StoreInfo, Store } from './Store';
import { SecretStatus } from './SecretKeyObserver';
// Logger为hilog封装后实现的打印功能
import Logger from '../common/Logger';

let store = new Store();

export class ECStoreManager {
  config(cInfo: StoreInfo, other: StoreInfo): void {
    this.cInfo = cInfo;
    this.eInfo = other;
  }

  configDataMover(mover: Mover): void {
    this.mover = mover;
  }

  async getCurrentStore(screenStatus: number): Promise<distributedKVStore.SingleKVStore> {
    Logger.info(\`ECDB\_Encry GetCurrentStore start screenStatus: ${screenStatus}\`);
    if (screenStatus === SecretStatus.UnLock) {
      try {
        this.eStore = await store.getECStore(this.eInfo);
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      // 解锁状态 获取e类库
      if (this.needMove) {
        if (this.eStore != undefined && this.cStore != undefined) {
          await this.mover.move(this.eStore, this.cStore);
        }
        this.deleteCStore();
        Logger.info(\`ECDB\_Encry Data migration is complete. Destroy cstore\`);
        this.needMove = false;
      }
      return this.eStore;
    } else {
      // 加锁状态 获取c类库
      this.needMove = true;
      try {
        this.cStore = await store.getECStore(this.cInfo);
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      return this.cStore;
    }
  }

  closeEStore(): void {
    try {
      let kvManager = distributedKVStore.createKVManager(this.eInfo.kvManagerConfig);
      Logger.info('Succeeded in creating KVManager');
      if (kvManager != undefined) {
        kvManager.closeKVStore(this.eInfo.kvManagerConfig.bundleName, this.eInfo.storeId);
        this.eStore = null;
        Logger.info(\`ECDB\_Encry close EStore success\`);
      }
    } catch (e) {
      let error = e as BusinessError;
      Logger.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
  }

  deleteCStore(): void {
    try {
      let kvManager = distributedKVStore.createKVManager(this.cInfo.kvManagerConfig);
      Logger.info('Succeeded in creating KVManager');
      if (kvManager != undefined) {
        kvManager.deleteKVStore(this.cInfo.kvManagerConfig.bundleName, this.cInfo.storeId);
        this.cStore = null;
        Logger.info('ECDB\_Encry delete cStore success');
      }
    } catch (e) {
      let error = e as BusinessError;
      Logger.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
  }

  private eStore: distributedKVStore.SingleKVStore = null;
  private cStore: distributedKVStore.SingleKVStore = null;
  private cInfo: StoreInfo | null = null;
  private eInfo: StoreInfo | null = null;
  private needMove: boolean = false;
  private mover: Mover | null = null;
}

#### \[h2\]EntryAbility

模拟应用启动期间，注册对COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED公共事件的监听，并配置相应的数据库信息、密钥状态信息等。

import { AbilityConstant, application, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { distributedKVStore } from '@kit.ArkData';
import { ECStoreManager } from './ECStoreManager';
import { StoreInfo } from './Store';
import { Mover } from './Mover';
import { SecretKeyObserver } from './SecretKeyObserver';
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
// Logger为hilog封装后实现的打印功能
import Logger from '../common/Logger';

export let storeManager = new ECStoreManager();
export let e\_secretKeyObserver = new SecretKeyObserver();
let mover = new Mover();
let subscriber: commonEventManager.CommonEventSubscriber;

export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
  if (!err) {
    Logger.info('ECDB\_Encry createSubscriber');
    subscriber = commonEventSubscriber;
    try {
      commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
        if (err) {
          Logger.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
        } else {
          Logger.info(\`ECDB\_Encry SubscribeCB ${data.code}\`);
          e\_secretKeyObserver.updateLockStatus(data.code);
        }
      });
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
    }
  } else {
    Logger.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
  }
}

let cInfo: StoreInfo | null = null;
let eInfo: StoreInfo | null = null;

export default class EntryAbility extends UIAbility {
  async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let cContext = this.context;
    cInfo = {
      'kvManagerConfig': {
        context: cContext,
        bundleName: 'com.example.ecstoresamples'
      },
      'storeId': 'cstore',
      'option': {
        createIfMissing: true,
        encrypt: false,
        backup: false,
        autoSync: false,
        // kvStoreType不填时，默认创建多设备协同数据库
        kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
        // 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE\_COLLABORATION
        securityLevel: distributedKVStore.SecurityLevel.S3
      }
    }
    let eContext = await application.createModuleContext(this.context,'entry');
    eContext.area = contextConstant.AreaMode.EL5;
    eInfo = {
      'kvManagerConfig': {
        context: eContext,
        bundleName: 'com.example.ecstoresamples'
      },
      'storeId': 'estore',
      'option': {
        createIfMissing: true,
        encrypt: false,
        backup: false,
        autoSync: false,
        // kvStoreType不填时，默认创建多设备协同数据库
        kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
        // 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE\_COLLABORATION
        securityLevel: distributedKVStore.SecurityLevel.S3
      }
    }
    Logger.info(\`ECDB\_Encry store area : estore:${eContext.area},cstore${cContext.area}\`);
    // 监听COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED事件 code == 1解锁状态，code==0加锁状态
    try {
      commonEventManager.createSubscriber({
        events: \[ 'COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED' \]
      }, createCB);
      Logger.info(\`ECDB\_Encry success subscribe\`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
    }
    storeManager.config(cInfo, eInfo);
    storeManager.configDataMover(mover);
    e\_secretKeyObserver.initialize(storeManager);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

#### \[h2\]Index按键事件

使用Button按钮，通过点击按钮来模拟应用操作数据库，如插入数据、删除数据、更新数据和获取数据数量的操作等，展示数据库基本的增删改查能力。

import { storeManager, e\_secretKeyObserver } from '../entryability/EntryAbility';
import { distributedKVStore } from '@kit.ArkData';
import { Store } from '../entryability/Store';

let storeOption = new Store();
let lockStatus: number = 1;

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Button('加锁/解锁').onClick((event: ClickEvent) => {
          if (lockStatus) {
            e\_secretKeyObserver.onLock();
            lockStatus = 0;
          } else {
            e\_secretKeyObserver.onUnLock();
            lockStatus = 1;
          }
          lockStatus ? this.message = '解锁' : this.message = '加锁';
        }).margin(5)
          .width(100) // 宽度，单位默认vp（可视像素）
          .height(40) // 高度

        Button('StoreType').onClick(async (event: ClickEvent) => {
          e\_secretKeyObserver.getCurrentStatus() ? this.message = 'estore' : this.message = 'cstore';
        }).margin(5)
          .width(100) // 宽度，单位默认vp（可视像素）
          .height(40) // 高度

        Button('Put').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.putOnedata(store);
        }).margin(5)
          .width(100) // 宽度，单位默认vp（可视像素）
          .height(40) // 高度

        Button('Get').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.getDataNum(store);
        }).margin(5)
          .width(100) // 宽度，单位默认vp（可视像素）
          .height(40) // 高度

        Button('Delete').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.deleteOnedata(store);
        }).margin(5)
          .width(100) // 宽度，单位默认vp（可视像素）
          .height(40) // 高度

        Button('Update').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.updateOnedata(store);
        }).margin(5)
          .width(100) // 宽度，单位默认vp（可视像素）
          .height(40) // 高度

        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### 关系型数据库E类加密

本章节提供关系型数据库的E类加密数据库使用方式，提供[Mover](#mover-1)类，[Store](#store-1)类，[SecretKeyObserver](#secretkeyobserver-1)类和[ECStoreManager](#ecstoremanager-1)类的具体实现，并在[EntryAbility](#entryability-1)和[index按键事件](#index按键事件-1)中展示这几个类的使用方式。

#### \[h2\]Mover

提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中有数据，使用该接口将数据迁移到E类数据库。

import { relationalStore } from '@kit.ArkData';

export class Mover {
  async move(eStore: relationalStore.RdbStore, cStore: relationalStore.RdbStore) {
    if (eStore != null && cStore != null) {
      let predicates = new relationalStore.RdbPredicates('employee');
      let resultSet = await cStore.query(predicates);
      while (resultSet.goToNextRow()) {
        let bucket = resultSet.getRow();
        await eStore.insert('employee', bucket);
      }
    }
  }
}

#### \[h2\]Store

提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。其中StoreInfo类用于存储获取数据库相关信息。

import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { Context } from '@kit.AbilityKit';

export class StoreInfo {
  context: Context;
  config: relationalStore.StoreConfig;
  storeId: string;
}

let id = 1;
const SQL\_CREATE\_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)';

export class Store {
  async getECStore(storeInfo: StoreInfo): Promise<relationalStore.RdbStore> {
    let rdbStore: relationalStore.RdbStore | null;
    try {
      rdbStore = await relationalStore.getRdbStore(storeInfo.context, storeInfo.config);
      if (rdbStore.version == 0) {
        await rdbStore.executeSql(SQL\_CREATE\_TABLE);
        console.info(\`ECDB\_Encry succeeded in getting Store ：${storeInfo.storeId}\`);
        rdbStore.version = 1;
      }
    } catch (e) {
      let error = e as BusinessError;
      console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
    }
    return rdbStore;
  }

  async putOnedata(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      const valueBucket: relationalStore.ValuesBucket = {
        ID: id++,
        NAME: 'Lisa',
        AGE: 18,
        SALARY: 100.5,
        CODES: new Uint8Array(\[1, 2, 3, 4, 5\]),
      };
      try {
        await rdbStore.insert('EMPLOYEE', valueBucket);
        console.info(\`ECDB\_Encry insert success\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  async getDataNum(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      try {
        let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
        let resultSet = await rdbStore.query(predicates);
        let count = resultSet.rowCount;
        console.info(\`ECDB\_Encry getdatanum success count : ${count}\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  async deleteAlldata(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      try {
        let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
        predicates.equalTo('AGE', 18);
        await rdbStore.delete(predicates);
        console.info(\`ECDB\_Encry delete Success\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  async updateOnedata(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      try {
        let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
        predicates.equalTo('NAME', 'Lisa');
        const valueBucket: relationalStore.ValuesBucket = {
          NAME: 'Anna',
          SALARY: 100.5,
          CODES: new Uint8Array(\[1, 2, 3, 4, 5\]),
        };
        await rdbStore.update(valueBucket, predicates);
        console.info(\`ECDB\_Encry update success\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }
}

#### \[h2\]SecretKeyObserver

该类提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。

import { ECStoreManager } from './ECStoreManager';

export enum SecretStatus {
  Lock,
  UnLock
}

export class SecretKeyObserver {
  onLock(): void {
    this.lockStatus = SecretStatus.Lock;
    this.storeManager.closeEStore();
  }

  onUnLock(): void {
    this.lockStatus = SecretStatus.UnLock;
  }

  getCurrentStatus(): number {
    return this.lockStatus;
  }

  initialize(storeManager: ECStoreManager): void {
    this.storeManager = storeManager;
  }

  updateLockStatus(code: number) {
    if (this.lockStatus === SecretStatus.Lock) {
      this.onLock();
    } else {
      this.lockStatus = code;
    }
  }

  private lockStatus: number = SecretStatus.UnLock;
  private storeManager: ECStoreManager;
}

export let lockObserve = new SecretKeyObserver();

#### \[h2\]ECStoreManager

ECStoreManager类用于管理应用的E类数据库和C类数据库。支持配置数据库信息、配置迁移函数的信息，可根据密钥状态为应用提供相应的数据库句柄，并提供了关闭E类数据库、数据迁移完成后销毁C类数据库等接口。

import { relationalStore } from '@kit.ArkData';
import { Mover } from './Mover';
import { BusinessError } from '@kit.BasicServicesKit';
import { StoreInfo, Store } from './Store';
import { SecretStatus } from './SecretKeyObserver';

let store = new Store();

export class ECStoreManager {
  config(cInfo: StoreInfo, other: StoreInfo): void {
    this.cInfo = cInfo;
    this.eInfo = other;
  }

  configDataMover(mover: Mover): void {
    this.mover = mover;
  }

  async getCurrentStore(screenStatus: number): Promise<relationalStore.RdbStore> {
    if (screenStatus === SecretStatus.UnLock) {
      try {
        this.eStore = await store.getECStore(this.eInfo);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      // 解锁状态 获取e类库
      if (this.needMove) {
        if (this.eStore != undefined && this.cStore != undefined) {
          await this.mover.move(this.eStore, this.cStore);
          console.info(\`ECDB\_Encry cstore data move to estore success\`);
        }
        this.deleteCStore();
        this.needMove = false;
      }
      return this.eStore;
    } else {
      // 加锁状态 获取c类库
      this.needMove = true;
      try {
        this.cStore = await store.getECStore(this.cInfo);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      return this.cStore;
    }
  }

  closeEStore(): void {
    this.eStore = undefined;
  }

  async deleteCStore() {
    try {
      await relationalStore.deleteRdbStore(this.cInfo.context, this.cInfo.storeId)
    } catch (e) {
      let error = e as BusinessError;
      console.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
  }

  private eStore: relationalStore.RdbStore = null;
  private cStore: relationalStore.RdbStore = null;
  private cInfo: StoreInfo | null = null;
  private eInfo: StoreInfo | null = null;
  private needMove: boolean = false;
  private mover: Mover | null = null;
}

#### \[h2\]EntryAbility

模拟在应用启动期间，注册对COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED公共事件的监听，并配置相应的数据库信息、密钥状态信息等。

import { AbilityConstant, contextConstant, UIAbility, Want, application } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { relationalStore } from '@kit.ArkData';
import { ECStoreManager } from '../encryptedEStoreGuidelines/ECStoreManager';
import { StoreInfo } from '../encryptedEStoreGuidelines/Store';
import { Mover } from '../encryptedEStoreGuidelines/Mover';
import { SecretKeyObserver } from '../encryptedEStoreGuidelines/SecretKeyObserver';
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

export let storeManager = new ECStoreManager();
export let e\_secretKeyObserver = new SecretKeyObserver();
let mover = new Mover();
let subscriber: commonEventManager.CommonEventSubscriber;

export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
  if (!err) {
    console.info('ECDB\_Encrypt createSubscriber');
    subscriber = commonEventSubscriber;
    try {
      commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
        if (err) {
          console.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
        } else {
          console.info(\`ECDB\_Encrypt SubscribeCB ${data.code}\`);
          e\_secretKeyObserver.updateLockStatus(data.code);
        }
      });
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
    }
  } else {
    console.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
  }
}

let cInfo: StoreInfo | null = null;
let eInfo: StoreInfo | null = null;

export default class EntryAbility extends UIAbility {
  async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let cContext = this.context;
    cInfo = {
      context: cContext,
      config: {
        name: 'cstore.db',
        securityLevel: relationalStore.SecurityLevel.S3,
      },
      storeId: 'cstore.db'
    };
    let eContext = await application.createModuleContext(this.context, 'entry');
    eContext.area = contextConstant.AreaMode.EL5;
    eInfo = {
      context: eContext,
      config: {
        name: 'estore.db',
        securityLevel: relationalStore.SecurityLevel.S3,
      },
      storeId: 'estore.db',
    };
    // 监听COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED事件 code == 1解锁状态，code==0加锁状态
    console.info(\`ECDB\_Encry store area : estore:${eContext.area},cstore${cContext.area}\`)
    try {
      commonEventManager.createSubscriber({
        events: \['COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED'\]
      }, createCB);
      console.info(\`ECDB\_Encry success subscribe\`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
    }
    storeManager.config(cInfo, eInfo);
    storeManager.configDataMover(mover);
    e\_secretKeyObserver.initialize(storeManager);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

#### \[h2\]Index按键事件

使用Button按钮，通过点击按钮来模拟应用操作数据库，如插入数据、删除数据、更新数据和获取数据数量的操作等，展示数据库基本的增删改查能力。

import { storeManager, e\_secretKeyObserver } from '../entryability/EntryAbility';
import { relationalStore } from '@kit.ArkData';
import { Store } from './Store';

let storeOption = new Store();

let lockStatus: number = 1;

@Entry
@Component
struct Index {
  @State message: string = '';

  build() {
    Row() {
      Column() {
        Button('加锁/解锁')
          .onClick((event: ClickEvent) => {
            if (lockStatus) {
              e\_secretKeyObserver.onLock();
              lockStatus = 0;
            } else {
              e\_secretKeyObserver.onUnLock();
              lockStatus = 1;
            }
            lockStatus ? this.message = '解锁' : this.message = '加锁';
          })
          .margin('5')
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('store type')
          .onClick(async (event: ClickEvent) => {
            e\_secretKeyObserver.getCurrentStatus() ? this.message = 'estore' : this.message = 'cstore';
            console.info(\`ECDB\_Encry current store : ${this.message}\`);
          })
          .margin('5')
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('put')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.putOnedata(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('Get')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.getDataNum(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('delete')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.deleteAlldata(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('update')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.updateOnedata(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
