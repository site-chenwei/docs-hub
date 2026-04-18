---
title: "xcomponent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-xcomponent"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "基础组件"
  - "xcomponent"
captured_at: "2026-04-17T01:48:05.086Z"
---

# xcomponent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/EnSv9q4_TkSHI_7ifARtMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=E5081D8F33879E46DA7A477C995C139AE27F2888FFFB3F0AC592D669392E3785)

该组件从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

用于显示写入了EGL/OpenGLES或媒体数据的组件。

#### 权限列表

无

#### 子组件

不支持。

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，还支持如下属性：

| 名称 | 参数类型 | 必填 | 描述 |
| :-- | :-- | :-- | :-- |
| id | string | 是 | 组件的唯一标识，支持最大的字符串长度128。 |
| type | string | 是 | 
用于指定xcomponent组件类型，可选值为：

\- surface：组件内容单独送显，直接合成到屏幕。

\- component：组件内容与其他组件合成后统一送显。

 |
| libraryname | string | 否 | 应用Native层编译输出动态库名称。 |

#### 样式

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。

#### 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：

| 名称 | 功能描述 |
| :-- | :-- |
| onLoad(context?: object) => void | 
插件加载完成时回调事件。

context：开发者扩展的xcomponent方法的实例对象，context对象的接口由开发者自定义。

 |
| onDestroy() => void | 插件卸载完成时回调事件。 |

#### 方法

除支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)外，还支持如下方法：

| 名称 | 参数 | 返回值类型 | 描述 |
| :-- | :-- | :-- | :-- |
| getXComponentSurfaceId | \- | string | 获取xcomponent对应Surface的ID，供@ohos接口使用，比如camera相关接口。 |
| setXComponentSurfaceSize | 
{

surfaceWidth: number,

surfaceHeight: number

}

 | \- | 设置xcomponent持有Surface的宽度和高度。 |
| getXComponentContext | \- | object | 获取开发者扩展的xcomponent方法的实例对象。 |

#### 示例

提供surface类型xcomponent，支持相机预览等能力。

```html
<!-- xxx.hml -->
<div style="height: 500px; width: 500px; flex-direction: column; justify-content: center; align-items: center;">
    <text id = 'camera' class = 'title'>camera_display</text>
    <xcomponent id = 'xcomponent' type = 'surface' onload = 'onload' ondestroy = 'ondestroy'></xcomponent>
</div>
```

```js
// xxx.js
import camera from '@ohos.multimedia.camera';
export default {
    onload() {
        var surfaceId = this.$element('xcomponent').getXComponentSurfaceId();
        camera.createPreviewOutput(surfaceId).then((previewOutput) => {
            console.info('Promise returned with the PreviewOutput instance');
        })
    }
}
```
