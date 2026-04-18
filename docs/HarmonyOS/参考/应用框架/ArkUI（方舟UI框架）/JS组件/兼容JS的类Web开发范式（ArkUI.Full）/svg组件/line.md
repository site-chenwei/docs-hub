---
title: "line"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-line"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "svg组件"
  - "line"
captured_at: "2026-04-17T01:48:05.891Z"
---

# line

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/sDjSDF0tSmSQOTu8JceTBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=2FDA2337289770B14AA1D9BE5BD0930369B67EAB8E33DF09254295FCEBE436B1)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制线条。

#### 权限列表

无

#### 子组件

支持[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。

#### 属性

支持Svg组件[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)和以下属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| id | string | \- | 否 | 组件的唯一标识。 |
| x1 | <length>|<percentage> | \- | 否 | 设置线条起点的x轴坐标。支持属性动画。 |
| y1 | <length>|<percentage> | \- | 否 | 设置线条起点的y轴坐标。支持属性动画。 |
| x2 | <length>|<percentage> | \- | 否 | 设置线条终点的x轴坐标。支持属性动画。 |
| y2 | <length>|<percentage> | \- | 否 | 设置线条终点的y轴坐标。支持属性动画。 |

#### 示例

```html
<!-- xxx.hml -->
<div class="container">
    <svg width="400" height="400">
        <line x1="10" x2="300" y1="50" y2="50" stroke-width="4" fill="white" stroke="blue"></line>
        <line x1="10" x2="300" y1="100" y2="100" stroke-width="4" fill="white" stroke="blue"></line>
        <line x1="10" x2="300" y1="150" y2="150" stroke-width="10" stroke="red" stroke-dasharray="5 3"
            stroke-dashoffset="3"></line>
        <!--round：在路径的末端延伸半个圆，直径等于线宽-->
        <line x1="10" x2="300" y1="200" y2="200" stroke-width="10" stroke="black" stroke-linecap="round"></line>
        <!--butt：不在路径两端扩展-->
        <line x1="10" x2="300" y1="220" y2="220" stroke-width="10" stroke="black" stroke-linecap="butt"></line>
        <!-- square：在路径的末端延伸一个矩形，宽度等于线宽的一半，高度等于线宽 -->
        <line x1="10" x2="300" y1="240" y2="240" stroke-width="10" stroke="black" stroke-linecap="square"></line>
    </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/SyXorAnRT6CVUrSiKurpXw/zh-cn_image_0000002538181120.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=DA797E25C24F044E3B1A2AFA47143CD3E5ADF11E09F4AB5ED4C0D86F5F00B5C5)
