---
title: "如何在构建任务中执行shell脚本"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-104"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何在构建任务中执行shell脚本"
captured_at: "2026-04-17T02:03:22.305Z"
---

# 如何在构建任务中执行shell脚本

在hvigorfile.ts文件中执行如下示例：

import { harTasks } from '@ohos/hvigor-ohos-plugin';
import { exec } from 'node:child\_process';
import util from 'node:util';

const scriptPath = 'xxxx.bat';

export function customPluginFunction1(str?: string) {
  return {
    pluginId: 'CustomPluginID1',
    apply(pluginContext) {
      pluginContext.registerTask({
       // Write a custom task
        name: 'customTask1',
        run: (taskContext) => {
          console.log('run into: ');
          const execPromise = util.promisify(exec)
          execPromise(scriptPath).then(res => {
            console.log(res, 'res');
          }).catch(err => {
            console.log(err, 'err');
          })
        },
        // Confirm custom task insertion position
        dependencies: \['default@BuildJS'\],
        postDependencies: \['default@CompileArkTS'\]
      })
    }
  }
}

export default {
  system: harTasks, /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins: \[customPluginFunction1()\] /\* Custom plugin to extend the functionality of Hvigor. \*/
}
