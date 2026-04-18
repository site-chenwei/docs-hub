---
title: "GetCoreNumAiv"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorenumaiv"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "Host API"
  - "平台信息获取PlatformAscendC"
  - "GetCoreNumAiv"
captured_at: "2026-04-17T01:36:27.761Z"
---

# GetCoreNumAiv

#### 函数功能

获取当前硬件平台AI Core中Vector核数。若AI Core的架构为Cube、Vector分离架构，返回AI Core上的Vector核数；非分离架构返回AI Core的核数。

#### 函数原型

```cpp
uint32_t GetCoreNumAiv(void) const;
```

#### 参数说明

无

#### 返回值

针对Kirin9020系列处理器，Cube、Vector分离架构，返回AI Core上的Vector核数。

#### 约束说明

无

#### 调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    auto aicNum = ascendcPlatform.GetCoreNumAic();
    auto aivNum = ascendcPlatform.GetCoreNumAiv();
    // ...按照aivNum切分
    context->SetBlockDim(ascendcPlatform.CalcTschBlockDim(aivNum, aicNum, aivNum));
    return ret;
}
```
