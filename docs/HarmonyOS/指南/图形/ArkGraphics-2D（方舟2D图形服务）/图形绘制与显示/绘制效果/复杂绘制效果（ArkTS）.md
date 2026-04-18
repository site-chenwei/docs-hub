---
title: "复杂绘制效果（ArkTS）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "绘制效果"
  - "复杂绘制效果（ArkTS）"
captured_at: "2026-04-17T01:36:08.626Z"
---

# 复杂绘制效果（ArkTS）

除了基础填充颜色、描边颜色和一些样式设置的绘制效果外，还支持通过画刷和画笔实现更多复杂的绘制效果。比如：

-   混合模式。
    
-   路径效果，如虚线效果。
    
-   着色器效果，如线性渐变、径向渐变等。
    
-   滤波效果，如模糊效果等。
    

#### 混合模式

混合模式可以用于画笔或画刷，它定义了如何将源像素（要绘制的内容）与目标像素（已存在于画布上的内容）进行组合。

可以使用setBlendMode()接口将混合模式应用于画刷或画笔中，该接口需要接受一个参数BlendMode，即混合模式的类型，具体可参考[BlendMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blendmode)。

关键示例和效果示意图如下所示：

import { DrawContext, FrameNode, NodeController, RenderNode, UIContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

function drawRenderNode(canvas: drawing.Canvas) {
  canvas.saveLayer(null, null);
  const brushCircle = new drawing.Brush();
  const colorCircle: common2D.Color = {alpha: 255, red: 0, green: 0, blue: 255};
  brushCircle.setColor(colorCircle);
  canvas.attachBrush(brushCircle);
  canvas.drawCircle(500, 500, 200);
  const brush = new drawing.Brush();
  //  设置混合模式
  brush.setBlendMode(drawing.BlendMode.SRC\_IN);
  canvas.saveLayer(null, brush);

  const brushRect = new drawing.Brush();
  const colorRect: common2D.Color = {alpha: 255, red: 255, green: 255, blue: 0};
  brushRect.setColor(colorRect);
  canvas.attachBrush(brushRect);
  const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
  canvas.drawRect(rect);
  canvas.restore();
  canvas.restore();
  canvas.detachBrush();
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/CranwxTKTM2P5qFlQLCnSA/zh-cn_image_0000002568899295.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=C1B799BC35F374DFB0B4D07825FE7AB5174B48E0050016DFAC4C83EDAA666785)

#### 路径效果

路径效果如虚线效果，只用于画笔。

可使用createDashPathEffect()接口设置路径效果。接口接受2个参数，分别为：

-   浮点数数组intervals：表示虚线或者点线的间隔。
    
-   浮点数phase：表示在intervals数组中的偏移量，即从数组的哪个位置开始应用虚线或点线效果。
    

此处以绘制矩形虚线路径效果为例，关键示例和效果示意图如下所示：

// 创建画笔
let pen = new drawing.Pen();
// 设置线宽
pen.setStrokeWidth(10.0);
// 设置颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// 表示10px的实线，5px的间隔，2px的实线，5px的间隔，以此循环
let intervals = \[10, 5, 2, 5\];
// 设置虚线路径效果
let effect = drawing.PathEffect.createDashPathEffect(intervals, 0);
pen.setPathEffect(effect);
// 设置画笔描边效果
canvas.attachPen(pen);
// 创建矩形
let rect: common2D.Rect = {
  left: VALUE\_200,
  top: VALUE\_200,
  right: VALUE\_1000,
  bottom: VALUE\_700
};
// 绘制矩形
canvas.drawRect(rect);
// 去除描边效果
canvas.detachPen();

| 原始图 | 设置虚线效果后的效果图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ZpmM0YziQSWRM2jaCWfHgg/zh-cn_image_0000002538019590.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=E782EA3D8E96C8076FD6EA2B3C056D3021B8CE92574A4008DDFA7641E0FB8481) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/138VzHxmRPW8imCpES6YAA/zh-cn_image_0000002538179520.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=D760CA472D9EECA6FB34A58437CE78DC7BD05C3F4D80383650A71D757DD8404E) |

#### 着色器效果

着色器效果基于画刷或画笔实现，可使用setShaderEffect()接口设置画刷或画笔的着色器效果。当前支持不同的着色器效果，如线性渐变着色器效果、径向渐变着色器效果、扇形渐变着色器效果。

着色器相关接口和具体参数的说明请见[ShaderEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadereffect)。

#### \[h2\]线性渐变着色器效果

可使用createLinearGradient()接口创建想要设置的线性渐变着色器效果。接口接受6个参数，分别是开始点、结束点、颜色数组、平铺模式、相对位置数组以及矩阵对象。

-   开始点和结束点用来确定渐变方向。
    
-   颜色数组用于存储渐变使用到的颜色。
    
-   相对位置数组则用于确定每种颜色在渐变中的相对位置，如果相对位置为空，颜色将会被均匀地分布在开始点和结束点之间。
    
-   矩阵对象，用于对着色器做矩阵变换，默认为null，表示单位矩阵。
    
-   平铺模式用于确定如何在渐变区域之外继续渐变效果，平铺模式分为以下4类：
    
    -   CLAMP：当图像超出其原始边界时，复制边缘颜色。
    -   REPEAT：在水平和垂直方向上重复图像。
    -   MIRROR：在水平和垂直方向上重复图像，并在相邻的图像之间交替使用镜像图像。
    -   DECAL：只在原始域内绘制，在其他地方返回透明黑色。

此处以绘制矩形并使用画刷设置线性渐变着色器效果为例，关键示例和效果示意图如下所示：

let startPt: common2D.Point = { x: VALUE\_100, y: VALUE\_100 };
let endPt: common2D.Point = { x: VALUE\_900, y: VALUE\_900 };
let colors = \[0xFFFFFF00, 0xFFFF0000, 0xFF0000FF\];
// 创建线性渐变着色器
let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, colors, drawing.TileMode.CLAMP);
// 创建画刷
let brush = new drawing.Brush();
// 设置线性着色器
brush.setShaderEffect(shaderEffect);
// 设置画刷填充效果
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_100,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// 绘制矩形
canvas.drawRect(rect);
// 去除填充效果
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/A2cW9BQrTRCVqnf2yCx-Zg/zh-cn_image_0000002569019305.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=59960647D7F92CA3CB9C320AC436FED90300E56783142108B106BFBD7D1C0B61)

#### \[h2\]径向渐变着色器效果

可使用createRadialGradient()接口创建想要设置的径向渐变着色器效果。接口接受6个参数，分别是圆心坐标（centerPt）、半径（radius）、颜色数组（colors）、平铺模式（TileMode）、相对位置数组（pos）以及矩阵对象（matrix）。

其实现方式与线性渐变着色器类似，不同的是，径向渐变是由圆心开始向外径向渐变的。

此处以绘制矩形并使用画刷设置径向渐变着色器效果为例，关键示例和效果示意图如下所示：

let centerPt: common2D.Point = { x: VALUE\_500, y: VALUE\_500 };
let colors = \[0xFFFF0000, 0xFF00FF00, 0xFF0000FF\];
// 创建径向渐变着色器
let shaderEffect = drawing.ShaderEffect.createRadialGradient(centerPt, VALUE\_600, colors, drawing.TileMode.CLAMP);
// 创建画刷
let brush = new drawing.Brush();
// 设置径向渐变着色器
brush.setShaderEffect(shaderEffect);
// 设置画刷填充效果
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_100,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// 绘制矩形
canvas.drawRect(rect);
// 去除填充效果
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/r-ml9ry7Q2W9T7i0fOlllQ/zh-cn_image_0000002568899297.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=FE55E8A48EBC5E7A51A7D6EADC3C797EAB834ECFD4268A9EDF566D2776BE692A)

#### \[h2\]扇形渐变着色器效果

可使用createSweepGradient()接口创建想要设置的扇形渐变着色器效果。接口接受7个参数，分别是圆心坐标（centerPt）、颜色数组（colors）、平铺模式（TileMode）、扇形渐变的起始角度（startAngle）、扇形渐变的结束角度（endAngle）、相对位置数组（pos）以及矩阵对象（matrix）。

其实现方式也与线性渐变着色器类似，不同的是，扇形渐变是在围绕中心点旋转的过程中渐变。

此处以绘制矩形并使用画刷设置扇形渐变着色器效果为例，关键示例和效果示意图如下所示：

let centerPt: common2D.Point = { x: VALUE\_500, y: VALUE\_500 };
let colors = \[0xFF00FFFF, 0xFFFF00FF, 0xFFFFFF00\];
// 创建扇形渐变着色器
let shaderEffect = drawing.ShaderEffect.createSweepGradient(centerPt, colors, drawing.TileMode.CLAMP, 0, 360);
// 创建画刷
let brush = new drawing.Brush();
// 设置扇形渐变着色器
brush.setShaderEffect(shaderEffect);
// 设置画刷填充效果
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_100,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// 绘制矩形
canvas.drawRect(rect);
// 去除填充效果
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/SkvdR8RBTNyxZfYUuz0BoQ/zh-cn_image_0000002538019592.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=8C8081ED2D43EA3D1D8E630FA112448AF3F22E726D5E901336BD4DDB0B645A3B)

#### 滤波器效果

滤波器效果可基于画刷或画笔实现。当前支持不同的滤波器效果，比如图像滤波器、颜色滤波器、蒙版滤波器。

滤波器相关接口和具体参数的说明请见[ImageFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-imagefilter)。

#### \[h2\]颜色滤波器效果

颜色滤波器可基于画笔或画刷实现，颜色滤波器的相关接口和具体参数的说明请见[ColorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-colorfilter)。

目前可实现多种颜色滤波器，包括如下：

-   具有混合模式的颜色滤波器。
    
-   具有5x4颜色矩阵的颜色滤波器。
    
-   将SRGB的伽玛曲线应用到RGB颜色通道的颜色滤波器。
    
-   将RGB颜色通道应用于SRGB的伽玛曲线的颜色滤波器。
    
-   将其输入的亮度值乘以透明度通道， 并将红色、绿色和蓝色通道设置为零的颜色滤波器。
    
-   由两个颜色滤波器组合而成的颜色滤波器。
    

此处以具有5x4颜色矩阵的颜色滤波器为例。

可使用createMatrixColorFilter()接口创建具有5x4颜色矩阵的颜色滤波器。接口接受1个参数，表示为颜色矩阵，它是一个长度为20的浮点数数组。数组格式如下：

\[ a0, a1, a2, a3, a4 \]

\[ b0, b1, b2, b3, b4 \]

\[ c0, c1, c2, c3, c4 \]

\[ d0, d1, d2, d3, d4 \]

对于每个原始的像素颜色色值（R, G, B, A），变换后的色值（R', G', B', A'）计算公式为：

R' = a0\*R + a1\*G + a2\*B + a3\*A + a4

G' = b0\*R + b1\*G + b2\*B + b3\*A + b4

B' = c0\*R + c1\*G + c2\*B + c3\*A + c4

A' = d0\*R + d1\*G + d2\*B + d3\*A + d4

此处以绘制矩形并使用画刷设置具有5x4颜色矩阵的颜色滤波器效果为例，关键示例和效果示意图如下所示：

// 创建画刷
let brush = new drawing.Brush();
// 设置颜色
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// 设置颜色矩阵
let matrix: number\[\] = \[
  1, 0, 0, 0, 0,
  0, 1, 0, 0, 0,
  0, 0, 0.5, 0.5, 0,
  0, 0, 0.5, 0.5, 0
\];
// 创建5x4颜色矩阵的颜色滤波器
let filter = drawing.ColorFilter.createMatrixColorFilter(matrix);
// 设置颜色滤波器
brush.setColorFilter(filter);
// 设置画刷填充效果
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_300,
  top: VALUE\_300,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// 绘制矩形
canvas.drawRect(rect);
// 去除填充效果
canvas.detachBrush();

| 原始图 | 设置5x4颜色矩阵的颜色滤波器后的效果图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/O79qO9gaRAeSpWrXllSqaw/zh-cn_image_0000002538179522.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=FDB15FBAA224C78398E40010F6FA6AA0EFAE2593FB0F0EDFC625E49D91F3C35D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ev9TnWe8RGW4LkioHiehrQ/zh-cn_image_0000002569019307.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=4A9469F575FBE0931FAC1BEB57456059CAE71934CB2F3AF21C6925CB1AEC2F7E) |

#### \[h2\]图像滤波器效果

图像滤波器可基于画笔或画刷来实现，图像滤波器的相关接口和具体参数的说明请见[ImageFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-imagefilter)。

目前只支持两种图像滤波器：

-   基于颜色滤波器的图像滤波器。
    
    可通过createFromColorFilter()接口实现，接口接受2个参数，颜色滤波器colorFilter和图像滤波器imageFilter，即把颜色滤波器的效果叠加到图像滤波器imageFilter上，imageFilter可为空，imageFilter为空则只添加颜色滤波器效果。
    
-   具有模糊效果的图像滤波器。
    
    可通过createBlurImageFilter()接口实现，接口接受4个参数，sigmaX，sigmaY，cTileMode和imageFilter。sigmaX和sigmaY是模糊的标准差，cTileMode是平铺模式，imageFilter是输入的图像滤波器。
    
    最终效果即为在输入的图像滤波器imageFilter的基础上进行模糊化处理，即滤波器效果可叠加，imageFilter可为空，imageFilter为空则只添加模糊效果。
    

此处以绘制矩形并使用画笔添加模糊效果的图像滤波器效果为例，关键示例和效果示意图如下所示：

// 设置画笔
let pen = new drawing.Pen();
// 设置线宽
pen.setStrokeWidth(10.0);
// 设置颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// 创建模糊效果图像滤波器
let filter = drawing.ImageFilter.createBlurImageFilter(20, 20, drawing.TileMode.CLAMP);
// 设置图像滤波器
pen.setImageFilter(filter);
// 设置画笔描边效果
canvas.attachPen(pen);
let rect: common2D.Rect = {
  left: VALUE\_300,
  top: VALUE\_300,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// 绘制矩形
canvas.drawRect(rect);
// 去除描边效果
canvas.detachPen();

| 原始图 | 设置模糊效果后的效果图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Y9-IFdBWQsyKm97rNY6pkQ/zh-cn_image_0000002568899299.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=33352B731E6E34DF4FCDE2B49BE98FC59E4B5FB2ABF62384515D8ACEB72C9382) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/8QkreG1CTd-dvU7c1Clmpw/zh-cn_image_0000002538019594.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=4263A4F43028974796FCC2690649ED9BE597D3B60D4404EFA9ACAD2AED272FC0) |

#### \[h2\]蒙版滤波器效果

蒙版滤波器的模糊效果仅对透明度和形状边缘进行模糊处理，相对于图像滤波器的模糊效果来说计算成本更低。

蒙版滤波器可基于画笔或画刷实现，蒙版滤波器的相关接口和具体参数的说明请见[MaskFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-maskfilter)。

可使用createBlurMaskFilter()接口创建想要设置具有模糊效果的蒙版滤波器。接口接受2个参数，分别为：

-   blurType：用于指定要应用的模糊类型，详细分类请参考[BlurType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blurtype12)。
    
-   sigma：用于指定要应用的高斯模糊的标准差，标准差必须大于0。
    

此处以绘制矩形并使用画笔设置蒙版滤波器效果为例，关键示例和效果示意图如下所示：

// 创建画笔
let pen = new drawing.Pen();
// 设置线宽
pen.setStrokeWidth(10.0);
// 设置颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// 创建模糊效果的蒙版滤波器
let filter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.NORMAL, 20);
// 设置模糊效果
pen.setMaskFilter(filter);
// 设置画笔描边效果
canvas.attachPen(pen);
let rect: common2D.Rect = {
  left: VALUE\_300,
  top: VALUE\_300,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// 绘制矩形
canvas.drawRect(rect);
// 去除描边效果
canvas.detachPen();

| 原始图 | 设置模糊效果后的效果图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ux__7W73T9KKhw_YaZe6Qg/zh-cn_image_0000002568899299.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=676DFA5C0B9F04D2F305612C83785F53768F66BE1912E3736B12339FE1B39523) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/VZ8d_6BdSdmrUFV9njIu8Q/zh-cn_image_0000002538019594.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=BD569A987A77FD9B477C255C7F7B80A4F3CA29B4456E64A13AE21BE98D8EAC88) |

#### 示例代码

-   [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
