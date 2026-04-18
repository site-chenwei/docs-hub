---
title: "画布操作及状态处理（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-operation-state-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "画布操作及状态"
  - "画布操作及状态处理（C/C++）"
captured_at: "2026-04-17T01:36:08.545Z"
---

# 画布操作及状态处理（C/C++）

#### 场景介绍

创建或获取Canvas画布之后，可以基于画布进一步地进行图形操作和状态处理。画布操作属于可选操作，开发者可以根据场景需要进行。需要先进行画布操作，再进行后续绘制，只有这样画布操作才有效果。

常见的画布操作如下：

-   裁剪。
    
-   矩阵变换，如平移、缩放、旋转等。
    
-   状态保存与恢复。
    

#### 裁剪操作

裁剪是图形处理中的常见操作，裁剪针对的是画布本身，可以用于限制绘图区域，只在指定的区域内进行绘制。需要先进行裁剪操作，再进行绘制，才会有对应效果。

当前支持的裁剪操作主要如下：

-   裁剪矩形。
    
-   裁剪圆角矩形。
    
-   裁剪自定义路径。
    
-   裁剪一个区域。
    

#### \[h2\]接口说明

裁剪操作常用接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h)。

| 接口 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_CanvasClipRect (OH\_Drawing\_Canvas \*, const OH\_Drawing\_Rect \*, OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias) | 用于裁剪一个矩形。 |
| void OH\_Drawing\_CanvasClipRoundRect (OH\_Drawing\_Canvas \*, const OH\_Drawing\_RoundRect \*, OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias) | 用于裁剪一个圆角矩形。 |
| void OH\_Drawing\_CanvasClipPath (OH\_Drawing\_Canvas \*, const OH\_Drawing\_Path \*, OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias) | 用于裁剪一个自定义路径。 |
| OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasClipRegion (OH\_Drawing\_Canvas \*canvas, const OH\_Drawing\_Region \*region, OH\_Drawing\_CanvasClipOp clipOp) | 用于裁剪一个区域。 |

#### \[h2\]开发示例

此处以在画布上裁剪矩形为例给出示例和效果图，其他裁剪操作的逻辑基本相同，注意调用对应的接口并确保要裁剪的数据类型对应准确即可，此处不再一一展开。详细的使用和参数说明请见[drawing\_canvas.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h)。

使用OH\_Drawing\_CanvasClipRect接口裁剪矩形。有以下四个入参：

-   第一个参数是画布Canvas，裁剪操作将在这个画布上进行。请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c)。
    
-   第二个参数是要裁剪的矩形区域。
    
-   第三个参数是裁剪的操作类型，包括交集（INTERSECT）和差集（DIFFERENCE）。
    
-   第四个参数表示是否需要进行抗锯齿处理。
    

// 创建画刷对象
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// 设置画刷填充颜色为蓝色
OH\_Drawing\_BrushSetColor(brush, 0xff0000ff);
// 在画布中设置画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value400\_, value400\_, value1200\_, value1200\_);
// 裁剪矩形区域
OH\_Drawing\_CanvasClipRect(canvas, rect, OH\_Drawing\_CanvasClipOp::INTERSECT, true);
OH\_Drawing\_Point \*point = OH\_Drawing\_PointCreate(value600\_, value600\_);
// 绘制圆形
OH\_Drawing\_CanvasDrawCircle(canvas, point, value600\_);
// 去除画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁画刷对象并收回其占的内存
OH\_Drawing\_BrushDestroy(brush);

| 原始图 | 裁剪后的图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/N3txYz_9TwSA3NHPeoPyzQ/zh-cn_image_0000002568899285.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=032B4774234B7A3300E76996458A1EEC043CA35ED8A3F23D74C1FCA491018CD6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/53iR1_-ASICHQgqB7I_69A/zh-cn_image_0000002538019580.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=B8C38EF1D216BF309FCF703FA78678359121B1520E1C9A244FCD4EE823EE2C1C) |

#### 矩阵变换操作

矩阵变换也是常见的画布操作，是一种坐标系的转换，用于进行图形的变化。

当前支持的矩阵变换主要如下：

-   平移
    
-   缩放
    
-   旋转
    

#### \[h2\]接口说明

矩阵变换操作常用接口如下表所示，详细的使用和参数说明请见[drawing\_matrix.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-matrix-h)。

| 接口 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_CanvasTranslate (OH\_Drawing\_Canvas \*, float dx, float dy) | 用于平移画布一段距离。 |
| void OH\_Drawing\_CanvasScale (OH\_Drawing\_Canvas \*, float sx, float sy) | 用于画布缩放。 |
| void OH\_Drawing\_CanvasRotate (OH\_Drawing\_Canvas \*, float degrees, float px, float py) | 用于画布旋转一定的角度，正数表示顺时针旋转，负数反之。 |
| void OH\_Drawing\_CanvasSkew (OH\_Drawing\_Canvas \*, float sx, float sy) | 用于画布倾斜变换。等同于将当前画布矩阵左乘（premultiply）倾斜变换矩阵，并应用到画布上。其中倾斜变换矩阵为：|1 sx 0| |sy 1 0| |0 0 1|。 |

#### \[h2\]平移

使用OH\_Drawing\_MatrixCreateTranslation()接口实现画布平移。接口接受2个参数，分别为水平方向和垂直方向的平移量，单位为px。

简单示例和示意图如下所示：

// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 设置填充颜色
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画布中的画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建在水平和垂直方向分别平移300px的矩阵对象
OH\_Drawing\_Matrix \*matrix = OH\_Drawing\_MatrixCreateTranslation(value300\_, value300\_);
// 对Canvas进行矩阵变换
OH\_Drawing\_CanvasConcatMatrix(canvas, matrix);
// 绘制矩形
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value200\_, value300\_, value700\_, value600\_);
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_MatrixDestroy(matrix);

| 原始图 | 平移后的效果图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/-G2po1SwTCaKz3A47qsT9Q/zh-cn_image_0000002569019297.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=453800D520DB2C1AA77D2BC04D577110BB1984DC8AF2EB7B04D9CBD08742BD66) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/osD9monrTwqJpc42AUW3Ew/zh-cn_image_0000002568899289.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=ACB79F96B41BFDFCBBD436ADB66F5566729A1B4BE4D133EAE7A0A0F7E8A39C53) |

#### \[h2\]旋转

使用OH\_Drawing\_MatrixCreateRotation()接口实现画布旋转，接口接受3个参数，分别为：旋转角度、旋转中心的x坐标和y坐标。

简单示例和示意图如下所示：

// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 设置填充颜色
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画布中的画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建旋转的矩阵对象，三个参数分别是旋转角度和旋转中心坐标
OH\_Drawing\_Matrix\* matrix = OH\_Drawing\_MatrixCreateRotation(45, value200\_, value300\_);
// 对Canvas进行矩阵变换
OH\_Drawing\_CanvasConcatMatrix(canvas, matrix);
// 绘制矩形
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value200\_, value300\_, value700\_, value600\_);
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_MatrixDestroy(matrix);

| 原始图 | 旋转后的效果图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/DCWZkaXDR-mrJ1AFj0_Y5A/zh-cn_image_0000002538019584.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=F36EC140B00618AE7751B10F785D0500A81FE0C3BEA4A6E34A189E80171B45FE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/QlDYKiD5RUCJuR0GNqP9YA/zh-cn_image_0000002538179514.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=404CC4D2C3157B907DF3D924D060A3B5376A02E6C0673DAF37FF048776D53FA2) |

#### \[h2\]缩放

使用OH\_Drawing\_MatrixCreateScale()接口进行画布缩放，接口接受4个参数，分别为沿x轴和y轴的缩放因子、旋转中心的x轴和y轴坐标。

简单示例和示意图如下所示：

// 创建画刷对象
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// 设置填充颜色
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画布中的画刷
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建缩放的矩阵对象，4个参数分别是旋转中心坐标和水平垂直方向的缩放因子
OH\_Drawing\_Matrix\* matrix = OH\_Drawing\_MatrixCreateScale(2, 2, value200\_, value300\_);
// 对Canvas进行矩阵变换
OH\_Drawing\_CanvasConcatMatrix(canvas, matrix);
// 绘制矩形
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value200\_, value300\_, value700\_, value600\_);
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// 去除画布中的画刷
OH\_Drawing\_CanvasDetachBrush(canvas);
OH\_Drawing\_RectDestroy(rect);

| 原始图 | 放大后的效果图 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/aBvpqWHDRbG2BbgLbqhKVw/zh-cn_image_0000002569019299.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=C8422F58F52788A2D85D2FA8D9D1BC05A06DD30C6079A1807FE169E65CE106FF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/FdSpbEFFT9CtBowT5dTNuA/zh-cn_image_0000002568899291.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=CEB5340E515DB8A8F08ECDA2D860A127B7BAE2B9D804F2D8BC9F022F5E36FE5A) |

#### 画布状态保存与恢复

保存操作用于保存当前画布的状态到一个栈顶，恢复操作用于恢复保存在栈顶的画布状态，恢复操作一旦执行，保存和恢复操作中间一系列平移、缩放、裁剪等操作都会被清除。

#### \[h2\]接口说明

画布状态保存与恢复使用的接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h)。

| 接口 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_CanvasSave (OH\_Drawing\_Canvas \*) | 用于保存当前画布的状态（画布矩阵）到一个栈顶。 |
| void OH\_Drawing\_CanvasRestore (OH\_Drawing\_Canvas \*) | 用于恢复保存在栈顶的画布状态（画布矩阵）。 |
| void OH\_Drawing\_CanvasRestoreToCount (OH\_Drawing\_Canvas \*, uint32\_t saveCount) | 用于恢复到指定数量的画布状态（画布矩阵）。 |

#### \[h2\]开发示例

// 创建画笔对象
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置画笔线宽为20
OH\_Drawing\_PenSetWidth(pen, 20);
// 在画布中设置画笔
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 保存当前画布状态，当前是不存在放大等操作的，这个原始状态会被保存下来
OH\_Drawing\_CanvasSave(canvas);
OH\_Drawing\_Matrix \*matrix = OH\_Drawing\_MatrixCreateScale(2, 2, 2, 2);
// 放大画布
OH\_Drawing\_CanvasConcatMatrix(canvas, matrix);
OH\_Drawing\_Point\* point = OH\_Drawing\_PointCreate(value300\_, value300\_);
// 绘制圆形，因为执行过放大操作，所以此时绘制的是大圆
OH\_Drawing\_CanvasDrawCircle(canvas, point, value200\_);
// 恢复操作，将恢复到没有放大的原始状态
OH\_Drawing\_CanvasRestore(canvas);
// 绘制圆形，因为已经恢复没有放大的原始状态，所以此时绘制的小圆
OH\_Drawing\_CanvasDrawCircle(canvas, point, value200\_);
// 去除画布中的画笔
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁画笔对象并收回其占的内存
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_PointDestroy(point);
OH\_Drawing\_MatrixDestroy(matrix);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/mVGKXmFgTFSJrGAeU1Gv5A/zh-cn_image_0000002538019586.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=3A2E32079BBACFD4AE241E01A0D9AB5FF00B63D30A11D4C574FA0B94B0001093)

#### 示例代码

-   [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
