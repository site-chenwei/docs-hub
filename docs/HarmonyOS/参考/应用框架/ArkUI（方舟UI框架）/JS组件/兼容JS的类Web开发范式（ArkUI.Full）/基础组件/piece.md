---
title: "piece"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-piece"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "基础组件"
  - "piece"
captured_at: "2026-04-17T01:48:01.338Z"
---

# piece

一种块状的入口，可包含图片和文本，常用于展示收件人。例如，邮件收件人或信息收件人。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/b5ivA05QR3axRdF7dqJb_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=BFDAA54DB6E77C6BF1F4001D4245243C01E2F66E070982BDB54415BE3B26E70B)

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，还支持如下属性：

| 名称 | 类型 | 必填 | 描述 |
| :-- | :-- | :-- | :-- |
| content | string | 是 | 操作块文本内容。 |
| closable | boolean | 否 | 
设置当前操作块是否显示删除图标，当显示删除图标时，点击删除图标会触发close事件。

true表示显示删除图标，false表示不显示删除图标。默认为false。

 |
| icon | string | 否 | 操作块删除图标的url，支持本地路径。 |

#### 样式

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/kYkCxI3rQueawz71RkNXSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=0BBA8E417D4FFA4A10E899FCFF45D7632BCC6E05944627E2F282BC3C27609E24)

文本和图片默认在整个piece组件中居中。

#### 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| :-- | :-- | :-- |
| close | \- | 当piece组件点击删除图标触发，此时可以通过渲染属性if删除该组件。 |

#### 方法

支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)。

#### 示例

```html
<!-- xxx.hml-->
<div class="container" >
  <piece if="{{first}}" content="example"></piece>
  <piece if="{{second}}" content="example" closable="true" onclose="closeSecond"></piece>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
}
```

```js
// xxx.js
export default {
  data: {
    first: true,
    second: true
  },
  closeSecond(e) {
    this.second = false;
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/-SuwcC4URx6jlAi-WQpoyA/zh-cn_image_0000002569020861.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=495DF03D25FF0728435860678BD2C69859706DEAD2940C9E4ED1D0105F76760F)
