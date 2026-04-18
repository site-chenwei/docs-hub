---
title: "使用Node"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-49"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "使用Node-API实现ArkTS与C/C++语言交互"
captured_at: "2026-04-17T02:03:02.165Z"
---

# 使用Node-API实现ArkTS与C/C++语言交互

在ArkTS侧不能向C++层注册对象或函数，开发者需要在C++层自行处理。Env可以长期持有，但在使用Env时，必须在创建该Env的ArkTS线程中进行。

**参考链接**

[Native与ArkTS对象绑定](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process)
