---
title: "如何在Native侧添加debug版本声明"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-12"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧添加debug版本声明"
captured_at: "2026-04-17T02:03:01.724Z"
---

# 如何在Native侧添加debug版本声明

**问题详情**

尝试过在需要编译的库的build-profile.json5文件中，buildOptionSet字段中添加 { "name": "debug", "externalNativeOptions": { "arguments": "-DDEBUG=1" } } 或在buildOption.externalNativeOptions.arguments字段中设置"-DDEBUG=1"， 在使用debug模式运行时均不会执行#ifdef DEBUG中的语句。

**解决措施**

1.CMakeLists.txt文件中增加如下语句：

if(CMAKE\_BUILD\_TYPE STREQUAL Debug)
    add\_definitions(-D\_DEBUG)
endif()

2.C++文件中增加如下代码：

#include "napi/native\_api.h" 
#include "hilog/log.h" 
#define LOG\_TAG "Pure" 
 
static napi\_value DefDebug(napi\_env env, napi\_callback\_info info) { 
#ifdef \_DEBUG 
    OH\_LOG\_INFO(LOG\_APP, "debug enter Project"); 
#else 
    OH\_LOG\_INFO(LOG\_APP, "release enter Project"); 
#endif 
    return nullptr; 
}
