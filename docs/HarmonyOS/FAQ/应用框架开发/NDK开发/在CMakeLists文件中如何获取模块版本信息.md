---
title: "在CMakeLists文件中如何获取模块版本信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-60"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "在CMakeLists文件中如何获取模块版本信息"
captured_at: "2026-04-17T02:03:02.268Z"
---

# 在CMakeLists文件中如何获取模块版本信息

**问题现象**

有一个har模块，在 oh-package.json5 中配置了版本 1.0.0。模块内部有C++代码，其中某一个文件会根据版本变化，因此不同版本参与编译的都是不同的文件。通过CMAKE\_VERSION变量可以获取CMake的版本信息，但获取不到har的版本信息，如何在CMakeLists中获取当前har模块oh-package.json5中的version版本号，以匹配不同的cpp文件。

**解决措施**

可以尝试通过转JSON字符串与版本号比较的方式解决。

cmake\_minimum\_required(VERSION 3.4.1)
project(CmakeModuleInfo)

set(JSON\_FILE\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../oh-package.json5)
file(READ ${JSON\_FILE\_PATH} JSON\_STRING)
message("json string:${JSON\_STRING}")
if("${JSON\_STRING}" MATCHES "1.0.0")
set(SRC\_LIST napi\_init.cpp)
else()
set(SRC\_LIST hello.cpp)
endif()
message("src\_file:${SRC\_LIST}")

set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
include\_directories(${NATIVERENDER\_ROOT\_PATH}
                    ${NATIVERENDER\_ROOT\_PATH}/include)

add\_library(entry SHARED ${SRC\_LIST})
target\_link\_libraries(entry PUBLIC libace\_napi.z.so)
