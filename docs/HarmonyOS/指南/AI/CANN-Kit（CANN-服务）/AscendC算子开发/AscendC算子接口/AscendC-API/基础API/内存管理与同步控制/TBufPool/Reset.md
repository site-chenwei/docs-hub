---
title: "Reset"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-reset"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "基础API"
  - "内存管理与同步控制"
  - "TBufPool"
  - "Reset"
captured_at: "2026-04-17T01:36:26.389Z"
---

# Reset

#### 功能说明

完成TbufPool资源的释放与eventId等变量的初始化操作。

#### 函数原型

```cpp
__aicore__ inline void Reset()
```

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 注意事项

切换TBufPool资源池时调用该接口，调用后对应资源池及资源池分配的Buffer不能继续使用。

#### 返回值

无

#### 调用示例

参考[InitBufPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-initbufpool)。
