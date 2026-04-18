---
title: "字块绘制（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/textblock-drawing-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "图元绘制"
  - "字块绘制（C/C++）"
captured_at: "2026-04-17T01:36:08.770Z"
---

# 字块绘制（C/C++）

#### 场景介绍

字块（TextBlob）是指文本的集合。无论是单个的文字还是大块的文本，都可以通过字块来绘制。

除了基本的字块绘制之外，还可以给文字添加各种绘制效果。常见的字块绘制场景包括[文字描边](#文字描边)、[文字渐变](#文字渐变)等，更多效果请见[绘制效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drawing-effect-overview)。

本节不涉及文本测量和布局排版相关内容，如需在开发中处理此类文本绘制需求，可参考[文本开发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-overview)，该文档系统讲解了排版策略与相关使用指导。

#### 基本字块绘制

使用OH\_Drawing\_CanvasDrawTextBlob()接口绘制字块，接口接受4个参数，分别为：画布Canvas对象、字块对象、文字基线左端点的x坐标和y坐标。

画布Canvas对象具体可见[画布的获取与绘制结果的显示（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c)。

字块对象可以通过多种方式创建得到，详细的字块创建方式请参考[drawing\_text\_blob.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-blob-h)。

此处以使用OH\_Drawing\_TextBlobCreateFromString()接口创建字块为例，接口接受3个参数，分别为：

-   需要显示的文本字符串内容。
    
-   指向OH\_Drawing\_Font字体对象的指针。OH\_Drawing\_Font用于设置和获取字体的各种属性，如字体大小、文本样式、字体对齐方式、字体渲染方式、字体描边方式等，详细的API介绍请参考[draw\_font](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-h)。
    
-   文本编码方式。
    

简单示例和示意图如下所示：

// 创建字体对象
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// 设置字体大小
OH\_Drawing\_FontSetTextSize(font, value100\_);
// 需要绘制的文字
const char \*str = "Hello world";
// 创建字块对象
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// 绘制字块
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// 释放字块对象
OH\_Drawing\_TextBlobDestroy(textBlob);
// 释放字体对象
OH\_Drawing\_FontDestroy(font);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/U56Ld1vWQxuen_y2xSFU3g/zh-cn_image_0000002568899319.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=7F4DA099C4602476389ED4DF56AA1A84CD15E3BDA6914903C81CF8C6386F9724)

#### 文字描边

基于基本的字块绘制，还可以通过画笔实现文字描边效果，描边效果的更多介绍请参考[描边效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/basic-drawing-effect-c#描边效果)。

以下以英文文字描边和中文文字描边给出示例和指导。

#### \[h2\]英文文字描边

英文文字描边的简要示例和示意图如下：

// 创建画笔
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// 设置抗锯齿
OH\_Drawing\_PenSetAntiAlias(pen, true);
// 设置描边颜色
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// 设置描边线宽为3
OH\_Drawing\_PenSetWidth(pen, 3);
// 设置画笔描边效果
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建字型对象
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// 设置字体大小
OH\_Drawing\_FontSetTextSize(font, value150\_);
const char \*str = "Hello world";
// 创建字块对象
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// 绘制字块
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// 去除描边效果
OH\_Drawing\_CanvasDetachPen(canvas);
// 销毁各类对象
OH\_Drawing\_TextBlobDestroy(textBlob);
OH\_Drawing\_FontDestroy(font);
OH\_Drawing\_PenDestroy(pen);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Oa3VOBH6S5eYMPwKS5MhsQ/zh-cn_image_0000002538019614.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=7DD44CC91DBBA7A0CBFC8DC92B332ADB9F8342DBD5CDA99F30C9B92C9585A1FA)

#### \[h2\]中文文字描边

首先需要通过画笔描边，然后需要调用画刷填充内部颜色，去除字体中间的杂质和重叠部分，实现中文文字描边效果。

中文文字描边的简要示例和示意图如下：

// 创建画刷
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// 创建画笔
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// 设置画刷抗锯齿
OH\_Drawing\_BrushSetAntiAlias(brush, true);
// 设置画刷描边颜色
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(0xFF, 0xFF, 0xFF, 0xFF));
// 设置画笔抗锯齿
OH\_Drawing\_PenSetAntiAlias(pen, true);
// 设置描边线宽为3
OH\_Drawing\_PenSetWidth(pen, 3);
// 设置画笔描边颜色
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(0xFF, 0xFF, 0x00, 0x00));
// 设置画笔描边效果
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// 创建字型对象
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// 设置字体大小
OH\_Drawing\_FontSetTextSize(font, value150\_);
const char \*str = "你好";
// 创建字块对象
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// 绘制字块
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// 去除描边效果
OH\_Drawing\_CanvasDetachPen(canvas);
// 设置画刷描边效果
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);

// 销毁各类对象
OH\_Drawing\_TextBlobDestroy(textBlob);
OH\_Drawing\_FontDestroy(font);
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_BrushDestroy(brush);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/pyFiYLaNQG6ZsZscDAjAQw/zh-cn_image_0000002538179544.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=BD81C59C95BCA7F6CFC9366AD7EBBB9E26DF1D3F8CACB015DF6FC12E0D51E479)

#### 文字渐变

基于基本字块绘制，还可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-c#着色器效果)。

以下为文字添加了线性渐变着色器效果的简要示例和示意图：

// 开始点
OH\_Drawing\_Point \*startPt = OH\_Drawing\_PointCreate(value100\_, value100\_);
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
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// 基于画刷设置着色器效果
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// 设置画刷填充效果
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// 创建字型对象
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// 设置字体大小
OH\_Drawing\_FontSetTextSize(font, value150\_);
const char \*str = "Hello world";
// 创建字块对象
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// 绘制字块
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// 取消填充效果
OH\_Drawing\_CanvasDetachBrush(canvas);
// 销毁各类对象
OH\_Drawing\_TextBlobDestroy(textBlob);
OH\_Drawing\_FontDestroy(font);
OH\_Drawing\_BrushDestroy(brush);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/KXqxGtvBSZqjUJXPIegFVg/zh-cn_image_0000002569019329.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=2367F0166C43F24876DF9402BCBA5C8F94CA111B6806D8974B39D5AD5B944D96)

#### 主题字体

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。如需涉及文本测量和布局排版相关内容，可参考[使用主题字体（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-c)。

设置跟随主题字体的示例代码和效果图如下：

// 创建字型对象
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// 设置文字大小
OH\_Drawing\_FontSetTextSize(font, value100\_);
// 设置跟随主题字体
OH\_Drawing\_FontSetThemeFontFollowed(font, true);
// 需要绘制的文字
const char \*str = "Hello World";
// 创建字块对象
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// 绘制字块
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// 释放字块对象
OH\_Drawing\_TextBlobDestroy(textBlob);
// 释放字型对象
OH\_Drawing\_FontDestroy(font);

| 未跟随主题字体的效果图 | 跟随主题字体的效果图（不同主题字体显示效果不同，此处仅示意） |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/F8HX-mV4TKOwtwhcq0ukmA/zh-cn_image_0000002538019608.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=CB5BB967860E55542739CCFB623220C4FB39BC473831E38774947D2206DBF930) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/oQriUg69QUShPyGA9IeYLw/zh-cn_image_0000002538179538.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=85D982136B75E4E757DBFD1B0A981ADA7494DA54822905AA7FC7708898F0BFCE) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/kdtNGW7eR5SPpUBm2zqijA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=830A39C1F1240516ED41D081E76E661701145CFE7F8AF4DECF616838E26E81A4)

需要在应用入口文件（默认工程中为EntryAbility.ets）中重写onConfigurationUpdate函数，以响应切换主题字体的操作，确保切换后页面能够及时刷新并生效。具体实现可参考[使用主题字体（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-c)。

#### 单字绘制

单字绘制是图形渲染中针对文本渲染的一种精细化控制技术。相比字块绘制，其核心优势在于能够利用字体退化机制，在当前字体无法显示某字符时，自动退化到使用系统字体绘制字符，提升对特殊字符的兼容性，避免字符缺失。同时，单字绘制支持逐字符配置字体特征（如连字、替代字形），满足复杂排版需求，增强用户体验。详细API说明请见[drawing\_canvas.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h#oh_drawing_canvasdrawsinglecharacter)。

基础场景：绘制无字体特征的字符。

对于无需字体特征的常规文本渲染场景，可以使用OH\_Drawing\_CanvasDrawSingleCharacter绘制单个字符，使用OH\_Drawing\_FontMeasureSingleCharacter测量单个字符的宽度，示例代码和效果图如下：

// 创建字型对象
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// 设置文字大小
OH\_Drawing\_FontSetTextSize(font, value100\_);
float startX = 100;
float startY = 100;
int strLen = 5;
const char\* str = "Hello";
for (int i = 0; i < strLen; ++i) {
    // 单字绘制
    OH\_Drawing\_CanvasDrawSingleCharacter(canvas, &str\[i\], font, startX, startY);
    float textWidth = 0.f;
    // 测量单个字符的宽度
    OH\_Drawing\_FontMeasureSingleCharacter(font, &str\[i\], &textWidth);
    startX += textWidth;
}
// 释放字型对象
OH\_Drawing\_FontDestroy(font);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/gko-RDwxQqeElh_M4WiT-A/zh-cn_image_0000002569019323.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=C01C82607FEC9CBE9C78599BF8D21BB8030300B337D89E88464A4156251E397A)

进阶场景：绘制带字体特征的字符。

对于需要字体特征的文本渲染场景，可以使用OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures绘制单个字符，使用OH\_Drawing\_FontMeasureSingleCharacterWithFeatures测量单个字符的宽度，示例代码和效果图如下：

// 创建字型对象
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// 设置文字大小
OH\_Drawing\_FontSetTextSize(font, value100\_);
// 创建字体特征对象
OH\_Drawing\_FontFeatures\* features = OH\_Drawing\_FontFeaturesCreate();
OH\_Drawing\_FontFeaturesAddFeature(features, "frac", 1);
float startX = 100;
float startY = 100;
int strLen = 5;
const char\* str = "a2+b2";
for (int i = 0; i < strLen; ++i) {
    // 单字绘制
    OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures(canvas, &str\[i\], font, startX, startY, features);
    float textWidth = 0.f;
    // 测量单个字符的宽度
    OH\_Drawing\_FontMeasureSingleCharacterWithFeatures(font, &str\[i\], features, &textWidth);
    startX += textWidth;
}
// 释放字体特征对象
OH\_Drawing\_FontFeaturesDestroy(features);
// 释放字型对象
OH\_Drawing\_FontDestroy(font);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/1L6NhS3vQs6uiwXKaxOxgw/zh-cn_image_0000002568899315.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=FFFA6E853805644EEEF3268DF0632F6D68DE04E6A0A178C3023DF5D133099095)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/8OcMUK81SoeH9JiN4hFdKA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=7FC69639F3E70B23E10DF2B8FB0B2C27F91309F5706214A2EFBECD1585C36EDA)

如果 OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures 与 OH\_Drawing\_FontMeasureSingleCharacter 混合使用，或者 OH\_Drawing\_CanvasDrawSingleCharacter 与 OH\_Drawing\_FontMeasureSingleCharacterWithFeatures 混合使用，字体绘制可能会重叠。

#### 示例代码

-   [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
