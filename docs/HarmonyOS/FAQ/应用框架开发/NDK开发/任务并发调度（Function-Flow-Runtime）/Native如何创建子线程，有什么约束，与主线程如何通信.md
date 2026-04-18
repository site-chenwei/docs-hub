---
title: "Native如何创建子线程，有什么约束，与主线程如何通信"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-68"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "任务并发调度（Function Flow Runtime）"
  - "Native如何创建子线程，有什么约束，与主线程如何通信"
captured_at: "2026-04-17T02:03:02.632Z"
---

# Native如何创建子线程，有什么约束，与主线程如何通信

请参照下面的代码，通过C++子线程调用arkts侧的函数：

#include "napi/native\_api.h" 
#include "hilog/log.h" 
#include "thread" 
 
napi\_ref cbObj = nullptr; 
napi\_threadsafe\_function tsfn; 
#define NUMBER 666 
static void CallJs(napi\_env env, napi\_value js\_cb, void \*context, void \*data) { 
    napi\_get\_reference\_value(env, cbObj, &js\_cb); 
    napi\_value argv; 
    napi\_create\_int32(env, NUMBER, &argv); 
    napi\_value result = nullptr; 
    napi\_call\_function(env, nullptr, js\_cb, 1, &argv, &result); 
} 
static napi\_value ThreadsTest(napi\_env env, napi\_callback\_info info) { 
    size\_t argc = 1; 
    napi\_value js\_cb, work\_name; 
    napi\_status status; 
    status = napi\_get\_cb\_info(env, info, &argc, &js\_cb, nullptr, nullptr); 
    OH\_LOG\_INFO(LOG\_APP, "ThreadSafeTest 0: %{public}d", status == napi\_ok); 
    // Set initial\_refcount to 0 for a weak reference, >0 for a strong reference. 
    status = napi\_create\_reference(env, js\_cb, 1, &cbObj); 
    OH\_LOG\_INFO(LOG\_APP, "napi\_create\_reference of js\_cb to cbObj: %{public}d", status == napi\_ok); 
    status = napi\_create\_string\_utf8(env, "Work Item", NAPI\_AUTO\_LENGTH, &work\_name); 
    status = napi\_create\_threadsafe\_function(env, js\_cb, NULL, work\_name, 0, 1, NULL, NULL, NULL, CallJs, &tsfn); 
    OH\_LOG\_INFO(LOG\_APP, "napi\_create\_threadsafe\_function : %{public}d", status == napi\_ok); 
    std::thread t(\[\]() { 
        std::thread::id this\_id = std::this\_thread::get\_id(); 
        OH\_LOG\_INFO(LOG\_APP, "thread0 %{public}d.\\n", this\_id); 
        napi\_status status; 
        status = napi\_acquire\_threadsafe\_function(tsfn); 
        OH\_LOG\_INFO(LOG\_APP, "thread : %{public}d", status == napi\_ok); 
        napi\_call\_threadsafe\_function(tsfn, NULL, napi\_tsfn\_blocking); 
    }); 
    t.detach(); 
    return NULL; 
}
