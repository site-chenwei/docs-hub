---
title: "几何形状绘制（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/geometric-shape-drawing-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "图元绘制"
  - "几何形状绘制（C/C++）"
captured_at: "2026-04-17T01:36:08.718Z"
---

# 几何形状绘制（C/C++）

#### 场景介绍

当前支持绘制的几何形状，主要包括以下几种：

-   点
    
-   圆弧
    
-   圆
    
-   路径
    
-   区域
    
-   矩形
    
-   圆角矩形
    

大部分的几何形状均可以选择使用画笔或者使用画刷来实现绘制，其中点的绘制只能使用画笔。

#### 接口说明

几何形状绘制的常用接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h)。

| 接口 | 描述 |
| :-- | :-- |
| OH\_Drawing\_Point\* OH\_Drawing\_PointCreate (float x, float y) | 用于创建一个坐标点对象。 |
| OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPoint (OH\_Drawing\_Canvas \*canvas, const OH\_Drawing\_Point2D \*point) | 用于画一个点。 |
| OH\_Drawing\_Rect\* OH\_Drawing\_RectCreate (float left, float top, float right, float bottom) | 用于创建一个矩形对象。 |
| void OH\_Drawing\_CanvasDrawArc (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Rect\*, float startAngle, float sweepAngle) | 用于画一个弧。 |
| void OH\_Drawing\_CanvasDrawCircle (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Point\*, float radius) | 用于画一个圆形。 |
| OH\_Drawing\_Path\* OH\_Drawing\_PathCreate (void) | 用于创建一个路径对象。 |
| void OH\_Drawing\_CanvasDrawPath (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Path\*) | 用于画一个自定义路径。 |
| OH\_Drawing\_Region\* OH\_Drawing\_RegionCreate (void) | 用于创建一个区域对象。 |
| void OH\_Drawing\_CanvasDrawRegion (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Region\*) | 用于画一块区域。 |
| void OH\_Drawing\_CanvasDrawRect (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Rect\*) | 用于画一个矩形。 |
| OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCreate (const OH\_Drawing\_Rect\*, float xRad, float yRad) | 用于创建一个圆角矩形对象。 |
| void OH\_Drawing\_CanvasDrawRoundRect (OH\_Drawing\_Canvas\*, const OH\_Drawing\_RoundRect\*) | 用于画一个圆角矩形。 |

#### 绘制点

点只能基于画笔在画布上进行绘制，通过使用OH\_Drawing\_CanvasDrawPoint()接口绘制点。接口接受两个参数，一个是画布对象Canvas，请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c)；另一个是要绘制的点的指针。

简单示例如下：

// 创建画笔对象
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// 设置画笔颜色
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画笔线宽为40
OH\_Drawing\_PenSetWidth(pen, 40);
// 设置画布的画笔
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 绘制5个点
AdaptationUtil\* adaptationUtil = AdaptationUtil::GetInstance();
OH\_Drawing\_Point2D point1 = {value200\_, value200\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point1);
OH\_Drawing\_Point2D point2 = {value400\_, value400\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point2);
OH\_Drawing\_Point2D point3 = {value600\_, value600\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point3);
OH\_Drawing\_Point2D point4 = {value800\_, value800\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point4);
OH\_Drawing\_Point2D point5 = {value1000\_, value1000\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point5);
// 去除掉画布中的画笔
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁各类对象
OH\_Drawing\_PenDestroy(pen);

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Mz7k0tk7TnC2FrEtYp8r-Q/zh-cn_image_0000002538019610.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=CD0540F1237C29705A2B2719FBBCFA47B1C72F0DC54F8D1898926F0BB431A960)

#### 绘制圆弧

可以使用画笔或画刷在画布上进行圆弧的绘制，通过使用OH\_Drawing\_CanvasDrawArc()接口绘制圆弧。使用接口需要传入4个参数，分别如下：

-   需要画布对象Canvas，请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c)。
    
-   绘制圆弧还需要一个矩形，会以矩形的边为轮廓进行绘制。
    
-   需要一个浮点参数，表示弧形的起始角度。
    
-   需要另一个浮点参数，表示弧形的扫描角度。
    

此处以使用画笔绘制圆弧为例，简单示例如下：

// 创建画笔对象
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画笔线宽为20
OH\_Drawing\_PenSetWidth(pen, 20);
// 设置画布的画笔
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建矩形对象，左上坐标为（100，200）右下坐标为（500，300）
OH\_Drawing\_Rect\* rect = OH\_Drawing\_RectCreate(100, 200, 500, 300);
// 基于矩形对象绘制圆弧，其实角度10°，扫描角度200°
OH\_Drawing\_CanvasDrawArc(canvas, rect, 10, 200);
// 去除掉画布中的画笔
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁各类对象
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_RectDestroy(rect);

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/tXmGyh3ZT7Ctc2_ocMBppA/zh-cn_image_0000002538179540.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=64F8FB173F12CB7368B11028750320F1220EA3F9E31E344FF6DDF2B6D285F553)

#### 绘制圆

可以使用画笔或画刷在画布上进行圆的绘制，通过使用OH\_Drawing\_CanvasDrawCircle()接口绘制圆。使用接口需要传入3个参数，分别如下：

-   需要画布对象Canvas，请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c)。
    
-   绘制圆还需要一个指向圆心点对象的指针，会以此点为圆心进行绘制。
    
-   最后需要一个浮点参数，表示圆的半径。
    

此处以使用画笔绘制圆为例，简单示例如下：

// 创建画笔对象
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画笔线宽为20
OH\_Drawing\_PenSetWidth(pen, 20);
// 设置画布的画笔
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建圆心点
OH\_Drawing\_Point \*point = OH\_Drawing\_PointCreate(value700\_, value700\_);
// 基于圆心点和半径在画布上绘制圆
OH\_Drawing\_CanvasDrawCircle(canvas, point, value600\_);
// 去除掉画布中的画笔
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁各类对象
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_PointDestroy(point);

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/OKmSzwQLSee7JVoiSN0qZg/zh-cn_image_0000002569019325.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=CDC2BBAC54CA6947C264A610F0E39E81F3F4894F054DA8A7C0DF119007EA9F0A)

#### 绘制路径

可以使用画笔或画刷在画布上进行路径的绘制，路径具体可以用于绘制直线、弧线、贝塞尔曲线等，也可以通过路径组合的方式组成其他复杂的形状。

绘制路径的相关接口和实现如下，详细的使用和参数说明请见[drawing\_path](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-path-h)。常用的接口如下：

1.  使用OH\_Drawing\_PathCreate()接口可以创建一个路径对象。
    
2.  使用OH\_Drawing\_PathMoveTo()接口可以设置自定义路径的起始点位置。
    
3.  使用OH\_Drawing\_PathLineTo()接口可以添加一条从起始点或路径的最后点位置（若路径没有内容则默认为(0,0)）到目标点位置的线段。
    

此处以使用画笔和画刷绘制五角星为例，示例如下：

// 创建画笔对象
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画笔线宽为10
OH\_Drawing\_PenSetWidth(pen, 10);
// 设置 画笔转角样式
OH\_Drawing\_PenSetJoin(pen, LINE\_ROUND\_JOIN);
// 设置画布中的画笔
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建画刷，此例对闭合路径进行了颜色填充，所以需要使用画刷
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MIN, RGBA\_MAX, RGBA\_MIN));
// 设置画布中的画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
int len = value551\_;
float aX = value630\_;
float aY = value551\_;
float dX = aX - len \* std::sin(18.0f);
float dY = aY + len \* std::cos(18.0f);
float cX = aX + len \* std::sin(18.0f);
float cY = dY;
float bX = aX + (len / 2.0);
float bY = aY + std::sqrt((cX - dX) \* (cX - dX) + (len / 2.0) \* (len / 2.0));
float eX = aX - (len / 2.0);
float eY = bY;
// 创建路径
OH\_Drawing\_Path\* path = OH\_Drawing\_PathCreate();
// 到起始点
OH\_Drawing\_PathMoveTo(path, aX, aY);
// 绘制直线
OH\_Drawing\_PathLineTo(path, bX, bY);
OH\_Drawing\_PathLineTo(path, cX, cY);
OH\_Drawing\_PathLineTo(path, dX, dY);
OH\_Drawing\_PathLineTo(path, eX, eY);
// 直线闭合，形成五角星
OH\_Drawing\_PathClose(path);
// 绘制闭合路径
OH\_Drawing\_CanvasDrawPath(canvas, path);
// 去除掉画布中的画笔和画刷
OH\_Drawing\_CanvasDetachPen(canvas);
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_PathDestroy(path);

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/1TcFyLMeScmlsnY5htxzfQ/zh-cn_image_0000002568899317.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=EBE3F1D59AA5DAEDAB17E0CA48C7E009150CDE2C1984B3D99B592248F850B56A)

#### 绘制区域

区域不是一个特定的形状，可以设置为指定的矩形或路径，也可以对两个区域进行组合操作。可以使用画笔或画刷在画布上进行区域的绘制。详细的API说明请参考[drawing\_region.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-region-h)。

目前支持设置矩形区域和路径区域，分别通过OH\_Drawing\_RegionSetRect()接口和OH\_Drawing\_RegionSetPath()接口来设置。

此处以使用画刷绘制矩形的组合区域为例，示例如下：

// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 设置画刷填充颜色
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画布的画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 矩形区域1
OH\_Drawing\_Region \*region1 = OH\_Drawing\_RegionCreate();
OH\_Drawing\_Rect \*rect1 = OH\_Drawing\_RectCreate(value100\_, value100\_, value600\_, value600\_);
OH\_Drawing\_RegionSetRect(region1, rect1);
// 矩形区域2
OH\_Drawing\_Region \*region2 = OH\_Drawing\_RegionCreate();
OH\_Drawing\_Rect \*rect2 = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
OH\_Drawing\_RegionSetRect(region2, rect2);
// 两个矩形区域组合
OH\_Drawing\_RegionOp(region1, region2, OH\_Drawing\_RegionOpMode::REGION\_OP\_MODE\_XOR);
OH\_Drawing\_CanvasDrawRegion(canvas, region1);
// 去除掉画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RegionDestroy(region1);
OH\_Drawing\_RegionDestroy(region2);
OH\_Drawing\_RectDestroy(rect1);
OH\_Drawing\_RectDestroy(rect2);

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/aGrgIgIqQBGWQXWW2cNJEA/zh-cn_image_0000002538019604.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=37C47F396DD57A57B525B72D18DD6E9349F69748008C898A75A7104D5F906FFF)

#### 绘制矩形

可以使用画笔或画刷在画布上进行矩形的绘制。使用OH\_Drawing\_RectCreate()接口创建矩形。接口需要传入四个浮点数，分别表示矩形的左、上、右、下四个位置的坐标，连接这4个坐标形成一个矩形。

简单示例如下：

// 创建画刷对象
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// 设置画刷的填充颜色
OH\_Drawing\_BrushSetColor(brush, 0xffff0000);
// 设置画布的画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect\* rect = OH\_Drawing\_RectCreate(0, 0, value800\_, value800\_);
// 绘制矩形
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/IgnI50nWRiiAwIbqx3gzsA/zh-cn_image_0000002538019612.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=BC5C04A895B02BD6BA8352260FF44F1376F0BAEE77A1DC98E6E8CB53E6B04EC7)

#### 绘制圆角矩形

可以使用画笔或画刷在画布上进行圆角矩形的绘制。使用OH\_Drawing\_RoundRectCreate()接口创建圆角矩形。接口需要传入3个参数，分别如下：

-   需要传入指向OH\_Drawing\_Rect矩形对象的指针，用于在此矩形的基础上切圆角进行绘制。
    
-   需要一个浮点参数，表示x轴上的圆角半径。
    
-   还需要一个浮点参数，表示y轴上的圆角半径。
    

简单示例如下：

// 创建画刷对象
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// 设置画刷的填充颜色
OH\_Drawing\_BrushSetColor(brush, 0xffff0000);
// 设置画布的画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建矩形
OH\_Drawing\_Rect\* rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value600\_);
// 创建圆角矩形
OH\_Drawing\_RoundRect\* roundRect = OH\_Drawing\_RoundRectCreate(rect, 30, 30);
// 绘制圆角矩形
OH\_Drawing\_CanvasDrawRoundRect(canvas, roundRect);
// 去除掉画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_RoundRectDestroy(roundRect);

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/MaUVSy93Rt2VYED6iuXQRw/zh-cn_image_0000002538179542.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=3384F30DF878B1D3F38E61598FC301FD0ED9CB53FD96649963EF9C4AE650C350)

#### 示例代码

-   [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
