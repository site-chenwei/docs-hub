---
title: "如何利用worker子线程调用napi实现loop改写变量"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-76"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "任务并发调度（Function Flow Runtime）"
  - "如何利用worker子线程调用napi实现loop改写变量"
captured_at: "2026-04-17T02:03:02.635Z"
---

# 如何利用worker子线程调用napi实现loop改写变量

**问题现象**

在特定场景中，需要用 napi 的 loop 完成消息循环，同时避免阻塞 UI 主线程。

**解决措施**

请参考以下代码实现。

ArkTS侧：

创建worker并监听：

import { MessageEvents, worker } from '@kit.ArkTS';
import { Prompt } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State progress: number = 0;
  @State message: string = '0'
  state: number = 0

  build() {
    Column() {
      Row() {
        Button("start")
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            if (this.state == 1) {
              this.getUIContext().getPromptAction().showToast({ message: "Please do not click again" })
              return
            }
            this.state = 1
            let worker1: worker.ThreadWorker =
              new worker.ThreadWorker('entry/ets/workers/Worker.ets', { name: "worker1" });
            worker1.postMessage('this is a msg to start worker1');
            worker1.onmessage = (e: MessageEvents) => {
              this.progress = e.data.data as number
              this.message = String(this.progress)
              console.log('=====js main, process is:' + this.message)

              if (this.progress == 100) {
                worker1.terminate()
                this.state = 0
              }
            }
          });
      }
      .margin({
        top: 10,
        bottom: 10,
        left: 5,
        right: 5
      })

      Row() {
        Text(this.message)
          .fontSize(50)
      }
      .margin({
        top: 10,
        bottom: 5,
        left: 5,
        right: 5
      })
    }
  }
}

在worker中调用napi函数：

import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import testNapi from 'libentry.so';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  testNapi.mainThread((data: ESObject) => {
    console.log("==worker func:data is :" + data);
    workerPort.postMessage({ 'type': 1, "data": data });
  });
}

Native侧：

在Native侧利用loop完成消息循环：

struct CallbackContext {
    napi\_env env = nullptr;
    napi\_ref callbackRef = nullptr;
    int retData = 0;
};

#include "WorkerCallNapiLoop.h" 
#include <thread> 
#include <uv.h> 
 
void WorkerCallNapiLoop::SubThread(CallbackContext \*context) { 
    uv\_loop\_s \*loop = nullptr; 
    napi\_get\_uv\_event\_loop(context->env, &loop); 
    // uv\_work\_t is the structure that associates loop and thread pool callback functions
    uv\_work\_t \*work = new uv\_work\_t; 
    work->data = (CallbackContext \*)context; 
    uv\_queue\_work( 
        loop, work, \[\](uv\_work\_t \*work) {}, 
        \[\](uv\_work\_t \*work, int status) { 
            CallbackContext \*context = (CallbackContext \*)work->data; 
            napi\_handle\_scope scope = nullptr; 
            // Manage the lifecycle of napi\_value to prevent memory leaks
            napi\_open\_handle\_scope(context->env, &scope); 
            if (scope == nullptr) { 
                return; 
            } 
            napi\_value callback = nullptr; 
            napi\_get\_reference\_value(context->env, context->callbackRef, &callback); 
            while (context->retData < 100) { 
                context->retData += 1; 
                napi\_value retArg; 
                napi\_create\_int32(context->env, context->retData, &retArg); 
                napi\_value ret; 
                napi\_call\_function(context->env, nullptr, callback, 1, &retArg, &ret); 
                std::this\_thread::sleep\_for(std::chrono::milliseconds(100)); 
            } 
            napi\_close\_handle\_scope(context->env, scope); 
            if (context->retData > 99) { 
                napi\_delete\_reference(context->env, context->callbackRef); 
                if (work != nullptr) { 
                    delete work; 
                } 
            } 
        }); 
}; 
napi\_value WorkerCallNapiLoop::MainThread(napi\_env env, napi\_callback\_info info) { 
        size\_t argc = 1; 
    napi\_value args\[1\] = {0}; 
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
    auto asyncContext = new CallbackContext(); 
    asyncContext->env = env; 
    napi\_create\_reference(env, args\[0\], 1, &asyncContext->callbackRef); 
    auto func = \[\](void \*asyncContext) { 
        delete asyncContext; 
    }; 
    napi\_add\_env\_cleanup\_hook(asyncContext->env, func, asyncContext); 
    uv\_loop\_s \*loop = nullptr; 
    napi\_get\_uv\_event\_loop(env, &loop); 
    // Start sub thread 
    std::thread testThread(SubThread, asyncContext); 
    testThread.detach(); 
    return nullptr; 
}
