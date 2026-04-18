---
title: "rcp请求是否有数据大小限制"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-2"
menu_path:
  - "FAQ"
  - "系统开发"
  - "网络"
  - "远场通信（Remote Communication）"
  - "rcp请求是否有数据大小限制"
captured_at: "2026-04-17T02:03:17.803Z"
---

# rcp请求是否有数据大小限制

rcp请求默认情况下，[response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#section156381815599)响应中最大数据量为50MB，超过此限制建议通过[HttpEventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#section87603011401)的[onDataReceive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#section9264115918536)实现流式数据接收。

**参考链接**

[response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#section156381815599)

[HttpEventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#section87603011401)

[onDataReceive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#section9264115918536)
