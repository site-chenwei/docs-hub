---
title: "NativeBuffer开发指导 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-buffer-guidelines"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "NativeBuffer开发指导 (C/C++)"
captured_at: "2026-04-17T01:36:09.056Z"
---

# NativeBuffer开发指导 (C/C++)

#### 场景介绍

NativeBuffer模块提供**共享内存**功能，支持内存的申请、使用、查询和释放等操作。

NativeBuffer的常见开发场景：通过Native API申请OH\_NativeBuffer实例，获取内存属性，将ION内存映射到进程空间。

#### 接口说明

| 接口名 | 描述 |
| :-- | :-- |
| OH\_NativeBuffer\_Alloc (const OH\_NativeBuffer\_Config \*config) | 通过OH\_NativeBuffer\_Config创建OH\_NativeBuffer实例，每次调用都会产生一个新的OH\_NativeBuffer实例。本接口需要与OH\_NativeBuffer\_Unreference接口配合使用，否则会存在内存泄露。 |
| OH\_NativeBuffer\_Reference (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对象的引用计数增加1。 |
| OH\_NativeBuffer\_Unreference (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对象的引用计数减1，当引用计数为0的时候，该NativeBuffer对象会被析构掉。 |
| OH\_NativeBuffer\_GetConfig (OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_Config \*config) | 用于获取OH\_NativeBuffer的属性。 |
| OH\_NativeBuffer\_Map (OH\_NativeBuffer \*buffer, void \*\*virAddr) | 将OH\_NativeBuffer对应的ION内存映射到进程空间。 |
| OH\_NativeBuffer\_Unmap (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对应的ION内存从进程空间移除。 |
| OH\_NativeBuffer\_GetSeqNum (OH\_NativeBuffer \*buffer) | 获取OH\_NativeBuffer的序列号。 |

详细的接口说明请参考[native\_buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)。

#### 开发步骤

以下步骤描述了如何使用NativeBuffer提供的Native API接口创建OH\_NativeBuffer实例，获取内存属性信息，并将ION内存映射到进程空间。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```txt
libnative_buffer.so
```

**头文件**

```
#include <native_buffer/native_buffer.h>
```

1.  **创建OH\_NativeBuffer实例**。
    
    OH\_NativeBuffer\_Config config {
        .width = 0x100,
        .height = 0x100,
        .format = NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888,
        .usage = NATIVEBUFFER\_USAGE\_CPU\_READ | NATIVEBUFFER\_USAGE\_CPU\_WRITE | NATIVEBUFFER\_USAGE\_MEM\_DMA,
    };
    
    OH\_NativeBuffer \*nativeBuffer = OH\_NativeBuffer\_Alloc(&config);
    if (nativeBuffer == nullptr) {
        LOGE("OH\_NativeBuffer\_Alloc fail, nativeBuffer is null");
    }
    
2.  **将OH\_NativeBuffer对应的ION内存映射到进程空间**。
    
    应用如需访问buffer内存空间，可通过OH\_NativeBuffer\_Map接口将ION内存映射到进程空间。
    
    void\* virAddr = nullptr;
    int32\_t ret = OH\_NativeBuffer\_Map(nativeBuffer, &virAddr);
    if (ret != 0) {
        LOGE("OH\_NativeBuffer\_Map Failed");
    }
    // ...
    ret = OH\_NativeBuffer\_Unmap(nativeBuffer);
    if (ret != 0) {
        LOGE("OH\_NativeBuffer\_Unmap Failed");
    }
    
3.  **获取内存的属性信息**。
    
    OH\_NativeBuffer\_Config config2 = {};
    OH\_NativeBuffer\_GetConfig(nativeBuffer, &config2);
    uint32\_t hwBufferID = OH\_NativeBuffer\_GetSeqNum(nativeBuffer);
    
4.  **销毁OH\_NativeBuffer**。
    
    OH\_NativeBuffer\_Unreference(nativeBuffer);
    nativeBuffer = nullptr;
