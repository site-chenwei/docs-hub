---
title: "Destroy"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-destroy"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "基础API"
  - "内存管理与同步控制"
  - "TPipe"
  - "Destroy"
captured_at: "2026-04-17T01:36:26.223Z"
---

# Destroy

#### 功能说明

释放资源。

#### 函数原型

```cpp
__aicore__ inline void Destroy()
```

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 注意事项

用于重复申请释放TPipe，创建Tpipe对象后，可调用Destroy手动释放资源。

#### 返回值

无

#### 调用示例

```cpp
AscendC::TPipe pipe; // Pipe内存管理对象
// 输出数据Queue队列管理对象，QuePosition为VECOUT
AscendC::TQue<AscendC::TPosition::VECOUT, 2> que;
uint8_t num = 2;
uint32_t len = 128;
pipe.InitBuffer(que, num, len);
pipe.Destroy();
```
