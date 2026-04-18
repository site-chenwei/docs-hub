---
title: "如何在Native侧直接使用其他模块的ArkTS方法"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-20"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧直接使用其他模块的ArkTS方法"
captured_at: "2026-04-17T02:03:01.837Z"
---

# 如何在Native侧直接使用其他模块的ArkTS方法

**问题详情**

在ArkTS侧已经定义了接口，但未实现对应的NDK接口。当使用C++代码实现业务逻辑时，可以直接使用已有的ArkTS接口。

**解决措施**

可通过napi\_load\_module接口实现对ArkTS文件中的接口的调用。具体步骤如下：

1.  通过napi\_load\_module接口加载模块。
2.  通过napi\_get\_named\_property接口获取模块属性。
3.  通过napi\_call\_function接口调用方法。
    
    具体方法请参考以下示例代码，展示如何加载ArkTS文件中的模块。
    

声明ArkTS侧方法：

// src/main/ets/pages/Test.ets
let value = 123;
function test() {
  console.log('Hello HarmonyOS');
}
export {value, test};

在模块级build-profile.json5文件中进行以下配置：

注意是在模块级的build-profile.json5文件中配置，而非工程级。同时需要确保"sources"配置项为正确的Test.ets文件路径。

"buildOption": {
  "externalNativeOptions": {
    "path": "./src/main/cpp/CMakeLists.txt",
    "arguments": "",
    "cppFlags": "",
  },
  "arkOptions": {
    "runtimeOnly": {
      "sources": \[
        "./src/main/ets/pages/Test.ets"
      \]
    }
  },
},

使用napi\_load\_module加载Test文件，调用函数test，并获取变量value。

#include "napi/native\_api.h" 
#include <string> 
 
static napi\_value LoadModule(napi\_env env, napi\_callback\_info info) { 
    napi\_value result; 
    // 1. Load modules from the Test file using napi\_load\_module 
    napi\_status status = napi\_load\_module(env, "ets/pages/Test", &result); 
    napi\_value testFn; 
    // 2. Use napi\_get\_named\_property to obtain the test function 
    napi\_get\_named\_property(env, result, "test", &testFn); 
    // 3. Call the function test using napi\_call\_function 
    napi\_call\_function(env, result, testFn, 0, nullptr, nullptr); 
    napi\_value value; 
    napi\_value key; 
    std::string keyStr = "value"; 
    napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key); 
    // 4. Get variable value using napi\_get\_property 
    napi\_get\_property(env, result, key, &value); 
    return value; 
}
