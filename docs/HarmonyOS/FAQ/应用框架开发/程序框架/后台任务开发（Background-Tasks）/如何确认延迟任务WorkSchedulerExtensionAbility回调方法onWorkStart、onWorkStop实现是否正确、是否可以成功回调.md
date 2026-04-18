---
title: "如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-8"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "后台任务开发（Background Tasks）"
  - "如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调"
captured_at: "2026-04-17T02:02:59.644Z"
---

# 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调

延迟任务申请成功之后，需要等到条件满足后才可以执行延迟任务回调，为了快速验证延迟任务回调功能是否正确，可以通过以下hidumper命令手动触发延迟任务执行回调。

```powershell
hdc shell hidumper -s 1904 -a '-t com.hmos.workschedulerdemo MyWorkSchedulerExtensionAbility'
```

com.hmos.workschedulerdemo、MyWorkSchedulerExtensionAbility需要替换为需要查询应用的bundleName和abilityName。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/mi9ZfNwlTtKljg-0hlXYrw/zh-cn_image_0000002194317960.png?HW-CC-KV=V1&HW-CC-Date=20260417T020301Z&HW-CC-Expire=86400&HW-CC-Sign=941218F2EC33ADA594A223C7E7198D258B2F82BE7BC621DAA63249741294ACF1 "点击放大")
