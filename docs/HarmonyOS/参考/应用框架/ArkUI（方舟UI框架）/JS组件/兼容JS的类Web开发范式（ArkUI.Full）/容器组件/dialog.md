---
title: "dialog"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-dialog"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "容器组件"
  - "dialog"
captured_at: "2026-04-17T01:48:00.591Z"
---

# dialog

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/gSHy2LOLSsyALvYoM9Pm9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014803Z&HW-CC-Expire=86400&HW-CC-Sign=9B628A500067F794992F2172D9233C63FA74C4DC258ABC4F3CE0C867D5C1150B)

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

自定义弹窗容器。

#### 权限列表

无

#### 子组件

支持单个子组件。

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| dragable7+ | boolean | false | 否 | 设置对话框是否支持拖拽。true表示支持拖拽，false表示不支持拖拽。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/9b5NmFbxR5mMWW4025F5VQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014803Z&HW-CC-Expire=86400&HW-CC-Sign=712AC540BA58BB56F7ECDDDD08E55C88CB1D94F69B86E0EBC2038BD1A4E74206)

弹窗类组件不支持focusable、click-effect属性。

#### 样式

仅支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)中的width、height、margin、margin-\[left | top | right | bottom\]、margin-\[start | end\]样式。

#### 事件

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)，仅支持如下事件：

| 名称 | 参数 | 描述 |
| :-- | :-- | :-- |
| cancel | \- | 用户点击非dialog区域触发取消弹窗时触发的事件。 |
| show7+ | \- | 对话框弹出时触发该事件。 |
| close7+ | \- | 对话框关闭时触发该事件。 |

#### 方法

不支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)，仅支持如下方法。

| 名称 | 参数 | 描述 |
| :-- | :-- | :-- |
| show | \- | 弹出对话框。 |
| close | \- | 关闭对话框。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/beKfvwfBQFevVdqSRg8G4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014803Z&HW-CC-Expire=86400&HW-CC-Sign=8CB5DAB582E67F58F8AAE718BAD4277EDEF9BB7AE498FF97B182D84733C0E995)

dialog属性、样式均不支持动态更新。

#### 示例

```html
<!-- xxx.hml -->
<div class="doc-page">
  <div class="btn-div">
    <button type="capsule" value="Click here" class="btn" onclick="showDialog"></button>
  </div>
  <dialog id="simpledialog" dragable="true" class="dialog-main" oncancel="cancelDialog">
    <div class="dialog-div">
      <div class="inner-txt">
        <text class="txt" ondoubleclick="doubleclick">Simple dialog</text>
      </div>
      <div class="inner-btn">
        <button type="capsule" value="Cancel" onclick="cancelSchedule" class="btn-txt"></button>
        <button type="capsule" value="Confirm" onclick="setSchedule" class="btn-txt"></button>
      </div>
    </div>
  </dialog>
</div>
```

```css
/* xxx.css */
.doc-page {
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.btn-div {
  width: 100%;
  height: 200px;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.btn {
  background-color: #F2F2F2;
  text-color: #0D81F2;
}
.txt {
  color: #000000;
  font-weight: bold;
  font-size: 39px;
}
.dialog-main {
  width: 500px;
}
.dialog-div {
  flex-direction: column;
  align-items: center;
}
.inner-txt {
  width: 400px;
  height: 160px;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}
.inner-btn {
  width: 400px;
  height: 120px;
  justify-content: space-around;
  align-items: center;
}
.btn-txt {
  background-color: #F2F2F2;
  text-color: #0D81F2;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  showDialog() {
    this.$element('simpledialog').show()
  },
  cancelDialog() {
    promptAction.showToast({
      message: 'Dialog cancelled'
    })
  },
  cancelSchedule() {
    this.$element('simpledialog').close()
    promptAction.showToast({
      message: 'Successfully cancelled'
    })
  },
  setSchedule() {
    this.$element('simpledialog').close()
    promptAction.showToast({
      message: 'Successfully confirmed'
    })
  },
  doubleclick(){
    promptAction.showToast({
      message: 'doubleclick'
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/0MwkULE7SPSs2JVrjWXE8Q/zh-cn_image_0000002538021130.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014803Z&HW-CC-Expire=86400&HW-CC-Sign=ADAFDD5F6D66E7D34824D038F300F0BB222F39C5B6119FBBB251B4952F39834B)
