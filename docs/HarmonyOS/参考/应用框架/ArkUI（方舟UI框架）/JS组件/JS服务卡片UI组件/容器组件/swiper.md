---
title: "swiper"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-swiper"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "JS服务卡片UI组件"
  - "容器组件"
  - "swiper"
captured_at: "2026-04-17T01:48:07.031Z"
---

# swiper

滑动容器，提供切换子组件显示的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ObV3W1naRxKCl4x976kXLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=6D864A18A3D6F9BDA891D9CD0AC9F190A5B0183C92157F1AAFDBB1D889D9E64A)

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-attributes)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| index | number | 0 | 否 | 当前在容器中显示的子组件的索引值。 |
| indicator | boolean | true | 否 | 是否启用导航点指示器，默认true。true为启用导航点指示器，false为不启用。 |
| digital | boolean | false | 否 | 
是否启用数字导航点，默认为false。true为启用数字导航点，false为不启用。

必须设置indicator时才能生效数字导航点。

 |
| loop | boolean | true | 否 | 是否开启循环滑动。true为开启循环，false为关闭循环。 |
| duration | number | 0 | 否 | 

子组件切换的动画时长。

单位：毫秒

取值范围：\[0, +∞)

 |
| vertical | boolean | false | 否 | 是否为纵向滑动。true为纵向滑动，false为水平滑动。纵向滑动时采用纵向的指示器。 |

#### 样式

除支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-styles)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| indicator-color | <color> | \- | 否 | 导航点指示器的填充颜色。 |
| indicator-selected-color | <color> | \- | 否 | 导航点指示器选中的颜色。 |
| indicator-size | <length> | 4px | 否 | 导航点指示器的直径大小。 |
| indicator-top|left|right|bottom | <length> | <percentage> | \- | 否 | 导航点指示器在swiper中的相对位置。 |

#### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-events)。

#### 示例

```html
<!-- xxx.hml -->
<swiper class="container" index="{{index}}">
  <div class="swiper-item primary-item">
    <text>1</text>
  </div>
  <div class="swiper-item warning-item">
    <text>2</text>
  </div>
  <div class="swiper-item success-item">
    <text>3</text>
  </div>
</swiper>
```

```css
/* xxx.css */
.container {
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.swiper-item {
  width: 454px;
  height: 454px;
  justify-content: center;
  align-items: center;
}
.primary-item {
  background-color: #007dff;
}
.warning-item {
  background-color: #ff7500;
}
.success-item {
  background-color: #41ba41;
}
```

```json
{
  "data": {
    "index": 1
  }
}
```

**4×4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/GhXJXeWtSR69WhPWoKST3A/zh-cn_image_0000002538181304.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=29DA50A2F394F1E797529EEBD7DBF98209E0DC6914AF124E610B7461F18A3FE7)
