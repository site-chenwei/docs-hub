---
title: "CanvasRenderingContext2D对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Lite）"
  - "画布组件"
  - "CanvasRenderingContext2D对象"
captured_at: "2026-04-17T01:48:06.671Z"
---

# CanvasRenderingContext2D对象

使用CanvasRenderingContext2D在canvas画布组件上进行绘制，绘制对象可以是矩形、文本。

**示例：**

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
    <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```javascript
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/61Wxwqm_TTGr3QRPvWp9og/zh-cn_image_0000002538021366.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=EBD998077DB3B0DCE0E8710A8216718E4CC286C1CFE796C846A549DBE3B860E0)

#### fillRect()

填充一个矩形。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| x | number | 指定矩形左上角点的x坐标。 |
| y | number | 指定矩形左上角点的y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/IE75HHvPRv2LVkkQ4OW3zg/zh-cn_image_0000002538181292.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=A0AC21BC3B5C692E85521ABD638BB10FF9DCE43A86A6F7024E458D270AE0E6C2)

```javascript
ctx.fillRect(20, 20, 200, 150);
```

#### fillStyle

指定绘制的填充色。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| color | <color> | 设置填充区域的颜色。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/ssVlLT7hS6C_LfKBv3_2bQ/zh-cn_image_0000002569021079.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=6969112F7555A57A7E5A37FB27E6B257109D13F2DB594116E117E29FB6E73293)

```javascript
ctx.fillStyle = '#0000ff';
ctx.fillRect(20, 20, 150, 100);
```

#### strokeRect()

绘制具有边框的矩形，矩形内部不填充。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| x | number | 指定矩形的左上角x坐标。 |
| y | number | 指定矩形的左上角y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/llAr60luTIOp2uNqkkfUhw/zh-cn_image_0000002568901069.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=7B0D9CD194DA9E744B4F64475C986A0498BECF5272285FF10447C403536A09BC)

```javascript
ctx.strokeRect(30, 30, 200, 150);
```

#### fillText()

绘制填充类文本。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| text | string | 需要绘制的文本内容。 |
| x | number | 需要绘制的文本的左下角x坐标。 |
| y | number | 需要绘制的文本的左下角y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/5p_boq0LQ1mCxWsqEX_Kcg/zh-cn_image_0000002538021368.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=1C8A0D41FE47D8E464524A7A16FFCE4A8F7695AA6738891D7388781655362752)

```javascript
ctx.font = '35px sans-serif';
ctx.fillText("Hello World!", 20, 60);
```

#### lineWidth

指定绘制线条的宽度值。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| lineWidth | number | 设置绘制线条的宽度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/G3ebE6xMRL-EQkJcUQh_tw/zh-cn_image_0000002538181294.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=4A81CAE4868BE9E5A0223F6C37BDC34BCFCD0F12F9EA8D9D2D0633765F54EA3E)

```javascript
ctx.lineWidth = 5;
ctx.strokeRect(25, 25, 85, 105);
```

#### strokeStyle

设置描边的颜色。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| color | <color> | 指定描边使用的颜色 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/41CZxXFPRi20aR09Jpq9wg/zh-cn_image_0000002569021081.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=8E525BCE4797F6E0BBE6EC2D78BDEFE16E222541A31D11F5E654A14ED38BBBA0)

```javascript
ctx.lineWidth = 10;
ctx.strokeStyle = '#0000ff';
ctx.strokeRect(25, 25, 155, 105);
```

#### \[h2\]stroke()5+

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/6Lcv5qrEREaIQ3ubtZ5fKQ/zh-cn_image_0000002568901071.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=DCB06EC201FB770B731EF11BEEDE29EF4F3EFF0E9C5CA1311FB9AECAC08DB819)

```javascript
ctx.moveTo(25, 25);
ctx.lineTo(25, 105);
ctx.strokeStyle = 'rgb(0,0,255)';
ctx.stroke();
```

#### \[h2\]beginPath()5+

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/SStS9RTwRAS6PX0sONlFlQ/zh-cn_image_0000002538021370.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=CE293330BFE42E7D4775CC688C97C55F37461D26451CD58BC0B2225CD7CFD9DA)

```javascript
ctx.beginPath();
ctx.lineWidth = 6;
ctx.strokeStyle = '#0000ff';
ctx.moveTo(15, 80);
ctx.lineTo(280, 80);
ctx.stroke();
```

#### \[h2\]moveTo()5+

路径从当前点移动到指定点。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/OsEppFI8SMmMUAvqRFNumA/zh-cn_image_0000002538181296.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=782EBBB01DC96B53E9077663CE32B504FEAD21CA9F8FC3BA9DB721BE7A9AD519)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

#### \[h2\]lineTo()5+

从当前点到指定点进行路径连接。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/IozWAlbWSSaJ4TMMqYp7dg/zh-cn_image_0000002569021083.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=3BE1AEF680F89B946D54ED9C4703A35AEDFC3BA27A50339D6FF1A45181CCCC5C)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

#### \[h2\]closePath()5+

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/hLmJimVpTBeCzOsOHuCgSA/zh-cn_image_0000002568901073.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=FE3A61E4E7BFFA82AD29A4D2CB772DA4BFCCFAC0A0E6C3B90470DE05F3ABA900)

```javascript
ctx.beginPath();
ctx.moveTo(30, 30);
ctx.lineTo(110, 30);
ctx.lineTo(70, 90);
ctx.closePath();
ctx.stroke();
```

#### font

设置文本绘制中的字体样式。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| value | string | 字体样式支持：sans-serif, serif, monospace，该属性默认值为30px HYQiHei-65S。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/zcYniV0sQjiWWpyO75wxEg/zh-cn_image_0000002538021372.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=8538FAE9B6BB943A3B1A6A26E75A5DDAA6D6CC4AA2305101A3F088FEF92EEFDB)

```javascript
ctx.font = '30px sans-serif';
ctx.fillText("Hello World", 20, 60);
```

#### textAlign

设置文本绘制中的文本对齐方式。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| align | string | 
可选值为：

\- left（默认）：文本左对齐；

\- right：文本右对齐；

\- center：文本居中对齐；

 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/uZ1YcctOQ9mnXpV-aur_qw/zh-cn_image_0000002538181298.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=7176F1C88B8E97A1107C8FCB3ECE3D387E097DBB802DA00D1F11773E334D51D7)

```javascript
ctx.strokeStyle = '#0000ff';
ctx.moveTo(140, 10);
ctx.lineTo(140, 160);
ctx.stroke();

ctx.font = '18px sans-serif';

// Show the different textAlign values
ctx.textAlign = 'left';
ctx.fillText('textAlign=left', 140, 100);
ctx.textAlign = 'center';
ctx.fillText('textAlign=center',140, 120);
ctx.textAlign = 'right';
ctx.fillText('textAlign=right',140, 140);
```

#### arc()5+

绘制弧线路径。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 弧线圆心的x坐标值，单位：vp。 |
| y | number | 是 | 弧线圆心的y坐标值，单位：vp。 |
| radius | number | 是 | 弧线的圆半径，单位：vp。 |
| startAngle | number | 是 | 弧线的起始弧度，单位：弧度。 |
| endAngle | number | 是 | 弧线的终止弧度，单位：弧度。 |
| anticlockwise | boolean | 否 | 
是否逆时针绘制圆弧。

true：逆时针方向绘制弧线。

false：顺时针方向绘制弧线。

默认值：false。

 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/mlR60lCbRbKInut2t2UugA/zh-cn_image_0000002569021085.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=66A69FDE89E186FF98841783C92F18093919CBBBFE171F16AD87F8FD70D8A7BB)

```javascript
ctx.beginPath();
ctx.arc(100, 75, 50, 0, 6.28);
ctx.stroke();
```

#### \[h2\]rect()5+

创建矩形路径。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 指定矩形的左上角x坐标值，单位：vp。 |
| y | number | 是 | 指定矩形的左上角y坐标值，单位：vp。 |
| width | number | 是 | 指定矩形的宽度，单位：vp。 |
| height | number | 是 | 指定矩形的高度，单位：vp。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/MtStwY9cQBul_xjtVvrDAQ/zh-cn_image_0000002568901075.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=35FA0DDD77896624BBC32643D0C8DD36DDD4F71E1BE296192983A9A770BAA720)

```javascript
ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
ctx.stroke(); // Draw it
```
