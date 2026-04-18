---
title: "NativeVSync开发指导 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-vsync-guidelines"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "NativeVSync开发指导 (C/C++)"
captured_at: "2026-04-17T01:36:09.075Z"
---

# NativeVSync开发指导 (C/C++)

#### 场景介绍

NativeVSync模块用于获取系统VSync信号，提供OH\_NativeVSync实例的创建、销毁及设置VSync回调函数的功能。VSync信号触发时，将调用已设置的回调函数。

#### 接口说明

| 接口名 | 描述 |
| :-- | :-- |
| OH\_NativeVSync\_Create (const char \*name, unsigned int length) | 创建一个OH\_NativeVSync实例，每次调用都会产生一个新的实例并创建一个vsync线程接收处理回调。本接口需要与OH\_NativeVSync\_Destroy接口配合使用，否则会存在内存泄露。 |
| OH\_NativeVSync\_Destroy (OH\_NativeVSync \*nativeVsync) | 销毁OH\_NativeVSync实例。 |
| OH\_NativeVSync\_FrameCallback (long long timestamp, void \*data) | 回调函数的形式，timestamp表示时间戳，data为回调函数入参。回调的处理在vsync初始化时创建的线程内。 |
| OH\_NativeVSync\_RequestFrame (OH\_NativeVSync \*nativeVsync, OH\_NativeVSync\_FrameCallback callback, void \*data) | 请求下一次VSync信号，当信号到来时，调用回调函数callback。 |

详细的接口说明请参考[native\_vsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync)。

#### 开发步骤

以下步骤描述如何使用NativeVSync提供的Native API接口创建和销毁OH\_NativeVSync实例，以及如何设置VSync回调函数。

**添加动态链接库**

CMakeLists.txt中添加以下库文件。

```txt
libnative_vsync.so
```

**头文件**

```
#include <native_vsync/native_vsync.h>
```

1.  **首先需要定义一个VSync回调函数**。
    
    void RenderEngine::OnVsync(long long timestamp, void \*data)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_DEBUG, LOG\_PRINT\_DOMAIN, "RenderEngine", "OnVsync %{public}lld.", timestamp);
        auto renderEngine = reinterpret\_cast<RenderEngine \*>(data);
        if (renderEngine == nullptr) {
            return;
        }
    
        renderEngine->vSyncCnt\_++;
        renderEngine->wakeUpCond\_.notify\_one();
    }
    
2.  **创建OH\_NativeVSync实例**。
    
    const char\* demoName = "NativeImageSample";
    nativeVsync\_ = OH\_NativeVSync\_Create(demoName, strlen(demoName));
    
3.  **通过OH\_NativeVSync实例设置VSync回调函数**。
    
    wakeUpCond\_.wait(lock, \[this\]() { return wakeUp\_ || vSyncCnt\_ > 0; });
    wakeUp\_ = false;
    if (vSyncCnt\_ > 0) {
        vSyncCnt\_--;
        (void)OH\_NativeVSync\_RequestFrame(nativeVsync\_, &RenderEngine::OnVsync, this);
        OH\_NativeVSync\_GetPeriod(nativeVsync\_, &period);
    }
    
4.  **销毁OH\_NativeVSync实例**。
    
    OH\_NativeVSync\_Destroy(nativeVsync\_);
    nativeVsync\_ = nullptr;
