---
title: "Text组件的文本绘制与显示"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-styled-string"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (基于NDK构建UI)"
  - "使用文本"
  - "Text组件的文本绘制与显示"
captured_at: "2026-04-17T01:35:39.837Z"
---

# Text组件的文本绘制与显示

部分框架或应用具备自研的文字排版能力，在移植时，这些能力会被对接到[方舟2D图形服务的文本引擎](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-c)。为了避免开发者重复开发文本组件，Text组件提供了接口[NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype)，可以直接渲染方舟文本引擎生成的文本。

以下场景基于[接入ArkTS页面章节](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)，阐述了如何创建字体引擎文本，并利用[Text组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodetype)进行渲染显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/r2r9qXhbR8SUnYNmPmpqhw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=73D5CACF726C05FC4026BE33EDC87303534BA910C85470835977D159C63748E6)

涉及字体引擎的接口，需在CMakeLists.txt中添加target\_link\_libraries(entry PUBLIC libnative\_drawing.so)，否则链接阶段会报错。

下图展示了 NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING 接口的主要使用流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/Z6-ImHdaRxqnnBhvuQwvXQ/zh-cn_image_0000002568898695.png?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=6953846B4AF273C48BF2FD11F50E785D8A1FFEFAA13AB03C1531CC176963C411)

#### 创建Text组件

创建文本组件时，无需配置文字颜色、字体大小等样式属性，因为这些属性通过字体引擎接口设置。但仍需设置基础的[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype)，如宽度和高度。如果不指定，组件自动适应文本的宽度和高度。

ArkUI\_NativeNodeAPI\_1 \*nodeApi = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
    OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
if (nodeApi == nullptr) {
    return;
}
// ···
// 创建Text组件
ArkUI\_NodeHandle text = nodeApi->createNode(ARKUI\_NODE\_TEXT);
ArkUI\_NumberValue textWidth\[\] = {{.f32 = 300}};
ArkUI\_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
nodeApi->setAttribute(text, NODE\_WIDTH, &textWidthItem);
ArkUI\_NumberValue textHeight\[\] = {{.f32 = 100}};
ArkUI\_AttributeItem textHeightItem = {.value = textHeight, .size = 1};
nodeApi->setAttribute(text, NODE\_HEIGHT, &textHeightItem);

#### 设置段落与文本样式

-   设置段落样式
    
    段落样式定义了一段文字的整体属性，例如最大显示行数、文字方向等。以下代码示例设置了文字居中，最大行数限制为10。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/8XUn59itS7eQIX3_QEDXcg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=0101E593357B0EFC6E6A913655E9D15BE0DD4C4A3B0630A07670FB0EDC439208)
    
    OH\_Drawing\_前缀的接口由方舟字体引擎提供，参考[简单文本绘制与显示（C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/simple-text-c)、[复杂文本绘制与显示（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-c)。
    
    ```
    OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
    OH_Drawing_SetTypographyTextAlign(typographyStyle, OH_Drawing_TextAlign::TEXT_ALIGN_CENTER);
    OH_Drawing_SetTypographyTextMaxLines(typographyStyle, NUM_10);
    ```
    
-   设置文本样式
    
    不同内容的文本可以设置不同的文本样式，但必须按照以下三个接口的逻辑调用顺序进行设置，否则将无法生效。
    
    1.  [OH\_ArkUI\_StyledString\_PushTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_styledstring_pushtextstyle)：将文字样式推入栈中。
    2.  [OH\_ArkUI\_StyledString\_AddText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_styledstring_addtext)：添加要修改样式的文字内容。
    3.  [OH\_ArkUI\_StyledString\_PopTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_styledstring_poptextstyle)：将文字样式弹出栈。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/MCTxdxSpQquzW-j7qeYkSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=898D3A68E5C5ECEA058024BA979C1B8CCE7B2411F2B9ABF7A81D52C3F3D30A19)
    
    OH\_ArkUI\_StyledString\_前缀的接口由Text组件提供。
    
    OH\_Drawing\_前缀的接口由方舟字体引擎提供，参考[简单文本绘制与显示（C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/simple-text-c)、[复杂文本绘制与显示（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-c)。
    
    [OH\_Drawing\_CreateTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_createtextstyle)创建文本样式。设置“Hello”字体大小28px，颜色为0xFF707070。设置“World!”字体大小为28px，颜色为0xFF2787D9。
    
    ```
    ArkUI_StyledString *styledString = OH_ArkUI_StyledString_Create(typographyStyle, OH_Drawing_CreateFontCollection());
    // 创建文本样式，设置字体和颜色。
    OH_Drawing_TextStyle *textStyle = OH_Drawing_CreateTextStyle();
    OH_Drawing_SetTextStyleFontSize(textStyle, NUM_28);
    OH_Drawing_SetTextStyleColor(textStyle, OH_Drawing_ColorSetArgb(0xFF, 0x70, 0x70, 0x70));
    // 文本样式的设置顺序push -> add -> pop.
    OH_ArkUI_StyledString_PushTextStyle(styledString, textStyle);
    OH_ArkUI_StyledString_AddText(styledString, "Hello");
    OH_ArkUI_StyledString_PopTextStyle(styledString);
    // ···
    // 设置不同样式的文字
    OH_Drawing_TextStyle *worldTextStyle = OH_Drawing_CreateTextStyle();
    OH_Drawing_SetTextStyleFontSize(worldTextStyle, NUM_28);
    OH_Drawing_SetTextStyleColor(worldTextStyle, OH_Drawing_ColorSetArgb(0xFF, 0x27, 0x87, 0xD9));
    OH_ArkUI_StyledString_PushTextStyle(styledString, worldTextStyle);
    OH_ArkUI_StyledString_AddText(styledString, "World!");
    OH_ArkUI_StyledString_PopTextStyle(styledString);
    ```
    

#### 添加占位

占位保留指定大小的空白区域，此区域不绘制文字，但参与布局测量，影响文字排版。

行高是文字高度与占位高度中的较大值。

以下示例展示在Hello与World!中间插入占位。

OH\_Drawing\_TextStyle \*textStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleFontSize(textStyle, NUM\_28);
OH\_Drawing\_SetTextStyleColor(textStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x70, 0x70, 0x70));
// 文本样式的设置顺序push -> add -> pop.
OH\_ArkUI\_StyledString\_PushTextStyle(styledString, textStyle);
OH\_ArkUI\_StyledString\_AddText(styledString, "Hello");
OH\_ArkUI\_StyledString\_PopTextStyle(styledString);
// 添加占位，此区域内不会绘制文字，可以在此位置挂载Image组件实现图文混排。
OH\_Drawing\_PlaceholderSpan placeHolder{.width = 100, .height = 100};
OH\_ArkUI\_StyledString\_AddPlaceholder(styledString, &placeHolder);
// 设置不同样式的文字
OH\_Drawing\_TextStyle \*worldTextStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleFontSize(worldTextStyle, NUM\_28);
OH\_Drawing\_SetTextStyleColor(worldTextStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x27, 0x87, 0xD9));
OH\_ArkUI\_StyledString\_PushTextStyle(styledString, worldTextStyle);
OH\_ArkUI\_StyledString\_AddText(styledString, "World!");
OH\_ArkUI\_StyledString\_PopTextStyle(styledString);

#### 文本布局与绘制

-   文本布局
    
    文字样式和内容设置完成后，调用字体引擎接口[OH\_Drawing\_TypographyLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_typographylayout)对文本进行布局，传入最大宽度。超过此宽度的文字会自动换行。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/y1CnKzs9TluPLI9xqgoTog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=17A9391E173F4B0A8AD03243944589F0A5FBBB9DB3E4C0F40A62BC6DDEF418FD)
    
    未经过布局的文本无法显示。
    
    OH\_Drawing\_Typography \*typography = OH\_ArkUI\_StyledString\_CreateTypography(styledString);
    // 字体引擎布局方法，需传入一个宽度，此宽度需与Text组件宽度匹配。
    // 布局宽度 = Text组件宽度 - (左padding + 右padding)
    OH\_Drawing\_TypographyLayout(typography, NUM\_400);
    
-   文本绘制
    
    文本绘制由字体引擎与图形交互完成，无需额外设置。Text组件会在ArkUI渲染机制下，在组件触发绘制时调用字体引擎绘制接口。此处仅需将已创建的StyledString对象传递给已创建的Text组件。
    
    ArkUI\_AttributeItem styledStringItem = {.object = styledString};
    // 布局完成后，通过NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING设置给Text组件。
    nodeApi->setAttribute(text, NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING, &styledStringItem);
    

#### 销毁对象

Text组件不对本文涉及的任何对象的生命周期进行管理，需由开发者自行负责。字体引擎接口均配有相应的销毁方法。

OH\_Drawing\_DestroyTextStyle(OH\_Drawing\_TextStyle \*style)：销毁文本样式对象。

OH\_Drawing\_DestroyTypographyStyle(OH\_Drawing\_TypographyStyle \*style)：销毁段落样式对象。

当Text组件仍在界面上显示时，此时释放会导致文字无法绘制。在实际业务场景下需确保Text组件不再使用时才释放。

相关字体引擎销毁的接口请参考[OH\_Drawing\_DestroyTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_destroytextstyle) 和 [OH\_Drawing\_DestroyTypographyStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_destroytypographystyle)。

Text组件提供[OH\_ArkUI\_StyledString\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_styledstring_destroy)，用于销毁属性字符串对象。

#### 完整示例

本篇示例仅提供核心接口的调用方法，完整的示例工程请参考[StyledStringNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/StyledStringNDK)。

#include "manager.h"
#include <sstream>
#include <arkui/native\_interface.h>
#include <arkui/styled\_string.h>
// ···
#include <native\_drawing/drawing\_font\_collection.h>
#include <native\_drawing/drawing\_text\_declaration.h>

namespace NativeNode::Manager {
constexpr int32\_t NUM\_10 = 10;
constexpr int32\_t NUM\_28 = 28;
constexpr int32\_t NUM\_400 = 400;
// ···
void NodeManager::CreateNativeNode()
{
    // ···
    ArkUI\_NativeNodeAPI\_1 \*nodeApi = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
    if (nodeApi == nullptr) {
        return;
    }
    // 创建一个Column容器组件
    ArkUI\_NodeHandle column = nodeApi->createNode(ARKUI\_NODE\_COLUMN);
    ArkUI\_NumberValue colWidth\[\] = {{.f32 = 300}};
    ArkUI\_AttributeItem widthItem = {.value = colWidth, .size = 1};
    nodeApi->setAttribute(column, NODE\_WIDTH, &widthItem);
    // 创建Text组件
    ArkUI\_NodeHandle text = nodeApi->createNode(ARKUI\_NODE\_TEXT);
    ArkUI\_NumberValue textWidth\[\] = {{.f32 = 300}};
    ArkUI\_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
    nodeApi->setAttribute(text, NODE\_WIDTH, &textWidthItem);
    ArkUI\_NumberValue textHeight\[\] = {{.f32 = 100}};
    ArkUI\_AttributeItem textHeightItem = {.value = textHeight, .size = 1};
    nodeApi->setAttribute(text, NODE\_HEIGHT, &textHeightItem);
    ArkUI\_NumberValue borderWidth\[\] = {{.f32 = 1}};
    ArkUI\_AttributeItem borderWidthItem = {.value = borderWidth, .size = 1};
    nodeApi->setAttribute(text, NODE\_BORDER\_WIDTH, &borderWidthItem);
    
    // OH\_Drawing\_开头的API是字体引擎提供的，typographyStyle表示段落样式。
    OH\_Drawing\_TypographyStyle \*typographyStyle = OH\_Drawing\_CreateTypographyStyle();
    OH\_Drawing\_SetTypographyTextAlign(typographyStyle, OH\_Drawing\_TextAlign::TEXT\_ALIGN\_CENTER);
    OH\_Drawing\_SetTypographyTextMaxLines(typographyStyle, NUM\_10);
    // 创建 ArkUI\_StyledString。
    ArkUI\_StyledString \*styledString = OH\_ArkUI\_StyledString\_Create(typographyStyle, OH\_Drawing\_CreateFontCollection());
    // 创建文本样式，设置字体和颜色。
    OH\_Drawing\_TextStyle \*textStyle = OH\_Drawing\_CreateTextStyle();
    OH\_Drawing\_SetTextStyleFontSize(textStyle, NUM\_28);
    OH\_Drawing\_SetTextStyleColor(textStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x70, 0x70, 0x70));
    // 文本样式的设置顺序push -> add -> pop.
    OH\_ArkUI\_StyledString\_PushTextStyle(styledString, textStyle);
    OH\_ArkUI\_StyledString\_AddText(styledString, "Hello");
    OH\_ArkUI\_StyledString\_PopTextStyle(styledString);
    // 添加占位，此区域内不会绘制文字，可以在此位置挂载Image组件实现图文混排。
    OH\_Drawing\_PlaceholderSpan placeHolder{.width = 100, .height = 100};
    OH\_ArkUI\_StyledString\_AddPlaceholder(styledString, &placeHolder);
    // 设置不同样式的文字
    OH\_Drawing\_TextStyle \*worldTextStyle = OH\_Drawing\_CreateTextStyle();
    OH\_Drawing\_SetTextStyleFontSize(worldTextStyle, NUM\_28);
    OH\_Drawing\_SetTextStyleColor(worldTextStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x27, 0x87, 0xD9));
    OH\_ArkUI\_StyledString\_PushTextStyle(styledString, worldTextStyle);
    OH\_ArkUI\_StyledString\_AddText(styledString, "World!");
    OH\_ArkUI\_StyledString\_PopTextStyle(styledString);
    // 依赖StyledString对象创建字体引擎的Typography，此时它已经包含了设置的文本及其样式。
    OH\_Drawing\_Typography \*typography = OH\_ArkUI\_StyledString\_CreateTypography(styledString);
    // 字体引擎布局方法，需传入一个宽度，此宽度需与Text组件宽度匹配。
    // 布局宽度 = Text组件宽度 - (左padding + 右padding)
    OH\_Drawing\_TypographyLayout(typography, NUM\_400);
    ArkUI\_AttributeItem styledStringItem = {.object = styledString};
    // 布局完成后，通过NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING设置给Text组件。
    nodeApi->setAttribute(text, NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING, &styledStringItem);

    // 资源释放，应用侧可以自由决定何时释放。
    OH\_ArkUI\_StyledString\_Destroy(styledString);
    // Text作为Column子组件
    nodeApi->addChild(column, text);
    // Column作为XComponent子组件
    OH\_NativeXComponent\_AttachNativeRootNode(xComponent\_, column);
}
} // namespace NativeNode::Manager

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/oS3hbXojThe7ThnVrUXckw/zh-cn_image_0000002538018990.png?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=C93EB0A9EB8AB3C168532079139571FAF4A5A3D2FF04D2AED3CF88C6D3612AA2)
