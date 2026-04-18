---
title: "OH_AudioSuite_SpaceRenderRotationParams"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/audiosuite-oh-audiosuite-spacerenderrotationparams"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "C API"
  - "结构体"
  - "OH_AudioSuite_SpaceRenderRotationParams"
captured_at: "2026-04-17T01:48:36.878Z"
---

# OH\_AudioSuite\_SpaceRenderRotationParams

```c
typedef struct {...} OH_AudioSuite_SpaceRenderRotationParams
```

#### 概述

定义空间渲染效果节点旋转模式配置参数。

**起始版本：** 23

**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)

**所在头文件：** [native\_audio\_suite\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| float x | 空间中的X坐标。取值范围为\[-5.0, 5.0\]，单位为米。 |
| float y | 空间中的Y坐标。取值范围为\[-5.0, 5.0\]，单位为米。 |
| float z | 空间中的Z坐标。取值范围为\[-5.0, 5.0\]，单位为米。 |
| int32\_t surroundTime | 单周环绕时间。取值范围为\[2, 40\]，单位为秒。 |
| [OH\_AudioSuite\_SurroundDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audiosuite_surrounddirection) surroundDirection | 单周环绕方向。取值范围为\[0, 1\]。 |
