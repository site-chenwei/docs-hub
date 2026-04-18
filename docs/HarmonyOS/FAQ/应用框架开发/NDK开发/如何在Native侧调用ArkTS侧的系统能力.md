---
title: "如何在Native侧调用ArkTS侧的系统能力"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-18"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧调用ArkTS侧的系统能力"
captured_at: "2026-04-17T02:03:01.774Z"
---

# 如何在Native侧调用ArkTS侧的系统能力

**问题详情**

系统提供了 ArkTS 接口，但未提供对应的 NAPI 接口。使用 C++ 代码实现业务逻辑时，部分系统能力需要依赖 ArkTS 接口。

**解决措施**

1.  通过napi\_load\_module接口加载模块。
2.  通过napi\_get\_named\_property接口获取模块属性。
3.  通过napi\_call\_function接口调用方法。

具体方法请参考以下示例代码，用于获取设备的屏幕宽高。

#include "CallSystemModule.h" 
#include "napi/native\_api.h" 
#include <hilog/log.h> 
#define LOG\_TAG "Pure" 
 
napi\_value CallSystemModule::GetDisplaySize(napi\_env env, napi\_callback\_info info) { 
    // Obtain the system library path on the arkts side
    char path\[64\] = "@ohos.display"; 
    size\_t typeLen = 0; 
    napi\_value string; 
    napi\_create\_string\_utf8(env, path, typeLen, &string); 
    // Loading system libraries 
    napi\_value sysModule; 
    napi\_load\_module(env, path, &sysModule); 
    // Retrieve the 'getDefault Display Sync' method from the system library 
    napi\_value func = nullptr; 
    napi\_get\_named\_property(env, sysModule, "getDefaultDisplaySync", &func); 
    napi\_value funcResult; 
    napi\_call\_function(env, sysModule, func, 0, nullptr, &funcResult); 
    napi\_value widthValue = nullptr; 
    napi\_get\_named\_property(env, funcResult, "width", &widthValue); 
    double width; 
    napi\_get\_value\_double(env, widthValue, &width); 
    OH\_LOG\_INFO(LOG\_APP, "width: %{public}f", width); 
    napi\_value heightValue = nullptr; 
    napi\_get\_named\_property(env, funcResult, "height", &heightValue); 
    double height; 
    napi\_get\_value\_double(env, heightValue, &height); 
    OH\_LOG\_INFO(LOG\_APP, "height: %{public}f", height); 
    // By obtaining the width and height of the business, specific business logic can be further processed
    return nullptr; 
}
