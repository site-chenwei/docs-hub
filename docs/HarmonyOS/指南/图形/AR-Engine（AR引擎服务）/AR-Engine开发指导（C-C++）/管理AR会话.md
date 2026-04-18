---
title: "管理AR会话"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession"
menu_path:
  - "指南"
  - "图形"
  - "AR Engine（AR引擎服务）"
  - "AR Engine开发指导（C/C++）"
  - "管理AR会话"
captured_at: "2026-04-17T01:36:08.119Z"
---

# 管理AR会话

#### 概要

对于任何AR应用，都需要创建一个AR会话[AREngine\_ARSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arsession)，用于管理AR Engine的系统状态。

从6.1.0(23)开始，使用任何AR特性都需要通过[HMS\_AREngine\_CheckSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_checksupported)接口来查询当前设备是否支持该特性。

#### 使用特性检查接口

1.  引入头文件。
    
    ```cpp
    #include "ar/ar_engine_core.h"
    ```
    
2.  调用接口，根据返回值判断当前设备是否支持使用该特性。
    
    ```cpp
    AREngine_ARStatus ret = HMS_AREngine_CheckSupported(ARENGINE_FEATURE_TYPE_SLAM);
    ```
    

#### 引入AR Engine

1.  引入头文件。
    
    ```cpp
    #include "ar/ar_engine_core.h"
    ```
    
2.  编写CMakeLists.txt。
    
    ```cpp
    find_library(
        # Sets the name of the path variable.
        arengine-lib
        # Specifies the name of the NDK library that
        # you want CMake to locate.
        libarengine_ndk.z.so
    )
    
    target_link_libraries(entry PUBLIC
        ${arengine-lib}
    )
    ```
    

#### 创建AR会话

应用开始时，调用[HMS\_AREngine\_ARSession\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_create)函数创建一个AR会话。

```cpp
AREngine_ARSession *arSession = nullptr;
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
```

#### 自定义配置AR会话

创建一个[AREngine\_ARConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arconfig)对象来配置当前AR会话。如缺省，则使用默认配置，具体配置可参考[HMS\_AREngine\_ARConfig\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arconfig_create)。

```cpp
// 创建一个拥有合理默认配置的配置对象。
AREngine_ARConfig *arConfig = nullptr;
HMS_AREngine_ARConfig_Create(arSession, &arConfig);

// 此处配置arConfig。

// 配置AREngine_ARSession会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);

// 释放指定的配置对象的内存空间。
HMS_AREngine_ARConfig_Destroy(arConfig);
```

具体可配置项，请参考[AR Engine API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)。

#### 销毁AR会话

应用结束时，调用[HMS\_AREngine\_ARSession\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_destroy)函数销毁当前的AR会话。

```cpp
HMS_AREngine_ARSession_Destroy(arSession);
```
