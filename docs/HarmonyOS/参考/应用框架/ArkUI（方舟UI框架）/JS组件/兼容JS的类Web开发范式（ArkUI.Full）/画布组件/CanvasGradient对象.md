---
title: "CanvasGradient对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "画布组件"
  - "CanvasGradient对象"
captured_at: "2026-04-17T01:48:05.645Z"
---

# CanvasGradient对象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/IdaXhxTPSpa09dKGB25lag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=01B56CE79818A4F40F8C94325D0C5FA41015FE6803BE5EE9540A0DC4993CF65B)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

渐变对象。

#### addColorStop

addColorStop(offset: number, color: string): void

设置渐变断点值，包括偏移和颜色。

**参数：**

| 参数 | 类型 | 描述 |
| :-- | :-- | :-- |
| offset | number | 设置渐变点距离起点的位置占总体长度的比例，范围为0到1。 |
| color | string | 设置渐变的颜色。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    const gradient = ctx.createLinearGradient(50, 0, 300, 100);
    gradient.addColorStop(0.0, '#ff0000')
    gradient.addColorStop(0.5, '#ffffff')
    gradient.addColorStop(1.0, '#00ff00')
    ctx.fillStyle = gradient
    ctx.fillRect(0, 0, 300, 300)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/J79EYHIFQkehtYf3DBWtew/zh-cn_image_0000002569020895.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=E8D1FE9CD2AC101CBC076C51E44E9CA80E0671373CF4BF4FF71B9E91F344D4FF)
