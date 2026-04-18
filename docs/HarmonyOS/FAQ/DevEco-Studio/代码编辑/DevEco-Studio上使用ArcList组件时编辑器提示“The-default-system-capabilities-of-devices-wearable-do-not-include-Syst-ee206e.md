---
title: "DevEco Studio上使用ArcList组件时编辑器提示“The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-18"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "代码编辑"
  - "DevEco Studio上使用ArcList组件时编辑器提示“The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle”"
captured_at: "2026-04-17T02:03:20.856Z"
---

# DevEco Studio上使用ArcList组件时编辑器提示“The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle”

**问题现象**

使用ArcList组件时，编辑器报错，错误信息如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/CWP21C7nTFGiHgL8TnZX7g/zh-cn_image_0000002459313966.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=BDD4C0CBAE88ED57A1BBF927DCDEC50753704FDC30393AC1EBC0770A302042CE)

**解决措施**

1.  请前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至6.0.1 Release及以上版本。
2.  若仍需使用当前版本，可在src/main目录下添加syscap.json配置文件。可参考[SysCap开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap#syscap开发指导)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/BQ3wbR75TWWpLZSih29X8w/zh-cn_image_0000002460277990.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=6A8F4833AA3CE02968FF636EE8637C45937BA8C8689B9CB7ED2507843DAC0985)
