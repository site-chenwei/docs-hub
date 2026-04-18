---
title: "如何在Native侧释放ArkTS对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-82"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧释放ArkTS对象"
captured_at: "2026-04-17T02:03:02.519Z"
---

# 如何在Native侧释放ArkTS对象

使用napi\_wrap接口时，如果最后一个参数result不为nullptr，需在适当时机调用napi\_remove\_wrap函数删除创建的napi\_ref对象。

// Usage 1: Napi\_wrap does not need to receive the created napi\_ref, and the last parameter is passed as nullptr. The created napi\_ref is a weak reference, managed by the system, and does not require manual release by the user
napi\_wrap(env, jsobject, nativeObject, cb, nullptr, nullptr);

// Usage 2: napi\_wrap needs to receive the created napi\_ref, the last parameter is not null ptr, and the returned napi\_ref is a strong reference that needs to be manually released by the user, otherwise it will cause memory leakage
napi\_ref result;
napi\_wrap(env, jsobject, nativeObject, cb, nullptr, &result);
// When jsobject and result are no longer used in the future, promptly call napi\_remove\_wrap to release result
void\*\* result1;
napi\_remove\_wrap(env, jsobject, result1);
