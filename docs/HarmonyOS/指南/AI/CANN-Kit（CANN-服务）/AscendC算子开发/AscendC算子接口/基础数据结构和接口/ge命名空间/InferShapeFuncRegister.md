---
title: "InferShapeFuncRegister"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapefuncregister"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferShapeFuncRegister"
captured_at: "2026-04-17T01:36:34.407Z"
---

# InferShapeFuncRegister

#### 函数功能

InferShapeFuncRegister构造函数和析构函数。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/KC1-y1yBQ6mr-sHP6dWrwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=D7D5535D2F38A7992AA5972DE5F013F87380359B071C1F2FE1E31836891420C6)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
InferShapeFuncRegister (const std::string &operator_type, const InferShapeFunc &infer_shape_func);
InferShapeFuncRegister(const char *const operator_type, const InferShapeFunc &infer_shape_func);
~ InferShapeFuncRegister()
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| operator\_type | 输入 | 算子类型。 |
| infer\_shape\_func | 输入 | 算子InferShape函数。 |

#### 返回值

InferShapeFuncRegister构造函数返回InferShapeFuncRegister类型的对象。

#### 约束说明

算子InferShape函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。
