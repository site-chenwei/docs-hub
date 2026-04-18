---
title: "NativeWindow开发指导 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-guidelines"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "NativeWindow开发指导 (C/C++)"
captured_at: "2026-04-17T01:36:09.083Z"
---

# NativeWindow开发指导 (C/C++)

#### 场景介绍

NativeWindow是**本地平台化窗口**，表示图形队列的生产者端。开发者可以通过NativeWindow接口进行申请和提交Buffer，配置Buffer属性信息。

针对NativeWindow，常见的开发场景如下：

-   通过NativeWindow提供的Native API接口申请图形Buffer，并将生成的图形内容写入图形Buffer，最终提交Buffer到图形队列。
-   在适配EGL层的eglswapbuffer接口时，进行申请和提交Buffer。

#### 接口说明

| 接口名 | 描述 |
| :-- | :-- |
| OH\_NativeWindow\_NativeWindowRequestBuffer (OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer, int \*fenceFd) | 通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产。 |
| OH\_NativeWindow\_NativeWindowFlushBuffer (OHNativeWindow \*window, OHNativeWindowBuffer \*buffer, int fenceFd, Region region) | 通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费。 |
| OH\_NativeWindow\_NativeWindowHandleOpt (OHNativeWindow \*window, int code,...) | 设置/获取OHNativeWindow的属性，包括设置/获取宽高、内容格式等。 |

详细的接口说明请参考[native\_window](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow)。

#### 开发步骤

以下步骤描述了如何使用NativeWindow提供的Native API接口申请图形Buffer，写入图形内容，并提交Buffer到图形队列。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```txt
libace_ndk.z.so
libnative_window.so
```

**头文件**

```
#include <sys/poll.h>
#include <sys/mman.h>
#include <unistd.h>
#include <ace/xcomponent/native_interface_xcomponent.h>
#include <native_window/external_window.h>
```

1.  获取OHNativeWindow实例。
    
    可通过[OH\_NativeXComponent\_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback)接口获取OHNativeWindow。代码示例如下。关于XComponent模块的使用方法，详见[XComponent开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。
    
    1.  在xxx.ets中添加一个XComponent组件。
        
        XComponent({ id: 'xcomponentId', type: 'texture', libraryname: 'nativerender' })
          .margin({ bottom: 26 })
          .onLoad((nativeWindowContext) => {
            this.nativeWindowContext = nativeWindowContext as NativeWindowContext;
          })
        
    2.  在 native c++ 层获取 NativeXComponent。
        
        napi\_value exportInstance = nullptr;
        OH\_NativeXComponent \*nativeXComponent = nullptr;
        int32\_t ret;
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        
        status = napi\_get\_named\_property(env, exports, OH\_NATIVE\_XCOMPONENT\_OBJ, &exportInstance);
        if (status != napi\_ok) {
            return false;
        }
        
        status = napi\_unwrap(env, exportInstance, reinterpret\_cast<void\*\*>(&nativeXComponent));
        if (status != napi\_ok) {
            return false;
        }
        
        ret = OH\_NativeXComponent\_GetXComponentId(nativeXComponent, idStr, &idSize);
        if (ret != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            return false;
        }
        
    3.  定义 OH\_NativeXComponent\_Callback。
        
        void OnSurfaceCreatedCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ...
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
            // ...
        }
        
        void OnSurfaceChangedCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ...
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
            // ...
        }
        
        void OnSurfaceDestroyedCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ...
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
            // ...
        }
        
        void DispatchTouchEventCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ...
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
        }
        // ...
        callback\_.OnSurfaceCreated = OnSurfaceCreatedCB;
        callback\_.OnSurfaceChanged = OnSurfaceChangedCB;
        callback\_.OnSurfaceDestroyed = OnSurfaceDestroyedCB;
        callback\_.DispatchTouchEvent = DispatchTouchEventCB;
        
    4.  将OH\_NativeXComponent\_Callback 注册给 NativeXComponent。
        
        OH\_NativeXComponent\_RegisterCallback(nativeXComponent, &callback\_);
        
2.  设置OHNativeWindowBuffer的属性。使用OH\_NativeWindow\_NativeWindowHandleOpt设置OHNativeWindowBuffer的属性（默认携带NATIVEBUFFER\_USAGE\_CPU\_READ usage参数，如果不使用CPU读写数据，建议去除NATIVEBUFFER\_USAGE\_CPU\_READ usage参数，具体可见[关闭CPU访问窗口缓冲区数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-14)）。
    
    int code = SET\_BUFFER\_GEOMETRY;
    int32\_t bufferHeight = static\_cast<int32\_t>(height\_ / 4);
    int32\_t bufferWidth = static\_cast<int32\_t>(width\_ / 2);
    OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow\_, code, bufferWidth, bufferHeight);
    
3.  从图形队列申请OHNativeWindowBuffer。
    
    int fenceFd = -1;
    OHNativeWindowBuffer \*nativeWindowBuffer = nullptr;
    ret = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow, &nativeWindowBuffer, &fenceFd);
    if (ret != 0 || nativeWindowBuffer == nullptr) {
        return;
    }
    BufferHandle \*bufferHandle = OH\_NativeWindow\_GetBufferHandleFromNative(nativeWindowBuffer);
    
4.  内存映射mmap。
    
    void \*mappedAddr =
        mmap(bufferHandle->virAddr, bufferHandle->size, PROT\_READ | PROT\_WRITE, MAP\_SHARED, bufferHandle->fd, 0);
    
5.  将生产的内容写入OHNativeWindowBuffer，在这之前需要等待releaseFenceFd可用（注意releaseFenceFd不等于-1才需要调用poll）。如果没有等待releaseFenceFd事件的数据可用（POLLIN），则可能造成花屏、裂屏、HEBC（High Efficiency Bandwidth Compression，高效带宽压缩） fault等问题。releaseFenceFd是消费者进程创建的一个文件句柄，代表消费者消费buffer完毕，buffer可读，生产者可以开始填充buffer内容。
    
    int retCode = -1;
    uint32\_t timeout = 3000;
    if (fenceFd != -1) {
        struct pollfd pollfds = {0};
        pollfds.fd = fenceFd;
        pollfds.events = POLLIN;
        do {
            retCode = poll(&pollfds, 1, timeout);
        } while (retCode == -1 && (errno == EINTR || errno == EAGAIN));
        close(fenceFd);
    }
    uint32\_t \*pixel = static\_cast<uint32\_t \*>(mappedAddr);
    for (uint64\_t x = 0; x < bufferHandle->width; x++) {
        for (uint64\_t y = 0; y < bufferHandle->height; y++) {
            \*pixel++ = value;
        }
    }
    
6.  提交OHNativeWindowBuffer到图形队列。请注意OH\_NativeWindow\_NativeWindowFlushBuffer接口的acquireFenceFd不可以和OH\_NativeWindow\_NativeWindowRequestBuffer接口获取的releaseFenceFd相同，acquireFenceFd可传入默认值-1。acquireFenceFd是生产者需要传入的文件句柄，消费者获取到buffer后可根据生产者传入的acquireFenceFd决定何时去渲染并上屏buffer内容。
    
    struct Region \*region = new Region();
    ret = OH\_NativeWindow\_NativeWindowFlushBuffer(nativeWindow, nativeWindowBuffer, fenceFd, \*region);
    if (ret != NATIVE\_ERROR\_OK) {
        LOGE("flush failed");
        (void)OH\_NativeWindow\_NativeWindowAbortBuffer(nativeWindow, nativeWindowBuffer);
        return;
    }
    
7.  使用munmap取消内存映射。
    
    if (munmap(mappedAddr, bufferHandle->size) < 0) {
        OH\_NativeWindow\_DestroyNativeWindow(nativeWindow);
        LOGE("munmap failed");
        return;
    }
