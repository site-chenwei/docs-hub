---
title: "签名时，提示“Failed to query agreement signing records”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-11"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "签名服务"
  - "签名时，提示“Failed to query agreement signing records”"
captured_at: "2026-04-17T02:03:23.684Z"
---

# 签名时，提示“Failed to query agreement signing records”

**问题现象**

使用未实名认证的华为账号登录会导致签名错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/16PYQ4xxQhahQjMPWONR6A/zh-cn_image_0000002194318468.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=BA52F85AD9E59E56D156A3BF6E3C93087131EE847BDF678018E83A4929F63F27)

**解决措施**

出现该问题的原因是签名过程中，DevEco Studio与查询协议的连接通道发生异常

请尝试以下两种方法解决此问题

方式一：该问题可能是由于DevEco Studio的HTTP代理问题引起的，请参考[配置代理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-config)。

方式二：进行开发者实名认证，具体指导可以参考[实名认证介绍](https://developer.huawei.com/consumer/cn/doc/start/itrna-0000001076878172)。
