---
title: "如何在Native侧构建一个ArkTS对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-45"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧构建一个ArkTS对象"
captured_at: "2026-04-17T02:03:02.084Z"
---

# 如何在Native侧构建一个ArkTS对象

1.  调用接口napi\_create\_object创建对象。
    
    // Create object arg\_order in the native layer
    napi\_value arg\_object;
    napi\_create\_object(env, &arg\_object);
    
2.  调用接口napi\_set\_named\_property给对象属性赋值。
    
    napi\_value testNum, testString;
    // Set the property testNum and assign a value of 123 to the arg\_order object created above
    napi\_create\_int32(env, 123, &testNum);
    napi\_set\_named\_property(env, arg\_object, "testNum", testNum);
    // Set the property testString and assign 'Pure' to the arg\_order object created above
    napi\_create\_string\_utf8(env, "Pure", NAPI\_AUTO\_LENGTH, &testString);
    napi\_set\_named\_property(env, arg\_object, "testString", testString);
