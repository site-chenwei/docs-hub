---
title: "应用静态快捷方式如何接入X键"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-71"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序包结构"
  - "应用静态快捷方式如何接入X键"
captured_at: "2026-04-17T02:02:58.614Z"
---

# 应用静态快捷方式如何接入X键

**现有机制：**

X键当前已经支持将应用的静态快捷方式，添加至X键的九宫格面板，后续用户可以通过单击X键呼出九宫格面板后，点击已添加进来的静态快捷方式图标，快速启动，一键直达。注：当前X键九宫格面板对所有应用开放静态快捷方式，X键双击/长按列表中只对部分应用开放静态快捷方式。

**适用场景：**

应用的功能入口深，操作步骤复杂。

**实现方案：**

应用的静态快捷方式可以接入X键的前提是，应用需要创建自己的静态快捷方式，创建出来的静态快捷方式，在桌面长按应用图标，图标上方会显示静态快捷方式（注：桌面上最多显示4个静态快捷方式），另外X键编辑界面中也会显示（注：X键编辑界面暂不限制应用静态快捷方式的显示数量），并且可以点击快捷方式后面的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/uAuYf0OMSAGyFQXwsNWSRQ/zh-cn_image_0000002537542426.png?HW-CC-KV=V1&HW-CC-Date=20260417T020300Z&HW-CC-Expire=86400&HW-CC-Sign=7DA8FB5B2223ABE76988A2C7F70A1881DDF80A787EF7621D727DDA896CC40801)图标添加至X键九宫格面板，具体效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/0IB6X0odS5m1j_5CVLuvhA/zh-cn_image_0000002568302199.png?HW-CC-KV=V1&HW-CC-Date=20260417T020300Z&HW-CC-Expire=86400&HW-CC-Sign=7596597A6F36FC83C4F19CD610F89DD2FA79DFFA596B30010FBE8064C7C63D1D)

**参考链接：**

[创建应用静态快捷方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typical-scenario-configuration)
