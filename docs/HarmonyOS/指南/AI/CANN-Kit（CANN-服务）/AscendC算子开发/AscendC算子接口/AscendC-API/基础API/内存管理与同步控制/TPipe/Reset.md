---
title: "Reset"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tpipe-reset"
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
  - "Reset"
captured_at: "2026-04-17T01:36:26.214Z"
---

# Reset

#### 功能说明

完成资源的释放与eventId等变量的初始化操作，恢复到Tpipe的初始化状态。

#### 函数原型

```cpp
__aicore__ inline void Reset()
```

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 注意事项

无

#### 返回值

无

#### 调用示例

```cpp
AscendC::TPipe pipe; // Pipe内存管理对象
AscendC::TQue<AscendC::TPosition::VECOUT, 1> que; // 输出数据Queue队列管理对象，QuePosition为VECOUT
uint8_t num = 1;
uint32_t len = 192 * 1024;
for (int i = 0; i < 2; i++) {
    pipe.InitBuffer(que, num, len);
    // ... // process
    pipe.Reset();
}
```
