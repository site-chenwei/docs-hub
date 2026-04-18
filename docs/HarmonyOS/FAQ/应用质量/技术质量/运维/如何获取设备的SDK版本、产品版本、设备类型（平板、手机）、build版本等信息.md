---
title: "如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-23"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息"
captured_at: "2026-04-17T02:02:57.336Z"
---

# 如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息

应用所在设备的信息，可以通过@kit.BasicServicesKit的deviceInfo模块获取：

-   SDK版本：deviceInfo.sdkApiVersion。
-   产品版本：deviceInfo.displayVersion。
-   设备类型（平板、手机）：deviceInfo.deviceType。
-   build版本：deviceInfo.buildVersion。

更多请参见[@ohos.deviceInfo (设备信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info)。
