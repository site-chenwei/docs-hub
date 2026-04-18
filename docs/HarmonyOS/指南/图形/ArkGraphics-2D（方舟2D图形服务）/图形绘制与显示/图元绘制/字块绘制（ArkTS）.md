---
title: "字块绘制（ArkTS）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/textblock-drawing-arkts"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "图元绘制"
  - "字块绘制（ArkTS）"
captured_at: "2026-04-17T01:36:08.699Z"
---

# 字块绘制（ArkTS）

#### 场景介绍

字块（TextBlob）是指文本的集合。无论是单个的文字还是大块的文本，都可以通过字块来绘制。

除了基本的字块绘制之外，还可以给文字添加各种绘制效果。常见的字块绘制场景包括[文字描边](#文字描边)、[文字渐变](#文字渐变)等，更多效果请见[绘制效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drawing-effect-overview)。

本节不涉及文本测量和布局排版相关内容，如需在开发中处理此类文本绘制需求，可参考[文本开发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-overview)，该文档系统讲解了排版策略与相关使用指导。

#### 基本字块绘制

Canvas通过drawTextBlob()来绘制字块。函数接受三个参数：TextBlob字块对象，以及文字基线左端点的x坐标和y坐标。

画布Canvas对象具体可见[画布的获取与绘制结果的显示（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-arkts)。

字块对象可以通过多种方式创建得到，详细的字块创建方式和接口使用请参考[TextBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-textblob)。

此处以使用makeFromString()接口创建字块为例，接口接受3个参数，分别为：

-   需要显示的字符串text。
    
-   font字型对象。其中font用于设置和获取字体的各种属性，如字体大小、文本样式、字体对齐方式、字体渲染方式、字体描边方式等，详细的API介绍请参考[Font](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-font)。
    
-   文本编码方式。当前支持的文本编码方式如下：
    
    -   TEXT\_ENCODING\_UTF8：使用1个字节表示UTF-8或ASCII；
    -   TEXT\_ENCODING\_UTF16：使用2个字节表示大部分unicode；
    -   TEXT\_ENCODING\_UTF32：使用4个字节表示全部unicode；
    -   TEXT\_ENCODING\_GLYPH\_ID：使用2个字节表示glyph index。

基本效果的示例代码和效果图如下：

// 创建字型对象
const font = new drawing.Font();
// 设置字体大小
font.setSize(100);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/pueNMyZBRG-aBPtZCLdrnw/zh-cn_image_0000002538019606.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=7BF5CA8C9B9126DA0A000F00806233AA37BC207251DB0985A0C46A7E8B04631D)

#### 文字描边

基于基本的字块绘制，还可以通过画笔实现文字描边效果，描边效果的更多介绍请参考[描边效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/basic-drawing-effect-arkts#描边效果)。

以下以英文文字描边和中文文字描边给出示例和指导。

#### \[h2\]英文文字描边

英文文字描边的简要示例和示意图如下：

// 创建画笔
let pen = new drawing.Pen();
// 设置抗锯齿
pen.setAntiAlias(true);
// 设置描边线宽
pen.setStrokeWidth(3.0);
// 设置描边颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// 创建字型对象
const font = new drawing.Font();
// 设置字体大小
font.setSize(100);
// 添加画笔描边效果
canvas.attachPen(pen);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);
// 去除描边效果
canvas.detachPen();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/kAGqeB3oSQq2RPacuKOSVQ/zh-cn_image_0000002538179536.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=0E43FBDDE1D119FA32C1A00318CF33149070376C263A11D1D4F3BD44BB25BD8C)

#### \[h2\]中文文字描边

首先需要通过画笔描边，然后需要调用画刷填充内部颜色，去除字体中间的杂质和重叠部分，实现中文文字描边效果。

中文文字描边的简要示例和示意图如下：

// 创建画刷
let brush = new drawing.Brush();
// 创建画笔
let pen = new drawing.Pen();
// 设置抗锯齿
brush.setAntiAlias(true);
// 设置描边颜色
brush.setColor(0xFF, 0xFF, 0xFF, 0xFF);

pen.setAntiAlias(true);
// 设置描边线宽
pen.setStrokeWidth(3.0);
// 设置描边颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);

// 创建字型对象
const font = new drawing.Font();
// 设置字体大小
font.setSize(100);
// 添加画笔描边效果
canvas.attachPen(pen);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString(STROKE\_SAMPLE, font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE\_200,  VALUE\_300);
// 去除描边效果
canvas.detachPen();

canvas.attachBrush(brush);
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/doTTi8JNSX6hNM6MJRR5fA/zh-cn_image_0000002569019321.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=AA53574AF0BE0DF4EC97E5BAC89C69B91410DB88502C98B98D121D1487EE96DC)

#### 文字渐变

基于基本字块绘制，还可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts#着色器效果)。

以下为文字添加了线性渐变着色器效果的简要示例和示意图：

let startPt: common2D.Point = { x: VALUE\_100, y: VALUE\_100 };
let endPt: common2D.Point = { x: VALUE\_900, y: VALUE\_900 };
let colors = \[0xFFFFFF00, 0xFFFF0000, 0xFF0000FF\];
// 创建线性渐变着色器
let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, colors, drawing.TileMode.CLAMP);
// 创建画刷
let brush = new drawing.Brush();
// 设置着色器
brush.setShaderEffect(shaderEffect);
// 添加画刷填充效果
canvas.attachBrush(brush);
// 创建字型
const font = new drawing.Font();
// 设置字体大小
font.setSize(VALUE\_200);
// 创建字块
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE\_100, VALUE\_300);
// 去除填充效果
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/0RWK0BnTQ--dI6GOodTrFA/zh-cn_image_0000002568899313.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=54B41C94B39B3FC6A1867893F1B853EB588A781D55356ECFB3DB168D50A6624B)

#### 主题字体

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。如需涉及文本测量和布局排版相关内容，可参考[使用主题字体（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-arkts)。

设置跟随主题字体的示例代码和效果图如下：

// 创建线性渐变着色器
const font = new drawing.Font();
// 设置文字大小
font.setSize(100);
// 设置跟随主题字体
font.setThemeFontFollowed(true);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString('Hello World', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);

| 未跟随主题字体的效果图 | 跟随主题字体的效果图（不同主题字体显示效果不同，此处仅示意） |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Z46wkEOnREiS9_YW8njFXQ/zh-cn_image_0000002538019608.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=2DB33D7457E48B7536788DB60260D846302C0D64C6AD81562E2FDCE21ACE91FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/g6FiKk6aRyqJGLhzt5zhHQ/zh-cn_image_0000002538179538.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=68661A48516B6483B152F6DF43F6DC7B43BED5C22FE0D9900433016CC4BE8AB6) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/fQa8F7XSTG2vN9PmNFn5Xg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=95492DF16AA168B2DADE4D05D7B6C7DE41B48E02A2E7E026368DCC86ED38177E)

需要在应用入口文件（默认工程中为EntryAbility.ets）中复写onConfigurationUpdate函数，以响应切换主题字体的操作，确保切换后页面能够及时刷新并生效。具体实现可参考[使用主题字体（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-arkts)。

#### 单字绘制

单字绘制是图形渲染中针对文本渲染的一种精细化控制技术。相比字块绘制，其核心优势在于能够利用字体退化机制，在当前字体无法显示某字符时，自动退化到使用系统字体绘制字符，提升对特殊字符的兼容性，避免字符缺失。同时，单字绘制支持逐字符配置字体特征（如连字、替代字形），满足复杂排版需求，增强用户体验。详细API说明请见[drawing.Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas#drawsinglecharacter12)。

基础场景：绘制无字体特征的字符。

对于无需字体特征的常规文本渲染场景，可以使用drawSingleCharacter绘制单个字符，使用measureSingleCharacter测量单个字符的宽度，示例代码和效果图如下：

// 创建字型对象
const font = new drawing.Font();
// 设置文字大小
font.setSize(100);
let startX = 100;
let startY = 100;
let text = \['H', 'e', 'l', 'l', 'o'\];
for (let s of text) {
  // 单字绘制
  canvas.drawSingleCharacter(s, font, startX, startY);
  // 测量单个字符的宽度
  let textWidth = font.measureSingleCharacter(s);
  startX += textWidth;
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/X4PDmxLfRxG1J_pEZhqJLg/zh-cn_image_0000002569019323.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=663FCEEDBCAD6F855A4F0636645EB7F7915B7C13800FB68BA568E71E8355264E)

进阶场景：绘制带字体特征的字符。

对于需要字体特征的文本渲染场景，可以使用drawSingleCharacterWithFeatures绘制单个字符，使用measureSingleCharacterWithFeatures测量单个字符的宽度，示例代码和效果图如下：

// 创建字型对象
const font = new drawing.Font();
// 设置文字大小
font.setSize(100);
let startX = 100;
let startY = 100;
let text = \['a', '2', '+', 'b', '2'\];
// 创建字体特征对象数组
let fontFeatures: drawing.FontFeature\[\] = \[{name: 'frac', value: 1}\];
for (let s of text) {
  // 单字绘制
  canvas.drawSingleCharacterWithFeatures(s, font, startX, startY, fontFeatures);
  // 测量单个字符的宽度
  let textWidth = font.measureSingleCharacterWithFeatures(s, fontFeatures);
  startX += textWidth;
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/rrVv8K7IS2qwTqLgWd-yiw/zh-cn_image_0000002568899315.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=96E1A3233B4B156A0E0D23480F27129ADDC24133799D49034F98ADADC5F7BC23)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ZGraDRRnTfGh2xaqWxD60A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=1B19EC04D975739C4A1D987326C7F29DA9D22085544D144818EF5EA3DAD21AAB)

如果 drawSingleCharacterWithFeatures 与 measureSingleCharacter 混合使用，或者 drawSingleCharacter 与 measureSingleCharacterWithFeatures 混合使用，字体绘制可能会重叠。

#### 示例代码

-   [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
