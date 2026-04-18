---
title: "Enums"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "ArkTS API"
  - "@ohos.graphics.drawing (绘制模块)"
  - "Enums"
captured_at: "2026-04-17T01:48:46.972Z"
---

# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/YEO9q4wnSvCGDxW5c1HSEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=D3B7044B0E5F7B179E7FBDE43A0D67F7D47B2174077622B2883EBFDA1FC6E2E0)

-   本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本模块使用屏幕物理像素单位px。
    
-   本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。
    

#### BlendMode

混合模式枚举。混合模式会将两种颜色（源色、目标色）以特定的方式混合生成一种新的颜色，通常用于叠加、滤镜和遮罩等图形操作场景。混合操作会分别作用于红、绿、蓝三个颜色通道，采用相同的混合逻辑，而透明度（Alpha通道）则根据各模式的定义另行处理。

为简洁起见，我们使用以下缩写：

s : source 源的缩写。 d : destination 目标的缩写。 sa : source alpha 源透明度的缩写。 da : destination alpha 目标透明度的缩写。

计算结果用如下缩写表示：

r : 如果4个通道（透明度、红、绿、蓝）的计算方式相同，用r表示。 ra : 如果只操作透明度通道，用ra表示。 rc : 如果操作3个颜色通道，用rc表示。

以黄色矩形为源图像，蓝色圆形为目标图像，各混合模式枚举生成的效果示意图请参考下表。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 | 示意图 |
| :-- | :-- | :-- | :-- |
| CLEAR | 0 | 清除模式，r = 0，设置为全透明。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Hy4pNYPBQDuenw6ewvVzaw/zh-cn_image_0000002569021531.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=6E4F7EF36F51E9105F103CB8C9F0D554EDB62687D13277935FC72062EF3310E7) |
| SRC | 1 | r = s（result的4个通道，都等于source的4个通道，即结果等于源。），使用源像素替换目标像素。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/6p-DpUq4QZCZfV7TPL7h1A/zh-cn_image_0000002568901521.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=778293113CC7EFA3096E20C053E7C68D40705508D579992EB0B3D521527FEC3E) |
| DST | 2 | r = d（result的4个通道，都等于destination的4个通道，即结果等于目标。），保持目标像素不变。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/bnFMD3wuSfOy4HYqQZw6EQ/zh-cn_image_0000002538021820.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=99EB767737B2D76D963FC0F42B6B3664F260823510C14D24B9DB3AD6E85D203D) |
| SRC\_OVER | 3 | r = s + (1 - sa) \* d，在目标像素上方绘制源像素，考虑源像素的透明度。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7efpdolCQyyDdLR9z91Biw/zh-cn_image_0000002538181746.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=D4CA77C6264BEF0A578B0FE5304A51C90BEEA78FD4D093E10ADF1FC4E04C527D) |
| DST\_OVER | 4 | r = d + (1 - da) \* s，在源像素上方绘制目标像素，考虑目标像素的透明度。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/2UDPJpomQbmyK3tWFFpe6g/zh-cn_image_0000002569021533.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=6D59DF8D4EDA081E81C4684247FD9830B6551F1F8D5BD22D616B3A02603E9A31) |
| SRC\_IN | 5 | r = s \* da，仅保留源像素与目标不透明部分的交集。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/YaRcjWY4RkKX3YkoImrJZw/zh-cn_image_0000002568901523.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=60F8F4115FABE3B1BC1F6146060EB323D6E339A6C190E118188348EE1CB069BE) |
| DST\_IN | 6 | r = d \* sa，仅保留目标像素与源不透明部分的交集。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/8YuN2l7RRr6VE9w8sXHlFA/zh-cn_image_0000002538021822.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=71FB8D6172F1A72C7E73C9B6A95F8AEEF97165E4BBC5B164A21F73B7D62AF551) |
| SRC\_OUT | 7 | r = s \* (1 - da)，保留源像素中不与目标重叠的部分。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/jyn7VCB1SiK7VJ0X8IFeWQ/zh-cn_image_0000002538181748.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=D088131BFB4E1B32B6F4616BD23C24CDB0B42AB984AB9D73FB185573D845CAB1) |
| DST\_OUT | 8 | r = d \* (1 - sa)，保留目标像素中不与源重叠的部分。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/r267MWAHQk-QdiujnGpncQ/zh-cn_image_0000002569021535.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=F1B5CE1C7D92BFAB5B65F95695D88D7DF88CC664BD50A7579D8106790928E21D) |
| SRC\_ATOP | 9 | r = s \* da + d \* (1 - sa)，源像素覆盖在目标像素上，仅在目标不透明部分显示源像素。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/IqvMxYadR2GE7OJnqZZFng/zh-cn_image_0000002568901525.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=E4F372C65BF0565E6C472564D85D5AB394E9B01D499037A3F79D700D1F0D2451) |
| DST\_ATOP | 10 | r = d \* sa + s \* (1 - da)，目标像素覆盖在源像素上，仅在源不透明部分显示目标像素。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ezaWqnTUQ9KYf-dAn3ZKmQ/zh-cn_image_0000002538021824.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=A6D1AC7C0CDCE7B93F5D040F67CF74CE82B879EC6F1B1C79C97463E816A56D90) |
| XOR | 11 | r = s \* (1 - da) + d \* (1 - sa)，仅显示源像素和目标像素中不重叠的部分。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/KoGfBG6mQ4yI_Jet_bJLtA/zh-cn_image_0000002538181750.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=2D6A9C9D667E1D36D11118DB1C641AB78F62AD2EAB613BD189614340E6AEDE83) |
| PLUS | 12 | r = min(s + d, 1)，源和目标像素的颜色值相加。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/FxOmicUORlW6984JjIyr1w/zh-cn_image_0000002569021537.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=D5A83714506FE8F4586BFD4C26C6BB5E0F46E4FBB332604FC32435684C52F619) |
| MODULATE | 13 | r = s \* d，源和目标像素的颜色值相乘。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/UFR9d1YUQ8CuhSAfD63ESg/zh-cn_image_0000002568901527.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=C4CDF27CFCDFBEBCDC7F427731ABAB7EFEEDA83EDB4A6316E13EC551A1A4DDAE) |
| SCREEN | 14 | 滤色模式，r = s + d - s \* d，反转源和目标像素的颜色值，相乘后再反转，结果通常更亮。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/nIpFzEo6RIKKjul0SEKFHA/zh-cn_image_0000002538021826.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=4B2BDD5F290FCF0424D71A21D4F1C30B988AA60EC513D5EF5039AED6A8B11142) |
| OVERLAY | 15 | 叠加模式，根据目标像素的亮度，选择性地应用MULTIPLY或SCREEN模式，增强对比度。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/LU61qmj-TluzRNry3XGVzw/zh-cn_image_0000002538181752.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=0DD732E4A68487C8AF4831640C58BB174C564BE308159709071F60CB43D49B9C) |
| DARKEN | 16 | 变暗模式，rc = s + d - max(s \* da, d \* sa), ra = s + (1 - sa) \* d，取源和目标像素中较暗的颜色值。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/mB9_RcpIQg2Hr0zeiOpzKQ/zh-cn_image_0000002569021539.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=42DEAB2F4781C5855B5799179C94DEFBFC47B907CB86374383F02118A50259F7) |
| LIGHTEN | 17 | 变亮模式，rc = s + d - min(s \* da, d \* sa), ra = s + (1 - sa) \* d，取源和目标像素中较亮的颜色值。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/zOVBtZZNSZmYfT5OZ3QVAQ/zh-cn_image_0000002568901529.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=98BFB3D50A59896802B44AAF0EBFF6E027B22C18039512FBCC82F3D60F54F4C6) |
| COLOR\_DODGE | 18 | 颜色减淡模式，通过减小对比度使目标像素变亮以反映源像素。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/Qt6cgYRLQMSORY6yz6cQwQ/zh-cn_image_0000002538021828.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=E2C215F9FDAC98DFE17934396C422EDF289256C2FCD951AC8C6CEE701BFE4E43) |
| COLOR\_BURN | 19 | 颜色加深模式，通过增加对比度使目标像素变暗以反映源像素。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Tf7uafWhRdGNNVk7PLY9hw/zh-cn_image_0000002538181754.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=8978F6F31AF07866290FDBD7D8CE3970C9E9608B1DA276D764648AD30FBF51BC) |
| HARD\_LIGHT | 20 | 强光模式，根据源像素的亮度，选择性地应用MULTIPLY或SCREEN模式。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/bvGignQGSwyFDLnSQqDpNg/zh-cn_image_0000002569021541.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=EDF4E17145388B4232F203EE55818FFBCE2E4E58C77D799A709CCECAE8073908) |
| SOFT\_LIGHT | 21 | 柔光模式，根据源像素的亮度，柔和地变亮或变暗目标像素。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/AJdOQK_IS26qp-ygxTjz9Q/zh-cn_image_0000002568901531.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=4728CC5020ADF5E13E88F10CB014A22B05343ABE57FF4F124D47046C65B33275) |
| DIFFERENCE | 22 | 差值模式，rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = s + (1 - sa) \* d，计算源和目标像素颜色值的差异。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/L---tN2aTdGofH9mtrQ2Vg/zh-cn_image_0000002538021830.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=BB7912236CB1CB91AC2C567DF58F388C52237C1FA661E4EFC7447D4CF87213B2) |
| EXCLUSION | 23 | 排除模式，rc = s + d - two(s \* d), ra = s + (1 - sa) \* d，类似于DIFFERENCE，但对比度较低。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/r5EaecigQSy5GOFfF-RlLA/zh-cn_image_0000002538181756.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=BA04B075BBBBFD8AA018906D8A3704CA5E254119BD80EE751F83603D4CC158EB) |
| MULTIPLY | 24 | 正片叠底，r = s \* (1 - da) + d \* (1 - sa) + s \* d，源和目标像素的颜色值相乘，结果通常更暗。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/zIfbLWRMTE2wTAZeGX1pvA/zh-cn_image_0000002569021543.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=D7DBFD7AF26450D96E8C3C2F14BC242BCEB06DAB62927437D7E817D945EF8FA8) |
| HUE | 25 | 色相模式，使用源像素的色相，目标像素的饱和度和亮度。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/JPxNudwgSJyGy3UjX1jB5Q/zh-cn_image_0000002568901533.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=9F6E9A94FCAE20DF503C79C4ABCA49C428C236AA490263652814AD2A3F37A456) |
| SATURATION | 26 | 饱和度模式，使用源像素的饱和度，目标像素的色相和亮度。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/wWlo_N-HQP6BcTOgKFwpDQ/zh-cn_image_0000002538021832.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=56858EB39C410D793F2220964BA8FB1DAE7AE8EF1AB2A81CB7157F6AF3E05F54) |
| COLOR | 27 | 颜色模式，使用源像素的色相和饱和度，目标像素的亮度。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/RxBiFdQRSA2JVC4Oa7j6wQ/zh-cn_image_0000002538181758.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=E4633479736AFE4ECBC4445895F0ABAC360F67CE9D42AEF35DB5795009F8D82A) |
| LUMINOSITY | 28 | 亮度模式，使用源像素的亮度，目标像素的色相和饱和度。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/FfJwUg_9SquvHfXqOSYMiw/zh-cn_image_0000002569021545.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=44818F284E1B61A0E68296A62C5E8F1B2E19290B7E77118D7F4C35C05E15993F) |

#### PathMeasureMatrixFlags12+

路径测量中的矩阵信息维度枚举，常用于控制物体沿路径移动的动画场景。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| GET\_POSITION\_MATRIX | 0 | 获取位置信息对应的矩阵。 |
| GET\_TANGENT\_MATRIX | 1 | 获取切线信息对应的矩阵。 |
| GET\_POSITION\_AND\_TANGENT\_MATRIX | 2 | 获取位置和切线信息对应的矩阵。 |

#### SrcRectConstraint12+

源矩形区域约束类型枚举，用于在画布绘制图像时指定是否将采样范围限制在源矩形区域内。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STRICT | 0 | 严格限制采样范围在源矩形区域内，速度较慢。 |
| FAST | 1 | 允许采样范围超出源矩形范围，速度较快。 |

#### ShadowFlag12+

控制阴影绘制行为的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 不使用任何阴影处理选项。 |
| TRANSPARENT\_OCCLUDER | 1 | 遮挡物是半透明的。 |
| GEOMETRIC\_ONLY | 2 | 仅使用几何阴影效果。 |
| ALL | 3 | 使用所有可用的阴影处理选项，以生成组合阴影效果，包括半透明遮挡和几何阴影效果。 |

#### PathOp12+

路径操作类型枚举，可用于合并或裁剪路径等功能。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DIFFERENCE | 0 | 差集操作。 |
| INTERSECT | 1 | 交集操作。 |
| UNION | 2 | 并集操作。 |
| XOR | 3 | 异或操作。 |
| REVERSE\_DIFFERENCE | 4 | 反向差集操作。 |

#### PathIteratorVerb18+

迭代器包含的路径操作类型枚举，可用于读取path的操作指令。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| MOVE | 0 | 设置起始点。 |
| LINE | 1 | 添加线段。 |
| QUAD | 2 | 添加二阶贝塞尔圆滑曲线。 |
| CONIC | 3 | 添加圆锥曲线。 |
| CUBIC | 4 | 添加三阶贝塞尔圆滑曲线。 |
| CLOSE | 5 | 路径闭合。 |
| DONE | CLOSE + 1 | 路径设置完成。 |

#### TextEncoding

文本的编码类型枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| TEXT\_ENCODING\_UTF8 | 0 | 使用1个字节表示UTF-8或ASCII。 |
| TEXT\_ENCODING\_UTF16 | 1 | 使用2个字节表示大部分unicode。 |
| TEXT\_ENCODING\_UTF32 | 2 | 使用4个字节表示全部unicode。 |
| TEXT\_ENCODING\_GLYPH\_ID | 3 | 使用2个字节表示glyph index。 |

#### ClipOp12+

画布裁剪方式的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 | 示意图 |
| :-- | :-- | :-- | :-- |
| DIFFERENCE | 0 | 将指定区域裁剪（取差集）。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/oUY9xcOZRU21NFkn5ONluA/zh-cn_image_0000002568901535.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=1AECDCD7776A8680911B064BEB11BBFCBB0E25E19E7B4D746ECB185B9F3A80DF) |
| INTERSECT | 1 | 将指定区域保留（取交集）。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/5KoFosKPS4q8Chn4JamnVw/zh-cn_image_0000002538021834.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=2A41838F919FA0EFD1FD904650FD194BC3D2CE6C5D0D42B8C40F5FAC13533265) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/pHCV9GUQTZGzgszNwvzSfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=F3FBA7ACECDF3F4954EBA19DD60625B7AE47941C6F4E069DAC388245FE345F6C)

示意图展示了以INTERSECT方式裁剪一个矩形后，使用不同枚举值继续裁剪一个圆形的结果，绿色区域为最终的裁剪区域。

#### FilterMode12+

过滤模式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FILTER\_MODE\_NEAREST | 0 | 邻近过滤模式。 |
| FILTER\_MODE\_LINEAR | 1 | 线性过滤模式。 |

#### PathDirection12+

添加闭合轮廓方向的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CLOCKWISE | 0 | 顺时针方向添加闭合轮廓。 |
| COUNTER\_CLOCKWISE | 1 | 逆时针方向添加闭合轮廓。 |

#### PathFillType12+

定义路径的填充类型枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| WINDING | 0 | 绘制区域中的任意一点，向任意方向射出一条射线，对于射线和路径的所有交点，初始计数为0，遇到每个顺时针的交点（路径从射线的左边向右穿过），计数加1，遇到每个逆时针的交点（路径从射线的右边向左穿过），计数减1，若最终的计数结果不为0，则认为这个点在路径内部，需要被涂色；若计数为0则不被涂色。 |
| EVEN\_ODD | 1 | 绘制区域中的任意一点，向任意方向射出一条射线，若这条射线和路径相交的次数是奇数，则这个点被认为在路径内部，需要被涂色；若是偶数则不被涂色。 |
| INVERSE\_WINDING | 2 | WINDING涂色规则取反。 |
| INVERSE\_EVEN\_ODD | 3 | EVEN\_ODD涂色规则取反。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UhvYuL5vRCiQBrZ9bWMlaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=41B688F4F9181DD204A3C07FC4633989EA69998AEF2E8331AE3C406DAA325F3F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/gjf05x-zQymFxi-FxGm08Q/zh-cn_image_0000002538181760.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=447B9897DF3C55D5B2C71250A8844960DA6E7C689BB70E30983EFF69A39D41BD)

如图所示圆环为路径，箭头指示路径的方向，p为区域内任意一点，蓝色线条为点p出发的射线，黑色箭头所指为对应填充规则下使用蓝色填充路径的结果。WINDING填充规则下，射线与路径的交点计数为2，不为0，点p被涂色；EVEN\_ODD填充规则下，射线与路径的相交次数为2，是偶数，点p不被涂色。

#### PointMode12+

绘制数组点的方式的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| POINTS | 0 | 分别绘制每个点。 |
| LINES | 1 | 将每对点绘制为线段。 |
| POLYGON | 2 | 将点阵列绘制为开放多边形。 |

#### FontEdging12+

字型边缘效果类型枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ALIAS | 0 | 无抗锯齿处理。 |
| ANTI\_ALIAS | 1 | 使用抗锯齿来平滑字型边缘。 |
| SUBPIXEL\_ANTI\_ALIAS | 2 | 使用次像素级别的抗锯齿平滑字型边缘，可以获得更平滑的字型渲染效果。 |

#### FontHinting12+

字型轮廓效果类型枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 不修改字型轮廓。 |
| SLIGHT | 1 | 最小限度修改字型轮廓以改善对比度。 |
| NORMAL | 2 | 修改字型轮廓以提高对比度。 |
| FULL | 3 | 修改字型轮廓以获得最大对比度。 |

#### FontMetricsFlags12+

字体度量标志枚举，指示字体度量中的各字段数据是否有效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| UNDERLINE\_THICKNESS\_VALID | 1 << 0 | 表示[FontMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-i#fontmetrics)结构中的underlineThickness（下划线厚度）字段有效。 |
| UNDERLINE\_POSITION\_VALID | 1 << 1 | 表示[FontMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-i#fontmetrics)结构中的underlinePosition（下划线位置）字段有效。 |
| STRIKETHROUGH\_THICKNESS\_VALID | 1 << 2 | 表示[FontMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-i#fontmetrics)结构中strikethroughThickness（删除线厚度）是有效的。 |
| STRIKETHROUGH\_POSITION\_VALID | 1 << 3 | 表示[FontMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-i#fontmetrics)结构中strikethroughPosition（删除线位置）字段有效。 |
| BOUNDS\_INVALID | 1 << 4 | 表示[FontMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-i#fontmetrics)结构中的边界度量值（如top、bottom、xMin、xMax）无效。 |

#### RectType12+

定义填充网格的矩形类型的枚举。仅在[Lattice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-lattice)中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DEFAULT | 0 | 将图像绘制到矩形网格中。 |
| TRANSPARENT | 1 | 将矩形网格设置为透明的。 |
| FIXEDCOLOR | 2 | 将[Lattice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-lattice)中fColors数组的颜色绘制到矩形网格中。 |

#### PathDashStyle18+

路径效果的绘制样式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| TRANSLATE | 0 | 不会随着路径旋转，只会平移。 |
| ROTATE | 1 | 随着路径的旋转而旋转。 |
| MORPH | 2 | 随着路径的旋转而旋转，并在转折处进行拉伸或压缩等操作以增加平滑度。 |

#### TileMode12+

着色器效果平铺模式的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CLAMP | 0 | 如果着色器效果超出其原始边界，剩余区域使用着色器的边缘颜色填充。 |
| REPEAT | 1 | 在水平和垂直方向上重复着色器效果。 |
| MIRROR | 2 | 在水平和垂直方向上重复着色器效果，交替镜像图像，以便相邻图像始终接合。 |
| DECAL | 3 | 仅在其原始边界内渲染着色器效果。 |

#### JoinStyle12+

定义线条转角样式的枚举，即画笔在绘制折线段时，在折线转角处的样式。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 | 示意图 |
| :-- | :-- | :-- | :-- |
| MITER\_JOIN | 0 | 转角类型为尖角，如果折线角度比较小，则尖角会很长，需要使用限制值（miter limit）进行限制。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Fiup3QErSuS7Y8l6vhnIJw/zh-cn_image_0000002569021547.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=EB9485F75C6CD348B0B88957B978E956C7C78A5334DF7D7985D46C52908DD444) |
| ROUND\_JOIN | 1 | 转角类型为圆头。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/BMUhKzW5QTe0mWYr05PSCg/zh-cn_image_0000002568901537.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=5DE95B03FD34A1FFFC3B93059CFBFF11674C30E79406DEEF49637EF5A65429BA) |
| BEVEL\_JOIN | 2 | 转角类型为平头。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/xuXkWLv9QpODSY4VkUhrmQ/zh-cn_image_0000002538021836.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=A88F5C3EE5628D5E5E2CE8D29DEBECA6559131C16C36347ADEF8B978F2330219) |

#### CapStyle12+

定义线帽样式的枚举，即画笔在绘制线段时，在线段头尾端点的样式。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 | 示意图 |
| :-- | :-- | :-- | :-- |
| FLAT\_CAP | 0 | 没有线帽样式，线条头尾端点处横切。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/7AFh1wGlRsCbk3s0cNTShA/zh-cn_image_0000002538181762.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=ABDBC8833CBC597ED5C6FB2F508EB363FEB18987DA698E7347BC621CB7C6C86C) |
| SQUARE\_CAP | 1 | 线帽的样式为方框，线条的头尾端点处多出一个方框，方框宽度和线段一样宽，高度是线段宽度的一半。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/VDdEh28uRASjVy0eeEV2kQ/zh-cn_image_0000002569021549.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=6E2EB7723A92CA07E469BADEB00C26240CCE9E10F8C1BD27185910C3CC9BE6B4) |
| ROUND\_CAP | 2 | 线帽的样式为圆弧，线条的头尾端点处多出一个半圆弧，半圆的直径与线段宽度一致。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/SI8LdiCYR2yzKjBvtXBXQw/zh-cn_image_0000002568901539.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=D7A89FF31EFDFADE2B6318B055A8CE4D2EE8C22A32BDD4C3CBDE2CFCACBC02E3) |

#### BlurType12+

定义蒙版滤镜模糊中操作类型的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 | 示意图 |
| :-- | :-- | :-- | :-- |
| NORMAL | 0 | 全面模糊，外圈边缘和内部实体一起模糊。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/QjTkf7MFTBSmHkwf1TS1WA/zh-cn_image_0000002538021838.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=D1941463F52452BA69F1CE1D510555A0214AF700ECBAB4E507121EDAEF93776B) |
| SOLID | 1 | 内部实体不变，只模糊外圈边缘部分。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/n_4eon1lTt2_UUkV-mz6Bw/zh-cn_image_0000002538181764.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=291700951729D1F9BA31FD88F66CE6AEBA46B4E531C8E5D629EE42372C7328D8) |
| OUTER | 2 | 只有外圈边缘模糊，内部实体完全透明。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/wU9-fSM1TD-ArnyCKcER9Q/zh-cn_image_0000002569021551.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=633F5EB683273EC75CCFEDA85264E8AAD1019AB07FEEF70C3ED7F525C6EAD986) |
| INNER | 3 | 只有内部实体模糊，外圈边缘清晰。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Bfaj7I0hQqqQOV0ZhVFU1w/zh-cn_image_0000002568901541.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=F550A5BA8068A091FBCAED4F62FAE249B5A0BAB9135B533D691FFA11603A6A2D) |

#### ScaleToFit12+

源矩形到目标矩形的缩放方式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FILL\_SCALE\_TO\_FIT | 0 | 将源矩形缩放以填充满整个目标矩形，可能会改变源矩形的长宽比。 |
| START\_SCALE\_TO\_FIT | 1 | 保持源矩形的长宽比进行缩放，并对齐到目标矩形的左上方。 |
| CENTER\_SCALE\_TO\_FIT | 2 | 保持源矩形的长宽比进行缩放，并居中对齐到目标矩形。 |
| END\_SCALE\_TO\_FIT | 3 | 保持源矩形的长宽比进行缩放，并对齐到目标矩形的右下方。 |

#### RegionOp12+

两个区域合并时的操作的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 | 示意图 |
| :-- | :-- | :-- | :-- |
| DIFFERENCE | 0 | 两个区域的相减操作。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/DOQBHryHRnKPx-PeYxlGjg/zh-cn_image_0000002538021840.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=F175E085132779B99E4715A5B6CA7191E744F07C25957E7FBE4ED4C42205D6BC) |
| INTERSECT | 1 | 两个区域的相交操作。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/R8wIrp-wQLuZnKPC65W0DQ/zh-cn_image_0000002538181766.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=F0619CF6CE3FB5AB38D667682D3DD15134D4EB41E6E200569F43ED88B316A461) |
| UNION | 2 | 两个区域的联合操作。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/w1abCzGmQtu-imKN71nz9w/zh-cn_image_0000002569021553.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=3C1CAF09446C2181A33E6B2A6F6397580488CBAFDB8E529E3571273FCEC49ACD) |
| XOR | 3 | 两个区域的异或操作。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/lJBLGneGQgqUtD9Mz27dAg/zh-cn_image_0000002568901543.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=5EADC58AD70BAF0B76346B9AA894D52CD68C4407EF0F3FDF1B87FE407F9E8473) |
| REVERSE\_DIFFERENCE | 4 | 两个区域的反向相减操作。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/9u5kN-3RRmKDBQ1p5p2Jrw/zh-cn_image_0000002538021842.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=0FDA5CE7BEBB214058F2FFCC6B0618A523E0386B48328B3B1B6C8E1E69161ECE) |
| REPLACE | 5 | 两个区域替换操作。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/wrdPP-7cQ0SMO10hFGEGDg/zh-cn_image_0000002538181768.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=26D1531B07794ABF72EF8DB6D5D6FBD9FC8F796AC15C565C8CB00C542F31A958) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/NIafBwaiQba6XigEG-_EWQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=6BA6B15A3A91113420B8AC70FA26C9A26D37E949A88E509058C9FD24CD71D048)

示意图展示了一个以红色区域为基础，使用不同枚举值与另一个蓝色区域合并后获得的结果，其中绿色区域为最终得到的区域。

#### CornerPos12+

圆角位置枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| TOP\_LEFT\_POS | 0 | 左上角圆角位置。 |
| TOP\_RIGHT\_POS | 1 | 右上角圆角位置。 |
| BOTTOM\_RIGHT\_POS | 2 | 右下角圆角位置。 |
| BOTTOM\_LEFT\_POS | 3 | 左下角圆角位置。 |

#### VertexMode23+

顶点绘制的连接方式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 值 | 说明 | 示意图 |
| :-- | :-- | :-- | :-- |
| TRIANGLES\_VERTEXMODE | 0 | 每三个顶点来自不同的三角形。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/edBnjudwQlaLtAQRQ0wWGQ/zh-cn_image_0000002569021555.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=8B83E191AC8C05C53637CACFD1E70BC96AE8CC451332B37729D305FFD96B5813) |
| TRIANGLESSTRIP\_VERTEXMODE | 1 | 连续的三角形共享一条边。对于连续表面效率高。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/gR8G4LTKT9StGF_TCfm_qQ/zh-cn_image_0000002568901545.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=F6E2EE8C2646599374AF6001D4A1FB23F432C7BD90286726017FF7E520E63721) |
| TRIANGLESFAN\_VERTEXMODE | 2 | 所有三角形共享一个顶点。非常适合圆形/扇形。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/BbMLB7N7TJK9quXzh_K-xw/zh-cn_image_0000002538021844.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=B8B50C2808E36E3F6D1FBB98BC59CF4911B446B7FB9C0F13C51AA7789E964102) |
