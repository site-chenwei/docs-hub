---
title: "几何形状绘制（ArkTS）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/geometric-shape-drawing-arkts"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "图元绘制"
  - "几何形状绘制（ArkTS）"
captured_at: "2026-04-17T01:36:08.657Z"
---

# 几何形状绘制（ArkTS）

#### 场景介绍

当前支持绘制的几何形状，主要包括以下几种：

-   点
    
-   圆弧
    
-   圆
    
-   路径
    
-   区域
    
-   矩形
    
-   圆角矩形
    

大部分的几何形状均可以选择使用画笔或使用画刷来实现绘制，其中点的绘制只能使用画笔。

#### 接口说明

几何形状绘制的常用接口如下表所示，详细的使用和参数说明请见[drawing.Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas)。

| 接口 | 描述 |
| :-- | :-- |
| drawPoint(x: number, y: number): void | 用于画一个点。 |
| drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void | 用于画一个弧。 |
| drawCircle(x: number, y: number, radius: number): void | 用于画一个圆形。 |
| drawPath(path: Path): void | 用于画一个自定义路径。 |
| drawRegion(region: Region): void | 用于画一块区域。 |
| drawRect(left: number, top: number, right: number, bottom: number): void | 用于画一个矩形。 |
| drawRoundRect(roundRect: RoundRect): void | 用于画一个圆角矩形。 |

#### 绘制点

点只能基于画笔在画布上进行绘制，通过使用drawPoint()接口绘制点。绘制点需要接受两个参数，分别为需要绘制的点的x坐标和y坐标。

简单示例如下：

// 设置画笔
let pen = new drawing.Pen();
// 设置颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// 设置线宽
pen.setStrokeWidth(40);
// 设置画笔描边效果
canvas.attachPen(pen);
// 绘制5个点
canvas.drawPoint(VALUE\_200, VALUE\_200);
canvas.drawPoint(VALUE\_400, VALUE\_400);
canvas.drawPoint(VALUE\_600, VALUE\_600);
canvas.drawPoint(VALUE\_800, VALUE\_800);
canvas.drawPoint(VALUE\_1000, VALUE\_1000);
// 去除描边效果
canvas.detachPen();

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/qOp-XViSSXulIqA8P31KnA/zh-cn_image_0000002538019602.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=88B604889553362AEEA633C5ACDABA4D2E52F83C406FA1229871EFC3D8FFC9BA)

#### 绘制圆弧

可以使用画笔或画刷在画布上进行圆弧的绘制，通过使用drawArc()接口绘制圆弧。

绘制圆弧需要一个矩形（[common2D.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d#rect)），以矩形的边为轮廓进行绘制，还需要两个参数，分别表示弧形的起始角度（startAngle）和扫描角度（sweepAngle）。

此处以使用画笔绘制圆弧为例，简单示例如下：

// 创建画笔
let pen = new drawing.Pen();
// 设置颜色
pen.setColor({
  alpha: 0xFF,
  red: 0xFF,
  green: 0x00,
  blue: 0x00
});
// 设置线宽
pen.setStrokeWidth(20);
// 设置画笔描边效果
canvas.attachPen(pen);
// 创建矩形对象
const rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_200,
  right: VALUE\_1000,
  bottom: VALUE\_600
};
// 绘制矩形
canvas.drawArc(rect, 0, 180);
// 去除描边效果
canvas.detachPen();

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/nisMpp6JTZ-CxEiGsE8fHA/zh-cn_image_0000002538179532.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=3F8D86E8E925F973846409A33FF91A1CAB6C7C1AB973760BB3F5CF5A1CEA4E20)

#### 绘制圆

可以使用画笔或画刷在画布上进行圆的绘制，通过使用drawCircle()接口绘制圆。

绘制圆需要圆心点的x坐标和y坐标，以及圆半径（radius）。

此处以使用画笔绘制圆为例，简单示例如下：

// 创建画笔
let pen = new drawing.Pen();
// 设置颜色
pen.setColor({
  alpha: 0xFF,
  red: 0xFF,
  green: 0x00,
  blue: 0x00
});
// 设置线宽
pen.setStrokeWidth(20);
// 设置画笔描边效果
canvas.attachPen(pen);
// 绘制圆
canvas.drawCircle(VALUE\_630, VALUE\_630, VALUE\_500);
// 去除描边效果
canvas.detachPen();

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/ev1lVpDjReCKYlM3-__k4w/zh-cn_image_0000002569019317.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=6A43513F632038A7F3CB272F3EC804E629CA47303D5F4BF2E45CBEF311492730)

#### 绘制路径

可以使用画笔或画刷在画布上进行路径的绘制，路径具体可以用于绘制直线、弧线、贝塞尔曲线等，也可以通过路径组合的方式组成其他复杂的形状。

绘制路径的相关接口和实现如下，详细的使用和参数说明请见[Path](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-path)。常用的接口如下：

1.  使用new drawing.Path()可以创建一个路径对象。
    
2.  使用moveTo()接口可以设置自定义路径的起始点位置。
    
3.  使用lineTo()接口可以添加一条从起始点或路径的最后点位置（若路径没有内容则默认为(0,0)）到目标点位置的线段。
    

此处以使用画笔和画刷绘制五角星为例，简单示例如下：

let height\_ = VALUE\_1800;
let width\_ = VALUE\_1800;
let len = height\_ / 4;
let aX = width\_ / 3;
let aY = height\_ / 6;
let dX = aX - len \* Math.sin(18.0);
let dY = aY + len \* Math.cos(18.0);
let cX = aX + len \* Math.sin(18.0);
let cY = dY;
let bX = aX + (len / 2.0);
let bY = aY + Math.sqrt((cX - dX) \* (cX - dX) + (len / 2.0) \* (len / 2.0));
let eX = aX - (len / 2.0);
let eY = bY;

// 创建一个path对象，然后使用接口连接成一个五角星形状
let path = new drawing.Path();
// 指定path的起始位置
path.moveTo(aX, aY);
// 用直线连接到目标点
path.lineTo(bX, bY);
path.lineTo(cX, cY);
path.lineTo(dX, dY);
path.lineTo(eX, eY);
// 闭合形状，path绘制完毕
path.close();

// 创建画笔对象
let pen = new drawing.Pen();
// 设置抗锯齿
pen.setAntiAlias(true);
// 设置描边颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// 设置线宽
pen.setStrokeWidth(10.0);
// 设置画笔描边效果
canvas.attachPen(pen);
// 创建画刷
let brush = new drawing.Brush();
// 设置填充颜色
brush.setColor(0xFF, 0x00, 0xFF, 0x00);
// 设置画刷填充效果
canvas.attachBrush(brush);
// 绘制路径
canvas.drawPath(path);
// 去除填充效果
canvas.detachBrush();
// 去除描边效果
canvas.detachPen();

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/JZgiq92RQsa1PsGiG9B_gA/zh-cn_image_0000002568899309.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=ADEB626CA2FD3F45C41FA47E1F4B4F70FE8278078CE5E3BCC282EC0034046ED7)

#### 绘制区域

区域不是一个特定的形状，可以设置为指定的矩形或路径，也可以对两个区域进行组合操作。可以使用画笔或画刷对区域进行绘制。详细的API说明请参考[Region](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-region)。

目前支持设置矩形区域和路径区域，分别通过setRect()接口和setPath()接口来设置。

此处以使用画刷绘制矩形的组合区域为例，示例如下：

// 创建画刷
let brush = new drawing.Brush();
// 设置颜色
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// 设置画刷填充效果
canvas.attachBrush(brush);
// 创建左上角的region1
let region1 = new drawing.Region();
region1.setRect(VALUE\_100, VALUE\_100, VALUE\_600, VALUE\_600);
// 创建右下角的region2
let region2 = new drawing.Region();
region2.setRect(VALUE\_300, VALUE\_300, VALUE\_900, VALUE\_900);
// 将两个区域以XOR的方式组合
region1.op(region2, drawing.RegionOp.XOR);
// 绘制区域
canvas.drawRegion(region1);
// 去除填充效果
canvas.detachBrush();

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/uxp_okN4QiuBunWOoDCTMg/zh-cn_image_0000002538019604.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=43360B6EF89855DDD6D77716A0A3B02E3F87D5E9D2C9CAECA367C6C56D75F3A2)

#### 绘制矩形

可以使用画笔或画刷在画布上进行矩形的绘制。使用drawRect()接口绘制矩形。接口需要传入四个浮点数，分别表示矩形的左、上、右、下四个位置的坐标，连接这4个坐标形成一个矩形。

此处以使用画刷绘制矩形为例，简单示例如下：

// 创建画刷
let brush = new drawing.Brush();
// 设置颜色
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// 设置画刷填充效果
canvas.attachBrush(brush);
// 绘制矩形
canvas.drawRect(VALUE\_200, VALUE\_200, VALUE\_1000, VALUE\_700);
// 去除填充效果
canvas.detachBrush();

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/01kiFAswQ5u9D_ZCN5qJ8w/zh-cn_image_0000002538179534.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=D8B29B86A6F5C6A745005716D3864E5B2254E67A974C13DFE8DB365E769E084A)

#### 绘制圆角矩形

可以使用画笔或画刷在画布上进行圆角矩形的绘制。使用drawRoundRect()接口绘制圆角矩形。接口接受1个入参roundRect，对应为圆角矩形对象。

圆角矩形对象通过new drawing.RoundRect()接口构造，构造函数接受3个参数，分别为：

-   common2D.Rect（矩形对象），圆角矩形是在该矩形的基础上切圆角形成。
    
-   x轴上的圆角半径。
    
-   y轴上的圆角半径。
    

此处以使用画刷绘制圆角矩形为例，简单示例代码如下：

// 创建画刷
let brush = new drawing.Brush();
// 设置颜色
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// 设置画刷填充效果
canvas.attachBrush(brush);
// 创建矩形对象
let rect: common2D.Rect = {
  left: VALUE\_200,
  top: VALUE\_200,
  right: VALUE\_1000,
  bottom: VALUE\_700
};
console.info('rect:', rect.right);
// 创建圆角矩形对象
let rrect = new drawing.RoundRect(rect, 30, 30);
// 绘制圆角矩形
canvas.drawRoundRect(rrect);
// 去除填充效果
canvas.detachBrush();

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/7oK1qAeUQsOcQ30H-wFvlA/zh-cn_image_0000002569019319.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=EEA839B9A36E1AC340D2E1AF5172694429CF53280623D0AC1C532136F7BAFF6A)

#### 示例代码

-   [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
