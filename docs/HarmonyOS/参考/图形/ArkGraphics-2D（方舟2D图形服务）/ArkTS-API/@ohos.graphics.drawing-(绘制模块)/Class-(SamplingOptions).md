---
title: "Class (SamplingOptions)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-samplingoptions"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "ArkTS API"
  - "@ohos.graphics.drawing (绘制模块)"
  - "Class (SamplingOptions)"
captured_at: "2026-04-17T01:48:46.832Z"
---

# Class (SamplingOptions)

采样选项对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/wELuAorOTV-C5fhn0ZdoHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014849Z&HW-CC-Expire=86400&HW-CC-Sign=6EDBCAF20EC64012C105F415CDEB09A8DC12F914A20C1E3CAB5C713ECDC1BC58)

-   本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   本模块使用屏幕物理像素单位px。
    
-   本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。
    

#### 导入模块

```ts
import { drawing } from '@kit.ArkGraphics2D';
```

#### constructor12+

constructor()

构造一个新的采样选项对象，[FilterMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#filtermode12)的默认值为FILTER\_MODE\_NEAREST。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```ts
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    let samplingOptions = new drawing.SamplingOptions();
  }
}
```

#### constructor12+

constructor(filterMode: FilterMode)

构造一个新的采样选项对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filterMode | [FilterMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#filtermode12) | 是 | 过滤模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```ts
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let samplingOptions = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
  }
}
```
