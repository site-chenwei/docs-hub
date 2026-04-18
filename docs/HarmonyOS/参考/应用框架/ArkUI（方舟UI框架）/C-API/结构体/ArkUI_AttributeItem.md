---
title: "ArkUI_AttributeItem"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_AttributeItem"
captured_at: "2026-04-17T01:48:09.291Z"
---

# ArkUI\_AttributeItem

```c
typedef struct {...} ArkUI_AttributeItem
```

#### 概述

定义[setAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute)函数通用入参结构。各个属性设置接口可选择使用其中的成员变量来存储特定类型的参数数据。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_node.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const [ArkUI\_NumberValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-numbervalue)\* value | 数字类型数组，用于存储数字数组类型的参数。 |
| int32\_t size | 数字类型数组大小，配合变量value使用，value数组的长度。 |
| const char\* string | 字符串类型，用于存储字符串类型的参数。 |
| void\* object | 对象类型，用于存储对象类型的参数。 |
