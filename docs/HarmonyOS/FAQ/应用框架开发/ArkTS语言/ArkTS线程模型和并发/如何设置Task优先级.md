---
title: "如何设置Task优先级"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-26"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "ArkTS线程模型和并发"
  - "如何设置Task优先级"
captured_at: "2026-04-17T02:03:01.109Z"
---

# 如何设置Task优先级

设置任务优先级，示例如下：

import { taskpool } from '@kit.ArkTS';

@Concurrent
function printArgs(args: number): number {
  console.log("printArgs: " + args);
  return args;
}

let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
taskpool.execute(task, taskpool.Priority.HIGH).then((res) => {
  console.log("taskpool result is :" + res);
});

-   HIGH：值为0，表示任务是高优先级。
-   MEDIUM：值为1，表示任务是中优先级。
-   LOW：值为2，表示任务是低优先级。

**参考链接**

[Priority](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#priority)
