---
title: "@ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendablecolorspacemanager"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "ArkTS API"
  - "@ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)"
captured_at: "2026-04-17T01:48:46.490Z"
---

# @ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)

本模块提供管理抽象化色域对象的一些基础能力，包括可共享的色彩管理的创建与可共享的色域基础属性的获取等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/NcIC677QRUC9OHdMrk_mpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014848Z&HW-CC-Expire=86400&HW-CC-Sign=65C449A217EFDE6FE790C85F9149A03985D4EB3BE8840B2CDB8351AFC6547A83)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { sendableColorSpaceManager } from '@kit.ArkGraphics2D';
```

#### ISendable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 类型 | 说明 |
| :-- | :-- |
| [lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang#langisendable) | 所有Sendable类型的父类型。 |

#### sendableColorSpaceManager.create

create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager

创建标准可共享的色彩管理。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| colorSpaceName | [colorSpaceManager.ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager#colorspace) | 是 | 
标准色域类型枚举值。

UNKNOWN与CUSTOM不可用于直接创建色域对象。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ColorSpaceManager](#colorspacemanager) | 
返回当前创建的可共享的色彩管理实例。

该实例继承ISendable，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[色彩管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-colorspace-manager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```ts
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
colorSpace = sendableColorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
```

#### sendableColorSpaceManager.create

create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager

创建用户自定义可共享的色彩管理实例。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| primaries | [colorSpaceManager.ColorSpacePrimaries](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager#colorspaceprimaries) | 是 | 色域标准三原色。 |
| gamma | number | 是 | 色域gamma值，取值为大于0的浮点数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ColorSpaceManager](#colorspacemanager) | 
返回当前创建的可共享的色彩管理实例。

色域类型定义为[colorSpaceManager.ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager#colorspace)枚举值CUSTOM。

该实例继承ISendable，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[色彩管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-colorspace-manager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```ts
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
let primaries: colorSpaceManager.ColorSpacePrimaries = {
  redX: 0.1,
  redY: 0.1,
  greenX: 0.2,
  greenY: 0.2,
  blueX: 0.3,
  blueY: 0.3,
  whitePointX: 0.4,
  whitePointY: 0.4
};
let gamma: number = 2.2;
colorSpace = sendableColorSpaceManager.create(primaries, gamma);
```

#### ColorSpaceManager

当前可共享的色彩管理实例。

下列API示例中都需先使用[create()](#sendablecolorspacemanagercreate)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

#### \[h2\]getColorSpaceName

getColorSpaceName(): colorSpaceManager.ColorSpace

获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [colorSpaceManager.ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager#colorspace) | 返回色域类型枚举值。 |

**示例：**

```ts
let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();
```

#### \[h2\]getWhitePoint

getWhitePoint(): collections.Array<number>

获取色域白点值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [collections.Array<number>](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array) | 返回色域白点值\[x, y\]。 |

**示例：**

```ts
import { collections } from '@kit.ArkTS';
let point: collections.Array<number> = colorSpace.getWhitePoint();
```

#### \[h2\]getGamma

getGamma(): number

获取色域gamma值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回色域gamma值。 |

**示例：**

```ts
let gamma: number = colorSpace.getGamma();
```
