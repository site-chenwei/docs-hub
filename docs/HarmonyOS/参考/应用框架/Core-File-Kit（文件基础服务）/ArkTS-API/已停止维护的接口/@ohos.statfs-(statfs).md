---
title: "@ohos.statfs (statfs)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statfs"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.statfs (statfs)"
captured_at: "2026-04-17T01:48:14.098Z"
---

# @ohos.statfs (statfs)

该模块提供文件系统相关存储信息的功能，向应用程序提供获取文件系统总字节数、空闲字节数的ArkTS接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/t13ERnoNRlSVY-85gp-Zrg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=5DDD247206BB9EEA61571CAF773790EC306E119EE1BA643E17C6E076FD64D7E5)

-   本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块从API version 9开始废弃，建议使用[@ohos.file.statvfs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-statvfs)替代。

#### 导入模块

```ts
import statfs from '@ohos.statfs';
```

#### Statfs.getFreeBytes

getFreeBytes(path:string):Promise<number>

异步方法获取指定文件系统空闲字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 需要查询的文件系统的文件路径 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 返回空闲字节数 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let path = "/dev";
statfs.getFreeBytes(path).then((number: number) => {
  console.info("getFreeBytes promise successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getFreeBytes failed with error:" + JSON.stringify(err));
});
```

#### Statfs.getFreeBytes

getFreeBytes(path:string, callback:AsyncCallback<number>): void

异步方法获取指定文件系统空闲字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 需要查询的文件系统的文件路径 |
| callback | AsyncCallback<number> | 是 | 异步获取空闲字节数之后的回调 |

**示例：**

```ts
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getFreeBytes(path, (err: BusinessError, freeBytes:Number) => {
    if (err) {
        console.error('getFreeBytes callback failed');
    } else {
        console.info('getFreeBytes callback success' + freeBytes);
    }
});
```

#### Statfs.getTotalBytes

getTotalBytes(path: string): Promise<number>

异步方法获取指定文件系统总字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 需要查询的文件系统的文件路径 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 返回总字节数 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let path = "/dev";
statfs.getTotalBytes(path).then((number: number) => {
  console.info("getTotalBytes promise successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getTotalBytes failed with error:" + JSON.stringify(err));
});
```

#### Statfs.getTotalBytes

getTotalBytes(path: string, callback: AsyncCallback<number>): void

异步方法获取指定文件系统总字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 需要查询的文件系统的文件路径 |
| callback | AsyncCallback<number> | 是 | 异步获取总字节数之后的回调 |

**示例：**

```ts
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalBytes(path, (err: BusinessError, totalBytes:Number) => {
    if (err) {
        console.error('getTotalBytes callback failed');
    } else {
        console.info('getTotalBytes callback success' + totalBytes);
    }
});
```
