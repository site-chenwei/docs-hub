---
title: "Native侧如何访问ArkTS侧系统定义的异步方法"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-19"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何访问ArkTS侧系统定义的异步方法"
captured_at: "2026-04-17T02:03:01.779Z"
---

# Native侧如何访问ArkTS侧系统定义的异步方法

**问题详情**

系统仅提供ArkTS异步接口，未提供NDK接口。当使用C++代码实现业务逻辑时，部分系统能力需要依赖ArkTS异步接口。

**解决措施**

创建线程安全的函数来调用系统的异步接口。

1.  通过napi\_get\_cb\_info接口获取应用参数。
2.  通过napi\_create\_threadsafe\_function接口创建线程安全函数。
3.  通过napi\_create\_async\_work接口创建异步任务。
4.  通过napi\_load\_module接口加载模块。
5.  通过napi\_get\_named\_property接口获取模块属性。
6.  通过napi\_call\_function接口调用方法。

具体方法请参考以下示例代码，用于获取设备屏幕宽度。

Native侧代码实现：

#include "napi/native\_api.h" 
#include <future> 
#include <hilog/log.h> 
 
#define LOG\_TAG "Pure" // Global tag macro, identifying module log tags
 
// Context data, used for transferring data between threads
struct CallbackData { 
    napi\_threadsafe\_function tsfn; 
    napi\_async\_work work; 
    napi\_deferred deferred = nullptr; 
    double res; 
}; 
static napi\_value ResolvedCallback(napi\_env env, napi\_callback\_info info) { 
    void \*data = nullptr; 
    size\_t argc = 1; 
    napi\_value argv\[1\]; 
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, &data); 
    napi\_value widthProp = nullptr; 
    napi\_get\_named\_property(env, argv\[0\], "width", &widthProp); 
    double result = 0; 
    napi\_get\_value\_double(env, widthProp, &result); 
    OH\_LOG\_INFO(LOG\_APP, "width in ResolvedCallback is %{public}f", result); 
    // Data is reinterpreted as a pointer to std:: promise<double>and the value of the promise is set to width 
    reinterpret\_cast<std::promise<double> \*>(data)->set\_value(result); 
    return nullptr; 
} 
static void CallJs(napi\_env env, napi\_value jsCb, void \*context, void \*data) { 
    // Import system library modules and call down to methods layer by layer
    napi\_value systemModule; 
    napi\_load\_module(env, "@ohos.display", &systemModule); 
    napi\_value displayFunc = nullptr; 
    napi\_get\_named\_property(env, systemModule, "getDefaultDisplay", &displayFunc); 
    napi\_value promise = nullptr; 
    napi\_call\_function(env, systemModule, displayFunc, 0, nullptr, &promise); 
    napi\_value thenFunc = nullptr; 
    napi\_get\_named\_property(env, promise, "then", &thenFunc); 
    napi\_value resolvedCallback; 
    // Promise resolve callback
    napi\_create\_function(env, "resolvedCallback", NAPI\_AUTO\_LENGTH, ResolvedCallback, data, &resolvedCallback); 
    napi\_value argv\[\] = {resolvedCallback}; 
    napi\_call\_function(env, promise, thenFunc, 1, argv, nullptr); 
} 
static void ExecuteWork(napi\_env env, void \*data) { 
    CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data); 
    std::promise<double> promise; 
    auto future = promise.get\_future(); 
    napi\_call\_threadsafe\_function(callbackData->tsfn, &promise, napi\_tsfn\_nonblocking); 
    try { 
        auto result = future.get(); 
        callbackData->res = result; 
        OH\_LOG\_INFO(LOG\_APP, "width in ExecuteWork %{public}f", result); 
    } catch (const std::exception &e) { 
        OH\_LOG\_INFO(LOG\_APP, "XXX, Result from JS %{public}s", e.what()); 
    } 
} 
static void WorkComplete(napi\_env env, napi\_status status, void \*data) { 
    CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data); 
    // Return the calculation results of the business code to the application 
    napi\_value result = nullptr; 
    napi\_create\_double(env, callbackData->res, &result); 
    napi\_resolve\_deferred(env, callbackData->deferred, result); 
    // Release thread safety methods 
    napi\_release\_threadsafe\_function(callbackData->tsfn, napi\_tsfn\_release); 
    // Delete asynchronous work items 
    napi\_delete\_async\_work(env, callbackData->work); 
    callbackData->tsfn = nullptr; 
    callbackData->work = nullptr; 
} 
static napi\_value getDisplayWidthAsync(napi\_env env, napi\_callback\_info info) { 
    size\_t argc = 1; 
    napi\_value jsCb = nullptr; 
    CallbackData \*callbackData = nullptr; 
    napi\_get\_cb\_info(env, info, &argc, &jsCb, nullptr, reinterpret\_cast<void \*\*>(&callbackData)); 
     
    napi\_value sysModule; 
    napi\_load\_module(env, "@ohos.display", &sysModule); 
    napi\_value getDefaultDisplay; 
    napi\_get\_named\_property(env, sysModule, "getDefaultDisplay", &getDefaultDisplay); 
    // Create a thread safe function 
    napi\_value resourceName = nullptr; 
    napi\_create\_string\_utf8(env, "getDisplayWidthAsync", NAPI\_AUTO\_LENGTH, &resourceName); 
    napi\_create\_threadsafe\_function(env, getDefaultDisplay, nullptr, resourceName, 0, 1, callbackData, nullptr, 
                                    callbackData, CallJs, &callbackData->tsfn); 
    // Create an asynchronous task 
    napi\_create\_async\_work(env, nullptr, resourceName, ExecuteWork, WorkComplete, callbackData, &callbackData->work); 
    // Add asynchronous tasks to the asynchronous queue and have them executed by the underlying scheduling system 
    napi\_queue\_async\_work(env, callbackData->work); 
    // Method returns promise 
    napi\_value result = nullptr; 
    napi\_create\_promise(env, &callbackData->deferred, &result); 
    return result; 
}

Index.d.ts文件声明接口：

export const getDisplayWidthAsync: () => Promise<number>;

ArkTS侧代码实现：

import testNapi from 'libcallsystemasyncwork.so';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('c++ asynchronous call to ts')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            testNapi.getDisplayWidthAsync().then((res: number) =>{
              console.info(\`display width = ${res.toString()}\`);
              this.getUIContext().getPromptAction().showToast({
                message: "screen width：" + res.toString()
              })
            });
          })
          .margin('30')
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)
    }
    .height('100%')
  }
}
