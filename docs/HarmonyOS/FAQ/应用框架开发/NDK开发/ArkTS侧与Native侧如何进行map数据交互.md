---
title: "ArkTS侧与Native侧如何进行map数据交互"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-6"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "ArkTS侧与Native侧如何进行map数据交互"
captured_at: "2026-04-17T02:03:01.630Z"
---

# ArkTS侧与Native侧如何进行map数据交互

当前没有专门的接口用于在ArkTS侧与Native侧之间转换map。要实现map（二维数组）的数据交互，可以读取map中的数据并传递到Native侧进行重组。

参考代码如下：

在ArkTS中声明hashmap，获取数据并传递到Native侧。

let hashmap: HashMap<string, number> = new HashMap()
hashmap.set("Abc", 123)
hashmap.set("Bcd", 234)
hashmap.set("Cde", 345)
for (let key of hashmap.keys()) {
  testNapi.mapDemo(key, hashmap.get(key))
  console.info(\`key is ${key}, value is ${hashmap.get(key)}\`)
}

获取数据并重组为map。

#define LOG\_DOMAIN 0x3200 // Global domain macro, identifying the business domain
#define LOG\_TAG "MY\_TAG"  // Global tag macro, identifying module log tag 
#include "NativeMap.h"
#include "hilog/log.h"
#include <map>
#include <string>
std::map<std::string, int> testmap;
napi\_value NativeMap::MapDemo(napi\_env env, napi\_callback\_info info) {
    size\_t requireArgc = 2;
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    char str1\[1024\];
    size\_t str1\_len;
    napi\_get\_value\_string\_utf8(env, args\[0\], str1, 100, &str1\_len);
    int num;
    napi\_get\_value\_int32(env, args\[1\], &num);
    testmap.insert(std::make\_pair(str1, num));
    for(auto e: testmap){
        OH\_LOG\_ERROR(LOG\_APP, "key is: %{public}s, value is  %{public}d", (e.first).c\_str(), e.second);
    }
    
    return nullptr;
}
