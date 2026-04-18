---
title: "短时任务(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-transient-task"
menu_path:
  - "指南"
  - "应用框架"
  - "Background Tasks Kit（后台任务开发服务）"
  - "短时任务(C/C++)"
captured_at: "2026-04-17T01:35:42.939Z"
---

# 短时任务(C/C++)

#### 场景介绍

应用退至后台一小段时间后，应用进程会被挂起，无法执行对应的任务。如果应用在后台仍需要执行耗时不长的任务，如状态保存等，可以通过本文申请短时任务，扩展应用在后台的运行时间。

#### 约束与限制

申请短时任务的按钮，不可连续点击超过3次，否则会超出短时任务数量限制并报错。使用过程中更多的约束与限制请参考短时任务（ArkTS）的[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/transient-task#约束与限制)。

#### 接口说明

常用接口如下表所示，具体API说明详见[transient\_task\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-api-h)。

| 接口名 | 描述 |
| :-- | :-- |
| [int32\_t OH\_BackgroundTaskManager\_RequestSuspendDelay(const char \*reason, TransientTask\_Callback callback, TransientTask\_DelaySuspendInfo \*info)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_requestsuspenddelay) | 申请短时任务。 |
| [int32\_t OH\_BackgroundTaskManager\_GetRemainingDelayTime(int32\_t requestId, int32\_t \*delayTime)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_getremainingdelaytime) | 获取对应短时任务的剩余时间。 |
| [int32\_t OH\_BackgroundTaskManager\_CancelSuspendDelay(int32\_t requestId)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_cancelsuspenddelay) | 取消短时任务。 |
| [int32\_t OH\_BackgroundTaskManager\_GetTransientTaskInfo(TransientTask\_TransientTaskInfo \*transientTaskInfo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_gettransienttaskinfo) | 获取所有短时任务信息，如当日剩余总配额等。 |

#### 开发步骤

#### \[h2\]在napi\_init.cpp文件中封装接口并注册模块

1.  封装函数
    
    #include "napi/native\_api.h"
    #include "transient\_task/transient\_task\_api.h"
    
    TransientTask\_DelaySuspendInfo delaySuspendInfo;
    const int32\_t TransientTask\_TIMER = 3;
    static void Callback(void)
    {
        // 短时任务即将结束，业务在这里取消短时任务
        OH\_BackgroundTaskManager\_CancelSuspendDelay(delaySuspendInfo.requestId);
    }
    
    // 申请短时任务
    static napi\_value RequestSuspendDelay(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        int32\_t res = OH\_BackgroundTaskManager\_RequestSuspendDelay("test", Callback, &delaySuspendInfo);
        if (res == 0) {
            napi\_create\_int32(env, delaySuspendInfo.requestId, &result);
        } else {
            napi\_create\_int32(env, -1, &result);
        }
        return result;
    }
    
    // 获取剩余时间
    static napi\_value GetRemainingDelayTime(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        int32\_t delayTime = 0;
        int32\_t res = OH\_BackgroundTaskManager\_GetRemainingDelayTime(delaySuspendInfo.requestId, &delayTime);
        if (res == 0) {
            napi\_create\_int32(env, delayTime, &result);
        } else {
            napi\_create\_int32(env, -1, &result);
        }
        return result;
    }
    
    // 取消短时任务
    static napi\_value CancelSuspendDelay(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        int32\_t res = OH\_BackgroundTaskManager\_CancelSuspendDelay(delaySuspendInfo.requestId);
        napi\_create\_int32(env, res, &result);
        return result;
    }
    
    // 获取所有短时任务信息
    TransientTask\_TransientTaskInfo transientTaskInfo;
    
    static napi\_value GetTransientTaskInfo(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        napi\_create\_object(env, &result);
        int32\_t res = OH\_BackgroundTaskManager\_GetTransientTaskInfo(&transientTaskInfo);
        napi\_value napiRemainingQuota = nullptr;
        // 获取成功，格式化数据并返回给接口
        if (res == 0) {
            napi\_create\_int32(env, transientTaskInfo.remainingQuota, &napiRemainingQuota);
            napi\_set\_named\_property(env, result, "remainingQuota", napiRemainingQuota); // 格式化当日总配额
    
            napi\_value info {nullptr};
            napi\_create\_array(env, &info);
            uint32\_t count = 0;
            // 格式化所有已申请的短时任务信息
            for (int index = 0; index < TransientTask\_TIMER; index++) {
                if (transientTaskInfo.transientTasks\[index\].requestId == 0) {
                    continue;
                }
                
                napi\_value napiWork = nullptr;
                napi\_create\_object(env, &napiWork);
    
                napi\_value napiRequestId = nullptr;
                napi\_create\_int32(env, transientTaskInfo.transientTasks\[index\].requestId, &napiRequestId);
                napi\_set\_named\_property(env, napiWork, "requestId", napiRequestId);
    
                napi\_value napiActualDelayTime = nullptr;
                napi\_create\_int32(env, transientTaskInfo.transientTasks\[index\].actualDelayTime, &napiActualDelayTime);
                napi\_set\_named\_property(env, napiWork, "actualDelayTime", napiActualDelayTime);
    
                napi\_set\_element(env, info, count, napiWork);
                count++;
            }
            napi\_set\_named\_property(env, result, "transientTasks", info);
        } else {
            napi\_create\_int32(env, 0, &napiRemainingQuota);
            napi\_set\_named\_property(env, result, "remainingQuota", napiRemainingQuota);
            napi\_value info {nullptr};
            napi\_create\_array(env, &info);
            napi\_set\_named\_property(env, result, "transientTasks", info);
        }
        return result;
    }
    
2.  注册函数
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"RequestSuspendDelay", nullptr, RequestSuspendDelay, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"GetRemainingDelayTime", nullptr, GetRemainingDelayTime, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"CancelSuspendDelay", nullptr, CancelSuspendDelay, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"GetTransientTaskInfo", nullptr, GetTransientTaskInfo, nullptr, nullptr, nullptr, napi\_default, nullptr },
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
3.  注册模块
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = ((void\*)0),
        .reserved = { 0 },
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
    {
        napi\_module\_register(&demoModule);
    }
    

#### \[h2\]在index.d.ts文件中声明函数

import backgroundTaskManager from '@kit.BackgroundTasksKit';

export const RequestSuspendDelay: () => number;
export const GetRemainingDelayTime: () => number;
export const CancelSuspendDelay: () => number;
export const GetTransientTaskInfo: () => backgroundTaskManager.TransientTaskInfo;

#### \[h2\]在index.ets文件中调用函数

import testTransientTask from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = '';
  // ...

  build() {
    Row() {
      Column() {
        // ...
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Button() {
          Text("RequestSuspendDelay").fontSize(20)
        }
        .id('request\_suspend\_delay')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.RequestSuspendDelay();
        })

        Button(){
          Text('GetRemainingDelayTime').fontSize(20)
        }
        .id('get\_remaining\_delay\_time')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.GetRemainingDelayTime();
        })

        Button(){
          Text('CancelSuspendDelay').fontSize(20)
        }
        .id('cancel\_suspend\_delay')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.CancelSuspendDelay();
        })

        Button(){
          Text('GetTransientTaskInfo').fontSize(20)
        }
        .id('get\_transient\_task\_info')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.GetTransientTaskInfo();
        })
      }
      .width('100%')
    }
    .height('100%')
  }

  RequestSuspendDelay() {
    let requestId = testTransientTask.RequestSuspendDelay();
    // ...
    console.info('The return requestId is ' + requestId);
  }

  GetRemainingDelayTime() {
    let time = testTransientTask.GetRemainingDelayTime();
    console.info('The time is ' + time);
  }

  CancelSuspendDelay() {
    let ret = testTransientTask.CancelSuspendDelay();
    console.info('The ret is ' + ret);
  }

  GetTransientTaskInfo() {
    let ret = testTransientTask.GetTransientTaskInfo();
    console.info('The ret is ' + JSON.stringify(ret));
  }
}

#### \[h2\]配置库依赖

配置CMakeLists.txt，本模块需要用到的共享库是libtransient\_task.so，在工程自动生成的CMakeLists.txt中的target\_link\_libraries中添加此共享库。

```txt
target_link_libraries(entry PUBLIC libace_napi.z.so libtransient_task.so)
```

#### 测试步骤

1.  连接设备并运行程序。
    
2.  点击 申请短时任务 按钮，控制台会打印日志，示例如下：
    
    ```txt
    The return requestId is 1
    ```
    
3.  点击 获取剩余时间 按钮，控制台会打印日志，示例如下：
    
    ```txt
    The return requestId is 18000
    ```
    
4.  点击 取消短时任务 按钮，控制台会打印日志，示例如下：
    
    ```txt
    The ret is 0
    ```
    
5.  点击 获取所有短时任务信息 按钮，控制台会打印日志，示例如下：
    
    ```txt
    The ret is {"remainingQuota":600000,"transientTasks":[]}
    ```
