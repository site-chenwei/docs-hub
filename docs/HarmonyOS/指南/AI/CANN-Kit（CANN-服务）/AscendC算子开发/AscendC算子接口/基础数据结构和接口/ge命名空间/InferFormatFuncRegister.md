---
title: "InferFormatFuncRegister"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inferformatfuncregister"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferFormatFuncRegister"
captured_at: "2026-04-17T01:36:31.856Z"
---

# InferFormatFuncRegister

#### 函数功能

InferFormatFuncRegister构造函数和析构函数。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/sz7Q6v-DTVuUE7l6Iv_pSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=92A20DFCF63011FCA201070699AF03F963DD4A9BF485FF82E88720B2E544BBA2)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
InferFormatFuncRegister(const std::string &operator_type, const InferFormatFunc &infer_format_func);
InferFormatFuncRegister(const char_t *const operator_type, const InferFormatFunc &infer_format_func);
~InferFormatFuncRegister() = default;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| operator\_type | 输入 | 算子类型。 |
| infer\_format\_func | 输入 | 算子InferFormat函数。 |

#### 返回值

InferFormatFuncRegister构造函数返回InferFormatFuncRegister类型的对象。

#### 约束说明

算子InferFormat函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。
