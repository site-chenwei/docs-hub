---
title: "设备连接Wi"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-4"
menu_path:
  - "FAQ"
  - "系统开发"
  - "网络"
  - "短距通信（Connectivity）"
  - "设备连接Wi-Fi后，如何获取当前设备的IP地址"
captured_at: "2026-04-17T02:03:17.893Z"
---

# 设备连接Wi-Fi后，如何获取当前设备的IP地址

使用wifiManager模块获取ipInfo，然后转换为IP常用格式，注意wifiManager.getIpInfo()接口需要权限ohos.permission.GET\_WIFI\_INFO。

参考代码如下：

import { wifiManager } from '@kit.ConnectivityKit';

let ipAddress = wifiManager.getIpInfo().ipAddress;
let ip = (ipAddress >>> 24) + "." + (ipAddress >> 16 & 0xFF) + "." + (ipAddress >> 8 & 0xFF) + "." + (ipAddress & 0xFF);
