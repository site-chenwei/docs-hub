---
title: "在室内时，在持续定位场景中设置interval为1，为何不生效"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-kit-3"
menu_path:
  - "FAQ"
  - "应用服务开发"
  - "位置服务（Location Kit）"
  - "在室内时，在持续定位场景中设置interval为1，为何不生效"
captured_at: "2026-04-17T02:03:20.075Z"
---

# 在室内时，在持续定位场景中设置interval为1，为何不生效

在室内由于没有GNSS信号，返回的是网络位置。WLAN扫描功耗较大，系统限制每20秒扫描一次。因此，即使将interval设置为1，在室内也只能每20秒获取一次位置。
