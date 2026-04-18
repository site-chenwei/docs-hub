---
title: "使用主题字体（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "文本"
  - "字体管理"
  - "使用主题字体（C/C++）"
captured_at: "2026-04-17T01:36:08.834Z"
---

# 使用主题字体（C/C++）

#### 场景介绍

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。可以通过相关接口调用使能主题应用中的主题字体。

#### 实现机制

**图1** 主题字体的切换和使用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/IhASGhphRdu2kqWrKIwpYg/zh-cn_image_0000002538179546.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=B0A311553F6AE16392EB204FA584775BD7641068DFAEA45ED78DFA0D5D2EBA10)

针对主题字的切换使用，应用方应确保订阅主题字变更事件，当接收字体变更事件后，由应用方主动调用页面刷新才能实现主题字的切换，否则主题字只能在重启应用后才生效；主题字的绘制需要使用OH\_Drawing\_GetFontCollectionGlobalInstance来获取全局字体集对象，仅该接口返回的对象拥有主题字体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sCxUpExCSoCCrjPpSetztA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=0FDE4460396D715BABA84349BC43DDFFF2700FE32DB2CA0CBB6027DD11AD0D3E)

由OH\_Drawing\_CreateSharedFontCollection创建的字体集对象不包含主题字信息，无法用于绘制主题字。

#### 接口说明

注册使用主题字体的常用接口如下表所示，详细接口说明请参考[Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)。

| 接口名 | 描述 |
| :-- | :-- |
| OH\_Drawing\_FontCollection\* OH\_Drawing\_GetFontCollectionGlobalInstance(void) | 获取全局的字体集对象OH\_Drawing\_FontCollection。 |
| [onConfigurationUpdate()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability#abilityonconfigurationupdate) | 
系统配置更新时调用。

主题应用当前仅提供ArkTS接口发布变更事件，需要应用自行处理进行跨语言调用。

 |

#### 开发步骤

1.  请确保在设备系统**主题应用**中，能成功应用一项主题字体。
    
2.  在应用入口文件（默认工程中为EntryAbility.ets）中重写onConfigurationUpdate函数，以响应fontId变更，适配主题字体的切换和页面刷新，重写方式可参考[主题字变更事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-arkts#开发步骤)。
    
    系统配置信息（即示例中的newConfig）变化时，会自动触发onConfigurationUpdate函数。应用可从系统发送的配置信息获取fontId，通过判断是否与应用本地保存的fontId一致来识别主题字的切换。若不一致则刷新本地fontId，并调用C++代码刷新排版结果。从ArkTS到C++的调用通路需应用根据实际情况选取调用方式，本示例不作推荐。跨语言调用可参考[Node-API简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-introduction)。
    
3.  导入C++侧依赖，本步骤及之后均为主题字体在C++侧的使用
    
    在工程的src/main/cpp/CMakeLists.txt文件中添加以下lib。
    
    ```
    libnative_drawing.so
    ```
    
    导入头文件。
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_register\_font.h>
    
4.  创建字体管理器。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/M0VQz5SyS6WAZ9s4Y3yzbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=27F78B9698DB9DFA5348FD5017A2C76348EB1BF1C88FD222695CEE5AD3B313C0)
    
    注册主题字体作用于字体管理集全局对象，故必须使用OH\_Drawing\_GetFontCollectionGlobalInstance获取全局字体集对象进行绘制。如若使用OH\_Drawing\_CreateSharedFontCollection或OH\_Drawing\_CreateFontCollection创建字体集对象，无法使用主题字体。OH\_Drawing\_GetFontCollectionGlobalInstance获取的全局字体集不允许释放，释放会造成字体绘制紊乱问题。
    
    OH\_Drawing\_FontCollection \*fontCollection = OH\_Drawing\_GetFontCollectionGlobalInstance();
    
5.  OH\_Drawing\_SetTextStyleFontFamilies()接口可以用来指定字体家族名，从而实现使用指定字体。但使用主题字体，不需要使用OH\_Drawing\_SetTextStyleFontFamilies()接口指定字体，否则行为变更为优先使用指定字体，而不是主题字体。
    
    OH\_Drawing\_TextStyle \*myTextStyle = OH\_Drawing\_CreateTextStyle();
    // const char\* myFontFamilies\[\] = {"otherFontFamilyName"};
    // 注意不要使用此接口来指定字体
    // OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
6.  设置段落文本内容为"Hello World. \\nThis is the theme font."，此时该段落文本将应用主题字体。
    
    // 设置其他文本样式
    OH\_Drawing\_SetTextStyleColor(myTextStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
    // 设置字体大小为100.0
    OH\_Drawing\_SetTextStyleFontSize(myTextStyle, 100.0);
    // 创建一个段落样式对象，以设置排版风格
    OH\_Drawing\_TypographyStyle \*typographyStyle = OH\_Drawing\_CreateTypographyStyle();
    OH\_Drawing\_SetTypographyTextAlign(typographyStyle, TEXT\_ALIGN\_LEFT); // 设置段落样式为左对齐
    // 创建一个段落生成器
    OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typographyStyle, fontCollection);
    // 在段落生成器中设置文本样式
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, myTextStyle);
    // 在段落生成器中设置文本内容
    const char \*text = "Hello World. \\nThis is the theme font.";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    // 通过段落生成器生成段落
    OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
    

#### 效果展示

以下展示了在系统**主题应用**中切换使用不同主题字体后，对应的文字渲染效果。

不同主题字体显示效果不同，此处仅示意。

**图2** 主题字体1的效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/3ydhOdpJT9qQmACfTfxYZw/zh-cn_image_0000002538019620.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=B32138D164A86B6F5204442773011AA1D8147F0F74A0D19CA4CF1BB729E1A1B6)

**图3** 主题字体2的效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/dtHo5SwiRCuEjUXSMms9fA/zh-cn_image_0000002538179550.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=7F086FE998099609B8B93756D834F43D4BF15ADD05A3E628B153FE31DFBC1E0D)
