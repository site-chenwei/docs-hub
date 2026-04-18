---
title: "OH_NativeXComponent_Callback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "OH_NativeXComponent_Callback"
captured_at: "2026-04-17T01:48:09.132Z"
---

# OH\_NativeXComponent\_Callback

```c
typedef struct OH_NativeXComponent_Callback {...} OH_NativeXComponent_Callback
```

#### 概述

注册Surface生命周期和触摸事件回调。

**起始版本：** 8

**相关模块：** [OH\_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)

**所在头文件：** [native\_interface\_xcomponent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h)

#### 汇总

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [void (\*OnSurfaceCreated)(OH\_NativeXComponent\* component, void\* window)](#onsurfacecreated) | 创建Surface时调用。 |
| [void (\*OnSurfaceChanged)(OH\_NativeXComponent\* component, void\* window)](#onsurfacechanged) | 当Surface改变时调用。 |
| [void (\*OnSurfaceDestroyed)(OH\_NativeXComponent\* component, void\* window)](#onsurfacedestroyed) | 当Surface被销毁时调用。 |
| [void (\*DispatchTouchEvent)(OH\_NativeXComponent\* component, void\* window)](#dispatchtouchevent) | 当触摸事件被触发时调用。 |

#### 成员函数说明

#### \[h2\]OnSurfaceCreated()

```c
void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window)
```

**描述：**

创建Surface时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)\* component | 表示指向[OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)实例的指针。 |
| void\* window | 
表示NativeWindow句柄。

通过XComponent生命周期获取的NativeWindow本身由系统侧持有了一次引用计数，并会在OnSurfaceDestroyed回调触发之后将引用计数减一，引用计数归零后NativeWindow将被释放。

 |

#### \[h2\]OnSurfaceChanged()

```c
void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface改变时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)\* component | 表示指向[OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)实例的指针。 |
| void\* window | 表示NativeWindow句柄。 |

#### \[h2\]OnSurfaceDestroyed()

```c
void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface被销毁时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)\* component | 表示指向[OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)实例的指针。 |
| void\* window | 表示NativeWindow句柄。 |

#### \[h2\]DispatchTouchEvent()

```c
void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window)
```

**描述：**

当触摸事件被触发时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)\* component | 表示指向[OH\_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent)实例的指针。 |
| void\* window | 表示NativeWindow句柄。 |
