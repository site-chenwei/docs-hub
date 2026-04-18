---
title: "复杂绘制效果（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "绘制效果"
  - "复杂绘制效果（C/C++）"
captured_at: "2026-04-17T01:36:08.632Z"
---

# 复杂绘制效果（C/C++）

除了基础填充颜色、描边颜色和一些样式设置的绘制效果外，还支持通过画刷和画笔实现更多复杂的绘制效果。比如：

-   混合模式。
    
-   路径效果，如虚线效果。
    
-   着色器效果，如线性渐变、径向渐变等。
    
-   滤波效果，如模糊效果等。
    

#### 混合模式

混合模式可以用于画笔或画刷，它定义了如何将源像素（要绘制的内容）与目标像素（已存在于画布上的内容）进行组合。

可以使用OH\_Drawing\_BrushSetBlendMode()接口将混合模式应用于画刷中，使用OH\_Drawing\_PenSetBlendMode()接口将混合模式应用于画笔中。这两个接口都需要接受一个参数OH\_Drawing\_BlendMode，即混合模式的类型，具体可参考[OH\_Drawing\_BlendMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h#oh_drawing_blendmode)。

此处以使用画刷设置叠加混合模式为例（为了防止混合模式的效果被背景色干扰，示例中的canvas并未设置背景色，使用的是默认的黑色背景），关键示例和效果示意图如下所示：

// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 设置目标像素颜色
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 将目标像素的画刷效果设置到Canvas中
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建矩形对象
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value600\_, value600\_);
// 绘制矩形（目标像素）
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 设置源像素颜色
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MIN, RGBA\_MIN, 0xFF));
// 设置混合模式为叠加模式
OH\_Drawing\_BrushSetBlendMode(brush, OH\_Drawing\_BlendMode::BLEND\_MODE\_PLUS);
// 将源像素的画刷效果设置到Canvas中
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建圆心的点对象
OH\_Drawing\_Point \*point = OH\_Drawing\_PointCreate(value600\_, value600\_);
// 绘制圆（源像素）
OH\_Drawing\_CanvasDrawCircle(canvas, point, value300\_);
// 去除掉画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_PointDestroy(point);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/nXn8y9dbQpmNd0X7WEaD5A/zh-cn_image_0000002538019596.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=2EA4C7986584E3095B7DDA6255A11349B8A8E6FD8897E67CA4C9E1E9EF961B5B)

#### 路径效果

路径效果如虚线效果，只用于画笔。

可使用OH\_Drawing\_CreateDashPathEffect()接口设置路径效果。接口接受3个参数，分别为：

-   浮点数数组intervals：表示虚线或者点线的间隔。
    
-   整数count：表示intervals数组中的元素数量。
    
-   浮点数phase：表示在intervals数组中的偏移量，即从数组的哪个位置开始应用虚线或点线效果。
    

此处以绘制矩形虚线路径效果为例，关键示例和效果示意图如下所示：

// 创建画笔
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, 0xffff0000);
// 设置画笔线宽为10
OH\_Drawing\_PenSetWidth(pen, 10);
// 表示10px的实线，5px的间隔，2px的实线，5px的间隔，以此循环
float intervals\[\] = {10, 5, 2, 5};
// 设置虚线路径效果
OH\_Drawing\_PathEffect \*pathEffect = OH\_Drawing\_CreateDashPathEffect(intervals, 4, 0.0);
OH\_Drawing\_PenSetPathEffect(pen, pathEffect);
// 在画布上设置画笔，请确保已获取得到画布对象
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建矩形
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除掉画布中的画笔
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁各类对象
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_PathEffectDestroy(pathEffect);

| 不设置虚线路径效果的示意图 | 设置虚线效果的示意图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Cd2n11fKQeCFjzGIJvl76g/zh-cn_image_0000002538179526.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=2F887CC0458F2952A21C27274CEEFA6827453E0BA8E947A5023BFA44C7C82880) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/93kRT4dQQdmPWlHedzhVHA/zh-cn_image_0000002569019311.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=D8119A33187D53BBAB9B47A71E393C58C73CFC6BE85B70A8707B55E1CEE6F6FD) |

#### 着色器效果

着色器效果基于画刷或画笔实现，可使用OH\_Drawing\_BrushSetShaderEffect()接口设置画刷的着色器效果，或者使用 OH\_Drawing\_PenSetShaderEffect()接口设置画笔的着色器效果。当前支持不同的着色器效果，如线性渐变着色器效果、径向渐变着色器效果、扇形渐变着色器效果。

着色器相关接口和具体参数的说明请见[drawing\_shader\_effect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-shader-effect-h)。

#### \[h2\]线性渐变着色器效果

可使用OH\_Drawing\_ShaderEffectCreateLinearGradient()接口创建想要设置的线性渐变着色器效果。接口接受6个参数，分别为开始点、结束点、颜色数组、相对位置数组、颜色数组的大小以及平铺模式。

-   开始点和结束点用来确定渐变方向。
    
-   颜色数组用于存储渐变使用到的颜色。
    
-   相对位置数组则用于确定每种颜色在渐变中的相对位置，如果相对位置为空，颜色将会被均匀地分布在开始点和结束点之间。
    
-   平铺模式用于确定如何在渐变区域之外继续渐变效果，平铺模式分为以下4类：
    
    -   CLAMP：当图像超出其原始边界时，复制边缘颜色。
    -   REPEAT：在水平和垂直方向上重复图像。
    -   MIRROR：在水平和垂直方向上重复图像，并在相邻的图像之间交替使用镜像图像。
    -   DECAL：只在原始域内绘制，在其他地方返回透明黑色。

此处以绘制矩形并使用画刷设置线性渐变着色器效果为例，关键示例和效果示意图如下所示：

// 开始点
OH\_Drawing\_Point \*startPt = OH\_Drawing\_PointCreate(20, 20);
// 结束点
OH\_Drawing\_Point \*endPt = OH\_Drawing\_PointCreate(value900\_, value900\_);
// 颜色数组
uint32\_t colors\[\] = {0xFFFFFF00, 0xFFFF0000, 0xFF0000FF};
// 相对位置数组
float pos\[\] = {0.0f, 0.5f, 1.0f};
// 创建线性渐变着色器效果
OH\_Drawing\_ShaderEffect \*colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateLinearGradient(startPt, endPt, colors, pos, 3, OH\_Drawing\_TileMode::CLAMP);
// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 基于画刷设置着色器效果
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// 在画布上设置画刷，请确保已获取得到画布对象
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value900\_);
 // 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除掉画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_PointDestroy(startPt);
OH\_Drawing\_PointDestroy(endPt);

此例绘制的具有线性渐变着色器效果的矩形如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/O0f-FuN8Qeu9i-Zharo5KQ/zh-cn_image_0000002568899303.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=031F6A9FF4DE0AC4C1C1CCFAE4AF05775F1670A6E98BBBB1113FCF8FFC3452E5)

#### \[h2\]径向渐变着色器效果

可使用OH\_Drawing\_ShaderEffectCreateRadialGradient()接口创建想要设置的径向渐变着色器效果。接口接受6个参数，分别为圆心坐标（centerPt）、半径（radius）、颜色数组（colors）、相对位置数组（pos）、颜色和位置的数量（size）以及平铺模式（OH\_Drawing\_TileMode）。

其实现方式与线性渐变着色器类似，不同的是，径向渐变是由圆心开始向外径向渐变的。

此处以绘制矩形并使用画刷设置径向渐变着色器效果为例，关键示例和效果示意图如下所示：

// 圆心坐标
OH\_Drawing\_Point \*centerPt = OH\_Drawing\_PointCreate(value500\_, value500\_);
// 半径
float radius = value600\_;
// 颜色数组
uint32\_t gColors\[\] = {0xFFFF0000, 0xFF00FF00, 0xFF0000FF};
// 相对位置数组
float\_t gPos\[\] = {0.0f, 0.25f, 0.75f};
// 创建径向渐变着色器效果
OH\_Drawing\_ShaderEffect \*colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateRadialGradient(centerPt, radius, gColors, gPos, 3, OH\_Drawing\_TileMode::REPEAT);
// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 基于画刷设置着色器效果
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// 在画布上设置画刷，请确保已获取得到画布对象
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value900\_);
 // 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除掉画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_PointDestroy(centerPt);

此例绘制的具有径向渐变着色器效果的矩形如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/pRCIAQjZSGCfkgSKhcVwhw/zh-cn_image_0000002538019598.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=E455D5DF9A1FD5F0D3CF6610F7E137B9C02C193F94767AB851437663B9895C80)

#### \[h2\]扇形渐变着色器效果

可使用OH\_Drawing\_ShaderEffectCreateSweepGradient()接口创建想要设置的扇形渐变着色器效果。接口接受5个参数，分别是中心点、颜色数组、相对位置数组、颜色和相对位置的数量以及平铺模式。

其实现方式也与线性渐变着色器类似，不同的是，扇形渐变是在围绕中心点旋转的过程中渐变。

此处以绘制矩形并使用画刷设置扇形渐变着色器效果为例，关键示例和效果示意图如下所示：

// 中心点
OH\_Drawing\_Point \*centerPt = OH\_Drawing\_PointCreate(value500\_, value500\_);
// 颜色数组
uint32\_t colors\[3\] = {0xFF00FFFF, 0xFFFF00FF, 0xFFFFFF00};
// 相对位置数组
float pos\[3\] = {0.0f, 0.5f, 1.0f};
// 创建扇形渐变着色器效果
OH\_Drawing\_ShaderEffect\* colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateSweepGradient(centerPt, colors, pos, 3, OH\_Drawing\_TileMode::CLAMP);
// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 基于画刷设置着色器效果
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// 在画布上设置画刷，请确保已获取得到画布对象
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value900\_);
 // 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除掉画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_PointDestroy(centerPt);

此例绘制的具有扇形渐变着色器效果的矩形如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/8HU_GjmLSA6qaXJQkSz5GA/zh-cn_image_0000002538179528.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=1D7E4A9167A4F5D0C81B0A6FC839A743368302180E4F0ACA6B5AD9C5B1F32994)

#### 滤波器效果

滤波器效果可基于画刷或画笔实现。可使用OH\_Drawing\_PenSetFilter()接口设置画笔的滤波器效果，或者使用OH\_Drawing\_BrushSetFilter()接口设置画刷的滤波器效果。当前支持不同的滤波器效果，比如图像滤波器、颜色滤波器、蒙版滤波器。

滤波器相关接口和具体参数的说明请见[drawing\_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-filter-h)。

#### \[h2\]颜色滤波器效果

颜色滤波器可基于画笔或画刷实现，颜色滤波器的相关接口和具体参数的说明请见[drawing\_color\_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-filter-h)。

目前可实现多种颜色滤波器，包括如下：

-   具有混合模式的颜色滤波器。
    
-   具有5x4颜色矩阵的颜色滤波器。
    
-   将SRGB的伽玛曲线应用到RGB颜色通道的颜色滤波器。
    
-   将RGB颜色通道应用于SRGB的伽玛曲线的颜色滤波器。
    
-   将其输入的亮度值乘以透明度通道， 并将红色、绿色和蓝色通道设置为零的颜色滤波器。
    
-   由两个颜色滤波器组合而成的颜色滤波器。
    

此处以具有5x4颜色矩阵的颜色滤波器为例。

可使用OH\_Drawing\_ColorFilterCreateMatrix()接口创建具有5x4颜色矩阵的颜色滤波器。接口接受1个参数，表示为颜色矩阵，它是一个长度为20的浮点数数组。数组格式如下：

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
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// 设置画刷抗锯齿
OH\_Drawing\_BrushSetAntiAlias(brush, true);
// 设置画刷填充颜色
OH\_Drawing\_BrushSetColor(brush, 0xffff0000);
// 设置颜色矩阵
const float matrix\[20\] = {
    1, 0, 0, 0, 0,
    0, 1, 0, 0, 0,
    0, 0, 0.5f, 0.5f, 0,
    0, 0, 0.5f, 0.5f, 0
};
    
// 创建滤波器颜色
OH\_Drawing\_ColorFilter\* colorFilter = OH\_Drawing\_ColorFilterCreateMatrix(matrix);
// 创建一个滤波器对象
OH\_Drawing\_Filter \*filter = OH\_Drawing\_FilterCreate();
// 为滤波器对象设置颜色滤波器
OH\_Drawing\_FilterSetColorFilter(filter, colorFilter);
// 设置画刷的滤波器效果
OH\_Drawing\_BrushSetFilter(brush, filter);
// 在画布上设置画刷，请确保已获取得到画布对象
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建矩形
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除掉画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_ColorFilterDestroy(colorFilter);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_FilterDestroy(filter);

| 不设置颜色滤波器效果的示意图 | 设置5x4颜色矩阵的颜色滤波器效果的示意图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/5OsM7gSFRIKmhJtl7bZ6aA/zh-cn_image_0000002569019313.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=479F4E57D18768786F283026C57EB843A3FEA738EF3AB08CD7E8DA3AF1423E9E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/pQ1gfdCbTWSgwwOXPbbUpA/zh-cn_image_0000002568899305.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=6602BDA79ACF1F72A0C08A559124FE607898FA5C34D76A658D23CA62C23F5817) |

#### \[h2\]图像滤波器效果

图像滤波器可基于画笔或画刷来实现，图像滤波器的相关接口和具体参数的说明请见[drawing\_image\_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-image-filter-h)。

目前只支持两种图像滤波器：

-   基于颜色滤波器的图像滤波器。
    
    可通过OH\_Drawing\_ImageFilterCreateFromColorFilter()接口实现，接口接受2个参数，颜色滤波器colorFilter和图像滤波器input，即把颜色滤波器的效果叠加到图像滤波器input上，input可为空，input为空则只添加颜色滤波器效果。
    
-   具有模糊效果的图像滤波器。
    
    可通过OH\_Drawing\_ImageFilterCreateBlur()接口实现，接口接受4个参数，分别为X轴上的模糊标准差、Y轴上的模糊标准差、平铺模式和图像滤波器（input）。
    
    最终效果即为在输入的图像滤波器（input）的基础上进行模糊化处理，即滤波器效果可叠加，input可为空，input为空则只添加模糊效果。
    

此处以绘制矩形并使用画笔添加模糊效果的图像滤波器效果为例，关键示例和效果示意图如下所示：

// 创建画笔
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// 设置画笔抗锯齿
OH\_Drawing\_PenSetAntiAlias(pen, true);
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, 0xffff0000);
// 设置画笔线宽为20
OH\_Drawing\_PenSetWidth(pen, 20);
// 创建图像滤波器实现模糊效果
OH\_Drawing\_ImageFilter \*imageFilter =
    OH\_Drawing\_ImageFilterCreateBlur(20.0f, 20.0f, OH\_Drawing\_TileMode::CLAMP, nullptr);
// 创建一个滤波器对象
OH\_Drawing\_Filter \*filter = OH\_Drawing\_FilterCreate();
// 为滤波器对象设置图像滤波器
OH\_Drawing\_FilterSetImageFilter(filter, imageFilter);
// 设置画笔的滤波器效果
OH\_Drawing\_PenSetFilter(pen, filter);
// 在画布上设置画笔，请确保已获取得到画布对象
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建矩形
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除掉画布中的画笔
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁各类对象
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_ImageFilterDestroy(imageFilter);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_FilterDestroy(filter);

| 不设置图像滤波器效果的示意图 | 设置图像滤波器效果的示意图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/t0XvfhMQTm-WB5kfiH5DEg/zh-cn_image_0000002538019600.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=DBCC601C08F3435D894A3526F06D8C8D281FE6669F27EA3C78B259E9F1D3DD9A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/zTk3LOuTQziaF-3zCzi3xA/zh-cn_image_0000002538179530.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=F5ADC31987656D9E991D2639D4721C19CFE8FAE87D312F43219CF8DD10F9E76C) |

#### \[h2\]蒙版滤波器效果

蒙版滤波器的模糊效果仅对透明度和形状边缘进行模糊处理，相对于图像滤波器的模糊效果来说计算成本更低。

蒙版滤波器可基于画笔或画刷实现，蒙版滤波器的相关接口和具体参数的说明请见[drawing\_mask\_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-mask-filter-h)。

可使用OH\_Drawing\_MaskFilterCreateBlur()接口创建想要设置具有模糊效果的蒙版滤波器。接口接受3个参数，分别为：

-   blurType：用于指定要应用的模糊类型，详细分类请参考[OH\_Drawing\_BlurType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-mask-filter-h#oh_drawing_blurtype)。
    
-   sigma：用于指定要应用的高斯模糊的标准差，标准差必须大于0。
    
-   respectCTM：指定模糊的标准差是否会被CTM（coordinate transformation matrix，坐标变换矩阵）修改，默认为true，表示会被对应修改。
    

此处以绘制矩形并使用画笔设置蒙版滤波器效果为例，关键示例和效果示意图如下所示：

// 创建画笔
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// 设置画笔抗锯齿
OH\_Drawing\_PenSetAntiAlias(pen, true);
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, 0xffff0000);
// 设置画笔线宽为20
OH\_Drawing\_PenSetWidth(pen, 20);
// 创建蒙版滤波器
OH\_Drawing\_MaskFilter \*maskFilter = OH\_Drawing\_MaskFilterCreateBlur(OH\_Drawing\_BlurType::NORMAL, 20, true);
// 创建一个滤波器对象
OH\_Drawing\_Filter \*filter = OH\_Drawing\_FilterCreate();
// 为滤波器对象设置蒙版滤波器
OH\_Drawing\_FilterSetMaskFilter(filter, maskFilter);
// 设置画笔的滤波器效果
OH\_Drawing\_PenSetFilter(pen, filter);
// 在画布上设置画笔，请确保已获取得到画布对象
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建矩形
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除掉画布中的画笔
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁各类对象
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_MaskFilterDestroy(maskFilter);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_FilterDestroy(filter);

| 不设置蒙版滤波器效果的示意图 | 设置蒙版滤波器效果的示意图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/qDEu91F1Q9uL_46NX8u86Q/zh-cn_image_0000002569019315.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=E6EA78B2839F09DDA05A704ECC5D38C94023FC246A9C51218E07571F6DF4B29B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-fKWa2dRTe6xWlk8bSFMBA/zh-cn_image_0000002568899307.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=FCCB5033DC42C5135FEDD76EE7E1A7E6FFC15FD7FF14D491C8AAE02EC0D69CA5) |

#### 示例代码

-   [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
