---
title: "polyline"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polyline"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "svg组件"
  - "polyline"
captured_at: "2026-04-17T01:48:05.920Z"
---

# polyline

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/-iGk1q3ySAKoq31XowaKUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=C0DD77A9657D50651C519FFC1DE64489EC96A24356DD04EA98AD0006FE210C94)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制折线。

#### 权限列表

无

#### 子组件

支持[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。

#### 属性

支持Svg组件[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)和以下属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| id | string | \- | 否 | 组件的唯一标识。 |
| points | string | \- | 否 | 
设置折线的多个坐标点。

格式为\[x1,y1 x2,y2 x3,y3\]。

支持属性动画，如果属性动画里设置的动效变化值的坐标个数与原始points的格式不一样，则无效。

 |

#### 示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" stroke="blue" width="400" height="400">
    <polyline points="10,110 60,35 60,85 110,10" fill="red"></polyline>
    <polyline points="10,200 60,125 60,175 110,100" stroke-dasharray="10 5" stroke-dashoffset="3"></polyline>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/P_fck82nT7yHN9gG0DG5rQ/zh-cn_image_0000002569020907.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=271AA66206342378ED4AA45A42B259149D4884AACC3453D26B9A30FB5CDB4C55)
