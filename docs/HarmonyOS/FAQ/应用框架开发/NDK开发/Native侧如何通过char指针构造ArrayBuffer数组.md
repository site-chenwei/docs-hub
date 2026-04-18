---
title: "Native侧如何通过char指针构造ArrayBuffer数组"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-59"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何通过char指针构造ArrayBuffer数组"
captured_at: "2026-04-17T02:03:02.265Z"
---

# Native侧如何通过char指针构造ArrayBuffer数组

可以通过napi\_create\_arraybuffer接口实现。

#include "CharToArrBuffer.h" 
napi\_value CharToArrBuffer::TestCharBuf(napi\_env env, napi\_callback\_info info) { 
    napi\_value result = nullptr; 
    char \*buf = nullptr; 
    // Create an Array buffer 
    napi\_create\_arraybuffer(env, 100, reinterpret\_cast<void \*\*>(&buf), &result); 
    // Assign an ArrayBuffer 
    for (int i = 0; i < 100; i++) { 
        buf\[i\] = i + 2; 
    } 
    return result; 
}
