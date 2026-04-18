---
title: "@ohos.bytrace (性能打点)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bytrace"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.bytrace (性能打点)"
captured_at: "2026-04-17T01:48:34.656Z"
---

# @ohos.bytrace (性能打点)

本模块提供了追踪进程轨迹。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/6aUIRQWXRGOdAuih4OBEig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014836Z&HW-CC-Expire=86400&HW-CC-Sign=C9C11C3C036FE92BF7CEF6BAB509FB2422D2B1B1F5FA5163BE1FB275D134D529)

-   本模块接口从API Version 8开始废弃，建议使用新接口[@ohos.hiTraceMeter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter)替代。
-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { bytrace } from '@kit.PerformanceAnalysisKit';
```

#### bytrace.startTrace

startTrace(name: string, taskId: number, expectedTime?: number): void

标记一个时间片跟踪任务的开始。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/GW9XbUFUTH6yeL9cNGDRNQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014836Z&HW-CC-Expire=86400&HW-CC-Sign=BFB0B4EDD0B04790D51ED4E8142E57724813AE9246A26DC63FCCAEB39FAA69F9)

如果有多个相同name的任务需要追踪或者对同一个任务要追踪多次，并且这些跟踪任务会同时被执行，则每次调用startTrace的taskId必须不一致。如果具有相同name的跟踪任务是串行执行的，则taskId可以相同。在下面bytrace.finishTrace的示例中会举例说明。

**系统能力**： SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 时间片跟踪任务名称。 |
| taskId | number | 是 | 时间片跟踪任务id。 |
| expectedTime | number | 否 | 期望的耗时时间（单位：ms）。可选，默认为空。 |

**示例：**

```ts
bytrace.startTrace("myTestFunc", 1);
bytrace.startTrace("myTestFunc", 1, 5); // 从startTrace到finishTrace流程的期望耗时为5ms
```

#### bytrace.finishTrace

finishTrace(name: string, taskId: number): void

标记一个时间片跟踪事件的结束。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/0ldt5yY_RwqPlASVbOc8eg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014836Z&HW-CC-Expire=86400&HW-CC-Sign=4E7317F575FC070DED088F9B269A56C872A4DBA615042BB6396585C9B50A3CA5)

finishTrace的name和taskId必须与流程开始的startTrace对应参数值一致。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 时间片跟踪任务名称。 |
| taskId | number | 是 | 时间片跟踪任务id。 |

**示例：**

```ts
bytrace.finishTrace("myTestFunc", 1);
```

```ts
// 跟踪并行执行的同名任务
bytrace.startTrace("myTestFunc", 1);
// 业务流程......
bytrace.startTrace("myTestFunc", 2);  // 第二个跟踪任务开始，同时第一个同名跟踪任务还没结束，出现了并行执行，对应接口的taskId需要不同
// 业务流程......
bytrace.finishTrace("myTestFunc", 1);
// 业务流程......
bytrace.finishTrace("myTestFunc", 2);
```

```ts
// 跟踪串行执行的同名任务
bytrace.startTrace("myTestFunc", 1);
// 业务流程......
bytrace.finishTrace("myTestFunc", 1);  // 第一个跟踪任务结束
// 业务流程......
bytrace.startTrace("myTestFunc", 1);   // 第二个跟踪任务开始，同名跟踪任务串行执行
// 业务流程......
bytrace.finishTrace("myTestFunc", 1);
```

#### bytrace.traceByValue

traceByValue(name: string, count: number): void

标记预追踪耗时任务的数值变量，该变量的数值会不断变化。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 数值变量的名称。 |
| count | number | 是 | 数值变量的值 |

**示例：**

```ts
let traceCount = 3;
bytrace.traceByValue("myTestCount", traceCount);
traceCount = 4;
bytrace.traceByValue("myTestCount", traceCount);
// 业务流程......
```
