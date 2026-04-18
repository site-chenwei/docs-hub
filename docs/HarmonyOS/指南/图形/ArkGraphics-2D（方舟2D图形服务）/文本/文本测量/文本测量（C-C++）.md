---
title: "文本测量（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-measure-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "文本"
  - "文本测量"
  - "文本测量（C/C++）"
captured_at: "2026-04-17T01:36:08.874Z"
---

# 文本测量（C/C++）

#### 场景介绍

文本测量指的是在图形绘制中，对文本的尺寸和布局进行评估，计算文本在给定字体和样式下占用的空间（例如宽度、高度和其他相关信息）的过程。文本测量用于文本排版、布局、渲染以及调整文本显示的位置和大小等场景，便于更精准地控制与调整界面的布局和呈现，以达到设计预期。

当前主要支持以下方面的文本测量能力：

-   **文本宽度**：测量给定文本在特定字体、大小和样式下的水平长度。
    
-   **文本高度**：测量给定文本的垂直高度，通常涉及字体的上升线、下降线等。
    
-   **行间距**：测量多行文本之间的垂直距离，通常与字体的行距相关。
    
-   **字符间距**：测量单个字符之间的水平距离，通常与字形和字体设计有关。
    

#### 接口说明

文本测量中常用接口如下表所示，详细接口说明参考[drawing\_text\_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)。

| 接口名 | 描述 |
| :-- | :-- |
| double OH\_Drawing\_TypographyGetLongestLine(OH\_Drawing\_Typography\*) | 获取最长行的宽度，建议实际使用时将返回值向上取整。 |
| double OH\_Drawing\_TypographyGetLongestLineWithIndent(OH\_Drawing\_Typography\*) | 获取最长行的宽度（该宽度包含当前行缩进的宽度），建议实际使用时将返回值向上取整。 |
| size\_t OH\_Drawing\_TypographyGetLineCount (OH\_Drawing\_Typography\* ) | 获取文本行数。 |
| OH\_Drawing\_LineMetrics\* OH\_Drawing\_TypographyGetLineMetrics (OH\_Drawing\_Typography\* ) | 获取段落行的度量信息。包含行的高度、宽度、起始坐标等信息。 |
| double OH\_Drawing\_TextStyleGetLetterSpacing (OH\_Drawing\_TextStyle \*) | 获取文本的字符间距。 |

#### 开发步骤

1.  在工程的src/main/cpp/CMakeLists.txt文件中添加以下lib。
    
    ```
    libnative_drawing.so
    ```
    
2.  导入依赖的相关头文件。
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_text\_declaration.h>
    
3.  创建段落生成器ParagraphBuilder，并设置段落样式。
    
    // 创建文本样式，并设置字体大小为50
    OH\_Drawing\_SetTextStyleColor(myTextStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
    OH\_Drawing\_SetTextStyleFontSize(myTextStyle, 50.0);
    // 创建一个段落样式对象，以设置排版风格
    OH\_Drawing\_TypographyStyle \*typographyStyle = OH\_Drawing\_CreateTypographyStyle();
    // 设置段落样式的对齐方式为左对齐
    OH\_Drawing\_SetTypographyTextAlign(typographyStyle, TEXT\_ALIGN\_LEFT);
    // 创建一个段落生成器
    OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typographyStyle, fontCollection);
    // 在段落生成器中设置文本样式
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, myTextStyle);
    // 在段落生成器中添加文本内容
    const char \*text = "排版测量的文字度量信息";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    // 通过段落生成器生成段落
    OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
    
4.  调用排版接口并设置段落排版宽度，对段落进行塑型排版。
    
    // 对段落进行塑形排版，设置排版宽度为maxWidth
    OH\_Drawing\_TypographyLayout(typography, maxWidth);
    
5.  调用段落测量信息获取接口，获取指定数据。
    
    // case1: 获取排版后最长行行宽
    double longestLine = OH\_Drawing\_TypographyGetLongestLine(typography);
    DRAWING\_LOGI("第%{public}d行 longestLine: %{public}f", longestLine);
    
    // case2:获取排版后段落行数
    size\_t lineCnt = OH\_Drawing\_TypographyGetLineCount(typography);
    DRAWING\_LOGI("lineCnt: %{public}zu", lineCnt);
    
    // case3:获取段落每行的度量信息
    OH\_Drawing\_LineMetrics \*lineMetrics = OH\_Drawing\_TypographyGetLineMetrics(typography);
    int lineMetricsSize = OH\_Drawing\_LineMetricsGetSize(lineMetrics);
    for (int i = 0; i < lineMetricsSize; ++i) {
    // lineMetrics为经过排版测量的文字度量信息
    double curLineAscender = -lineMetrics\[i\].ascender;
    double curLineWidth = lineMetrics\[i\].width;
        DRAWING\_LOGI("第%{public}d行 lineMetrics ascender: %{public}f", i + 1, curLineAscender);
        DRAWING\_LOGI("第%{public}d行 lineMetrics width: %{public}f", i + 1, curLineWidth);
    }
    
    // case4:获取段落最长行宽度与带缩进最长行行宽
    double longestLineWithIndent = OH\_Drawing\_TypographyGetLongestLineWithIndent(typography);
    DRAWING\_LOGI("longestLineWithIndent: %{public}f", longestLineWithIndent);
    
    OH\_Drawing\_Font\_Metrics fontMetrics;
    // 获取文本字体属性
    bool result = OH\_Drawing\_TextStyleGetFontMetrics(typography, myTextStyle, &fontMetrics);
    DRAWING\_LOGI("result: %{public}zu, fontMetrics ascent: %{public}f" , result, fontMetrics.ascent);
    // 获取排版对象的指定行位置信息，该接口需要在OH\_Drawing\_TypographyLayout接口调用之后调用
    OH\_Drawing\_LineMetrics lineMetric;
    OH\_Drawing\_TypographyGetLineMetricsAt(typography, 0, &lineMetric);
    DRAWING\_LOGI("第1行 lineMetrics ascender: %{public}f", -lineMetric.ascender);
