---
title: "Sendable对象冻结"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-freeze"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkTS（方舟编程语言）"
  - "ArkTS并发"
  - "并发线程间通信"
  - "线程间通信对象"
  - "Sendable对象"
  - "Sendable对象冻结"
captured_at: "2026-04-17T01:35:34.589Z"
---

# Sendable对象冻结

Sendable对象支持冻结操作。冻结后，对象变为只读，不能修改属性。因此，多个并发实例间访问时无需加锁。可以通过调用[Object.freeze](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)接口冻结对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/-1_9LqRWTIi6XoU825oC9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013535Z&HW-CC-Expire=86400&HW-CC-Sign=0A5DDE6DDC2DFD20B1790903FD55FFFE69E47D4CD9345D7CB0574BDC3F295B7D)

不支持在.ets文件中使用Object.freeze接口。

#### 使用示例

1.  提供ts文件封装Object.freeze方法。
    
    ```ts
    // helper.ts
    export function freezeObj(obj: any) {
      Object.freeze(obj);
    }
    ```
    
2.  调用freeze方法冻结对象，然后将其发送到子线程。
    
    ```ts
    // Index.ets
    import { freezeObj } from './helper';
    import { worker } from '@kit.ArkTS';
     
    @Sendable
    export class GlobalConfig {
      // 一些配置属性与方法
      init() {
        // 初始化相关逻辑
        freezeObj(this); // 初始化完成后冻结当前对象
      }
    }
     
    @Entry
    @Component
    struct Index {
      build() {
        Column() {
          Text("Sendable freezeObj Test")
            .id('HelloWorld')
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              let gConfig = new GlobalConfig();
              gConfig.init();
              const workerInstance = new worker.ThreadWorker('entry/ets/workers/Worker.ets', { name: "Worker1" });
              workerInstance.postMessage(gConfig);
            })
        }
        .height('100%')
        .width('100%')
      }
    }
    ```
    
3.  子线程直接操作对象，不加锁。
    
    ```ts
    // Worker.ets
    import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
    import { GlobalConfig } from '../pages/Index';
    
    const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
    workerPort.onmessage = (e: MessageEvents) => {
      let gConfig: GlobalConfig = e.data;
      // 使用gConfig对象
    }
    ```
