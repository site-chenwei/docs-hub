---
title: "End"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-end"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "高阶API"
  - "矩阵相乘"
  - "Matmul"
  - "End"
captured_at: "2026-04-17T01:36:27.251Z"
---

# End

#### 功能说明

单核内Matmul矩阵相乘计算结束后必须调用一次End函数。

#### 函数原型

```cpp
__aicore__ inline void End()
```

#### 参数说明

无

#### 返回值

无

#### 支持的型号

Kirin9020系列处理器

#### 注意事项

无

#### 调用示例

```cpp
mm.IterateAll(gm_c);
mm.End();
```
