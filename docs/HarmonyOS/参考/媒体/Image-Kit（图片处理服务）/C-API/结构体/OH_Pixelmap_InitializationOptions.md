---
title: "OH_Pixelmap_InitializationOptions"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/age-nativemodule-oh-pixelmap-initializationoptions"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OH_Pixelmap_InitializationOptions"
captured_at: "2026-04-17T01:48:42.138Z"
---

# OH\_Pixelmap\_InitializationOptions

```c
struct OH_Pixelmap_InitializationOptions
```

#### 概述

OH\_Pixelmap\_InitializationOptions是native层封装的初始化参数结构体，用于设置Pixelmap的初始化参数。

创建OH\_Pixelmap\_InitializationOptions对象使用[OH\_PixelmapInitializationOptions\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_create)函数。

释放OH\_Pixelmap\_InitializationOptions对象使用[OH\_PixelmapInitializationOptions\_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_release)函数。

OH\_Pixelmap\_InitializationOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| :-- | :-- | :-- | :-- | :-- |
| uint32\_t | width | 图片宽 | [OH\_PixelmapInitializationOptions\_GetWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_getwidth) | 获取图片宽。 |
| uint32\_t | width | 图片宽 | [OH\_PixelmapInitializationOptions\_SetWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_setwidth) | 设置图片宽。 |
| uint32\_t | height | 图片高 | [OH\_PixelmapInitializationOptions\_GetHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_getheight) | 获取图片高。 |
| uint32\_t | height | 图片高 | [OH\_PixelmapInitializationOptions\_SetHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_setheight) | 设置图片高。 |
| int32\_t | pixelFormat | 像素格式 | [OH\_PixelmapInitializationOptions\_GetPixelFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_getpixelformat) | 获取像素格式。 |
| int32\_t | pixelFormat | 像素格式 | [OH\_PixelmapInitializationOptions\_SetPixelFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_setpixelformat) | 设置像素格式。 |
| int32\_t | alphaType | 透明度类型 | [OH\_PixelmapInitializationOptions\_GetAlphaType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_getalphatype) | 获取透明度类型。 |
| int32\_t | alphaType | 透明度类型 | [OH\_PixelmapInitializationOptions\_SetAlphaType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_setalphatype) | 设置透明度类型。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [pixelmap\_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
