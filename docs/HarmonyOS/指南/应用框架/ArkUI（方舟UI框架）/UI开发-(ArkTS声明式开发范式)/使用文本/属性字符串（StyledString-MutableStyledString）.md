---
title: "属性字符串（StyledString/MutableStyledString）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-styled-string"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "使用文本"
  - "属性字符串（StyledString/MutableStyledString）"
captured_at: "2026-04-17T01:35:37.738Z"
---

# 属性字符串（StyledString/MutableStyledString）

属性字符串StyledString/MutableStyledString（其中MutableStyledString继承自StyledString，下文统称为StyledString），可用于在字符或段落级别上设置文本样式。将StyledString应用到文本组件上，可以采用多种方式修改文本，包括调整字号、添加字体颜色、使文本具备可点击性，以及通过自定义方式绘制文本等。具体使用方法请参考[属性字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string)的API文档。

属性字符串提供多种类型样式对象，涵盖各种常见的文本样式格式，例如文本装饰线样式、文本行高样式、文本阴影样式等。也可以自行创建[CustomSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#customspan)，以应用自定义样式。

#### 创建并应用StyledString和MutableStyledString

可以通过[TextController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textcontroller11)提供的[setStyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#setstyledstring12)方法，将属性字符串附加到文本组件，并推荐在[onPageShow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#onpageshow)或者文本组件的[onAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide#onappear)回调中触发绑定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ViV_rKC1QjSO5lKFcv8lkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=77AD9087F63716304C263DB5A0FA3D2C791C0A2CC5E046C70074E660C5CB0E82)

在[aboutToAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-new-lifecycle#abouttoappear)中调用setStyledString方法时，由于该方法运行阶段组件尚未完成创建并成功挂载节点树，因此无法在页面初始化时显示属性字符串。

从API version 15开始，在aboutToAppear中调用setStyledString方法，页面初始化时可以显示属性字符串。

@Entry
@Component
struct styled\_string\_demo1 {
  // 请将$r('app.string.CreateApply\_Text\_Forty\_Five')替换为实际资源文件，在本示例中该资源文件的value值为"运动45分钟"
  styledString1: StyledString = new StyledString( this.getUIContext()
    .getHostContext()!.resourceManager.getStringSync($r('app.string.CreateApply\_Text\_Forty\_Five').id));
  // 请将$r('app.string.CreateApply\_Text\_Third\_Five')替换为实际资源文件，在本示例中该资源文件的value值为"运动35分钟"
  mutableStyledString1: MutableStyledString = new MutableStyledString( this.getUIContext()
    .getHostContext()!.resourceManager.getStringSync($r('app.string.CreateApply\_Text\_Third\_Five').id));
  controller1: TextController = new TextController();
  controller2: TextController = new TextController();

  async onPageShow() {
    // 在生命周期onPageShow回调中绑定属性字符串
    this.controller1.setStyledString(this.styledString1);
  }

  build() {
    Column() {
      // 显示属性字符串
      Text(undefined, { controller: this.controller1 })
      Text(undefined, { controller: this.controller2 })
        .onAppear(() => {
          // 在组件onAppear回调中绑定属性字符串
          this.controller2.setStyledString(this.mutableStyledString1);
        })
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/zydRXcMmQmChL73fohPEJg/zh-cn_image_0000002569018481.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=9B752D5EF883D944F3BEA567BF6A96F085C5567EA2890446E9828E6BEAFA49B4)

#### 设置文本样式

属性字符串目前提供了多种Style对象，包括[TextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#textstyle)、[TextShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#textshadowstyle)、[DecorationStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#decorationstyle)、[BaselineOffsetStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#baselineoffsetstyle)、[LineHeightStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#lineheightstyle)、[LetterSpacingStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#letterspacingstyle)，用于设置文本的各类样式。

-   创建及应用文本字体样式对象（TextStyle）
    
    import { LengthMetrics } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct styled\_string\_demo2 {
      @State str: string =
        this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply\_Text\_3') as string;
      textStyleAttrs: TextStyle =
        new TextStyle({
          fontWeight: FontWeight.Bolder,
          fontSize: LengthMetrics.vp(24),
          fontStyle: FontStyle.Italic,
          strokeWidth: LengthMetrics.px(5),
          strokeColor: Color.Green
        });
      mutableStyledString: MutableStyledString = new MutableStyledString(this.str, \[
        {
          start: 2,
          length: 2,
          styledKey: StyledStringKey.FONT,
          styledValue: this.textStyleAttrs
        },
        {
          start: 7,
          length: 4,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({
            fontColor: Color.Orange, fontSize: LengthMetrics.vp(12),
            superscript: SuperscriptStyle.SUPERSCRIPT
          })
        }
      \]);
      controller: TextController = new TextController();
    
      async onPageShow() {
        this.controller.setStyledString(this.mutableStyledString);
      }
    
      build() {
        Column() {
          // 显示属性字符串
          Text(undefined, { controller: this.controller })
            .margin({ top: 10 })
        }
        .width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Bx1ZWk_LRze8XcFCUa9PSA/zh-cn_image_0000002568898471.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=902810D28D3C22A9CCC5461755A2E1677940548B9587A7227C6AB2E1F4485327)
    
-   创建及应用文本阴影对象（TextShadowStyle）
    
    // xxx.ets
    @Entry
    @Component
    struct styled\_string\_demo3 {
      @State str: string =
        this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply\_Text\_Third\_Five') as string;
      mutableStyledString: MutableStyledString = new MutableStyledString(this.str, \[
        {
          start: 0,
          length: 3,
          styledKey: StyledStringKey.TEXT\_SHADOW,
          styledValue: new TextShadowStyle({
            radius: 5,
            type: ShadowType.COLOR,
            color: Color.Red,
            offsetX: 10,
            offsetY: 10
          })
        }
      \]);
      controller: TextController = new TextController();
    
      async onPageShow() {
        this.controller.setStyledString(this.mutableStyledString);
      }
    
      build() {
        Column() {
          // 显示属性字符串
          Text(undefined, { controller: this.controller })
        }
        .width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/a-oT65izQbGWelVbbfOxJg/zh-cn_image_0000002538018766.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D1755F6B7A20318FE9DBC30FF1A9BF03BE27FAD4C18214FAB5AD09E36E5544E9)
    
-   创建及应用文本装饰线对象（DecorationStyle）
    
    // xxx.ets
    @Entry
    @Component
    struct styled\_string\_demo4 {
      @State str: string =
        this.getUIContext()
          .getHostContext()?.resourceManager.getStringByNameSync('CreateApply\_Text\_Third\_Five') as string;
      mutableStyledString: MutableStyledString = new MutableStyledString(this.str, \[
        {
          start: 0,
          length: 4,
          styledKey: StyledStringKey.DECORATION,
          styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough, color: Color.Red, thicknessScale: 3 })
        },
        {
          start: 4,
          length: 2,
          styledKey: StyledStringKey.DECORATION,
          styledValue: new DecorationStyle(
            {
              type: TextDecorationType.Underline,
            },
            {
              // 开启多装饰线
              enableMultiType: true
            }
          )
        },
        {
          start: 4,
          length: 2,
          styledKey: StyledStringKey.DECORATION,
          styledValue: new DecorationStyle(
            {
              type: TextDecorationType.LineThrough,
            },
            {
              // 开启多装饰线
              enableMultiType: true
            }
          )
        },
      \]);
      controller: TextController = new TextController();
    
      async onPageShow() {
        this.controller.setStyledString(this.mutableStyledString);
      }
    
      build() {
        Column() {
          // 显示属性字符串
          Text(undefined, { controller: this.controller })
        }
        .width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/wpQ8Ar2CQeKP11r8lppTMQ/zh-cn_image_0000002538178694.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=BBAACD372FF5EA61C606361A3A433D0F67E88A7ED9878F3DE34447D84ECA66BA)
    
-   创建及应用文本基线偏移量对象（BaselineOffsetStyle）
    
    import { LengthMetrics } from '@kit.ArkUI';
    
    // xxx.ets
    @Entry
    @Component
    struct styled\_string\_demo5 {
      @State str: string =
        this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply\_Text\_Third\_Five') as string;
    
      mutableStyledString: MutableStyledString = new MutableStyledString(this.str, \[
        {
          start: 0,
          length: 3,
          styledKey: StyledStringKey.BASELINE\_OFFSET,
          styledValue: new BaselineOffsetStyle(LengthMetrics.px(20))
        }
      \]);
      controller: TextController = new TextController();
    
      async onPageShow() {
        this.controller.setStyledString(this.mutableStyledString);
      }
    
      build() {
        Column() {
          // 显示属性字符串
          Text(undefined, { controller: this.controller })
        }
        .width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/dvOU2cdfRfqWTqXf2DDgEA/zh-cn_image_0000002569018483.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=55C19A5C00260E8547FCB9D24BE2D4BFADE16FC62C0F22767DC6C78E4203F6C7)
    
-   创建及应用文本行高对象（LineHeightStyle）
    
    import { LengthMetrics } from '@kit.ArkUI';
    
    // xxx.ets
    @Entry
    @Component
    struct styled\_string\_demo6 {
      @State str: string =
        this.getUIContext()
          .getHostContext()?.resourceManager.getStringByNameSync('StyledStringStyle\_Text\_5') as string;
      mutableStyledString: MutableStyledString = new MutableStyledString(this.str, \[
        {
          start: 8,
          length: 3,
          styledKey: StyledStringKey.LINE\_HEIGHT,
          styledValue: new LineHeightStyle(LengthMetrics.vp(50))
        }
      \]);
      controller: TextController = new TextController();
    
      async onPageShow() {
        this.controller.setStyledString(this.mutableStyledString);
      }
    
      build() {
        Column() {
          // 显示属性字符串
          Text(undefined, { controller: this.controller })
        }
        .width('100%')
        .margin({ top: 10 })
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/grY0UJwfSfKNCeF0GVpIVw/zh-cn_image_0000002568898473.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F60FBBA1CB69A627AB27E9188675092882E5B731B400E281EB0C78BB4A88EB10)
    
-   创建及应用文本字符间距对象（LetterSpacingStyle）
    
    import { LengthMetrics, LengthUnit } from '@kit.ArkUI';
    
    // xxx.ets
    @Entry
    @Component
    struct styled\_string\_demo7 {
      @State str: string =
        this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply\_Text\_Third\_Five') as string;
      mutableStyledString: MutableStyledString = new MutableStyledString(this.str, \[
        {
          start: 0,
          length: 2,
          styledKey: StyledStringKey.LETTER\_SPACING,
          styledValue: new LetterSpacingStyle(new LengthMetrics(20, LengthUnit.VP))
        }
      \]);
      controller: TextController = new TextController();
    
      async onPageShow() {
        this.controller.setStyledString(this.mutableStyledString);
      }
    
      build() {
        Column() {
          // 显示属性字符串
          Text(undefined, { controller: this.controller })
        }
        .width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/qmvcifwPSgGAa645i7xQrg/zh-cn_image_0000002538018768.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=5A580225D28E224DE8CA8F259E07A884BC9E9CB7FAA666C64323D0468AAD9624)
    

#### 设置段落样式

可通过[ParagraphStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#paragraphstyle)设置段落样式布局。下图显示了如何分割文本中的段落，段落以换行符 \\n 结尾。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/TJ5SqYzEQdyZp1XazkpkOQ/zh-cn_image_0000002538178696.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=9FB8E1F79314F24E45EDD0AF9C29A5B521BF8566EB290103B320B29F8B10C025)

以下代码示例展示了如何创建ParagraphStyle并应用。如果将ParagraphStyle附加到段落开头、末尾或之间的任何位置，均会应用样式，非段落区间内则不会应用样式。

import { LengthMetrics} from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State str: string =
    this.getUIContext()
      .getHostContext()?.resourceManager.getStringByNameSync('StyledStringParagraphStyle\_Text\_1') as string;
  titleParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });
  // 段落首行缩进15vp
  paragraphStyleAttr1: ParagraphStyle = new ParagraphStyle({ textIndent: LengthMetrics.vp(15) });
  // 行高样式对象
  lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));
  // 创建含段落样式的对象paragraphStyledString1
  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.str, \[
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH\_STYLE,
        styledValue: this.titleParagraphStyleAttr
      },
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.LINE\_HEIGHT,
        styledValue: new LineHeightStyle(new LengthMetrics(50))
      }, {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
    },
      {
        start: 5,
        length: 3,
        styledKey: StyledStringKey.PARAGRAPH\_STYLE,
        styledValue: this.paragraphStyleAttr1
      },
      {
        start: 5,
        length: 20,
        styledKey: StyledStringKey.LINE\_HEIGHT,
        styledValue: this.lineHeightStyle1
      }
    \]);
  controller: TextController = new TextController();

  async onPageShow() {
    this.controller.setStyledString(this.paragraphStyledString1);
  }

  build() {
    Column() {
      // 显示属性字符串
      Text(undefined, { controller: this.controller })
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/OIt1aJtMQM6yygXRqC738g/zh-cn_image_0000002569018485.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=E2D5A0867AB46F5351FB2829DC761FA042317DC803917E712FF5E522BF907D54)

除了可以在创建属性字符串时就预设样式，也可以后续通过[replaceStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#replacestyle)清空原样式替换新样式，同时需要在附加的文本组件controller上主动触发更新绑定的属性字符串。

import { LengthMetrics } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext();
  /\* 请将$r('app.string.StyledStringParagraphStyle\_Text\_2')替换为实际资源文件，在本示例中该资源文件的value值为
   "段落标题\\n正文第一段落开始0123456789正文第一段落结束，通过replaceStyle清空原样式替换新样式。"\*/
  @State message1: string =
    this.context!.resourceManager.getStringSync($r('app.string.StyledStringParagraphStyle\_Text\_2').id);
  titleParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });
  // 段落首行缩进15vp
  paragraphStyleAttr1: ParagraphStyle = new ParagraphStyle({ textIndent: LengthMetrics.vp(15) });
  // 行高样式对象
  lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));
  // 创建含段落样式的对象paragraphStyledString1
  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.message1, \[
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH\_STYLE,
        styledValue: this.titleParagraphStyleAttr
      },
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.LINE\_HEIGHT,
        styledValue: new LineHeightStyle(new LengthMetrics(50))
      }, {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
    },
      {
        start: 5,
        length: 3,
        styledKey: StyledStringKey.PARAGRAPH\_STYLE,
        styledValue: this.paragraphStyleAttr1
      },
      {
        start: 5,
        length: 20,
        styledKey: StyledStringKey.LINE\_HEIGHT,
        styledValue: this.lineHeightStyle1
      }
    \]);
  paragraphStyleAttr3: ParagraphStyle = new ParagraphStyle({
    textAlign: TextAlign.End,
    maxLines: 1,
    wordBreak: WordBreak.BREAK\_ALL,
    overflow: TextOverflow.Ellipsis
  });
  controller: TextController = new TextController();

  async onPageShow() {
    this.controller.setStyledString(this.paragraphStyledString1);
  }

  build() {
    Column() {
      // 显示属性字符串
      Text(undefined, { controller: this.controller }).width(300)
      // 请将$r('app.string.Replace\_paragraph\_style')替换为实际资源文件，在本示例中该资源文件的value值为"替换段落样式"
      Button($r('app.string.Replace\_paragraph\_style'))
        .onClick(() => {
          this.paragraphStyledString1.replaceStyle({
            start: 5,
            length: 3,
            styledKey: StyledStringKey.PARAGRAPH\_STYLE,
            styledValue: this.paragraphStyleAttr3
          });
          this.controller.setStyledString(this.paragraphStyledString1);
        })
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/6bv9ZYNPTuOX5NckdPH58Q/zh-cn_image_0000002568898475.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=FFF7D6E6BBAFB6FC8CA739C0A79D458ABF9C7FEA5D6991118B2639A58A47B510)

#### 支持将属性字符串转换成Paragraph

可通过[getParagraphs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#getparagraphs20)将属性字符串根据文本布局选项转换成对应的[Paragraph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text#paragraph)数组。

-   以下示例展示了通过[MeasureUtils](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils)的getParagraphs方法测算文本，当内容超出最大显示行数的时候，截断文本显示并展示“...全文”的效果。
    
    import { LengthMetrics } from '@kit.ArkUI';
    import { drawing } from '@kit.ArkGraphics2D';
    
    class MyCustomSpan extends CustomSpan {
      constructor(word: string, width: number, height: number, context: UIContext) {
        super();
        this.word = word;
        this.width = width;
        this.height = height;
        this.context = context;
      }
    
      onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics {
        return { width: this.width, height: this.height };
      }
    
      onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
        let canvas = context.canvas;
        const brush = new drawing.Brush();
        brush.setColor({
          alpha: 255,
          red: 0,
          green: 74,
          blue: 175
        });
        const font = new drawing.Font();
        font.setSize(25);
        const textBlob = drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
        canvas.attachBrush(brush);
        canvas.drawRect({
          left: options.x + 10,
          right: options.x + this.context.vp2px(this.width) - 10,
          top: options.lineTop + 10,
          bottom: options.lineBottom - 10
        });
        brush.setColor({
          alpha: 255,
          red: 23,
          green: 169,
          blue: 141
        });
        canvas.attachBrush(brush);
        canvas.drawTextBlob(textBlob, options.x + 20, options.lineBottom - 15);
        canvas.detachBrush();
      }
    
      setWord(word: string) {
        this.word = word;
      }
    
      public width: number = 160;
      public word: string = 'drawing';
      public height: number = 10;
      public context: UIContext;
    }
    
    @Entry
    @Component
    struct Index {
      // 请在resources\\base\\element\\string.json文件中配置name为'Full\_text'，value为非空字符串的资源
      @State fullText: string =
        this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Full\_text') as string;
      // 请将$r('app.string.Original\_text')替换为实际资源文件，在本示例中该资源文件的value值为"原文"
      @State originalText: ResourceStr = $r('app.string.Original\_text');
      // 请将$r('app.string.After\_typesetting')替换为实际资源文件，在本示例中该资源文件的value值为"排版后"
      @State afterTypesetting: ResourceStr = $r('app.string.After\_typesetting');
      str: string =
        'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.';
      mutableStr2 = new MutableStyledString(this.str, \[
        {
          start: 0,
          length: 3,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontSize: LengthMetrics.px(20) })
        },
        {
          start: 3,
          length: 3,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontColor: Color.Brown })
        }
      \]);
    
      // 测算属性字符串在指定宽度下能显示的行数
      getLineNum(styledString: StyledString, width: LengthMetrics) {
        let paragraphArr = this.getUIContext().getMeasureUtils().getParagraphs(styledString, { constraintWidth: width });
        let res = 0;
        for (let i = 0; i < paragraphArr.length; ++i) {
          res += paragraphArr\[i\].getLineCount();
        }
        return res;
      }
    
      // 测算属性字符串显示maxLines行时最多可以显示的字数
      getCorrectIndex(styledString: MutableStyledString, maxLines: number, width: LengthMetrics) {
        let low = 0;
        let high = styledString.length - 1;
        // 使用二分查找
        while (low <= high) {
          let mid = (low + high) >> 1;
          console.info('demo: get ' + low + ' ' + high + ' ' + mid);
          let moreStyledString = new MutableStyledString(this.fullText, \[{
            start: 4,
            length: 2,
            styledKey: StyledStringKey.FONT,
            styledValue: new TextStyle({ fontColor: Color.Blue })
          }\]);
          moreStyledString.insertStyledString(0, styledString.subStyledString(0, mid));
          let lineNum = this.getLineNum(moreStyledString, LengthMetrics.px(500));
          if (lineNum <= maxLines) {
            low = mid + 1;
          } else {
            high = mid - 1;
          }
        }
        return high;
      }
    
      mutableStrAllContent = new MutableStyledString(this.str, \[
        {
          start: 0,
          length: 3,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontSize: LengthMetrics.px(40) })
        },
        {
          start: 3,
          length: 3,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontColor: Color.Brown })
        }
      \]);
      customSpan1: MyCustomSpan = new MyCustomSpan('Hello', 120, 10, this.getUIContext());
      mutableStrAllContent2 = new MutableStyledString(this.str, \[
        {
          start: 0,
          length: 3,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontSize: LengthMetrics.px(100) })
        },
        {
          start: 3,
          length: 3,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontColor: Color.Brown })
        }
      \]);
      controller: TextController = new TextController();
      controller2: TextController = new TextController();
      textController: TextController = new TextController();
      textController2: TextController = new TextController();
    
      aboutToAppear() {
        this.mutableStrAllContent2.insertStyledString(0, new StyledString(this.customSpan1));
        this.mutableStr2.insertStyledString(0, new StyledString(this.customSpan1));
      }
    
      build() {
        Scroll() {
          Column() {
            Text(this.originalText)
            Text(undefined, { controller: this.controller }).width('500px').onAppear(() => {
              this.controller.setStyledString(this.mutableStrAllContent);
            })
            Divider().strokeWidth(8).color('#F1F3F5')
            Text(this.afterTypesetting)
            Text(undefined, { controller: this.textController }).onAppear(() => {
              let now = this.getCorrectIndex(this.mutableStrAllContent, 3, LengthMetrics.px(500));
              if (now != this.mutableStrAllContent.length - 1) {
                let moreStyledString = new MutableStyledString(this.fullText, \[{
                  start: 4,
                  length: 2,
                  styledKey: StyledStringKey.FONT,
                  styledValue: new TextStyle({ fontColor: Color.Blue })
                }\]);
                moreStyledString.insertStyledString(0, this.mutableStrAllContent.subStyledString(0, now));
                this.textController.setStyledString(moreStyledString);
              } else {
                this.textController.setStyledString(this.mutableStrAllContent);
              }
            })
              .width('500px')
            Divider().strokeWidth(8).color('#F1F3F5')
            Text(this.originalText)
            Text(undefined, { controller: this.controller2 }).width('500px').onAppear(() => {
              this.controller2.setStyledString(this.mutableStrAllContent2);
            })
            Divider().strokeWidth(8).color('#F1F3F5')
            Text(this.afterTypesetting)
            Text(undefined, { controller: this.textController2 }).onAppear(() => {
              let now = this.getCorrectIndex(this.mutableStrAllContent2, 3, LengthMetrics.px(500));
              let moreStyledString = new MutableStyledString(this.fullText, \[{
                start: 4,
                length: 2,
                styledKey: StyledStringKey.FONT,
                styledValue: new TextStyle({ fontColor: Color.Blue })
              }\]);
              moreStyledString.insertStyledString(0, this.mutableStrAllContent2.subStyledString(0, now));
              this.textController2.setStyledString(moreStyledString);
            })
              .width('500px')
          }.width('100%')
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/XxbuohlGRMuLYtM0ynmIEQ/zh-cn_image_0000002538018770.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=90370D109EB6592A6926D2D83F27E54BAAFFEC79A5648CEBC810092546ECBF9F)
    

#### 使用图片

可通过[ImageAttachment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#imageattachment)来添加图片。

以下示例展示了如何将图片和文本附加到同一个MutableStyledString对象上，并实现图文混排。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/EEDUm9VSR-mbbm5NkdX7rg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=CC3261EC4C3751866F539F3ED4425F6E03A72DFDBEC14E59474B53D863534EE4)

属性字符串的构造函数[constructor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#constructor)中，当入参value的类型为ImageAttachment或CustomSpan时，styles参数不生效。需要设置styles时，通过[setStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#setstyle)、[insertStyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#insertstyledstring)等方法实现。

// xxx.ets
import { image } from '@kit.ImageKit';
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
export struct StyledStringImageAttachment {
  @State abled: boolean = true;
  @State message: string = 'Hello World';
  imagePixelMap: image.PixelMap | undefined = undefined;
  @State imagePixelMap3: image.PixelMap | undefined = undefined;
  mutableStr: MutableStyledString = new MutableStyledString('123');
  controller: TextController = new TextController();
  mutableStr2: MutableStyledString = new MutableStyledString('This is set decoration line style to the mutableStr2', \[{
    start: 0,
    length: 15,
    styledKey: StyledStringKey.DECORATION,
    styledValue: new DecorationStyle({
      type: TextDecorationType.Overline,
      color: Color.Orange,
      style: TextDecorationStyle.DOUBLE
    })
  }\]);

  async aboutToAppear() {
    console.info('aboutToAppear initial imagePixelMap');
    // $r('app.media.sea')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.sea'));
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer?.slice(0, unit8Array?.buffer?.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  leadingMarginValue: ParagraphStyle = new ParagraphStyle({ leadingMargin: LengthMetrics.vp(5)});
  //行高样式对象
  lineHeightStyle1: LineHeightStyle= new LineHeightStyle(new LengthMetrics(24));
  //Bold样式
  boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });
  //创建含段落样式的对象paragraphStyledString1
  // 请将$r('app.string.StyledStringImageAttachment\_Text\_1')替换为实际资源文件，在本示例中该资源文件的value值为"\\n品牌相纸 高清冲印30张\\n限时直降5.15元 限量赠送"
  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringImageAttachment\_Text\_1').id), \[
    {
      start: 0,
      length: 28,
      styledKey: StyledStringKey.PARAGRAPH\_STYLE,
      styledValue: this.leadingMarginValue
    },
    {
      start: 14,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontColor: '#B22222' })
    },
    {
      start: 24,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontWeight: FontWeight.Lighter })
    },
    {
      start: 11,
      length: 4,
      styledKey: StyledStringKey.LINE\_HEIGHT,
      styledValue: this.lineHeightStyle1
    }
  \]);
  // 请将$r('app.string.StyledStringImageAttachment\_Text\_2')替换为实际资源文件，在本示例中该资源文件的value值为"\\n￥16.21 3000+人好评"
  paragraphStyledString2: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringImageAttachment\_Text\_2').id), \[
    {
      start: 0,
      length: 5,
      styledKey: StyledStringKey.PARAGRAPH\_STYLE,
      styledValue: this.leadingMarginValue
    },
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.LINE\_HEIGHT,
      styledValue: new LineHeightStyle(new LengthMetrics(60))
    },
    {
      start: 0,
      length: 7,
      styledKey: StyledStringKey.FONT,
      styledValue: this.boldTextStyle
    },
    {
      start: 1,
      length: 1,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18) })
    },
    {
      start: 2,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(36) })
    },
    {
      start: 4,
      length: 3,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(20) })
    },
    {
      start: 7,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14)})
    }
  \]);

  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Row() {
            Column({ space: 10 }) {
              Text(undefined, { controller: this.controller })
                .id('text1')
                .copyOption(CopyOptions.InApp)
                .draggable(true)
                .backgroundColor('#FFFFFF')
                .borderRadius(5)
              // 请将$r('app.string.StyledStringImageAttachment\_Button\_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击查看商品卡片"
              Button($r('app.string.StyledStringImageAttachment\_Button\_1'))
                .enabled(this.abled)
                .onClick(() => {
                  if (this.imagePixelMap !== undefined) {
                    this.mutableStr = new MutableStyledString(new ImageAttachment({
                      value: this.imagePixelMap,
                      size: { width: 180, height: 160 },
                      verticalAlign: ImageSpanAlignment.BASELINE,
                      objectFit: ImageFit.Fill
                    }));
                    this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
                    this.mutableStr.appendStyledString(this.paragraphStyledString1);
                    this.controller.setStyledString(this.mutableStr);
                  }
                  this.abled = false;
                })
            }
            .width('100%')
          }
          .height('100%')
          .backgroundColor('#F8F8FF')
        }
        // ...
    }
    .backgroundColor('#f1f2f3')
    // 请将$r('app.string.StyledStringImageAttachment\_title')替换为实际资源文件，在本示例中该资源文件的value值为"通过ImageAttachment来添加图片"
    .title($r('app.string.StyledStringImageAttachment\_title'))
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/cL7GGQXeSU6NSBXfxEpJmQ/zh-cn_image_0000002538178698.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=0C123CB8F932EFCE179A28A084CDA1E2D97479B610CDAA60640B01C45C427A43)

#### 设置事件

可通过[GestureStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#gesturestyle)设置onClick、onLongPress事件来使文本响应点击长按事件。

除了初始化属性字符串对象即初始样式对象，亦可通过[setStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#setstyle)接口再叠加新样式或更新已有样式，同时需要在附加的文本组件controller上主动触发更新绑定的属性字符串。

import { drawing } from '@kit.ArkGraphics2D';

let gUIContext: UIContext;

class MyCustomSpan extends CustomSpan {
  constructor(word: string, width: number, height: number, fontSize: number) {
    super();
    this.word = word;
    this.width = width;
    this.height = height;
    this.fontSize = fontSize;
  }

  onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics {
    return { width: this.width, height: this.height };
  }

  onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
    let canvas = context.canvas;

    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 0,
      green: 0,
      blue: 0
    });
    const font = new drawing.Font();
    font.setSize(gUIContext.vp2px(this.fontSize));
    const textBlob =
      drawing.TextBlob.makeFromString(this.word.substring(0, 5), font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
    canvas.attachBrush(brush);

    this.onDrawRectByRadius(context, options.x, options.x + gUIContext.vp2px(this.width), options.lineTop,
      options.lineBottom, 20);
    brush.setColor({
      alpha: 255,
      red: 255,
      green: 255,
      blue: 255
    });
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, options.x, options.lineBottom - 30);
    brush.setColor({
      alpha: 255,
      red: 255,
      green: 228,
      blue: 196
    });
    canvas.attachBrush(brush);
    const textBlob1 =
      drawing.TextBlob.makeFromString(this.word.substring(5), font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
    canvas.drawTextBlob(textBlob1, options.x + gUIContext.vp2px(100), options.lineBottom - 30);

    canvas.detachBrush();
  }

  onDrawRectByRadius(context: DrawContext, left: number, right: number, top: number, bottom: number, radius: number) {
    let canvas = context.canvas;
    let path = new drawing.Path();

    // 画带radius的rect
    path.moveTo(left + radius, top);
    path.lineTo(right - radius, top);
    path.arcTo(right - 2 \* radius, top, right, top + 2 \* radius, 270, 90);
    path.lineTo(right, bottom - radius);
    path.arcTo(right - 2 \* radius, bottom - 2 \* radius, right, bottom, 0, 90);

    path.lineTo(left + 2 \* radius, bottom);
    path.arcTo(left, bottom - 2 \* radius, left + 2 \* radius, bottom, 90, 90);
    path.lineTo(left, top + 2 \* radius);
    path.arcTo(left, top, left + 2 \* radius, top + 2 \* radius, 180, 90);

    canvas.drawPath(path);
  }

  setWord(word: string) {
    this.word = word;
  }

  public width: number = 160;
  public word: string = 'drawing';
  public height: number = 10;
  public fontSize: number = 16;
}

@Entry
@Component
export struct StyledStringGestureStyle {
  customSpan3: MyCustomSpan = new MyCustomSpan('99VIP88%off', 200, 40, 30);
  customSpanStyledString: MutableStyledString = new MutableStyledString(this.customSpan3);
  textController: TextController = new TextController();
  isPageShow: boolean = true;
  @State backgroundColor1: ResourceColor | undefined = undefined;
  gestureStyleAttr: GestureStyle = new GestureStyle({
    onClick: () => {
      this.backgroundColor1 = Color.Green;
    },
    onLongPress: () => {
      this.backgroundColor1 = Color.Grey;
    }
  });

  aboutToAppear() {
    gUIContext = this.getUIContext();
  }

  async onPageShow() {
    if (!this.isPageShow) {
      return;
    }
    this.isPageShow = false;
    this.customSpanStyledString.setStyle({
      start: 0,
      length: 1,
      styledKey: StyledStringKey.GESTURE,
      styledValue: this.gestureStyleAttr
    })
    this.textController.setStyledString(this.customSpanStyledString);
  }

  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Row() {
            Column() {
              // 请将$r('app.string.StyledStringGestureStyle\_button\_content')替换为实际资源文件，在本示例中该资源文件的value值为"响应属性字符串事件改变背景色"
              Button($r('app.string.StyledStringGestureStyle\_button\_content'))
                .backgroundColor(this.backgroundColor1)
                .width('80%')
                .margin(10)
              Text(undefined, { controller: this.textController })
                .id('text1')
                .copyOption(CopyOptions.InApp)
                .fontSize(30)
            }
            .width('100%')
          }
          .height('100%')
        }
        // ...
    }
    .backgroundColor('#f1f2f3')
    // 请将$r('app.string.TStyledStringGestureStyle\_title')替换为实际资源文件，在本示例中该资源文件的value值为"设置事件"
    .title($r('app.string.TStyledStringGestureStyle\_title'))
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/4PBwaOjITD-Z7Mn_5fr1RQ/zh-cn_image_0000002569018487.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D73E40317DB10D637BC57121042D826489E0A5714613240B91A7722998663ECC)

#### 格式转换

可以通过[toHtml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#tohtml14)、[fromHtml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#fromhtml)接口实现属性字符串与HTML格式字符串的相关转换，当前支持转换的HTML标签范围：<p>、<span>、<img>、<br>、<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>。

-   以下示例展示了如何将属性字符串转换成HTML格式，并展示了如何从HTML格式转换回属性字符串。

// xxx.ets
import { image } from '@kit.ImageKit';
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
export struct StyledStringHtml {
  imagePixelMap: image.PixelMap | undefined = undefined;
  @State html: string | undefined = undefined;
  @State styledString: StyledString | undefined = undefined;
  controller1: TextController = new TextController;
  controller2: TextController = new TextController;
  private uiContext: UIContext = this.getUIContext();

  async aboutToAppear() {
    console.info('aboutToAppear initial imagePixelMap');
    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.startIcon'));
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.uiContext.getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Column() {
            Text(undefined, { controller: this.controller1 }).height(100)
            Row() {
              // 请将$r('app.string.StyledStringHtml\_Button\_1')替换为实际资源文件，在本示例中该资源文件的value值为"添加属性字符串"
              Button($r('app.string.StyledStringHtml\_Button\_1')).onClick(() => {
                // 请将$r('app.string.StyledStringHtml\_Text\_1')替换为实际资源文件，在本示例中该资源文件的value值为"属性字符串"
                let mutableStyledString1: MutableStyledString =
                  new MutableStyledString(this.getUIContext()
                    .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringHtml\_Text\_1').id), \[{
                  start: 0,
                  length: 6,
                  styledKey: StyledStringKey.FONT,
                  styledValue: new TextStyle({ fontColor: Color.Green, fontSize: LengthMetrics.px(50) })
                }\]);
                if (this.imagePixelMap !== undefined) {
                  let mutableStyledString2 = new MutableStyledString(new ImageAttachment({
                    value: this.imagePixelMap,
                    size: { width: 50, height: 50 },
                  }));
                  mutableStyledString1.appendStyledString(mutableStyledString2);
                }
                this.styledString = mutableStyledString1;
                this.controller1.setStyledString(mutableStyledString1);
              }).margin(5)
              // 请将$r('app.string.StyledStringHtml\_Button\_2')替换为实际资源文件，在本示例中该资源文件的value值为"toHtml"
              Button($r('app.string.StyledStringHtml\_Button\_2')).onClick(() => {
                this.html = StyledString.toHtml(this.styledString);
              }).margin(5)
              // 请将$r('app.string.StyledStringHtml\_Button\_3')替换为实际资源文件，在本示例中该资源文件的value值为"fromHtml"
              Button($r('app.string.StyledStringHtml\_Button\_3')).onClick(async () => {
                let styledString = await StyledString.fromHtml(this.html);
                this.controller2.setStyledString(styledString);
              }).margin(5)
            }

            Text(undefined, { controller: this.controller2 }).height(100)
            Text(this.html)
          }.width('100%')
        }
        // ...
    }
    .backgroundColor('#f1f2f3')
    // 请将$r('app.string.StyledStringHtml\_title')替换为实际资源文件，在本示例中该资源文件的value值为"格式转换"
    .title($r('app.string.StyledStringHtml\_title'))
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/69eGmIp7Romo-IVgKug1Ug/zh-cn_image_0000002568898477.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D5F25E672488A04DAE5E8753E67D525BF4A03DEC636F7EB9A9F64D4E10F622ED)

-   将HTML中<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>标签及其style属性中的background-color转换为属性字符串并转回HTML。
    
    // xxx.ets
    @Entry
    @Component
    struct HtmlSpanStringDemo {
      @State html: string =
        "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span style =   \\"foreground-color:blue\\"> <a href='https://www.example.com'>www.example</a> </span> <span   style=\\"background-color: red;\\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>";
      @State spanString: StyledString | undefined = undefined;
      @State resultText: string = ''; // 保存结果文本的状态
      controller: TextController = new TextController;
    
      build() {
        Column() {
          // 显示转换后的spanString
          Text(undefined, { controller: this.controller }).height(100).id('text1')
    
          // TextArea显示每个步骤的结果
          TextArea({ text: this.html })
            .width('100%')
            .height(100)
            .margin(5)
    
          // 按钮1:将HTML转换为SpanString
          // 请将$r('app.string.Converted\_HTML\_to\_SpanString')替换为实际资源文件，在本示例中该资源文件的value值为"Converted HTML to SpanString"
          Button($r('app.string.Converted\_HTML\_to\_SpanString')).onClick(async () => {
            this.spanString = await StyledString.fromHtml(this.html);
            this.controller.setStyledString(this.spanString);
            this.resultText = 'Converted HTML to SpanString successfully.';
          }).margin(5)
    
          // 按钮2:将SpanString转换为HTML
          // 请将$r('app.string.Converted\_SpanString\_to\_HTML')替换为实际资源文件，在本示例中该资源文件的value值为"Converted SpanString to HTML"
          Button($r('app.string.Converted\_SpanString\_to\_HTML')).onClick(() => {
            if (this.spanString) {
              // 将spanString转换为HTML并替换当前的HTML状态
              const newHtml = StyledString.toHtml(this.spanString);
              if (newHtml !== this.html) { // 通过检查内容是否已经相同来防止重复
                this.html = newHtml;
              }
              this.resultText = 'Converted SpanString to HTML successfully.';
            } else {
              this.resultText = 'SpanString is undefined.';
            }
          }).margin(5)
    
          // 按钮3:将HTML转换回SpanString
          /\* 请将$r('app.string.Converted\_HTML\_back\_to\_SpanString')替换为实际资源文件，在本示例中该资源文件的
           value值为"Converted HTML back to SpanString" \*/
          Button($r('app.string.Converted\_HTML\_back\_to\_SpanString')).onClick(async () => {
            this.spanString = await StyledString.fromHtml(this.html);
            this.controller.setStyledString(this.spanString);
            this.resultText = 'Converted HTML back to SpanString successfully.';
          }).margin(5)
    
          // 重置：重置HTML和SpanString
          // 请将$r('app.string.Reset')替换为实际资源文件，在本示例中该资源文件的value值为"Reset"
          Button($r('app.string.Reset')).onClick(() => {
            this.html =
              "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span   style = \\"foreground-color:blue\\"> <a href='https://www.example.com'>www.example</a> </span> <span   style=\\"background-color: red;\\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>";
            this.spanString = undefined;
            this.controller.setStyledString(new StyledString('')); // 使用空的StyledString实例
            this.resultText = 'Reset HTML and SpanString successfully.';
          }).margin(5)
        }.width('100%').padding(20)
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/GKNPZnz2S8-x769DkSpSuQ/zh-cn_image_0000002538018772.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F4264594F708AE7673F70658BBE3ED338C7A48A37B7942306CBFA9102A629E9C)
    

#### 场景示例

该示例通过ParagraphStyle、LineHeightStyle、TextStyle对象展示了会员过期提示的效果。

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
export struct StyledStringSceneExample {
  alignCenterParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });
  //行高样式对象
  lineHeightStyle1: LineHeightStyle = new LineHeightStyle(LengthMetrics.vp(24));
  //Bold样式
  boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });
  //创建含段落样式的对象paragraphStyledString1
  // 请将$r('app.string.StyledStringSceneExample\_Text\_1')替换为实际资源文件，在本示例中该资源文件的value值为"您的豪华钻石已过期1天\\n续费可继续享受会员专属权益"
  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample\_Text\_1').id), \[
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH\_STYLE,
        styledValue: this.alignCenterParagraphStyleAttr
      },
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.LINE\_HEIGHT,
        styledValue: new LineHeightStyle(LengthMetrics.vp(40))
      },
      {
        start: 11,
        length: 14,
        styledKey: StyledStringKey.FONT,
        styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontColor: Color.Grey })
      },
      {
        start: 11,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH\_STYLE,
        styledValue: this.alignCenterParagraphStyleAttr
      },
      {
        start: 11,
        length: 4,
        styledKey: StyledStringKey.LINE\_HEIGHT,
        styledValue: this.lineHeightStyle1
      }
    \]);
  // 请将$r('app.string.StyledStringSceneExample\_Text\_2')替换为实际资源文件，在本示例中该资源文件的value值为"\\n￥4.88￥15"
  paragraphStyledString2: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample\_Text\_2').id), \[
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.PARAGRAPH\_STYLE,
      styledValue: this.alignCenterParagraphStyleAttr
    },
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.LINE\_HEIGHT,
      styledValue: new LineHeightStyle(LengthMetrics.vp(60))
    },
    {
      start: 0,
      length: 6,
      styledKey: StyledStringKey.FONT,
      styledValue: this.boldTextStyle
    },
    {
      start: 1,
      length: 1,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18) })
    },
    {
      start: 2,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(40) })
    },
    {
      start: 6,
      length: 3,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14) })
    },
    {
      start: 6,
      length: 3,
      styledKey: StyledStringKey.DECORATION,
      styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough, color: Color.Grey })
    }
  \]);
  // 请将$r('app.string.StyledStringSceneExample\_Text\_3')替换为实际资源文件，在本示例中该资源文件的value值为"\\n02时06分后将失去该优惠"
  paragraphStyledString3: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample\_Text\_3').id), \[
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.PARAGRAPH\_STYLE,
      styledValue: this.alignCenterParagraphStyleAttr
    },
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.LINE\_HEIGHT,
      styledValue: new LineHeightStyle(LengthMetrics.vp(30))
    },
    {
      start: 1,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: '#FFD700', fontWeight: FontWeight.Bold })
    },
    {
      start: 4,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: '#FFD700', fontWeight: FontWeight.Bold })
    }
  \]);
  controller: TextController = new TextController();

  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Row() {
            Column({ space: 5 }) {
              Text(undefined, { controller: this.controller })
                .id('text1')
                .width(240)
                .copyOption(CopyOptions.InApp)
                .draggable(true)
                .onAppear(() => {
                  this.paragraphStyledString2.appendStyledString(this.paragraphStyledString3);
                  this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
                  this.controller.setStyledString(this.paragraphStyledString1);
                })
              // 请将$r('app.string.StyledStringSceneExample\_Button\_1')替换为实际资源文件，在本示例中该资源文件的value值为"限时4.88元 立即续费"
              Button($r('app.string.StyledStringSceneExample\_Button\_1'))
                .width(200)
                .fontColor(Color.White)
                .fontSize(18)
                .backgroundColor('#3CB371')
                .margin({ bottom: 10 })
            }
            .borderWidth(1).borderColor('#FFDEAD')
            .margin({ left: 10 })
          }
          .height('60%')
        }
        // ...
    }
    .backgroundColor('#f1f2f3')
    // 请将$r('app.string.StyledStringSceneExample\_title')替换为实际资源文件，在本示例中该资源文件的value值为"场景示例"
    .title($r('app.string.StyledStringSceneExample\_title'))
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/EHVcXozgSxG5rNe3vFcw-w/zh-cn_image_0000002538178700.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C70AED2F8208FC4DB022534685B8ACF08C1B70C267CD2295EF91E4F9A5100F75)
