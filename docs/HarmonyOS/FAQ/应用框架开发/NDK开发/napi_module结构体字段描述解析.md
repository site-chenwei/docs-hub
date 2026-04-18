---
title: "napi_module结构体字段描述解析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-37"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "napi_module结构体字段描述解析"
captured_at: "2026-04-17T02:03:02.025Z"
---

# napi\_module结构体字段描述解析

关于napi\_module\_register(napi\_module\* mod)方法的入参napi\_module有两个关键属性：一个是.nm\_register\_func，定义模块初始化函数；另一个是.nm\_modname，定义模块的名称，也就是ArkTS侧引入的so库的名称，模块系统会根据此名称来区分不同的so。napi\_module字段的详细描述如下：

static napi\_module demoModule = {
    .nm\_version = 1,             // nm Version number, default value is 1
    .nm\_flags = 0,               // nm Identifier
    .nm\_filename = nullptr,      // File name, don't pay attention to it for now, just use the default value
    .nm\_register\_func = Init,    // Specify the entrance function for nm
    .nm\_modname = "entry",       // Specify the module name to import from the ArkTS page
    .nm\_priv = ((void\*)0),       // Don't follow for now, just use the default settings
    .reserved = { 0 },           // Don't pay attention for now, just use the default value
};
