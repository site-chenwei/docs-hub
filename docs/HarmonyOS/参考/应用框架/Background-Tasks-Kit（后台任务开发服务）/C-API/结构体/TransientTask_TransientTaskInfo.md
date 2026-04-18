---
title: "TransientTask_TransientTaskInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-transienttaskinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Background Tasks Kit（后台任务开发服务）"
  - "C API"
  - "结构体"
  - "TransientTask_TransientTaskInfo"
captured_at: "2026-04-17T01:48:13.681Z"
---

# TransientTask\_TransientTaskInfo

```c
typedef struct TransientTask_TransientTaskInfo {...} TransientTask_TransientTaskInfo
```

#### 概述

定义所有短时任务信息结构体。用于返回当日剩余总配额和已申请的所有短时任务信息。

**起始版本：** 20

**相关模块：** [TransientTask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask)

**所在头文件：** [transient\_task\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t remainingQuota | 当日剩余总配额。单位：毫秒。 |
| [TransientTask\_DelaySuspendInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-delaysuspendinfo) transientTasks\[[TRANSIENT\_TASK\_MAX\_NUM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-type-h#宏定义)\] | 已申请的所有短时任务信息。包括短时任务请求ID、剩余时间（单位：毫秒）。 |
