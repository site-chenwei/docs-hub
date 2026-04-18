---
title: "GetSysWorkSpacePtr"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsysworkspaceptr"
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
  - "GetSysWorkSpacePtr"
captured_at: "2026-04-17T01:36:26.794Z"
---

# GetSysWorkSpacePtr

#### 功能说明

获取系统workspace指针。部分高阶API如Matmul需要使用系统workspace，相关接口需要传入系统workspace指针，此时可以通过该接口获取。使用系统workspace时，host侧开发者需要自行申请系统workspace的空间，其预留空间大小可以通过[GetLibApiWorkSpaceSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getlibapiworkspacesize)接口获取。

#### 函数原型

```cpp
__aicore__ inline __gm__ uint8_t* __gm__ GetSysWorkSpacePtr()
```

#### 参数说明

无

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 注意事项

无

#### 返回值

系统workspace指针。

#### 调用示例

```cpp
// ...
REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling); // 初始化
// CopyIn阶段：完成从GM到LocalMemory的搬运
mm.SetTensorA(gm_a);    // 设置左矩阵A
mm.SetTensorB(gm_b);    // 设置右矩阵B
mm.SetBias(gm_bias);    // 设置Bias
// Compute阶段：完成矩阵乘计算
while (mm.Iterate()) {
    // CopyOut阶段：完成从LocalMemory到GM的搬运
    mm.GetTensorC(gm_c);
}
// 结束矩阵乘操作
mm.End();
```
