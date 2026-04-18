---
title: "UIViewer获取页面时，无法展示页面截图和元素树如何处理"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-uiviewer-2"
menu_path:
  - "FAQ"
  - "DevEco Testing"
  - "实用工具"
  - "UIViewer"
  - "UIViewer获取页面时，无法展示页面截图和元素树如何处理"
captured_at: "2026-04-17T02:03:27.000Z"
---

# UIViewer获取页面时，无法展示页面截图和元素树如何处理

请排查设备UiTest框架是否正常，打开cmd窗口，在设备上运行 hdc shell uitest dumpLayout 和 hdc shell snapshot\_display -f /data/local/tmp/screenCasting.jpeg 两条指令，确认下是否能运行成功，成功运行截图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/i6yJf-QGR3627GDisHFeuw/zh-cn_image_0000002194318600.png?HW-CC-KV=V1&HW-CC-Date=20260417T020327Z&HW-CC-Expire=86400&HW-CC-Sign=23F7F6A98B389F90837F3A1675047CB40C4EEC8C2F96636B48FBBA6C89A303E6 "点击放大")

如运行失败，请前往DevEco Testing客户端-设置-问题反馈，或通过[华为开发者联盟-在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)，提交该场景信息（测试服务名称+异常任务信息+问题描述+问题截图），以便于研发团队进一步分析。

注意：客户端提交反馈需打开日志上传开关，华为开发者联盟提单请附上工具日志。

Windows日志路径：C:\\Users\\用户名\\AppData\\Local\\DevEco Testing\\common\\modules\\launcher\\logs

Mac日志路径：/Users/用户名/Library/Application Support/DevEco Testing/common/modules/launcher/logs
