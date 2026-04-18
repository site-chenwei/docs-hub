---
title: "@Extend装饰器：定义扩展组件样式"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "学习UI范式基本语法"
  - "组件扩展"
  - "@Extend装饰器：定义扩展组件样式"
captured_at: "2026-04-17T01:35:36.012Z"
---

# @Extend装饰器：定义扩展组件样式

在前文的示例中，可以使用[@Styles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style)用于样式的重用，在@Styles的基础上，我们提供了@Extend，用于扩展组件样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/trYYcZTNQzWxzCZmUtLotw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=FA2AEC1E51BF5B483D71B4F880FC1EFA4661AC5EC4FB38293EE4867EBCF1CA2B)

从API version 9开始支持。

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

#### 装饰器使用说明

#### \[h2\]语法

```ts
@Extend(UIComponentName) function functionName { ... }
```

#### \[h2\]使用规则

-   和@Styles不同，@Extend支持封装指定组件的私有属性、私有事件和自身定义的全局方法。
    
    // @Extend(Text)可以支持Text的私有属性fontColor
    @Extend(Text)
    function fancy() {
      .fontColor(Color.Red)
    }
    
    // superFancyText可以调用预定义的fancy
    @Extend(Text)
    function superFancyText(size: number) {
      .fontSize(size)
      .fancy()
    }
    
-   使用@Extend封装指定组件的私有属性、私有事件和自身定义的全局方法时，不支持和@Styles混用。
    
    ```typescript
    @Styles
    function fancy() {
      .backgroundColor(Color.Red)
    }
    
    // superFancyText不可以调用预定义的fancy
    @Extend(Text)
    function superFancyText(size: number) {
      .fontSize(size)
      .fancy()
    }
    ```
    
-   和@Styles不同，@Extend装饰的方法支持传入参数，调用遵循TS方法传值调用。
    
    // xxx.ets
    @Extend(Text)
    function fancy(fontSize: number) {
      .fontColor(Color.Red)
      .fontSize(fontSize)
    }
    
    @Entry
    @Component
    struct FancyUse {
      build() {
        Row({ space: 10 }) {
          Text('Fancy')
            .fancy(16)
          Text('Fancy')
            .fancy(24)
        }
      }
    }
    
-   @Extend装饰的方法的参数可以为function，作为Event事件的句柄。
    
    @Extend(Text)
    function makeMeClick(onClick: () => void) {
      .backgroundColor(Color.Blue)
      .onClick(onClick)
    }
    
    @Entry
    @Component
    struct FancyUse {
      @State label: string = 'Hello World';
    
      onClickHandler() {
        this.label = 'Hello ArkUI';
      }
    
      build() {
        Row({ space: 10 }) {
          Text(\`${this.label}\`)
            .makeMeClick(() => {
              this.onClickHandler();
            })
        }
      }
    }
    
-   @Extend的参数可以为[状态变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview)，当状态变量改变时，UI可以正常的被刷新渲染。
    
    @Extend(Text)
    function fancy(fontSize: number) {
      .fontColor(Color.Blue)
      .fontSize(fontSize)
    }
    
    @Entry
    @Component
    struct FancyUse {
      @State fontSizeValue: number = 20;
    
      build() {
        Column({ space: 10 }) {
          Text('Fancy')
            .fancy(this.fontSizeValue)
            .onClick(() => {
              this.fontSizeValue = 30;
            })
        }
        .width('100%')
      }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/yK0ve_wsT-W2WovCC-TWaw/zh-cn_image_0000002569018215.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=E1DF744C0E63749DD90C36E131BFBBC6ACCBD711162C8A58C966C27D0DDD3E83)

#### 限制条件

-   和@Styles不同，@Extend仅支持在全局定义，不支持在组件内部定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/DfF_QAwQRnKhyJ5GmV1RkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=C4DB55A38D73DA820FB75F22E7EE85F2806E67272A98EB86238BFC7CDD99E816)

仅限在当前文件内使用，不支持导出。

如果要实现export功能，推荐使用[AttributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-attributemodifier)。

【反例】

```ts
@Entry
@Component
struct FancyUse {
  // 错误写法，@Extend仅支持在全局定义，不支持在组件内部定义
  @Extend(Text) function fancy (fontSize: number) {
    .fontSize(fontSize)
  }

  build() {
    Row({ space: 10 }) {
      Text('Fancy')
        .fancy(16)
    }
  }
}
```

【正例】

// 正确写法
@Extend(Text)
function fancy(fontSize: number) {
  .fontSize(fontSize)
}

@Entry
@Component
struct FancyUse {
  build() {
    Row({ space: 10 }) {
      Text('Fancy')
        .fancy(16)
    }
  }
}

#### 使用场景

以下示例声明了3个Text组件，每个Text组件均设置了[fontStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontstyle)、[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontweight) 和[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundcolor)样式。

@Entry
@Component
struct FancyUse {
  @State label: string = 'Hello World';

  build() {
    Row({ space: 10 }) {
      Text(\`${this.label}\`)
        .fontStyle(FontStyle.Italic)
        .fontWeight(500)
        .backgroundColor(Color.Yellow)
      Text(\`${this.label}\`)
        .fontStyle(FontStyle.Italic)
        .fontWeight(600)
        .backgroundColor(Color.Pink)
      Text(\`${this.label}\`)
        .fontStyle(FontStyle.Italic)
        .fontWeight(700)
        .backgroundColor(Color.Orange)
    }.margin('20%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/H7QBF8NyStaKrQ8i7XtV0w/zh-cn_image_0000002568898211.png?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=A79C62107AD042A7AEB178ADDE5A9F682604C67490933A8F647939C260B22B48)

使用@Extend将样式组合复用，示例如下。

@Extend(Text)
function fancyText(weightValue: number, color: Color) {
  .fontStyle(FontStyle.Italic)
  .fontWeight(weightValue)
  .backgroundColor(color)
}

通过@Extend组合样式后，使得代码更加简洁，增强可读性。

@Entry
@Component
struct FancyUse {
  @State label: string = 'Hello World';

  build() {
    Row({ space: 10 }) {
      Text(\`${this.label}\`)
        .fancyText(100, Color.Blue)
      Text(\`${this.label}\`)
        .fancyText(200, Color.Pink)
      Text(\`${this.label}\`)
        .fancyText(300, Color.Orange)
    }.margin('20%')
  }
}
