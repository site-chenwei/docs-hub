---
title: "HandWrite"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-c"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Pen Kit（手写笔服务）"
  - "C API"
  - "模块"
  - "HandWrite"
captured_at: "2026-04-17T01:48:33.635Z"
---

# HandWrite

#### 概述

该模块对外提供手写能力。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

#### 汇总

#### \[h2\]文件

| 名称 | 描述 |
| :-- | :-- |
| [native\_handwrite\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-headerfile-declare) | 声明用于对外提供手写能力。 |

#### \[h2\]结构体

| 名称 | 描述 |
| :-- | :-- |
| struct [HandWrite\_HistoricalPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-struct-historicalpoint) | 定义历史触摸点信息的结构体。 |

#### \[h2\]枚举

| 名称 | 描述 |
| :-- | :-- |
| 
enum [HandWrite\_ErrCode](#handwrite_errcode) {

E\_NO\_ERROR = 0,

E\_PARAMS = 401,

E\_INNER\_ERROR = 1010400001

}

 | 定义手写错误码。 |

#### \[h2\]函数

| 名称 | 函数 |
| :-- | :-- |
| 
int32\_t [HMS\_HandWrite\_GetPredictPoint](#hms_handwrite_getpredictpoint)(const [HandWrite\_HistoricalPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-struct-historicalpoint)\* event,

int32\_t size, float \*predictPointX, float \*predictPointY)

 | 此接口用于获取预测点。 |

#### 枚举类型说明

#### \[h2\]HandWrite\_ErrCode

```c
enum HandWrite_ErrCode
```

**描述**

定义手写错误码。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| :-- | :-- |
| E\_NO\_ERROR | 执行成功。 |
| E\_PARAMS | 输入参数无效。 |
| E\_INNER\_ERROR | 系统内部错误，相关资源加载失败。 |

#### 函数说明

#### \[h2\]HMS\_HandWrite\_GetPredictPoint()

```c
int32_t HMS_HandWrite_GetPredictPoint(const HandWrite_HistoricalPoint* event,
    int32_t size, float *predictPointX, float *predictPointY)
```

**描述**

此接口用于获取预测点。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| event | 指示输入的历史点。 |
| size | 历史点的个数。 |
| predictPointX | 接收预测点X坐标的指针。 |
| predictPointY | 接收预测点Y坐标的指针。 |

**返回：** 手写错误码HandWrite\_ErrCode：

E\_NO\_ERROR 0 - 执行成功。

E\_PARAMS 401 - 输入参数无效。

E\_INNER\_ERROR 1010400001 - 系统内部错误，相关资源加载失败。
