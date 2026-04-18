---
title: "stack"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stack"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "容器组件"
  - "stack"
captured_at: "2026-04-17T01:48:00.708Z"
---

# stack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/ZIignbvBTueWZl84KFg_iw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014803Z&HW-CC-Expire=86400&HW-CC-Sign=8ADC642B9EC72D07DD3A330E30D691027B43C0285700D2D7E52346B9A33D11E1)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

#### 权限列表

无

#### 子组件

支持。

#### 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。

#### 样式

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。

#### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)。

#### 方法

支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)。

#### 示例

```html
<!-- xxx.hml -->
<stack class="stack-parent">
  <div class="back-child bd-radius"></div>
  <div class="positioned-child bd-radius"></div>
  <div class="front-child bd-radius"></div>
</stack>
```

```css
/* xxx.css */
.stack-parent {
  width: 400px;
  height: 400px;
  background-color: #ffffff;
  border-width: 1px;
  border-style: solid;
}
.back-child {
  width: 300px;
  height: 300px;
  background-color: #3f56ea;
}
.front-child {
  width: 100px;
  height: 100px;
  background-color: #00bfc9;
}
.positioned-child {
  width: 100px;
  height: 100px;
  left: 50px;
  top: 50px;
  background-color: #47cc47;
}
.bd-radius {
  border-radius: 16px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/421-eHIkTFOTwfqD12xiFg/zh-cn_image_0000002538181062.png?HW-CC-KV=V1&HW-CC-Date=20260417T014803Z&HW-CC-Expire=86400&HW-CC-Sign=84AF6C990A430BBAE3FDDD45CF4809509C822BA0243D0DD91812AFAB2466F57F)
