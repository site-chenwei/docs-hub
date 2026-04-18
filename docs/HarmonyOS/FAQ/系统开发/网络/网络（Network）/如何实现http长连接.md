---
title: "如何实现http长连接"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-48"
menu_path:
  - "FAQ"
  - "系统开发"
  - "网络"
  - "网络（Network）"
  - "如何实现http长连接"
captured_at: "2026-04-17T02:03:17.445Z"
---

# 如何实现http长连接

可使用定时HTTP请求模拟长连接。参考代码如下：

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
// 设置5秒轮询一次
setTimeout(() => {
  httpRequest.request("EXAMPLE\_URL", {
    method: http.RequestMethod.GET,
    connectTimeout: 60000,
    readTimeout: 60000
  }, (err, data) => {
    if (!err) {
      console.info('Received data:', JSON.stringify(data.result));
    } else {
      console.info('Polling error:', JSON.stringify(err));
    }
  })
}, 5000)
