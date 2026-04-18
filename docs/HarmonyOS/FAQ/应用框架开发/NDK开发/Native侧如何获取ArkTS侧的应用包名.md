---
title: "Native侧如何获取ArkTS侧的应用包名"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-17"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何获取ArkTS侧的应用包名"
captured_at: "2026-04-17T02:03:01.767Z"
---

# Native侧如何获取ArkTS侧的应用包名

**问题详情**

ArkTS侧调用Native开放的接口时，如何在Native侧获取TS侧应用包名？

**解决措施**

Native代码可以使用Native Bundle接口获取应用的包名和appId等信息。使用时，需在CMakeLists文件中添加libbundle\_ndk.z.so依赖。

具体代码如下：

#include "CGetAppPackageName.h" 
#include "napi/native\_api.h" 
#include <bundle/native\_interface\_bundle.h> 
#include <cstdlib> 
#include "hilog/log.h" 
#define LOG\_TAG "Pure" 
 
napi\_value CGetAppPackageName::GetCurrentApplicationPackageName(napi\_env env, napi\_callback\_info info) 
{ 
    // Call the Native interface to obtain application information 
    OH\_NativeBundle\_ApplicationInfo nativeApplicationInfo = OH\_NativeBundle\_GetCurrentApplicationInfo(); 
    // Convert the application package name obtained by the Native interface to the bundleName property in the JS object 
    napi\_value bundleName; 
    napi\_create\_string\_utf8(env, nativeApplicationInfo.bundleName, NAPI\_AUTO\_LENGTH, &bundleName); 
    OH\_LOG\_INFO(LOG\_APP, "napi get application package name： %{public}s", nativeApplicationInfo.bundleName); 
    // Finally, to prevent memory leaks, manually release
    free(nativeApplicationInfo.bundleName); 
    return nullptr; 
}

更多相关信息可参考链接：

[NativeBundle开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-bundle-guidelines)
