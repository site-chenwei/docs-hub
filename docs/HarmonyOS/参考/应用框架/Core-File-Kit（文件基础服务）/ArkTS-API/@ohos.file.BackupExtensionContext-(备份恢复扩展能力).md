---
title: "@ohos.file.BackupExtensionContext (备份恢复扩展能力)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-backupextensioncontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "ArkTS API"
  - "@ohos.file.BackupExtensionContext (备份恢复扩展能力)"
captured_at: "2026-04-17T01:48:14.095Z"
---

# @ohos.file.BackupExtensionContext (备份恢复扩展能力)

BackupExtensionContext是BackupExtension的上下文环境，继承自ExtensionContext。

BackupExtensionContext模块提供访问特定BackupExtension的资源的能力。对于拓展的BackupExtension，可直接将BackupExtensionContext作为上下文环境，或者定义一个继承自BackupExtensionContext的类型作为上下文环境。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Ws2_50_9SG2eefM2lUHfww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=41C11861A20A1E89646CEAB4D2218C6CBD9C04904D0FAE84425CE09B700F2927)

-   本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import  { BackupExtensionContext } from '@kit.CoreFileKit';
```

#### BackupExtensionContext

#### \[h2\]属性

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| backupDir | string | 是 | 否 | 获取备份恢复时的临时路径，该路径只允许在备份恢复过程中作为临时路径使用，不允许应用将该路径作为其他用途来使用。目前只支持el1, el2路径，使用其他路径会返回空值。 |

#### \[h2\]使用场景

BackupExtensionContext主要用于获取备份恢复过程中的临时路径。

**示例：**

```ts
import { BackupExtensionAbility } from '@kit.CoreFileKit';
import { contextConstant } from '@kit.AbilityKit';

export default class MyBackupExtAbility extends BackupExtensionAbility {
    async onBackup() {
        console.info("onBackup begin");
        // 使用者可通过改变 this.context.area 来进行切换el1，el2对应的沙箱路径
        this.context.area = contextConstant.AreaMode.EL1;
        // 使用者可通过 this.context.backupDir 对沙箱路径进行获取
        let dir = this.context.backupDir;
        console.info(`onBackup el1 dir: ${dir}`);
        this.context.area = contextConstant.AreaMode.EL2;
        dir = this.context.backupDir;
        console.info(`onBackup el2 dir: ${dir}`);
        console.info("onBackup end");
    }

    async onRestore() {
        console.info("onRestore begin");
        this.context.area = contextConstant.AreaMode.EL1;
        let dir = this.context.backupDir;
        console.info(`onRestore el1 dir: ${dir}`);
        this.context.area = contextConstant.AreaMode.EL2;
        dir = this.context.backupDir;
        console.info(`onRestore el2 dir: ${dir}`);
        console.info("onRestore end");
    }
}
```
