---
title: "三方应用如何获取蓝牙MAC地址"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-1"
menu_path:
  - "FAQ"
  - "系统开发"
  - "网络"
  - "短距通信（Connectivity）"
  - "三方应用如何获取蓝牙MAC地址"
captured_at: "2026-04-17T02:03:17.816Z"
---

# 三方应用如何获取蓝牙MAC地址

调用connection.startBluetoothDiscovery()接口，使用蓝牙扫描功能，在扫描结果中即可获取蓝牙MAC地址。需要权限：ohos.permission.ACCESS\_BLUETOOTH。参考代码如下：

import { connection } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onReceiveEvent(data: Array<string>) { // data is a collection of Bluetooth device addresses
  console.info('bluetooth device find = '+ JSON.stringify(data));
}

try {
  connection.on('bluetoothDeviceFind', onReceiveEvent);
  connection.startBluetoothDiscovery();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

**参考链接**

[发现蓝牙设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiononbluetoothdevicefind)
