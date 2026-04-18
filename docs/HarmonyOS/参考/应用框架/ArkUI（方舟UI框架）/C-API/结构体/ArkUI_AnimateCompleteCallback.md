---
title: "ArkUI_AnimateCompleteCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-animatecompletecallback"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_AnimateCompleteCallback"
captured_at: "2026-04-17T01:48:08.555Z"
---

# ArkUI\_AnimateCompleteCallback

```c
typedef struct {...} ArkUI_AnimateCompleteCallback
```

#### 概述

动画播放结束回调类型。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_animate.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [ArkUI\_FinishCallbackType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_finishcallbacktype) type | 在动画中定义结束回调的类型。 |
| void\* userData | 用于动画结束回调，传递用户自定义数据。 |

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [void (\*callback)(void\* userData)](#callback) | 动画播放结束回调。 |

#### 成员函数说明

#### \[h2\]callback()

```c
void (*callback)(void* userData)
```

**描述：**

动画播放结束回调。
