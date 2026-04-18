---
title: "GetUserWorkspace"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getuserworkspace"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "基础API"
  - "内存管理与同步控制"
  - "workspace"
  - "GetUserWorkspace"
captured_at: "2026-04-17T01:36:26.801Z"
---

# GetUserWorkspace

#### 功能说明

获取开发者使用的[workspace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsysworkspaceptr)指针。如果使用了[Matmul](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matmul-usage-description)等需要系统workspace的高阶API，kernel侧需要通过[SetSysWorkSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setsysworkspace)设置系统workspace，此时开发者workspace需要通过该接口获取。

#### 函数原型

```cpp
__aicore__ inline GM_ADDR GetUserWorkspace(GM_ADDR workspace)
```

#### 参数说明

**表1** 接口参数说明

| 参数名称 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| workspace | 输入 | 传入workspace的指针，包括系统workspace和开发者使用的workspace。 |

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 注意事项

无

#### 返回值

开发者使用workspace指针。
