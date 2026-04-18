---
title: "ArkUI_ActiveChildrenInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_ActiveChildrenInfo"
captured_at: "2026-04-17T01:48:09.791Z"
---

# ArkUI\_ActiveChildrenInfo

```c
typedef struct ArkUI_ActiveChildrenInfo ArkUI_ActiveChildrenInfo
```

#### 概述

定义ActiveChildrenInfo类信息。

**起始版本：** 14

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)

**相关接口：**

| 名称 | 描述 |
| :-- | :-- |
| [OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getactivechildreninfo) | 获取某个节点所有活跃的子节点。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_activechildreninfo_getnodebyindex) | 获取ActiveChildrenInfo结构体的下标为index的子节点。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_GetCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_activechildreninfo_getcount) | 获取ActiveChildrenInfo结构体内的节点数量。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_activechildreninfo_destroy) | 销毁ActiveChildrenInfo实例。 |
