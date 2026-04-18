---
title: "SuperKernel"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-superkernel"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC昇腾到麒麟兼容性迁移指南"
  - "Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导"
  - "基础API迁移指导"
  - "SuperKernel"
captured_at: "2026-04-17T01:36:38.668Z"
---

# SuperKernel

KirinX90/Kirin9030处理器不支持SuperKernel，所以如下接口在Kirin平台不生效。

**表1** KirinX90/Kirin9030任务间同步API

| 基础API | 兼容说明 |
| :-- | :-- |
| SetNextTaskStart、WaitPreTaskEnd | 
不生效。

KirinX90/Kirin9030不支持SuperKernel特性，所以任务间同步API不生效。算子代码无需进行修改。

 |
