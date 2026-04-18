---
title: "Native侧如何获取ArkTS侧Object对象及其成员变量"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-42"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何获取ArkTS侧Object对象及其成员变量"
captured_at: "2026-04-17T02:03:02.062Z"
---

# Native侧如何获取ArkTS侧Object对象及其成员变量

在ArkTS侧定义类，传递类到Native侧调用类函数。详情见示例代码。

ArkTS侧

// index.ets
import testNapi from 'libentry.so';
import { PromptAction } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class A {
  name: string = 'username'

  onCall() {
    try {
      new PromptAction().showToast({
        message: 'Message Info',
        duration: 2000
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`showToast undefined, code is ${err.code}, message is ${err.message}\`);
    }
  }
}

@Entry
@Component
struct NativeGetArkTSObject {
  build() {
    Button()
      .onClick(() => {
        testNapi.callFunction(new A());
      })
  }
}

// index.d.ts
export const callFunction: (a:object) => void;

Native侧

// Pass in an instance object and call functions in the object on the C++side 
#include "napi/native\_api.h" 
static napi\_value CallFunction(napi\_env env, napi\_callback\_info info) { 
    // Get instance object 
    size\_t argc = 1; 
    napi\_value args\[1\] = {nullptr}; 
    napi\_get\_cb\_info(env, info, &argc, args, NULL, NULL); 
    // Method for obtaining objects 
    napi\_value onCall; 
    napi\_get\_named\_property(env, args\[0\], "onCall", &onCall); 
    // Call functions in the object 
    napi\_value res; 
    napi\_call\_function(env, args\[0\], onCall, 0, nullptr, &res); 
    return onCall; 
} 
EXTERN\_C\_START 
static napi\_value Init(napi\_env env, napi\_value exports) { 
    napi\_property\_descriptor desc\[\] = { 
        {"callFunction", nullptr, CallFunction, nullptr, nullptr, nullptr, napi\_default, nullptr}}; 
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc); 
    return exports; 
} 
EXTERN\_C\_END
