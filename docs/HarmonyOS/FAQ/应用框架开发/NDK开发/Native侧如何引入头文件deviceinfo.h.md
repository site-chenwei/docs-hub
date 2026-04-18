---
title: "Native侧如何引入头文件deviceinfo.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-44"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何引入头文件deviceinfo.h"
captured_at: "2026-04-17T02:03:02.074Z"
---

# Native侧如何引入头文件deviceinfo.h

**问题现象：**

在C++文件中，参照官方指导文档，引入#include "deviceinfo.h"头文件后，编译时仍提示无法找到该头文件，日志提示未链接deviceinfo库。

**解决措施：**

当前public SDK中不包含deviceinfo.h头文件，该头文件仅在full SDK中才可以使用，并且需要在CMakeLists.txt导入libdeviceinfo\_ndk.z.so 库才能找到该头文件。方法如下：

\# CMakeLists.txt
# ...
target\_link\_libraries(cpplib PUBLIC libace\_napi.z.so libdeviceinfo\_ndk.z.so)
