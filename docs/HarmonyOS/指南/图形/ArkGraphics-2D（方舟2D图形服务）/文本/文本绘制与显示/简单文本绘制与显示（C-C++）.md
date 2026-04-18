---
title: "简单文本绘制与显示（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/simple-text-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "文本"
  - "文本绘制与显示"
  - "简单文本绘制与显示（C/C++）"
captured_at: "2026-04-17T01:36:08.962Z"
---

# 简单文本绘制与显示（C/C++）

#### 场景介绍

在一个简单的用户界面中，可能只需要展示几行静态文本，例如标签、按钮上的文字、菜单项或状态栏中的提示信息。此时，开发者只需要选择合适的字体、大小和颜色即可完成渲染。

#### 接口说明

| 接口定义 | 描述 |
| :-- | :-- |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void) | 创建指向OH\_Drawing\_TextStyle对象的指针。 |
| void OH\_Drawing\_SetTextStyleFontSize(OH\_Drawing\_TextStyle\* style, double fontSize) | 设置字号。 |
| void OH\_Drawing\_SetTextStyleFontWeight(OH\_Drawing\_TextStyle\* style, int fontWeight) | 设置字重。目前只有系统默认字体支持字重的调节，其他字体设置字重值小于semi-bold时字体粗细无变化，当设置字重值大于等于semi-bold时可能会触发伪加粗效果。 |

#### 开发步骤

1.  创建Canvas画布对象，画布Canvas对象创建方法具体可见[画布的获取与绘制结果的显示](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c)。
    
2.  初始化段落样式，设置文本对齐方式为居中对齐。
    
    // 创建一个 TypographyStyle 创建 Typography 时需要使用
    OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
    // 设置文本对齐方式为居中
    OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
    
3.  初始化文本样式，此处设置字体颜色为纯黑色，字体大小为60，字重为400。
    
    // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
    OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
    OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
    OH\_Drawing\_SetTextStyleFontSize(txtStyle, 60);
    OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);
    
4.  初始化段落对象，并添加文本。
    
    // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
    OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateFontCollection();
    // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
    OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
    
    // 将之前创建的 TextStyle 加入 handler 中
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
    // 设置文本内容，并将文本添加到 handler 中
    const char \*text = "Hello World Drawing\\n";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    
    OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
    
5.  排版段落并进行文本绘制。
    
    // 设置页面最大宽度
    double maxWidth = width\_;
    OH\_Drawing\_TypographyLayout(typography, maxWidth);
    // 将文本绘制到画布上
    OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 100);
    
6.  释放内存
    
    // 释放内存
    OH\_Drawing\_DestroyTypographyStyle(typoStyle);
    OH\_Drawing\_DestroyTextStyle(txtStyle);
    OH\_Drawing\_DestroyFontCollection(fc);
    OH\_Drawing\_DestroyTypographyHandler(handler);
    OH\_Drawing\_DestroyTypography(typography);
    

#### 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/FCH-2hSFSkyZPyMAUwRLzw/zh-cn_image_0000002538019636.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=446F941C40184586D35B077A73D4D7EAB76D09692BAF5C1686629273C645EBD5)
