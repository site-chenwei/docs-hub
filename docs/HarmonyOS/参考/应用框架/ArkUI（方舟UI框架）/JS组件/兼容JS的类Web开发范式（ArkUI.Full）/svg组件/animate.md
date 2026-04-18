---
title: "animate"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "svg组件"
  - "animate"
captured_at: "2026-04-17T01:48:05.982Z"
---

# animate

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/y2EmGeGaQJygHDv-E42OGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=D651BFFD3C986F7DDA9318626C478A1A358CF36DDEAE8B0037CFA7A6A0695C14)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

设置svg组件的属性动画。

#### 权限列表

无

#### 子组件

不支持。

#### 属性

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| id | string | \- | 否 | 组件的唯一标识。 |
| attributeName | string | \- | 否 | 设置需要进行动效的属性名。 |
| begin | <time> | 0 | 否 | 
设置动效的延迟时间。

支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。

 |
| dur | <time> | 0 | 否 | 

设置动效持续时间，如果dur没设置，按照end-begin的结果作为持续时间，小于等于0时，动效不触发。

支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。

 |
| end | <time> | 0 | 否 | 设置动效多久时间后结束。支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。 |
| repeatCount | <number | indefinite> | 1 | 否 | 设置动画播放的次数，默认无限次播放(indefinite)，可通过设置为数值1仅播放一次。 |
| fill | <freeze | remove> | remove | 否 | 设置动画结束时的状态。 |
| calcMode | <discrete | linear | paced | spline> | linear | 否 | 

设置动画的插值模式。

discrete：阶跃，from值直接跳转到to的值；

linear：线性；

paced：线性，设置此项后keyTimes和keyPoints值无效；

spline：自定义贝塞尔曲线，spline点定义在keyTimes属性中，每个时间间隔控制点由keySplines定义。

 |
| keyTimes | string | \- | 否 | 设置关键帧动画的开始时间，值为0~1之间的数值用分号隔开，比如0;0.3;0.8;1。keyTimes、keySplines、values组合设置关键帧动画。keyTimes和values的个数保持一致。keySplines个数为keyTimes个数减一。 |
| keySplines | string | \- | 否 | 与keyTimes相关联的一组贝塞尔控制点。定义每个关键帧的贝塞尔曲线，曲线之间用分号隔开。曲线内的两个控制点格式为x1 y1 x2 y2。比如0.5 0 0.5 1; 0.5 0 0.5 1;0.5 0 0.5 1 |
| by | number | \- | 否 | 在动画中对某一指定属性，添加相对偏移值，from默认为原属性值。 |
| from | string | \- | 否 | 

设置需要进行动画的属性的开始值。

如果已经设置了values属性，则from失效。

 |
| to | string | \- | 否 | 

设置需要进行动画的属性的结束值。

如果已经设置了values属性，则to都失效。

 |
| values | string | \- | 否 | 设置一组动画的变化值。格式为value1;value2;value3。 |

#### 示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
      <animate attributeName="rx" values="0;10;30;0" keyTimes="0;0.25;0.75;1" keySplines="0.5 0 0.5 1; 0.5 0 0.5 1; 0.5 0 0.5 1" dur="1000" repeatCount="indefinite">
      </animate>
    </rect>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/OibtaE5VQKGTHxzX8d_fzw/zh-cn_image_0000002538181130.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=48B29AA521EC0CB871EDFF75EAAAAC07C0A2861311BFB5656A054AF0B47C2A2F)

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
      <animate attributeName="fill" from="red" to="blue" dur="1000" repeatCount="indefinite"></animate>
      <animate attributeName="height" from="50" to="150" begin="500" end="1000" repeatCount="indefinite">  </animate>
    </rect>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/05JkHhywTneC7QGEm0XV2Q/zh-cn_image_0000002569020917.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=E129EE3B18436769B1384D171ED812F8EA8CC5DDE261B102CE5D2CE1A5546646)

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
      <animate attributeName="rx" values="0;30" dur="1000" repeatCount="indefinite" fill="freeze" calcMode="linear"></animate>
    </rect>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/KMxKlEIZSC6LSDmbuUUmUw/zh-cn_image_0000002568900907.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=978390B233042F2C821CA2BDCCC64380A4554CC1CE7A13C4524B6E1BCD3F8003)

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="600" height="600">
    <circle cx="60" cy="70" r="50" stroke-width="4" fill="white" stroke="blue">
      <animate attributeName="r" from="0" to="50" dur="2000" repeatCount="indefinite"></animate>
      <animate attributeName="cx" from="60" to="200" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="60" cy="200" r="50" stroke-width="4" fill="white" stroke="blue">
      <animate attributeName="stroke-width" from="4" to="10" calcMode="discrete" dur="2000" repeatCount="indefinite"></animate>
      <animate attributeName="stroke" values="red;blue" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="180" cy="200" r="50" stroke-width="10" stroke="red" stroke-dasharray="60 10" stroke-dashoffset="3">
      <animate attributeName="stroke-opacity" from="1.0" to="0.5" dur="2000" repeatCount="indefinite"></animate>
      <animate attributeName="stroke-dashoffset" values="30;0;30" dur="500" repeatCount="indefinite"></animate>
     <animate attributeName="cx" from="180" to="400" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="180" cy="200" r="5" fill="blue">
      <animate attributeName="cx" from="180" to="400" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="60" cy="380" r="50"  fill="blue">
      <animate attributeName="fill" values="red;blue" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="180" cy="380" r="50"  fill="blue">
      <animate attributeName="fill-opacity" from="1.0" to="0.5" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/9nhG9-7lRBSnsR6kB7UDiw/zh-cn_image_0000002538021206.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=4301E9B8D5149734851C5314C67D7DFD534F7B25DD6D96E45113C35D1272037C)
