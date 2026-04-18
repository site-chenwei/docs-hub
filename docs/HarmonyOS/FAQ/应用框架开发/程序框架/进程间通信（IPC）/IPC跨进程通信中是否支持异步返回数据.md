---
title: "IPC跨进程通信中是否支持异步返回数据"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ipc-1"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "进程间通信（IPC）"
  - "IPC跨进程通信中是否支持异步返回数据"
captured_at: "2026-04-17T02:02:59.656Z"
---

# IPC跨进程通信中是否支持异步返回数据

支持将服务端的onRemoteMessageRequest函数使用async设置为异步。具体可以参考：API参考[onRemoteMessageRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc#onremotemessagerequest9)中的“重载onRemoteMessageRequest方法异步处理请求示例”。

参考代码如下：

import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): Promise<boolean> {
    if (code === 1) {
      console.log("RpcServer: async onRemoteMessageRequest is called");
    } else {
      console.log("RpcServer: unknown code: " + code);
      return false;
    }
    await new Promise((resolve: (data: rpc.RequestResult) => void) => {
      setTimeout(resolve, 100);
    })
    return true;
  }
}

**参考链接**

[IPC与RPC通信开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ipc-rpc-development-guideline)
