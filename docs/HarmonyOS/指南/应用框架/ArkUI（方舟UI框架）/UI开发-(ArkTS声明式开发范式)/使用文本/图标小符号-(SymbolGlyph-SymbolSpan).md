---
title: "图标小符号 (SymbolGlyph/SymbolSpan)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-symbol"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "使用文本"
  - "图标小符号 (SymbolGlyph/SymbolSpan)"
captured_at: "2026-04-17T01:35:37.682Z"
---

# 图标小符号 (SymbolGlyph/SymbolSpan)

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参考[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)和[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)组件的API文档。

#### 创建图标

SymbolGlyph通过$r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

相关资源可参考[系统图标](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。

SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
  .fontSize(96)
  .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  .fontColor(\[Color.Black, Color.Green, Color.White\])

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/wrfkWD6-QyOwi2rD0qp2Qw/zh-cn_image_0000002568898463.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C94A969DF6E812A1B5B45BC2D5428B335B427A8C97F9A92320E48EDB1B9410E4)

#### 添加到文本中

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

-   创建SymbolSpan。
    
    SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。
    
    Text() {
      SymbolSpan($r('sys.symbol.ohos\_trash'))
        .fontWeight(FontWeight.Normal)
        .fontSize(96)
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/w6LaDUiESlO34vKYjBeSYQ/zh-cn_image_0000002538018758.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=B9604C0F715996D3D16DF97E1EB40A4A9C4666F4D4F282F5405E7B048442454C)
    
-   通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。
    
    Row() {
      Column() {
        Text('48')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(48)
            .renderingStrategy(SymbolRenderingStrategy.SINGLE)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }
      }
    
      Column() {
        Text('72')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(72)
            .renderingStrategy(SymbolRenderingStrategy.SINGLE)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }
      }
    
      Column() {
        Text('96')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.SINGLE)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/uZTsKOz6RhezWauisZNgnw/zh-cn_image_0000002538178686.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DBE764F4449437675C9E2A05EF7B84C03C818E6128D063E5130DD13C54E4A4F0)
    
-   通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。
    
    Row() {
      Column() {
        Text('Light')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_trash'))
            .fontWeight(FontWeight.Lighter)
            .fontSize(96)
        }
      }
    
      Column() {
        Text('Normal')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_trash'))
            .fontWeight(FontWeight.Normal)
            .fontSize(96)
        }
      }
    
      Column() {
        Text('Bold')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_trash'))
            .fontWeight(FontWeight.Bold)
            .fontSize(96)
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/60uut517RPeIgAjwDiODhA/zh-cn_image_0000002569018475.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=6086A750DA6237790B98CA8B2E52A61127A91C8EAB611D43CA0C9FC0673E9D27)
    
-   通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。
    
    Row() {
      Column() {
        Text('Black')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .fontColor(\[Color.Black\])
        }
      }
    
      Column() {
        Text('Green')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .fontColor(\[Color.Green\])
        }
      }
    
      Column() {
        Text('Pink')
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .fontColor(\[Color.Pink\])
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/iG1PaYNMQpu-kSuRCia1nw/zh-cn_image_0000002568898465.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=9247AFE045B073C161BA02C76B39B29F2C1629A76FBFBE33DF3501C619548E0B)
    
-   通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。
    
    Row() {
      Column() {
        // 请将$r('app.string.single\_color')替换为实际资源文件，在本示例中该资源文件的value值为"单色"
        Text($r('app.string.single\_color'));
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.SINGLE)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }
      }
    
      Column() {
        // 请将$r('app.string.multi\_color')替换为实际资源文件，在本示例中该资源文件的value值为"多色"
        Text($r('app.string.multi\_color'));
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }
      }
    
      Column() {
        // 请将$r('app.string.hierarchical')替换为实际资源文件，在本示例中该资源文件的value值为"分层"
        Text($r('app.string.hierarchical'));
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/myc-nK5uSmulWmdABCNVUg/zh-cn_image_0000002538018760.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F4C0DB8D52BE0283879AA7C23830A35545344064E557638A9ADA6F81F562AC32)
    
-   通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。
    
    Row() {
      Column() {
        // 请将$r('app.string.no\_action')替换为实际资源文件，在本示例中该资源文件的value值为"无动效"
        Text($r('app.string.no\_action'));
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.NONE)
        }
      }
    
      Column() {
        // 请将$r('app.string.overall\_scaling\_animation\_effect')替换为实际资源文件，在本示例中该资源文件的value值为"整体缩放动效"
        Text($r('app.string.overall\_scaling\_animation\_effect'));
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.SCALE)
        }
      }
    
      Column() {
        // 请将$r('app.string.hierarchical\_animation')替换为实际资源文件，在本示例中该资源文件的value值为"层级动效"
        Text($r('app.string.hierarchical\_animation'));
        Text() {
          SymbolSpan($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/3UQmj5O2RaSCnKICjiJQkQ/zh-cn_image_0000002538178688.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=AE0A0C286CA477C4A664821449AB7D0548DE69F07A58D5C9667AC722E1794281)
    
-   SymbolSpan不支持通用事件。
    

#### 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

-   通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。
    
    @State isActive: boolean = true;
    
    Column() {
      // 请将$r('app.string.variable\_color\_animation')替换为实际资源文件，在本示例中该资源文件的value值为"可变颜色动效"
      Text($r('app.string.variable\_color\_animation'));
      SymbolGlyph($r('sys.symbol.ohos\_wifi'))
        .fontSize(96)
        .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
      // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
      // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
      Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
        this.isActive = !this.isActive;
      })
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/AuvqK9QzQ5KHy2Wiwrw8dw/zh-cn_image_0000002569018477.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=51C408B4CE2510DE4CA10E09355AFB3EA45380C4C804E89BDBBBE94EDFB5249F)
    
-   通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。
    
    @State triggerValueReplace: number = 0;
    
    Column() {
      // 请将$r('app.string.bounce\_animation')替换为实际资源文件，在本示例中该资源文件的value值为"弹跳动效"
      Text($r('app.string.bounce\_animation'));
      SymbolGlyph($r('sys.symbol.ellipsis\_message\_1'))
        .fontSize(96)
        .fontColor(\[Color.Gray\])
        .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),
                      this.triggerValueReplace)
      Button('trigger').onClick(() => {
        this.triggerValueReplace = this.triggerValueReplace + 1;
      })
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ER_HxD8oRF2YOa2cecETsQ/zh-cn_image_0000002568898467.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=35EF9EAB1E235650F278F1DD06E98606A75D383B327CB90DCC6B4786384C6C04)
    
-   从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH\_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。
    
    @State triggerValueReplace: number = 0;
    replaceFlag: boolean = true;
    @State renderMode: number = 1;
    
    Column() {
      // 请将$r('app.string.disable\_animation')替换为实际资源文件，在本示例中该资源文件的value值为"禁用动效"
      Text($r('app.string.disable\_animation'));
      SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye\_slash') : $r('sys.symbol.eye'))
        .fontSize(96)
        .renderingStrategy(this.renderMode)
        .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH\_OVERLAY),
                      this.triggerValueReplace)
      Button('trigger').onClick(() => {
        this.replaceFlag = !this.replaceFlag;
        this.triggerValueReplace = this.triggerValueReplace + 1;
      })
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/qj2qLG4jTjagyUSq1cibeQ/zh-cn_image_0000002538018762.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=6B5CE75D974250961FF527B3528803CB655FB74C92E44106F7B369CE583C0FCC)
    
-   从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS\_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。
    
    @State triggerValueReplace: number = 0;
    replaceFlag: boolean = true;
    
    Column() {
      // 请将$r('app.string.quick\_replacement\_animation')替换为实际资源文件，在本示例中该资源文件的value值为"快速替换动效"
      Text($r('app.string.quick\_replacement\_animation'));
      SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark\_circle') : $r('sys.symbol.repeat\_1'))
        .fontSize(96)
        .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS\_FADE),
                      this.triggerValueReplace)
      Button('trigger').onClick(() => {
        this.replaceFlag = !this.replaceFlag;
        this.triggerValueReplace = this.triggerValueReplace + 1;
      })
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/GK5fNBgjSMug1--MgyEUeA/zh-cn_image_0000002538178690.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F6A711706DAAC117CF1030474AA79BA1FBB983165712DD7235FB1683753B790C)
    

#### 设置阴影和渐变色

-   从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。
    
    @State isActive: boolean = true;
    
    options: ShadowOptions = {
      radius: 10.0,
      color: Color.Blue,
      offsetX: 10,
      offsetY: 10,
    };
    
    Column() {
      // 请将$r('app.string.shadow\_ability')替换为实际资源文件，在本示例中该资源文件的value值为"阴影能力"
      Text($r('app.string.shadow\_ability'));
      SymbolGlyph($r('sys.symbol.ohos\_wifi'))
        .fontSize(96)
        .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)
        .symbolShadow(this.options)
      // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
      // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
      Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
        this.isActive = !this.isActive;
      })
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/nKpgRIghQEWbk5iAwZH8Zg/zh-cn_image_0000002569018479.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3DC850960A9CD6862EBA29B9FEF2A5DA68D0AA3E3198080EDE3421B0D32DA4B4)
    
-   从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。
    
    radialGradientOptions: RadialGradientOptions = {
      center: \['50%', '50%'\],
      radius: '20%',
      colors: \[\[Color.Red, 0.0\], \[Color.Blue, 0.3\], \[Color.Green, 0.5\]\],
      repeating: true,
    };
    
    Column() {
      // 请将$r('app.string.radial\_gradient')替换为实际资源文件，在本示例中该资源文件的value值为"径向渐变"
      Text($r('app.string.radial\_gradient'))
        .fontSize(18)
        .fontColor(0xCCCCCC)
        .textAlign(TextAlign.Center)
      SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
        .fontSize(96)
        .shaderStyle(\[new RadialGradientStyle(this.radialGradientOptions)\])
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/CU39hKYNTUSJET05R43FKA/zh-cn_image_0000002568898469.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=BF5ED552CD15D3203EC95AE74AD66EEAE467A856E660F84A99C5CF2282F92C11)
    

#### 添加事件

SymbolGlyph组件可以添加通用事件，例如绑定[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)等事件来响应操作。

@State wifiColor: ResourceColor = Color.Black;

SymbolGlyph($r('sys.symbol.ohos\_wifi'))
  .fontSize(96)
  .fontColor(\[this.wifiColor\])
  .onClick(() => {
    this.wifiColor = Color.Gray;
  })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/eRdwRhuETTioV0BHWXrc7g/zh-cn_image_0000002538018764.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=FC5BC50349090AD306E7E330B04D03074B2192E45D67717BCC95599B9E013E11)

#### 场景示例

该示例通过symbolEffect、fontSize、fontColor属性展示了播放列表的效果。

// resourceGetString封装工具，从资源中获取字符串
import resourceGetString from '../../common/resource';

@Entry
@Component
struct SymbolMusicDemo {
  @State triggerValueReplace: number = 0;
  @State symbolSources: Resource\[\] =
    \[$r('sys.symbol.repeat'), $r('sys.symbol.repeat\_1'), $r('sys.symbol.arrow\_left\_arrow\_right')\];
  @State symbolSourcesIndex: number = 0;
  @State symbolText: string\[\] = \[
    // 请将$r('app.string.play\_in\_order')替换为实际资源文件，在本示例中该资源文件的value值为"顺序播放"
    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.play\_in\_order').id),
    // 请将$r('app.string.play\_in\_single\_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"单曲循环"
    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.play\_in\_single\_repeat').id),
    // 请将$r('app.string.shuffle\_play')替换为实际资源文件，在本示例中该资源文件的value值为"随机播放"
    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.shuffle\_play').id),
  \];
  @State symbolTextIndex: number = 0;
  @State fontColorValue: ResourceColor = Color.Grey;
  @State fontColorValue1: ResourceColor = '#E8E8E8';

  build() {
    Column({ space: 10 }) {
      Row() {
        Text() {
          // 请将$r('app.string.current\_playlist')替换为实际资源文件，在本示例中该资源文件的value值为"当前播放列表"
          Span(this.getUIContext()
            .getHostContext()!.resourceManager.getStringSync($r('app.string.current\_playlist').id))
            .fontSize(20)
            .fontWeight(FontWeight.Bolder)
          Span('（101）')
        }
      }

      Row() {
        Row({ space: 5 }) {
          SymbolGlyph(this.symbolSources\[this.symbolSourcesIndex\])
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
            .fontSize(20)
            .fontColor(\[this.fontColorValue\])
          Text(this.symbolText\[this.symbolTextIndex\])
            .fontColor(this.fontColorValue)
        }
        .onClick(() => {
          this.symbolTextIndex++;
          this.symbolSourcesIndex++;
          this.triggerValueReplace++;
          if (this.symbolSourcesIndex > (this.symbolSources.length - 1)) {
            this.symbolSourcesIndex = 0;
            this.triggerValueReplace = 0;
          }
          if (this.symbolTextIndex > (this.symbolText.length - 1)) {
            this.symbolTextIndex = 0;
          }
        })
        .width('75%')

        Row({ space: 5 }) {
          Text() {
            SymbolSpan($r('sys.symbol.arrow\_down\_circle\_badge\_vip\_circle\_filled'))
              .fontColor(\[this.fontColorValue\])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.heart\_badge\_plus'))
              .fontColor(\[this.fontColorValue\])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.ohos\_trash'))
              .fontColor(\[this.fontColorValue\])
              .fontSize(20)
          }
        }
        .width('25%')
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲一"
          Text($r('app.string.song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play\_arrow\_triangle\_2\_circlepath'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song\_again')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲二"
          Text($r('app.string.song\_again'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play\_arrow\_triangle\_2\_circlepath'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.again\_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲三"
          Text($r('app.string.again\_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play\_arrow\_triangle\_2\_circlepath'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song\_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲四"
          Text($r('app.string.song\_repeat'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play\_arrow\_triangle\_2\_circlepath'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.repeat\_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲五"
          Text($r('app.string.repeat\_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play\_arrow\_triangle\_2\_circlepath'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song\_play')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲六"
          Text($r('app.string.song\_play'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play\_arrow\_triangle\_2\_circlepath'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.play\_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲七"
          Text($r('app.string.play\_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play\_arrow\_triangle\_2\_circlepath'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor(\[this.fontColorValue\])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Column() {
        // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
        Text($r('app.string.off'))
      }
      .alignItems(HorizontalAlign.Center)
      .width('98%')
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
    .height(400)
    .padding({
      left: 10,
      top: 10
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/oCB-4nr4QuaXvhvLYDH4Qw/zh-cn_image_0000002538178692.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F1F6E0AD8D26C20A5834F93D19B5DEC7D14365020BB94C7E69888A81021D4530)
