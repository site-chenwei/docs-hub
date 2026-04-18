---
title: "ModuleManager模块加载流程是什么样的"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-109"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "ModuleManager模块加载流程是什么样的"
captured_at: "2026-04-17T02:03:00.621Z"
---

# ModuleManager模块加载流程是什么样的

napi\_module结构体包含模块注册所需的信息，具体定义如下：

static napi\_module demoModule = {
  .nm\_version = 1, // Nm version number, default value is 1, type is int
  .nm\_flags = 0, // Nm identifier, type unsigned int
  .nm\_filename = nullptr, // File name, not currently paid attention to, use default value, type is char\*
  .nm\_register\_func = Init, // Specify the entry function for nm, type napi\_addon\_register\_func
  .nm\_modname = "entry", // Specify the module name for TS page import, type char\*
  .nm\_priv = ((void\*)0),  // Not paying attention for now, just use the default, type is void\*
  .reserved = { 0 } // Not paying attention for now, just use the default value, type is void\*
};

在requireNapi中，loadNativeModule加载模块，会先通过FindNativeModuleByCache在缓存中寻找目标module，如果在缓存中找到，使用GetNativeModulePath拼接so路径，最后用LoadModuleLibrary打开so；如果没有在缓存中找到，则要先查找dlopen打开对应so，打开so后，native中的extern "C" \_\_attribute\_\_((constructor)) void RegisterModule(void)函数进行NativeModule加载，然后完成static napi\_value Init(napi\_env env, napi\_value export)中的实际注册动作，返回一个js对象export，该js对象上挂载了开发者提供的native方法，以便于开发者在js侧调用。模块加载流程简介如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/RP3PQIzeQu2ClHESYdFV0A/zh-cn_image_0000002229604001.png?HW-CC-KV=V1&HW-CC-Date=20260417T020302Z&HW-CC-Expire=86400&HW-CC-Sign=2BBE0A046A1BD5538D0D30DAA541C04BCA6640059A33B88EDBB209A968919C99 "点击放大")
