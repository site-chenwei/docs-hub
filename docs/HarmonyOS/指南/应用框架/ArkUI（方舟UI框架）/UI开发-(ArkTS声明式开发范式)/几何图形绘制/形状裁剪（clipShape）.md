---
title: "形状裁剪（clipShape）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-clip-shape"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "几何图形绘制"
  - "形状裁剪（clipShape）"
captured_at: "2026-04-17T01:35:38.407Z"
---

# 形状裁剪（clipShape）

可利用[clipShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clipshape12)接口将组件裁剪为所需的形状。调用该接口后，可以保留该形状覆盖的组件部分，同时移除组件的其余部分。裁剪形状本身是不可见的。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/jdf4DgF3ToKvPlzTUHWhxQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=853566607E528AA7743408E0F678441229201970CC9701E4A76F126EFDC2668C)

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度，具体形状支持的属性参考具体[形状](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape)的文档。

形状中的[fill](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#fill)属性对clipShape接口不生效。

#### 裁剪圆形

通过设置CircleShape，将图片裁剪为圆形。

// xxx.ets
import { CircleShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      // 用一个280px直径的圆对图片进行裁剪
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new CircleShape({ width: '280px', height: '280px' }))
        .width('500px').height('280px')

      // 用一个350px直径的圆对图片进行裁剪
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new CircleShape({ width: '350px', height: '350px' }))
        .width('500px').height('370px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/5wB2a3WuTn6-E6_L3Xfcew/zh-cn_image_0000002569018575.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=3D2089C336D5D89F8050625634C9A7C2F78F2CC80DE624397C909A9D30E0B633)

#### 裁剪椭圆形

通过设置EllipseShape，将图片裁剪为椭圆形。

// xxx.ets
import { EllipseShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new EllipseShape({ width: '280px', height: '200px' }))
        .width('500px').height('400px')

      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new EllipseShape({ width: '380px', height: '280px' }))
        .width('500px').height('400px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/tQKPVuCWRRezds97f9R12A/zh-cn_image_0000002568898565.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=1586EB69AB54B8B52EF34CE676EE35CFEE12D4CABC0C34820FF88C1FAEBD32AC)

#### 裁剪矩形

通过设置RectShape，将图片裁剪为矩形。

// xxx.ets
import { RectShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new RectShape({ width: '200px', height: '200px' }))
        .width('500px').height('400px')

      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new RectShape({ width: '380px', height: '280px' }))
        .width('500px').height('400px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/jdy1W8MRRc6HTivWElC5ZQ/zh-cn_image_0000002538018860.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=D8FCC3744F4F39E3FD4A96D1D91C5B08D5E3CB371A162FE81717B896198877DC)

#### 裁剪不规则形状

通过设置PathShape，将图片裁剪为不规则形状。

// xxx.ets
import { PathShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      Row() {
        // 请将$r('app.media.background')替换为实际资源文件
        Image($r('app.media.background'))
          .clipShape(new PathShape({ commands: 'M0 0 H400 V200 H0 Z' }))
          .width('500px').height('300px')
      }
      .clip(true)
      .borderRadius(20)
    }
    .width('100%')
    .margin({ top: 15 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/Om1zqJTLQw2B3b3X5VsR3g/zh-cn_image_0000002538178788.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=DA8F2DF701615D4C1C026EF0EB36F13494E7104B18D53E4FE197F0C66193A9D0)
