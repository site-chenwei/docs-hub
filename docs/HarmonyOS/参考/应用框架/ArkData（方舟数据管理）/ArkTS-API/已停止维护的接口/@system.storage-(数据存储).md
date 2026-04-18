---
title: "@system.storage (数据存储)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-storage"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@system.storage (数据存储)"
captured_at: "2026-04-17T01:47:49.803Z"
---

# @system.storage (数据存储)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/8VhlHNT8RX-0fSHt79BZcQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=A6D53DFCEC4F8DF1021F7E790A95D1E2711C3E4D8555953CBB23BDD9A9D12337)

-   模块维护策略：
    
    -   对于Lite Wearable设备类型，该模块长期维护，可正常使用。
    -   对于支持该模块的其他设备类型，该模块从API version 6开始不再维护，可以使用模块[@ohos.data.storage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-storage)。在API version 9后，推荐使用新模块[@ohos.data.preferences](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences)。
-   本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本模块接口仅可在FA模型下使用。
    

#### 导入模块

```js
import storage from '@system.storage';
```

#### storage.get

get(options: GetStorageOptions): void

通过索引读取缓存中存储的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [GetStorageOptions](#getstorageoptions) | 是 | 接口配置信息。 |

**示例：**

```js
export default {
  storageGet() {
    storage.get({
      key: 'storage_key',
      success: function(data) {
        console.log('call storage.get success: ' + data);
      },
      fail: function(data, code) {
        console.log('call storage.get fail, code: ' + code + ', data: ' + data);
      },
      complete: function() {
        console.log('call complete');
      },
    });
  }
}
```

#### storage.set

set(options: SetStorageOptions): void

修改缓存中索引对应的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [SetStorageOptions](#setstorageoptions) | 是 | 接口配置信息。 |

**示例：**

```js
export default {
  storageSet() {
    storage.set({
      key: 'storage_key',
      value: 'storage value',
      success: function() {
        console.log('call storage.set success.');
      },
      fail: function(data, code) {
        console.log('call storage.set fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### storage.clear

clear(options?: ClearStorageOptions): void

清空缓存中存储的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ClearStorageOptions](#clearstorageoptions) | 否 | 接口配置信息。 |

**示例：**

```js
export default {
  storageClear() {
    storage.clear({
      success: function() {
        console.log('call storage.clear success.');
      },
      fail: function(data, code) {
        console.log('call storage.clear fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### storage.delete

delete(options: DeleteStorageOptions): void

删除缓存中索引对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [DeleteStorageOptions](#deletestorageoptions) | 是 | 接口配置信息。 |

**示例：**

```js
export default {
  storageDelete() {
    storage.delete({
      key: 'Storage1',
      success: function() {
        console.log('call storage.delete success.');
      },
      fail: function(data, code) {
        console.log('call storage.delete fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### GetStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 内容索引。 |
| default | string | 否 | key不存在则返回的默认值。 |
| success | (data: any) => void | 否 | 接口调用成功的回调函数，data为返回key对应的value。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

#### SetStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要修改的存储值的索引。 |
| value | string | 是 | 新值。长度需小于128字节。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

#### ClearStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

#### DeleteStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 内容索引。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |
