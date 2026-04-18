---
title: "如何导出C++自定义类，导出后如何在ArkTS侧进行类方法调用"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-7"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何导出C++自定义类，导出后如何在ArkTS侧进行类方法调用"
captured_at: "2026-04-17T02:03:01.654Z"
---

# 如何导出C++自定义类，导出后如何在ArkTS侧进行类方法调用

可以通过 napi\_define\_class 建立 ArkTS 类与 C++ 侧的映射关系，并将对应的对象挂载到 export 上导出。在 index.d.ts 文件中定义 ArkTS 侧类接口，实现对类的调用。

参考代码如下：

C++侧定义类。

// MyDemo.h Define C++classes
class MyDemo { 
  public: 
    MyDemo(std::string m\_name); 
    MyDemo(); 
    ~MyDemo();   
    std::string name; 
    int add(int a, int b); 
    int sub(int a, int b); 
};

在hello.cpp中完成ArkTS类与C++的映射，并将其挂载到export上。

// ArkTS Object Constructor
static napi\_value JsConstructor(napi\_env env, napi\_callback\_info info) {
    // Create Napi object
    napi\_value jDemo = nullptr;
    size\_t argc = 0;
    napi\_value args\[1\] = {0};
    // Get constructor input parameters
    napi\_get\_cb\_info(env, info, &argc, args, &jDemo, nullptr);
    // Parameters passed in args \[0\] js
    char name\[50\];
    size\_t result = 0;
    napi\_get\_value\_string\_utf8(env, args\[0\], name, sizeof(name) + 1, &result);
    // Create C++objects
    MyDemo \*cDemo = new MyDemo(name);
    OH\_LOG\_INFO(LOG\_APP, "%{public}s", (cDemo->name).c\_str());
    // Set the JS object name attribute
    napi\_set\_named\_property(env, jDemo, "name", args\[0\]);
    // Binding JS objects with C++objects
    napi\_wrap(
        env, jDemo, cDemo,
        // Define callback function for recycling JS objects, used to destroy C++objects and prevent memory leaks
        \[\](napi\_env env, void \*finalize\_data, void \*finalize\_hint) {
            MyDemo \*cDemo = (MyDemo \*)finalize\_data;
            delete cDemo;
            cDemo = nullptr;
        },
        nullptr, nullptr);
    return jDemo;
}
// ArkTS object add function
static napi\_value JsAdd(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_value jDemo = nullptr;
    napi\_get\_cb\_info(env, info, &argc, args, &jDemo, nullptr);
    MyDemo \*cDemo = nullptr;
    // Convert ArkTS object to c object
    napi\_unwrap(env, jDemo, (void \*\*)&cDemo);
    // Get parameters passed by ArkTS
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    int cResult = cDemo->add(value0, value1);
    napi\_value jResult;
    napi\_create\_int32(env, cResult, &jResult);
    return jResult;
}
// ArkTS object sub function
static napi\_value JsSub(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_value jDemo = nullptr;
    napi\_get\_cb\_info(env, info, &argc, args, &jDemo, nullptr);
    MyDemo \*cDemo = nullptr;
    // Convert ArkTS object to c object
    napi\_unwrap(env, jDemo, (void \*\*)&cDemo);
    // Get parameters passed by ArkTS
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    int cResult = cDemo->sub(value0, value1);
    napi\_value jResult;
    napi\_create\_int32(env, cResult, &jResult);
    return jResult;
}
static napi\_value Add(napi\_env env, napi\_callback\_info info) {
    size\_t requireArgc = 2;
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_valuetype valuetype0;
    napi\_typeof(env, args\[0\], &valuetype0);
    napi\_valuetype valuetype1;
    napi\_typeof(env, args\[1\], &valuetype1);
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    MyDemo \*demo = new MyDemo();
    // Call functions in so to perform operations
    int result = demo->add(value0, value1);
    napi\_value sum;
    napi\_create\_int32(env, result, &sum);
    delete demo;
    return sum;
}
static napi\_value Sub(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_valuetype valuetype0;
    napi\_typeof(env, args\[0\], &valuetype0);
    napi\_valuetype valuetype1;
    napi\_typeof(env, args\[1\], &valuetype1);
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    MyDemo \*demo = new MyDemo();
    // Call functions in so to perform operations
    int result = demo->sub(value0, value1);
    napi\_value num;
    napi\_create\_int32(env, result, &num);
    delete demo;
    return num;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports) {
    // Define the methods that modules need to be exposed externally
    napi\_property\_descriptor desc\[\] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr},
                                       {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    // Establish the mapping relationship between ArkTS class and C++side through napi\_fine\_class, and then mount the corresponding object onto export
    napi\_property\_descriptor classProp\[\] = {{"add", nullptr, JsAdd, nullptr, nullptr, nullptr, napi\_default, nullptr},
                                            {"sub", nullptr, JsSub, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_value jDemo = nullptr;
    const char \*jDemoName = "MyDemo";
    // Establish an association between ArkTS constructor and C++methods, specifying 2 props
    napi\_define\_class(env, jDemoName, sizeof(jDemoName), JsConstructor, nullptr,
                      sizeof(classProp) / sizeof(classProp\[0\]), classProp, &jDemo);
    napi\_set\_named\_property(env, exports, jDemoName, jDemo);
    return exports;
}
EXTERN\_C\_END

在index.d.ts文件中定义ArkTS类。

declare namespace testNapi {
  const add: (a: number, b: number) => number;
  const sub: (a: number, b: number) => number;
  // Defining the ArkTS Interface
  class MyDemo {
    constructor(name:string)
    name: string
    add(a: number, b: number): number
    sub(a: number, b: number): number
  }
}
export default testNapi;

在ArkTS侧实现调用。

import testNapi from 'libentry.so';
// ...
  // ...
  new testNapi.MyDemo('abc');
  hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
  hilog.info(0x0000, 'testTag', 'Test NAPI 2 - 3 = %{public}d', testNapi.sub(2, 3));
  // ...
