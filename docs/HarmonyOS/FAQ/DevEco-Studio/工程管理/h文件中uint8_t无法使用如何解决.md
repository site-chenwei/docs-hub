---
title: ".h文件中uint8_t无法使用如何解决"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-16"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "工程管理"
  - ".h文件中uint8_t无法使用如何解决"
captured_at: "2026-04-17T02:03:20.495Z"
---

# .h文件中uint8\_t无法使用如何解决

**解决措施**

1.  在CPP导入头文件修改如下：
    
    #ifdef \_\_cplusplus
    extern “C” {
    #endif
    #include “MGDolphinTOTP.h”
    #include “MGDolphinTOTPsha1.h”
    #ifdef \_\_cplusplus}
    #endif
    
2.  CMakeLists.txt 中需要增加 .c 文件进行编译 ：
    
    add\_library(entry SHARED hello.cpp NapiTest.cpp MGDolphinTOTP.c MGDolphinTOTPSha1.c)
