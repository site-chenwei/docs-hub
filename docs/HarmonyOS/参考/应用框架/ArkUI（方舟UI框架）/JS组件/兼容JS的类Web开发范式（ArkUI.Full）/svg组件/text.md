---
title: "text"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-text"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "svg组件"
  - "text"
captured_at: "2026-04-17T01:48:05.943Z"
---

# text

文本，用于呈现一段信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/kY-uE8h7RE2yG1TYSfZ2vA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=468E1D2F47572B65EF9D9A03AF905FF340936F395A463BB62D742FDA5B222BD7)

-   该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   文本的展示内容需要写在元素标签内，可嵌套tspan子元素标签分段，可嵌套textPath子元素标签按指定路径绘制。
    
-   只支持被父元素标签svg嵌套。
    
-   只支持默认字体sans-serif。
    

#### 权限列表

无

#### 子组件

支持[tspan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-tspan)、[textPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-textpath)、[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。

#### 属性

支持以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| id | string | \- | 否 | 组件的唯一标识。 |
| x | <length>|<percentage> | 0 | 否 | 设置组件左上角x轴坐标。 |
| y | <length>|<percentage> | 0 | 否 | 设置组件左上角y轴坐标。 |
| dx | <length>|<percentage> | 0 | 否 | 设置文本x轴偏移。 |
| dy | <length>|<percentage> | 0 | 否 | 设置文本y轴偏移。 |
| rotate | number | 0 | 否 | 字体以左下角为圆心旋转角度，正数顺时针，负数逆时针。 |
| font-size | <length> | 30px | 否 | 设置文本的尺寸。 |
| fill | <color> | black | 否 | 字体填充颜色。 |
| fill-opacity | number | 1.0 | 否 | 字体填充透明度。 |
| opacity | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。 |
| stroke | <color> | black | 否 | 绘制字体边框并指定颜色。 |
| stroke-width | number | 1 | 否 | 
字体边框宽度。

默认单位：px

 |
| stroke-opacity | number | 1.0 | 否 | 字体边框透明度。 |

#### 示例

```css
/* xxx.css */
.container {
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 1000px;
    width: 1080px;
}
```

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20px" y="0px" font-size="30" fill="blue">test x|y</text>
    <text x="150" y="15" font-size="30" fill="blue">test x|y</text>
    <text x="300" y="30" font-size="30" fill="blue" opacity="0.1">test opacity</text>
    <text dx="20" y="30" dy="50" fill="blue" font-size="30">test dx|dy|fill|font-size</text>
    <text x="20" y="150" fill="blue" font-size="30" fill-opacity="0.2">test fill-opacity</text>
    <text x="20" y="200" fill="red" font-size="40">test 0123456789</text>
    <text x="20" y="250" fill="red" font-size="40" fill-opacity="0.2">test 中文</text>
    <text x="20" y="300" rotate="30" fill="red" font-size="40">test rotate</text>
    <text x="20" y="350" fill="blue" font-size="40" stroke="red" stroke-width="2">test stroke</text>
    <text x="20" y="400" fill="white" font-size="40" stroke="red" stroke-width="2" stroke-opacity="0.5">test stroke-opacity</text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/oQ1hkB1RRnCp2WwIxrJE2g/zh-cn_image_0000002538021196.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=FCBDC241C075237B0744654F8E67EE7B9B6DC90678195F6659CAEB93610F67BA)

属性动画示例

```css
/* xxx.css  */
.container {
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 3000px;
    width: 1080px;
}
```

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text y="50" font-size="30" fill="blue">
        text attribute x|opacity|rotate
      <animate attributeName="x" from="100" by="400" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animate>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/_q34g7oaR16fqKM7ekydBQ/zh-cn_image_0000002538181122.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=83D2D6B8A99D3B3E38E5B0FD00DE1CE36AD1891A3E38E762BFA4EE5AE35F71E2)

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20" y="200" fill="blue">
      text attribute font-size
      <animate attributeName="font-size" from="10" to="50" dur="3s" repeatCount="indefinite">
      </animate>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/uhp2w6WkTviEoTk-MKhz1g/zh-cn_image_0000002569020909.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=7D52AA3CE6E0742C730DD84B6EB4411756AF56A419C9EAD5B4E7EE48B3F81A1F)

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20" y="250" font-size="25" fill="blue" stroke="red">
      text attribute stroke
      <animate attributeName="stroke" from="red" to="#00FF00" dur="3s" repeatCount="indefinite"></animate>
    </text>
    <text x="300" y="250" font-size="25" fill="white" stroke="red">
      text attribute stroke-width-opacity
      <animate attributeName="stroke-width" from="1" to="5" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="stroke-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/UUGjq1UXTRyx3CAd0WsxUg/zh-cn_image_0000002568900899.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=FAC57580528F3AB71A85AC620326FEDEF645D8AD0BADDED272BB1C4C4503301E)
