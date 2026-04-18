---
title: "DeQue"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-deque"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "基础API"
  - "内存管理与同步控制"
  - "TQueBind"
  - "DeQue"
captured_at: "2026-04-17T01:36:26.623Z"
---

# DeQue

#### 功能说明

将Tensor从队列中取出，用于后续处理。

#### 函数原型

```cpp
template <typename T> 
__aicore__ inline LocalTensor<T> DeQue()
```

**图1** 将LocalTensor通过EnQue放入A1/B1的Queue中后再通过DeQue搬出

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/nh7OxduKRJudZuk1-LPPiA/zh-cn_image_0000002568899933.png?HW-CC-KV=V1&HW-CC-Date=20260417T013628Z&HW-CC-Expire=86400&HW-CC-Sign=706E13C0A1A238604EAE5F6605E9C65C4BA818FCED91C7278307AD76F02D9DF0)

#### 参数说明

无

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 注意事项

无

#### 返回值

从队列中取出的[LocalTensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-localtensor)。

#### 调用示例

```cpp
// 接口: DeQue Tensor
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue(tensor1);
AscendC::LocalTensor<half> tensor2 = que.DeQue<half>(); // 将tensor从VECOUT的Queue中搬出
```
