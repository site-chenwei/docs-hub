---
title: "select"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-select"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "基础组件"
  - "select"
captured_at: "2026-04-17T01:48:01.761Z"
---

# select

下拉选择按钮，可使用下拉菜单展示并选择内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/HaJtv6M7RGeR1XxzSUoUYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=0FF6387A9D288E541DBA83A7C4433F9555856754908B5175641F4FC3F38BCA32)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

支持<[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-option)\>。

#### 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。

#### 样式

除支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)外，还支持如下样式：

| 名称 | 类型 | 必填 | 描述 |
| :-- | :-- | :-- | :-- |
| font-family | string | 否 | 
字体样式列表，用逗号分隔。列表中第一个系统中存在的字体样式或者通过[自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-customizing-font)指定的字体样式，会被选中作为当前文本的字体样式。

默认值：sans-serif

 |

#### 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| :-- | :-- | :-- |
| change | {newValue: newValue} | 选择下拉选项后触发该事件，返回值为一个对象，其中newValue为选中项option的value值。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Dabab8QKQaCQCCyYYeiDRQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=CB4A2ACF4CF5A9CC3861A33A6A3300E89E6926552B27BB411803091206592DE7)

select组件不支持click事件。

#### 方法

支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)。

#### 示例

```html
<!-- xxx.hml -->
<div class="container">
    <select>
        <option for="{{ array }}" value="{{ $item.value }}">
            {{ $item.name }}
        </option>
    </select>
</div>
```

```css
/* xxx.css */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
```

```js
// xxx.js
export default {
    data: {
        array: [
            {
                "value": "下拉选项0", "name": "选项0"
            },
            {
                "value": "下拉选项1", "name": "选项1"
            },
            {
                "value": "下拉选项2", "name": "选项2"
            },
            {
                "value": "下拉选项3", "name": "选项3"
            },
        ]
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/gD2m91-MT1OcgGxKJwNaxA/zh-cn_image_0000002568900853.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=C8F3657E38726AF8B602DDC93942CF4B5CDA3755305F9114A14ED940C554CA72)
