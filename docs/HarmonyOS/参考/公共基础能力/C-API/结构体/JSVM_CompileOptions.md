---
title: "JSVM_CompileOptions"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileoptions"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_CompileOptions"
captured_at: "2026-04-17T01:49:06.578Z"
---

# JSVM\_CompileOptions

```c
typedef struct {...} JSVM_CompileOptions
```

#### 概述

配合[OH\_JSVM\_CompileScriptWithOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_compilescriptwithoptions)接口使用，是其参数中options数组的元素类型。

**起始版本：** 12

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [JSVM\_CompileOptionId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h#jsvm_compileoptionid) id | 编译选项对应的ID。 |
| content | id对应的编译选项值联合体。 |
| content.ptr | 指向编译选项值的指针。 |
| content.num | 存储整数类型的编译选项值。 |
| content.boolean | 存储布尔类型的编译选项值。 |
