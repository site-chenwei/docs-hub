---
title: "Native侧如何获取可操作的文件目录"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-38"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何获取可操作的文件目录"
captured_at: "2026-04-17T02:03:01.997Z"
---

# Native侧如何获取可操作的文件目录

当前native侧暂无可直接获取文件目录的接口，可以通过ArkTS侧获取相关路径信息，然后传递到native侧使用。

ArkTS侧获取路径信息代码示例：

import { common } from '@kit.AbilityKit';

const context = AppStorage.get("context") as UIContext;
let hostContext = context.getHostContext() as common.UIAbilityContext;
let filesDir = hostContext.filesDir;
