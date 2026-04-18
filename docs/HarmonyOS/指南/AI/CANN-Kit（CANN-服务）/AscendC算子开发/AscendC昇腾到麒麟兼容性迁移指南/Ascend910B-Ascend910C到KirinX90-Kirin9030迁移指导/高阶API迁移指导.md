---
title: "高阶API迁移指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-adv-api"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC昇腾到麒麟兼容性迁移指南"
  - "Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导"
  - "高阶API迁移指导"
captured_at: "2026-04-17T01:36:38.686Z"
---

# 高阶API迁移指导

高阶API，数据类型支持范围存在差异，详见[《Ascend C算子接口》](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascend-c-apis)。数据类型差异兼容策略，参考[数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-datatype)。下面重点描述接口功能差异的兼容说明。

#### HCCL通信类

不支持HCCL通信类高阶API。

#### 矩阵计算

KirinX90/Kirin9030支持Matmul高阶API，但在涉及领域特性的部分存在不兼容情况。

**表1** Matmul高阶API

| 接口名称 | 兼容说明 |
| :-- | :-- |
| SetHF32 | 不支持。 |
| SetSparseIndex | 不支持。 |
| MatmulConfig | 不支持IBShare模板。 |
