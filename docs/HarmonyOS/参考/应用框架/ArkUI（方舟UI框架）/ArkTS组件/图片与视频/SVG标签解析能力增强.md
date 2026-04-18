---
title: "SVG标签解析能力增强"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "图片与视频"
  - "SVG标签解析能力增强"
captured_at: "2026-04-17T01:47:57.579Z"
---

# SVG标签解析能力增强

从API version 21开始，当Image组件的[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)属性设置为true时，将启用SVG标签解析能力增强功能，该增强功能主要包含SVG1.1规范中的以下功能。

-   易用性提升：SVG图源颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA；引用的URL类型进行严格校验；Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性对整个SVG图源生效；Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性不对SVG图源中fill = 'none'的元素填充颜色。
    
-   仿射变换能力扩展：支持变换全局中心点可配置；支持rotate旋转的局部中心点；支持矩阵(matrix)转换方式；支持非法值的校验；裁剪路径内支持仿射变换操作；组合场景支持仿射变换操作。
    
-   解析能力扩展：[viewBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#viewbox属性支持对齐和缩放规则可配置)属性支持对齐和缩放规则的自定义配置；支持裁剪路径单元的解析；支持渐变单元的解析；支持遮罩单元和遮罩内容单元的解析；支持图案单元和图案内容单元的解析；支持滤镜单元和原语单元解析。
    
-   显示效果扩展：分组标签g元素中透明度opacity对整个分组下的多层子元素生效；增强g标签内clip-path裁剪路径规则的处理；pattern增强平铺效果和偏移值处理；线性渐变和径向渐变增强平移和缩放效果；mask和filter的参数异常时默认效果变更。
    

#### SVG标签解析能力增强对SVG图源标签和属性的影响

启用增强的解析处理能力后，影响的SVG元素和属性说明如下：

| 元素 | 属性 | 说明 |
| :-- | :-- | :-- |
| clipPath | clipPathUnits | 
clipPathUnits裁剪路径单元，指定裁剪路径的坐标系统基准。

clipPathUnits属性可取值：

userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。

 |
| filter | 

filterUnits

primitiveUnits

x

y

width

height

 | 

filterUnits滤镜单元，定义滤镜效果（如模糊、阴影）的坐标和尺寸基准。

primitiveUnits滤镜原语单元，定义滤镜内元素效果的坐标和尺寸基准。

filterUnits和primitiveUnits两个属性均可取值：

userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。

x：滤镜区域x轴偏移分量，默认值：-10%

y：滤镜区域y轴偏移分量，默认值：-10%

width：滤镜区域宽，默认值：120%

height：滤镜区域高，默认值：120%

 |
| mask | 

maskUnits

maskContentUnits

x

y

width

height

 | 

maskUnits遮罩单元，控制遮罩的坐标系统和内容渲染方式。

maskContentUnits遮罩内容单元，控制遮罩内元素的坐标系统和内容渲染方式。

maskUnits和maskContentUnits两个属性均可取值：

userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。

x：遮罩区域x轴偏移分量，默认值：-10%

y：遮罩区域y轴偏移分量，默认值：-10%

width：遮罩区域宽，默认值：120%

height：遮罩区域高，默认值：120%

 |
| radialGradient | gradientUnits | 

gradientUnits渐变单元，决定渐变（线性/径向）的坐标参考系。

gradientUnits属性可取值：

userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。

 |
| linearGradient | gradientUnits | 

gradientUnits渐变单元，决定渐变（线性/径向）的坐标参考系。

gradientUnits属性可取值：

userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。

 |
| pattern | 

patternUnits

patternContentUnits

 | 

patternUnits图案单元，控制图案整体（<pattern>）的坐标系和内容缩放。

patternContentUnits图案内容单元，控制图案内部元素的坐标系和内容缩放。

patternUnits和patternContentUnits两个属性均可取值：

userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。

 |
| g | 

opacity

clip-path

 | 

opacity透明度：对整个分组下的多层子元素生效。

clip-path裁剪路径：对整个分组下的多层子元素生效。

 |
| 通用 | transform | 

用于对SVG元素进行2D变换（如平移、旋转、缩放、倾斜等）。

translate(x, y)‌：沿X/Y轴平移元素。 ‌

rotate(angle, \[cx\], \[cy\])‌：旋转元素（可选参数指定旋转中心）。

‌scale(sx, \[sy\])‌：缩放元素（单参数时X/Y轴等比缩放）。

‌skewX(angle)/skewY(angle)‌：沿X/Y轴倾斜元素。 ‌

matrix(a, b, c, d, e, f)‌：通过矩阵定义复杂变换。

 |
| 通用 | transform-origin | 

用于定义变换的基准点。需和[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)属性配合使用。

当配置transform-origin时，按照全局中心点（transform-origin）属性指定的坐标偏移(x,y)作为变换中心点进行仿射变换。

 |

#### SVG易用性提升

SVG图源颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA；引用国际化资源标识（IRI）类型严格校验；调整Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性生效范围；调整Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性生效范围。

#### \[h2\]颜色解析格式变更

当Image组件的SVG图源使用十六进制格式的颜色时，颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA，涉及的SVG属性包括fill、stroke、stopColor、stop-color。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/xqfhGaKvQZyFw0qfJQ6XZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=55ED30C157CEC5DDAA181C183B730570DE89665CD5455F7D4570CD049B378649)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-movingphotoview#objectfit)参数。

SVG图源属性设置8位十六进制格式的颜色时，示例图源和效果如下：

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#ff000030" />
</svg>
```

| 提升前 | 提升后 |
| :-- | :-- |
| 
系统会把8位的十六进制颜色当#ARGB格式解析并显示。

例如fill="#ff000030"的矩形显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/bC8rPNzKTOaavmzZOrTabQ/zh-cn_image_0000002569020511.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=ACA9A688233960D58F74CFE10C34CA632B925DEC223EB99B3E52E1FFE5AEF9EB)

 | 

系统会把8位的十六进制颜色当#RGBA格式解析并显示。

例如fill="#ff000030"的矩形显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/PfHpqJCmSm256JHGjiaK5g/zh-cn_image_0000002568900503.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=0618D30EE8C1B8B621F1C8F9795AEC96C116456635D5720D62CFDBFCBA2D300D)

 |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| :-- | :-- |
| 
系统会把7位的十六进制颜色当#ARGB格式解析并显示。

例如fill="#BB88990"的矩形显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/IgmRm-UcT0CWfjZsv0c-dg/zh-cn_image_0000002538020802.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=D3153100D4DB9E2100A5AA37DB77A74F898BA0FE7D7B8E1AEC546B78C4F9542E)

 | 

系统会把7位十六进制颜色解析成默认黑色并显示。

例如fill="#BB88990"的矩形显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/VNw-9-s5REWF7YHA9FRtWg/zh-cn_image_0000002538180728.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=6F1BF723DCC8D4C590883DAEAD4CFD41787B450F6C558BC5F222DCC870079D46)

 |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| :-- | :-- |
| 
系统会把4位的十六进制颜色当#ARGB格式解析并显示。

例如fill="#8888"的矩形显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/2S_GaanPRdyQ1DqPYxDIXw/zh-cn_image_0000002569020513.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=3109A2AABA4A11E1E966E9806340E73BEF12CDE244B90136B76F2490680F7E7D)

 | 

系统会把4位的十六进制颜色当#RGBA解析并显示。

例如fill="#0000"的矩形显示效果（全透明）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/pKMuejXhRfSb1QCXS49G2g/zh-cn_image_0000002568900505.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=92AC890C7AD869A4112D1A04C2867C4372B035C9C182056CC8AAE4693408A66B)

 |

#### \[h2\]引用国际化资源标识（IRI）类型严格校验

严格校验filter滤镜/clip-path裁剪路径/mask遮罩引用的URL类型，避免引用类型不匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/tJMoyv8nSNa-zjT1dnWioQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=521DB79C396829E4DAC60B3DBB9D347200CCEB3B77C575205F339A58B086F3AE)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 提升前 | 提升后 |
| :-- | :-- |
| 滤镜/裁剪路径/遮罩引用的URL类型不匹配，导致错误的显示效果。 | 
滤镜/裁剪路径/遮罩引用的URL类型不匹配时，不显示对应效果。

例如，mask、clippath、filter、pattern、渐变等标签都有各自的id，filter、clip-path和mask属性绑定其它类型的标签id时，对应效果不生效。只有mask属性绑定mask标签id、clip-path属性绑定clipPath标签id和filter属性绑定filter标签id时，对应效果才生效。

 |

当URL类型不匹配时，遮罩效果不生效，示例图源如下：

```xml
<svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义遮罩 -->
  <defs>
    <clipPath id="myClipPath">
      <circle cx="50" cy="50" r="40"/>
    </clipPath>
    <mask id="myMask">
      <rect x="0" y="0" width="100" height="100" fill="red"/>
    </mask>
  </defs>

  <!-- 使用遮罩 -->
  <rect x="10" y="10" width="180" height="80" fill="blue" mask="url(#myClipPath)"/>
</svg>
```

#### \[h2\]调整colorFilter生效范围

Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性从只对stroke边框生效调整为对整个SVG图源生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/UkK7UrBgTGOvDhI_ckhrkw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=88A4D76A39DACE7A44B7BE415A802BB42577E571C020DE88B7FBF0D13F16B97A)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 原始图源 | 提升前 | 提升后 |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/rYdmyvRTQcmpdiBta1nnYg/zh-cn_image_0000002538020804.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=8AB3CFEFEA0DD0ECC6DBD7409DE61CCCDDEC4AD85CC2B8136CD599E8DF1DEF32) | 
Image组件的colorFilter属性只对图源的stroke边框起作用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Y_HlxMWWRB2rRER_bD_jhQ/zh-cn_image_0000002538180730.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C70CC6B2CA66F7F3BF22E85B439822C2F2C7E607757E23392D970D4B1D429F5C)

 | 

Image组件的colorFilter属性对整个SVG图源起作用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/NXHjPRD0TKeixDRqGUHAxg/zh-cn_image_0000002569020515.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=BB0ACCFB0F04D22FB88340EBC642DA9033E7945C30722D7D2E9F0844573FC1F1)

 |

示例图源和示例代码如下：

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
    <!-- 矩形 -->
    <rect x="10" y="10" width="180" height="80" stroke="gray" stroke-width='16' fill="orange"/>
</svg>
```

```ts
@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image111.svg'))
          .width(220)
          .height(220)
          .colorFilter(
            [ 0.6, 0,   0,   0, 0,
              0.2, 0.8, 0,   0, 0,
              0.2, 0.2, 1.2, 0, 0,
              0,   0,   0,   1, 0 ]
          )
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### \[h2\]调整fillColor生效范围

当SVG图源中元素的fill属性为none时，Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性从填充颜色变更为不填充颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/mUjSTLoLTOKAWrzlQvd5CA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C11F71A91CF8C63B1BB16E4A287C37592F5455258AA1E643B2A0CB5CB8CB1502)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 提升前 | 提升后 |
| :-- | :-- |
| 
Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/nVRP3TJhSPSN2W6a_ueBMw/zh-cn_image_0000002568900507.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C31E44EC590038705887C67C6F34C621137D783B656695AF09F60A34DD9243B6)

 | 

Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/rAf_Qg04TRK5-4Oj2jnD5A/zh-cn_image_0000002538020806.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=7A616EEB019D8F7DB8C450309950666AB48A946A675D9FB6B942AE5CFDC32552)

 |

示例图源和示例代码如下：

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 矩形 -->
  <rect x="10" y="10" width="180" height="80" fill="none"/>
</svg>
```

```ts
@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image11.svg'))
          .width(220)
          .height(220)
          .fillColor('blue')
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### 仿射变换能力扩展

对于[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)属性：支持变换全局中心点可配置；支持rotate旋转的局部中心点；支持矩阵(matrix)转换方式；支持非法值的校验；裁剪路径内支持仿射变换操作；组合场景支持仿射变换操作。

#### \[h2\]支持变换全局中心点配置

SVG支持解析[transform-origin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-animation)属性来配置全局中心点的能力，前后效果对比如下表格说明：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/ql2oFDNpT8SKBCNTgAP8UA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=99956A0472320CFF24B8BC7B277A7F3EF1174BB171491606E423875F79DC53C8)

SVG图片最终显示效果受Image组件的'[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| :-- | :-- | :-- |
| SVG基本图形配置变换功能和transform-origin属性。 | 固定按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点进行仿射变换。 | 按照全局中心点（transform-origin）属性指定的坐标偏移(x,y)作为变换中心点进行仿射变换。 |
| 
transform属性设置rotate旋转功能，同时配置transform-origin属性。

全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ceXTemdtSG-XgU9SofZxqA/zh-cn_image_0000002538180732.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=47510C0A23FA067F45A5C46ACB8FDE76A87EC2DD8E50B92630C7790009817A24) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/GaEEeoPpSQm0pCevdq6cpw/zh-cn_image_0000002569020517.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=746A861607CFBB65590AFED36775BB96046250C619E06277832B22FD25555E6C) |
| 

transform属性设置scale缩放功能，同时配置transform-origin属性。

全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/dhHhMHvdRRW87sC39TJN1w/zh-cn_image_0000002568900509.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=3F1CCF4DC4568C2BEF9FDC92424BD8B8F8097056D60D36834FAD74C8EB225FBA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/SwsZoaPtT3ekvS93T-xRsw/zh-cn_image_0000002538020808.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=2E247CC7850BAF4E955D56CFFD16E7AC67040F8BC3B61144DE6B326DC93B9482) |
| 

transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。

全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/mxGD7GtxTfWxLQXPhk4EIw/zh-cn_image_0000002538180734.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F6F1195BB295027BE0AEBB73DE2FD84A7A2551733115EDB19F376C35E2F95035) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Psa_dz4GQlKsoG2b2H96Rw/zh-cn_image_0000002569020519.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=D62F0C8E93ECEBF061FEF8565673F6BE1E3DAF14959129686B9C36400828B323) |
| 

transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。

全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/B3wYNourT66fTGGo87JfLQ/zh-cn_image_0000002568900511.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FE9A400979370FC0CC7D16DD5B69216D5F9C1C8E117AD2222626F078FCA2F61D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/b8oiQSMIRvepc2tbT0PNjA/zh-cn_image_0000002538020810.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C2B0AC5A79AAB79A190123CB37D4BA0D847CF99AA2C316726353370DEF0246CB) |
| 

transform属性设置translate平移功能，同时配置transform-origin属性。

全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Vt5OtCPpSkW-3sWwaoQzVg/zh-cn_image_0000002538180736.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=5117D17F115D85B888B5830B63608F96970FFA1DCBEB7418670EA9C9B508B977) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/yQh4TmLeQoOkehkd68yq0w/zh-cn_image_0000002569020521.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=D54AB9822C4FD5C87F457F07C611574FCE8DE8132B574DB96E34CA72FE52D488) |
| 

transform属性链式调用多个功能，同时配置transform-origin属性。

全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/RmWDX5uCTPSuydWWCccw1Q/zh-cn_image_0000002568900513.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=5FED2346669E3D0CB5D3D99EF05119D6A017546F07128AF917248C4ACE19415D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/0UqE-vt8QdSisPa9tc07vQ/zh-cn_image_0000002538020812.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=673A1AA92F9FB9997086A9AA3B36181B66160D92E4B20E5A780E3E8B7A0B2FFB) |

#### \[h2\]支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Ydi4a-mvTje9Wr6EID3UFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=39B8D36A82843028B9F73201CE37D7C4B507613C0AA823B3BE2B28823A8A6BEB)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| :-- | :-- | :-- |
| 
SVG基本图形同时配置两个属性：

局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。

 | 

按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/lJmu6DceQC6k9gS0ayoBlQ/zh-cn_image_0000002538180738.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FEE250ABE4B838D382F87E66D5CCF6CD6C82246B2679D4FB102BA9924BC8843D)

 | 

按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/hRdzpP96Tm2W_LvESlkt6A/zh-cn_image_0000002569020523.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=28CBD8A5D4C2235032264F189B27810605DA8BDF51CB4CE5CD3DDA0CD374AFA6)

 |

#### \[h2\]支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/R_JCVaG5TCqjdhMGhyg0RA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A97D0FA5F47436D355C97F67573F926CCF303313AC79046DAE725588C22EC482)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| :-- | :-- | :-- |
| 
transform属性设置matrix矩阵变换，同时配置transform-origin属性。

全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/73F0TTvcRWi8OGY-z7hHvw/zh-cn_image_0000002568900515.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=8CF20245B4BEF15A3F0D7505F1AFCB629607C2DB541B1C645C1212BBC9646163) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/yAt2oXHuTfqOMKkGOxSyig/zh-cn_image_0000002538020814.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=BE35264F43082AC12ADAD9AAB844DB07A73FA75765B7E3A5553E01E0A4D0B105) |

#### \[h2\]支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/0bJT5W8ISdqggqcCTTBZDQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=26CF4085F1A701D808ABC925CE552BED439B90AF570BB1F9CC642511A6DA03DB)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| :-- | :-- | :-- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 
按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/KroGNzfOSMmgkBniKC9SEw/zh-cn_image_0000002538180740.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=6721A03F482214DD2BE138114622A548E2A09F88E8FAD62C67161D3341C318B2)

 | 

不做旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/6tOLWw3wTp-ZZCXph4RJhw/zh-cn_image_0000002569020525.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=DFD9DD0DBC06E5F949DD9F8241D57EC0CAC1EB991C7E6BB0976E6477D4666265)

 |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 

按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/0Jqh6D_DTQiHX3FA0LjcoQ/zh-cn_image_0000002568900517.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=5E8B678A98BD2C2CF6C7E2820DEDA59B3B77FB8DE7D4F8CE3D05F78735D8BB7D)

 | 

不做旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/_2msvf5zR-u07FCiIuSWeg/zh-cn_image_0000002538020816.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=7F941DA0862BF0FDBAD7F06DDD5496F1272BE5F7F6784D0EB5B83394C2091E30)

 |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 

取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/MOpVh-6TQUKvGJw07KvCFw/zh-cn_image_0000002538180742.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=8478D1D4FB103DBFA894B206E0CE741187B72558D5517193FEA6883D171CEC9B)

 | 

不做变形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/unTKliOLRV6YtDJYSwJQYQ/zh-cn_image_0000002569020527.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=94A9FF3F0A08E7CD80B96DA3F927821A93EEC781EAF9C98A3FDE2E773CB86833)

 |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 

不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aTVi_-nzRFqCQJyIBVqJaw/zh-cn_image_0000002568900519.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=0A8B7AF6347CF87AB0EADE78DD3DE7274C9B7DBDBC42510884CE8250D5DBCFD5)

 | 

所有的变形功能均不处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/s9NJHJv_S3KpEchuLxSWDQ/zh-cn_image_0000002538020818.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FD03DC77BD39AEB4323C4BA0C152BCFA1DE42D80FA8A36EFDACDB1030F6E76D2)

 |

#### \[h2\]裁剪路径内支持仿射变换操作

支持clip-path裁剪路径内的transform仿射变换操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/G_4hESkXTMytLLuiUA8zjQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F19652B244546AF1765AF0113C6E85795507F4AE83B279BBE236846C8EDFC3D8)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```xml
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义一个ID为circleClip的clipPath，使用objectBoundingBox单位 -->
  <defs>
    <clipPath id="circleClip" clipPathUnits="objectBoundingBox">
      <!-- 圆心在对象中心，半径为0.5，即圆覆盖整个对象 -->
      <circle cx="50" cy="50" r="40" transform="translate(50 50)" />
    </clipPath>
  </defs>

  <!-- 应用clipPath到一个矩形上 -->
  <rect x="10" y="10" width="250" height="250" fill="blue"
        clip-path="url(#circleClip)" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/uVdKPqJNRweH0FbvVu043w/zh-cn_image_0000002538180744.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=2AC04366C8ACC1A495BAAB54A50D824B4E1430947BF671916537D7CA7E86E64F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/rFdV75aFThyzjTzI_vcy_Q/zh-cn_image_0000002569020529.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C11AE635A08EE59004562246C1938C8DB1ECC5682EE38AB8AA8A43FF02543EA9) |

#### \[h2\]组合场景支持仿射变换操作

支持多种元素组合场景的仿射变换操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/7o5SidltQ_CxDEhDnOQbJA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=B93AA25F1FF3AB45266F5D1663FAB9694EE58915F09AEE425455BC203040D84D)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

transform操作在use中，use对象也在相同的mask元素内。

```xml
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
      <use xlink:href="#rect1" transform="translate(0.6, 0.000000) scale(0.5 0.5)" />
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5" fill="red"  />
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg> 
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/rMtUkiuITp2q-xXh0PlXsA/zh-cn_image_0000002568900521.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A3D3597717954998C8C132F3235F8140E42E3B0799ADFE2664776D15F92C0FDA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/prf_GjxOSaePewlQ3EAUvg/zh-cn_image_0000002538020820.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=D11CDC53725F79113437AA298D7FA95E81D37E04248B40B8A3F2B682D76355BD) |

transform操作在g标签中，且不包含scale操作。

```xml
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
        <g transform="translate(0.6, 0.000000)">
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5"  fill="red"  />
      </g>
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg> 
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/xy1y46pmQtC5bco8_Lvueg/zh-cn_image_0000002538180746.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=31E7F80E1124C5D84EE7525F9D80FD4C0E19878F63CDCC3EE9057D8D5A221730) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Xtwcb34iThOXJydWMtMaDw/zh-cn_image_0000002569020531.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FCE6E744F5B865C567A32C755139A3D5995FA34F4B9CA59C5723AA5FF6EB65AB) |

#### SVG解析能力扩展

[viewBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#viewbox属性支持对齐和缩放规则可配置)属性支持对齐和缩放规则的自定义配置；支持裁剪路径单元的解析；支持渐变单元的解析；支持遮罩单元和遮罩内容单元的解析；支持图案单元和图案内容单元的解析；支持滤镜单元和原语单元解析。

#### \[h2\]viewBox属性支持对齐和缩放规则可配置

viewBox主要用来控制在SVG动态拉伸效果，可以通过参数preserveAspectRatio来控制内容区显示的对齐和缩放规则。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/E5iz8eJATmSZM0nFs8jD3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=7988C1A53ED24F8F47A2DB459216E576F2C9D1BD9C484876AD4E40711A81C572)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

SVG包含“preserveAspectRatio”属性且值为“none”，示例图源和行为变更如下：

```xml
<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" /> <!-- x 轴 -->
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" /> <!-- y 轴 -->
</svg>
```

| 参数值 | 扩展前 | 扩展后 |
| :-- | :-- | :-- |
| none | 
按宽高比最小值进行统一缩放。

同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/BWQxZHqSTBCd-Ocfy7lKGA/zh-cn_image_0000002568900523.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=357AA585EDD5DEE17BCC4D53E9557DA076F6DA13713A79315B3B9B9DBBEF9B60)

 | 

缩放元素的图形内容，使元素的边界完全匹配视图矩形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/O7Tp87gDSg67zod7fTAzDg/zh-cn_image_0000002538020822.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=97B840EE8F9D537339F449012AD2C9346A39F703C903B49F4B97969B6A86850D)

 |

SVG包含“preserveAspectRatio”属性且值为“<align> \[<meetOrSlice>\]”，示例图源和对齐方式、缩放比例变更如下：

```xml
<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="xMinYMin meet" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" /> <!-- x 轴 -->
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" /> <!-- y 轴 -->
</svg>
```

| 参数值 | 扩展前 | 扩展后 |
| :-- | :-- | :-- |
| xMinYMin meet | 
按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/pdIaUKTPRvyjnnUj7LjTAA/zh-cn_image_0000002538180748.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4E11C3744B2518B2E63CF4B8F609A32A9185B0AC8CA4EC1E9BB46491A80A1E25)

 | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐，

SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/hBxvPsaLSpSvQTY5T8I4Kg/zh-cn_image_0000002569020533.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4EE81D12F12CDF99632E00EBA83D3AEC3127520CE91271D45AD78C6B068B0767)

 |
| xMaxYMin meet | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/YH27jqCeR_alT7sJP0iwmQ/zh-cn_image_0000002568900525.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F3A10890B0957D80AFB4F881DC887F730A8697791B1F8AE6699B489C2165FB81)

 | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐，

SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Kj5jG8lXSSuzGk9Tr44jxg/zh-cn_image_0000002538020824.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=0219FAE5997A8A71C5176D558270EFE5297AD3B715A503B7380549525AA625A9)

 |
| xMinYMid meet | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ESDlrrL4Rt64QxKB6F73zg/zh-cn_image_0000002538180750.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=51DC149834415C738BDFE4B2B03C7041889DC1D698F28493A8EC37AC3265C336)

 | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/-uFugx9YQ9ODnmnriuNtqQ/zh-cn_image_0000002569020535.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=9806491EAB1E502015BBA0B1F58460B725B25C09622DAAFFDABCA1F342E72D37)

 |
| xMaxYMid meet | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/I7zluAiHRGWwyZ96fvIG_g/zh-cn_image_0000002568900527.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=9DA591CD142E74082A918CE7BB84EE44A6FAE3CC5A805E499438CE748C7BBC7A)

 | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/TP3HDiwAS5y4NseQGU91Ew/zh-cn_image_0000002538020826.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C6B649474F1CA624AF7603053B67BC24B8E59EEE5AD3EDD07EFE313F56519854)

 |
| xMinYMax meet | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/QybNNntPQtCyM1NZ7roaeA/zh-cn_image_0000002538180752.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=85AEB232704AC2BCD3CEBFC8632654BDD960AA7BCFB0519769B14610B9D153FE)

 | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐，

SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/63s8LRSoTKmxQW_lNwfygw/zh-cn_image_0000002569020537.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4C7B053E9246AB3E6CB8BBA18AAEB3BAB52082E5155F02CA1A948A9C8AC2E2B4)

 |
| xMaxYMax meet | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/crjQlNRsT1yUe6HQM8diRg/zh-cn_image_0000002568900529.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=80B7BF159101C6E55682D79475DE60E0D10BFE2F10B884B78AF9B72DB9E1BEB0)

 | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐，

SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/GJd8IfrVSUK8gQ6sAsrQzA/zh-cn_image_0000002538020828.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4E1A032C1DA11B02CEAD003BBF1EF7B61865A9AD2C487AB8654796B267D27632)

 |
| xMinYMin slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/eSzOmnSGQPGUvwgX5Z2XkQ/zh-cn_image_0000002538180754.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=CE80DD4059631327E09A1ED092F4E290221CBB19736DA682DFA0A936970B5F3B)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐，

SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/yrmu7WS0QSab0DsbDmJEGQ/zh-cn_image_0000002569020539.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C620119FF1C56B21BB6C249A56C36D2E9CBCDAF8F59C815716EC2BFB7E3E2099)

 |
| xMidYMin slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/ek4d1st8SimVog8ZMMrKsw/zh-cn_image_0000002568900531.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=8E32E74324352B6EDE7A52C533F9DDF2B037FEFF85AC1E4CA8E085721E0DD427)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/xB5W920NQP-Otuc_Un3bSQ/zh-cn_image_0000002538020830.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=5EA57F244F3782FDFCA306A2C661CB00060097D64BA80A079B80039942C54487)

 |
| xMaxYMin slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/PZddmxWVTsu9Fboiij2gkQ/zh-cn_image_0000002538180756.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=B50E98CD6496528D9B6017FCC7389C1ADE56845770F3D64A2FEB6597544070FD)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐，

SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/DrcA4e_TTxS0NNmCDxJPpQ/zh-cn_image_0000002569020541.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=24EBD072462835D1C6F818076EDBB5A41B3F2FD0C80EE79D3047E15C6BE4B7B1)

 |
| xMinYMid slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/--zjtwsbQcWKIWZ_z6W_xg/zh-cn_image_0000002568900533.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C14932706C59406F2E6BECB30710F147C89015C0F185DD172312CDB85B0F9138)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/MNVxO-4YSsqj3HmgcgRh-g/zh-cn_image_0000002538020832.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A83ACECE9137E914EAD0FF8ACEA82062F78EB36907A77F1F870914CBC990EAE1)

 |
| xMidYMid slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/eQ90zQaqTFaz2xSpUaujRA/zh-cn_image_0000002538180758.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=AF98398B5462A93A09E2F40C784C2A4ABE17F8CAC980DA2C22B71A9A9C5F33CD)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/8LFYgeGrQnK4I04CoWC_Lg/zh-cn_image_0000002569020543.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=EF160544534052C39BD8B2EBECA748D24B88B0D7CF6BB2A65D363B91E637642D)

 |
| xMaxYMid slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/bnJi51lZSnu3vUop775j_w/zh-cn_image_0000002568900533.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C49CA19B5F74F162229391B3FAF29B32CF178CE755ECB1FA8F7897DDCD74E7BB)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/mCC8sqLHS6KpbkEzvvGfXw/zh-cn_image_0000002568900535.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=0D37881FC091B9D709F6B9BA1D549C60E2ECE297B56916608F2540F745CA72D7)

 |
| xMinYMax slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/IEOArhGMQ7-kbN06KgmPvA/zh-cn_image_0000002538020834.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A2808CF223545AA80DC439E0A78B932A48EA9E67C0056FEEF088D36A35D567D5)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐，

SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/lrmizAmiSiufn9AaB7YQyg/zh-cn_image_0000002538180760.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=D0782EDC07AF86C212C263C570F9BEDC75F6A2363F75B70E042DFF7F392E4549)

 |
| xMidYMax slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/f6oxpGXxQ0avvQTSkCU7Qw/zh-cn_image_0000002569020545.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=EF093A869FA51F51FE29E530FE20019A8767EF45B100296473215DB26772844B)

 | 

按宽高比最大值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/0LgtVrusSsqCVMy7ZMDjkA/zh-cn_image_0000002568900537.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=E4D4E75FE173A5EDEAD16A0E1C90736613C0DAE7BDAA006E7BC1C170DD2B5933)

 |
| xMaxYMax slice | 

按宽高比最小值进行统一缩放。

SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐，

SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/0rDTP6kVSEmDSEKVVTi_Yg/zh-cn_image_0000002538020836.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=2048F0B682924333DB1DD10051D6C12E8EFA15175548362659090E7138BED92B)

 | 

按宽高比最大值进行统一缩放。

将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐，

SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/gFMnnzmdT42-NL4bbzmXgg/zh-cn_image_0000002538180762.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=0D7ED901C0E5C4FA8A45FF4DE5BB5E2EA21976D3CDBC5325791CB2527A06D483)

 |

#### \[h2\]支持裁剪路径单元的解析

支持裁剪路径单元值[clipPathUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加clipPathUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/1L5wY7wQRGCbEUtxqtnx3A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=CC58017ACA937D570C8C0882AEDC8491D30C1B623AC44B5C0C568C9386EC7EE8)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

下面图源示例当裁剪路径单元为"objectBoundingBox"时，长方形裁剪路径位于应用裁剪路径长方形图形左上角x,y乘以图形包围盒宽度和高度。尺寸为width乘以图形包围盒的宽度，height乘以图形包围盒的高度。

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="clip1" clipPathUnits="objectBoundingBox">
      <rect x="0.2" y="0.2" width="0.7" height="0.6" />
    </clipPath>
  </defs>
  <rect x="10" y="10" width="100" height="100" fill="blue" clip-path="url(#clip1)" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/OgfuDVNGTvq7xrw3dZNWrg/zh-cn_image_0000002569020547.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=28882C1848A3CE0EE23C1FDF5E8E21667C731AF0FDAA6928F27160EE5C7333AD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Wfx3vH8uTZi3mX7s84NJlw/zh-cn_image_0000002568900539.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=1B014EFB36653DD6E1F1E95D41A63BDFCA29221A500398CC20E8AF239BEDCFC6) |

#### \[h2\]支持渐变单元的解析

支持渐变单元值[gradientUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加gradientUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/M1pdqSX3SpWs3gKHADVeqA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=E9EAF7C0CE0F593749BD62D92355DA2B6EFEF1C6AFB776209916857AC44D6467)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例显示一个线性渐变从绝对坐标(10，10) 到 (180，180)的长方形范围内。

```xml
 <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="10" y1="10" x2="180" y2="180"  gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect x="10" y="10" width="180" height="180" fill="url(#grad1)" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/VX0Z6ZzaT8GUWPwpJyECvQ/zh-cn_image_0000002538020838.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F10C0295C1AC534032EC28169523AA1F3421E808962E54F05FD9255F7415DE42) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/EPp7loAoQE6YR1Fi7dKNAA/zh-cn_image_0000002538180764.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=CF9B022F114BE9ACB18635E956380BD3F6BE9048AD75992C4B51880813C5DB5A) |

图源示例显示一个径向渐变从绝对坐标圆心 (100，90) 开始，半径为90的渐变效果。

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
     <radialGradient id="grad2" cx="100" cy="100" r="90" gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </radialGradient>
  </defs>
  <circle cx="100" cy="100" r="90" fill="url(#grad2)" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/VrMumIKnSkedt44UcJ5kJw/zh-cn_image_0000002569020549.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=15AF80C67D3E3A36F7B3B231B374F0593DEB2EE394AAFC0FD62961A1D5AD2748) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/VPKWIL2ASYO-7_Cv8PVsxw/zh-cn_image_0000002568900541.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=DBE2808AE49767DAB5206A7D6C07C3E160DEB6432EB0DE65421A829DBC7EFB21) |

#### \[h2\]支持遮罩单元和遮罩内容单元的解析

支持遮罩单元[maskUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和遮罩内容单元[maskContentUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加maskContentUnits和maskUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Qw-CpLTmS1GlBcUGAKYehQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=6C76F5A2C1DBFB70AA5E3796D896F3A4E903E140E1FBDC5C9150742592BA8E4F)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例显示一个五角星遮罩范围从绝对坐标 (10，10)到(200，200)，遮罩内容相对于应用矩形左上角，水平尺寸乘以图形包围盒宽度，垂直尺寸乘以图形包围盒高度。

```xml
<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" maskUnits="userSpaceOnUse" x="10" y="10" width="200" height="200" clip-rule="evenodd" maskContentUnits="objectBoundingBox">
        <path d="M 0.5,0.05 L 0.2,0.99 L 0.95,0.39 L 0.05,0.39 L 0.8,0.99 Z" fill="blue" fill-rule="nonzero"/>
    </mask>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="red" mask="url(#mask1)" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/u9Pc85KHRoyXYT7814diog/zh-cn_image_0000002538020840.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A08E9E14B0AC789FB644C25D55DF0DA0F0D56A39A7CD4A29650D589CBC004772) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/KOnEXth3SiKmKigJ4ADFRg/zh-cn_image_0000002538180766.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=6033F72CCEB5658664523715C58E7A98292BF81C79259A604A23C23D1FDF2E5B) |

#### \[h2\]支持图案单元和图案内容单元的解析

支持图案单元[patternUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和图案内容单元[patternContentUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加patternUnits和patternContentUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/X0OX4YOlS7KCooQtT5NN_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=7E479243F18718BFB630D93B9CA68FAF0B6B8C25FB0EC467C33B3DB3CF790BEB)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源图案单元位置尺寸为绝对坐标，图案内容位置、尺寸相对于应用图案的图形，横轴乘以图形包围盒宽度，纵轴乘以图形高度。

```xml
<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1" patternUnits="userSpaceOnUse" x="10" y="10" width="100" height="100" patternContentUnits="objectBoundingBox" >
      <rect x="0" y="0" width="0.25" height="0.25" fill="red" opacity="0.5" />
      <rect x="0.25" y="0.25" width="0.25" height="0.25" fill="blue" opacity="0.5" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200"  stroke="red" stroke-width="2" fill="url(#pattern1)"/>
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/sjJQIhFwTgCWv4O230ko7Q/zh-cn_image_0000002569020551.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=9D6A04D1E79A33AD490FE6D742E213266BD8DDE2A76F87FBA47C00CBD131C617) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/MP3s5opaSfOc3rycC3BRcg/zh-cn_image_0000002568900543.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4DA363134CBEAF33501D4A565B37C5037B46BBCE5221269FD9B2FD9A7D5F0089) |

#### \[h2\]支持滤镜单元和原语单元解析

支持滤镜单元[filterUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和原语单元[primitiveUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加filterUnits和primitiveUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。目前支持到的原语有feFlood,feOffset,feGaussianBlur,feBlood,feColorMatrix,feComposite。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/n7zWcX-tTIubZCq9oQJsug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=2820CBDEB7F4EA6BB6D89C7F0A09E78F6CC481866CAD1FF50FA570A83A797BC8)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例：原语值为"objectBoundingBox"时，feGaussianBlur的模糊标准差X，Y轴的stdDeviation数值分别需要乘以应用滤镜图形包围盒的宽度和高度。滤镜原语子区间x，y坐标相对图形左上角分别乘以图形包围盒的宽度和高度，滤镜原语子区间尺寸的width，height参数分别乘以图形包围盒的宽度和高度。

```xml
 <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg"> 
 <defs>
   <filter id="blend" primitiveUnits="objectBoundingBox">
     <feGaussianBlur in="SourceGraphic" stdDeviation="0.1, 0.1" x="25%" y="25%" width="50%" height="50%" />
   </filter>
 </defs>
 
 <g fill="none" stroke="blue" stroke-width="4">
    <rect width="200" height="200" fill="none"/>
    <line x2="200" y2="200"  stroke="blue" stroke-width="4" />
    <line x1="200" y2="200"  stroke="blue" stroke-width="4"/>
 </g>
 <circle fill="green" filter="url(#blend)" cx="100" cy="100" r="90"/>
 </svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/fVzx6YLfSbK4HNhrdT9tyA/zh-cn_image_0000002538020842.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A62CCF1A03011B263C8F13ADD7874037FD387BB38A3D8A7D23E73E9B65AE408D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/PQx0JomXTQyFjGmSjuIs7A/zh-cn_image_0000002538180768.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=E3047B092BA9C62BFE454D4C2D3497503D61D32290983D8BF28DBCD9D669C350) |

#### 显示效果扩展

分组标签g元素中透明度opacity对整个分组下的多层子元素生效；增强g标签内clip-path裁剪路径规则的处理；pattern增强平铺效果和偏移值处理；线性渐变和径向渐变增强平移和缩放效果；mask和filter的参数异常时默认效果变更。

#### \[h2\]分组标签中透明度

分组标签g元素中透明度opacity从对整个分组下的一层子元素生效到对整个分组下的多层子元素生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/iiwXME4MSACvu5cSSo2FQA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=7E3922B56301F1A249A05DE2A343360B03A05D9D50AB48E4E663840D296CC374)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源有两层分组标签嵌套，被裁剪路径截取的半圆形的透明度为0.4。

```xml
<svg  width="200" height="200" viewBox = "0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="myClip" clipPathUnits="userSpaceOnUse">
      <rect x="25" y="0" width="60" height="60" />
    </clipPath>
  </defs>
  <g opacity="0.4" clip-path="url(#myClip)"  fill="red"  > 
    <g >
    <circle cx="25" cy="25" r="25"  />
    </g>
  </g>
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/j2ZkNrYXRY2xT0WiF8Yrfg/zh-cn_image_0000002569020553.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=889831B1AFD4700DCF7D05F11731C0A17E37CC8951151B9D821811134BBF3EAA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Tkqu3R8mTIWE7SYk097uLg/zh-cn_image_0000002568900545.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=44692DD0B42F47740CD832DD4B9A5C7EF25C4C501C28EFD3D0C81315C8A5A436) |

#### \[h2\]分组标签内引用裁剪路径规则

增强g标签内clip-path裁剪路径规则的处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/rOaY5BuKSG-eypqFVlARoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=DA80E4C791F1448D446BA884F1C6298B6070270F113626E6F4671DE0FBC4372F)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源裁剪路径引用于g标签里，默认裁剪路径规则为"nonzero"，路径标签里的填充规则为"evenodd"，左图实际的填充规则为"evenodd"，右图的填充规则为裁剪路径的默认规则，也就是"nonzero"。

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义五角星裁剪路径 -->
  <defs>
    <clipPath id="heartClipPath" >
   <path d="M 100,10 L 40,198 L 190,78 L 10,78 L 160,198 Z" fill-rule="evenodd" /> 
    </clipPath>
  </defs>

  <!-- 应用裁剪路径到矩形 -->
  <g opacity="0.4" clip-path="url(#heartClipPath)" >
  <rect x="0" y="0" width="200" height="200" fill="red"  />
  </g>
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/7HcoR_6LQU6ZvAkhqG7xSw/zh-cn_image_0000002538020844.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=8771F0371E52F413BD5DD8C5D52DF0D11D6F7AA46505303A454581674D0347D3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/IiwYwZfhRgKwPvg_squlpg/zh-cn_image_0000002538180770.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4E2E128EEE51AB15B647E094C33A311F561191FF1341BCB6372A183724439E00) |

#### \[h2\]pattern支持平铺效果

[pattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)图案支持重复平铺效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/HiVB3wbXRFm3baTTD1dwxg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=9DD7D07884AAA213F799F22595E08FDF8DBADE3E0FF14B5507ED4A0134F78CBA)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源如下：

```xml
  <svg width="210" height="210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1"  x="0" y="0" width="0.5" height="0.5"  >
      <rect x="0" y="0" width="50" height="50" fill="red" />
      <rect x="50" y="50" width="50" height="50" fill="blue" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="url(#pattern1)" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| 
图案不支持重复平铺。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/KODxzZbTQmWt2GN8p4lLAQ/zh-cn_image_0000002569020555.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=BC24513D1BEBD4A8AA0B7D749962E8581D43453A6C4DB7161B22383D6CE0F1D1)

 | 

图案支持重复平铺

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/tB_m3ak4Q4qrI4yWvtCGtA/zh-cn_image_0000002568900547.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4541F45E9E1AB5B8E414C21A7336E33368B1B39F8295E038A54CC208042803E2)

 |

#### \[h2\]pattern偏移值处理

支持pattern图案在x，y参数非0时，从只显示平移后的部分图形变更为显示完整图形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/UrO-E4N4Q2WydBNzk5WSFg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4E73E49C6B387C805C4A480115C86E37CB2DE608B2F561347789800FE4D9AE40)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```xml
<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect width="40" height="40" fill="url(#pattern0_0_37)"/>
  <defs>
    <pattern id="pattern0_0_37" patternContentUnits="objectBoundingBox" x="0.5" width="1" height="1">
      <use xlink:href="#image0_0_37" transform="scale(0.00833333)"/>
    </pattern>
    <image id="image0_0_37" width="120" height="120" xlink:href="data:image/png;base64,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"/>
  </defs>
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/1fNQWvYaSF6RgZN13aC3Ig/zh-cn_image_0000002538020846.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=3D9BB0280CC35CAA325B66E928010B142448498CC4344CCD133C08EFE96CCF6A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/SfaUdhibQ-6aVUQMmTB9qw/zh-cn_image_0000002538180772.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=0543EF6533A725C005756899C9B479D16CC4FF812FC3D1BF07F7AD41BA0C05EE) |

#### \[h2\]线性渐变

[linearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)线性渐变支持做平移和缩放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/7B9bYovrTKipbRDrKCgYBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=B2C90CDD52CD5BA914600E9E8DC9D1253D094548C28D03D0460652677246C613)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <linearGradient id="grad1" x1="50%" y1="0%" x2="0%" y2="50%">
            <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
            <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="115" y="15" width="170" height="110" fill="url(#grad1)" />
    <line x1="200" y1="15" x2="115" y2="70" stroke="black" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Xeo37fA1SfOgEHAYIfNVzw/zh-cn_image_0000002569020557.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=195024D18521EC1A3581F0A2E3E977EFE4AC93C25F94D83A62BC4B5B1B72C2AB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/XJOHjxQSSym7_Qk5gt1rxQ/zh-cn_image_0000002568900549.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4E1998ECFD576565B28DE90AAFF82D6DCFCD4F1BC43FB9A1F628838D13D3FC5E) |

#### \[h2\]径向渐变

[radialGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)径向渐变支持做平移和缩放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Ta_MXZEkQAGcU7F1prbxFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=9C447872C280B60C734C91BE3F20BA18B0F1B80248A5021956BC7527F3BC7A1E)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <radialGradient id="grad1" cx = "50%" cy="50%" r= "50%" fx="40%" fy="40%"  >
            <stop offset="0%" style="stop-color:rgb(255,255,255);
      stop-opacity:0" />
            <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
        </radialGradient>
    </defs>
    <rect x="10" y="10" width="100" height="80" fill="url(#grad1)" />
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/6dh49JrST92a32iLYB_AiQ/zh-cn_image_0000002538020848.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=CA4FF96E184674C52FC71362E3FCDE6A11507F9CAF8586E16BE0FEAAF00A5C85) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/jKFUFy6dRiu9F-M_FE804w/zh-cn_image_0000002538180774.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C7A804D6C4A09955BAE46334F263E57CEF36DA5921D881F4B0C0DBD11F98AB8F) |

#### \[h2\]mask参数异常时默认效果变更

[mask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)遮罩的x、y、width、height等参数允许是数字、百分数、小数，当参数赋予错误类型时，从取0值变更为取默认值{-10%，-10%，120%，120%}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/E4OyWE_kQky9-K-yWenpTg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A85A3FBC7962945F91E657B001A82C72C5A057A96A4A0264A15F7833CAD85631)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" x="0%” y=“0%" width="100" height="100" maskUnits="userSpaceOnUse" maskContentUnits="userSpaceOnUse">
      <circle cx="50" cy="50" r="50" fill="red" />
    </mask>
  </defs>
  <rect x="0" y="0" width="200" height="200" fill="blue" mask="url(#mask1)"/>
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nk4ZbU2vSl6OBjlXC7PisA/zh-cn_image_0000002569020559.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=2EB1207BBF6CE7C52A143FBA26869BF6D0F53969DD2FB421192AAD568EE999FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/k8R4b9dqRL2i-J7CIhqsLA/zh-cn_image_0000002568900551.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=7C1CE10311087B5A938DEC6C0D6527EBA559F90A541324AD217EED94676D2710) |

#### \[h2\]filter参数异常时默认效果变更

[filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)滤镜的x、y、width、height等参数允许是数字、百分数、小数，当参数赋予错误类型时，从取0值变更为取默认值{-10%，-10%，120%，120%}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/y3KvaQr8SRiW3_9U03wT8g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=938E06F634A85845F48414F89BE7215068E958945FE8B894E42A4ABB8CAD2A28)

SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```xml
<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" width="300" height="300">
  <defs>
    <filter id="blurMe" x="0%” y=“0%" width="100%" height="100%">
      <feColorMatrix in="SourceGraphic" type = "hueRotate" values="180"/>
    </filter>
  </defs>
  <circle cx="60" cy="60" r="50" fill="blue" filter="url(#blurMe)"/>
</svg>
```

| 扩展前 | 扩展后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/0y_Tmz-bRLCu70pCiWS0-g/zh-cn_image_0000002538020850.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=15DA24FDD009C12FC8C09FF6E7C84F7ECB855214615ED022C2138005AEA69F6D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/3qHObjHHRCme-G1bvEJ8-g/zh-cn_image_0000002538180776.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A588E36CD809E9831D8438D82198EEE5E63CFC1D706C3E876F0C5DF87323616F) |
