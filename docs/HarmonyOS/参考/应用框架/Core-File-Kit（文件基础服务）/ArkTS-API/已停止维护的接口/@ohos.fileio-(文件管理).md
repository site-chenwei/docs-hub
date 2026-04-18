---
title: "@ohos.fileio (文件管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileio"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.fileio (文件管理)"
captured_at: "2026-04-17T01:48:14.246Z"
---

# @ohos.fileio (文件管理)

该模块提供文件存储管理能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xBunrzn0R-SZTqWTWLm2HQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=325DEA35AC931B9B665EF4C597853B4F905E16284FBB045D73D008F4BF9C5952)

-   本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块从API version 9开始废弃，建议使用[@ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)替代。

#### 导入模块

```ts
import fileio from '@ohos.fileio';
```

#### 使用说明

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```ts
 import UIAbility from '@ohos.app.ability.UIAbility';
 import window from '@ohos.window';

 export default class EntryAbility extends UIAbility {
   onWindowStageCreate(windowStage: window.WindowStage) {
     let context = this.context;
     let pathDir = context.filesDir;
   }
 }
```

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：[应用上下文Context-获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取应用文件路径)

#### fileio.stat

stat(path: string): Promise<Stat>

获取文件信息，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/-WCGM3qNRli0wvejdYHpSQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BC6A0C3FB8F207F45909B18C48043A1CAB2FD7CD1B1281EAFA1288C96E8BA9E9)

从API version 9开始废弃，请使用[fileIo.stat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiostat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise对象。返回文件的具体信息。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "test.txt";
fileio.stat(filePath).then((stat: fileio.Stat) => {
  console.info("getFileInfo succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("getFileInfo failed with error:" + err);
});
```

#### fileio.stat

stat(path: string, callback: AsyncCallback<Stat>): void

获取文件信息，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ePVRpR2SSX-UPHmQpJe2yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=123C627DC9390A95FCD4CE53D3C07D4B36C9D807E154A8DC8331AD2D444B82E9)

从API version 9开始废弃，请使用[fileIo.stat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiostat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |
| callback | AsyncCallback<[Stat](#stat)\> | 是 | 异步获取文件的信息之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
fileio.stat(pathDir, (err: BusinessError, stat: fileio.Stat) => {
  // example code in Stat
});
```

#### fileio.statSync

statSync(path: string): Stat

以同步方法获取文件的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/6vCIT661SDKbHaqJ2ZxLEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=62875A47DA39F2D3E53C976D14AA5ABE1F0F5E97E7BABF4349D699F16F7D688C)

从API version 9开始废弃，请使用[fileIo.statSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiostatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Stat](#stat) | 表示文件的具体信息。 |

**示例：**

```ts
let stat = fileio.statSync(pathDir);
// example code in Stat
```

#### fileio.opendir

opendir(path: string): Promise<Dir>

打开文件目录，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/i_kC7lroRdOiPPahzIk9fg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=E28CBC150F5440381DCD6E47083E1C6098A7A6B72F9D5D315B7FD3A0CB261037)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Dir](#dir)\> | Promise对象。返回Dir对象。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + "/testDir";
fileio.opendir(dirPath).then((dir: fileio.Dir) => {
  console.info("opendir succeed");
}).catch((err: BusinessError) => {
  console.error("opendir failed with error:" + err);
});
```

#### fileio.opendir

opendir(path: string, callback: AsyncCallback<Dir>): void

打开文件目录，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/TxpGHsAmRK6EqPo5p4YHqQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=DF8E8415466F24B5637881127C789E86A6C64A5150A1997A9AB5F002B0DC6238)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |
| callback | AsyncCallback<[Dir](#dir)\> | 是 | 异步打开文件目录之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
fileio.opendir(pathDir, (err: BusinessError, dir: fileio.Dir) => {
  // example code in Dir struct
  // use read/readSync/close
});
```

#### fileio.opendirSync

opendirSync(path: string): Dir

以同步方法打开文件目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/q7_5Ew7_Rkif7AMCCXdcgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7C0E878FE461C06F5448CDB341133742778A8063939CA9C71562ADF6666313F5)

从API version 9开始废弃，请使用[fileIo.listFileSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Dir](#dir) | 返回Dir对象。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
// example code in Dir struct
// use read/readSync/close
```

#### fileio.access

access(path: string, mode?: number): Promise<void>

检查当前进程是否可访问某文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/FhSjhdOZSWCoHO523cNu5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=0D4ABD7FA5BD5BCCE4581DF3FAB2FF14AB04A712AAEAE1350F277ED95CF0801D)

从API version 9开始废弃，请使用[fileIo.access](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioaccess)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 
访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。

确认当前进程是否具有对应权限：

\- 0：确认文件是否存在。

\- 1：确认当前进程是否具有可执行权限。

\- 2：确认当前进程是否具有写权限。

\- 4：确认当前进程是否具有读权限。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath).then(() => {
  console.info("access succeed");
}).catch((err: BusinessError) => {
  console.error("access failed with error:" + err);
});
```

#### fileio.access

access(path: string, mode?: number, callback: AsyncCallback<void>): void

检查当前进程是否可访问某文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/pak3O7M7TtCay47_6fxBVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=C04C166FD582568488C5D67EE3C961F61EB86596649A24BB364638BA1BE16F05)

从API version 9开始废弃，请使用[fileIo.access](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioaccess-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 
访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。

确认当前进程是否具有对应权限：

\- 0：确认文件是否存在。

\- 1：确认当前进程是否具有可执行权限。

\- 2：确认当前进程是否具有写权限。

\- 4：确认当前进程是否具有读权限。

 |
| callback | AsyncCallback<void> | 是 | 异步检查当前进程是否可访问某文件之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath, (err: BusinessError) => {
  // do something
});
```

#### fileio.accessSync

accessSync(path: string, mode?: number): void

以同步方法检查当前进程是否可访问某文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Q07P_KIdT9GZLKkhDENH4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=1906366BAB9E760B6F1618771EC8C78F741FA2131C1E52FAE804541B250C71D9)

从API version 9开始废弃，请使用[fileIo.accessSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioaccesssync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 
访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。

确认当前进程是否具有对应权限：

\- 0：确认文件是否存在。

\- 1：确认当前进程是否具有可执行权限。

\- 2：确认当前进程是否具有写权限。

\- 4：确认当前进程是否具有读权限。

 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
try {
  fileio.accessSync(filePath);
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error:" + err);
}
```

#### fileio.close7+

close(fd: number): Promise<void>

关闭文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/_6KzHEUBQby-8jV84OFKVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A232D08C9900D7F4EC40683BE5C2BD41564E95686C65B94A66EB7EAC6D2D3C72)

从API version 9开始废弃，请使用[fileIo.close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioclose)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待关闭文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error:" + err);
});
```

#### fileio.close7+

close(fd: number, callback: AsyncCallback<void>): void

关闭文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/IsiR863uR4GKIP75nEiqEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=6B1DB0EAE0254342E9C4F1411D19818E29886DBD46FA56B4B8158C23F2570734)

从API version 9开始废弃，请使用[fileIo.close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioclose-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待关闭文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步关闭文件之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.closeSync

closeSync(fd: number): void

以同步方法关闭文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/WiRvhch7QXO5ZYaEriIXuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9E42BA398D85BF0F87B909B136235A371D24C6E10B9A3DA5917B4D77C92E8B7F)

从API version 9开始废弃，请使用[fileIo.closeSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioclosesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待关闭文件的文件描述符。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.closeSync(fd);
```

#### fileio.copyFile

copyFile(src: string|number, dest: string|number, mode?: number): Promise<void>

复制文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/-FO6_YzpQPC_0jDRsitpFA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=476B2965166FC06E112E9CAD3FC2788FFA807195E9C228E3D2DE00EE654315B6)

从API version 9开始废弃，请使用[fileIo.copyFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocopyfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | 
mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath).then(() => {
  console.info("copyFile succeed");
}).catch((err: BusinessError) => {
  console.error("copyFile failed with error:" + err);
});
```

#### fileio.copyFile

copyFile(src: string|number, dest: string|number, mode: number, callback: AsyncCallback<void>): void

复制文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ILVG6m3iTHCccbVnC_i-mw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=02AD55A945B3C66EEB3549835E8E7F3B2E44829F45D7A965017F2E2D4A7EF196)

从API version 9开始废弃，请使用[fileIo.copyFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocopyfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | 
mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

 |
| callback | AsyncCallback<void> | 是 | 异步复制文件之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath, (err: BusinessError) => {
  // do something
});
```

#### fileio.copyFileSync

copyFileSync(src: string|number, dest: string|number, mode?: number): void

以同步方法复制文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Z3NxK3coQHWtVlroJSozpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=EAEB9A19376C4684962829798EB2CFC5887EBA6C30C5D8146C9AC9D711FFD496)

从API version 9开始废弃，请使用[fileIo.copyFileSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocopyfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | 
mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

 |

**示例：**

```ts
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFileSync(srcPath, dstPath);
```

#### fileio.mkdir

mkdir(path: string, mode?: number): Promise<void>

创建目录，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/uWB-TTWYQtWlMDbZ9c-glQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=64F7F72C142B5E313E0D1709FBD7D5DAA61809E55C60C27035C5CB96E588CF1D)

从API version 9开始废弃，请使用[fileIo.mkdir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomkdir)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 
创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。

\- 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((error: BusinessError) => {
  console.error("mkdir failed with error:" + error);
});
```

#### fileio.mkdir

mkdir(path: string, mode: number, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Pe1y9CcWTQqCYMku1MvgBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=F822BCB122C65DC2CBB4172E9E69940D859766300CA114E3C6D2BC672ADEBF40)

从API version 9开始废弃，请使用[fileIo.mkdir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomkdir-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 
创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。

\- 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |
| callback | AsyncCallback<void> | 是 | 异步创建目录操作完成之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath, (err: BusinessError) => {
  console.info("mkdir succeed");
});
```

#### fileio.mkdirSync

mkdirSync(path: string, mode?: number): void

以同步方法创建目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/tv34DU4yQa-2ZCUDgwpIaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=833D1E05F121646B81EAC6A7CB32F2C5DFB8A9C4FD383AF0589365604194FF1A)

从API version 9开始废弃，请使用[fileIo.mkdirSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomkdirsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 
创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。

\- 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |

**示例：**

```ts
let dirPath = pathDir + '/testDir';
fileio.mkdirSync(dirPath);
```

#### fileio.open7+

open(path: string, flags?: number, mode?: number): Promise<number>

打开文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/gLD1xPX-Tq2PI7-2elVzvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=525076138A830C2A6A9DB07E40E8B07B88F356E0EBB5C2C6CC77C9304CFC95AF)

从API version 9开始废弃，请使用[fileIo.open](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopen)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 
打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：

\- 0o0：只读打开。

\- 0o1：只写打开。

\- 0o2：读写打开。

同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项：

\- 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。

\- 0o200：如果追加了0o100选项，且文件已经存在，则出错。

\- 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。

\- 0o2000：以追加方式打开，后续写将追加到文件末尾。

\- 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- 0o200000：如果path不指向目录，则出错。

\- 0o400000：如果path指向符号链接，则出错。

\- 0o4010000：以同步IO的方式打开文件。

 |
| mode | number | 否 | 

若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。

\- 0o660：所有者具有读、写权限，所有用户组具有读、写权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回打开文件的文件描述符。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.open(filePath, 0o1, 0o0200).then((number: number) => {
  console.info("open file succeed");
}).catch((err: BusinessError) => {
  console.error("open file failed with error:" + err);
});
```

#### fileio.open7+

open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void

打开文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/VGU8VcTyRIat3OaLuY6uvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=1773DEFD16AE676D4AED11634B12FB7B487C1E6A62ECA220F73154EA1812335D)

从API version 9开始废弃，请使用[fileIo.open](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopen-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 
打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：

\- 0o0：只读打开。

\- 0o1：只写打开。

\- 0o2：读写打开。

同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项：

\- 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。

\- 0o200：如果追加了0o100选项，且文件已经存在，则出错。

\- 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。

\- 0o2000：以追加方式打开，后续写将追加到文件末尾。

\- 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- 0o200000：如果path不指向目录，则出错。

\- 0o400000：如果path指向符号链接，则出错。

\- 0o4010000：以同步IO的方式打开文件。

 |
| mode | number | 否 | 

若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。

\- 0o660：所有者具有读、写权限，所有用户组具有读、写权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |
| callback | AsyncCallback<number> | 是 | 异步打开文件之后的回调，返回打开文件的文件描述符。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.open(filePath, 0, (err: BusinessError, fd: number) => {
  // do something
});
```

#### fileio.openSync

openSync(path: string, flags?: number, mode?: number): number

以同步方法打开文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/CF6RM7QoSuOVdftm6ruC-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=F5CE7A47981F66F52364A40A95A0094CBE8F63B90A0C62D3863FD065D77FD454)

从API version 9开始废弃，请使用[fileIo.openSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopensync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 
打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：

\- 0o0：只读打开。

\- 0o1：只写打开。

\- 0o2：读写打开。

同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项：

\- 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。

\- 0o200：如果追加了0o100选项，且文件已经存在，则出错。

\- 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。

\- 0o2000：以追加方式打开，后续写将追加到文件末尾。

\- 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- 0o200000：如果path不指向目录，则出错。

\- 0o400000：如果path指向符号链接，则出错。

\- 0o4010000：以同步IO的方式打开文件。

 |
| mode | number | 否 | 

若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。

\- 0o660：所有者具有读、写权限，所有用户组具有读、写权限。

\- 0o640：所有者具有读、写权限，所有用户组具有读权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

创建出的文件权限受umask影响，umask随进程启动确定，其修改当前不开放。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 打开文件的文件描述符。 |

#### fileio.read

read(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): Promise<ReadOut>

从文件读取数据，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/fZ2bn0YDTMOzjoLf7yWpEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=D75DD1D2B01A1C67D37A69E8EC7327D2F3646648B399AD183F5A8DB9815C9755)

从API version 9开始废弃，请使用[fileIo.read](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioread)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。

\- position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读，单位为Byte。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ReadOut](#readout)\> | Promise对象。返回读取的结果。 |

#### fileio.read

read(fd: number, buffer: ArrayBuffer, options: { offset?: number; length?: number; position?: number; }, callback: AsyncCallback<ReadOut>): void

从文件读取数据，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/TuVf_Pu7SoeJMBfasQ7UJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BE03E1E8FDCE92F19C896EC04CC4B957012D7F50AB0B8BFA52515A2CD33850E8)

从API version 9开始废弃，请使用[fileIo.read](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioread-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示将数据读取到缓冲区的位置，单位为Byte，即相对于缓冲区首地址的偏移。可选，默认为0。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

约束：offset+length<=buffer.size。

 |
| callback | AsyncCallback<[ReadOut](#readout)\> | 是 | 异步读取数据之后的回调。 |

#### fileio.readSync

readSync(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): number

以同步方法从文件读取数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/qctIxix_TaCIu-j5yUDXIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=DCE81483F6951B5F54D6FE7FF90F45B7B73ABFD25729874C9540C5E5D94B9923)

从API version 9开始废弃，请使用[fileIo.readSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioreadsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。

\- position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读，单位为Byte。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际读取的长度，单位为Byte。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o2);
let buf = new ArrayBuffer(4096);
let num = fileio.readSync(fd, buf);
```

#### fileio.rmdir7+

rmdir(path: string): Promise<void>

删除目录，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/jLmbRHxHSRy9jJeSqQri_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=DA0C4E9BD027852A43176F5CB17F4C63DCD299FD228255013CF7CD4B1290C7DE)

从API version 9开始废弃，请使用[fileIo.rmdir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiormdir)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.rmdir(dirPath).then(() => {
  console.info("rmdir succeed");
}).catch((err: BusinessError) => {
  console.error("rmdir failed with error:" + err);
});
```

#### fileio.rmdir7+

rmdir(path: string, callback: AsyncCallback<void>): void

删除目录，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/kAUdLI4ESfiyheF6o0S_yg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=917F266B6CC4AAD81E2E75329BFB951D6F9C707875F1BF07DBE9002AEEBA48E5)

从API version 9开始废弃，请使用[fileIo.rmdir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiormdir-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除目录之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.rmdir(dirPath, (err: BusinessError) => {
  // do something
  console.info("rmdir succeed");
});
```

#### fileio.rmdirSync7+

rmdirSync(path: string): void

以同步方法删除目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/rZZ7JDoyRhSOqdqoiDaoyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=E9FCEBB9588395AD27D50EC8A62EB267F75ED7BF8045CB6F52B470463A3D75FF)

从API version 9开始废弃，请使用[fileIo.rmdirSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiormdirsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |

**示例：**

```ts
let dirPath = pathDir + '/testDir';
fileio.rmdirSync(dirPath);
```

#### fileio.unlink

unlink(path: string): Promise<void>

删除文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/95LGXZTXTyqEuVh7xP9Hyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9E29400D8953CC8EB4FA5CFA1E0F31715C84BE0B9175963E66AB81BE5AE4FBCF)

从API version 9开始废弃，请使用[fileIo.unlink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiounlink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.unlink(filePath).then(() => {
  console.info("remove file succeed");
}).catch((error: BusinessError) => {
  console.error("remove file failed with error:" + error);
});
```

#### fileio.unlink

unlink(path: string, callback: AsyncCallback<void>): void

删除文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/SPAqbBcLQI6we3lzYqGu0Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=4ED32D51C5F151FA29E80E03CB73A6E40C588CC7DC1A57BF7A67F0282AEA8727)

从API version 9开始废弃，请使用[fileIo.unlink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiounlink-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除文件之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.unlink(filePath, (err: BusinessError) => {
  console.info("remove file succeed");
});
```

#### fileio.unlinkSync

unlinkSync(path: string): void

以同步方法删除文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/QwOEgAeiTSCoYUo8vuNN4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7B035931460C238178B9B752D450A30F5BC0C1A449DD8EB50EEA486CF1A7E702)

从API version 9开始废弃，请使用[fileIo.unlinkSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiounlinksync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
fileio.unlinkSync(filePath);
```

#### fileio.write

write(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

将数据写入文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/e_3qsx-qRJqwP483EVm4iw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=1E7642D205081E66F39BD3CCA5D79099626995B85BDF12D0FD9921AC3A039CDE)

从API version 9开始废弃，请使用[fileIo.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiowrite)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world").then((number: number) => {
  console.info("write data to file succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error:" + err);
});
```

#### fileio.write

write(fd: number, buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/sMt6tCSxRq66gjcgAz7ovA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=B01DF94BB63EDC3D8210C529390DA03AA51F3E38B39A2F3932A09C7BAD29F3EF)

从API version 9开始废弃，请使用[fileIo.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiowrite-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

约束：offset+length<=buffer.size。

 |
| callback | AsyncCallback<number> | 是 | 异步将数据写入完成后执行的回调函数。返回实际写入的长度，单位为Byte。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world", (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    console.info("write data to file succeed and size is:" + bytesWritten);
  }
});
```

#### fileio.writeSync

writeSync(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

以同步方法将数据写入文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/UaQbe7fLTpqsJ9PJD-6AuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=D709036413418FC305C45D18BFC492303D0333D8FDBD5B2D6E249D0E08823585)

从API version 9开始废弃，请使用[fileIo.writeSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiowritesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际写入的长度，单位为Byte。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
let num = fileio.writeSync(fd, "hello, world");
```

#### fileio.hash

hash(path: string, algorithm: string): Promise<string>

计算文件的哈希值，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/SFjfQPRtSu-tPeli7uLx6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=2B5658D3AC65CB1755DB36AE147FC53FD344EE32614E4F67E9A2AE85C950516B)

从API version 9开始废弃，请使用[hash.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-hash#hashhash)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象。返回文件的哈希值。表示为十六进制数字串，所有字母均大写。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256").then((str: string) => {
  console.info("calculate file hash succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("calculate file hash failed with error:" + err);
});
```

#### fileio.hash

hash(path: string, algorithm: string, callback: AsyncCallback<string>): void

计算文件的哈希值，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/XXutsEM8ThCHnp-QD4c4jg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=2639A96C61F079916590D5F07AC3DD5CD329DBC6EC612E934F84B28DB2FB459E)

从API version 9开始废弃，请使用[hash.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-hash#hashhash-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |
| callback | AsyncCallback<string> | 是 | 异步计算文件哈希操作之后的回调函数（其中给定文件哈希值表示为十六进制数字串，所有字母均大写）。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256", (err: BusinessError, hashStr: string) => {
  if (hashStr) {
    console.info("calculate file hash succeed:" + hashStr);
  }
});
```

#### fileio.chmod7+

chmod(path: string, mode: number): Promise<void>

改变文件权限，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/c_zLoZRjSbKf9xh1g84Wzw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=2140D15EE886C42EA67C685ECCE42C0BCFAEA99CCCEF2B06E9D1C69414662386)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 
改变文件权限，可给定如下权限，以按位或的方式追加权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.chmod(filePath, 0o700).then(() => {
  console.info("chmod succeed");
}).catch((err: BusinessError) => {
  console.error("chmod failed with error:" + err);
});
```

#### fileio.chmod7+

chmod(path: string, mode: number, callback: AsyncCallback<void>): void

改变文件权限，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/LkjeMWL_QcKW8h11kU-E8Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=D44C024A80EA6241488551CEE2078BEAE823C7D268145C4EF452F2DEBA565F64)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 
改变文件权限，可给定如下权限，以按位或的方式追加权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |
| callback | AsyncCallback<void> | 是 | 异步改变文件权限之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.chmod(filePath, 0o700, (err: BusinessError) => {
  // do something
});
```

#### fileio.chmodSync7+

chmodSync(path: string, mode: number): void

以同步方法改变文件权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/rm0iSXSMQHGjqOE35PdnHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=31B261C0BE8AA5BD39CE3C202C2F4F89A0BA777CA63C84B21E69AEC8C5865B15)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 
改变文件权限，可给定如下权限，以按位或的方式追加权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
fileio.chmodSync(filePath, 0o700);
```

#### fileio.fstat7+

fstat(fd: number): Promise<Stat>

基于文件描述符获取文件状态信息，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/lYR59KDwS7-iEmb-813SuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=37F409B55ADBAB281FECC06DEC2986867861BBD9BC07C902FC3533963F277064)

从API version 9开始废弃，请使用[fileIo.stat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiostat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise对象。返回表示文件状态的具体信息。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fstat(fd).then((stat: fileio.Stat) => {
  console.info("fstat succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("fstat failed with error:" + err);
});
```

#### fileio.fstat7+

fstat(fd: number, callback: AsyncCallback<Stat>): void

基于文件描述符获取文件状态信息，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/HqiP6mJrRFWg_b6DYzlPqQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7B853E0534EB5DC034077ABFBA391EB4F3427B02CBEE83754C38DEF2FB60BA02)

从API version 9开始废弃，请使用[fileIo.stat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiostat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |
| callback | AsyncCallback<[Stat](#stat)\> | 是 | 异步获取文件状态信息之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fstat(fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.fstatSync7+

fstatSync(fd: number): Stat

以同步方法基于文件描述符获取文件状态信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/C3UTJyS8SjurmxP9qrk6jA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=C8FE7418023D371EB90D954DEE9AAA6C843A189D0AA7478F10B13459E44688A9)

从API version 9开始废弃，请使用[fileIo.statSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiostatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Stat](#stat) | 表示文件状态的具体信息。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.fstatSync(fd);
```

#### fileio.ftruncate7+

ftruncate(fd: number, len?: number): Promise<void>

基于文件描述符截断文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/scLYmRjGS_OeYiIjHBl0tw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=D927F191CC2BFDBF51D05B8E64CE268D0F9D54FB45F1F78BEED4C726C142D2B8)

从API version 9开始废弃，请使用[fileIo.truncate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiotruncate)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.ftruncate(fd, 5).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error:" + err);
});
```

#### fileio.ftruncate7+

ftruncate(fd: number, len?: number, callback: AsyncCallback<void>): void

基于文件描述符截断文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/pzCIY1p3Q2qLPd8G2gWESA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=F11A40001567827FC3E95888CF7BC438891B42D20478A869E7BA26037D945BBB)

从API version 9开始废弃，请使用[fileIo.truncate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiotruncate-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let len = 5;
fileio.ftruncate(fd, 5, (err: BusinessError) => {
  // do something
});
```

#### fileio.ftruncateSync7+

ftruncateSync(fd: number, len?: number): void

以同步方法基于文件描述符截断文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/of7sljmbRdS5Nx9ui-dIkw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=4A4338892B0C81380995C995C1362CF19E3E19E50CC8091883BD63ABC6B5A3DC)

从API version 9开始废弃，请使用[fileIo.truncateSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiotruncatesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let len = 5;
fileio.ftruncateSync(fd, len);
```

#### fileio.truncate7+

truncate(path: string, len?: number): Promise<void>

基于文件路径截断文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/NSmCSGVEQmSZlAI1LNtG9w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=C6C3FB468626538FA6054228DD4EBBE4E47B53C6518733975BEC343434F66573)

从API version 9开始废弃，请使用[fileIo.truncate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiotruncate)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncate(filePath, len).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error:" + err);
});
```

#### fileio.truncate7+

truncate(path: string, len?: number, callback: AsyncCallback<void>): void

基于文件路径截断文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/RuH98n6qS2yb3lX9GUfNcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=255AB9158840B6D7989CB71AA02EAE408B1590354E5ECB2C1E31647AC3BD7B1D)

从API version 9开始废弃，请使用[fileIo.truncate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiotruncate-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncate(filePath, len, (err: BusinessError) => {
  // do something
});
```

#### fileio.truncateSync7+

truncateSync(path: string, len?: number): void

以同步方法基于文件路径截断文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/zSThiOc0ThyHC9XA_JoldA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=66F7C53FA1DCA29318B81A6B05653BC5BA666B91E61F187EA80CC646A6F2DD5A)

从API version 9开始废弃，请使用[fileIo.truncateSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiotruncatesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncateSync(filePath, len);
```

#### fileio.readText7+

readText(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): Promise<string>

基于文本方式读取文件（即直接读取文件的文本内容），使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/1n6biX3RRTerdHgk12fj6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7CC2458B97C974667CB919B74C50DAE9991174186F23CDB6130A6DFB7CD769C8)

从API version 9开始废弃，请使用[fileIo.readText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioreadtext)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 
支持如下选项：

\- position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象。返回读取文件的内容。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.readText(filePath).then((str: string) => {
  console.info("readText succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("readText failed with error:" + err);
});
```

#### fileio.readText7+

readText(filePath: string, options: { position?: number; length?: number; encoding?: string; }, callback: AsyncCallback<string>): void

基于文本方式读取文件（即直接读取文件的文本内容），使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/r49ifL27QDOQJqUCVMbzkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9CB369C1E11280CA5DB8D1999378FD02583CBA4E580A0693D4D3E2B7A33A0FFD)

从API version 9开始废弃，请使用[fileIo.readText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioreadtext-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 
支持如下选项：

\- position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- encoding，string类型，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回读取文件的内容。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
class Option {
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.position = 1;
option.encoding = 'utf-8';
fileio.readText(filePath, option, (err: BusinessError, str: string) => {
  // do something
});
```

#### fileio.readTextSync7+

readTextSync(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): string

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/1kZPoCcDRXaeld-A6PC7xQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=CADFAAE961ADEBE600F7B5C76532FE1D6C8E89B4E3A86806B861D238B4CCBF2B)

从API version 9开始废弃，请使用[fileIo.readTextSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioreadtextsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 
支持如下选项：

\- position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回读取文件的内容。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
class Option {
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.position = 1;
option.length = 3;
let str = fileio.readTextSync(filePath, option);
```

#### fileio.lstat7+

lstat(path: string): Promise<Stat>

获取链接信息，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/LLltDtAvQh-Wj0yZfILzrQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7C0A1B4183C3496E1CBAA49D8A41B26B66A1DFC6E0DE4E75C4442AFD2AB663EA)

从API version 9开始废弃，请使用[fileIo.lstat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolstat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目标文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Stat](#stat)\> | promise对象，返回文件对象，表示文件的具体信息，详情见stat。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.lstat(filePath).then((stat: fileio.Stat) => {
  console.info("get link status succeed, the size of file is" + stat.size);
}).catch((err: BusinessError) => {
  console.error("get link status failed with error:" + err);
});
```

#### fileio.lstat7+

lstat(path: string, callback: AsyncCallback<Stat>): void

获取链接信息，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/341R9xLfTiC3h-BLcr1Vzg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A777960617E32049C2A82CFAE4C0103DC13E902EA2FAD527D6BB1303D0F23B08)

从API version 9开始废弃，请使用[fileIo.lstat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolstat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目标文件的应用沙箱路径。 |
| callback | AsyncCallback<[Stat](#stat)\> | 是 | 回调函数，返回文件的具体信息。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.lstat(filePath, (err: BusinessError, stat: fileio.Stat) => {
  // do something
});
```

#### fileio.lstatSync7+

lstatSync(path: string): Stat

以同步方法获取链接信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/ZTnOquonR7GDBippVU3g3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=03E3DD06B4E63473BFCA1CB2DC1FD38D2E4272081150BBFB4E0A24266F0B8A17)

从API version 9开始废弃，请使用[fileIo.lstatSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolstatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目标文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Stat](#stat) | 表示文件的具体信息。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let stat = fileio.lstatSync(filePath);
```

#### fileio.rename7+

rename(oldPath: string, newPath: string): Promise<void>

重命名文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/wc5qcK7JRheSekl7PbI11A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9D385D14C8F8268F9E9341FED799CE0108BD6B7291D105251539109785794620)

从API version 9开始废弃，请使用[fileIo.rename](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiorename)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile).then(() => {
  console.info("rename succeed");
}).catch((err: BusinessError) => {
  console.error("rename failed with error:" + err);
});
```

#### fileio.rename7+

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

重命名文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/nFrmS1SdTCevNQgNX9p6gA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=C32D6AFE64A8B964696D26A2A004D343A6346A709D64A4A176C9BB19FCF2CD42)

从API version 9开始废弃，请使用[fileIo.rename](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiorename-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步重命名文件之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile, (err: BusinessError) => {
});
```

#### fileio.renameSync7+

renameSync(oldPath: string, newPath: string): void

以同步方法重命名文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/mcUTqg7qQSegrdssOO7VzQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=107BFB200C38FDACF7E7B214C7D12E9B98CAFD6BF3E003B22A43936A1C49C60A)

从API version 9开始废弃，请使用[fileIo.renameSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiorenamesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |

**示例：**

```ts
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.renameSync(srcFile, dstFile);
```

#### fileio.fsync7+

fsync(fd: number): Promise<void>

同步文件数据，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/gA9fJoY1T5WwMLQq07r1pQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BCEDCB7F0FE3224BE34EF7A9A6DB6AB8B04744B6F62135F4CE854C29AF32F6D3)

从API version 9开始废弃，请使用[fileIo.fsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error:" + err);
});
```

#### fileio.fsync7+

fsync(fd: number, callback: AsyncCallback<void>): void

同步文件数据，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/zodN00iJRWma8gG2C7az5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=80A88C41C7A33387AF6C4DB78A13383A1FADFE74F091BDA26792A1E4FE38AC9C)

从API version 9开始废弃，请使用[fileIo.fsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofsync-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待同步文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件数据同步之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.fsyncSync7+

fsyncSync(fd: number): void

以同步方法同步文件数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/i2GWbFJ_TU2bOZl--ilqxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=95E89FCBDDE95E4BB7C197FE9809BEDBD2CEB6D13274A983588874A6E5AF0B6C)

从API version 9开始废弃，请使用[fileIo.fsyncSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofsyncsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsyncSync(fd);
```

#### fileio.fdatasync7+

fdatasync(fd: number): Promise<void>

实现文件内容数据同步，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/_jnXlfVeRj-BM9aAuo_hVg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BF67FD48EE2A8D775CF0BC08C3E5E9A2825C1F6B6B10D2B745A1069A33347B2D)

从API version 9开始废弃，请使用[fileIo.fdatasync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofdatasync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdatasync(fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error:" + err);
});
```

#### fileio.fdatasync7+

fdatasync(fd: number, callback: AsyncCallback<void>): void

实现文件内容数据同步，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/8n9zrc-6QOG6_4jAvp98XA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=B4C88D2339EE066FE4E41996A1FA9523C9D06A99E04C2ACC79F8245B717C6B1E)

从API version 9开始废弃，请使用[fileIo.fdatasync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofdatasync-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待同步文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件内容数据同步之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdatasync (fd, (err: BusinessError) => {
  // do something
});
```

#### fileio.fdatasyncSync7+

fdatasyncSync(fd: number): void

以同步方法实现文件内容数据同步。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/gvbRsjNwQvm-cDl0O_wzFg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7F4BEDB7584BC08EFF522A530A355D3F0CFF9896F0B958B8DF2D92120162F31F)

从API version 9开始废弃，请使用[fileIo.fdatasyncSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofdatasyncsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.fdatasyncSync(fd);
```

#### fileio.symlink7+

symlink(target: string, srcPath: string): Promise<void>

基于文件路径创建符号链接，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Wc8_H9QyT4qEhQuG9L9WlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=89A92023831AE7DBAA552DDE3E97368C9452153A891088D6C7842072AAE71943)

从API version 9开始废弃，请使用[fileIo.symlink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiosymlink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile).then(() => {
  console.info("symlink succeed");
}).catch((err: BusinessError) => {
  console.error("symlink failed with error:" + err);
});
```

#### fileio.symlink7+

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

基于文件路径创建符号链接，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/jkioIHMMS-ajjRwf9fOYew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9B6890E716C8D6678758AE4A5027FA05CA7F23FD91D6951C5DB85EB8ED369190)

从API version 9开始废弃，请使用[fileIo.symlink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiosymlink-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步创建符号链接信息之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile, (err: BusinessError) => {
  // do something
});
```

#### fileio.symlinkSync7+

symlinkSync(target: string, srcPath: string): void

以同步的方法基于文件路径创建符号链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/DE-Cj9hRT4el23dhVFUqxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=58DCDC355B3FFF672C0E2FC4F26C5DA04456AA93DBF222D5D7821C52AF39754A)

从API version 9开始废弃，请使用[fileIo.symlinkSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiosymlinksync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**示例：**

```ts
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlinkSync(srcFile, dstFile);
```

#### fileio.chown7+

chown(path: string, uid: number, gid: number): Promise<void>

基于文件路径改变文件所有者，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/D4ZkPDhHRTKUvbb-ROCA2A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=2B733BAA6B23CB6693BE6FEDC812213199923923DB006A247413453D8F704B06)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID（UserID）。 |
| gid | number | 是 | 新的GID（GroupID）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.chown(filePath, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});
```

#### fileio.chown7+

chown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件路径改变文件所有者，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/h_qdp6kqQ7-4XfBMUsll_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9587E06FA2FFC90A23D1BBB750641831E963B122CE0E691EF994F07415F2424A)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath)
fileio.chown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
  // do something
});
```

#### fileio.chownSync7+

chownSync(path: string, uid: number, gid: number): void

以同步的方法基于文件路径改变文件所有者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/eLFkTGWWQ2SBv_7KFEF3Ng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=AFDEB571D84611913BBBD275FE673BDAE63C8A26331AE18DE210F3DFA70B9A58)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath)
fileio.chownSync(filePath, stat.uid, stat.gid);
```

#### fileio.mkdtemp7+

mkdtemp(prefix: string): Promise<string>

创建临时目录，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/0t3RcBYeTBOiumO3vHIKqg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=FAD6490E8318242F4126924546A7C96EDBED3AFB47DCE09873AE6D749E184CDF)

从API version 9开始废弃，请使用[fileIo.mkdtemp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomkdtemp)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象。返回生成的唯一目录路径。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX").then((pathDir: string) => {
  console.info("mkdtemp succeed:" + pathDir);
}).catch((err: BusinessError) => {
  console.error("mkdtemp failed with error:" + err);
});
```

#### fileio.mkdtemp7+

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

创建临时目录，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/k68q2jwXRCW4M1beBpCLag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=307C83C1E2C03A3E71AC2ED9097164BE5364A26DE034809CEC65C48DBDAF1323)

从API version 9开始废弃，请使用[fileIo.mkdtemp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomkdtemp-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |
| callback | AsyncCallback<string> | 是 | 异步创建临时目录之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  // do something
});
```

#### fileio.mkdtempSync7+

mkdtempSync(prefix: string): string

以同步的方法创建临时目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/2mfq367rSoidJD_t0jrCfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=64CACCE7A46E694D8DE6D8460E83337FD729C3DC1CF38766E75B0AE06DF53993)

从API version 9开始废弃，请使用[fileIo.mkdtempSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomkdtempsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 产生的唯一目录路径。 |

**示例：**

```ts
let res = fileio.mkdtempSync(pathDir + "/XXXXXX");
```

#### fileio.fchmod7+

fchmod(fd: number, mode: number): Promise<void>

基于文件描述符改变文件权限，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/1ZJNhMPMSQmsJJ020FZ7TA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=D968F608C6B5E7D0B2A42CA88491D830268B0A3E5F734A281A59917A7816BDC3)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 
若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmod(fd, mode).then(() => {
  console.info("chmod succeed");
}).catch((err: BusinessError) => {
  console.error("chmod failed with error:" + err);
});
```

#### fileio.fchmod7+

fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void

基于文件描述符改变文件权限，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/cmxVv3azQ3CgnqHWKghU7A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=2E6A842344273ECFF817CDAA0F6F17BA432B661E69B87E80F94EED71ABE60038)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 
若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |
| callback | AsyncCallback<void> | 是 | 异步改变文件权限之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmod(fd, mode, (err: BusinessError) => {
  // do something
});
```

#### fileio.fchmodSync7+

fchmodSync(fd: number, mode: number): void

以同步方法基于文件描述符改变文件权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/P6wqaIwZTa65L-ftOzk1tA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=F4EE176BE7D53631363D8E6E741A3A07B7DF7273B113784A0F5F3949DE7328FD)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 
若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。

\- 0o700：所有者具有读、写及可执行权限。

\- 0o400：所有者具有读权限。

\- 0o200：所有者具有写权限。

\- 0o100：所有者具有可执行权限。

\- 0o070：所有用户组具有读、写及可执行权限。

\- 0o040：所有用户组具有读权限。

\- 0o020：所有用户组具有写权限。

\- 0o010：所有用户组具有可执行权限。

\- 0o007：其余用户具有读、写及可执行权限。

\- 0o004：其余用户具有读权限。

\- 0o002：其余用户具有写权限。

\- 0o001：其余用户具有可执行权限。

 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmodSync(fd, mode);
```

#### fileio.createStream7+

createStream(path: string, mode: string): Promise<Stream>

基于文件路径打开文件流，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/kDZbneLIThGKVlK1puXUTA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=EA70C99FEB7E0656C65F309E08AAAAA40F274860B5FE442CA423BDD51AF12C4B)

从API version 9开始废弃，请使用[fileIo.createStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocreatestream)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Stream](#stream)\> | Promise对象。返回文件流的结果。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.createStream(filePath, "r+").then((stream: fileio.Stream) => {
  console.info("createStream succeed");
}).catch((err: BusinessError) => {
  console.error("createStream failed with error:" + err);
});
```

#### fileio.createStream7+

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

基于文件路径打开文件流，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/rbwRStN-Qg-oxbcl4kN9FQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A2D29DC17E40DAA2D943DA32CCE816B9D9F557F7A60705ED6E38BD29207CC873)

从API version 9开始废弃，请使用[fileIo.createStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocreatestream-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |
| callback | AsyncCallback<[Stream](#stream)\> | 是 | 异步打开文件流之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.createStream(filePath, "r+", (err: BusinessError, stream: fileio.Stream) => {
  // do something
});
```

#### fileio.createStreamSync7+

createStreamSync(path: string, mode: string): Stream

以同步方法基于文件路径打开文件流。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/AAZ92ftrS6ufOEMnuLWXWw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7D6FB031EAD2C08F2A907E5CC11B851BA3E7C743066DC2DA82679F4FB2486A94)

从API version 9开始废弃，请使用[fileIo.createStreamSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocreatestreamsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Stream](#stream) | 返回文件流的结果。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
```

#### fileio.fdopenStream7+

fdopenStream(fd: number, mode: string): Promise<Stream>

基于文件描述符打开文件流，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/OQ8xzhWdRqGJneNxxQlygw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=1513639C186829413D55AD909B9BD74BEAF8DCA3C94A8A600A88407FACF6BB82)

从API version 9开始废弃，请使用[fileIo.fdopenStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofdopenstream)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Stream](#stream)\> | Promise对象。返回文件流的结果。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdopenStream(fd, "r+").then((stream: fileio.Stream) => {
  console.info("openStream succeed");
}).catch((err: BusinessError) => {
  console.error("openStream failed with error:" + err);
});
```

#### fileio.fdopenStream7+

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

基于文件描述符打开文件流，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/iCEq9AwUR9ugxmHb1Rp8mQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=318C4D85E390A484E03CFEEC8F2C6E2807779BFFC2C46DF02C78E95F1F3CF6BC)

从API version 9开始废弃，请使用[fileIo.fdopenStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofdopenstream-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |
| callback | AsyncCallback<[Stream](#stream)\> | 是 | 异步打开文件流之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdopenStream(fd, "r+", (err: BusinessError, stream: fileio.Stream) => {
  // do something
});
```

#### fileio.fdopenStreamSync7+

fdopenStreamSync(fd: number, mode: string): Stream

以同步方法基于文件描述符打开文件流。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/3LWuNh4yQ8Smb9IlDJfmng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=63AC3D7BB6E44CC842307237FF8AA15FF3A95D2CFD9A2D6CF1DAE7DB3E3F3F35)

从API version 9开始废弃，请使用[fileIo.fdopenStreamSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiofdopenstreamsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Stream](#stream) | 返回文件流的结果。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let ss = fileio.fdopenStreamSync(fd, "r+");
```

#### fileio.fchown7+

fchown(fd: number, uid: number, gid: number): Promise<void>

基于文件描述符改变文件所有者，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/0YtvQ7efT5O1dO4m07EaGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=104EE384575AA50B244D70ACCECCFB41121ED1B061B2A7612041B8335EAE4643)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchown(fd, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});
```

#### fileio.fchown7+

fchown(fd: number, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件描述符改变文件所有者，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/8W5Bbrp2SjK8QDcmDreu1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=D25942B2D090EA6E60FBB35E57BCE8A43D461E03EE56123901FD9C0B25210309)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchown(fd, stat.uid, stat.gid, (err: BusinessError) => {
  // do something
});
```

#### fileio.fchownSync7+

fchownSync(fd: number, uid: number, gid: number): void

以同步方法基于文件描述符改变文件所有者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/_77grXUBTbmpceyQgCVFAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=02C2918C1E44930B50A0A063E4934E68DFF141992E48B57C56B9E26720522414)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchownSync(fd, stat.uid, stat.gid);
```

#### fileio.lchown7+

lchown(path: string, uid: number, gid: number): Promise<void>

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是符号链接所指向的实际文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/dUJ51TQvTf6LeAKtznqk6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A8348D0417BFD7BC69ED9F454D2DAD135E68FB5DD00F1F7B612909DEDFADCFEF)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchown(filePath, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});
```

#### fileio.lchown7+

lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/r1RvbqQyS7adP9yk1DUkMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=970FA9FE9FB00B6FF286A29F96DF80820760D47D4053FEFD9500DC08622F49CD)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
  // do something
});
```

#### fileio.lchownSync7+

lchownSync(path: string, uid: number, gid: number): void

以同步方法基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/5WLvppWoRaShLBRfr-Ylvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A5CF06F56B6F584EE278A89234D97428C0B6C97B3E4D214372FB5F057BF2751F)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchownSync(filePath, stat.uid, stat.gid);
```

#### fileio.createWatcher7+

createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher

监听文件或者目录的变化，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/um7Zhxn1S-WYRQLkxgeaPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9404067833E0E165888C36DEC830B65872256826EC829C8C9B77B877DA688704)

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filename | string | 是 | 待监视文件的应用沙箱路径。 |
| events | number | 是 | 
\- 1: 监听文件或者目录是否发生重命名。

\- 2：监听文件或者目录内容的是否修改。

\- 3：两者都有。

 |
| callback | AsyncCallback<number> | 是 | 每发生变化一次，调用一次此函数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Watcher](#watcher7) | Promise对象。返回文件变化监听的实例。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
```

#### Readout

仅用于read方法，获取文件的读取结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/3aikfoYlSWeilJtXFWBYCw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=1E5403840ECBE2445E6C3DFBFDA143A724403D9E153CFC70E78B48EAA69BC7A3)

从API version 9开始废弃。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

| 名称 | 类型 | 只读 | 可写 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bytesRead | number | 是 | 是 | 实际读取长度，单位为Byte。 |
| offset | number | 是 | 是 | 读取数据相对于缓冲区首地址的偏移，单位为Byte。 |
| buffer | ArrayBuffer | 是 | 是 | 保存读取数据的缓冲区。 |

#### Stat

文件具体信息，在调用Stat的方法前，需要先通过[stat()](#fileiostat)方法（同步或异步）来构建一个Stat实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/btQUrO3TQXWuCQaH5XCUTg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=8EB8F1FFB581E86FD9CB77193C831E38E79B79DE9B72BD909DED54EA4B26DA56)

从API version 9开始废弃，请使用[fileIo.Stat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#stat)替代。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可写 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| dev | number | 是 | 否 | 标识包含该文件的主设备号。 |
| ino | number | 是 | 否 | 标识该文件。通常同设备上的不同文件的INO不同。 |
| mode | number | 是 | 否 | 
表示文件类型及权限，其首 4 位表示文件类型，后 12 位表示权限。各特征位的含义如下：

\- 0o170000：可用于获取文件类型的掩码。

\- 0o140000：文件是套接字。

\- 0o120000：文件是符号链接。

\- 0o100000：文件是一般文件。

\- 0o060000：文件属于块设备。

\- 0o040000：文件是目录。

\- 0o020000：文件是字符设备。

\- 0o010000：文件是命名管道，即FIFO。

\- 0o0700：可用于获取用户权限的掩码。

\- 0o0400：用户读，对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。

\- 0o0200：用户写，对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。

\- 0o0100：用户执行，对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。

\- 0o0070：可用于获取用户组权限的掩码。

\- 0o0040：用户组读，对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。

\- 0o0020：用户组写，对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。

\- 0o0010：用户组执行，对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。

\- 0o0007：可用于获取其他用户权限的掩码。

\- 0o0004：其他读，对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。

\- 0o0002：其他写，对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。

\- 0o0001：其他执行，对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。

 |
| nlink | number | 是 | 否 | 文件的硬链接数。 |
| uid | number | 是 | 否 | 文件所有者的ID。 |
| gid | number | 是 | 否 | 文件所有组的ID。 |
| rdev | number | 是 | 否 | 标识包含该文件的从设备号。 |
| size | number | 是 | 否 | 文件的大小，单位为Byte。仅对普通文件有效。 |
| blocks | number | 是 | 否 | 文件占用的块数，计算时块大小按512B计算。 |
| atime | number | 是 | 否 | 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| mtime | number | 是 | 否 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| ctime | number | 是 | 否 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。 |

#### \[h2\]isBlockDevice

isBlockDevice(): boolean

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/649ZpO46T_GDVw5HscM5bg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=4BCD815464CA4660D076D5527CAEA4CCE74D4450FBFBB658F925A9354972E16C)

从API version 9开始废弃，请使用[fileIo.Stat.isBlockDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#isblockdevice)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是块特殊设备。true为是，false为不是。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isBLockDevice = fileio.statSync(filePath).isBlockDevice();
```

#### \[h2\]isCharacterDevice

isCharacterDevice(): boolean

用于判断文件是否是字符特殊文件。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/qT5Ob_3TQ1C_FAxBF9xNXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=868A238C11DCA14653AC783B0BC73A55EA3BB6743DA88364EF4593B1AF54A401)

从API version 9开始废弃，请使用[fileIo.Stat.isCharacterDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#ischaracterdevice)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是字符特殊设备。true为是，false为不是。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isCharacterDevice = fileio.statSync(filePath).isCharacterDevice();
```

#### \[h2\]isDirectory

isDirectory(): boolean

用于判断文件是否是目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/K8K5WrWhSzGDYLlBWOaKoA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=3CDD8A18FFA876B7A29EB3C7F78A8C577839BA1B269920A3E45C97363D46051D)

从API version 9开始废弃，请使用[fileIo.Stat.isDirectory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#isdirectory)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是目录。true为是，false为不是。 |

**示例：**

```ts
let dirPath = pathDir + "/test";
let isDirectory = fileio.statSync(dirPath).isDirectory();
```

#### \[h2\]isFIFO

isFIFO(): boolean

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/MOq4cz1qSECEgrMVqivOJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=B6FFC6297AF31581024AA2872E7D6E5E36A9039714780E2A4B3BB22229290134)

从API version 9开始废弃，请使用[fileIo.Stat.isFIFO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#isfifo)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是 FIFO。true为是，false为不是。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isFIFO = fileio.statSync(filePath).isFIFO();
```

#### \[h2\]isFile

isFile(): boolean

用于判断文件是否是普通文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/6ZPTVlBPRnuHe4ffyr756g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=17A3D0BCD38FC0BE77B2DBADDCB671B00C6196ADF5283AABEDB4136E914730F8)

从API version 9开始废弃，请使用[fileIo.Stat.isFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#isfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是普通文件。true为是，false为不是。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isFile = fileio.statSync(filePath).isFile();
```

#### \[h2\]isSocket

isSocket(): boolean

用于判断文件是否是套接字。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/bLuJQEv8SQGvN0Y5nfv_-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=1121D79A290650111A731824274D244F7F79B2A7AF4F041EBBC53816E2098CF7)

从API version 9开始废弃，请使用[fileIo.Stat.isSocket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#issocket)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是套接字。true为是，false为不是。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isSocket = fileio.statSync(filePath).isSocket();
```

#### \[h2\]isSymbolicLink

isSymbolicLink(): boolean

用于判断文件是否是符号链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/GL5rNyL7RRa-An9J2hIZ_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=C36A4D5F949E3E43AFF7640D42FA72DFB7DF45F67AEC8C563548322843F6AE2D)

从API version 9开始废弃，请使用[fileIo.Stat.isSymbolicLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#issymboliclink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是符号链接。true为是，false为不是。 |

**示例：**

```ts
let filePath = pathDir + "/test";
let isSymbolicLink = fileio.statSync(filePath).isSymbolicLink();
```

#### Watcher7+

Watcher是文件变化监听的实例，调用Watcher.stop()方法（同步或异步）来停止文件监听。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/c0Gf_ilFT6C3wYPHiEMjbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=881B89E8B1D7DB2FD325B51D507B39691D0FA2DEEBFBB0A6DEE34BA6A4B54049)

从API version 10开始废弃。

#### \[h2\]stop7+

stop(): Promise<void>

关闭watcher监听，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/lB-RVSunTTu86q9nbY0W-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=26633D6774126F09C8CA0EE8B7C7AF845206CE853F6A608C91347D6BF3827A2C)

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
watcher.stop().then(() => {
  console.info("close watcher succeed");
});
```

#### \[h2\]stop7+

stop(callback: AsyncCallback<void>): void

关闭watcher监听，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/gudPI-_YRqu-7kI-ZWkpVg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A31626EBC6EC202E2E885BFA6C4FE3E46479A6DAA14BBDFB9055464757BB6D1F)

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 以异步方法关闭watcher监听之后的回调。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
watcher.stop(() => {
  console.info("close watcher succeed");
})
```

#### Stream

文件流，在调用Stream的方法前，需要先通过createStream()方法（同步或异步）来构建一个Stream实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Vw0AS5-GRHuealOoP45c9A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=41D5A1072EE1DFE09346BDC741B5073CD4B3FF53A385370DA9E92552D2011992)

从API version 9开始废弃，请使用[fileIo.Stream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#stream)替代。

#### \[h2\]close7+

close(): Promise<void>

关闭文件流，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/vZtcCLiOTjKufj5Brfac6w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=386A832ADAA97E23B33F5B2B910B51BC76861AD85161D438F0696B0E6C297DAF)

从API version 9开始废弃，请使用[fileIo.Stream.close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#close)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。返回表示异步关闭文件流的结果。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error:" + err);
});
```

#### \[h2\]close7+

close(callback: AsyncCallback<void>): void

异步关闭文件流，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/dWkOT8-hTGG55o0jHK62FQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=41CFD7B606A4AB5B8BBAA5547F1A717FD35081589105327AB927553444229C22)

从API version 9开始废弃，请使用[fileIo.Stream.close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#close-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 异步关闭文件流之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close((err: BusinessError) => {
  // do something
});
```

#### \[h2\]closeSync

closeSync(): void

同步关闭文件流。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/3kxepxxESxGjfr3ly1vO5Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=06262839D9D688A9E58A445D3C242D127A7ACAD56D182DA523235E7F24A66546)

从API version 9开始废弃，请使用[fileIo.Stream.closeSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#closesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.closeSync();
```

#### \[h2\]flush7+

flush(): Promise<void>

刷新文件流，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/UE9QEcArS-C9d3jkci0ixQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=087722228502F2DFA6C55F85A758C79F86388BE3F3CCE4E846FC67F23E84EE0F)

从API version 9开始废弃，请使用[fileIo.Stream.flush](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#flush)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。返回表示异步刷新文件流的结果。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush().then(() => {
  console.info("flush succeed");
}).catch((err: BusinessError) => {
  console.error("flush failed with error:" + err);
});
```

#### \[h2\]flush7+

flush(callback: AsyncCallback<void>): void

异步刷新文件流，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/XagfrdLLT5mTzvRMUfKFog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=791AC56032C10C2CC1AE99473A30F8B7AF37FD43846E0BA82AC2C594BD3D1926)

从API version 9开始废弃，请使用[fileIo.Stream.flush](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#flush-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 异步刷新文件流后的回调函数。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush((err: BusinessError) => {
  // do something
});
```

#### \[h2\]flushSync7+

flushSync(): void

同步刷新文件流。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/rxWkYMWNQrG8fY4_ow7yzw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=C7CF6D43402676B5FB9F00134481F7AE5203B63A15DB2F66390D9670660E3591)

从API version 9开始废弃，请使用[fileIo.Stream.flushSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#flushsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flushSync();
```

#### \[h2\]write7+

write(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

将数据写入流文件，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/dIYp0J0kT5i9CHaH2WhdvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=766AFDC1520790C2A0604B988D1482B3D99CFA2012434505E9D48BA836A1A919)

从API version 9开始废弃，请使用[fileIo.Stream.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#write)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option).then((number: number) => {
  console.info("write succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write failed with error:" + err);
});
```

#### \[h2\]write7+

write(buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

将数据写入流文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/4yt7-Y7YRnO6qG1tY7KQuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=99B420FE0E778C4A3AD4E2A8D987530003AE9098BFB589C77129876BA80FFF5E)

从API version 9开始废弃，请使用[fileIo.Stream.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#write-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

约束：offset+length<=buffer.size。

 |
| callback | AsyncCallback<number> | 是 | 异步写入完成后执行的回调函数，返回实际写入的长度，单位为Byte。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option, (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    // do something
    console.info("write succeed and size is:" + bytesWritten);
  }
});
```

#### \[h2\]writeSync7+

writeSync(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

以同步方法将数据写入流文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/TCcCtZ0vTt6wOq30ajDAOQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=60B46D3ECD65057349E7EE835CE3F1FB4F1EA715F9146C32CFA429EBCAC156AB)

从API version 9开始废弃，请使用[fileIo.Stream.writeSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#writesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际写入的长度，单位为Byte。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath,"r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let num = ss.writeSync("hello, world", option);
```

#### \[h2\]read7+

read(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): Promise<ReadOut>

从流文件读取数据，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Q50PKL83TEGuSvINdmYmEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=F3E56744D663DF60430702573A0747CB9B01AF50BDE1F5748EDC4E605BEECA20)

从API version 9开始废弃，请使用[fileIo.Stream.read](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#read)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。

\- position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读，单位为Byte。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ReadOut](#readout)\> | Promise对象。返回读取的结果。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option).then((readResult: fileio.ReadOut) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
  console.info(`The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error("read data failed with error:" + err);
});
```

#### \[h2\]read7+

read(buffer: ArrayBuffer, options: { position?: number; offset?: number; length?: number; }, callback: AsyncCallback<ReadOut>): void

从流文件读取数据，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/mH1mdttSQqSPWRRmP2IAog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=ECA5FC39DCD562D7C7A5A6F6B13D07F5AEC69A1428945104AC19A27B9CA517FA)

从API version 9开始废弃，请使用[fileIo.Stream.read](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#read-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。

\- position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

约束：offset+length<=buffer.size。

 |
| callback | AsyncCallback<[ReadOut](#readout)\> | 是 | 异步从流文件读取数据之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option, (err: BusinessError, readResult: fileio.ReadOut) => {
  if (readResult.bytesRead) {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
    console.info(`The content of file: ${buf.toString()}`);
  }
});
```

#### \[h2\]readSync7+

readSync(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): number

以同步方法从流文件读取数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/lxILdbThR7q449PxBWqMGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BDA21C5E86D8BCBCD3172E5271F5A10C857E9041CF4F3E3575E3F4780D5290E3)

从API version 9开始废弃，请使用[fileIo.Stream.readSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#readsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 
支持如下选项：

\- offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。

\- length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。

\- position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

约束：offset+length<=buffer.size。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际读取的长度，单位为Byte。 |

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let buf = new ArrayBuffer(4096)
let num = ss.readSync(buf, option);
```

#### Dir

管理目录，在调用Dir的方法前，需要先通过opendir方法（同步或异步）来构建一个Dir实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/qn8IpRQPRnGwjsv5nZAoYA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7F1AA1CB759C433F5AFF45C44F039E3BD22D68083115A240188987C2D16345D8)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile)替代。

#### \[h2\]read

read(): Promise<Dirent>

读取下一个目录项，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/IzbjVNESTiuCmJMwhD8T_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=185C1B2D2B9084AF45DEB3AFE9D9E7ADD672D8909BEF094567470892F7BCB712)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Dirent](#dirent)\> | Promise对象。返回表示异步读取目录项的结果。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
dir.read().then((dirent: fileio.Dirent) => {
  console.info("read succeed, the name of dirent is " + dirent.name);
}).catch((err: BusinessError) => {
  console.error("read failed with error:" + err);
});
```

#### \[h2\]read

read(callback: AsyncCallback<Dirent>): void

读取下一个目录项，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/k2p-X0pURU2GoikyTQfltQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=38F4A7A726E9549DA44D235FF4C5EFB2B3ED703F5C356E5A8E3AB1013AE54223)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Dirent](#dirent)\> | 是 | 异步读取下一个目录项之后的回调。 |

**示例：**

```ts
import { BusinessError } from '@ohos.base';
dir.read((err: BusinessError, dirent: fileio.Dirent) => {
  if (dirent) {
    // do something
    console.info("read succeed, the name of file is " + dirent.name);
  }
});
```

#### \[h2\]readSync

readSync(): Dirent

同步读取下一个目录项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/b6agxroGRNmVu2ROmZWlrw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BA73D8BD5D2717F85428D8206F38F8C3A739FDED6CD1AD1032E4829F0ED4A96A)

从API version 9开始废弃，请使用[fileIo.listFileSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Dirent](#dirent) | 表示一个目录项。 |

**示例：**

```ts
let dirent = dir.readSync();
```

#### \[h2\]close7+

close(): Promise<void>

异步关闭目录，使用promise形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/F8uyI00eRTSH__ybLKcgeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=91DA96CD5677C9DD83A646D2386B512B7DB90F3E43D79D45C8D5648AEA6AF888)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ts
import { BusinessError } from '@ohos.base';
dir.close().then(() => {
  console.info("close dir successfully");
});
```

#### \[h2\]close7+

close(callback: AsyncCallback<void>): void

异步关闭目录，使用callback形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/QZjIo5zXSPyYXh34D1TkKA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=40BDE98D7D24EBEBB172E5BB854EBCD5D8AA911E6ACBF42B04510F2AB236819D)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ts
import { BusinessError } from '@ohos.base';
dir.close((err: BusinessError) => {
  console.info("close dir successfully");
});
```

#### \[h2\]closeSync

closeSync(): void

用于关闭目录。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/8pb8X4jSSCWmLozS2C0tEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=6F29BAE1C5B509A38B9FF1F82ED636DF62B6CDC4EACCF779A57B2CF60D2CEBAB)

从API version 9开始废弃，请使用[fileIo.listFileSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```ts
dir.closeSync();
```

#### Dirent

在调用Dirent的方法前，需要先通过[dir.read()](#read)方法（同步或异步）来构建一个Dirent实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/zq8ejSQjQ2-S91xLkCFsSg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=604FA9BBDA9D9EBF9046B4F08BBEC8D0D484BEFA0FE3FCBDD0BABAFD59FD4F4B)

从API version 9开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile)替代。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可写 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 是 | 否 | 目录项的名称。 |

#### \[h2\]isBlockDevice

isBlockDevice(): boolean

用于判断当前目录项是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/8_c_yyaSR5CcUaoHk8SFMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=613F9215254476151558F31ED72B34099F78B09830C138AE637A855988F692C3)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示当前目录项是否是块特殊设备。true为是，false为不是。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
let isBLockDevice = dir.readSync().isBlockDevice();
```

#### \[h2\]isCharacterDevice

isCharacterDevice(): boolean

用于判断当前目录项是否是字符特殊设备。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/9dOoTdIURnCtSxV0DEZyOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=64162724EC426695984F3059AFD10B40EE61C2E978E7B10FC053A9A52F7A9257)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示当前目录项是否是字符特殊设备。true为是，false为不是。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
let isCharacterDevice = dir.readSync().isCharacterDevice();
```

#### \[h2\]isDirectory

isDirectory(): boolean

用于判断当前目录项是否是目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/0zGwKLOPRraRaqxTMRBhPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A2EBD3C020B8695AACCC41C25023D65AAEBEC840F476D43CC364AE3989D3F13C)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示当前目录项是否是目录。true为是，false为不是。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
let isDirectory = dir.readSync().isDirectory();
```

#### \[h2\]isFIFO

isFIFO(): boolean

用于判断当前目录项是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/uXKqBxi2RpO9qGFShdKc3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=371CAF80AD0EEEFDF64562587F5FE0C2CF51D03CE0AA4606FC82406D356A86B8)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示当前目录项是否是FIFO。true为是，false为不是。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
let isFIFO = dir.readSync().isFIFO();
```

#### \[h2\]isFile

isFile(): boolean

用于判断当前目录项是否是普通文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/PWi88VckSOyZHJKJkiJtcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9793ACBEE6E4475A7A42DFABA7ED125E06C09A2A717432F400D9AD1DFBBBE571)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示当前目录项是否是普通文件。true为是，false为不是。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
let isFile = dir.readSync().isFile();
```

#### \[h2\]isSocket

isSocket(): boolean

用于判断当前目录项是否是套接字。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/MV0xIUYNSI-jvidHs9ISHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=FF2A2C60C43DFD8AAF8739F0FBDD95B8414FF8054784491C1C4BDDEBC6188D1A)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示当前目录项是否是套接字。true为是，false为不是。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
let isSocket = dir.readSync().isSocket();
```

#### \[h2\]isSymbolicLink

isSymbolicLink(): boolean

用于判断当前目录项是否是符号链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/RUCPefrHTIi62oEwjDG2Wg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=FB55AB5BD1E8384F5CF37585C515E1B8EAC2DF2297410BFB1389CD53FB3E8352)

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示当前目录项是否是符号链接。true为是，false为不是。 |

**示例：**

```ts
let dir = fileio.opendirSync(pathDir);
let isSymbolicLink = dir.readSync().isSymbolicLink();
```
