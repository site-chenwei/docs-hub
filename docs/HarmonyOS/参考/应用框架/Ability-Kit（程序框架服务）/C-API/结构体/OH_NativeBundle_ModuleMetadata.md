---
title: "OH_NativeBundle_ModuleMetadata"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-modulemetadata"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "C API"
  - "结构体"
  - "OH_NativeBundle_ModuleMetadata"
captured_at: "2026-04-17T01:47:48.820Z"
---

# OH\_NativeBundle\_ModuleMetadata

```c
typedef struct OH_NativeBundle_ModuleMetadata {...} OH_NativeBundle_ModuleMetadata
```

#### 概述

模块元数据的信息。

**起始版本：** 20

**相关模块：** [Native\_Bundle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)

**所在头文件：** [native\_interface\_bundle.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* moduleName | 模块名称。 |
| [OH\_NativeBundle\_Metadata\*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-metadata) metadataArray | 模块的元数据数组。 |
| size\_t metadataArraySize | 模块的元数据数组大小。 |
