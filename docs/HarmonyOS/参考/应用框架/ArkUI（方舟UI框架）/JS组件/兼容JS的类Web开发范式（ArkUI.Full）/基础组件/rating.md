---
title: "rating"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-rating"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "基础组件"
  - "rating"
captured_at: "2026-04-17T01:48:01.647Z"
---

# rating

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/z50ZktfkT1SyFXSDuUEGiw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=F5828623FE900D97DE153875BC686DFD5B8973C9BEF22F0965A490F2C57F8008)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

评分条，表示用户使用感受的衡量标准条。

#### 权限列表

无

#### 子组件

不支持。

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| numstars | number | 5 | 否 | 设置评分条的星级总数。 |
| rating | number | 0 | 否 | 设置评分条当前评星数。 |
| stepsize | number | 0.5 | 否 | 设置评分条的评星步长。 |
| indicator | boolean | false | 否 | 
设置评分条是否为指示器。

true：作为指示器，用户不可操作。

false：非指示器，用户可操作。

 |

#### 样式

除支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| star-background | string | \- | 否 | 设置单个星级未选中的背景图片，只支持本地路径图片，图片格式为png和jpg。 |
| star-foreground | string | \- | 否 | 设置单个星级选中的前景图片，只支持本地路径图片，图片格式为png和jpg。 |
| star-secondary | string | \- | 否 | 设置单个星级部分选中的次级背景图片，该图片会覆盖背景图片，只支持本地路径图片，图片格式为png和jpg。 |
| width | <length>|<percentage> | 
120px

60px（不可操作）

 | 否 | 默认值是在未设置自定义资源和评分星数时，使用5个星和默认资源下的宽度值。 |
| height | <length>|<percentage> | 

24px

12px（不可操作）

 | 否 | 默认值是在未设置自定义资源和评分星数时，使用5个星和默认资源下的高度值。 |
| rtl-flip | boolean | true | 否 | 

在rtl文字方向下是否自动翻转图源。

true：在rtl文字方向下自动翻转图源。

false：在rtl文字方向下不自动翻转图源。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/PACLb6ShRTivv4hVE2vsAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=383EA829B2E42ED6E8BF9100CD4B0F9DA8A86237701967BEEE0C86CAC8AF8026)

star-background，star-secondary，star-foreground三个星级图源必须全部设置，否则默认的星级颜色为灰色，以此提示图源设置错误。

#### 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| :-- | :-- | :-- |
| change | { rating: number } | 评分条的评星发生改变时触发该回调。 |

#### 方法

支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)。

#### 示例

```html
<!-- xxx.hml -->
<div class="container">
  <rating numstars="5" rating="5" @change="changeRating" id="rating">
  </rating>
</div>
```

```css
/* xxx.css */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.rating {
  width: 200px;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
    changeRating(e){
        promptAction.showToast({
            message: e.rating
        });
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/NL3G64dfQ3SX-yEu_DfOzA/zh-cn_image_0000002538181076.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=18F2C57E708FD0BA54EA01BB94DA90A979A40ECE4DB7528F531C8BAC05CC91CF)
