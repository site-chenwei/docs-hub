---
title: "Canvas对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (兼容JS的类Web开发范式)"
  - "常见组件开发指导"
  - "Canvas开发指导"
  - "Canvas对象"
captured_at: "2026-04-17T01:35:40.771Z"
---

# Canvas对象

Canvas组件提供画布，用于自定义绘制图形。具体用法请参考[CanvasRenderingContext2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d)。

#### 创建Canvas组件

在pages/index目录下的hml文件中创建一个Canvas组件。

```html
<!-- xxx.hml -->
<div class="container">
  <canvas></canvas>
</div>
```

```css
/* xxx.css */
.container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F1F3F5;
}

canvas {
    background-color: #00ff73;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/FVxAbFz0QXG1s6QO6u3l8g/zh-cn_image_0000002538019054.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=6B28DBAD9C4A6DDE74A88437D6578596DC76394FF4A7DE138007197A4D1B3ABA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/bxAW9vfaQhO55Lj_OzVsYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=DD5DBD44B8D2F2E40BFA21A2C33D8C6A99F9134A01479E13E454926D99A726CB)

-   Canvas组件默认背景色与父组件的背景色一致。
    
-   Canvas默认宽高为width: 300px，height: 150px。
    

#### 添加样式

Canvas组件设置宽（width）、高（height）、背景色（background-color）及边框样式（border）。

```html
<!-- xxx.hml -->
<div class="container">
  <canvas></canvas>
</div>
```

```css
/* xxx.css */
.container {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F1F3F5;
    width: 100%;
    height: 100%;
}

canvas {
    width: 500px;
    height: 500px;
    background-color: #fdfdfd;
    border: 5px solid red;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/clq8ZlKKS_C67HAV4RarUg/zh-cn_image_0000002538178982.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=8E3B263B599C3B0C3D0DE94E0F3AAB4B3778FCFFEF550D982D62570CCE5682F0)

#### 添加事件

Canvas添加长按事件，长按后可获取Canvas组件的dataUrl值（toDataURL方法返回的图片信息），打印在下方文本区域内。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/AmagBHNvS-KIFt300FOt9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=23B760A427656A1C1894B5D860BFC8F75EF90B1A70DAEA4BC6784AF4CD4F46C6)

promptAction相关接口参考[弹窗](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction)。

```html
<!-- xxx.hml -->
<div class="container">
    <canvas ref="canvas1" onlongpress="getUrl"></canvas>
    <text>dataURL</text>
    <text class="content">{{ dataURL }}</text>
</div>
```

```css
/* xxx.css */
.container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F1F3F5;
}

canvas {
    width: 500px;
    height: 500px;
    background-color: #fdfdfd;
    border: 5px solid red;
    margin-bottom: 50px;
}

.content {
    border: 5px solid blue;
    padding: 10px;
    width: 90%;
    height: 400px;
    overflow: scroll;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';

export default {
    data: {
        dataURL: null,
    },
    onShow() {
        let el = this.$refs.canvas1;
        let ctx = el.getContext("2d");
        ctx.strokeRect(100, 100, 300, 300);
    },
    getUrl() {
        let el = this.$refs.canvas1
        let dataUrl = el.toDataURL()
        this.dataURL = dataUrl;
        promptAction.showToast({ duration: 2000, message: "long press,get dataURL" })
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/_cfCEy2cRqK2JU-bh5YGWw/zh-cn_image_0000002569018771.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=85F41CBBB1F3902BDB17311BC3E0EC8C8FC95473E16097C1B7CF0C986A67E4B8)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Fnpn_uguS66zU6OiexwBmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=8A62DE994612A9FD7D812200018755C187658AC56CB28D7ECBFF155823D7BF93)

画布不支持在onInit和onReady中进行创建。
