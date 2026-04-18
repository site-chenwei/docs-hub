---
title: "Kernel Tiling"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-kernel-tiling"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC昇腾到麒麟兼容性迁移指南"
  - "Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导"
  - "基础API迁移指导"
  - "Kernel Tiling"
captured_at: "2026-04-17T01:36:38.673Z"
---

# Kernel Tiling

KirinX90/Kirin9030处理器不支持如下Kernel Tiling接口。

**表1** Kernel Tiling兼容说明

| 基础API | 兼容说明 |
| :-- | :-- |
| KERNEL\_TASK\_TYPE\_DEFAULT、KERNEL\_TASK\_TYPE | 
不支持。

KirinX90/Kirin9030 AI处理器为耦合架构(AI Core: 1 \* AIC + 1 \* AIV)，下发Task执行时，会将整个AI Core启动。当算子配置MIX\_AIC\_1\_2时，需要关注AIV核个数的差异对算子功能的影响。

 |
