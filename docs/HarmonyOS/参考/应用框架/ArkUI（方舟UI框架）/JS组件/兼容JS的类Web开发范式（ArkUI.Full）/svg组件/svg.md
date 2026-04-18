---
title: "svg"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "svg组件"
  - "svg"
captured_at: "2026-04-17T01:48:05.836Z"
---

# svg

基础容器，主要作为svg的根节点使用，也可以在svg中嵌套使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/V7rMuCNSQYmezfvVyFOmag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=8DB2329B2D421849A7F6328FF4C3CE75A40A660A45AC4595CEB4634C15F8B1F5)

-   该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   svg父组件或者svg组件需要定义宽高值，否则不进行绘制。
    

#### 权限列表

无

#### 子组件

支持[svg](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg)、[rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-rect)、[circle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-circle)、[ellipse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-ellipse)、[path](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-path)、[line](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-line)、[polygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polygon)、[polyline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polyline)、[text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-text)、[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。

#### 属性

支持svg组件[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)和以下属性，设置的通用属性会传递给子组件。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| id | string | \- | 否 | 组件的唯一标识。 |
| width | <length>|<percentage> | \- | 否 | 设置组件的宽度。 |
| height | <length>|<percentage> | \- | 否 | 设置组件的高度。 |
| x | <length>|<percentage> | \- | 否 | 设置当前svg的x轴坐标，根svg节点无效。 |
| y | <length>|<percentage> | \- | 否 | 设置当前svg的y轴坐标，根svg节点无效。 |
| viewBox | string | \- | 否 | 设置当前svg的视口。支持的格式为<number number number number>，4个参数分别表示min-x, min-y, width and height，viewBox的宽高和svg的宽高不一致，会以中心对齐进行缩放。 |

#### 示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <svg width="200" height="200" viewBox="0 0 100 100">
      <rect x="10" y="10" width="80" height="80" fill="#00FF00"></rect>
    </svg>
    <rect x="10" y="10" width="80" height="80" fill="red" ></rect>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 200 200">
      <rect x="10" y="10" width="80" height="80" fill="red"></rect>
    </svg>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 400 400">
      <rect x="10" y="10" width="80" height="80" fill="blue"></rect>
    </svg>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ciSDQdRMQQiYBA1vdPUWIg/zh-cn_image_0000002538021192.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=21AD0F370FF0C897E0570492E70B517DB59E05DFFFD698FD3B6F67E261CC5799)
