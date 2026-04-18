---
title: "如何写har包的编译脚本"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-64"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何写har包的编译脚本"
captured_at: "2026-04-17T02:03:21.850Z"
---

# 如何写har包的编译脚本

在har包目录下的hvigorfile.ts文件中编写代码如下：

import { harTasks } from '@ohos/hvigor-ohos-plugin';

function harTask(): HvigorPlugin {
    return {
        pluginId: 'harTask',
        apply(node: HvigorNode) {
            console.log('hello harTasks!');
        }
    }
}

export default {
    system: harTasks,
    plugins: \[harTask()\]
}
