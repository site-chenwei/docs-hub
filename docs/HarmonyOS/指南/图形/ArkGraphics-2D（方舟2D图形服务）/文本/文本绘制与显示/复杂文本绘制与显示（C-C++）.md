---
title: "复杂文本绘制与显示（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "文本"
  - "文本绘制与显示"
  - "复杂文本绘制与显示（C/C++）"
captured_at: "2026-04-17T01:36:09.021Z"
---

# 复杂文本绘制与显示（C/C++）

在进行文本绘制时，可以通过选择合适的字体、大小和颜色完成简单文本的绘制与显示；此外，还支持通过设置其他丰富的样式、语言、段落等进行复杂文本的绘制。

复杂文本绘制主要包含以下几个场景：

-   多语言文本绘制与显示
    
-   多行文本绘制与显示
    
-   多样式文本绘制与显示
    
-   样式的拷贝、绘制与显示
    

#### 多语言文本绘制与显示

多语言支持是全球化应用的基础。多语言文本绘制需要支持不同语言的字符集及其独特的显示需求，例如右到左语言（如阿拉伯语）或竖排文本（如中文）。开发者需要理解不同语言的渲染特性，确保文本的正确显示。

在多语言文本使用的场景下，主要通过指定TextStyle文本样式中的**locale**字段来实现，可直接通过locale字段的值优先匹配对应字体，跳过遍历列表匹配字体的过程，从而降低匹配时间和内存使用。

#### \[h2\]接口说明

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyTextLocale(OH\_Drawing\_TypographyStyle\* style, const char\* locale) | 设置指定排版样式的语言环境。 |

#### \[h2\]开发步骤

画布Canvas对象具体可见[画布的获取与绘制结果的显示](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c)。

// 创建一个 TypographyStyle，创建 TypographyCreate 时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置文本对齐方式为居中
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// 设置 locale 为中文
OH\_Drawing\_SetTypographyTextLocale(typoStyle, "zh-Hans");

// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);

// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 将之前创建的 TextStyle 加入 handler 中
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// 设置文本内容，并将文本添加到 handler 中
const char \*text = "你好，中文\\n";
OH\_Drawing\_TypographyHandlerAddText(handler, text);

// 通过 handler 创建一个 Typography
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放内存
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

#### \[h2\]效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/q84vpu7BTOyvlaU6hiKNnw/zh-cn_image_0000002538179566.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=E29DA638CDAF82A1088A73E0ECB97E893FE5060538D2A9FE20B58C79DD412803)

#### 多行文本绘制与显示

多行文本相对于单行文本比较复杂，一般针对多行文本，需要进行文本排版、断词策略设置、文本对齐方式、最大行数限制等，主要通过设置段落样式实现。

#### \[h2\]接口说明

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyTextAlign(OH\_Drawing\_TypographyStyle\* style, int align) | 设置文本对齐方式。 |
| void OH\_Drawing\_SetTypographyTextWordBreakType(OH\_Drawing\_TypographyStyle\* style, int wordBreakType) | 设置单词的断词方式。 |
| void OH\_Drawing\_SetTypographyTextMaxLines(OH\_Drawing\_TypographyStyle\* style, int lineNumber) | 设置文本最大行数。 |

#### \[h2\]开发步骤

以下以断行策略为 BREAK\_ALL 的场景为例，其余策略同理。

// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();

// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TWENTY(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);

// 设置文本内容
const char \*text =
    "Nunc quis augue viverra, venenatis arcu eu, gravida odio. Integer posuere nisi quis ex pretium, a dapibus "
    "nisl gravida. Mauris lacinia accumsan enim, non tempus ligula. Mauris iaculis dui eu nisi tristique, in porta "
    "urna varius. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris "
    "congue nibh mi, vel ultrices ex volutpat et. Aliquam consectetur odio in libero tristique, a mattis ex "
    "mollis. Praesent et nisl iaculis, facilisis metus nec, faucibus lacus. Duis nec dolor at nibh eleifend "
    "tempus. Nunc et enim interdum, commodo eros ac, pretium sapien. Pellentesque laoreet orci a nunc pharetra "
    "pharetra.";

// 创建一个断词策略为 BREAK\_ALL 的 TypographyStyle
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置文本对齐方式为居中
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// 设置断词策略为 WORD\_BREAK\_TYPE\_BREAK\_ALL
OH\_Drawing\_SetTypographyTextWordBreakType(typoStyle, OH\_Drawing\_WordBreakType::WORD\_BREAK\_TYPE\_BREAK\_ALL);
// 设置最大行数为 10，行数大于 10 的部分不显示
OH\_Drawing\_SetTypographyTextMaxLines(typoStyle, 10);

// 使用之前创建的 FontCollection 和 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// 将之前创建的 TextStyle 加入 handler
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放内存
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

| BREAK\_ALL | BREAK\_WORD |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Zi59e2NpRI-jNxnN9FhlZw/zh-cn_image_0000002569019351.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=DDC9B88D952BC268DB586BC7B67084FD3D3020433E72F0D25B35C6B6225256DB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/5q3UvspVS0WMeNnJ8HpwXA/zh-cn_image_0000002568899343.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=962245F33909C04668231309EC4F8C9D8B0C7B92833591DC76B750692D253355) |

| BREAK\_HYPHEN（locale：未设置） | BREAK\_HYPHEN（locale：en-gb） | BREAK\_HYPHEN（locale：en-us） |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/JlpQ95yeSOimS7ozkWAI_g/zh-cn_image_0000002538019638.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=FD859F15782F59F1FA9FE85EF2F0D09726C5BE2489A3384CEB7158FE24E7E418) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/FYtpwfCCT_qwk912hefW5Q/zh-cn_image_0000002538179568.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=39829B7BFBD96434781DE614AF786DCA90D44D0112B7FA691822AF93867D40EE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/FYAfY5HMRWitklJ5e6plAA/zh-cn_image_0000002569019353.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=92E2E98CD4EBD2F2DA0553E6E1AC0C0806A25576A11CC1F03A13B2AF0087313C) |

#### 多样式文本绘制与显示

除基本文字、排版属性之外，针对应用中不同文本的设计，开发者可能需要设置使用不同的绘制样式或能力，以凸显对应文本的独特表现或风格，此时可以结合使用多种绘制样式进行文本的渲染。

当前支持的多样式绘制及各绘制样式侧重效果如下：

-   **装饰线样式绘制：** 主要通过不同的线条样式对文本进行装饰，可以使文本更加突出，富有表现力。
    
-   **字体特性绘制：** 主要通过字体的变化，包括粗细、斜体等特性来改变文本的外观，增强文本的可读性和美观性。
    
-   **可变字体绘制：** 对应提供文本在不同的显示环境和设备上灵活调整的能力，可满足更为精细的视觉效果。
    
-   **文本阴影绘制：** 主要通过在文本周围添加阴影效果，以提升文本的层次感和立体感，从而使文本更具吸引力。
    
-   **占位符绘制：** 可以在不确定文本内容时保持文本布局的稳定性，使得文本显示更为流畅和自然。
    
-   **自动间距绘制：** 可以在一些字符混排切换的地方自动添加额外间距，提升阅读体验。
    
-   **渐变色绘制：** 可以为文字提供颜色渐变效果，增强文字表现力。
    
-   **垂直对齐：** 调整文本在垂直方向排版位置，提升排版质量。
    
-   **上下标：** 可以将任意字符处理成上标或下标，更精准表达文本含义。
    
-   **高对比度文字绘制：** 主要通过将深色文字变黑、浅色文字变白，增强文本的对比效果。
    
-   **行高调整：** 调整行高可改变文本行的垂直间距，使行间距更松散或更紧凑，显著改善文本垂直截断问题，提高可读性。
    
-   **行间距调整：** 通过调整行间距的方式可以实现行高调整一样的效果，优化阅读体验。
    

#### \[h2\]装饰线

**装饰线**是指在文本上方、下方或中间添加的装饰性线条，当前支持上划线、下划线、删除线。

可以通过添加文本装饰线，提升文本的视觉效果和可读性。

使用装饰线需要初始化装饰线样式对象，并添加到文本样式中，从而在文本绘制时生效。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration) | 设置指定文本样式中的装饰线类型，只能设置一个装饰线类型，添加多个需要使用OH\_Drawing\_AddTextStyleDecoration。 |
| void OH\_Drawing\_SetTextStyleDecorationStyle(OH\_Drawing\_TextStyle\* style, int decorationStyle) | 设置指定文本样式中的装饰线样式。 |
| void OH\_Drawing\_SetTextStyleDecorationColor(OH\_Drawing\_TextStyle\* style, uint32\_t color) | 设置指定文本样式中的装饰线颜色。 |

示例及示意效果如下所示：

// 创建一个TypographyStyle创建Typography时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置文本对齐方式为居中
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// 设置文本内容
const char \*text = "Hello World Drawing\\n";

// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_TextStyle \*txtStyleWithDeco = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyleWithDeco, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithDeco, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithDeco, FONT\_WEIGHT\_400);
// 设置装饰线为 LINE\_THROUGH
OH\_Drawing\_SetTextStyleDecoration(txtStyleWithDeco, TEXT\_DECORATION\_LINE\_THROUGH);
// 设置装饰线样式为 WAVY
OH\_Drawing\_SetTextStyleDecorationStyle(txtStyleWithDeco, TEXT\_DECORATION\_STYLE\_WAVY);
// 设置装饰线颜色
OH\_Drawing\_SetTextStyleDecorationColor(txtStyleWithDeco, OH\_Drawing\_ColorSetArgb(0xFF, 0x6F, 0xFF, 0xFF));

// 创建一个不带装饰线的 TextStyle 用于对比
OH\_Drawing\_TextStyle \*txtStyleNoDeco = OH\_Drawing\_CreateTextStyle();
// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_SetTextStyleColor(txtStyleNoDeco, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoDeco, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoDeco, FONT\_WEIGHT\_400);

// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 加入带有装饰线的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithDeco);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);

// 后续加入的不带装饰线的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoDeco);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放内存
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithDeco);
OH\_Drawing\_DestroyTextStyle(txtStyleNoDeco);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/_G2ILiKfSIa0n6o29BSYIw/zh-cn_image_0000002568899345.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=ADA6E51DF2BCFD32963EECDC5C737011B517607A0C9D2B571C187807216B9340)

#### \[h2\]字体特征

**字体特征**绘制专注于在文本渲染过程中对字体特性（如粗体、斜体、字体变种等）的处理，允许字体在不同的排版场景下表现出不同的效果，可用于增强文本的表现力，使其更符合设计和阅读需求。

常见的**FontFeature**包含有liga、frac、case等，需要对应的ttf文件支持才能正常使能。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_TextStyleAddFontFeature(OH\_Drawing\_TextStyle\* style, const char\* tag, int value) | 设置文本样式中指定字体特征是否启用。 |

示例及示意效果如下所示：

// 创建一个 TypographyStyle，创建 TypographyCreate 时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置文本对齐方式为居中
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// 设置文本内容
const char \*text = "1/2 1/3 1/4\\n";

// 设置文字颜色、大小、字重，不设置TextStyle无法绘制出文本
OH\_Drawing\_TextStyle \*txtStyleWithFeature = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyleWithFeature, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithFeature, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithFeature, FONT\_WEIGHT\_900);
// 设置启用frac font feature，此功能将斜线分隔的数字替换为普通（对角线）分数。
OH\_Drawing\_TextStyleAddFontFeature(txtStyleWithFeature, "frac", 1);

// 创建一个不带字体特征的 TextStyle 用于对比
OH\_Drawing\_TextStyle \*txtStyleNoFeature = OH\_Drawing\_CreateTextStyle();
// 设置文字颜色、大小、字重。不设置 TextStyle 无法绘制出文本
OH\_Drawing\_SetTextStyleColor(txtStyleNoFeature, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoFeature, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoFeature, FONT\_WEIGHT\_900);

// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 加入带有字体特征的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithFeature);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// 销毁之前创建的 TextStyle
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

// 后续加入的不带字体特征的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoFeature);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// 销毁之前创建的 TextStyle
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放内存
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithFeature);
OH\_Drawing\_DestroyTextStyle(txtStyleNoFeature);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/1PSX4cozS5WadhVQzmDR9w/zh-cn_image_0000002538019640.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=F05DB7E33FB3EDBAD3E95F18E431CE1871D7ED1C93CC459669BA7435DE5183C9)

#### \[h2\]可变字体

**可变字体**是一种在一个字体文件中包含多个字形变体的字体格式，允许在一个字体文件内灵活地调整字体的各种属性（如字重、字宽、斜体等）。

与传统字体文件（每种变体需要一个独立的文件）不同，可变字体在一个字体文件中包含多个变体轴，可通过使用可变字体实现文本渲染绘制时的平滑过渡。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_TextStyleAddFontVariation(OH\_Drawing\_TextStyle\* style, const char\* axis, const float value) | 添加可变字体属性。对应的字体文件（.ttf文件）需要支持可变调节，此接口才能生效。当对应的字体不支持可变调节时，此接口调用不生效。 |

示例及示意效果如下所示：

// 创建一个 TypographyStyle 创建 Typography 时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置文本对齐方式为居中
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// 设置文字内容
const char \*text = "Hello World Drawing\\n";

OH\_Drawing\_TextStyle \*txtStyleWithVar = OH\_Drawing\_CreateTextStyle();
// 设置可变字体的字重为800，在字体文件支持的情况下，还可以设置"slnt", "wdth"
OH\_Drawing\_TextStyleAddFontVariation(txtStyleWithVar, "wght", 800);
// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_SetTextStyleColor(txtStyleWithVar, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithVar, DIV\_TEN(width\_));
// 此处设置字重不生效，将被可变字体的字重覆盖
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithVar, FONT\_WEIGHT\_400);

// 创建一个不带可变字体的 TextStyle 用于对比
OH\_Drawing\_TextStyle \*txtStyleNoVar = OH\_Drawing\_CreateTextStyle();
// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_SetTextStyleColor(txtStyleNoVar, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoVar, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoVar, FONT\_WEIGHT\_400);

// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 加入带有可变字体的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithVar);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// 弹出之前创建的 TextStyle
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

// 后续加入的不带可变字体的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoVar);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// 弹出之前创建的 TextStyle
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放内存
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithVar);
OH\_Drawing\_DestroyTextStyle(txtStyleNoVar);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/7w8-t5AjRuiszcMVMDNGcw/zh-cn_image_0000002538179570.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=06221A2151B8B93B5B8345E68C54D893DDAC3CC015AC79A610331C748094D531)

#### \[h2\]文本阴影

**文本阴影**为文本提供了深度感，使得文本在背景上更具立体感。通常用于提升文本的视觉吸引力或增强可读性，尤其是在色彩对比度较低的场景下。

其中，TextShadow有三个属性，分别为阴影颜色color、阴影基于当前文本的偏移位置point、阴影半径blurRadius。

使用阴影效果需要在文本样式中设置对应的阴影效果数组，从而在文本绘制时生效。

| 接口定义 | 描述 |
| :-- | :-- |
| OH\_Drawing\_Point\* OH\_Drawing\_PointCreate(float x, float y) | 用于创建一个坐标点对象。 |
| OH\_Drawing\_TextShadow\* OH\_Drawing\_CreateTextShadow(void) | 创建指向字体阴影对象的指针。 |
| void OH\_Drawing\_SetTextShadow(OH\_Drawing\_TextShadow\* shadow, uint32\_t color, OH\_Drawing\_Point\* offset, double blurRadius) | 设置字体阴影对象的参数。 |
| void OH\_Drawing\_TextStyleAddShadow(OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextShadow\* shadow) | 字体阴影容器中添加字体阴影元素。 |
| void OH\_Drawing\_DestroyTextShadow(OH\_Drawing\_TextShadow\* shadow) | 释放被字体阴影对象占据的内存。 |

示例及示意效果如下所示：

// 创建一个 TypographyStyle 创建 Typography 时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置文本对齐方式为居中
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// 设置文本内容
const char \*text = "Hello World Drawing\\n";

// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_TextStyle \*txtStyleWithShadow = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyleWithShadow, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithShadow, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithShadow, FONT\_WEIGHT\_400);
// 设置阴影偏移量
OH\_Drawing\_Point \*offset = OH\_Drawing\_PointCreate(1, 1);
OH\_Drawing\_TextShadow \*shadow = OH\_Drawing\_CreateTextShadow();
double radius = 10.0;
// 为 TextShadow 设置样式
OH\_Drawing\_SetTextShadow(shadow, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00), offset, radius);
// 将 TextShadow 加入 TextStyle
OH\_Drawing\_TextStyleAddShadow(txtStyleWithShadow, shadow);

// 创建一个不带阴影的 TextStyle 用于对比
OH\_Drawing\_TextStyle \*txtStyleNoShadow = OH\_Drawing\_CreateTextStyle();
// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_SetTextStyleColor(txtStyleNoShadow, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoShadow, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoShadow, FONT\_WEIGHT\_400);

// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 加入带有阴影的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithShadow);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);

// 后续加入的不带阴影的文本样式
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoShadow);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放内存
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithShadow);
OH\_Drawing\_PointDestroy(offset);
OH\_Drawing\_DestroyTextShadow(shadow);
OH\_Drawing\_DestroyTextStyle(txtStyleNoShadow);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/EOPfSpi9T1Gr654jsgHRYQ/zh-cn_image_0000002569019357.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=DBE24CCADF119DF8C7399B1DC30443F1440EFAF1AC5C8CFE4402C958CA913FAB)

#### \[h2\]占位符

占位符绘制用于处理文本中占位符符号的渲染。

占位符也是用来实现图文混排的关键，是指在实际图像或内容注册之前，用来预先提供或替代某个位置的视觉元素。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_TypographyHandlerAddPlaceholder(OH\_Drawing\_TypographyCreate\* handler, OH\_Drawing\_PlaceholderSpan\* span) | 设置占位符。 |

示例及示意效果如下所示：

// 设置页面最大宽度
double maxWidth = width\_;
// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();

// 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);

// 设置文本内容
const char \*text = "Hello World Drawing\\n";

// 创建一个 TypographyStyle 创建 Typography 时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置文本对齐方式为居中
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);

// 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
OH\_Drawing\_TypographyCreate \*handlerWithPlaceholder = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// 创建一个 placeholder，并且初始化其成员变量
OH\_Drawing\_PlaceholderSpan placeholder;
placeholder.width = DIV\_TEN(width\_);
placeholder.height = DIV\_FIVE(width\_);
placeholder.alignment = ALIGNMENT\_ABOVE\_BASELINE; // 基线对齐策略
placeholder.baseline = TEXT\_BASELINE\_ALPHABETIC;  // 使用的文本基线类型
placeholder.baselineOffset = 0.0; // 相比基线的偏移量。只有对齐策略是 OFFSET\_AT\_BASELINE 时生效

// 将 placeholder 放在开头
OH\_Drawing\_TypographyHandlerAddPlaceholder(handlerWithPlaceholder, &placeholder);

// 将之前创建的 TextStyle 加入 handler
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerWithPlaceholder, txtStyle);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handlerWithPlaceholder, text);

OH\_Drawing\_Typography \*typographyWithPlaceholder = OH\_Drawing\_CreateTypography(handlerWithPlaceholder);
OH\_Drawing\_TypographyLayout(typographyWithPlaceholder, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typographyWithPlaceholder, cCanvas\_, 0, DIV\_TEN(width\_));

// 创建 OH\_Drawing\_TypographyCreate
OH\_Drawing\_TypographyCreate \*handlerNoPlaceholder = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// 将之前创建的 TextStyle 加入 handler
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerNoPlaceholder, txtStyle);
// 将文本添加到 handler 中
OH\_Drawing\_TypographyHandlerAddText(handlerNoPlaceholder, text);

OH\_Drawing\_Typography \*typographyNoPlaceholder = OH\_Drawing\_CreateTypography(handlerNoPlaceholder);

OH\_Drawing\_TypographyLayout(typographyNoPlaceholder, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typographyNoPlaceholder, cCanvas\_, 0, DIV\_TWO(width\_));

// 释放内存
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handlerWithPlaceholder);
OH\_Drawing\_DestroyTypographyHandler(handlerNoPlaceholder);
OH\_Drawing\_DestroyTypography(typographyWithPlaceholder);
OH\_Drawing\_DestroyTypography(typographyNoPlaceholder);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/iDdTQ7HaRFulQgA-rvxapw/zh-cn_image_0000002568899347.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=4A6FC10C1044989A8203E393A4C62AB57BDC9C0DA61F068D8346939DF2EF481C)

#### \[h2\]自动间距

使能自动间距，则会在文本排版时自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。例如，在中英文混排场景中，使能自动间距即可在中英文切换的地方自动添加额外间距，提升阅读体验。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyTextAutoSpace(OH\_Drawing\_TypographyStyle \*style, bool enableAutoSpace) | 设置文本排版时是否使能自动间距。默认不使能自动间距，一旦使能则会自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。 |

示例及示意效果如下所示：

// 创建一个TypographyStyle创建Typography时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 设置使能自动间距，默认为false
OH\_Drawing\_SetTypographyTextAutoSpace(typoStyle, true);
// 设置文字内容
const char \*text = "test测试©test©测。";

OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// 设置文字颜色、大小、字重，不设置TextStyle会使用TypographyStyle中的默认TextStyle
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));

// 创建FontCollection，FontCollection用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// 使用FontCollection和之前创建的TypographyStyle创建TypographyCreate。TypographyCreate用于创建Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 将文本样式添加到handler中
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// 将文本添加到handler中
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// 创建段落
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
// 将段落按照排版宽度进行排版
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 设置使能自动间距，用于对比
OH\_Drawing\_SetTypographyTextAutoSpace(typoStyle, false);

// 使用FontCollection和之前创建的TypographyStyle创建TypographyCreate。TypographyCreate用于创建Typography
OH\_Drawing\_TypographyCreate \*handlerWithoutAutoSpace = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 将文本样式添加到handlerWithoutAutoSpace中
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerWithoutAutoSpace, txtStyle);
// 将文本添加到handlerWithoutAutoSpace中
OH\_Drawing\_TypographyHandlerAddText(handlerWithoutAutoSpace, text);
// 创建段落
OH\_Drawing\_Typography \*typographyWithoutAutoSpace = OH\_Drawing\_CreateTypography(handlerWithoutAutoSpace);
// 将段落按照排版宽度进行排版
OH\_Drawing\_TypographyLayout(typographyWithoutAutoSpace, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typographyWithoutAutoSpace, cCanvas\_, 0, DIV\_FOUR(width\_));

// 释放内存
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypographyHandler(handlerWithoutAutoSpace);
OH\_Drawing\_DestroyTypography(typography);
OH\_Drawing\_DestroyTypography(typographyWithoutAutoSpace);

| 段落样式设置（自动间距） | 示意效果 |
| :-- | :-- |
| 不使能自动间距 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ZYflp9ZWSGSH3E6LRpxvNQ/zh-cn_image_0000002538019642.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=4F6595BD9239433274180148890070B123666CD97297B07CFFF878FCCBC69B47) |
| 使能自动间距 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/oVPDhlFTRmmovmG3QzjCTQ/zh-cn_image_0000002538179572.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=4CBCE4E97393674E12493CEC1D2701EC21E3EACD8BEAF979437F0EC721B0449E) |

#### \[h2\]渐变色

**渐变色**是一种在文字设计中广泛应用的视觉效果，通过在文字的不同部分应用不同的颜色，从而创造出从一种颜色平滑过渡到另一种颜色的效果。可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-c#着色器效果)。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTextStyleForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush) | 添加前景画刷，渐变着色器属性依附于前景画刷中。 |

示例及效果如下所示：

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// 设置文字大小
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
// 创建着色器对象，并设置颜色、变化起始点与结束点
OH\_Drawing\_Point \*startPt = OH\_Drawing\_PointCreate(0, 0);
// 结束点位于(900, 900)
OH\_Drawing\_Point \*endPt = OH\_Drawing\_PointCreate(900, 900);
uint32\_t colors\[\] = {0xFFFFFF00, 0xFFFF0000, 0xFF0000FF};
float pos\[\] = {0.0f, 0.5f, 1.0f};
// pos数组长度为3
OH\_Drawing\_ShaderEffect \*colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateLinearGradient(startPt, endPt, colors, pos, 3, OH\_Drawing\_TileMode::CLAMP);
// 创建画刷对象,并将着色器添加到画刷
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// 将画刷添加到文本样式中
OH\_Drawing\_SetTextStyleForegroundBrush(txtStyle, brush);
// 创建排版对象，并绘制
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
// 将段落按照排版宽度进行排版
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放对象
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/RnrVRXeKTrC1KcJaYPrBiw/zh-cn_image_0000002569019359.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=50988E0A763C39FC8F8EE2AA3CA33E451A880F3470A259D9D5FF720C529E4822)

#### \[h2\]垂直对齐

**垂直对齐**用于调整文本在一行中垂直方向的排版位置。开启行高缩放或行内存在不同字号文本混排时使能垂直对齐，可以让文本实现顶部对齐、居中对齐、底部对齐或基线对齐（默认）。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyVerticalAlignment(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TextVerticalAlignment align) | 设置文本垂直方向排版方式。 |

示例及效果如下所示：

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// 设置垂直对齐方式
OH\_Drawing\_SetTypographyVerticalAlignment(typoStyle,
                                          OH\_Drawing\_TextVerticalAlignment::TEXT\_VERTICAL\_ALIGNMENT\_CENTER);
// 设置文字大小
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
// 设置文字颜色
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// 创建排版对象，并绘制
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "VerticalAlignment-center";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
// 将段落按照排版宽度进行排版
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放对象
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

效果如下（黑框仅为展示文本绘制区域，实际不绘制）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/kVxfOuHLQqqx5Cet49JuiA/zh-cn_image_0000002568899335.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=B555C8EAD43FD26EA02B2FE5112A9EACC2AD9EA33B6666848B1407735B300CE2)

#### \[h2\]上下标

**上下标**能将文本作为上标或下标参与排版。一般用于数学公式、化学式等场景。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTextStyleBadgeType(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextBadgeType textBadgeType) | 使能上下标样式。 |

示例及效果如下所示：

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_TextStyle \*badgeTxtStyle = OH\_Drawing\_CreateTextStyle();
// 设置文字大小
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TWENTY(width\_));
OH\_Drawing\_SetTextStyleFontSize(badgeTxtStyle, DIV\_TWENTY(width\_));
// 设置文字颜色
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleColor(badgeTxtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// 使能文本上标
OH\_Drawing\_SetTextStyleBadgeType(badgeTxtStyle, OH\_Drawing\_TextBadgeType::TEXT\_SUPERSCRIPT);
// 创建排版对象，并绘制
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Mass-energy equivalence: E=mc";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, badgeTxtStyle);
const char \*badgeText = "2";
OH\_Drawing\_TypographyHandlerAddText(handler, badgeText);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
// 将段落按照排版宽度进行排版
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放对象
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTextStyle(badgeTxtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/E4KZOCA0R5-Dm8Yf_vZNvQ/zh-cn_image_0000002569019345.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=619FAF892816B885B0A5F8C8D721AC5AFBBA604E0B0DFA085C1C068531E56ADA)

#### \[h2\]高对比度

高对比度可将深色文字变黑、浅色文字变白。开发者可选择开启或关闭应用的高对比度文字渲染，或遵循系统设置中的高对比度文字配置。

| 接口定义 | 描述 |
| :-- | :-- |
| void OH\_Drawing\_SetTextHighContrast(OH\_Drawing\_TextHighContrast action) | 设置文字渲染高对比度模式。模式具体可参考[OH\_Drawing\_TextHighContrast](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-global-h#oh_drawing_texthighcontrast)。 |

示例及示意效果如下所示：

// 开启APP的文字渲染高对比模式，该模式的优先级要高于系统设置中的高对比度文字配置
OH\_Drawing\_SetTextHighContrast(TEXT\_APP\_ENABLE\_HIGH\_CONTRAST);
// 创建一个 TypographyStyle，创建 Typography 时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();

// 设置文字颜色、大小，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x6F, 0xFF, 0xFF));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));

// 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// 将之前创建的 TextStyle 加入 handler 中
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// 设置文本内容，并将文本添加到 handler 中
const char \*text = "Hello World Drawing\\n";
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 设置页面最大宽度
double maxWidth = width\_;
// 将段落按照排版宽度进行排版
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// 将文本绘制到画布上
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 释放内存
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

| 高对比度设置 | 示意效果 |
| :-- | :-- |
| 不开启高对比度 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/ZoEID1DST8qxv7RLRLmTUA/zh-cn_image_0000002568899349.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=101AB3829C34EF5E075E01A68B594623774CE29488467180D0B429EB629BF984) |
| 开启高对比度 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ndx9X7YnRGOIaU4FuOFePw/zh-cn_image_0000002538019644.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=AB8C73D72DC8DAC2E4BB088DABD82F93C86919002C5D3DEC9120F621717DA782) |

#### \[h2\]行高调整

调整行高可以改变文本行的垂直间距，行间距将变得更松散或更紧凑，可以显著改善文本垂直方向截断问题，使文本更易读。

当前行高调整方式包括两种：设置行高上限/下限和使用行高缩放系数。

**行高调整（方式一）**

从API version 21开始，支持为文本行设置行高上限与下限。

| 接口定义 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstyleattributedouble) | 传入id为OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM，设置行高上限。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstyleattributedouble) | 传入id为OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM，设置行高下限。 |

示例及效果如下所示：

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// 设置文字大小为50
OH\_Drawing\_SetTextStyleFontSize(txtStyle, 50);
// 设置文字颜色
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleAttributeDouble(txtStyle,
    OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM, 65); // 设置行高上限为65
OH\_Drawing\_SetTextStyleAttributeDouble(txtStyle,
    OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM, 65); // 设置行高下限为65
// 创建排版对象，并绘制
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World!";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 排版宽度为1000
OH\_Drawing\_TypographyLayout(typography, 1000);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 0);

// 释放对象
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

具体效果如下所示：

| 行高上限值 | 行高下限值 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| :-- | :-- | :-- |
| 65 | 65 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/zOyUqJETSWCm346nBVlBtg/zh-cn_image_0000002538179562.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=E63F7CBBFE6E747C6532EB8E9874C59A97B2E299B9507137A47A3D28BF02F01B) |
| 200 | 200 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/AhBGHIRMTeuvSsdHeoFFVQ/zh-cn_image_0000002569019347.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=BE8417D7ADFC405487BC6C331336BA40D811171338FE65DD9DE8B3308EEAEE3B) |

**行高调整（方式二）**

设置行高缩放系数。

| 接口定义 | 描述 |
| :-- | :-- |
| [void OH\_Drawing\_SetTextStyleFontHeight(OH\_Drawing\_TextStyle\* style, double fontHeight)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstylefontheight) | 使能行高缩放。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstyleattributeint) | 传入id为OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE，使能行高缩放样式。 |

示例及效果如下所示：

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// 设置文字大小为50
OH\_Drawing\_SetTextStyleFontSize(txtStyle, 50);
// 设置文字颜色
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// 设置行高缩放系数为1.5
OH\_Drawing\_SetTextStyleFontHeight(txtStyle, 1.5);
// 设置行高缩放样式（1代表行高缩放以字形高度作为缩放基数）
OH\_Drawing\_SetTextStyleAttributeInt(txtStyle,
    OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE, 1);
// 创建排版对象，并绘制
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World!";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 排版宽度为1000
OH\_Drawing\_TypographyLayout(typography, 1000);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 0);

// 释放对象
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

具体效果如下所示：

| 行高缩放样式 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| :-- | :-- |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/Tvu09oBIRB-6W0j2vH4yiA/zh-cn_image_0000002568899339.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=40B06209D9DB0632BFEFCF8B38C4D29408FD5995785C4D316E7456BE8835F751) |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_HEIGHT | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/9q_R__uNTNeVY3VUPGARZw/zh-cn_image_0000002538019634.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=0848274055E7AF7AAE65155BD42DE8D4F78B4D023E93663B9B05BC3D4BB4DE02) |

#### \[h2\]行间距调整

从API version 21开始，支持设置行间距可以改善文本行之间的距离，提高阅读体验。

| 接口定义 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double value)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settypographystyleattributedouble) | 传入id为OH\_Drawing\_TypographyStyleAttributeId::TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_SPACING，设置行间距。 |

示例及效果如下所示：

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_SetTypographyStyleAttributeDouble(typoStyle,
    OH\_Drawing\_TypographyStyleAttributeId::TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_SPACING, 100); // 设置行间距为100
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// 设置文字大小为50
OH\_Drawing\_SetTextStyleFontSize(txtStyle, 50);
// 设置文字颜色
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// 创建排版对象，并绘制
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World!";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// 排版宽度为200
OH\_Drawing\_TypographyLayout(typography, 200);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 0);

// 释放对象
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

具体效果如下所示：

| 上升部下降部开关 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| :-- | :-- |
| TEXT\_HEIGHT\_DISABLE\_ALL | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Pq2PK3g6Rb21bkYU7eMXpA/zh-cn_image_0000002538179564.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=E416478A83CB82D8E01BB5F0FD66B4D489EAA36FC28E1A3FD35C5E97CC5E3532) |
| TEXT\_HEIGHT\_ALL | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/2OlImb3XRLW17fd3OOmU0A/zh-cn_image_0000002569019349.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=996E8BF61DE1A69515E1A11ECEB2F66B7052B15DBBADB19C9C4EA6B469E558B7) |

#### 样式的拷贝、绘制与显示

支持拷贝文本样式、段落样式、阴影样式，以便快速复制相关样式作用到不同文字上。

| 接口定义 | 描述 |
| :-- | :-- |
| OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CopyTypographyStyle(OH\_Drawing\_TypographyStyle\* style) | 创建一个段落样式的对象副本，用于拷贝一个已有的段落样式对象。 |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CopyTextStyle(OH\_Drawing\_TextStyle\* style) | 创建一个文本样式的对象副本，用于拷贝一个已有的文本样式对象。 |
| OH\_Drawing\_TextShadow\* OH\_Drawing\_CopyTextShadow(OH\_Drawing\_TextShadow\* shadow) | 创建一个文本阴影的对象副本，用于拷贝一个已有的文本阴影对象。 |

示例及示意效果如下所示：

// 创建一个TypographyStyle，其中创建Typography时需要使用
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// 配置段落样式包括：使能自动间距、最大行数、省略号样式、省略号文本、对齐方式
// 使能自动间距
OH\_Drawing\_SetTypographyTextAutoSpace(typoStyle, true);
// 设置段落最大行数为3行
OH\_Drawing\_SetTypographyTextMaxLines(typoStyle, 3);
// 设置省略号模式为尾部省略号
OH\_Drawing\_SetTypographyTextEllipsisModal(typoStyle, ELLIPSIS\_MODAL\_TAIL);
// 设置省略号文本
OH\_Drawing\_SetTypographyTextEllipsis(typoStyle, "...");
// 设置对齐方式为居中对齐
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);

OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// 设置文字颜色、大小、字重，不设置TextStyle会使用TypographyStyle中的默认TextStyle
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
// 设置文本的装饰线
// 添加下划线
OH\_Drawing\_SetTextStyleDecoration(txtStyle, TEXT\_DECORATION\_UNDERLINE);
// 设置装饰线样式为波浪线样式
OH\_Drawing\_SetTextStyleDecorationStyle(txtStyle, TEXT\_DECORATION\_STYLE\_WAVY);
// 设置下划线粗细
OH\_Drawing\_SetTextStyleDecorationThicknessScale(txtStyle, 1);
// 设置下划线颜色为蓝色
OH\_Drawing\_SetTextStyleDecorationColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0xFF));

// 设置阴影的颜色、偏移量、模糊半径
// 创建阴影对象
OH\_Drawing\_TextShadow \*shadow = OH\_Drawing\_CreateTextShadow();
// 设置阴影偏移量为(5, 5)
OH\_Drawing\_Point \*offset = OH\_Drawing\_PointCreate(5, 5);
// 定义阴影模糊半径为4
double blurRadius = 4;
OH\_Drawing\_SetTextShadow(shadow, OH\_Drawing\_ColorSetArgb(0xFF, 0xFF, 0x00, 0xFF), offset, blurRadius);

// 拷贝阴影对象
OH\_Drawing\_TextShadow \*shadowCopy = OH\_Drawing\_CopyTextShadow(shadow);
// 将拷贝出的阴影添加到文本样式中
OH\_Drawing\_TextStyleAddShadow(txtStyle, shadowCopy);

// 创建FontCollection，FontCollection用于管理字体匹配逻辑
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();

// 使用FontCollection和之前创建的TypographyStyle创建TypographyCreate。TypographyCreate用于创建Typography
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// 将段落一文本样式添加到handler中
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// 将段落一文本添加到handler中
const char \*text = "The text style, paragraph style, and text shadow of the copied text will be exactly the same "
                   "as those of the original text.";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// 创建段落一，并将段落一按照排版宽度进行排版
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// 生成第二段文本，其中，文本样式和段落样式均由第一段文本拷贝而来
// 复制文本样式
OH\_Drawing\_TextStyle \*textStyleCopy = OH\_Drawing\_CopyTextStyle(txtStyle);
// 复制段落样式
OH\_Drawing\_TypographyStyle \*typographyStyleCopy = OH\_Drawing\_CopyTypographyStyle(typoStyle);

// 使用复制的样式创建段落二，后续可以观察段落一和段落二是否绘制效果一致
OH\_Drawing\_TypographyCreate \*handlerCopy = OH\_Drawing\_CreateTypographyHandler(typographyStyleCopy, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerCopy, textStyleCopy);
OH\_Drawing\_TypographyHandlerAddText(handlerCopy, text);
OH\_Drawing\_Typography \*typographyCopy = OH\_Drawing\_CreateTypography(handlerCopy);
OH\_Drawing\_TypographyLayout(typographyCopy, maxWidth);
OH\_Drawing\_TypographyPaint(typographyCopy, cCanvas\_, 0, DIV\_TWO(width\_));

// 释放内存
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);
// 拷贝的段落样式也需要释放内存
OH\_Drawing\_DestroyTypographyStyle(typographyStyleCopy);
// 拷贝的文本样式也需要释放内存
OH\_Drawing\_DestroyTextStyle(textStyleCopy);
OH\_Drawing\_DestroyTypographyHandler(handlerCopy);
OH\_Drawing\_DestroyTypography(typographyCopy);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Kb2cG172Q6K62Zkd7woE1A/zh-cn_image_0000002538179574.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=25A40CA1B8910A0C845A1C2E7CD4F9F644BB86D6F54E644695FE45C0541B23C1)
