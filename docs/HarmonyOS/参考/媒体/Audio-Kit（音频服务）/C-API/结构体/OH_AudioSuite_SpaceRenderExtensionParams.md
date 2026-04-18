---
title: "OH_AudioSuite_SpaceRenderExtensionParams"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/udiosuite-oh-audiosuite-spacerenderextensionparams"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "C API"
  - "结构体"
  - "OH_AudioSuite_SpaceRenderExtensionParams"
captured_at: "2026-04-17T01:48:36.863Z"
---

# OH\_AudioSuite\_SpaceRenderExtensionParams

```c
struct OH_AudioSuite_SpaceRenderExtensionParams {...}
```

#### 概述

定义空间渲染效果节点扩展模式配置参数。

**起始版本：** 23

**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)

**所在头文件：** [native\_audio\_suite\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| float extRadius | 扩展半径。取值范围为\[1.0, 5.0\]，单位为米。 |
| int32\_t extAngle | 扩展角度。取值范围为(0, 360)，单位为度。 |
