---
title: "ImageData对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "画布组件"
  - "ImageData对象"
captured_at: "2026-04-17T01:48:05.672Z"
---

# ImageData对象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/4EeAq82EQyi0gHPqBMETCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=78FAE36DDBB3BE44CAB06943812682A5A612B28E81EA7ED2245E71AA0217687E)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

ImageData对象可以存储[canvas组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvas)渲染的像素数据。

#### 属性

| 属性 | 类型 | 描述 |
| :-- | :-- | :-- |
| width | number | 矩形区域实际像素宽度。 |
| height | number | 矩形区域实际像素高度。 |
| data | <Uint8ClampedArray> | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 |

#### 示例

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  onShow() {
    const el =this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(0,0,200,200);
    var imageData = ctx.createImageData(1,1);
    promptAction.showToast({
      message:imageData,
      duration:5000
    })
  }
}
```
