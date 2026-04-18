---
title: "ArkTS侧如何接收Native侧的键值对进行修改并返回到Native侧"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-41"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "ArkTS侧如何接收Native侧的键值对进行修改并返回到Native侧"
captured_at: "2026-04-17T02:03:02.073Z"
---

# ArkTS侧如何接收Native侧的键值对进行修改并返回到Native侧

1.  使用具体类型如 Record<string, number> 或 Map<string, number> 接收并修改数据。
2.  在ArkTS侧的函数中返回修改后的数据，在Native层通过napi\_call\_function可以获取到修改的数据。
3.  在Native侧，目前只能使用napi\_set\_property对对象的属性进行设置。

示例代码如下：

ArkTS侧

import testNapi from 'libentry.so';
// ...
  build() {
    // ...
          .onClick(() => {
            let data: Record<string, number> = testNapi.callbackToArkTS((value: object) => {
              let obj: Record<string, number> = value as Record<string, number>;
              console.info("pre type:" + obj\["type"\].toString())
              console.info(JSON.stringify(value))
              obj\["type"\] += 10;
              return value;
            });
            console.info(JSON.stringify(data))
          })
      }

Native侧

#include "napi/native\_api.h" 
#include "hilog/log.h" 
#undef LOG\_DOMAIN 
#undef LOG\_TAG 
#define LOG\_DOMAIN 0x3200 
#define LOG\_TAG "MY\_TAG" 
 
static bool Napi\_AddPropertyInt32(napi\_env env, napi\_value obj, const char \*key, int32\_t value) { 
    napi\_value key\_napi = nullptr; 
    napi\_status status = napi\_create\_string\_utf8(env, key, NAPI\_AUTO\_LENGTH, &key\_napi); 
    napi\_value value\_napi = nullptr; 
    status = napi\_create\_int32(env, value, &value\_napi); 
    status = napi\_set\_property(env, obj, key\_napi, value\_napi); 
    return true; 
} 
static  napi\_value CallbackToArkTS(napi\_env env, napi\_callback\_info info) { 
    size\_t argc = 1; 
    napi\_value args\[1\] = {nullptr}; 
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
    // Native callback to ArkTS layer object
    napi\_value argv = nullptr; 
    napi\_create\_object(env, &argv); 
    Napi\_AddPropertyInt32(env, argv, "type", 1); 
    Napi\_AddPropertyInt32(env, argv, "index", 2); 
    // Native callback to ArkTS layer
    napi\_value result = nullptr; 
    napi\_call\_function(env, NULL, args\[0\], 1, &argv, &result); 
    // Obtain the modified object of ArkTS
    napi\_value typeNumber = nullptr; 
    napi\_get\_named\_property(env, result, "type", &typeNumber); 
    int32\_t number; 
    napi\_get\_value\_int32(env, typeNumber, &number); 
    OH\_LOG\_INFO(LOG\_APP, "ArkTS modified type：%{public}d", number); 
    // Return the modified object
    return result; 
} 
EXTERN\_C\_START 
static napi\_value Init(napi\_env env, napi\_value exports) 
{ 
    napi\_property\_descriptor desc\[\] = { 
        { "callbackToArkTS", nullptr, CallbackToArkTS, nullptr, nullptr, nullptr, napi\_default, nullptr } 
    }; 
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc); 
    return exports; 
} 
EXTERN\_C\_END 

index.d.ts

export const callbackToArkTS: (a: object) => Record<string, number>
