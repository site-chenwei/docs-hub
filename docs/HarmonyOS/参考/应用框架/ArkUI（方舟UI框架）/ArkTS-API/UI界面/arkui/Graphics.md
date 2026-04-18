---
title: "Graphics"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "arkui"
  - "Graphics"
captured_at: "2026-04-17T01:47:53.517Z"
---

# Graphics

自定义节点相关属性定义的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Ytawz2orTfG0P6HX_GBEvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=9C5941F600A6CB9C23E9A12961342DF88438544BB368CBD6C9F9082A5E258A53)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { DrawContext, Size, Offset, Position, Pivot, Scale, Translation, Matrix4, Rotation, Frame, LengthMetricsUnit } from "@kit.ArkUI";
```

#### Size

用于返回组件布局大小的宽和高。默认单位为vp，不同的接口使用Size类型时会再定义单位，以接口定义的单位为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| width | number | 否 | 否 | 
组件大小的宽度。

单位：vp

取值范围：\[0, +∞)

 |
| height | number | 否 | 否 | 

组件大小的高度。

单位：vp

取值范围：\[0, +∞)

 |

#### Position

type Position = Vector2

用于设置或返回组件的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Vector2](#vector2) | 
包含x和y两个值的向量。

单位：vp

 |

#### PositionT12+

type PositionT<T> = Vector2T<T>

用于设置或返回组件的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Vector2T<T>](#vector2tt12) | 
包含x和y两个值的向量。

单位：vp

 |

#### Frame

用于设置或返回组件的布局大小和位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 
水平方向位置。

单位：vp

取值范围：(-∞, +∞)

 |
| y | number | 否 | 否 | 

垂直方向位置。

单位：vp

取值范围：(-∞, +∞)

 |
| width | number | 否 | 否 | 

组件的宽度。

单位：vp

取值范围：\[0, +∞)

 |
| height | number | 否 | 否 | 

组件的高度。

单位：vp

取值范围：\[0, +∞)

 |

#### Pivot

type Pivot = Vector2

用于设置组件的轴心坐标，轴心会作为组件的旋转/缩放中心点，影响旋转和缩放效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Vector2](#vector2) | 轴心的x和y轴坐标。该参数为浮点数，默认值为0.5， 取值范围为\[0.0, 1.0\]。 |

#### Scale

type Scale = Vector2

用于设置组件的缩放比例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Vector2](#vector2) | x和y轴的缩放参数。该参数为浮点数，默认值为1.0。 |

#### Translation

type Translation = Vector2

用于设置组件的平移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Vector2](#vector2) | 
x和y轴的平移量。

单位：px

 |

#### Rotation

type Rotation = Vector3

用于设置组件的旋转角度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Vector3](#vector3) | 
x、y、z轴方向的旋转角度。

单位：度

 |

#### Offset

type Offset = Vector2

用于设置组件或效果的偏移。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Vector2](#vector2) | 
x和y轴方向的偏移量。

单位：vp

 |

#### Matrix4

type Matrix4 = \[number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number\]

设置四阶矩阵。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| 
\[number,number,number,number,

number,number,number,number,

number,number,number,number,

number,number,number,number\]

 | 

参数为长度为16（4\*4）的number数组。

各number取值范围：(-∞, +∞)

 |

用于设置组件的变换信息，该类型为一个 4x4 矩阵，使用一个长度为16的number\[\]进行表示，例如：

```ts
const transform: Matrix4 = [
  1, 0, 45, 0,
  0, 1,  0, 0,
  0, 0,  1, 0,
  0, 0,  0, 1
]
```

#### Vector2

用于表示包含x和y两个值的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 
向量x轴方向的值。

取值范围：(-∞, +∞)

 |
| y | number | 否 | 否 | 

向量y轴方向的值。

取值范围：(-∞, +∞)

 |

#### Vector3

用于表示包含x、y、z三个值的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 
x轴方向的旋转角度。

取值范围：(-∞, +∞)

 |
| y | number | 否 | 否 | 

y轴方向的旋转角度。

取值范围：(-∞, +∞)

 |
| z | number | 否 | 否 | 

z轴方向的旋转角度。

取值范围：(-∞, +∞)

 |

#### Vector2T<T>12+

用于表示T类型的包含x和y两个值的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | T | 否 | 否 | 向量x轴方向的值。 |
| y | T | 否 | 否 | 向量y轴方向的值。 |

#### DrawContext

图形绘制上下文，提供绘制所需的画布宽度和高度。

#### \[h2\]size

get size(): Size

获取画布的宽度和高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Size](#size) | 画布的宽度和高度。 |

#### \[h2\]sizeInPixel12+

get sizeInPixel(): Size

获取以px为单位的画布的宽度和高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Size](#size) | 画布的宽度和高度，以px为单位。 |

#### \[h2\]canvas

get canvas(): drawing.Canvas

获取用于绘制的画布。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [drawing.Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas) | 用于绘制的画布。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, DrawContext } from "@kit.ArkUI";

class MyRenderNode extends RenderNode {
  flag: boolean = false;

  draw(context: DrawContext) {
    const size = context.size;
    const canvas = context.canvas;
    const sizeInPixel = context.sizeInPixel;
  }
}

const renderNode = new MyRenderNode();
renderNode.frame = { x: 0, y: 0, width: 100, height: 100 };
renderNode.backgroundColor = 0xff519db4;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/o2ZLEgSiRSmVAaARjFPLiA/zh-cn_image_0000002538180324.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=11AB0E8811C6A815926C57CFC501CDBD1A5269D79E071F5131C6D85B925B9C38)

#### Edges<T>12+

用于设置边框的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| left | T | 否 | 否 | 左侧边框的属性。 |
| top | T | 否 | 否 | 顶部边框的属性。 |
| right | T | 否 | 否 | 右侧边框的属性。 |
| bottom | T | 否 | 否 | 底部边框的属性。 |

#### LengthUnit12+

长度属性单位枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PX | 0 | 长度类型，用于描述以px像素单位为单位的长度。 |
| VP | 1 | 长度类型，用于描述以vp像素单位为单位的长度。 |
| FP | 2 | 长度类型，用于描述以fp像素单位为单位的长度。 |
| PERCENT | 3 | 长度类型，用于描述以%像素单位为单位的长度。 |
| LPX | 4 | 长度类型，用于描述以lpx像素单位为单位的长度。 |

#### SizeT<T>12+

用于设置宽高的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| width | T | 否 | 否 | 宽度的属性。 |
| height | T | 否 | 否 | 高度的属性。 |

#### LengthMetricsUnit12+

长度属性单位枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DEFAULT | 0 | 长度类型，用于描述以默认的vp像素单位为单位的长度。 |
| PX | 1 | 长度类型，用于描述以px像素单位为单位的长度。 |

#### LengthMetrics12+

用于设置长度属性，当长度单位为PERCENT时，值为1表示100%。

#### \[h2\]属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| value | number | 否 | 否 | 长度属性的值。 |
| unit | [LengthUnit](#lengthunit12) | 否 | 否 | 长度属性的单位，默认为VP。 |

#### \[h2\]constructor12+

constructor(value: number, unit?: LengthUnit)

LengthMetrics的构造函数。若参数unit不传入值或传入undefined，返回值使用默认单位VP；若unit传入非LengthUnit类型的值，返回默认值0VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 
长度属性的值。

取值范围：\[0, +∞)

 |
| unit | [LengthUnit](#lengthunit12) | 否 | 长度属性的单位。 |

#### \[h2\]px12+

static px(value: number): LengthMetrics

用于生成单位为PX的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 
长度属性的值。

取值范围：(-∞, +∞)

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | LengthMetrics 类的实例。 |

#### \[h2\]vp12+

static vp(value: number): LengthMetrics

用于生成单位为VP的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 
长度属性的值。

取值范围：(-∞, +∞)

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | LengthMetrics 类的实例。 |

#### \[h2\]fp12+

static fp(value: number): LengthMetrics

用于生成单位为FP的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 
长度属性的值。

取值范围：(-∞, +∞)

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | LengthMetrics 类的实例。 |

#### \[h2\]percent12+

static percent(value: number): LengthMetrics

用于生成单位为PERCENT的长度属性，值为1表示100%。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 
长度属性的值。

取值范围：\[0, 1\]

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | LengthMetrics 类的实例。 |

#### \[h2\]lpx12+

static lpx(value: number): LengthMetrics

用于生成单位为LPX的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 
长度属性的值。

取值范围：(-∞, +∞)

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | LengthMetrics 类的实例。 |

#### \[h2\]resource12+

static resource(value: Resource): LengthMetrics

用于生成Resource类型资源的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | Resource | 是 | 长度属性的值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | LengthMetrics 类的实例。 |

**示例：**

使用LengthMetrics设置Row的padding和margin属性。

```ts
import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

@Entry
@Component
struct SizeExample {
  build() {
    Column({ space: 10 }) {
      Text('margin and padding:')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Row() {
        Row() {
          Row()
            .size({ width: '100%', height: '100%' })
            .backgroundColor('#ffd5d5d5')
        }
        .width(80)
        .height(80)
        .padding({
          top: new LengthMetrics(20, LengthUnit.VP),
          bottom: LengthMetrics.px(15),
          start: LengthMetrics.vp(10),
          end: LengthMetrics.fp(20)
        })
        .margin({
          top: LengthMetrics.percent(0.1),
          bottom: LengthMetrics.lpx(20),
          start: LengthMetrics.resource($r('app.float.row_margin_start')),
          end: LengthMetrics.vp(10)
        })
        .backgroundColor(Color.White)
      }
      .backgroundColor("#ff2787d9")
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/KNR8kIsLRaqtfzsQ5WRi-g/zh-cn_image_0000002569020111.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=30E9D77DF3372AB2ACB4A389681E1B416F4C00A609E3D2985AE15DDF892A420F)

#### ColorMetrics12+

用于混合颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]numeric12+

static numeric(value: number): ColorMetrics

使用HEX格式颜色实例化 ColorMetrics 类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 
HEX格式颜色。

取值范围：支持rgb或者argb

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | ColorMetrics 类的实例。 |

#### \[h2\]rgba12+

static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics

使用rgb或者rgba格式颜色实例化 ColorMetrics 类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| red | number | 是 | 颜色的R分量（红色），值是0~255的整数。 |
| green | number | 是 | 颜色的G分量（绿色），值是0~255的整数。 |
| blue | number | 是 | 颜色的B分量（蓝色），值是0~255的整数。 |
| alpha | number | 否 | 
颜色的A分量（透明度），值是0.0~1.0的浮点数，默认值为1.0，不透明。

**说明：** alpha小于0为全透明，大于1为不透明。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | ColorMetrics 类的实例。 |

#### \[h2\]colorWithSpace20+

static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics

使用[ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#colorspace20)和rgba格式颜色实例化ColorMetrics类。仅部分属性支持在display-p3色彩空间中设置颜色。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| colorSpace | [ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#colorspace20) | 是 | 颜色空间，用于指定颜色的色彩空间。使用ColorSpace.DISPLAY\_P3，需要对应窗口调用[setWindowColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowcolorspace9-1)接口，将当前窗口设置为广色域模式。 |
| red | number | 是 | 颜色的R分量（红色），值是0~1的浮动数值。 |
| green | number | 是 | 颜色的G分量（绿色），值是0~1的浮动数值。 |
| blue | number | 是 | 颜色的B分量（蓝色），值是0~1的浮动数值。 |
| alpha | number | 否 | 颜色的A分量（透明度），值是0.0~1.0的浮点数，默认值为1.0，不透明。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | ColorMetrics类的实例。 |

#### \[h2\]resourceColor12+

static resourceColor(color: ResourceColor): ColorMetrics

使用资源格式颜色实例化 ColorMetrics 类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 是 | 资源格式颜色。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | ColorMetrics 类的实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[系统资源错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-system-resource)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible cause:1.The type of the input color parameter is not ResourceColor;2.The format of the input color string is not RGB or RGBA. |
| 180003 | Failed to obtain the color resource. |

#### \[h2\]blendColor12+

blendColor(overlayColor: ColorMetrics): ColorMetrics

在当前颜色的上方叠加上一层指定的颜色（overlayColor），并返回混合后的新颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| overlayColor | [ColorMetrics](#colormetrics12) | 是 | 要叠加在上方的颜色对象。alpha属性决定叠加强度。1.0表示完全覆盖，0.0表示完全透明，混合结果为原色。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | 新的颜色对象，其red、green、blue和alpha通道均为当前颜色与叠加颜色混合后的结果值。 |

**混合公式：**

混合后透明度为完全不透明，rgb按照以下公式计算：

result\_rgb = overlay\_rgb\*(overlay\_alpha) + (1 - overlay\_alpha) \* base\_rgb

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. The type of the input parameter is not ColorMetrics. |

#### \[h2\]color12+

get color(): string

获取ColorMetrics的颜色，返回的是rgba字符串的格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | rgba字符串格式的颜色。 示例：'rgba(255, 100, 255, 0.5)' |

#### \[h2\]red12+

get red(): number

获取ColorMetrics颜色的R分量（红色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 颜色的R分量（红色），值是0~255的整数。 |

#### \[h2\]green12+

get green(): number

获取ColorMetrics颜色的G分量（绿色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 颜色的G分量（绿色），值是0~255的整数。 |

#### \[h2\]blue12+

get blue(): number

获取ColorMetrics颜色的B分量（蓝色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 颜色的B分量（蓝色），值是0~255的整数。 |

#### \[h2\]alpha12+

get alpha(): number

获取ColorMetrics颜色的A分量（透明度）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 颜色的A分量（透明度），值是0~255的整数。 |

**示例：**

```ts
import { ColorMetrics } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

function getBlendColor(baseColor: ResourceColor): ColorMetrics {
  let sourceColor: ColorMetrics;
  try {
    // 在使用ColorMetrics的resourceColor和blendColor需要追加捕获异常处理
    // 可能返回的arkui子系统错误码有401和180003
    // 61 157 180
    sourceColor = ColorMetrics.resourceColor(baseColor).blendColor(ColorMetrics.resourceColor("#083d9db4"));
    console.info(`current color is ${sourceColor.color} r:${sourceColor.red} g:${sourceColor.green} b:${sourceColor.blue} a :${sourceColor.alpha}`);
  } catch (error) {
    console.error("getBlendColor failed, code = " + (error as BusinessError).code + ", message = " +
    (error as BusinessError).message);
    sourceColor = ColorMetrics.resourceColor("#19000000");
  }
  return sourceColor;
}

@Entry
@Component
struct ColorMetricsSample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button("ColorMetrics blendColor")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(getBlendColor("#ff3d9db4").color)
        .margin(10)
      Button("ColorMetrics numeric")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(ColorMetrics.numeric(0xff707070).color)
        .margin(10)
      Button("ColorMetrics rgba")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(ColorMetrics.rgba(0, 74, 175, 255).color)
        .margin(10)
      Button("ColorMetrics colorWithSpace")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.4392, 0.4392, 0.4392).color)
        .margin(10)
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/zgNPrQY-SmqMdjLVozdWZw/zh-cn_image_0000002568900103.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=78C9442D5CD12E3DEE482CFE6DF244D65071E3328FA286805F24EABCEBB77AB0)

#### Corners<T>12+

用于设置四个角的圆角属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| topLeft | T | 否 | 否 | 左上边框的圆角属性。 |
| topRight | T | 否 | 否 | 右上边框的圆角属性。 |
| bottomLeft | T | 否 | 否 | 左下边框的圆角属性。 |
| bottomRight | T | 否 | 否 | 右下边框的圆角属性。 |

#### CornerRadius12+

type CornerRadius = Corners<Vector2>

设置四个角的圆角x轴与y轴的半轴长。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Corners](#cornerst12)<[Vector2](#vector2)\> | 四个角的圆角x轴与y轴的半轴长。 |

#### BorderRadiuses12+

type BorderRadiuses = Corners<number>

设置四个角的圆角半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [Corners](#cornerst12)<number> | 四个角的圆角半径。 |

#### Rect12+

type Rect = common2D.Rect

用于设置矩形的形状。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [common2D.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d#rect) | 矩形区域。 |

#### RoundRect12+

用于设置带有圆角的矩形。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| rect | [Rect](#rect12) | 否 | 否 | 设置矩形的属性。 |
| corners | [CornerRadius](#cornerradius12) | 否 | 否 | 设置圆角的属性。 |

#### Circle12+

用于设置圆形的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| centerX | number | 否 | 否 | 圆心x轴的位置，单位为px。 |
| centerY | number | 否 | 否 | 圆心y轴的位置，单位为px。 |
| radius | number | 否 | 否 | 
圆形的半径，单位为px。

取值范围：\[0, +∞)

 |

#### CommandPath12+

用于设置路径绘制的指令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| [commands](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-path#commands) | string | 否 | 否 | 
路径绘制的指令字符串。像素单位的转换方法请参考[像素单位](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units)。

单位：px

 |

#### ShapeMask12+

用于设置图形遮罩。

#### \[h2\]属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| fillColor | number | 否 | 否 | 
遮罩的填充颜色，使用ARGB格式。默认值为0XFF000000。

通过fillColor的透明度和亮度生成一个仅含透明度的颜色。亮度越高，颜色越透明。然后，使用[BlendMode.SRC\_IN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blendmode)方式与RenderNode本身的颜色混合，生成最终颜色。

 |
| strokeColor | number | 否 | 否 | 

遮罩的边框颜色，使用ARGB格式。默认值为0XFF000000。

通过strokeColor的透明度和亮度生成一个仅含透明度的颜色。亮度越高，颜色越透明。然后，使用[BlendMode.SRC\_IN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blendmode)方式与RenderNode本身的颜色混合，生成最终颜色。

 |
| strokeWidth | number | 否 | 否 | 遮罩的边框宽度，单位为px。默认值为0。 |

#### \[h2\]constructor12+

constructor()

ShapeMask的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setRectShape12+

setRectShape(rect: Rect): void

用于设置矩形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rect | [Rect](#rect12) | 是 | 矩形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    mask.setRectShape({
      left: 0,
      right: uiContext.vp2px(150),
      top: 0,
      bottom: uiContext.vp2px(150)
    });
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = {
      x: 0,
      y: 0,
      width: 150,
      height: 150
    };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/q9v9Da_MTr2p4v7dyMLPRA/zh-cn_image_0000002538020400.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=F6B7F0FF60F293FAB3938AC3241C0B9F2D0618C92C640006F0B3638815084E31)

#### \[h2\]setRoundRectShape12+

setRoundRectShape(roundRect: RoundRect): void

用于设置圆角矩形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| roundRect | [RoundRect](#roundrect12) | 是 | 圆角矩形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeMask,RoundRect} from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    const roundRect: RoundRect = {
      rect: { left: 0, top: 0, right: uiContext.vp2px(150), bottom: uiContext.vp2px(150) },
      corners: {
        topLeft: { x: 32, y: 32 },
        topRight: { x: 32, y: 32 },
        bottomLeft: { x: 32, y: 32 },
        bottomRight: { x: 32, y: 32 }
      }
    }
    mask.setRoundRectShape(roundRect);
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/pavjjAJrTFm1o920JyMXaQ/zh-cn_image_0000002538180326.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=36F3C7145B754E77CBBCE878C1076B082A122C8574D9DD7136D3FFDA3F74CBDA)

#### \[h2\]setCircleShape12+

setCircleShape(circle: Circle): void

用于设置圆形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| circle | [Circle](#circle12) | 是 | 圆形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    mask.setCircleShape({ centerY: uiContext.vp2px(75), centerX: uiContext.vp2px(75), radius: uiContext.vp2px(75) });
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = {
      x: 0,
      y: 0,
      width: 150,
      height: 150
    };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/y8Vp0p99QyujaK7Ssg42rg/zh-cn_image_0000002569020113.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=1858718F6003D2A9BB055C87676BF0057930A50BFC6B700BA4037875E32DC760)

#### \[h2\]setOvalShape12+

setOvalShape(oval: Rect): void

用于设置椭圆形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oval | [Rect](#rect12) | 是 | 椭圆形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    mask.setOvalShape({ left: 0, right: uiContext.vp2px(150), top: 0, bottom: uiContext.vp2px(100) });
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/vjNaUWtxSzSORuCOF2SWTg/zh-cn_image_0000002568900105.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=616B403A3A7C8911F0121D55CE5DAEFA0C26D5F634929C943DDA5E394D1B80F6)

#### \[h2\]setCommandPath12+

setCommandPath(path: CommandPath): void

用于设置路径绘制指令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | [CommandPath](#commandpath12) | 是 | 路径绘制指令。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

const mask = new ShapeMask();
mask.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });
mask.fillColor = 0X55FF0000;

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeMask = mask;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/G9uQd1fvRwGOV2JZG0bclg/zh-cn_image_0000002538020402.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=09A971D2CE28E5CA49E1EBB37AD53BA34BC483946A2032BA61EB2C632F523C42)

#### ShapeClip12+

用于设置图形裁剪。

#### \[h2\]constructor12+

constructor()

ShapeClip的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### \[h2\]setRectShape12+

setRectShape(rect: Rect): void

用于裁剪矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rect | [Rect](#rect12) | 是 | 矩形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xff519db4;
renderNode.shapeClip = clip;
const shapeClip = renderNode.shapeClip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .margin({ bottom: 20 })
      Button("setRectShape")
        .onClick(() => {
          shapeClip.setRectShape({
            left: 0,
            right: 150,
            top: 0,
            bottom: 150
          });
          renderNode.shapeClip = shapeClip;
        })
    }.margin(20)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/fA4y6VDZTtCvitliGnuudA/zh-cn_image_0000002538180328.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=0ECB3CA08E88D677A7A1A9010B357BDBE19B9DE56B25450A2AFAAE71406542D4)

#### \[h2\]setRoundRectShape12+

setRoundRectShape(roundRect: RoundRect): void

用于裁剪圆角矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| roundRect | [RoundRect](#roundrect12) | 是 | 圆角矩形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setRoundRectShape")
        .onClick(() => {
          renderNode.shapeClip.setRoundRectShape({
            rect: {
              left: 0,
              top: 0,
              right: this.getUIContext().vp2px(150),
              bottom: this.getUIContext().vp2px(150)
            },
            corners: {
              topLeft: { x: 32, y: 32 },
              topRight: { x: 32, y: 32 },
              bottomLeft: { x: 32, y: 32 },
              bottomRight: { x: 32, y: 32 }
            }
          });
        })
    }
  }
}
```

#### \[h2\]setCircleShape12+

setCircleShape(circle: Circle): void

用于裁剪圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| circle | [Circle](#circle12) | 是 | 圆形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setCircleShape")
        .onClick(() => {
          renderNode.shapeClip.setCircleShape({ centerY: 75, centerX: 75, radius: 75 });

        })
    }
  }
}
```

#### \[h2\]setOvalShape12+

setOvalShape(oval: Rect): void

用于裁剪椭圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| oval | [Rect](#rect12) | 是 | 椭圆形的形状。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setOvalShape")
        .onClick(() => {
          renderNode.shapeClip.setOvalShape({
            left: 0,
            right: this.getUIContext().vp2px(150),
            top: 0,
            bottom: this.getUIContext().vp2px(100)
          });
        })
    }
  }
}
```

#### \[h2\]setCommandPath12+

setCommandPath(path: CommandPath): void

用于裁剪路径绘制指令。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | [CommandPath](#commandpath12) | 是 | 路径绘制指令。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setCommandPath")
        .onClick(() => {
          renderNode.shapeClip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });
        })
    }
  }
}
```

#### edgeColors12+

edgeColors(all: number): Edges<number>

用于生成边框颜色均设置为传入值的边框颜色对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| all | number | 是 | 
边框颜色，ARGB格式，示例：0xffff00ff。

取值范围：\[0, 0xffffffff\]

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Edges](#edgest12)<number> | 边框颜色均设置为传入值的边框颜色对象。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, edgeColors } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
renderNode.backgroundColor = 0xffd5d5d5;
renderNode.borderWidth = { left: 8, top: 8, right: 8, bottom: 8 };
renderNode.borderColor = edgeColors(0xff519db4);

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(30)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/5oT-49dYTsu1qDCb-lj0Aw/zh-cn_image_0000002569020115.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=E22FD14DE97B2026F0C5C951601BF690FFDE05EA43C0AEE1F61E41EB5EE1274B)

#### edgeWidths12+

edgeWidths(all: number): Edges<number>

用于生成边框宽度均设置为传入值的边框宽度对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| all | number | 是 | 
边框宽度，单位为vp。

取值范围：\[0, +∞)

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Edges](#edgest12)<number> | 边框宽度均设置为传入值的边框宽度对象。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, edgeWidths } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xffd5d5d5;
renderNode.borderWidth = edgeWidths(8);
renderNode.borderColor = {
  left: 0xff519db4,
  top: 0xff519db4,
  right: 0xff519db4,
  bottom: 0xff519db4
};

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(30)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/DErMEjlwRQqDx9KAZo2BZg/zh-cn_image_0000002568900107.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=5D0A446AB8E47372B4079C8179B32E124EA6D6C7480CAF9E32ED872FC297FA97)

#### borderStyles12+

borderStyles(all: BorderStyle): Edges<BorderStyle>

用于生成边框样式均设置为传入值的边框样式对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| all | [BorderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#borderstyle) | 是 | 边框样式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Edges](#edgest12)<[BorderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#borderstyle)\> | 边框样式均设置为传入值的边框样式对象。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, borderStyles } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xffd5d5d5;
renderNode.borderWidth = {
  left: 8,
  top: 8,
  right: 8,
  bottom: 8
};
renderNode.borderColor = {
  left: 0xff519db4,
  top: 0xff519db4,
  right: 0xff519db4,
  bottom: 0xff519db4
};
renderNode.borderStyle = borderStyles(BorderStyle.Dotted);

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(30)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Gzo7h-dGSt2OjyEYjg18wQ/zh-cn_image_0000002538020404.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=902C5D23A6AA91690193D53CB6773E06B17443B8A237EFA283D6F5CE0CFB177B)

#### borderRadiuses12+

borderRadiuses(all: number): BorderRadiuses

用于生成边框圆角均设置为传入值的边框圆角对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| all | number | 是 | 
边框圆角。

单位：vp

取值范围：\[0, +∞)

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [BorderRadiuses](#borderradiuses12) | 边框圆角均设置为传入值的边框圆角对象。 |

**示例：**

```ts
import { RenderNode, FrameNode, NodeController, borderRadiuses } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xff519db4;
renderNode.borderRadius = borderRadiuses(32);

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(20)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Ze22VdTES4qc1e_yey2W8w/zh-cn_image_0000002538180330.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=8D5BB66B3C9BB3E0793A8C80DA502442CF1399E9308F1BFB8752D567A5D6A58B)
