---
title: "Image对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-image"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "画布组件"
  - "Image对象"
captured_at: "2026-04-17T01:48:05.635Z"
---

# Image对象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/tnt2E9KEQMWsUI6mopw9sQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=33A76AFCA1D3D1EF3194B8FC3FBDE0A8E5C67D909EBEF3651FA8D4972D942E4F)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

图片对象。

#### 属性

| 属性 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| src | string | \- | 是 | 图片资源的路径。 |
| width | <length> | 0px | 否 | 图片的宽度。 |
| height | <length> | 0px | 否 | 图片的高度。 |
| onload | Function | \- | 否 | 图片加载成功后触发该事件，无参数。 |
| onerror | Function | \- | 否 | 图片加载失败后触发该事件，无参数。 |

#### 示例

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
    onShow() {
        const el = this.$refs.canvas;
        var ctx = el.getContext('2d');
        var img = new Image();
        // 图片路径建议放在common目录下
        img.src = 'common/images/example.jpg';
        img.onload = function () {
            console.log('Image load success');
            ctx.drawImage(img, 0, 0, 360, 250);
        };
        img.onerror = function () {
            console.error('Image load fail');
        };
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/teUOnYprTsq5Aje8T_Zn9A/zh-cn_image_0000002538181108.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=45C493D6B469D7AD86F4E795CD333AD5F49B4311F502E1645F2E418756FB079E)
