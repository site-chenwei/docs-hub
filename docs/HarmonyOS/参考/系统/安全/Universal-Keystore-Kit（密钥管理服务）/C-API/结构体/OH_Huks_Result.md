---
title: "OH_Huks_Result"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-result"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_Result"
captured_at: "2026-04-17T01:48:20.690Z"
---

# OH\_Huks\_Result

```c
struct OH_Huks_Result {...}
```

#### 概述

表示状态返回数据，包括返回码和消息。

**起始版本：** 9

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native\_huks\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t errorCode | 状态返回码，参考[OH\_Huks\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_errcode)。 |
| const char \*errorMsg | 对状态返回码的说明信息。 |
| uint8\_t \*data | 其他返回数据。 |
