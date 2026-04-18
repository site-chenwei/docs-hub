---
title: "Native侧获取env具有线程限制，如何在C++子线程触发ArkTS侧回调"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-25"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "任务并发调度（Function Flow Runtime）"
  - "Native侧获取env具有线程限制，如何在C++子线程触发ArkTS侧回调"
captured_at: "2026-04-17T02:03:02.567Z"
---

# Native侧获取env具有线程限制，如何在C++子线程触发ArkTS侧回调

可以通过线程安全函数实现在C++子线程触发ArkTS侧回调。native主线程外的其他线程通常不能直接使用需要napi\_env、napi\_value的NAPI函数，线程安全函数可以在其他线程中被调用，并回到主线程中执行。参考代码如下：

在Native入口定义线程安全函数，计算两数之和。

napi\_threadsafe\_function tsfn;
using namespace std;
struct CallbackData {
    napi\_threadsafe\_function tsfn;
    napi\_async\_work work;
    double result = 0;
    double data\[2\] = {0};
};

static void CallJsFunction(napi\_env env, napi\_value callBack, \[\[maybe\_unused\]\] void \*context, void \*data) {
    CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data);

    napi\_value callBackArgs = nullptr;
    napi\_create\_double(env, callbackData->result, &callBackArgs);
    napi\_value callBackResult = nullptr;
    napi\_call\_function(env, nullptr, callBack, 1, &callBackArgs,
                       &callBackResult); // Call the callback to send the result to the ArkTS side.
}

static void Thread\_Finalize\_CBFunction(napi\_env env, void \*finalize\_data, void \*finalize\_hint) {
    CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(finalize\_data);
    delete finalize\_data;
}

static void AddFunc(void \*data) {
    CallbackData \*callbackData = static\_cast<CallbackData \*>(data); // Parse the context, and process the service (add the two numbers).
    callbackData->result = callbackData->data\[0\] + callbackData->data\[1\]; // Place the result.
    napi\_call\_threadsafe\_function(callbackData->tsfn, data, napi\_tsfn\_blocking); // Call the thread-safe function.
    napi\_release\_threadsafe\_function(callbackData->tsfn, napi\_tsfn\_release);
}

static napi\_value AddTSFCallback(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 3;
    napi\_value args\[3\] = {nullptr};

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    CallbackData \*callbackData = new CallbackData();
    napi\_get\_value\_double(env, args\[0\], &callbackData->data\[0\]);
    napi\_get\_value\_double(env, args\[1\], &callbackData->data\[1\]);

    napi\_value resourceName = nullptr;
    napi\_create\_string\_utf8(env, "Thread\_safe Function", NAPI\_AUTO\_LENGTH, &resourceName);

    // Create a thread-safe function object, and register and bind callback and call\_js\_cb.
    napi\_create\_threadsafe\_function(env, args\[2\], nullptr, resourceName, 0, 1, callbackData, Thread\_Finalize\_CBFunction, callbackData,
                                    CallJsFunction, &callbackData->tsfn);
    thread t(AddFunc, reinterpret\_cast<void \*>(callbackData)); // Create a C++ subthread to process service logic.
    t.detach();
    return nullptr;
}

ArkTS侧调用接口。

import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  result: number = 0;
  // ...
    .onClick(() => {
      testNapi.addTSFCallback(2, 3, (nativeResult: number) => {
        this.result = nativeResult;
      });
    })

**参考链接**

[使用Node-API接口进行线程安全开发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-thread-safety)
