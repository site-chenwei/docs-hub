---
title: "如何对多个C++源文件中接口进行导出声明"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-3"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何对多个C++源文件中接口进行导出声明"
captured_at: "2026-04-17T02:03:01.552Z"
---

# 如何对多个C++源文件中接口进行导出声明

**问题现象**

DevEco Studio创建的默认C++工程中是只有一个hello.cpp，想在C++侧加一个 a.cpp文件，并且希望可以从a.cpp文件中导出一个函数给ArkTS侧调用，具体如何实现？

**解决措施**

首先需要引入对应的a.cpp对应的头文件a.h，然后在初始化函数Init中进行接口映射，最后通过index.d.ts文件将接口导出。参考代码如下：

在NumberType.cpp文件中实现Add函数业务功能。

#include "NumberType.h" // Import header file
// NumberType is the class name, and Add is its function 
napi\_value NumberType::Add(napi\_env env, napi\_callback\_info info) {
    // ... Business Function Implementation Code
    // ...
}

在hello.cpp文件中引入头文件并初始化函数Init中进行接口映射。

#include "NumberType.h"
#include "napi/native\_api.h"

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    /\* Associate the externally provided interface with the written method, for example, associate add with the Add 
     \* method. 
    \*/ 
    napi\_property\_descriptor desc\[\] = {
        { "add", nullptr, NumberType::Add, nullptr, nullptr, nullptr, napi\_default, nullptr }
    };
    // napi\_define\_properties construct a return value that contains a list of methods that correspond. 
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

在接口声明文件（index.d.ts）中对要传递给ArkTS侧的函数进行导出。

export const add: (a: number, b: number) => number;

**参考链接**

[基于XComponent组件实现图像绘制功能](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-XComponent)
