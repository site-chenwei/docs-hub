---
title: "L2 Cache"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-l2cache"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC昇腾到麒麟兼容性迁移指南"
  - "Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导"
  - "基础API迁移指导"
  - "L2 Cache"
captured_at: "2026-04-17T01:36:38.572Z"
---

# L2 Cache

KirinX90/Kirin9030处理器不支持L2 Cache，GlobalTensor::SetL2CacheHint接口不生效。算子代码无需进行修改。只影响性能，不影响功能。
