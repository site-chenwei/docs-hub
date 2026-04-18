---
title: "静态共享包HAR如何引用另一个HAR包中的so文件"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-56"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "静态共享包HAR如何引用另一个HAR包中的so文件"
captured_at: "2026-04-17T02:03:21.737Z"
---

# 静态共享包HAR如何引用另一个HAR包中的so文件

可以将so库导出并放置在libs目录下，然后在CMakeLists.txt中添加以下代码，将libnativeSub.so添加到har包中。

target\_link\_directories(entry PUBLIC ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../libs/${OHOS\_ARCH}/)
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libc++.a libnativeSub.so)
