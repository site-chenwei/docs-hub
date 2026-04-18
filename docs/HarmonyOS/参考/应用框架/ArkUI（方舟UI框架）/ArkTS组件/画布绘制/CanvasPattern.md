---
title: "CanvasPattern"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "画布绘制"
  - "CanvasPattern"
captured_at: "2026-04-17T01:47:57.933Z"
---

# CanvasPattern

一个Object对象，使用[createPattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#createpattern)方法创建，通过指定图像和重复方式创建图片填充的模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/E_3jSpo6StGE-Gr-oAv6iw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=9C264D3B5865834BAAE859A2850CE18F238750AB827041545EA60888B1E6C07B)

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 方法

#### \[h2\]setTransform

setTransform(transform?: Matrix2D): void

使用Matrix2D对象作为参数，对当前CanvasPattern进行矩阵变换。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| transform | [Matrix2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-matrix2d) | 否 | 
转换矩阵。

异常值undefined和null按无效值不做矩阵变换处理。

默认值：不做矩阵变换

 |

#### 示例

通过setTransform对当前CanvasPattern进行矩阵变换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/sQF-V596TCitSP38w7zi7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=78D29B362FA82AA51E015898346C4C668ABD8B7B0F307E069ACC18C7427C079A)

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356)相关介绍。

```ts
// xxx.ets
@Entry
@Component
struct CanvasPatternPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();
  // "common/pattern.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/pattern.jpg");
  private pattern: CanvasPattern | null = null;

  build() {
      Column() {
        Button("Click to set transform")
          .onClick(() => {
            this.matrix.scaleY = 1
            this.matrix.scaleX = 1
            this.matrix.translateX = 50
            this.matrix.translateY = 200
            if (this.pattern) {
              this.pattern.setTransform(this.matrix)
            }
            this.context.fillRect(0, 0, 480, 720)
          })
          .width("45%")
          .margin("5px")
        Canvas(this.context)
          .width('100%')
          .height('80%')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            this.pattern = this.context.createPattern(this.img, 'no-repeat')
            this.matrix.scaleY = 0.5
            this.matrix.scaleX = 0.5
            this.matrix.translateX = 50
            this.matrix.translateY = 50
            if (this.pattern) {
              this.context.fillStyle = this.pattern
              this.pattern.setTransform(this.matrix)
            }
            this.context.fillRect(0, 0, 480, 720)
          })
      }
      .width('100%')
      .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/bW8VUApTS0O4MgQKGCCBFg/zh-cn_image_0000002538180806.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=0685D2A05B1C7B35CCC56F6630B2D8259F6EA08BE8EBC15703159B1973985E77)
