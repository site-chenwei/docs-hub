---
title: "stack"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "JS服务卡片UI组件"
  - "容器组件"
  - "stack"
captured_at: "2026-04-17T01:48:07.020Z"
---

# stack

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/4zNHUoXESHiKkrR9qvGCrw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=1321E62139DF90ED9F05AACD3A9A451334AAB9B7C1D751A4F7C28743C512A8CC)

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

支持。

#### 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-attributes)。

#### 样式

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-styles)。

#### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-events)。

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
  margin: 50px;
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

**4×4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ElEMcWE6T7W99OfkFdernQ/zh-cn_image_0000002538021378.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=EE971AA12976626293316356B0012B2ADAB3F60D821C9AF4A26C8AF8E89348CF)
