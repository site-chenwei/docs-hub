---
title: "napi_call_function调用时除了会有pending exception外，是否还有其他异常场景"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-69"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "napi_call_function调用时除了会有pending exception外，是否还有其他异常场景"
captured_at: "2026-04-17T02:03:02.369Z"
---

# napi\_call\_function调用时除了会有pending exception外，是否还有其他异常场景

调用NAPI接口时可能会产生异常，因此在业务的关键流程中需要对接口调用的结果进行判断，以检查是否出现异常。例如：

napi\_status status = napi\_create\_object(env, &object); 
if (status != napi\_ok) { 
    napi\_throw\_error(env, nullptr, "Error"); 
return; 
}
