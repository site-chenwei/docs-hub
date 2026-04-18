---
title: "ImageEffect_FilterDelegate"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-filterdelegate"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "ImageEffect_FilterDelegate"
captured_at: "2026-04-17T01:48:42.828Z"
---

# ImageEffect\_FilterDelegate

```c
typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterDelegate
```

#### 概述

自定义滤镜回调函数结构体。

**起始版本：** 12

**相关模块：** [ImageEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect)

**所在头文件：** [image\_effect\_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_EffectFilterDelegate\_SetValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_setvalue) setValue | 参数设置函数指针。 |
| [OH\_EffectFilterDelegate\_Render](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_render) render | 滤镜渲染函数指针。 |
| [OH\_EffectFilterDelegate\_Save](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_save) save | 序列化效果器函数指针。 |
| [OH\_EffectFilterDelegate\_Restore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_restore) restore | 反序列化效果器函数指针。 |
