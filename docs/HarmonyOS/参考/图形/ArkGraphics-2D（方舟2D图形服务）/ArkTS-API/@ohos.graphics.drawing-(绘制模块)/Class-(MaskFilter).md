---
title: "Class (MaskFilter)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-maskfilter"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "ArkTS API"
  - "@ohos.graphics.drawing (绘制模块)"
  - "Class (MaskFilter)"
captured_at: "2026-04-17T01:48:46.633Z"
---

# Class (MaskFilter)

蒙版滤镜对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Ij-tAjaLT36pwGY1lretjg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=47F6AD473B9C1EC67DBED678F47FB927156AF7F6F5DFEF21644EB774802843CD)

-   本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   本模块使用屏幕物理像素单位px。
    
-   本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。
    

#### 导入模块

```ts
import { drawing } from '@kit.ArkGraphics2D';
```

#### createBlurMaskFilter12+

static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter

创建具有模糊效果的蒙版滤镜。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| blurType | [BlurType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blurtype12) | 是 | 模糊类型。 |
| sigma | number | 是 | 高斯模糊的标准偏差，必须为大于0的浮点数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [MaskFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-maskfilter) | 返回创建的蒙版滤镜对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```ts
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
  }
}
```
