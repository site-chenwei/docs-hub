---
title: "toolbar"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toolbar"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "基础组件"
  - "toolbar"
captured_at: "2026-04-17T01:48:05.069Z"
---

# toolbar

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/lXgcSmbCTKO9_8UhvROP6g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=E8DFA0F9BD90F5117232023DDD3A755DC22890DADC3ED59D11DC21D5D1BE82BE)

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

工具栏。放在界面底部，用于展示针对当前界面的操作选项。

#### 权限列表

无

#### 子组件

支持<toolbar-item>子组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/nkesfYU2SQy_ruU2Mi6jZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=44CF49DF42A0D19BA20F8BDCFCDBBEF0C265D498F470BAB5A99C006FCF17754B)

工具栏最多可以展示5个toolbar-item子组件，如果存在6个及以上toolbar-item子组件，则保留前面4个子组件，后续的子组件收纳到工具栏上的更多项中，通过点击更多项弹窗展示剩下的子组件，更多项展示的组件样式采用系统默认样式，toolbar-item上设置的自定义样式不生效。

#### 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。

#### 样式

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/qcbkFHBsTtauHYneikCK9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014804Z&HW-CC-Expire=86400&HW-CC-Sign=65C0E17E73E260B74C16519B155E8BEF09278DD422F229320CA7D3BEF1490286)

不支持height样式，高度固定为56px。

#### 事件

不支持。

#### 方法

不支持。

#### 示例

详见[toolbar-item示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toolbar-item)。
