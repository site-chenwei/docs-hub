---
title: "@ohos.file.fs (文件管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "ArkTS API"
  - "@ohos.file.fs (文件管理)"
captured_at: "2026-04-17T01:48:14.093Z"
---

# @ohos.file.fs (文件管理)

该模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/HsAoAx_NQuSlYh574jYY1Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9F18D01D0347155F171737876AB21D3AD337EB6F1C4097D177C9238813497C7D)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { fileIo } from '@kit.CoreFileKit';
```

#### 使用说明

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```ts
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
  }
}
```

获取沙箱路径的方式及其接口用法也可参考：[应用上下文Context-获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取应用文件路径)。

将指向资源的字符串称为URI。对于只支持沙箱路径作为入参的接口，可以使用构造fileUri对象并获取其沙箱路径的属性的方式将URI转换为沙箱路径，然后使用文件接口。URI定义解及其转换方式请参考：[文件URI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri)。

#### fileIo.stat

stat(file: string | number): Promise<Stat>

获取文件或目录详细属性信息，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | number | 是 | 
文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。

**说明**：从API version 22开始，支持传入URI。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise对象。返回文件或目录的具体信息。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.stat(filePath).then((stat: fileIo.Stat) => {
  console.info("get file info succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("get file info failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.stat

stat(file: string | number, callback: AsyncCallback<Stat>): void

获取文件或目录的详细属性信息，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | number | 是 | 
文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。

**说明**：从API version 22开始，支持传入URI。

 |
| callback | AsyncCallback<[Stat](#stat)\> | 是 | 异步获取文件或目录的信息之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
fileIo.stat(pathDir, (err: BusinessError, stat: fileIo.Stat) => {
  if (err) {
    console.error("get file info failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("get file info succeed, the size of file is " + stat.size);
  }
});
```

#### fileIo.statSync

statSync(file: string | number): Stat

以同步方法获取文件或目录详细属性信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | number | 是 | 
文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。

**说明**：从API version 22开始，支持传入URI。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Stat](#stat) | 表示文件或目录的具体信息。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let stat = fileIo.statSync(pathDir);
console.info("get file info succeed, the size of file is " + stat.size);
```

#### fileIo.access

access(path: string, mode?: AccessModeType): Promise<boolean>

检查文件或目录是否存在，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode12+ | [AccessModeType](#accessmodetype12) | 否 | 文件或目录校验的权限。不填该参数则默认校验文件是否存在。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回布尔值。返回true，表示文件存在；返回false，表示文件不存在。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.access(filePath).then((res: boolean) => {
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
}).catch((err: BusinessError) => {
  console.error("access failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.access12+

access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>

检查文件或目录是否在本地，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode | [AccessModeType](#accessmodetype12) | 是 | 文件或目录校验的权限。 |
| flag | [AccessFlagType](#accessflagtype12) | 是 | 文件或目录校验的位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回布尔值。返回true，表示文件或目录在本地且校验权限存在；返回false，表示文件或目录不存在或者文件或目录在云端或其他分布式设备上。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.access(filePath, fileIo.AccessModeType.EXIST, fileIo.AccessFlagType.LOCAL).then((res: boolean) => {
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
}).catch((err: BusinessError) => {
  console.error("access failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.access

access(path: string, callback: AsyncCallback<boolean>): void

检查文件或目录是否存在，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| callback | AsyncCallback<boolean> | 是 | 异步检查文件或目录是否存在的回调。如果存在，回调返回true；否则返回false。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.access(filePath, (err: BusinessError, res: boolean) => {
  if (err) {
    console.error("access failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (res) {
      console.info("file exists");
    } else {
      console.info("file not exists");
    }
  }
});
```

#### fileIo.accessSync

accessSync(path: string, mode?: AccessModeType): boolean

以同步方法检查文件或目录是否存在，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode12+ | [AccessModeType](#accessmodetype12) | 否 | 文件或目录校验的权限。不填该参数则默认校验文件或目录是否存在。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回true，表示文件存在；返回false，表示文件不存在。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
try {
  let res = fileIo.accessSync(filePath);
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error message: " + err.message + ", error code: " + err.code);
}
```

#### fileIo.accessSync12+

accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean

以同步方法检查文件或目录是否在本地，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件应用沙箱路径。 |
| mode | [AccessModeType](#accessmodetype12) | 是 | 文件或目录校验的权限。 |
| flag | [AccessFlagType](#accessflagtype12) | 是 | 文件或目录校验的位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回true，表示文件在本地且校验权限存在；返回false，表示文件不存在或者文件在云端或其他分布式设备上。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
try {
  let res = fileIo.accessSync(filePath, fileIo.AccessModeType.EXIST, fileIo.AccessFlagType.LOCAL);
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error message: " + err.message + ", error code: " + err.code);
}
```

#### fileIo.close

close(file: number | File): Promise<void>

关闭文件或目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | number | [File](#file) | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.close(file).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.close

close(file: number | File, callback: AsyncCallback<void>): void

关闭文件或目录，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | number | [File](#file) | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |
| callback | AsyncCallback<void> | 是 | 异步关闭文件或目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.close(file, (err: BusinessError) => {
  if (err) {
    console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close file succeed");
  }
});
```

#### fileIo.closeSync

closeSync(file: number | File): void

以同步方法关闭文件或目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | number | [File](#file) | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.closeSync(file);
```

#### fileIo.copy11+

copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>

拷贝文件或目录，使用promise异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| options | [CopyOptions](#copyoptions11) | 否 | options中提供拷贝进度回调。不填该参数则无拷贝进度回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
  console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let copyOption: fileIo.CopyOptions = {
  "progressListener" : progressListener
}
try {
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, copyOption).then(()=>{
    console.info("Succeeded in copying.");
  }).catch((err: BusinessError)=>{
    console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
  })
} catch(err) {
  console.error(`Failed to copy.Code: ${err.code}, message: ${err.message}`);
}
```

#### fileIo.copy11+

copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| callback | AsyncCallback<void> | 是 | 异步拷贝之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
}
```

#### fileIo.copy11+

copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| options | [CopyOptions](#copyoptions11) | 是 | 拷贝进度回调。 |
| callback | AsyncCallback<void> | 是 | 异步拷贝之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
    console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
  };
  let copyOption: fileIo.CopyOptions = {
    "progressListener" : progressListener
  }
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, copyOption, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
}
```

#### fileIo.copyFile

copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>

复制文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 否 | 
mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFile(srcPath, dstPath, 0).then(() => {
  console.info("copy file succeed");
}).catch((err: BusinessError) => {
  console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.copyFile

copyFile(src: string | number, dest: string | number, mode: number, callback: AsyncCallback<void>): void

复制文件，可设置覆盖文件的方式，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 是 | 
mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

 |
| callback | AsyncCallback<void> | 是 | 异步复制文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFile(srcPath, dstPath, 0, (err: BusinessError) => {
  if (err) {
    console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy file succeed");
  }
});
```

#### fileIo.copyFile

copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void

复制文件，覆盖方式为完全覆盖目标文件，未覆盖部分将被裁切。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步复制文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFile(srcPath, dstPath, (err: BusinessError) => {
  if (err) {
    console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy file succeed");
  }
});
```

#### fileIo.copyFileSync

copyFileSync(src: string | number, dest: string | number, mode?: number): void

以同步方法复制文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 否 | 
mode提供覆盖文件的选项，当前仅支持0，且默认为0。

0：完全覆盖目标文件，未覆盖部分将被裁切掉。

 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFileSync(srcPath, dstPath);
```

#### fileIo.copyDir10+

copyDir(src: string, dest: string, mode?: number): Promise<void>

复制源目录至目标路径下，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 
复制模式，默认值为0。

\- mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)\>形式提供。

\- mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, 0).then(() => {
  console.info("copy directory succeed");
}).catch((err: BusinessError) => {
  console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.copyDir10+

copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

复制源目录至目标路径下，可设置复制模式。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 
复制模式，默认值为0。

\- mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)\>形式提供。

\- mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

 |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | 是 | 异步复制目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, 0, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("copy directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy directory succeed");
  }
});
```

#### fileIo.copyDir10+

copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

复制源目录至目标路径下，使用callback异步回调。

如果目标目录下有与源目录名冲突的目录，且冲突目录下有同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)\>形式提供。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | 是 | 异步复制目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("copy directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy directory succeed");
  }
});
```

#### fileIo.copyDirSync10+

copyDirSync(src: string, dest: string, mode?: number): void

以同步方法复制源目录至目标路径下。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 
复制模式，默认值为0。

\- mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)\>形式提供。

\- mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
try {
  fileIo.copyDirSync(srcPath, destPath, 0);
  console.info("copy directory succeed");
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
}
```

#### fileIo.dup10+

dup(fd: number): File

复制文件描述符，并返回对应的File对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [File](#file) | 打开的File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file1 = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let fd: number = file1.fd;
let file2 = fileIo.dup(fd);
console.info("The name of the file2 is " + file2.name);
fileIo.closeSync(file1);
fileIo.closeSync(file2);
```

#### fileIo.connectDfs12+

connectDfs(networkId: string, listeners: DfsListeners): Promise<void>

业务调用connectDfs接口，触发建链。如果对端设备出现异常，业务执行回调DfsListeners内[onStatus](#onstatus12)通知应用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| networkId | string | 是 | 设备的网络Id。通过[distributedDeviceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager)接口调用[DeviceBasicInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicebasicinfo)获得。 |
| listeners | [DfsListeners](#fileiodfslisteners12) | 是 | 分布式文件系统状态监听器。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Success to get available device list`);
  let networkId = deviceInfoList[0].networkId;
  let listeners: fileIo.DfsListeners = {
    onStatus(networkId, status) {
      console.info('onStatus');
    }
  };
  fileIo.connectDfs(networkId, listeners).then(() => {
    console.info("Success to connectDfs");
  }).catch((err: BusinessError) => {
    console.error(`Failed to connectDfs. Code: ${err.code}, message: ${err.message}`);
  });
}
```

#### fileIo.disconnectDfs12+

disconnectDfs(networkId: string): Promise<void>

业务调用disconnectDfs接口，传入networkId参数，触发断链。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| networkId | string | 是 | 设备的网络Id。通过[distributedDeviceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager)接口调用[DeviceBasicInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicebasicinfo)获得。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[空间统计错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#空间统计错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Success to get available device list`);
  let networkId = deviceInfoList[0].networkId;
  fileIo.disconnectDfs(networkId).then(() => {
    console.info("Success to disconnect dfs");
  }).catch((err: BusinessError) => {
    console.error(`Failed to disconnect dfs. Code: ${err.code}, message: ${err.message}`);
  })
}
```

#### fileIo.setxattr12+

setxattr(path: string, key: string, value: string): Promise<void>

设置文件或目录的扩展属性。使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。 |
| value | string | 是 | 扩展属性的value。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

fileIo.setxattr(filePath, attrKey, attrValue).then(() => {
  console.info("Set extended attribute successfully.");
}).catch((err: BusinessError) => {
  console.error("Failed to set extended attribute with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.setxattrSync12+

setxattrSync(path: string, key: string, value: string): void

设置文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。 |
| value | string | 是 | 扩展属性的value。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

try {
  fileIo.setxattrSync(filePath, attrKey, attrValue);
  console.info("Set extended attribute successfully.");
} catch (err) {
  console.error("Failed to set extended attribute with error message: " + err.message + ", error code: " + err.code);
}
```

#### fileIo.getxattr12+

getxattr(path: string, key: string): Promise<string>

获取文件或目录的扩展属性。使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象。返回扩展属性的value。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

fileIo.getxattr(filePath, attrKey).then((attrValue: string) => {
  console.info("Get extended attribute succeed, the value is: " + attrValue);
}).catch((err: BusinessError) => {
  console.error("Failed to get extended attribute with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.getxattrSync12+

getxattrSync(path: string, key: string): string

使用同步接口获取文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回扩展属性的value。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

try {
  let attrValue = fileIo.getxattrSync(filePath, attrKey);
  console.info("Get extended attribute succeed, the value is: " + attrValue);
} catch (err) {
  console.error("Failed to get extended attribute with error message: " + err.message + ", error code: " + err.code);
}
```

#### fileIo.mkdir

mkdir(path: string): Promise<void>

创建目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((err: BusinessError) => {
  console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.mkdir11+

mkdir(path: string, recursion: boolean): Promise<void>

创建目录，使用promise异步回调。当recursion指定为true时，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true).then(() => {
  console.info("mkdir succeed");
}).catch((err: BusinessError) => {
  console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.mkdir

mkdir(path: string, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步创建目录操作完成之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdir succeed");
  }
});
```

#### fileIo.mkdir11+

mkdir(path: string, recursion: boolean, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。当recursion指定为true，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |
| callback | AsyncCallback<void> | 是 | 异步创建目录操作完成之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true, (err: BusinessError) => {
  if (err) {
    console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdir succeed");
  }
});
```

#### fileIo.mkdirSync

mkdirSync(path: string): void

以同步方法创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let dirPath = pathDir + "/testDir";
fileIo.mkdirSync(dirPath);
```

#### fileIo.mkdirSync11+

mkdirSync(path: string, recursion: boolean): void

以同步方法创建目录。当recursion指定为true，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdirSync(dirPath, true);
```

#### fileIo.open

open(path: string, mode?: number): Promise<File>

打开文件或目录，使用promise异步回调。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录的应用沙箱路径或文件URI。 |
| mode | number | 否 | 
打开文件或目录的[选项](#openmode)，必须指定如下选项中的一个，默认以只读方式打开：

\- OpenMode.READ\_ONLY(0o0)：只读打开。

\- OpenMode.WRITE\_ONLY(0o1)：只写打开。

\- OpenMode.READ\_WRITE(0o2)：读写打开。

可以追加以下功能选项，以按位或的方式组合，默认情况下不追加任何额外选项。

\- OpenMode.CREATE(0o100)：如果文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO方式打开文件。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[File](#file)\> | Promise对象。返回File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).then((file: fileIo.File) => {
  console.info("file fd: " + file.fd);
  fileIo.closeSync(file);
}).catch((err: BusinessError) => {
  console.error("open file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.open

open(path: string, mode: number, callback: AsyncCallback<File>): void

打开文件或目录，可设置打开文件的选项。使用callback异步回调。

支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录的应用沙箱路径或URI。 |
| mode | number | 是 | 
打开文件或目录的[选项](#openmode)，必须指定如下选项中的一个，默认以只读方式打开：

\- OpenMode.READ\_ONLY(0o0)：只读打开。

\- OpenMode.WRITE\_ONLY(0o1)：只写打开。

\- OpenMode.READ\_WRITE(0o2)：读写打开。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。

 |
| callback | AsyncCallback<[File](#file)\> | 是 | 异步打开文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE, (err: BusinessError, file: fileIo.File) => {
  if (err) {
    console.error("open failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("file fd: " + file.fd);
    fileIo.closeSync(file);
  }
});
```

#### fileIo.open

open(path: string, callback: AsyncCallback<File>): void

打开文件或目录，使用callback异步回调。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件或目录的应用沙箱路径或URI。 |
| callback | AsyncCallback<[File](#file)\> | 是 | 异步打开文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.open(filePath, (err: BusinessError, file: fileIo.File) => {
  if (err) {
    console.error("open failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("file fd: " + file.fd);
    fileIo.closeSync(file);
  }
});
```

#### fileIo.openSync

openSync(path: string, mode?: number): File

以同步方法打开文件或目录。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 打开文件或目录的应用沙箱路径或URI。 |
| mode | number | 否 | 
打开文件或目录的[选项](#openmode)，必须指定如下选项中的一个，默认以只读方式打开：

\- OpenMode.READ\_ONLY(0o0)：只读打开。

\- OpenMode.WRITE\_ONLY(0o1)：只写打开。

\- OpenMode.READ\_WRITE(0o2)：读写打开。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [File](#file) | 打开的File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
console.info("file fd: " + file.fd);
fileIo.closeSync(file);
```

#### fileIo.read

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

读取文件数据，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer).then((readLen: number) => {
  console.info("read file data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error("read file data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fileIo.closeSync(file);
});
```

#### fileIo.read

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从文件读取数据，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。

 |
| callback | AsyncCallback<number> | 是 | 异步读取数据之后的回调。返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read file data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`The content of file: ${buf.toString()}`);
  }
  fileIo.closeSync(file);
});
```

#### fileIo.readSync

readSync(fd: number, buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let buf = new ArrayBuffer(4096);
fileIo.readSync(file.fd, buf);
fileIo.closeSync(file);
```

#### fileIo.rmdir

rmdir(path: string): Promise<void>

删除目录及其所有子目录和文件，使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/T1wV9Y1hT6GkCX4jG2gwaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=99AC72261300E7AC3F6899A103C72D030B9A93FCDEC79CBB5542758D772C7614)

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath).then(() => {
  console.info("rmdir succeed");
}).catch((err: BusinessError) => {
  console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.rmdir

rmdir(path: string, callback: AsyncCallback<void>): void

删除目录及其所有子目录和文件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/5Q1KRaK1QVuM03ccAoBP1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=ADC70E1A80C13C49A5F4B797C7B4748CCE4DDDE8ACEFEF7A4B163EED64EDD495)

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("rmdir succeed");
  }
});
```

#### fileIo.rmdirSync

rmdirSync(path: string): void

以同步方法删除目录及其所有子目录和文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/EEGU8rBFR9OD0nuvAiaWfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=3A655E6EBF2C9E20F7889EFCD8641955B9538A9E26C59BC34F4F49848D6D05AB)

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlinkSync接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let dirPath = pathDir + "/testDir";
fileIo.rmdirSync(dirPath);
```

#### fileIo.unlink

unlink(path: string): Promise<void>

删除单个文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.unlink(filePath).then(() => {
  console.info("remove file succeed");
}).catch((err: BusinessError) => {
  console.error("remove file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.unlink

unlink(path: string, callback: AsyncCallback<void>): void

删除文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.unlink(filePath, (err: BusinessError) => {
  if (err) {
    console.error("remove file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("remove file succeed");
  }
});
```

#### fileIo.unlinkSync

unlinkSync(path: string): void

以同步方法删除文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
fileIo.unlinkSync(filePath);
```

#### fileIo.write

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写入。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str).then((writeLen: number) => {
  console.info("write data to file succeed and size is:" + writeLen);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fileIo.closeSync(file);
});
```

#### fileIo.write

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。

 |
| callback | AsyncCallback<number> | 是 | 异步将数据写入完成后执行的回调函数。返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error("write data to file failed with error message:" + err.message + ", error code: " + err.code);
  } else {
    console.info("write data to file succeed and size is:" + writeLen);
  }
  fileIo.closeSync(file);
});
```

#### fileIo.writeSync

writeSync(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
let writeLen = fileIo.writeSync(file.fd, str);
console.info("write data to file succeed and size is:" + writeLen);
fileIo.closeSync(file);
```

#### fileIo.truncate

truncate(file: string | number, len?: number): Promise<void>

截断文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let len: number = 5;
fileIo.truncate(filePath, len).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.truncate

truncate(file: string | number, len?: number, callback: AsyncCallback<void>): void

截断文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let len: number = 5;
fileIo.truncate(filePath, len, (err: BusinessError) => {
  if (err) {
    console.error("truncate failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("truncate succeed");
  }
});
```

#### fileIo.truncateSync

truncateSync(file: string | number, len?: number): void

以同步方法截断文件内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let len: number = 5;
fileIo.truncateSync(filePath, len);
```

#### fileIo.readLines11+

readLines(filePath: string, options?: Options): Promise<ReaderIterator>

逐行读取文件文本内容，使用promise异步回调。只支持读取utf-8格式文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [Options](#options11) | 否 | 
可选项。支持以下选项：

\- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ReaderIterator](#readeriterator11)\> | Promise对象。返回文件读取迭代器。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options).then((readerIterator: fileIo.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info("content: " + it.value);
  }
}).catch((err: BusinessError) => {
  console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.readLines11+

readLines(filePath: string, options?: Options, callback: AsyncCallback<ReaderIterator>): void

逐行读取文件文本内容，使用callback异步回调，只支持读取utf-8格式文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [Options](#options11) | 否 | 
可选项。支持以下选项：

\- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |
| callback | AsyncCallback<[ReaderIterator](#readeriterator11)\> | 是 | 逐行读取文件文本内容回调。返回文件读取迭代器。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options, (err: BusinessError, readerIterator: fileIo.ReaderIterator) => {
  if (err) {
    console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
      console.info("content: " + it.value);
    }
  }
});
```

#### fileIo.readLinesSync11+

readLinesSync(filePath: string, options?: Options): ReaderIterator

以同步方式逐行读取文件的文本内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [Options](#options11) | 否 | 
可选项。支持以下选项：

\- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ReaderIterator](#readeriterator11) | 返回文件读取迭代器。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
let readerIterator = fileIo.readLinesSync(filePath, options);
for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
  console.info("content: " + it.value);
}
```

#### ReaderIterator11+

文件读取迭代器。在调用ReaderIterator的方法前，需要先通过readLines方法（同步或异步）来构建一个ReaderIterator实例。

#### \[h2\]next11+

next(): ReaderIteratorResult

获取迭代器下一项内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ReaderIteratorResult](#readeriteratorresult11) | 文件读取迭代器返回结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/uHnX1V9gTGK2uCl_VQWjTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=9865EF4B28FD74486B28A9F1D1A8E2B58B383115BA4AE83C88B0990B0DF4549A)

如果ReaderIterator读取的当前行的编码方式不是'utf-8'，接口返回错误码13900037。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options).then((readerIterator: fileIo.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info("content: " + it.value);
  }
}).catch((err: BusinessError) => {
  console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### ReaderIteratorResult11+

文件读取迭代器返回结果，支持ReaderIterator接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| done | boolean | 迭代器是否已完成迭代。true：已完成迭代；false：未完成迭代。 |
| value | string | 逐行读取的文件文本内容。 |

#### fileIo.readText

readText(filePath: string, options?: ReadTextOptions): Promise<string>

基于文本方式读取文件（即直接读取文件的文本内容），使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](#readtextoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。

\- length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。

\- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象。返回读取文件的内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.readText(filePath).then((str: string) => {
  console.info("readText succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("readText failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.readText

readText(filePath: string, options?: ReadTextOptions, callback: AsyncCallback<string>): void

基于文本方式读取文件内容，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](#readtextoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。

\- length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。

\- encoding，string类型，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回读取文件的内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadTextOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stat = fileIo.statSync(filePath);
let readTextOption: ReadTextOptions = {
    offset: 1,
    length: stat.size,
    encoding: 'utf-8'
};
fileIo.readText(filePath, readTextOption, (err: BusinessError, str: string) => {
  if (err) {
    console.error("readText failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("readText succeed:" + str);
  }
});
```

#### fileIo.readTextSync

readTextSync(filePath: string, options?: ReadTextOptions): string

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](#readtextoptions11) | 否 | 
支持如下选项：

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。

\- length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。

\- encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回读取文件的内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { ReadTextOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let readTextOptions: ReadTextOptions = {
  offset: 1,
  length: 0,
  encoding: 'utf-8'
};
let stat = fileIo.statSync(filePath);
readTextOptions.length = stat.size;
let str = fileIo.readTextSync(filePath, readTextOptions);
console.info("readText succeed:" + str);
```

#### fileIo.lstat

lstat(path: string): Promise<Stat>

获取符号链接文件信息，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 
文件的应用沙箱路径path或URI。

**说明**：从API version 22开始，支持传入URI。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise对象。返回Stat对象，表示文件的具体信息，详情见Stat。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath).then((stat: fileIo.Stat) => {
  console.info("lstat succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("lstat failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.lstat

lstat(path: string, callback: AsyncCallback<Stat>): void

获取符号链接文件信息，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 
文件的应用沙箱路径path或URI。

**说明**：从API version 22开始，支持传入URI。

 |
| callback | AsyncCallback<[Stat](#stat)\> | 是 | 异步获取文件具体信息之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath, (err: BusinessError, stat: fileIo.Stat) => {
  if (err) {
    console.error("lstat failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("lstat succeed, the size of file is " + stat.size);
  }
});
```

#### fileIo.lstatSync

lstatSync(path: string): Stat

以同步方法获取符号链接文件信息。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 
文件的应用沙箱路径path或URI。

**说明**：从API version 22开始，支持传入URI。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Stat](#stat) | 表示文件的具体信息。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/linkToFile";
let fileStat = fileIo.lstatSync(filePath);
console.info("lstat succeed, the size of file is " + fileStat.size);
```

#### fileIo.rename

rename(oldPath: string, newPath: string): Promise<void>

重命名文件或目录，使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/HyJg0JVBSeab020PARtGZA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BE6AF0D9594A60769A5CB65F84012793145C5CB38801667917F84EAEA2C7F3E3)

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fileIo.rename(srcFile, dstFile).then(() => {
  console.info("rename succeed");
}).catch((err: BusinessError) => {
  console.error("rename failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.rename

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

重命名文件或目录，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/ZwkKFCU_Q320XTY_PzeKXg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=EDD3E5BE1C4E861FD4D4120A7B56EA5C4A30A7C312CF3493CC83912F01E8DC50)

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |
| callback | AsyncCallback<void> | 是 | 异步重命名文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fileIo.rename(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error("rename failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("rename succeed");
  }
});
```

#### fileIo.renameSync

renameSync(oldPath: string, newPath: string): void

以同步方法重命名文件或目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/J7i3zBcgTB6vybRtjDAp2Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=25A7D39842AC488CA93EEB8ABE522E9E29F517D452FA5C0147A7FB6237CFBCC8)

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fileIo.renameSync(srcFile, dstFile);
```

#### fileIo.fsync

fsync(fd: number): Promise<void>

将文件系统缓存数据写入磁盘，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fsync(file.fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fileIo.closeSync(file);
});
```

#### fileIo.fsync

fsync(fd: number, callback: AsyncCallback<void>): void

将文件系统缓存数据写入磁盘，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件数据同步之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fsync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error("fsync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("fsync succeed");
  }
  fileIo.closeSync(file);
});
```

#### fileIo.fsyncSync

fsyncSync(fd: number): void

以同步方法将文件系统缓存数据写入磁盘。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fsyncSync(file.fd);
fileIo.closeSync(file);
```

#### fileIo.fdatasync

fdatasync(fd: number): Promise<void>

实现文件内容数据同步，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdatasync(file.fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fileIo.closeSync(file);
});
```

#### fileIo.fdatasync

fdatasync(fd: number, callback: AsyncCallback<void>): void

实现文件内容数据同步，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件内容数据同步之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdatasync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error("fdatasync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("fdatasync succeed");
  }
  fileIo.closeSync(file);
});
```

#### fileIo.fdatasyncSync

fdatasyncSync(fd: number): void

以同步方法实现文件内容的数据同步。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdatasyncSync(file.fd);
fileIo.closeSync(file);
```

#### fileIo.symlink

symlink(target: string, srcPath: string): Promise<void>

基于文件路径创建符号链接，使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/BL1Kq84hRQSN8mW8juKExw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=423B46C919FD4D4F6255BC6012ECBB6FBE632224BAA2BF6A260453972F47659D)

从API version 11开始，不支持三方应用使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fileIo.symlink(srcFile, dstFile).then(() => {
  console.info("symlink succeed");
}).catch((err: BusinessError) => {
  console.error("symlink failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.symlink

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

基于文件路径创建符号链接，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/NqAOKISOSZ2b3N2-IHF3hA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=DFBF28809306CFF836091E05C9C6D84243AB97DB545E280C3EF2B7000F9A7CD6)

从API version 11开始，不支持三方应用使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步创建符号链接信息之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fileIo.symlink(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error("symlink failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("symlink succeed");
  }
});
```

#### fileIo.symlinkSync

symlinkSync(target: string, srcPath: string): void

以同步的方法基于文件路径创建符号链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/JLS5dUjnQwOn6BnVJ3GoHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=E73EC24CE6437AE7425094A1EFD6CDC0DE87D3D7C6B5CAA43D97953C73143BEE)

从API version 11开始，不支持三方应用使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fileIo.symlinkSync(srcFile, dstFile);
```

#### fileIo.listFile

listFile(path: string, options?: ListFileOptions): Promise<string\[\]>

默认列出当前目录下所有文件名和目录名。支持过滤。使用promise异步回调。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | [ListFileOptions](#listfileoptions11) | 否 | 文件过滤选项。默认不进行过滤。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string\[\]> | Promise对象。返回文件名数组，默认以'utf-8'编码。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
}
fileIo.listFile(pathDir, listFileOption).then((filenames: Array<string>) => {
  console.info("listFile succeed");
  for (let i = 0; i < filenames.length; i++) {
    console.info("fileName: %s", filenames[i]);
  }
}).catch((err: BusinessError) => {
  console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.listFile

listFile(path: string, options?: ListFileOptions, callback: AsyncCallback<string\[\]>): void

默认列出当前目录下所有文件名和目录名。支持过滤。使用callback异步回调。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | [ListFileOptions](#listfileoptions11) | 否 | 文件过滤选项。默认不进行过滤。 |
| callback | AsyncCallback<string\[\]> | 是 | 异步列出文件名数组之后的回调，默认以'utf-8'编码。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
};
fileIo.listFile(pathDir, listFileOption, (err: BusinessError, filenames: Array<string>) => {
  if (err) {
    console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("listFile succeed");
    for (let i = 0; i < filenames.length; i++) {
      console.info("filename: %s", filenames[i]);
    }
  }
});
```

#### fileIo.listFileSync

listFileSync(path: string, options?: ListFileOptions): string\[\]

默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | [ListFileOptions](#listfileoptions11) | 否 | 文件过滤选项。默认不进行过滤。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string\[\] | 返回文件名数组，默认以'utf-8'编码。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { Filter, ListFileOptions} from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
};
let filenames = fileIo.listFileSync(pathDir, listFileOption);
console.info("listFile succeed");
for (let i = 0; i < filenames.length; i++) {
  console.info("filename: %s", filenames[i]);
}
```

#### fileIo.lseek11+

lseek(fd: number, offset: number, whence?: WhenceType): number

调整文件偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 文件描述符。 |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](#whencetype11) | 否 | 偏移指针相对位置类型。不指定则默认为文件起始位置处。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 当前文件偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
console.info('The current offset is at ' + fileIo.lseek(file.fd, 5, fileIo.WhenceType.SEEK_SET));
fileIo.closeSync(file);
```

#### fileIo.moveDir10+

moveDir(src: string, dest: string, mode?: number): Promise<void>

移动源目录至目标路径下，使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/WUclIX-QRgO62KQ6kzDUrA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=291EE9367FE7745D48D31C36CC650F7441E3136B84C96E33904DC57F78385CF2)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 
移动模式，默认值为0。

\- mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的非空目录，则抛出异常。

\- mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)\>形式提供。

\- mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

\- mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下的所有原始文件将被删除。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, 1).then(() => {
  console.info("move directory succeed");
}).catch((err: BusinessError) => {
  console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.moveDir10+

moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

移动源目录至目标路径下，支持设置移动模式。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/zhKgY272SY6P4iL6B3lojQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A190A54914D1F87549EBD0A6AFC6972763753207C64335E7A83610461F16E67A)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 
移动模式，默认值为0。

\- mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。

\- mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)\>形式提供。

\- mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

\- mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。

 |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | 是 | 异步移动目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, 1, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move directory succeed");
  }
});
```

#### fileIo.moveDir10+

moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

移动源目录至目标路径下。使用callback异步回调。

移动模式为目录级别抛异常。当目标目录下存在与源目录名冲突的目录，则抛出异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/rJqVUyDmQay3GpON14pUZQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=4DFF666223F4CCDC2F0DB5BEE29ED634934078D19811005AA17AB66FD269E4BA)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | 是 | 异步移动目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else if (err) {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move directory succeed");
  }
});
```

#### fileIo.moveDirSync10+

moveDirSync(src: string, dest: string, mode?: number): void

以同步方法移动源目录至目标路径下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/HDffK24XR7mU6q_3Ehn_Nw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=66E279A85B7003CB6F8924448CB3F462B024564E2A15ADD93A3E8DB033E603F6)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 
移动模式，默认值为0。

\- mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。

\- mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)\>形式提供。

\- mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。

\- mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。

 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
try {
  fileIo.moveDirSync(srcPath, destPath, 1);
  console.info("move directory succeed");
} catch (error) {
  let err: BusinessError<Array<ConflictFiles>> = error as BusinessError<Array<ConflictFiles>>;
  if (err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data[i].srcFile + " " + err.data[i].destFile);
    }
  } else {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  }
}
```

#### fileIo.moveFile

moveFile(src: string, dest: string, mode?: number): Promise<void>

移动文件，使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/qQykyNnCQZSWDOb2lMeEeA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=4CF306D2956CAF776BD71B80E07249CDAC7E62908ED4E6B72A06BEB78FB7CDF1)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 否 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0).then(() => {
  console.info("move file succeed");
}).catch((err: BusinessError) => {
  console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.moveFile

moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void

移动文件，支持设置移动模式。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/78uVSP_VRAiqXr9u2OAuHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=16EEA6E016A9BE66D84653210CDD84027BBC27C9AB101585FE0947C5BBD20307)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 是 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |
| callback | AsyncCallback<void> | 是 | 异步移动文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});
```

#### fileIo.moveFile

moveFile(src: string, dest: string, callback: AsyncCallback<void>): void

移动文件。如果移动位置存在同名文件，将强制覆盖。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/qwKD0p0lQaWnryq330oXJw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=6229F4B4AC9D39BCA20B7CE9C18803AD5E4838E4958546F3ED8CE50E17CD36F9)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步移动文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});
```

#### fileIo.moveFileSync

moveFileSync(src: string, dest: string, mode?: number): void

以同步方式移动文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/CSR6l9X6SI6M7slnaYELqg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=4F1FE2B22CF88F49DCFA33D6CD154080AC5461BB7D90A25BD16DD566F946F9D3)

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 否 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFileSync(srcPath, destPath, 0);
console.info("move file succeed");
```

#### fileIo.mkdtemp

mkdtemp(prefix: string): Promise<string>

创建临时目录，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象。返回生成的唯一目录路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
fileIo.mkdtemp(pathDir + "/XXXXXX").then((dir: string) => {
  console.info("mkdtemp succeed:" + dir);
}).catch((err: BusinessError) => {
  console.error("mkdtemp failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.mkdtemp

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

创建临时目录，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |
| callback | AsyncCallback<string> | 是 | 异步创建临时目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
fileIo.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  if (err) {
    console.error("mkdtemp failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdtemp succeed");
  }
});
```

#### fileIo.mkdtempSync

mkdtempSync(prefix: string): string

以同步的方法创建临时目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 产生的唯一目录路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let res = fileIo.mkdtempSync(pathDir + "/XXXXXX");
```

#### fileIo.utimes11+

utimes(path: string, mtime: number): void

更改文件上次修改该文件的时间。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mtime | number | 是 | 待更新的时间戳。自1970年1月1日起至目标时间的毫秒数。仅支持更改上次修改该文件的时间属性。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.writeSync(file.fd, 'test data');
fileIo.closeSync(file);
fileIo.utimes(filePath, new Date().getTime());
```

#### fileIo.createRandomAccessFile10+

createRandomAccessFile(file: string | File, mode?: number): Promise<RandomAccessFile>

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 
创建文件RandomAccessFile对象的[选项](#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

\- OpenMode.READ\_ONLY(0o0)：只读创建。

\- OpenMode.WRITE\_ONLY(0o1)：只写创建。

\- OpenMode.READ\_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path未指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RandomAccessFile](#randomaccessfile10)\> | Promise对象。返回RandomAccessFile对象的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.createRandomAccessFile(file).then((randomAccessFile: fileIo.RandomAccessFile) => {
  console.info("randomAccessFile fd: " + randomAccessFile.fd);
  randomAccessFile.close();
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fileIo.closeSync(file);
});
```

#### fileIo.createRandomAccessFile10+

createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void

基于文件路径或文件对象，以只读方式创建RandomAccessFile对象，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| callback | AsyncCallback<[RandomAccessFile](#randomaccessfile10)\> | 是 | 异步创建RandomAccessFile对象之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.createRandomAccessFile(file, (err: BusinessError, randomAccessFile: fileIo.RandomAccessFile) => {
  if (err) {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  }
  fileIo.closeSync(file);
});
```

#### fileIo.createRandomAccessFile10+

createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void

基于文件路径或文件对象创建RandomAccessFile对象，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 是 | 
创建文件RandomAccessFile对象的[选项](#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

\- OpenMode.READ\_ONLY(0o0)：只读创建。

\- OpenMode.WRITE\_ONLY(0o1)：只写创建。

\- OpenMode.READ\_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

 |
| callback | AsyncCallback<[RandomAccessFile](#randomaccessfile10)\> | 是 | 异步创建RandomAccessFile对象之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.createRandomAccessFile(file, fileIo.OpenMode.READ_ONLY, (err: BusinessError, randomAccessFile: fileIo.RandomAccessFile) => {
  if (err) {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  }
  fileIo.closeSync(file);
});
```

#### fileIo.createRandomAccessFile12+

createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 
创建文件RandomAccessFile对象的[选项](#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

\- OpenMode.READ\_ONLY(0o0)：只读创建。

\- OpenMode.WRITE\_ONLY(0o1)：只写创建。

\- OpenMode.READ\_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

 |
| options | [RandomAccessFileOptions](#randomaccessfileoptions12) | 否 | 

支持如下选项：

\- start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

\- end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。

此选项仅对[getreadstream](#getreadstream12)及[getwritestream](#getwritestream12)获取的文件流对象生效。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RandomAccessFile](#randomaccessfile10)\> | Promise对象。返回RandomAccessFile对象的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.createRandomAccessFile(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE, { start: 10, end: 100 })
  .then((randomAccessFile: fileIo.RandomAccessFile) => {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  })
  .catch((err: BusinessError) => {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  });
```

#### fileIo.createRandomAccessFileSync10+

createRandomAccessFileSync(file: string | File, mode?: number): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 
创建文件RandomAccessFile对象的[选项](#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

\- OpenMode.READ\_ONLY(0o0)：只读创建。

\- OpenMode.WRITE\_ONLY(0o1)：只写创建。

\- OpenMode.READ\_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [RandomAccessFile](#randomaccessfile10) | 返回RandomAccessFile对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
randomAccessFile.close();
```

#### fileIo.createRandomAccessFileSync12+

createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 
创建文件RandomAccessFile对象的[选项](#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：

\- OpenMode.READ\_ONLY(0o0)：只读创建。

\- OpenMode.WRITE\_ONLY(0o1)：只写创建。

\- OpenMode.READ\_WRITE(0o2)：读写创建。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。

 |
| options | [RandomAccessFileOptions](#randomaccessfileoptions12) | 否 | 

支持如下选项：

\- start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

\- end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。

此选项仅对[getreadstream](#getreadstream12)及[getwritestream](#getwritestream12)获取的文件流对象生效。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [RandomAccessFile](#randomaccessfile10) | 返回RandomAccessFile对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE,
  { start: 10, end: 100 });
randomAccessFile.close();
```

#### fileIo.createStream

createStream(path: string, mode: string): Promise<Stream>

基于文件路径创建文件流，使用promise异步回调。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的应用沙箱路径。 |
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

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.createStream(filePath, "a+").then((stream: fileIo.Stream) => {
  stream.closeSync();
  console.info("createStream succeed");
}).catch((err: BusinessError) => {
  console.error("createStream failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### fileIo.createStream

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

基于文件路径创建文件流，使用callback异步回调。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |
| callback | AsyncCallback<[Stream](#stream)\> | 是 | 异步打开文件流之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fileIo.createStream(filePath, "r+", (err: BusinessError, stream: fileIo.Stream) => {
  if (err) {
    console.error("create stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    stream.closeSync();
    console.info("createStream succeed");
  }
})
```

#### fileIo.createStreamSync

createStreamSync(path: string, mode: string): Stream

以同步方法基于文件路径创建文件流。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的应用沙箱路径。 |
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

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
console.info("createStream succeed");
stream.closeSync();
```

#### fileIo.fdopenStream

fdopenStream(fd: number, mode: string): Promise<Stream>

基于文件描述符打开文件流，使用promise异步回调。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
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

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdopenStream(file.fd, "r+").then((stream: fileIo.Stream) => {
  console.info("openStream succeed");
  stream.closeSync();
}).catch((err: BusinessError) => {
  console.error("openStream failed with error message: " + err.message + ", error code: " + err.code);
  // 文件流打开失败后，文件描述符需要手动关闭
  fileIo.closeSync(file);
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/1uOg7U8NRiGIK-HJVfnarA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=3FBBFD092F2D1D1278C41AD8E79CCB286E42C908F4BC20D28F8D2161F866CABC)

使用文件描述符创建的文件流时，文件描述符的生命周期将由文件流对象管理。调用文件流的close()函数后，初始的文件描述符也会被关闭。

#### fileIo.fdopenStream

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

基于文件描述符打开文件流，使用callback异步回调。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
| mode | string | 是 | 
\- r：打开只读文件，该文件必须存在。

\- r+：打开可读写的文件，该文件必须存在。

\- w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。

\- a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。

\- a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。

 |
| callback | AsyncCallback<[Stream](#stream)\> | 是 | 异步打开文件流之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
fileIo.fdopenStream(file.fd, "r+", (err: BusinessError, stream: fileIo.Stream) => {
  if (err) {
    console.error("fdopen stream failed with error message: " + err.message + ", error code: " + err.code);
    // 文件流打开失败后，文件描述符需要手动关闭
    fileIo.closeSync(file);
  } else {
    console.info("fdopen stream succeed");
    stream.closeSync();
  }
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/htMzfng7QGGdQDqdMwrIOg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=399E0E660637A8017FDB69834FD2800CEF7B277E687D77DE0705853BDF892A7E)

使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。

#### fileIo.fdopenStreamSync

fdopenStreamSync(fd: number, mode: string): Stream

以同步方法基于文件描述符打开文件流。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 已打开的文件描述符。 |
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

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
let stream = fileIo.fdopenStreamSync(file.fd, "r+");
stream.closeSync();
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/i4HqHYDvTDSInDS7APUltQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=4A694899134ED07DA5716CDDB1D2FA5DF08E03E508F6828681B2918F7AF9378D)

使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。

#### fileIo.createReadStream12+

createReadStream(path: string, options?: ReadStreamOptions ): ReadStream

以同步方法打开文件可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件路径。 |
| options | [ReadStreamOptions](#readstreamoptions12) | 否 | 
支持如下选项：

\- start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

\- end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ReadStream](#readstream12) | 文件可读流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
// 创建文件可读流
const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});
```

#### fileIo.createWriteStream12+

createWriteStream(path: string, options?: WriteStreamOptions): WriteStream

以同步方法打开文件可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件路径。 |
| options | [WriteStreamOptions](#writestreamoptions12) | 否 | 
支持如下选项：

\- start，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- mode，number 类型，创建文件可写流的[选项](#openmode)，可选，默认以只写方式创建。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WriteStream](#writestream12) | 文件可写流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
// 创建文件可读流
const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});
```

#### AtomicFile15+

AtomicFile是一个用于对文件进行原子读写操作的类。

在写操作时，通过写入临时文件，并在写入成功后将其重命名到原始文件位置来确保写入文件的完整性；而在写入失败时删除临时文件，不修改原始文件内容。

使用者可以自行调用finishWrite或failWrite来完成文件内容的写入或回滚。

**系统能力**：SystemCapability.FileManagement.File.FileIO

#### \[h2\]constructor15+

constructor(path: string)

对于给定路径的文件创建一个AtomicFile类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 文件的沙箱路径。 |

#### \[h2\]getBaseFile15+

getBaseFile(): File

通过AtomicFile对象获取文件对象。

文件描述符fd需要由用户调用close方法关闭。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [File](#file) | 打开的File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let atomicFile = new fileIo.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = atomicFile.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    atomicFile.finishWrite();
    let File = atomicFile.getBaseFile();
    console.info('AtomicFile getBaseFile File.fd is: ' + File.fd + ' path: ' + File.path + ' name: ' + File.name);
  })
} catch (err) {
  console.error(`Failed to get baseFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]openRead15+

openRead(): ReadStream

创建一个读文件流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ReadStream](#readstream12) | 文件可读流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let readStream = file.openRead();
      readStream.on('readable', () => {
        const data = readStream.read();
        if (!data) {
          console.error('AtomicFile read data is null.');
          return;
        }
        console.info('AtomicFile read data is: ' + data);
      });
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]readFully15+

readFully(): ArrayBuffer

读取文件全部内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| ArrayBuffer | 文件的全部内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';
import { util, buffer } from '@kit.ArkTS';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      console.info('AtomicFile readFully str is: ' + str);
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]startWrite15+

startWrite(): WriteStream

对文件开始新的写入操作。将返回一个WriteStream，用于在其中写入新的文件数据。

当文件不存在时新建文件。

在写入文件完成后，写入成功需要调用finishWrite()，写入失败需要调用failWrite()。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WriteStream](#writestream12) | 文件可写流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    console.info('AtomicFile write finished!');
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]finishWrite15+

finishWrite(): void

在完成对startWrite返回流的写入操作时调用，表示文件写入成功。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]failWrite15+

failWrite(): void

文件写入失败后调用，将执行文件回滚操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
try {
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    console.info('AtomicFile write succeed!');
  })
} catch (err) {
  file.failWrite();
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]delete15+

delete(): void

删除AtomicFile类，会删除原始文件和临时文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      console.info('AtomicFile readFully str is: ' + str);
      file.delete();
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```

#### fileIo.createWatcher10+

createWatcher(path: string, events: number, listener: WatchEventListener): Watcher

创建Watcher对象，监听文件或目录变动。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 监听文件或目录的沙箱路径。 |
| events | number | 是 | 
监听变动的事件集，多个事件通过或(|)的方式进行集合。

\- 0x1: IN\_ACCESS， 文件被访问。

\- 0x2: IN\_MODIFY，文件内容被修改。

\- 0x4: IN\_ATTRIB，文件元数据被修改。

\- 0x8: IN\_CLOSE\_WRITE，文件在打开时进行了写操作，然后被关闭。

\- 0x10: IN\_CLOSE\_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。

\- 0x20: IN\_OPEN，文件或目录被打开。

\- 0x40: IN\_MOVED\_FROM，监听目录中文件被移动走。

\- 0x80: IN\_MOVED\_TO，监听目录中文件被移动过来。

\- 0x100: IN\_CREATE，监听目录中文件或子目录被创建。

\- 0x200: IN\_DELETE，监听目录中文件或子目录被删除。

\- 0x400: IN\_DELETE\_SELF，监听的目录被删除，删除后监听停止。

\- 0x800: IN\_MOVE\_SELF，监听的文件或目录被移动，移动后监听继续。

\- 0xfff: IN\_ALL\_EVENTS，监听以上所有事件。

 |
| listener | [WatchEventListener](#watcheventlistener10) | 是 | 监听事件发生后的回调。监听事件每发生一次，回调一次。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Watcher](#watcher10) | 返回Watcher对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { common } from '@kit.AbilityKit';
import { WatchEvent } from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let watcher = fileIo.createWatcher(filePath, 0x2 | 0x10, (watchEvent: WatchEvent) => {
  if (watchEvent.event == 0x2) {
    console.info(watchEvent.fileName + 'was modified');
  } else if (watchEvent.event == 0x10) {
    console.info(watchEvent.fileName + 'was closed');
  }
});
watcher.start();
fileIo.writeSync(file.fd, 'test');
fileIo.closeSync(file);
watcher.stop();
```

#### WatchEventListener10+

(event: WatchEvent): void

事件监听类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| event | [WatchEvent](#watchevent10) | 是 | 回调的事件类。 |

#### WatchEvent10+

事件类

#### \[h2\]属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| fileName | string | 是 | 否 | 发生监听事件对应文件的沙箱路径，该沙箱路径包含文件名称。 |
| event | number | 是 | 否 | 
监听变动的事件集，多个事件通过或(|)的方式进行集合。

\- 0x1: IN\_ACCESS， 文件被访问。

\- 0x2: IN\_MODIFY，文件内容被修改。

\- 0x4: IN\_ATTRIB，文件元数据被修改。

\- 0x8: IN\_CLOSE\_WRITE，文件在打开时进行了写操作，然后被关闭。

\- 0x10: IN\_CLOSE\_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。

\- 0x20: IN\_OPEN，文件或目录被打开。

\- 0x40: IN\_MOVED\_FROM，监听目录中文件被移动走。

\- 0x80: IN\_MOVED\_TO，监听目录中文件被移动过来。

\- 0x100: IN\_CREATE，监听目录中文件或子目录被创建。

\- 0x200: IN\_DELETE，监听目录中文件或子目录被删除。

\- 0x400: IN\_DELETE\_SELF，监听的目录被删除，删除后监听停止。

\- 0x800: IN\_MOVE\_SELF，监听的文件或目录被移动，移动后监听继续。

\- 0xfff: IN\_ALL\_EVENTS，监听以上所有事件。

 |
| cookie | number | 是 | 否 | 绑定相关事件的cookie。当前仅支持事件IN\_MOVED\_FROM与IN\_MOVED\_TO，同一个文件的移动事件IN\_MOVED\_FROM和IN\_MOVED\_TO具有相同的cookie值。 |

#### Progress11+

拷贝进度回调数据

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| processedSize | number | 是 | 否 | 已拷贝的数据大小，单位为Byte。 |
| totalSize | number | 是 | 否 | 待拷贝的数据总大小，单位为Byte。 |

#### TaskSignal12+

拷贝中断信号。

**系统能力**：SystemCapability.FileManagement.File.FileIO

#### \[h2\]cancel12+

cancel(): void

取消拷贝任务。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";
let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);
let copySignal = new fileIo.TaskSignal;
let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
  console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
  if (progress.processedSize / progress.totalSize > 0.5) {
    copySignal.cancel();
    console.info("copy cancel.");
  }
};
let options: fileIo.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}

try {
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, options, (err: BusinessError) => {
    if (err) {
      console.error("copy fail, err: ", err.message);
      return;
    }
    console.info("copy success.");
  })
} catch (err) {
  console.error("copyFileWithCancel failed, err: ", err.message);
}
```

#### \[h2\]onCancel12+

onCancel(): Promise<string>

取消拷贝事件监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象。最后一个拷贝的文件路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { TaskSignal } from '@kit.CoreFileKit';
let copySignal: fileIo.TaskSignal = new TaskSignal();
copySignal.onCancel();
```

#### CopyOptions11+

拷贝进度回调监听

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| progressListener | [ProgressListener](#progresslistener11) | 否 | 是 | 拷贝进度监听。 |
| copySignal | [TaskSignal](#tasksignal12) | 否 | 是 | 取消拷贝信号。 |

#### ProgressListener11+

拷贝进度监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 类型 | 说明 |
| :-- | :-- |
| (progress: [Progress](#progress11)) => void | 拷贝进度监听 |

**示例：**

```ts
import { TaskSignal } from '@kit.CoreFileKit';
let copySignal: fileIo.TaskSignal = new TaskSignal();
let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
  console.info(`processedSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let copyOption: fileIo.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}
```

#### Stat

文件具体信息，在调用Stat的方法前，需要先通过[stat()](#fileiostat)方法（同步或异步）构建一个Stat实例。

#### \[h2\]属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| ino | bigint | 是 | 否 | 标识该文件。通常同设备上的不同文件的INO不同。 |
| mode | number | 是 | 否 | 
表示文件权限，各特征位的含义如下：

**说明**：以下值为八进制，取得的返回值为十进制，请换算后查看。

\- 0o400：用户读。对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。

\- 0o200：用户写。对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。

\- 0o100：用户执行。对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。

\- 0o040：用户组读。对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。

\- 0o020：用户组写。对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。

\- 0o010：用户组执行。对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。

\- 0o004：其他读。对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。

\- 0o002：其他写。对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。

\- 0o001：其他执行。对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| uid | number | 是 | 否 | 文件所有者的ID。 |
| gid | number | 是 | 否 | 文件所有组的ID。 |
| size | number | 是 | 否 | 

文件的大小，单位为Byte。仅对普通文件有效。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| atime | number | 是 | 否 | 

上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。

**注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| mtime | number | 是 | 否 | 

上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| ctime | number | 是 | 否 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| atimeNs15+ | bigint | 是 | 是 | 

上次访问该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。

**注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。

 |
| mtimeNs15+ | bigint | 是 | 是 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。 |
| ctimeNs15+ | bigint | 是 | 是 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的纳秒数。 |
| location11+ | [LocationType](#locationtype11) | 是 | 否 | 文件的位置，表示该文件是本地文件或者云端文件。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/lttTTjqGREuPLhIv-_pRdA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=99C669D5F9C9CA8C3540AE69E87C2B086ADCFF115A0E8CA8B8A8F102FB081ADB)

Stat中部分属性仅支持普通文件获取，开发者可通过[isFile()](#isfile)接口判断文件是否为普通文件。

#### \[h2\]isBlockDevice

isBlockDevice(): boolean

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是块特殊设备。true：是块特殊设备；false：不是块特殊设备。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isBLockDevice = fileIo.statSync(filePath).isBlockDevice();
```

#### \[h2\]isCharacterDevice

isCharacterDevice(): boolean

判断文件是否为字符特殊文件。字符特殊设备支持随机访问，且访问时无缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是字符特殊设备。true：是字符特殊设备；false：不是字符特殊设备。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isCharacterDevice = fileIo.statSync(filePath).isCharacterDevice();
```

#### \[h2\]isDirectory

isDirectory(): boolean

判断文件是否为目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是目录。true：是目录；false：不是目录。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let dirPath = pathDir + "/test";
let isDirectory = fileIo.statSync(dirPath).isDirectory();
```

#### \[h2\]isFIFO

isFIFO(): boolean

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是 FIFO。true：是FIFO；false：不是FIFO。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isFIFO = fileIo.statSync(filePath).isFIFO();
```

#### \[h2\]isFile

isFile(): boolean

用于判断文件是否是普通文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是普通文件。true：是普通文件；false：不是普通文件。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isFile = fileIo.statSync(filePath).isFile();
```

#### \[h2\]isSocket

isSocket(): boolean

判断文件是否是套接字。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是套接字。true：是套接字；false：不是套接字。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isSocket = fileIo.statSync(filePath).isSocket();
```

#### \[h2\]isSymbolicLink

isSymbolicLink(): boolean

判断文件是否为符号链接。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 表示文件是否是符号链接。true：是符号链接；false：不是符号链接。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let isSymbolicLink = fileIo.statSync(filePath).isSymbolicLink();
```

#### Stream

文件流，在调用Stream的方法前，需要先通过[fileIo.createStream](#fileiocreatestream)方法或者[fileIo.fdopenStream](#fileiofdopenstream)（同步或异步）来构建一个Stream实例。

#### \[h2\]close

close(): Promise<void>

关闭文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### \[h2\]close

close(callback: AsyncCallback<void>): void

异步关闭文件流，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 异步关闭文件流之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.close((err: BusinessError) => {
  if (err) {
    console.error("close stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close stream succeed");
  }
});
```

#### \[h2\]closeSync

closeSync(): void

同步关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.closeSync();
```

#### \[h2\]flush

flush(): Promise<void>

刷新文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。返回表示异步刷新文件流的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flush().then(() => {
  console.info("flush succeed");
  stream.close();
}).catch((err: BusinessError) => {
  console.error("flush failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### \[h2\]flush

flush(callback: AsyncCallback<void>): void

异步刷新文件流，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 异步刷新文件流后的回调函数。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flush((err: BusinessError) => {
  if (err) {
    console.error("flush stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("flush succeed");
    stream.close();
  }
});
```

#### \[h2\]flushSync

flushSync(): void

同步刷新文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flushSync();
stream.close();
```

#### \[h2\]write

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入流文件，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望写入数据的长度，单位为Byte。默认缓冲区长度。

\- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption).then((number: number) => {
  console.info("write succeed and size is:" + number);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("write failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### \[h2\]write

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入流文件，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

\- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

 |
| callback | AsyncCallback<number> | 是 | 异步写入完成后执行的回调函数。返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  stream.close();
});
```

#### \[h2\]writeSync

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入流文件。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

\- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath,"r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let num = stream.writeSync("hello, world", writeOption);
stream.close();
```

#### \[h2\]read

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

从流文件读取数据，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回读取的结果，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption).then((readLen: number) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`The content of file: ${buf.toString()}`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("read data failed with error message: " + err.message + ", error code: " + err.code);
});
```

#### \[h2\]read

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从流文件读取数据，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。

 |
| callback | AsyncCallback<number> | 是 | 异步读取完成后的回调。返回读取的结果，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`The content of file: ${buf.toString()}`);
    stream.close();
  }
});
```

#### \[h2\]readSync

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从流文件读取数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。

\- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际读取的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
let buf = new ArrayBuffer(4096);
let num = stream.readSync(buf, readOption);
stream.close();
```

#### File

由open接口打开的File对象。

#### \[h2\]属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | 是 | 否 | 
打开的文件描述符。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| path10+ | string | 是 | 否 | 文件路径。 |
| name10+ | string | 是 | 否 | 文件名。 |

#### \[h2\]getParent11+

getParent(): string

获取File对象对应文件父目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回父目录路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
console.info('The parent path is: ' + file.getParent());
fileIo.closeSync(file);
```

#### \[h2\]lock

lock(exclusive?: boolean): Promise<void>

对文件阻塞式施加共享锁或独占锁，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock(true).then(() => {
  console.info("lock file succeed");
}).catch((err: BusinessError) => {
  console.error("lock file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fileIo.closeSync(file);
});
```

#### \[h2\]lock

lock(exclusive?: boolean, callback: AsyncCallback<void>): void

对文件阻塞式施加共享锁或独占锁，使Callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |
| callback | AsyncCallback<void> | 是 | 异步文件上锁之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock(true, (err: BusinessError) => {
  if (err) {
    console.error("lock file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("lock file succeed");
  }
  fileIo.closeSync(file);
});
```

#### \[h2\]tryLock

tryLock(exclusive?: boolean): void

文件非阻塞式施加共享锁或独占锁。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.tryLock(true);
console.info("lock file succeed");
fileIo.closeSync(file);
```

#### \[h2\]unlock

unlock(): void

以同步方式解锁文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.tryLock(true);
file.unlock();
console.info("unlock file succeed");
fileIo.closeSync(file);
```

#### fileIo.DfsListeners12+

事件监听类。创建DFSListener对象，用于监听分布式文件系统状态。

**系统能力**：SystemCapability.FileManagement.File.FileIO

#### \[h2\]onStatus12+

onStatus(networkId: string, status: number): void;

事件回调类。参数由[connectDfs](#fileioconnectdfs12)传入。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| networkId | string | 是 | 设备的网络Id。 |
| status | number | 是 | 
分布式文件系统的状态码（以connectDfs回调onStatus的特定错误码作为入参）。触发场景为connectDfs调用过程中出现对端设备异常，对应错误码为：

\- [13900046](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#section13900046-软件造成连接中断)：软件造成连接中断。

 |

#### RandomAccessFile10+

随机读写文件流。在调用RandomAccessFile的方法前，需要先通过createRandomAccessFile()方法（同步或异步）来构建一个RandomAccessFile实例。

#### \[h2\]属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | 是 | 否 | 打开的文件描述符。 |
| filePointer | number | 是 | 否 | RandomAccessFile对象的偏移指针，单位为Byte。 |

#### \[h2\]setFilePointer10+

setFilePointer(filePointer:number): void

设置文件偏移指针。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filePointer | number | 是 | RandomAccessFile对象的偏移指针，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
randomAccessFile.setFilePointer(1);
randomAccessFile.close();
```

#### \[h2\]close10+

close(): void

以同步方式关闭RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
randomAccessFile.close();
```

#### \[h2\]write10+

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入文件，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望写入数据的长度，单位为Byte。默认缓冲区长度。

\- offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: 5,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: number) => {
  console.info("randomAccessFile bytesWritten: " + bytesWritten);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

#### \[h2\]write10+

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认为缓冲区长度。

\- offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

 |
| callback | AsyncCallback<number> | 是 | 异步写入完成后执行的回调函数。返回实际写入数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: bufferLength,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

#### \[h2\]writeSync10+

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](#writeoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

\- offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

\- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let bytesWritten = randomAccessFile.writeSync("hello, world", writeOption);
randomAccessFile.close();
```

#### \[h2\]read10+

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

从文件读取数据，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认为缓冲区长度。

\- offset，number类型，表示期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回读取的结果，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.read(arrayBuffer, readOption).then((readLength: number) => {
  console.info("randomAccessFile readLength: " + readLength);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

#### \[h2\]read10+

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从文件读取数据，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示读取数据的长度，单位为Byte。可选，默认为缓冲区长度。

\- offset，number类型，表示读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从filePointer开始读。

 |
| callback | AsyncCallback<number> | 是 | 异步读取完成后的回调。返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 20;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (readLength) {
      console.info("read succeed and size is:" + readLength);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

#### \[h2\]readSync10+

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](#readoptions11) | 否 | 
支持如下选项：

\- length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。

\- offset，number类型，表示期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 实际读取的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 4096;
let arrayBuffer = new ArrayBuffer(length);
let readLength = randomAccessFile.readSync(arrayBuffer);
randomAccessFile.close();
fileIo.closeSync(file);
```

#### \[h2\]getReadStream12+

getReadStream(): ReadStream

获取当前 RandomAccessFile 的一个 ReadStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ReadStream](#readstream12) | 文件可读流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
const filePath = pathDir + "/test.txt";
const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
const rs = randomAccessFile.getReadStream();
rs.close();
randomAccessFile.close();
```

#### \[h2\]getWriteStream12+

getWriteStream(): WriteStream

获取当前 RandomAccessFile 的一个 WriteStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WriteStream](#writestream12) | 文件可写流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
const filePath = pathDir + "/test.txt";
const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
const ws = randomAccessFile.getWriteStream();
ws.close();
randomAccessFile.close();
```

#### Watcher10+

文件目录变化监听对象。由createWatcher接口获得。

#### \[h2\]start10+

start(): void

开启监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

#### \[h2\]stop10+

stop(): void

停止监听并移除Watcher对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

#### OpenMode

open接口flags参数常量。文件打开标签。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 值 | 说明 |
| :-- | :-- | :-- | :-- |
| READ\_ONLY | number | 0o0 | 
只读打开。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| WRITE\_ONLY | number | 0o1 | 

只写打开。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| READ\_WRITE | number | 0o2 | 

读写打开。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| CREATE | number | 0o100 | 

若文件不存在，则创建文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| TRUNC | number | 0o1000 | 

如果文件存在且以只写或读写的方式打开，则将其长度裁剪为零。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| APPEND | number | 0o2000 | 

以追加方式打开，后续写将追加到文件末尾。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| NONBLOCK | number | 0o4000 | 如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 |
| DIR | number | 0o200000 | 如果path不指向目录，则出错。 |
| NOFOLLOW | number | 0o400000 | 如果path指向符号链接，则出错。 |
| SYNC | number | 0o4010000 | 以同步IO的方式打开文件。 |

#### Filter10+

文件过滤配置项，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| suffix | Array<string> | 否 | 是 | 文件后缀名完全匹配，各个关键词OR关系。 |
| displayName | Array<string> | 否 | 是 | 文件名模糊匹配，各个关键词OR关系。当前仅支持通配符\*。 |
| mimeType | Array<string> | 否 | 是 | mime类型完全匹配，各个关键词OR关系。预留字段，暂不支持使用。 |
| fileSizeOver | number | 否 | 是 | 文件大小匹配，大于指定大小的文件，单位为Byte。 |
| lastModifiedAfter | number | 否 | 是 | 文件最近修改时间匹配，在指定时间点及之后的文件。 |
| excludeMedia | boolean | 否 | 是 | 是否排除Media中已有的文件。true：排除Media中已有的文件；false：不排除Media中已有的文件。 |

#### ConflictFiles10+

冲突文件信息，支持copyDir及moveDir接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| srcFile | string | 源冲突文件路径。 |
| destFile | string | 目标冲突文件路径。 |

#### Options11+

可选项类型，支持readLines接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| encoding | string | 文件编码方式。可选项。 |

#### WhenceType11+

枚举，文件偏移指针相对偏移位置类型，支持lseek接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SEEK\_SET | 0 | 文件起始位置处。 |
| SEEK\_CUR | 1 | 当前文件偏移指针位置处。 |
| SEEK\_END | 2 | 文件末尾位置处。 |

#### LocationType11+

枚举，文件位置，表示该文件是否在本地或者云端存在。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| LOCAL | 1 | 文件在本地存在。 |
| CLOUD | 2 | 文件在云端存在。 |

#### AccessModeType12+

枚举，表示需要校验的具体权限。若不填，默认校验文件是否存在。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| EXIST | 0 | 文件是否存在。 |
| WRITE | 2 | 文件是否具有写入权限。 |
| READ | 4 | 文件是否具有读取权限。 |
| READ\_WRITE | 6 | 文件是否具有读写权限。 |

#### AccessFlagType12+

枚举，表示需要校验的文件位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| LOCAL | 0 | 文件是否在本地。 |

#### ReadOptions11+

可选项类型，支持read接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| offset | number | 否 | 是 | 期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。 |
| length | number | 否 | 是 | 期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |

#### ReadTextOptions11+

可选项类型，支持readText接口使用，ReadTextOptions继承至[ReadOptions](#readoptions11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| offset | number | 否 | 是 | 期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 |
| length | number | 否 | 是 | 期望读取数据的长度，单位为Byte。可选，默认文件长度。 |
| encoding | string | 否 | 是 | 
当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |

#### WriteOptions11+

可选项类型，支持write接口使用，WriteOptions继承至[Options](#options11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| offset | number | 否 | 是 | 
期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| length | number | 否 | 是 | 

期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| encoding | string | 否 | 是 | 当数据是string类型时有效，表示数据的编码方式。默认 'utf-8'。仅支持 'utf-8'。 |

#### ListFileOptions11+

可选项类型，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| recursion | boolean | 否 | 是 | 是否递归子目录下文件名。可选，默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及目录名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。 |
| listNum | number | 否 | 是 | 列出文件名数量。可选，当设置0时，列出所有文件，默认为0。 |
| filter | [Filter](#filter10) | 否 | 是 | 文件过滤配置项。 可选，设置过滤条件。 |

#### ReadStream12+

文件可读流，需要先通过[fileIo.createReadStream](#fileiocreatereadstream12)方法来构建一个ReadStream实例。ReadStream继承自数据流基类[stream.Readable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stream#readable)。

**规格**：ReadStream读到的数据为解码后的字符串，其编码格式当前仅支持'utf-8'。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bytesRead | number | 是 | 否 | 可读流已经读取的字节数。 |
| path | string | 是 | 否 | 当前可读流对应的文件路径。 |

#### \[h2\]seek12+

seek(offset: number, whence?: WhenceType): number

调整可读流偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](#whencetype11) | 否 | 偏移指针相对位置类型。默认值：SEEK\_SET，文件起始位置处。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 当前可读流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
const curOff = rs.seek(5, fileIo.WhenceType.SEEK_SET);
console.info(`current offset is ${curOff}`);
rs.close();
```

#### \[h2\]close12+

close(): void

关闭可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
rs.close();
```

#### WriteStream12+

文件可写流，需要先通过[fileIo.createWriteStream](#fileiocreatewritestream12)方法来构建一个WriteStream实例。WriteStream继承自数据流基类[stream.Writable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stream#writable)。

#### \[h2\]属性

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bytesWritten | number | 是 | 否 | 可写流已经写入的字节数。 |
| path | string | 是 | 否 | 当前可写流对应的文件路径。 |

#### \[h2\]seek12+

seek(offset: number, whence?: WhenceType): number;

调整可写流的偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](#whencetype11) | 否 | 偏移指针相对位置类型。默认值：SEEK\_SET，文件起始位置处。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 当前可写流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```ts
const filePath = pathDir + "/test.txt";
const ws = fileIo.createWriteStream(filePath);
const curOff = ws.seek(5, fileIo.WhenceType.SEEK_SET);
console.info(`current offset is ${curOff}`);
ws.close();
```

#### \[h2\]close12+

close(): void

关闭可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```ts
const filePath = pathDir + "/test.txt";
const ws = fileIo.createWriteStream(filePath);
ws.close();
```

#### RandomAccessFileOptions12+

可选项类型，支持 createRandomAccessFile 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | number | 否 | 是 | 表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |
| end | number | 否 | 是 | 表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |

#### ReadStreamOptions12+

可选项类型，支持 createReadStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | number | 否 | 是 | 表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |
| end | number | 否 | 是 | 表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |

#### WriteStreamOptions12+

可选项类型，支持 createWriteStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | number | 否 | 是 | 表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 |
| mode | number | 否 | 是 | 
创建文件可写流的[选项](#openmode)，必须指定如下选项中的一个，默认只写方式创建：

\- OpenMode.READ\_ONLY(0o0)：只读。

\- OpenMode.WRITE\_ONLY(0o1)：只写。

\- OpenMode.READ\_WRITE(0o2)：读写。

给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：

\- OpenMode.CREATE(0o100)：若文件不存在，则创建文件。

\- OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。

\- OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。

\- OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

\- OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。

\- OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。

\- OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。

 |
