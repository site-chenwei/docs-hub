---
title: "出现“container is not running”错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用测试"
  - "出现“container is not running”错误"
captured_at: "2026-04-17T02:03:25.238Z"
---

# 出现“container is not running”错误

**问题现象**

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/PeRD_jNhQXOr93y69eIcng/zh-cn_image_0000002194318268.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=858A417E82F819C7AB5A47F3F1C6022D1BC60F94252F6CB1ADEF68A02811E8FD)

**解决措施**

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/9WHdGRZhR9idRuEu4EdkGQ/zh-cn_image_0000002194158644.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=F19CE64D5D4292C21809109193ECEECC80A8C78976C6E127B7F98B5C96678EEE)
