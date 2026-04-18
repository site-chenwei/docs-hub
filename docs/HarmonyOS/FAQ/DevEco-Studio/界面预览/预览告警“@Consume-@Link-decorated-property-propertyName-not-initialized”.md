---
title: "预览告警“@Consume/@Link decorated property <propertyName> not initialized”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-3"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "界面预览"
  - "预览告警“@Consume/@Link decorated property <propertyName> not initialized”"
captured_at: "2026-04-17T02:03:20.935Z"
---

# 预览告警“@Consume/@Link decorated property <propertyName> not initialized”

**问题现象**

启动预览后，预览窗口显示白屏，上方出现错误信息：“Preview failed. View details in the PreviewerLog window.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/c9xJjak1SgKNNJlkRhAemA/zh-cn_image_0000002194317968.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=C61E89F84E914D825C8965D27B8E299FB41F13EF9489D8E9ACB58F484F5A062D "点击放大")

此时，PreviewerLog 窗口显示如下告警信息：“@Consume/@Link 装饰的属性 \_<propertyName>\_未初始化。”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/2Nl3vQoJQo2u6xdqJmOCUw/zh-cn_image_0000002194158348.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=95F4E24CFF89C261DCD38A3AA72CE7D86FA4855D43312A8EC63F0845AB7A9964)

**解决措施**

由于@Consume/@Link装饰的成员需要与父组件建立绑定关系，单独预览时无法完成初始化，因此如果预览包含@Consume（或@Link）装饰的成员的页面或组件，就可能会出现空白屏幕。

建议不要直接预览含有@Consume或@Link装饰的子组件，而应通过预览父组件来查看子组件的预览效果。

示例代码：

// Suggest adding @ Preview on ParentComp to preview the preview effect of ChildComp
@Preview
@Component
struct ParentComp {
  // @Provide decoration is provided by the entrance component ParentComp as its descendant component
  @Provide reviewVotes: number = 10;

  build() {
    Column() {
      Button(\`reviewVotes(${this.reviewVotes}), give +1\`)
        .onClick(() => this.reviewVotes += 1)
      ChildComp()
    }
  }
}

// @Preview is not recommended to directly preview ChildComp
@Component
struct ChildComp {
  // The variable decorated with '@Consume' is bound to the variable decorated with '@Provide' in its ancestor component ParentComp using the same attribute name
  @Consume reviewVotes: number;
  build() {
    Column() {
      Text(\`reviewVotes(${this.reviewVotes})\`)
      Button(\`reviewVotes(${this.reviewVotes}), give +1\`)
        .onClick(() => this.reviewVotes += 1)
    }
    .width('50%')
  }
}
