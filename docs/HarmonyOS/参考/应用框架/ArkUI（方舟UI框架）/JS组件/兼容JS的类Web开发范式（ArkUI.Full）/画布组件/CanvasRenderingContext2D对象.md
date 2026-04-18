---
title: "CanvasRenderingContext2D对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "画布组件"
  - "CanvasRenderingContext2D对象"
captured_at: "2026-04-17T01:48:05.704Z"
---

# CanvasRenderingContext2D对象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/84SSTY3DSkqWnGuWvrymOQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=7511FA0EC6F229395AC208A844F6D99AA3267EE9051B03C2CAE954DE442984B7)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用CanvasRenderingContext2D在[canvas画布组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvas)上进行绘制，绘制对象可以是矩形、文本、图片等。

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="handleClick" onclick="handleClick" />
  <input type="button" style="width: 180px; height: 60px;" value="antialias" onclick="antialias" />
</div>
```

```js
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  },
  antialias() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d', { antialias: true });
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
    }
  }
```

-   示意图（关闭抗锯齿）
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/3Ye3tSnuRxyasLIeH-Pbfg/zh-cn_image_0000002538181082.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=24E36D04EEECDB51567758D71237E199C5C5EF35F64A13CC61F1E20357AEB60F)
    
-   示意图（开启抗锯齿）
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/UWxAFYVLRWyxkB0bJRDA1A/zh-cn_image_0000002569020869.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=B82DEDFDD5C9B762BC419AD0B7100D98D3DF8F578E6EE710E52B12C2D4A7B46A)
    

#### 属性

| 名称 | 类型 | 描述 |
| :-- | :-- | :-- |
| [fillStyle](#fillstyle) | <color> | [CanvasGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient) | [CanvasPattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern) | 
指定绘制的填充色。

\- 类型为<color>时，表示设置填充区域的颜色。

\- 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。

\- 类型为CanvasPattern时，使用 createPattern()方法创建。

超出取值范围填充为黑色。

 |
| [lineWidth](#linewidth) | number | 设置绘制线条的宽度。 |
| [strokeStyle](#strokestyle) | <color> | [CanvasGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient) | [CanvasPattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern) | 

设置描边的颜色。

\- 类型为<color>时，表示设置描边使用的颜色。

\- 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。

\- 类型为CanvasPattern时，使用 createPattern()方法创建。

 |
| [lineCap](#linecap) | string | 

指定线端点的样式，可选值为：

\- butt：线端点以方形结束。

\- round：线端点以圆形结束。

\- square：线端点以方形结束，该样式下会增加一个长度和线段厚度相同，宽度是线段厚度一半的矩形。

默认值：butt

 |
| [lineJoin](#linejoin) | string | 

指定线段间相交的交点样式，可选值为：

\- round：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。

\- bevel：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。

\- miter：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。

默认值：miter

 |
| [miterLimit](#miterlimit) | number | 

设置斜接面限制值，该值指定了线条相交处内角和外角的距离。

默认值：10

 |
| [font](#font) | string | 

设置文本绘制中的字体样式。

语法：ctx.font="font-style font-weight font-size font-family"5+

\- font-style(可选)，用于指定字体样式，支持如下几种样式：normal, italic。

\- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900。

\- font-size(可选)，指定字号和行高，单位只支持px。

\- font-family(可选)，指定字体系列，支持如下几种类型：sans-serif, serif, monospace。

默认值："normal normal 14px sans-serif"

 |
| [textAlign](#textalign) | string | 

设置文本绘制中的文本对齐方式，可选值为：

\- left：文本左对齐。

\- right：文本右对齐。

\- center：文本居中对齐。

\- start：文本对齐界线开始的地方。

\- end：文本对齐界线结束的地方。

ltr布局模式下start和left一致，rtl布局模式下start和right一致。

默认值：left

 |
| [textBaseline](#textbaseline) | string | 

设置文本绘制中的水平对齐方式，可选值为：

\- alphabetic：文本基线是标准的字母基线。

\- top：文本基线在文本块的顶部。

\- hanging：文本基线是悬挂基线。

\- middle：文本基线在文本块的中间。

\- ideographic：文字基线是表意字基线；如果字符本身超出了alphabetic 基线，那么ideographic基线位置在字符本身的底部。

\- bottom：文本基线在文本块的底部。 与 ideographic 基线的区别在于 ideographic 基线不需要考虑下行字母。

默认值： alphabetic

 |
| [globalAlpha](#globalalpha) | number | 

设置透明度。

范围为\[0.0, 1.0\]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。

 |
| [lineDashOffset](#linedashoffset) | number | 

设置画布的虚线偏移量，精度为float。

默认值：0.0

 |
| [globalCompositeOperation](#globalcompositeoperation) | string | 

设置合成操作的方式。类型字段可选值有source-over，source-atop，source-in，source-out，destination-over，destination-atop，destination-in，destination-out，lighter，copy，xor。具体请参考[类型字段说明](#globalcompositeoperation)。

默认值：source-over

 |
| [shadowBlur](#shadowblur) | number | 

设置绘制阴影时的模糊级别，值越大越模糊，精度为float。

默认值：0.0

 |
| [shadowColor](#shadowcolor) | <color> | 设置绘制阴影时的阴影颜色。 |
| [shadowOffsetX](#shadowoffsetx) | number | 设置绘制阴影时和原有对象的水平偏移值。 |
| [shadowOffsetY](#shadowoffsety) | number | 设置绘制阴影时和原有对象的垂直偏移值。 |
| [imageSmoothingEnabled](#imagesmoothingenabled) | boolean | 

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。

默认值：true

 |

#### \[h2\]fillStyle

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = '#0000ff';
    ctx.fillRect(20, 20, 150, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/1PmVdhhHS26qUdCCKHQPyQ/zh-cn_image_0000002568900859.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=CD4403B23FA9FF018960D7BDC6F260979251A897ECE09F3AF1010C839423B1A3)

#### \[h2\]lineWidth

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 5;
    ctx.strokeRect(25, 25, 85, 105);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Yb0-KlCiS1GJB3nGSpzYAw/zh-cn_image_0000002538021158.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=3EC718B499A501C862C8AC6D0F2228CAA48872A7CF9612B6610F01736E616AA4)

#### \[h2\]strokeStyle

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 10;
    ctx.strokeStyle = '#0000ff';
    ctx.strokeRect(25, 25, 155, 105);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/6BWkTb9vRNuGZ_orPOiEVA/zh-cn_image_0000002538181084.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=11017F81A2EA3106BB648CB72FF4CF2D5A9AC6A403157EA9F237B1A5CB4C1423)

#### \[h2\]lineCap

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.lineCap = 'round';
    ctx.moveTo(30, 50);
    ctx.lineTo(220, 50);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/5l4c8z45Q6StFNeAh5BIbw/zh-cn_image_0000002569020871.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=9E9FB2EE4C82EC4289DB5865B36092E299B3E5106CF0E682F3691FB230A457D8)

#### \[h2\]lineJoin

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = 8;
    ctx.lineJoin = 'miter';
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 110);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/q3WgYAD4RMWNGrj_KjQVGw/zh-cn_image_0000002568900861.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=DBC54814D1A8BC0EB09DA9068889D145BEA123734F44B13F0FC76E46566E9BB8)

#### \[h2\]miterLimit

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth =14;
    ctx.lineJoin = 'miter';
    ctx.miterLimit = 3;
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 70);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/35H0ml8FQl2JQTP4QUjuag/zh-cn_image_0000002538021160.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=B612BDC953D1DB7B3B524EB33E21F297E78384D5079AC73124CB4C45B1A82D00)

#### \[h2\]font

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '30px sans-serif';
    ctx.fillText("Hello World", 20, 60);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/w8TrhdnZRTOoo-CdFddicQ/zh-cn_image_0000002538181086.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=9A462389FE2CC4A0AA670169D98AB27AD8E3A0021F3EAA04F2FFC8EA49A20713)

#### \[h2\]textAlign

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(140, 10);
    ctx.lineTo(140, 160);
    ctx.stroke();
    ctx.font = '18px sans-serif';
    // Show the different textAlign values
    ctx.textAlign = 'start';
    ctx.fillText('textAlign=start', 140, 60);
    ctx.textAlign = 'end';
    ctx.fillText('textAlign=end', 140, 80);
    ctx.textAlign = 'left';
    ctx.fillText('textAlign=left', 140, 100);
    ctx.textAlign = 'center';
    ctx.fillText('textAlign=center',140, 120);
    ctx.textAlign = 'right';
    ctx.fillText('textAlign=right',140, 140);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/X0qRxxfqTVuysOq_pyK1EQ/zh-cn_image_0000002569020873.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=183A64F57C41B484EB934B3BA688E8B5620E6880E2304A99876C79819CD2EB9D)

#### \[h2\]textBaseline

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(0, 120);
    ctx.lineTo(400, 120);
    ctx.stroke();
    ctx.font = '20px sans-serif';
    ctx.textBaseline = 'top';
    ctx.fillText('Top', 10, 120);
    ctx.textBaseline = 'bottom';
    ctx.fillText('Bottom', 55, 120);
    ctx.textBaseline = 'middle';
    ctx.fillText('Middle', 125, 120);
    ctx.textBaseline = 'alphabetic';
    ctx.fillText('Alphabetic', 195, 120);
    ctx.textBaseline = 'hanging';
    ctx.fillText('Hanging', 295, 120);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/LgH0PE82Tb-8Qci2TN-YNQ/zh-cn_image_0000002568900863.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=54D29170FA5CDE0D380B0D7DC7B243712AD955AF50CC1EF8AFA6D48DC3C1E796)

#### \[h2\]globalAlpha

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 50, 50);
    ctx.globalAlpha = 0.4;
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/374KApBoRnSHpDi6NZ_PYA/zh-cn_image_0000002538021162.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=F70AD71978540945297873C9E3032EA5EA787A24CF2C5004CFD56741CA38AE4A)

#### \[h2\]lineDashOffset

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10,20]);
    ctx.lineDashOffset = 10.0;
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/zuK2_Vs2RYSWsJpDoyp6KA/zh-cn_image_0000002538181088.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=D4439AAF2E70F0D65C0CCFF1E6B5BDC96E3D404A43066C8BC3FBDAA3169FC9E6)

#### \[h2\]globalCompositeOperation

类型字段说明。

| 值 | 描述 |
| :-- | :-- |
| source-over | 在现有绘制内容上显示新绘制内容，属于默认值。 |
| source-atop | 在现有绘制内容顶部显示新绘制内容。 |
| source-in | 在现有绘制内容中显示新绘制内容。 |
| source-out | 在现有绘制内容之外显示新绘制内容。 |
| destination-over | 在新绘制内容上方显示现有绘制内容。 |
| destination-atop | 在新绘制内容顶部显示现有绘制内容。 |
| destination-in | 在新绘制内容中显示现有绘制内容。 |
| destination-out | 在新绘制内容外显示现有绘制内容。 |
| lighter | 显示新绘制内容和现有绘制内容。 |
| copy | 显示新绘制内容而忽略现有绘制内容。 |
| xor | 使用异或操作对新绘制内容与现有绘制内容进行融合。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 50, 50);
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);
    // Start drawing second example
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(120, 20, 50, 50);
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(150, 50, 50, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/c9mNAoHKTtqti-ul99SbdQ/zh-cn_image_0000002569020875.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=F458918F9E9BFA37C62C2EE69588F2FC948878D46AAA90846A938B2AB7BE90BF)

示例中，新绘制内容是蓝色矩形，现有绘制内容是红色矩形。

#### \[h2\]shadowBlur

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tltZCFVWSyiPSeHM_hN7uw/zh-cn_image_0000002568900865.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=5491834842CCEDE4EDB179D3462C2C5F95161CE101E037AED7154A6366039543)

#### \[h2\]shadowColor

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,255)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/WOPch3AyR6O8zGOXIL5caA/zh-cn_image_0000002538021164.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=1149A5966ECF30623063D89B27F1FA0F605648F0DFC8683E90F5477833E88308)

#### \[h2\]shadowOffsetX

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetX = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Gm9I3jZpTnO3qbjR3uqzHg/zh-cn_image_0000002538181090.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=8076BCFC703DBC07CD925D02C9180071A21AAA570190621FF81E938D2D51A7EF)

#### \[h2\]shadowOffsetY

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetY = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
 }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/nK_uv24JSHyKYBdcSoYLOQ/zh-cn_image_0000002569020877.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=9D35378555541A370EF14D080D8CF3A6AD42A75F6EBEE1D95598430D41FC6F66)

#### \[h2\]imageSmoothingEnabled

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/image/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/example.jpg';
    img.onload = function() {
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(img, 0, 0, 400, 200);
    };
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/L-2uSEhATgioH3gD4WUUwQ/zh-cn_image_0000002568900867.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=F3B1DDA10305EE44BE54CE6F641DDB2086F087E8874B570E174192355FD18633)

#### 方法

#### \[h2\]fillRect

fillRect(x: number, y: number, width:number, height: number): void

填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
指定矩形左上角点的x坐标。

单位：vp

 |
| y | number | 是 | 

指定矩形左上角点的y坐标。

单位：vp

 |
| width | number | 是 | 

指定矩形的宽度。

单位：vp

 |
| height | number | 是 | 

指定矩形的高度。

单位：vp

 |

**示例：**

```html
  <!-- xxx.hml -->
  <div>
    <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  </div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(20, 20, 200, 150);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/vNk6s3foQ46LMLHrohQYFg/zh-cn_image_0000002538021166.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=D2F3F8F7F7C9FDA16A0DBBFABCF329B770B84FFA305AC6B7E5806F1D2EA9AF02)

#### \[h2\]clearRect

clearRect(x: number, y: number, width:number, height: number): void

删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
指定矩形上的左上角x坐标。

单位：vp

 |
| y | number | 是 | 

指定矩形上的左上角y坐标。

单位：vp

 |
| width | number | 是 | 

指定矩形的宽度。

单位：vp

 |
| height | number | 是 | 

指定矩形的高度。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(100, 100, 200, 200);
    ctx.clearRect(110, 110, 80, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/e2G_-kevSNqTX3NV1_bTIA/zh-cn_image_0000002538181092.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=4A2DBAFAF77D956278963E6CF98DA55CB2ABBDFE09260ABC5117B691A34781F9)

#### \[h2\]strokeRect

strokeRect(x: number, y: number, width:number, height: number): void

绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
指定矩形的左上角x坐标。

单位：vp

 |
| y | number | 是 | 

指定矩形的左上角y坐标。

单位：vp

 |
| width | number | 是 | 

指定矩形的宽度。

单位：vp

 |
| height | number | 是 | 

指定矩形的高度。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(100, 100, 200, 150);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/lW7QR3kERba93G6Xg5AvTg/zh-cn_image_0000002569020879.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=A50C5535B6FB9BA2AAD95D1F5F2EDCB27BDB04F30A9DD980DF05ACBDBC570A08)

#### \[h2\]fillText

fillText(text: string, x: number, y: number): void

绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 
需要绘制的文本的左下角x坐标。

单位：vp

 |
| y | number | 是 | 

需要绘制的文本的左下角y坐标。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '35px sans-serif';
    ctx.fillText("Hello World!", 10, 60);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/JqInqlsUT-W0FdG7TrNW8w/zh-cn_image_0000002568900869.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=FE6AE26C2C8A0AFC479C485D6DF22FF0299CE582CC5E17E37D0C493496CF8575)

#### \[h2\]strokeText

strokeText(text: string, x: number, y: number): void

绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 
需要绘制的文本的左下角x坐标。

单位：vp

 |
| y | number | 是 | 

需要绘制的文本的左下角y坐标。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '25px sans-serif';
    ctx.strokeText("Hello World!", 10, 60);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/BEWK-6x6SZO8Ckz5qeVQwg/zh-cn_image_0000002538021168.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=B177E93BCEB1048BA5B837673DF885D6045CDAFC942FCA23E0856CEDC488E0EC)

#### \[h2\]measureText

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 需要进行测量的文本。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| TextMetrics | 包含指定字体的宽度，该宽度可以通过TextMetrics.width来获取。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '20px sans-serif';
    var txt = 'Hello World';
    ctx.fillText("width:" + ctx.measureText(txt).width, 20, 60);
    ctx.fillText(txt, 20, 110);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/7O1TI_m9T9iypX1hsufD5A/zh-cn_image_0000002538181094.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=36907DD162F00EED07D1B097B33408FF4251B37ADBE9FC4B9F58B50784C7D3E2)

#### \[h2\]stroke

stroke(): void

进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(25, 25);
    ctx.lineTo(25, 250);
    ctx.lineWidth = '6';
    ctx.strokeStyle = 'rgb(0,0,255)';
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/k2GpOaO5RsWkOzG8gRdFqA/zh-cn_image_0000002569020881.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=E8A03454970AB42DD9C7B7CC8712A1317BE7677C4E0FF610E08262AD27719097)

#### \[h2\]beginPath

beginPath(): void

创建一个新的绘制路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = '6';
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(15, 80);
    ctx.lineTo(280, 80);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/9McRS9D_QvCtiodSaVY32Q/zh-cn_image_0000002568900871.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=0BC618752B05C56AD14AE56B1308FD501EB6186773FAB5937A8A45551E5ABB86)

#### \[h2\]moveTo

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
指定位置的x坐标。

单位：vp

 |
| y | number | 是 | 

指定位置的y坐标。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/_bhT20ggRqma3Xn-H0PAyg/zh-cn_image_0000002538021170.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=134BB735343272360431D91922A249029802A27EA1155C539D233753D9E0BF4E)

#### \[h2\]lineTo

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
指定位置的x坐标。

单位：vp

 |
| y | number | 是 | 

指定位置的y坐标。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/6PP8H2qHQA-EvT7IpOllVA/zh-cn_image_0000002538181096.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=F7D50D3F2A1EE9C4F3708779E057ABE7E763F8035D5163EE2074A98E305961D9)

#### \[h2\]closePath

closePath(): void

结束当前路径形成一个封闭路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(30, 30);
    ctx.lineTo(110, 30);
    ctx.lineTo(70, 90);
    ctx.closePath();
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/0_xaoc5uR-y-_tjvy5znsw/zh-cn_image_0000002569020883.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=8422345C076AF7B471EDA07FC1BEFEC6A6CA2D69DAA07EC45B01043F0734C661)

#### \[h2\]createPattern

createPattern(image: Image, repetition: string): Object

通过指定图像和重复方式创建图片填充的模板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| image | Image | 是 | 图源对象，具体参考[Image对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-image)。 |
| repetition | string | 是 | 设置图像重复的方式，取值为：'repeat'、'repeat-x'、 'repeat-y'、'no-repeat'。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Object | 指定图像填充的Pattern对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 1000px; height: 1000px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/images/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/images/example.jpg';
    var pat = ctx.createPattern(img, 'repeat');
    ctx.fillStyle = pat;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/96rn3zKCTE6g0zNqJZDv0w/zh-cn_image_0000002568900873.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=FFBDFF0337BD043EB8EA6FE5063DB83FC5314991C90EB9E2079F4438D5D9EBE6)

#### \[h2\]bezierCurveTo

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| cp1x | number | 是 | 
第一个贝塞尔参数的x坐标值。

单位：vp

 |
| cp1y | number | 是 | 

第一个贝塞尔参数的y坐标值。

单位：vp

 |
| cp2x | number | 是 | 

第二个贝塞尔参数的x坐标值。

单位：vp

 |
| cp2y | number | 是 | 

第二个贝塞尔参数的y坐标值。

单位：vp

 |
| x | number | 是 | 

路径结束时的x坐标值。

单位：vp

 |
| y | number | 是 | 

路径结束时的y坐标值。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Ve4Qs76JSj2EqorYmyrX5Q/zh-cn_image_0000002538021172.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=7840C69CC99000C627704505A7B95D4112E2E54733B45F82C63FAA0D16A6439A)

#### \[h2\]quadraticCurveTo

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| cpx | number | 是 | 
贝塞尔参数的x坐标值。

单位：vp

 |
| cpy | number | 是 | 

贝塞尔参数的y坐标值。

单位：vp

 |
| x | number | 是 | 

路径结束时的x坐标值。

单位：vp

 |
| y | number | 是 | 

路径结束时的y坐标值。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(20, 20);
    ctx.quadraticCurveTo(100, 100, 200, 20);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/oJ5dxEyYTBSUE9E3z7P4Kw/zh-cn_image_0000002538181098.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=6B098899DF3242AB733FBBEAD1084868CCDDAA73CC29124658C0506EFBAF1518)

#### \[h2\]arc

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
弧线圆心的x坐标值。

单位：vp

 |
| y | number | 是 | 

弧线圆心的y坐标值。

单位：vp

 |
| radius | number | 是 | 

弧线的圆半径。

单位：vp

 |
| startAngle | number | 是 | 

弧线的起始弧度。

单位：vp

 |
| endAngle | number | 是 | 

弧线的终止弧度。

单位：vp

 |
| counterclockwise | boolean | 否 | 

是否逆时针绘制圆弧，true为逆时针，false为顺时针。

默认值：false

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/2uQ2JWe4Rri1fHSygRUcKg/zh-cn_image_0000002569020885.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=8372090051D2BC1AB302D4C93F6C91310389344D672DAA8857009D095B4680F6)

#### \[h2\]arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x1 | number | 是 | 
圆弧经过的第一个点的x坐标值。

单位：vp

 |
| y1 | number | 是 | 

圆弧经过的第一个点的y坐标值。

单位：vp

 |
| x2 | number | 是 | 

圆弧经过的第二个点的x坐标值。

单位：vp

 |
| y2 | number | 是 | 

圆弧经过的第二个点的y坐标值。

单位：vp

 |
| radius | number | 是 | 

圆弧的圆半径值。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(100, 20);
    ctx.arcTo(150, 20, 150, 70, 50); // Create an arc
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/cGwMaQBSTQSwK6v3WmH3GA/zh-cn_image_0000002568900875.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=9F5ADB9D40CD070ADA3FEF9C0B2450B64EF6DA5EE7DFE883B9F464E66D68A31B)

#### \[h2\]ellipse

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
椭圆圆心的x轴坐标。

单位：vp

 |
| y | number | 是 | 

椭圆圆心的y轴坐标。

单位：vp

 |
| radiusX | number | 是 | 

椭圆x轴的半径长度。

单位：vp

 |
| radiusY | number | 是 | 

椭圆y轴的半径长度。

单位：vp

 |
| rotation | number | 是 | 

椭圆的旋转角度，单位为弧度。

单位：vp

 |
| startAngle | number | 是 | 

椭圆绘制的起始点角度，以弧度表示。

单位：vp

 |
| endAngle | number | 是 | 

椭圆绘制的结束点角度，以弧度表示。

单位：vp

 |
| counterclockwise | number | 否 | 

是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。

单位：vp

默认值：0

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/dv2JX4sRTem7eyqooryyhQ/zh-cn_image_0000002538021174.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=E8CDE227874AF870A946A4A658CDD5F1874CBE4696380F8F4FCF76BD2DD89F8E)

#### \[h2\]rect

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
指定矩形的左上角x坐标值。

单位：vp

 |
| y | number | 是 | 

指定矩形的左上角y坐标值。

单位：vp

 |
| width | number | 是 | 

指定矩形的宽度。

单位：vp

 |
| height | number | 是 | 

指定矩形的高度。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.stroke(); // Draw it
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/jECL-cE_Sb6-M4mFwCQuSw/zh-cn_image_0000002538181100.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=9FB72B767D6AD7639322DBB473A107D8B177743515E8EA8C4629A5F3F8DC303E)

#### \[h2\]fill

fill(): void

对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.fill(); // Draw it in default setting
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/8g64nxxFSW2RKfG1VFtstw/zh-cn_image_0000002569020887.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=03748753651777AFD879B14D4E01D6449E5DD8FF9485CE5C136C0D72B6B6580F)

#### \[h2\]clip

clip(): void

设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(100, 100, 200, 200);
    ctx.stroke();
    ctx.clip();
    // Draw red rectangle after clip
    ctx.fillStyle = "rgb(255,0,0)";
    ctx.fillRect(100, 100, 150, 150);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/2VrmJVYTSyKufWRh-r5xAg/zh-cn_image_0000002568900877.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=E7C86A4B0FE95741611308F42310E8A27C29AF68D71D909750290E7E81BD4BE0)

#### \[h2\]rotate

rotate(rotate: number): void

针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotate | number | 是 | 
设置顺时针旋转的弧度值，可以通过Math.PI / 180将角度转换为弧度值。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rotate(45 * Math.PI / 180); // Rotate the rectangle 45 degrees
    ctx.fillRect(70, 20, 50, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/JzPPj7ieRfml0tXu4Iq52A/zh-cn_image_0000002538021176.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=DD4D89982F6C4D3BF040AFA4528DBDD7C7BE1A7EB41CF2922DFF23EAC6FC2C43)

#### \[h2\]scale

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
设置水平方向的缩放值。

单位：vp

 |
| y | number | 是 | 

设置垂直方向的缩放值。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(10, 10, 25, 25);
    ctx.scale(2, 2);// Scale to 200%
    ctx.strokeRect(10, 10, 25, 25);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/PxttLkEFROiuWDmXidg-IA/zh-cn_image_0000002538181102.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=3EAEE92C89375C16C7CD8DB6433BC5A7C6FDAAA10C45D1E60FDB679290718271)

#### \[h2\]transform

transform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/iTbXjCd5TtyNQKn81svyng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=F28EED666A760C2A6407FF24CAA927BD40930D93A80DAF54CB9E53D169B0E089)

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

-   x' = scaleX \* x + skewY \* y + translateX
    
-   y' = skewX \* x + scaleY \* y + translateY
    

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| scaleX | number | 是 | 
指定水平缩放值。

单位：vp

 |
| skewX | number | 是 | 

指定水平倾斜值。

单位：vp

 |
| skewY | number | 是 | 

指定垂直倾斜值。

单位：vp

 |
| scaleY | number | 是 | 

指定垂直缩放值。

单位：vp

 |
| translateX | number | 是 | 

指定水平移动值。

单位：vp

 |
| translateY | number | 是 | 

指定垂直移动值。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(0,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/HugNXppgQyeu3_r9zNLVtQ/zh-cn_image_0000002569020889.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=92850EDF602D645AF40071DE1B520BB236A2D4F178097DEDF068F2D0EE0B3607)

#### \[h2\]setTransform

setTransform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| scaleX | number | 是 | 
指定水平缩放值。

单位：vp

 |
| skewX | number | 是 | 

指定水平倾斜值。

单位：vp

 |
| skewY | number | 是 | 

指定垂直倾斜值。

单位：vp

 |
| scaleY | number | 是 | 

指定垂直缩放值。

单位：vp

 |
| translateX | number | 是 | 

指定水平移动值。

单位：vp

 |
| translateY | number | 是 | 

指定垂直移动值。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.setTransform(1,0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Az0ca5l1Tn-tke9fh438RA/zh-cn_image_0000002568900879.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=1FFA76A2A9F920D89EB5E12D8281FC41AFF3890638F5DC93A3B81799F33623FD)

#### \[h2\]translate

translate(x: number, y: number): void

移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 
设置水平平移量。

单位：vp

 |
| y | number | 是 | 

设置竖直平移量。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(10, 10, 50, 50);
    ctx.translate(70, 70);
    ctx.fillRect(10, 10, 50, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ew9Uzt3wQU-LNRcoKJkQkw/zh-cn_image_0000002538021178.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=6E8C1FFEBC158A75FA714AAA7B4D9C3EA859A1E25E6631AA98450FC5CAE552E4)

#### \[h2\]createPath2D6+

createPath2D(path: Path2D, cmds: string): Path2D

创建一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | Path2D | 是 | Path2D对象。 |
| cmds | string | 是 | SVG的Path描述字符串。 |

**返回值：**

[Path2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d)

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path1 = ctx.createPath2D();
    path1.moveTo(100, 100);
    path1.lineTo(200, 100);
    path1.lineTo(100, 200);
    path1.closePath();
    ctx.stroke(path1);
    var path2 = ctx.createPath2D("M150 150 L50 250 L250 250 Z");
    ctx.stroke(path2);
    var path3 = ctx.createPath2D(path2);
    ctx.stroke(path3);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/k7XCErqMQLKc8m_6rl_w5w/zh-cn_image_0000002538181104.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=CC6D2A00039E0A01E6DD40A620CC2BBF324444885351447CF84F7EA16E0638E9)

#### \[h2\]drawImage

drawImage(image: Image | PixelMap, sx: number, sy: number, sWidth: number, sHeight: number, dx: number, dy: number, dWidth: number, dHeight: number):void

进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| image | Image | PixelMap9+ | 是 | 图片资源，请参考[Image对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-image) 或[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)对象。 |
| sx | number | 是 | 
裁切源图像时距离源图像左上角的x坐标值。

单位：vp

 |
| sy | number | 是 | 

裁切源图像时距离源图像左上角的y坐标值。

单位：vp

 |
| sWidth | number | 是 | 

裁切源图像时需要裁切的宽度。

单位：vp

 |
| sHeight | number | 是 | 

裁切源图像时需要裁切的高度。

单位：vp

 |
| dx | number | 是 | 

绘制区域左上角在x轴的位置。

单位：vp

 |
| dy | number | 是 | 

绘制区域左上角在y 轴的位置。

单位：vp

 |
| dWidth | number | 是 | 

绘制区域的宽度。

单位：vp

 |
| dHeight | number | 是 | 

绘制区域的高度。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    var test = this.$refs.canvas;
    var ctx = test.getContext('2d');
    var img = new Image();
    // 'common/image/test.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/test.jpg';
    ctx.drawImage(img, 0, 0, 200, 200, 10, 10, 200, 200);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/RIDvrFVpRtqaAFkH8l2MwA/zh-cn_image_0000002569020891.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=4F9E7C0677AC2BB9F667620217CEA8969470D82A2C79D4F46756FC359D734B35)

#### \[h2\]restore

restore(): void

对保存的绘图上下文进行恢复。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.restore();
  }
}
```

#### \[h2\]save

save(): void

对当前的绘图上下文进行保存。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.save();
  }
}
```

#### \[h2\]createLinearGradient6+

createLinearGradient(x0: number, y0: number, x1: number, y1: number): Object

创建一个线性渐变色，返回CanvasGradient对象，请参考[CanvasGradient对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x0 | number | 是 | 
起点的x轴坐标。

单位：vp

 |
| y0 | number | 是 | 

起点的y轴坐标。

单位：vp

 |
| x1 | number | 是 | 

终点的x轴坐标。

单位：vp

 |
| y1 | number | 是 | 

终点的y轴坐标。

单位：vp

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```js
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Linear gradient: start(50,0) end(300,100)
    var gradient = ctx.createLinearGradient(50,0, 300,100);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Fv4TfLK6RRikoZpooiNkgA/zh-cn_image_0000002568900881.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=C1704774ECD9C0CAA2AAB0056317A74B28644C33622B3111AB11F946748AC930)

#### \[h2\]createRadialGradient6+

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): Object

创建一个径向渐变色，返回CanvasGradient对象，请参考CanvasGradient。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x0 | number | 是 | 
起始圆的x轴坐标。

单位：vp

 |
| y0 | number | 是 | 

起始圆的y轴坐标。

单位：vp

 |
| r0 | number | 是 | 

起始圆的半径。必须是非负且有限的。

单位：vp

 |
| x1 | number | 是 | 

终点圆的x轴坐标。

单位：vp

 |
| y1 | number | 是 | 

终点圆的y轴坐标。

单位：vp

 |
| r1 | number | 是 | 

终点圆的半径。必须为非负且有限的。

单位：vp

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```js
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Radial gradient: inner circle(200,200,r:50) outer circle(200,200,r:200)
    var gradient = ctx.createRadialGradient(200,200,50, 200,200,200);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/PLHXhAygRoaHaVAq_rIlZQ/zh-cn_image_0000002538021180.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=69109AF6263FE10E7D300569A2966797C245549712B9E6E2A77A07F2DF5BA06C)

#### \[h2\]createImageData

createImageData(width: number, height: number): ImageData

创建新的、空白的、指定大小的ImageData对象，请参考[ImageData对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| width | number | 是 | 
ImageData的宽度。

单位：vp

 |
| height | number | 是 | 

ImageData的高度。

单位：vp

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata) | 返回创建的ImageData对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
  }
}
```

#### \[h2\]createImageData

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象，重新创建一个宽、高相同但不会复制图像数据的ImageData对象，请参考[ImageData对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| imageData | [ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata) | 是 | 复制现有的ImageData对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata) | 返回创建的ImageData对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
    var newImageData = ctx.createImageData(imageData);  // Create ImageData using the input imageData
  }
}
```

#### \[h2\]getImageData

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sx | number | 是 | 
需要输出的区域的左上角x坐标。

单位：vp

 |
| sy | number | 是 | 

需要输出的区域的左上角y坐标。

单位：vp

 |
| sw | number | 是 | 

需要输出的区域的宽度。

单位：vp

 |
| sh | number | 是 | 

需要输出的区域的高度。

单位：vp

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata) | 返回包含指定区域像素的ImageData对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="getImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const test = this.$element('getImageData')
    const ctx = test.getContext('2d');
    var imageData = ctx.getImageData(0, 0, 280, 300);
  }
}
```

#### \[h2\]putImageData

putImageData(imageData: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void

使用ImageData数据裁剪后填充至新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| imageData | [ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata) | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 
填充区域在x轴方向的偏移量。

单位：vp

 |
| dy | number | 是 | 

填充区域在y轴方向的偏移量。

单位：vp

 |
| dirtyX | number | 是 | 

源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。

单位：vp

 |
| dirtyY | number | 是 | 

源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。

单位：vp

 |
| dirtyWidth | number | 是 | 

源图像数据矩形裁切范围的宽度。

单位：vp

 |
| dirtyHeight | number | 是 | 

源图像数据矩形裁切范围的高度。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #D5D5D5;"></canvas>
</div>
```

```js
// xxx.js
export default {
    onShow() {
        const test = this.$element('putImageData')
        const ctx = test.getContext('2d');
        var imgData = ctx.createImageData(100, 100);
        for (var i = 0; i < imgData.data.length; i += 4) {
            imgData.data[i + 0] = 39;
            imgData.data[i + 1] = 135;
            imgData.data[i + 2] = 217;
            imgData.data[i + 3] = 255;
        }
        ctx.putImageData(imgData, 10, 10, 0, 0, 100, 50);
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/riQLEeVFSyW1QMfnrZlpsA/zh-cn_image_0000002538181106.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=42C7F13B50CAC76C05950B882D85C211E85F1719A229954023840E5FF7DEB69F)

#### \[h2\]putImageData

putImageData(imageData: ImageData, dx: number, dy: number): void

使用ImageData数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| imageData | [ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata) | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 
填充区域在x轴方向的偏移量。

单位：vp

 |
| dy | number | 是 | 

填充区域在y轴方向的偏移量。

单位：vp

 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const test = this.$element('putImageData')
    const ctx = test.getContext('2d');
    var imgData = ctx.createImageData(100, 100);
    for (var i = 0; i < imgData.data.length; i += 4) {
      imgData.data[i + 0] = 255;
      imgData.data[i + 1] = 0;
      imgData.data[i + 2] = 0;
      imgData.data[i + 3] = 255;
  }
    ctx.putImageData(imgData, 10, 10);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/NflgzHyjSvarh2I3TeMCZA/zh-cn_image_0000002569020893.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=2EDBFB0C33DA6E04E524331B9336FAFE8C650815A49DE5A8BF854DC12DD6AA61)

#### \[h2\]getPixelMap9+

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

获取用当前canvas指定区域内的像素创建的PixelMap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sx | number | 是 | 
指定区域的左上角x坐标。

单位：vp

 |
| sy | number | 是 | 

指定区域的左上角y坐标。

单位：vp

 |
| sw | number | 是 | 

指定区域的宽度。

单位：vp

 |
| sh | number | 是 | 

指定区域的高度。

单位：vp

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 返回包含指定区域像素的PixelMap对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="canvasId" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const test = this.$element('canvasId')
    const ctx = test.getContext('2d');
    var pixelMap = ctx.getPixelMap(0, 0, 280, 300);
  }
}
```

#### \[h2\]setLineDash

setLineDash(segments: Array): void

设置画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| segments | Array | 是 | 作为数组用来描述线段如何交替和间距长度。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10,20]);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/jio3qc7vSvOMcHHDRbgz7g/zh-cn_image_0000002568900883.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=4EEC76BB31A433F1C533EE1002551AC4D7465E86D149CE37FEA4CAED2DBCDEF1)

#### \[h2\]getLineDash

getLineDash(): Array

获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array | 返回数组，该数组用来描述线段如何交替和间距长度。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var info = ctx.getLineDash();
  }
}
```

#### \[h2\]transferFromImageBitmap7+

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的[ImageBitmap对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagebitmap)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bitmap | [ImageBitmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagebitmap) | 是 | 待显示的ImageBitmap对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var canvas = this.$refs.canvas.getContext('2d');
    var offscreen = new OffscreenCanvas(500,500);
    var offscreenCanvasCtx = offscreen.getContext("2d");
    offscreenCanvasCtx.fillRect(0, 0, 200, 200);

    var bitmap = offscreen.transferToImageBitmap();
    canvas.transferFromImageBitmap(bitmap);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/zbXSo3wqQ2aXXqcdTWxmAA/zh-cn_image_0000002538021182.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=086A8DF1C68DC5325E572ECB353D4B727ABDA458DAEFDF076F593E1C25551CD2)
