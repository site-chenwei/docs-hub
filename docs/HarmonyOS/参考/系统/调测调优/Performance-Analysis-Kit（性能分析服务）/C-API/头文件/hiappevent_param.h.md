---
title: "hiappevent_param.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-param-h"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "C API"
  - "头文件"
  - "hiappevent_param.h"
captured_at: "2026-04-17T01:48:34.876Z"
---

# hiappevent\_param.h

#### 概述

定义所有预定义事件的参数名称。除了与特定应用关联的自定义事件之外，开发者还可以使用预定义事件进行打点。

**引用文件：** <hiappevent/hiappevent\_param.h>

**库：** libhiappevent\_ndk.z.so

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 8

**相关模块：** [HiAppEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent)

#### 汇总

#### \[h2\]宏定义

| 名称 | 描述 |
| :-- | :-- |
| [PARAM\_USER\_ID](#param_user_id) "user\_id" | 
用户ID。

**起始版本：** 8

 |
| [PARAM\_DISTRIBUTED\_SERVICE\_NAME](#param_distributed_service_name) "ds\_name" | 

分布式服务名称。

**起始版本：** 8

 |
| [PARAM\_DISTRIBUTED\_SERVICE\_INSTANCE\_ID](#param_distributed_service_instance_id) "ds\_instance\_id" | 

分布式服务实例ID。

**起始版本：** 8

 |
| [MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE](#main_thread_jank_param_log_type) "log\_type" | 

用于MAIN\_THREAD\_JANK\_V2事件，主线程超时检测采集日志的类型。

**起始版本：** 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL](#main_thread_jank_param_sample_interval) "sample\_interval" | 

用于MAIN\_THREAD\_JANK\_V2事件，主线程超时检测间隔和采样间隔。

**起始版本：** 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_IGNORE\_STARTUP\_TIME](#main_thread_jank_param_ignore_startup_time) "ignore\_startup\_time" | 

用于MAIN\_THREAD\_JANK\_V2事件，应用启动期间忽略主线程超时检测的时间。

**起始版本：** 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT](#main_thread_jank_param_sample_count) "sample\_count" | 

用于MAIN\_THREAD\_JANK\_V2事件，主线程超时检测的采样栈的次数。

**起始版本：** 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_REPORT\_TIMES\_PER\_APP](#main_thread_jank_param_report_times_per_app) "report\_times\_per\_app" | 

用于MAIN\_THREAD\_JANK\_V2事件，每个应用PID一个生命周期内，主线程超时采样上报的次数，一个生命周期内只能设置一次。

**起始版本：** 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING](#main_thread_jank_param_auto_stop_sampling) "auto\_stop\_sampling" | 

用于MAIN\_THREAD\_JANK\_V2事件，主线程超时结束时，是否停止采样主线程堆栈。

**起始版本：** 22

 |

#### 宏定义说明

#### \[h2\]PARAM\_USER\_ID

```c
#define PARAM_USER_ID "user_id"
```

**描述**

用户ID。

**起始版本：** 8

#### \[h2\]PARAM\_DISTRIBUTED\_SERVICE\_NAME

```c
#define PARAM_DISTRIBUTED_SERVICE_NAME "ds_name"
```

**描述**

分布式服务名称。

**起始版本：** 8

#### \[h2\]PARAM\_DISTRIBUTED\_SERVICE\_INSTANCE\_ID

```c
#define PARAM_DISTRIBUTED_SERVICE_INSTANCE_ID "ds_instance_id"
```

**描述**

分布式服务实例ID。

**起始版本：** 8

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE

```c
#define MAIN_THREAD_JANK_PARAM_LOG_TYPE "log_type"
```

**描述**

用于MAIN\_THREAD\_JANK\_V2事件，主线程超时检测采集日志的类型。

**起始版本：** 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL

```c
#define MAIN_THREAD_JANK_PARAM_SAMPLE_INTERVAL "sample_interval"
```

**描述**

用于MAIN\_THREAD\_JANK\_V2事件，主线程超时检测间隔和采样间隔。

**起始版本：** 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_IGNORE\_STARTUP\_TIME

```c
#define MAIN_THREAD_JANK_PARAM_IGNORE_STARTUP_TIME "ignore_startup_time"
```

**描述**

用于MAIN\_THREAD\_JANK\_V2事件，应用启动期间忽略主线程超时检测的时间。

**起始版本：** 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT

```c
#define MAIN_THREAD_JANK_PARAM_SAMPLE_COUNT "sample_count"
```

**描述**

用于MAIN\_THREAD\_JANK\_V2事件，主线程超时检测的采样栈的次数。

**起始版本：** 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_REPORT\_TIMES\_PER\_APP

```c
#define MAIN_THREAD_JANK_PARAM_REPORT_TIMES_PER_APP "report_times_per_app"
```

**描述**

用于MAIN\_THREAD\_JANK\_V2事件，每个应用PID一个生命周期内，主线程超时采样上报的次数，一个生命周期内只能设置一次。

**起始版本：** 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING

```c
#define MAIN_THREAD_JANK_PARAM_AUTO_STOP_SAMPLING "auto_stop_sampling"
```

**描述**

用于MAIN\_THREAD\_JANK\_V2事件，是否停止采样主线程堆栈。

**起始版本：** 22
