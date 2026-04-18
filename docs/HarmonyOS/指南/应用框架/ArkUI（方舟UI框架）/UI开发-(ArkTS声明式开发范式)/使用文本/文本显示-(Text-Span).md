---
title: "文本显示 (Text/Span)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "使用文本"
  - "文本显示 (Text/Span)"
captured_at: "2026-04-17T01:35:37.675Z"
---

# 文本显示 (Text/Span)

Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于展示行内文本。

具体用法请参考[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)组件的API文档。

常见问题请参考[文本显示（Text/Span）常见问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq#文本显示textspan常见问题)。

#### 创建文本

Text可通过以下两种方式来创建：

-   string字符串。
    
    Text('我是一段文本')
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/GYg3Krt_RQa8gb96JQI2vg/zh-cn_image_0000002538018714.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C46A79751ADC3D44ED9E38B8A175C8125ACA3E02FBDD8A49D9F8450766C71187)

-   引用Resource资源。
    
    资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json，具体内容如下：
    
    ```json
    {
      "string": [
        {
          "name": "module_desc",
          "value": "模块描述"
        }
      ]
    }
    ```
    
    // 请将$r('app.string.module\_desc')替换为实际资源文件，在本示例中该资源文件的value值为"模块描述"
    Text($r('app.string.module\_desc'))
      .baselineOffset(0)
      .fontSize(30)
      .border({ width: 1 })
      .padding(10)
      .width(300)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/qcGCovMrT7OES_140ksFew/zh-cn_image_0000002538178642.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=31484DB6724A9E2DFA457DE6FF7372B530CFCD53EF4BC9A757A467B24DC7C5CA)
    

#### 添加子组件

[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)只能作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

-   创建Span。
    
    Span组件需嵌入在Text组件中才能显示，单独使用时不会显示任何内容。Text与Span同时配置文本内容时，Span内容将覆盖Text内容。
    
    // 请将$r('app.string.TextSpan\_textContent\_text')替换为实际资源文件，在本示例中该资源文件的value值为"我是Text"
    Text($r('app.string.TextSpan\_textContent\_text')) {
      // 请将$r('app.string.TextSpan\_textContent\_span')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span"
      Span($r('app.string.TextSpan\_textContent\_span'))
    }
    .padding(10)
    .borderWidth(1)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/6Gcvb-tJTiK_z8ksXgR49w/zh-cn_image_0000002569018431.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=5FC70259F320702895AD0B951CEC71D22CE7529F2A2C60F432A355AC27F33D0A)
    
-   设置文本装饰线及颜色。
    
    通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#decoration)设置文本装饰线及颜色。
    
    Text() {
      // 请将$r('app.string.TextSpan\_textContent\_span\_one')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span1，"
      Span($r('app.string.TextSpan\_textContent\_span\_one'))
        .fontSize(16)
        .fontColor(Color.Grey)
        .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
      // 请将$r('app.string.TextSpan\_textContent\_span\_two')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span2"
      Span($r('app.string.TextSpan\_textContent\_span\_two'))
        .fontColor(Color.Blue)
        .fontSize(16)
        .fontStyle(FontStyle.Italic)
        .decoration({ type: TextDecorationType.Underline, color: Color.Black })
      // 请将$r('app.string.TextSpan\_textContent\_span\_three')替换为实际资源文件，在本示例中该资源文件的value值为"，我是Span3"
      Span($r('app.string.TextSpan\_textContent\_span\_three'))
        .fontSize(16)
        .fontColor(Color.Grey)
        .decoration({ type: TextDecorationType.Overline, color: Color.Green })
    }
    .borderWidth(1)
    .padding(10)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/nWvnRRycSm2RCTqKe8887Q/zh-cn_image_0000002568898421.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=447905690298981F785F18C1F59DE011783688F7997BCF46B49548F03FE1FC82)
    
-   通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#textcase)设置文字一直保持大写或者小写状态。
    
    Text() {
      Span('I am Upper-span').fontSize(12)
        .textCase(TextCase.UpperCase)
    }
    .borderWidth(1)
    .padding(10)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/FUBLbKTQTi6uCSr191xbTg/zh-cn_image_0000002538018716.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D7DD3CA91DC81F9E566E097BACBC8CC4403A22177F793F457DFA649EEC2C2817)
    
-   添加事件。
    
    由于Span组件无尺寸信息，仅支持添加点击事件[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、悬浮事件[onHover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover#onhover)。
    
    // xxx.ets
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    @Entry
    @Component
    export struct TextSpanOnHover {
      @State textStr1: string = '';
      @State textStr2: string = '';
    
      build() {
        NavDestination() {
          Row() {
            Column() {
              Text() {
                Span('I am Upper-span')
                  .textCase(TextCase.UpperCase)
                  .fontSize(30)
                  .onClick(() => {
                    hilog.info(0x0000, 'Sample\_TextComponent', 'Span onClick is triggering');
                    this.textStr1 = 'Span onClick is triggering';
                  })
                  .onHover(() => {
                    hilog.info(0x0000, 'Sample\_TextComponent', 'Span onHover is triggering');
                    this.textStr2 = 'Span onHover is triggering';
                  })
              }
    
              Text('onClick：' + this.textStr1)
                .fontSize(20)
              Text('onHover：' + this.textStr2)
                .fontSize(20)
            }.width('100%')
          }
          .height('100%')
        }
        // ···
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/FvHAw9uERJ2JbX3jv_g4jQ/zh-cn_image_0000002538178644.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=7A9487CABA0D0244414EB3DEEE84DC9676BE86684A455A08D69504D305FB3D9E)
    

#### 创建自定义文本样式

Text组件支持创建自定义文本样式，以下为修改文本样式的主要属性。

| 属性名称 | 功能描述 |
| :-- | :-- |
| baselineOffset | 设置文本基线的偏移量。 |
| contentTransition | 设置数字翻牌效果。 |
| copyOption | 设置文本是否可复制粘贴。 |
| decoration | 设置文本装饰线样式，如类型、颜色及其粗细。 |
| enableAutoSpacing | 设置是否开启中文与西文的自动间距。 |
| enableDataDetector | 设置是否进行文本特殊实体识别。 |
| font | 设置文本字体相关属性。 |
| fontColor | 设置文本字体颜色。 |
| fontFamily | 设置文本字体族。 |
| fontFeature | 设置文字特性效果，比如数字等宽的特性。 |
| fontSize | 设置文本字体大小。 |
| fontStyle | 设置文本字体风格。 |
| fontWeight | 设置文本字体粗细。 |
| halfLeading | 设置文本是否将行间距平分至行的顶部与底部。 |
| heightAdaptivePolicy | 设置文本自适应布局调整字号的方式。 |
| letterSpacing | 设置文本字符间距。 |
| lineHeight | 设置文本行高。 |
| lineSpacing | 设置文本的行间距。 |
| marqueeOptions | 设置跑马灯配置项，如开关、步长、循环次数、方向等。 |
| maxFontSize | 设置自适应字体最大尺寸。 |
| maxLines | 设置文本最大显示行数。 |
| minFontSize | 设置自适应字体最小尺寸。 |
| optimizeTrailingSpace | 控制每行末尾空格的优化。 |
| privacySensitive | 设置是否支持卡片敏感隐私信息。 |
| shaderStyle | 设置文本渐变色样式。 |
| textCase | 设置文本大小写转换。 |
| textAlign | 设置文本段落在水平方向的对齐方式。 |
| textIndent | 设置首行文本缩进。 |
| textOverflow | 控制文本超长处理方式。 |
| textSelectable | 设置文本是否可选择。 |
| textVerticalAlign | 设置文本段落在垂直方向的对齐方式。 |
| wordBreak | 设置断行规则。 |

下面对常用的接口进行举例说明。

-   通过[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)属性设置文本对齐样式。
    
    // 请将$r('app.string.TextAlign\_Start')替换为实际资源文件，在本示例中该资源文件的value值为"左对齐"
    Text($r('app.string.TextAlign\_Start'))
      .width(300)
      .textAlign(TextAlign.Start)
      .border({ width: 1 })
      .padding(10)
    // 请将$r('app.string.TextAlign\_Center')替换为实际资源文件，在本示例中该资源文件的value值为"中间对齐"
    Text($r('app.string.TextAlign\_Center'))
      .width(300)
      .textAlign(TextAlign.Center)
      .border({ width: 1 })
      .padding(10)
    // 请将$r('app.string.TextAlign\_End')替换为实际资源文件，在本示例中该资源文件的value值为"右对齐"
    Text($r('app.string.TextAlign\_End'))
      .width(300)
      .textAlign(TextAlign.End)
      .border({ width: 1 })
      .padding(10)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/FT0p5G8cQWKKSICrEUTUgQ/zh-cn_image_0000002569018433.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=50DECCFCF9A4404EE9D9312CBE91D7E410123266E808E151C7C9A838C1CEF538)
    
-   通过[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)属性控制文本超长处理，textOverflow需配合[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)一起使用（默认情况下文本自动折行）。从API version 18开始，文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。
    
    Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +
      'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +
      'of textOverflow to None text content.')
      .width(250)
      .textOverflow({ overflow: TextOverflow.None })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
    // 'app.string.CustomTextStyle\_textContent\_epsis'资源文件中的value值为
    // '我是超长文本，超出的部分显示省略号 I am an extra long text, with ellipses displayed for any excess。'
    Text($r('app.string.CustomTextStyle\_textContent\_epsis'))
      .width(250)
      .textOverflow({ overflow: TextOverflow.Ellipsis })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
    // 'app.string.CustomTextStyle\_textContent\_marq'资源文件中的value值为
    // '当文本溢出其尺寸时，文本将滚动显示
    // When the text overflows its dimensions,the text will scroll for displaying.'
    Text($r('app.string.CustomTextStyle\_textContent\_marq'))
      .width(250)
      .textOverflow({ overflow: TextOverflow.MARQUEE })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
    // 'app.string.CustomTextStyle\_textContent\_marq\_def'资源文件中的value值为
    // '当文本溢出其尺寸时，文本将滚动显示，支持设置跑马灯配置项
    // When the text overflows its dimensions, the text will scroll for displaying.'
    Text($r('app.string.CustomTextStyle\_textContent\_marq\_def'))
      .width(250)
      .textOverflow({ overflow: TextOverflow.MARQUEE })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .marqueeOptions({
        start: true,
        fromStart: true,
        step: 6,
        loop: -1,
        delay: 0,
        fadeout: false,
        marqueeStartPolicy: MarqueeStartPolicy.DEFAULT
      })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/XesJ8EEFSKGteyPw6s7DwQ/zh-cn_image_0000002568898423.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=31561BDF2753034840973A66E5ECAF922BB98E0C430C3714E05707CD5F621FB6)
    
-   通过[lineHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#lineheight)属性设置文本行高。
    
    Text('This is the text with the line height set. This is the text with the line height set.')
      .width(300).fontSize(12).border({ width: 1 }).padding(10)
    Text('This is the text with the line height set. This is the text with the line height set.')
      .width(300)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .lineHeight(20)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Vnt4jV9KSY-EqSiCwXD80Q/zh-cn_image_0000002538018718.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=79660145D78C6559A98D69896E18D294810B650ABE35DE8DCE51C23B3FFF8532)
    
-   通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#decoration)属性设置文本装饰线样式、颜色及其粗细。
    
    Text('This is the text')
      .decoration({
        type: TextDecorationType.LineThrough,
        color: Color.Red
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Overline,
        color: Color.Red
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Red
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.DASHED
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.DOTTED
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.DOUBLE
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.WAVY,
        thicknessScale: 4
      })
      .borderWidth(1).padding(15).margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/2FTi1prsQB2n3RGzXI954w/zh-cn_image_0000002538178646.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=EB1E0FF16DBFD0507610B947AE1CB7D8A81EBE0C7A8DA716EBF5E5DC86879D2D)
    
-   通过[baselineOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#baselineoffset)属性设置文本基线的偏移量。
    
    Text('This is the text content with baselineOffset 0.')
      .baselineOffset(0)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with baselineOffset 30.')
      .baselineOffset(30)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with baselineOffset -20.')
      .baselineOffset(-20)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/J-4wSv7IShWEV8sPvwba6A/zh-cn_image_0000002569018435.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3864815B285E8794486FF4FEE1CA84E483FEF3683D062D4207AFF704826B2F56)
    
-   通过[letterSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#letterspacing)属性设置文本字符间距。
    
    Text('This is the text content with letterSpacing 0.')
      .letterSpacing(0)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with letterSpacing 3.')
      .letterSpacing(3)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with letterSpacing -1.')
      .letterSpacing(-1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/vWdSxt3ER0uQKc-ssfhP_A/zh-cn_image_0000002568898425.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=8CB13E4AD57F65A622999DDF390F715671D634B16230BEB6975E626E423C5B5E)
    
-   通过[minFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#minfontsize)与[maxFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxfontsize)自适应字体大小。
    
    minFontSize用于设置文本的最小显示字号，maxFontSize用于设置文本的最大显示字号。这两个属性必须同时设置才能生效，并且需要与[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)属性或布局大小限制配合使用，单独设置任一属性将不会产生效果。
    
    /\* 请将$r('app.string.CustomTextStyle\_textContent\_one\_style')替换为实际资源文件，
     \* 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为5，宽度为250，maxLines为1"
     \*/
    Text($r('app.string.CustomTextStyle\_textContent\_one\_style'))
      .width(250)
      .maxLines(1)
      .maxFontSize(30)
      .minFontSize(5)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    /\* 请将$r('app.string.CustomTextStyle\_textContent\_two\_style')替换为实际资源文件，
     \* 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为5，宽度为250，maxLines为2"
     \*/
    Text($r('app.string.CustomTextStyle\_textContent\_two\_style'))
      .width(250)
      .maxLines(2)
      .maxFontSize(30)
      .minFontSize(5)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    /\* 请将$r('app.string.CustomTextStyle\_textContent\_no\_max')替换为实际资源文件，
     \* 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为15，宽度为250,高度为50"
     \*/
    Text($r('app.string.CustomTextStyle\_textContent\_no\_max'))
      .width(250)
      .height(50)
      .maxFontSize(30)
      .minFontSize(15)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    /\* 请将$r('app.string.CustomTextStyle\_textContent\_high')替换为实际资源文件，
     \* 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为15，宽度为250,高度为100"
     \*/
    Text($r('app.string.CustomTextStyle\_textContent\_high'))
      .width(250)
      .height(100)
      .maxFontSize(30)
      .minFontSize(15)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/mLO1RHbdQiebd835iBy2QA/zh-cn_image_0000002538018720.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=4B0851BF4A38F6E7D3D058A6634217170B2D140E55E93E1A7F63319EC8FBB16A)
    
-   通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textcase)属性设置文本大小写。
    
    Text('This is the text content with textCase set to Normal.')
      .textCase(TextCase.Normal)
      .padding(10)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    // 文本全小写展示
    Text('This is the text content with textCase set to LowerCase.')
      .textCase(TextCase.LowerCase)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    // 文本全大写展示
    Text('This is the text content with textCase set to UpperCase.')
      .textCase(TextCase.UpperCase)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/s9cJ4riZS0yZCaRXS5umRw/zh-cn_image_0000002538178648.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=0D68F98F580DB7949EC53EA5D21C7498C468D4A759482F5F55E741B07C12FCE0)
    
-   通过[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性设置文本是否可复制粘贴。
    
    // 请将$r('app.string.CustomTextStyle\_textContent\_incopy')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段可复制文本。"
    Text($r('app.string.CustomTextStyle\_textContent\_incopy'))
      .fontSize(30)
      .copyOption(CopyOptions.InApp)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/TbzFBKpqSb2wO3OMyqDEwg/zh-cn_image_0000002569018437.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=1E0E6A513AEBB4E7731268BBA920AD26556E3AE3F69573BEACDF8B7B0A34E833)
    
-   通过[fontFamily](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfamily)属性设置字体列表。应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。
    
    Text('This is the text content with fontFamily')
      .fontSize(30)
      .fontFamily('HarmonyOS Sans')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/HbvhHTgDRtqysvOfOSYvvw/zh-cn_image_0000002568898427.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=A83F29D9E7EA62E822A6AEA3EDEA62A159D730EB5BB5211F456D58EE66978B53)
    
-   从API version 20开始，支持通过[contentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#contenttransition20)属性设置数字翻牌效果。
    
    @Entry
    @Component
    export struct ContentTransition {
      private static readonly INITIAL\_SCORE: number = 98;
      @State number: number = ContentTransition.INITIAL\_SCORE;
      @State numberTransition: NumericTextTransition =
        new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });
      build() {
        NavDestination() {
          Column() {
            Text(this.number + '')
              .borderWidth(1)
              .fontSize(40)
              .contentTransition(this.numberTransition)
            Button('chang number')
              .onClick(() => {
                this.number++
              })
              .margin(10)
          }
          .width('100%')
          .height('100%')
        }
        // ···
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Cyorke_rRkafdAMhoJ5xNw/zh-cn_image_0000002538018722.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DC9DFBAC0A731FAF48273E39536BF937B06AAB9DE822DC94FBEAB446254DBA7B)
    
-   从API version 20开始，支持通过[optimizeTrailingSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#optimizetrailingspace20)设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。
    
    Column() {
      // 启用优化行尾空格功能
      Text('Trimmed space enabled     ')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 20 })
        .optimizeTrailingSpace(true)
        .textAlign(TextAlign.Center)
      // 不启用优化行尾空格功能
      Text('Trimmed space disabled     ')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 20 })
        .optimizeTrailingSpace(false)
        .textAlign(TextAlign.Center)
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/iSLueVLATZ-YtUmuNEvViQ/zh-cn_image_0000002538178650.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=27B6212BF9652C94EFA6F8C83DF2235FDD3DA4BB27320405EBEBA3BA6058C009)
    
-   从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。当不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距，当onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外的行间距。
    
    import { LengthMetrics } from '@kit.ArkUI';
    
    @Extend(Text)
    function style() {
      .width(250)
      .height(100)
      .maxFontSize(30)
      .minFontSize(15)
      .border({ width: 1 })
    }
    
    @Entry
    @Component
    export struct LineSpacing {
      build() {
        NavDestination() {
          Column() {
            Text('The line spacing of this context is set to 20\_px, and the spacing is effective only between the lines.')
              .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
              .style()
          }
        }
        // ···
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/QZTOuzksTYWarEWXKk7R2g/zh-cn_image_0000002569018439.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=00237444E6D4F80E3CB9532282A54F3604E2A9ACD41178D9741279AA8F0164F0)
    
-   从API version 20开始，支持通过[enableAutoSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enableautospacing20)设置是否开启中文与西文的自动间距。
    
    @Entry
    @Component
    export struct EnableAutoSpacing {
      @State enableSpacing: boolean = false;
    
      build() {
        NavDestination() {
        Column() {
          Row({ space: 20 }) {
            // 请将$r('app.string.Enable\_automatic\_spacing')替换为实际资源文件，在本示例中该资源文件的value值为"开启自动间距"
            Button($r('app.string.Enable\_automatic\_spacing'))
              .onClick(() => this.enableSpacing = true)
              .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')
              .fontColor(this.enableSpacing ? Color.White : Color.Black)
            // 请将$r('app.string.off\_automatic\_spacing')替换为实际资源文件，在本示例中该资源文件的value值为"关闭自动间距"
            Button($r('app.string.off\_automatic\_spacing'))
              .onClick(() => this.enableSpacing = false)
              .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')
              .fontColor(!this.enableSpacing ? Color.White : Color.Black)
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({ top: 30, bottom: 20 })
          // 请将$r('app.string.Automatic\_spacing\_has\_been\_enabled')替换为实际资源文件，在本示例中该资源文件的value值为"当前状态:已开启自动间距"
          // 请将$r('app.string.Automatic\_spacing\_has\_been\_turned\_off')替换为实际资源文件，在本示例中该资源文件的value值为"当前状态:已关闭自动间距"
          Text(this.enableSpacing ? $r('app.string.Automatic\_spacing\_has\_been\_enabled') : $r('app.string.Automatic\_spacing\_has\_been\_turned\_off'))
            .fontSize(16)
            .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')
            .margin({ bottom: 20 })
    
          // 设置是否应用中西文自动间距
          /\* 请将$r('app.string.Chinese\_and\_Western\_Auto\_Spacing\_automatic\_spacing')替换为实际资源文件，
           \* 在本示例中该资源文件的value值为"中西文Auto Spacing自动间距"
           \*/
          Text($r('app.string.Chinese\_and\_Western\_Auto\_Spacing\_automatic\_spacing'))
            .fontSize(24)
            .padding(15)
            .backgroundColor('#F5F5F5')
            .width('90%')
            .enableAutoSpacing(this.enableSpacing)
        }
        .width('100%')
        .height('100%')
        .padding(20)
        }
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/buiUUxa_TN2WbH4TuNNJtA/zh-cn_image_0000002568898429.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D49764C66B61D3A739FDACA275B71783852583F6B83A67A5373B7DC660E48B7F)
    
-   从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#shaderstyle20)设置渐变色。
    
    @Entry
    @Component
    export struct ShaderStyle {
      @State message: string = 'Hello World';
      @State linearGradientOptions: LinearGradientOptions =
        {
          direction: GradientDirection.LeftTop,
          colors: \[\[Color.Red, 0.0\], \[Color.Blue, 0.3\], \[Color.Green, 0.5\]\],
          repeating: true,
        };
    
      build() {
        NavDestination() {
          Column({ space: 5 }) {
            // 请将$r('app.string.direction\_LeftTop')替换为实际资源文件，在本示例中该资源文件的value值为"direction为LeftTop的线性渐变"
            Text($r('app.string.direction\_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)
              .margin({ top: 40, left: 40 })
            Text(this.message)
              .fontSize(50)
              .width('80%')
              .height(50)
              .shaderStyle(this.linearGradientOptions)
          }
          .height('100%')
          .width('100%')
        }
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/tKvUbETDQ-KKxsf0FXsKLg/zh-cn_image_0000002538018724.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D4DC7BDEC5D596F8F906CE8E3D9E4DA686BBC834A9357D3FE91EB7A72AD92180)
    

#### 添加事件

Text组件可以添加通用事件，可以绑定[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)等事件来响应操作。

// xxx.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
export struct GeneralEvents {
  @State textStr1: string = '';
  @State textStr2: string = '';

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text('This is a text component.')
            .fontSize(30)
            .onClick(() => {
              hilog.info(0x0000, 'Sample\_TextComponent', 'Text onClick is triggering');
              this.textStr1 = 'Text onClick is triggering';
            })
            .onTouch(() => {
              hilog.info(0x0000, 'Sample\_TextComponent', 'Text onTouch is triggering');
              this.textStr2 = 'Text onTouch is triggering';
            })
          Text('onClick：' + this.textStr1)
            .fontSize(20)
          Text('onTouch：' + this.textStr2)
            .fontSize(20)
        }.width('100%')
      }
      .height('100%')
    }
    // ···
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/jKCs-bAFQ7KebxzAEK6Q7w/zh-cn_image_0000002538178652.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F820185BAE423E9F396C204FD953F3D814E6F77F671E301352A9E58BEB1DD918)

#### 设置垂直居中

从API version 20开始，Text组件支持通过[textVerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textverticalalign20)属性实现文本段落在垂直方向的对齐。

-   以下示例展示了如何通过textVerticalAlign属性设置文本垂直居中对齐效果。
    
    // 请将$r('app.media.startIcon')替换为实际资源文件
    Text() {
      Span('Hello')
        .fontSize(50)
      ImageSpan($r('app.media.startIcon'))
        .width(30).height(30)
        .verticalAlign(ImageSpanAlignment.FOLLOW\_PARAGRAPH)
      Span('World')
    }
    .textVerticalAlign(TextVerticalAlign.CENTER)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/vYwFmwS0RGW9BVsbLhTxvA/zh-cn_image_0000002569018441.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=AC60A62E5F04A184F13DAC758A0DFF5871C45398CBF671DB1CF3EA5187B05AD9)
    

#### 设置选中菜单

#### \[h2\]弹出选中菜单

-   设置Text被选中时，会弹出包含复制、翻译、搜索的菜单。
    
    Text组件需要设置[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性才可以被选中。
    
    // 请将$r('app.string.selected\_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
    Text($r('app.string.selected\_menu'))
      .fontSize(30)
      .copyOption(CopyOptions.InApp)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/CAbi6RkAQvGM68Vox6i2Wg/zh-cn_image_0000002568898431.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F71C4806A6D377139813D9F24EE2D5248BBFCB3613A8D20DA91F70AEBD3AD2BA)
    
-   Text组件通过设置[bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#bindselectionmenu11)属性绑定自定义选择菜单。
    
    controller: TextController = new TextController();
    options: TextOptions = { controller: this.controller };
    
    // 请将$r('app.string.show\_selected\_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
    Text($r('app.string.show\_selected\_menu'), this.options)
      .fontSize(30)
      .copyOption(CopyOptions.InApp)
      .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT\_CLICK, {
        onAppear: () => {
          // 请将$r('app.string.SelectMenu\_Text\_Ejected')替换为实际资源文件，在本示例中该资源文件的value值为"自定义选择菜单弹出时触发该回调"
          hilog.info(0x0000, 'Sample\_TextComponent',
            this.getUIContext()
              .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_Ejected').id));
        },
        onDisappear: () => {
          // 'SelectMenu\_Text\_Close'资源文件中的value值为'自定义选择菜单关闭时触发该回调'
          hilog.info(0x0000, 'Sample\_TextComponent',
            this.getUIContext()
              .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_Close').id));
        }
      })
    
    // 定义菜单项
    @Builder
    RightClickTextCustomMenu() {
      Column() {
        Menu() {
          MenuItemGroup() {
            // 请将$r('app.media.app\_icon')替换为实际资源文件
            MenuItem({ startIcon: $r('app.media.app\_icon'), content: 'CustomMenu One', labelInfo: '' })
              .onClick(() => {
                // 使用closeSelectionMenu接口关闭菜单
                this.controller.closeSelectionMenu();
              })
            MenuItem({ startIcon: $r('app.media.app\_icon'), content: 'CustomMenu Two', labelInfo: '' })
            MenuItem({ startIcon: $r('app.media.app\_icon'), content: 'CustomMenu Three', labelInfo: '' })
          }
        }.backgroundColor('#F0F0F0')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/kxIwSNo3QhKkITl92bnrXg/zh-cn_image_0000002538018726.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=6C33E548FC73796111C100B933EAEAF11C3123A2D50C15B305A4D34003DD4D6B)
    
-   Text组件通过设置[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)属性扩展自定义选择菜单，可以设置扩展项的文本内容、图标以及回调方法。
    
    // 请将$r('app.string.show\_selected\_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
    Text($r('app.string.show\_selected\_menu'))
      .fontSize(20)
      .copyOption(CopyOptions.LocalDevice)
      .editMenuOptions({
        onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick
      })
    
    // 定义onCreateMenu，onMenuItemClick
    // 请将$r('app.media.app\_icon')替换为实际资源文件
    onCreateMenu = (menuItems: Array<TextMenuItem>) => {
      let item1: TextMenuItem = {
        content: 'customMenu1',
        icon: $r('app.media.app\_icon'),
        id: TextMenuItemId.of('customMenu1'),
      };
      let item2: TextMenuItem = {
        content: 'customMenu2',
        id: TextMenuItemId.of('customMenu2'),
        icon: $r('app.media.app\_icon'),
      };
      menuItems.push(item1);
      menuItems.unshift(item2);
      return menuItems;
    }
    onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
      if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {
        // 请将$r('app.string.SelectMenu\_Text\_customMenu')替换为实际资源文件，在本示例中该资源文件的value值为"拦截 id: customMenu2 start:"
        hilog.info(0x0000, 'Sample\_TextComponent',
          this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_customMenu')
            .id) + textRange.start + '; end:' +
          textRange.end);
        return true;
      }
      if (menuItem.id.equals(TextMenuItemId.COPY)) {
        // 请将$r('app.string.SelectMenu\_Text\_copy')替换为实际资源文件，在本示例中该资源文件的value值为"拦截 COPY start:"
        hilog.info(0x0000, 'Sample\_TextComponent',
          this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_copy').id) +
          textRange.start + '; end:' + textRange.end);
        return true;
      }
      if (menuItem.id.equals(TextMenuItemId.SELECT\_ALL)) {
        // 请将$r('app.string.SelectMenu\_Text\_SelectionAll')替换为实际资源文件，在本示例中该资源文件的value值为"不拦截 SELECT\_ALL start:"
        hilog.info(0x0000, 'Sample\_TextComponent',
          this.getUIContext()
            .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_SelectionAll').id) +
          textRange.start + '; end:' +
          textRange.end);
        return false;
      }
      return false;
    };
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/wImXqJWiSnmj8tQY4PDHiQ/zh-cn_image_0000002538178654.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D44FBD97AFD72126F6D8EC55D249029CA280C3C86F8304D1D0FF2E89F4CE2279)
    

#### \[h2\]关闭选中菜单

使用Text组件时，若需要实现点击空白处关闭选中的场景，分为以下两种情况：

-   在Text组件区域内点击空白处，会正常关闭选中态和菜单；
    
-   在Text组件区域外点击空白处，前提是Text组件设置[selection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#selection11)属性，具体示例如下：
    
    // xxx.ets
    @Entry
    @Component
    export struct SelectionChange {
      @State text: string =
        'This is set selection to Selection text content This is set selection to Selection text content.';
      @State start: number = 0;
      @State end: number = 20;
    
      build() {
        NavDestination() {
          Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
            Text(this.text)
              .fontSize(12)
              .border({ width: 1 })
              .lineHeight(20)
              .margin(30)
              .copyOption(CopyOptions.InApp)
              .selection(this.start, this.end)
              .onTextSelectionChange((selectionStart, selectionEnd) => {
                // 更新选中态位置
                this.start = selectionStart;
                this.end = selectionEnd;
              })
          }
          .height(600)
          .width(335)
          .borderWidth(1)
          .onClick(() => {
            // 监听父组件的点击事件，将选中首尾位置均设置为-1，即可清除选中
            this.start = -1;
            this.end = -1;
          })
        }
        // ···
      }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/2jooMFjpT9an2GHCSfEkSw/zh-cn_image_0000002569018443.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=89D8F669061B91D1B343D89719F826A47255F61FE320C0E0085865FAA4EABD80)

#### \[h2\]屏蔽系统菜单回调和自定义扩展菜单

从API version 12开始，支持通过[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)屏蔽系统菜单回调和自定义扩展菜单项。

```typescript
// xxx.ets
@Entry
@Component
export struct CustomAndBlockMenus {
  private static readonly CREATE_MENU_ITEM_ID_1: string = 'create1';
  private static readonly CREATE_MENU_ITEM_ID_2: string = 'create2';
  private static readonly PREPARE_MENU_ITEM_ID: string = 'prepare1';
  @State private text: string = 'Text editMenuOptions';
  @State private endIndex: number = 0;
  @State blockCallbackText: string = '';

  // 创建菜单项辅助方法
  private createMenuItem(id: string, content: string): TextMenuItem {
    // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
    return {
      content: content,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of(id)
    };
  }

  // 查找菜单项索引
  private findMenuItemIndex(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): number {
    return menuItems.findIndex((item: TextMenuItem) => item.id.equals(menuItemId));
  }

  // 创建菜单回调
  private onCreateMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const createItem1: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE_MENU_ITEM_ID_1,
      'create1'
    );

    const createItem2: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2,
      'create2'
    );

    // 添加自定义菜单项
    menuItems.push(createItem1);
    menuItems.unshift(createItem2);

    // 移除不需要的系统菜单项
    this.removeMenuItemById(menuItems, TextMenuItemId.AI_WRITER);
    this.removeMenuItemById(menuItems, TextMenuItemId.TRANSLATE);

    return menuItems;
  }

  // 移除指定菜单项
  private removeMenuItemById(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): void {
    const targetIndex: number = this.findMenuItemIndex(menuItems, menuItemId);
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
  }

  // 菜单项点击回调
  private onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange): boolean => {
    const menuItemId: TextMenuItemId = menuItem.id;

    // 处理自定义菜单项
    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2))) {
      let msg = '拦截 id: create2 start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.PREPARE_MENU_ITEM_ID))) {
      let msg = '拦截 id: prepare1 start:' + textRange.start + '; end:+' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    // 处理系统菜单项
    if (menuItemId.equals(TextMenuItemId.COPY)) {
      let msg = '拦截 COPY start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    if (menuItemId.equals(TextMenuItemId.SELECT_ALL)) {
      let msg = '不拦截 SELECT_ALL start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return false;
    }

    return false;
  }
  // 准备菜单回调
  private onPrepareMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const prepareItem: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.PREPARE_MENU_ITEM_ID,
      `prepare1_${this.endIndex}`
    );

    menuItems.unshift(prepareItem);
    return menuItems;
  }
  // 编辑菜单选项
  @State private editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };
  // 文本选择变化回调
  private onTextSelectionChange = (selectionStart: number, selectionEnd: number): void => {
    this.endIndex = selectionEnd;
  }

  build() {
    NavDestination() {
      Column() {
        Text(this.text)
          .fontSize(20)
          .copyOption(CopyOptions.LocalDevice)
          .editMenuOptions(this.editMenuOptions)
          .margin({ top: 100 })
          .onTextSelectionChange(this.onTextSelectionChange)
        Text(this.blockCallbackText).borderWidth(1)
      }
      .width('90%')
      .margin('5%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/gIh0qp-OSfy0-C5YvHHKLw/zh-cn_image_0000002568898433.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3F8D2F4A8EB43A69D9835207877C5B62564BDA2EB786942B3B8DBCD916515CD5)

#### \[h2\]屏蔽系统服务类菜单

-   从API version 20开始，支持通过[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)屏蔽文本选择菜单内所有系统服务菜单项。
    
    import { TextMenuController } from '@kit.ArkUI';
    // xxx.ets
    @Entry
    @Component
    export struct ServiceMenuItems {
      aboutToAppear(): void {
        // 禁用所有系统服务菜单
        TextMenuController.disableSystemServiceMenuItems(true);
      }
    
      aboutToDisappear(): void {
        // 页面消失恢复系统服务菜单
        TextMenuController.disableSystemServiceMenuItems(false);
      }
      build() {
        NavDestination() {
          Row() {
            Column() {
              // 请将$r('app.string.Service\_MenuItems\_Text')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，长按弹出文本选择菜单。"
              Text($r('app.string.Service\_MenuItems\_Text'))
                .height(60)
                .fontStyle(FontStyle.Italic)
                .fontWeight(FontWeight.Bold)
                .textAlign(TextAlign.Center)
                .copyOption(CopyOptions.InApp)
                .editMenuOptions({
                  onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                    // menuItems不包含被屏蔽的系统菜单项
                    return menuItems;
                  },
                  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                    return false;
                  }
                })
            }.width('100%')
          }
          .height('100%')
        }
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/hnu7pONkTKGEy2p8dU2Q6A/zh-cn_image_0000002538018728.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=8D33C6A8EFBB01D068854309971E13CE0922167AA312919CA9FC92F90E0EC7C7)
    
-   从API version 20开始，支持通过[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)屏蔽文本选择菜单内指定的系统服务菜单项。
    
    import { TextMenuController } from '@kit.ArkUI';
    
    // xxx.ets
    @Entry
    @Component
    export struct DisableMenuItems {
      aboutToAppear(): void {
        // 禁用搜索菜单
        TextMenuController.disableMenuItems(\[TextMenuItemId.SEARCH\])
      }
    
      aboutToDisappear(): void {
        // 恢复系统服务菜单
        TextMenuController.disableMenuItems(\[\])
      }
    
      build() {
        NavDestination() {
          Row() {
            Column() {
              // 请将$r('app.string.Service\_MenuItems\_Text')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，长按弹出文本选择菜单。"
              Text($r('app.string.Service\_MenuItems\_Text'))
                .height(60)
                .fontStyle(FontStyle.Italic)
                .fontWeight(FontWeight.Bold)
                .textAlign(TextAlign.Center)
                .copyOption(CopyOptions.InApp)
                .editMenuOptions({
                  onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                    // menuItems不包含搜索
                    return menuItems;
                  },
                  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                    return false
                  }
                })
            }.width('100%')
          }
          .height('100%')
        }
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/JHkr1rfqTJOQr4gt5ES7_g/zh-cn_image_0000002538178656.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=661E3E3C785F993130D00FA91B07D6765BE531E6F3944E760F340BDED28C5DBD)
    

#### \[h2\]默认菜单支持自定义刷新能力

从API version 20开始，当文本选择区域变化后显示菜单之前触发[onPrepareMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#属性-1)回调，可在该回调中进行菜单数据设置。

// 请将$r('app.media.xxx')替换为实际资源文件
// xxx.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0000;
@Entry
@Component

export struct PrepareMenu {
  @State text: string = 'Text editMenuOptions';
  @State endIndex: number = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    };
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    };
    menuItems.push(item1);
    menuItems.unshift(item2);
    return menuItems;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: create2 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: prepare1 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept COPY start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT\_ALL)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'No interception SELECT\_ALL start:' + textRange.start + '; end:' + textRange.end);
      return false;
    }
    return false;
  }
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'prepare1\_' + this.endIndex,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('prepare1'),
    };
    menuItems.unshift(item1);
    return menuItems;
  }
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  build() {
    NavDestination() {
    Column() {
      Text(this.text)
        .fontSize(20)
        .copyOption(CopyOptions.LocalDevice)
        .editMenuOptions(this.editMenuOptions)
        .margin({ top: 100 })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.endIndex = selectionEnd;
        })
    }
    .width('90%')
    .margin('5%')
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/sNAP-_SXQwam5j9RwAm-tg/zh-cn_image_0000002569018445.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C86D7BC4389B14359ABFEA1DB82B61A9C5692EA1708CFC355E2143451BB8DC5C)

#### 设置AI菜单

Text组件通过[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)和[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)属性实现AI菜单的显示。AI菜单的表现形式包括：单击AI实体（指可被识别的内容，包括地址、邮箱等）弹出菜单的实体识别选项，选中文本后，文本选择菜单与鼠标右键菜单中显示的实体识别选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/OXStt9YsSMqZgM5mJ1GHew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=6359790FE72B928C539295CA893DA9C8560E64086CF1D28913F4295631A840FF)

从API version 20开始，支持在文本选择菜单与鼠标右键菜单中显示实体识别选项。当[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)设置为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice时，该功能生效。菜单选项包括[TextMenuItemId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textmenuitemid12)中的url(打开链接)、email(新建邮件)、phoneNumber(呼叫)、address(导航至该位置)、dateTime(新建日程提醒)。

该功能生效时，需选中范围内，包括一个完整的AI实体，才能展示对应的选项。

-   如果需要单击AI实体弹出菜单的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true。
    
-   如果在单击的交互方式之外，还需要文本选择菜单与鼠标右键菜单中显示的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice，具体示例如下所示：
    
    // 'app.string.AIMenu\_Text\_One'资源文件中的value值为'电话号码：(86) (755) \*\*\*\*\*\*\*\*  \\n \\n 链接：www.\*\*\*\*\*\*\*\*.com
    // \\n \\n 邮箱：\*\*\*@example.com\\n \\n 地址：XX省XX市XX区XXXX \\n \\n 时间：XX年XX月XX日XXXX'
    Text($r('app.string.AIMenu\_Text\_One'))
      .fontSize(16)
      .copyOption(CopyOptions.LocalDevice)
      .enableDataDetector(true)// 使能实体识别
      .dataDetectorConfig({
        // 配置识别样式
        // types可支持PHONE\_NUMBER电话号码、URL链接、EMAIL邮箱、ADDRESS地址、DATE\_TIME时间
        // types设置为null或者\[\]时，识别所有类型的实体
        types: \[\], onDetectResultUpdate: (result: string) => {
        }
      })
    
-   如果需要调整识别出的样式，可以通过[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)实现，具体可以参考[TextDataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textdatadetectorconfig11对象说明)配置项。
    
-   如果需要调整菜单的位置，可以通过[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)实现，具体可以参考示例[文本扩展自定义菜单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#示例12文本扩展自定义菜单)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/PfFVkbJfQUKZ3UeO9xbWcA/zh-cn_image_0000002568898435.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F8C004AB0E964572269810572B4E9CF9605F76236206FE0A5710FEE7C2D5C224)
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/lR8-MLB5TN-AwS0o7u2Fng/zh-cn_image_0000002538018730.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=E355067C94920CF23BD718021E766FE4E7B0B02504A73D5A66BE485E6415A81B)

#### 实现热搜榜

该示例通过[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)、[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)、[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)、[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)属性展示了热搜榜的效果。

import { ComponentCard } from '../../common/Card';

@Entry
@Component
export struct TextHotSearch {
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Column() {
            Row() {
              Text('1').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
              // 请将$r('app.string.TextHotSearch\_textContent\_one')替换为实际资源文件，在本示例中该资源文件的value值为"我是热搜词条1"
              Text($r('app.string.TextHotSearch\_textContent\_one'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .fontWeight(300)
              // 请将$r('app.string.TextHotSearch\_textContent\_two')替换为实际资源文件，在本示例中该资源文件的value值为"爆"
              Text($r('app.string.TextHotSearch\_textContent\_two'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0x770100)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('2').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
              /\* 请将$r('app.string.TextHotSearch\_textContent\_three')替换为实际资源文件，
               \* 在本示例中该资源文件的value值为"我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2"
               \*/
              Text($r('app.string.TextHotSearch\_textContent\_three'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
              // 请将$r('app.string.TextHotSearch\_textContent\_four')替换为实际资源文件，在本示例中该资源文件的value值为"热"
              Text($r('app.string.TextHotSearch\_textContent\_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('3').fontSize(14).fontColor(Color.Orange).margin({ left: 10, right: 10 })
              // 请将$r('app.string.TextHotSearch\_textContent\_five')替换为实际资源文件，在本示例中该资源文件的value值为"我是热搜词条3"
              Text($r('app.string.TextHotSearch\_textContent\_five'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .maxLines(1)
                .constraintSize({ maxWidth: 200 })
                .textOverflow({ overflow: TextOverflow.Ellipsis })
              // 请将$r('app.string.TextHotSearch\_textContent\_four')替换为实际资源文件，在本示例中该资源文件的value值为"热"
              Text($r('app.string.TextHotSearch\_textContent\_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('4').fontSize(14).fontColor(Color.Grey).margin({ left: 10, right: 10 })
              /\* 请将$r('app.string.TextHotSearch\_textContent\_six')替换为实际资源文件，
               \* 在本示例中该资源文件的value值为"我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4"
               \*/
              Text($r('app.string.TextHotSearch\_textContent\_six'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
            }.width('100%').margin(5)
          }.width('100%')
        // ...
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/j_A0ueF8SzGMk8rM6g8efQ/zh-cn_image_0000002538178658.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=000C084DDBA3B5C12FB8D2F9F64DCF89BD9327B892AA86EC4A94FF0177C1C4DE)

#### 示例代码

-   [文字特效合集](https://gitcode.com/HarmonyOS_Samples/text-effects)
