---
title: "Camera_ConcurrentInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-concurrentinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_ConcurrentInfo"
captured_at: "2026-04-17T01:48:39.940Z"
---

# Camera\_ConcurrentInfo

```c
typedef struct Camera_ConcurrentInfo {...} Camera_ConcurrentInfo
```

#### 概述

相机并发能力信息。

**起始版本：** 18

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Camera\_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device) camera | 相机实例。 |
| [Camera\_ConcurrentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_concurrenttype) type | 相机并发状态。 |
| [Camera\_SceneMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_scenemode)\* sceneModes | 相机并发支持的模式。 |
| [Camera\_OutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-outputcapability)\* outputCapabilities | 相机输出能力集。 |
| uint32\_t modeAndCapabilitySize | 相机输出能力集大小。 |
