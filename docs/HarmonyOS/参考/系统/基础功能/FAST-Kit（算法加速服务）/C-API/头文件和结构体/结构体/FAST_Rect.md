---
title: "FAST_Rect"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "FAST Kit（算法加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "FAST_Rect"
captured_at: "2026-04-17T01:48:30.002Z"
---

# FAST\_Rect

#### 概述

定义矩形的数据结构（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.0.2(22)

**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)

**所在头文件：** [fast\_solver\_rect\_partition.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-rect-partition-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t [left](#left) | 横坐标左边界（![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/_gokWNbaTAehTuDFy8xzig/zh-cn_image_0000002538181422.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=03178D4382A555A18E52BE16285109B0BAF01EEBEA4B432162D56A88D21A3F25)）。 |
| int32\_t [top](#top) | 纵坐标上边界（![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Q9FhsOzQTY268rsEsnpQKA/zh-cn_image_0000002569021209.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=1B410D278CF3345C50566B046AA119A1B1C46CEA38FE17CE99042C6B03DA043F)）。 |
| int32\_t [right](#right) | 横坐标右边界（![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/U3PqKfvbRj2LsSYyrWU6Kw/zh-cn_image_0000002568901199.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=7830086775478856327B558C432C43E70DACE7D14CEDD789093165D9D87B4C4B)）。 |
| int32\_t [bottom](#bottom) | 纵坐标下边界（![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/APYcoOQ1TwKUz73ggaZshw/zh-cn_image_0000002538021498.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=DED5277D84F967ADC524024127D9F7E046F2BE25825E1D104446F5C553B8B911)）。 |

#### 结构体成员变量说明

#### \[h2\]bottom

```c
int32_t FAST_Rect::bottom
```

**描述**

纵坐标下边界。

#### \[h2\]left

```c
int32_t FAST_Rect::left
```

**描述**

横坐标左边界。

#### \[h2\]right

```c
int32_t FAST_Rect::right
```

**描述**

横坐标右边界。

#### \[h2\]top

```c
int32_t FAST_Rect::top
```

**描述**

纵坐标上边界。
