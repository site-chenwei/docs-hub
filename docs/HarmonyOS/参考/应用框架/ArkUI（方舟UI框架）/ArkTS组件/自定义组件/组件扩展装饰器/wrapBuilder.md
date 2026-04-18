---
title: "wrapBuilder"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-wrapbuilder"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "自定义组件"
  - "组件扩展装饰器"
  - "wrapBuilder"
captured_at: "2026-04-17T01:47:59.384Z"
---

# wrapBuilder

使用wrapBuilder封装全局@Builder，可以帮助维护代码。开发指南见[wrapBuilder：封装全局@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/9iVHKdnTQWGbYJJDr5FGUQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=FBFA501B949EF66FE3650289CB1AB2ECDF803DF7BA9B22849AA3CF668C41E069)

本模块首批接口从API version 11开始支持。

后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### wrapBuilder

wrapBuilder<Args extends Object\[\]>(builder: (...args: Args) => void): WrappedBuilder<Args>

wrapBuilder是一个模板函数，返回一个WrappedBuilder对象。模板参数Args extends Object\[\]是需要包装的builder函数的参数列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| builder | (...args: Args) => void | 是 | @Builder装饰的全局函数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WrappedBuilder<Args>](#wrappedbuilder) | WrappedBuilder对象。 |

**示例：**

```ts
@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<[string, number]> = wrapBuilder(MyBuilder);
```

#### WrappedBuilder

@Builder函数的包装类。模板参数Args extends Object\[\]应传入@Builder函数的参数类型列表。

#### \[h2\]属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| builder | (...args: Args) => void | 否 | 否 | @Builder修饰的全局函数。 |

#### \[h2\]constructor

constructor(builder: (...args: Args) => void)

WrappedBuilder的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| builder | (...args: Args) => void | 是 | @Builder装饰的全局函数。 |

**示例：**

```ts
@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<[string, number]> = new WrappedBuilder<[string, number]>(MyBuilder);
```
