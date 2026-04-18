---
title: "使用WebSocket访问网络(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-websocket-guidelines"
menu_path:
  - "指南"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "访问网络"
  - "使用WebSocket访问网络(C/C++)"
captured_at: "2026-04-17T01:35:53.417Z"
---

# 使用WebSocket访问网络(C/C++)

#### 场景介绍

通过WebSocket模块可以建立服务器与客户端的双向连接。

#### 接口说明

WebSocket常用接口如下表所示，详细的接口说明请参考[net\_websocket.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h)。

| 接口名 | 描述 |
| :-- | :-- |
| OH\_WebSocketClient\_Constructor(WebSocket\_OnOpenCallback onOpen, WebSocket\_OnMessageCallback onMessage, WebSocket\_OnErrorCallback onError, WebSocket\_OnCloseCallback onclose) | WebSocket客户端的构造函数。 |
| OH\_WebSocketClient\_AddHeader(struct WebSocket \*client, struct WebSocket\_Header header) | 将header头信息添加到client客户端request中。 |
| OH\_WebSocketClient\_Connect(struct WebSocket \*client, const char \*url, struct WebSocket\_RequestOptions options) | 客户端连接服务端。 |
| OH\_WebSocketClient\_Send(struct WebSocket \*client, char \*data, size\_t length) | 客户端向服务端发送数据。 |
| OH\_WebSocketClient\_Close(struct WebSocket \*client, struct WebSocket\_CloseOption options) | 客户端主动关闭websocket连接。 |
| OH\_WebSocketClient\_Destroy(struct WebSocket \*client) | 释放websocket连接上下文和资源。 |

#### WebSocket接口开发示例

#### \[h2\]开发步骤

使用本文档涉及接口创建并连接到WebSocket服务器时，需先创建Native C++工程，在源文件中封装相关接口，然后在ArkTS层调用封装好的接口，使用hilog或console.info等方法将日志打印到控制台或生成设备日志。

本文以建立与WebSocket服务器的连接、向WebSocket服务器发送消息、关闭WebSocket连接为例，提供具体的开发指导。

#### \[h2\]添加开发依赖

**添加动态链接库**

CMakeLists.txt中添加以下lib:

```txt
libace_napi.z.so
libnet_websocket.so
```

**头文件**

```c
#include "napi/native_api.h"
#include "network/netstack/net_websocket.h"
#include "network/netstack/net_websocket_type.h"
```

#### \[h2\]构建工程

1、在源文件中编写调用该API的代码，接受ArkTS传递过来的url字符串参数，创建WebSocket对象指针后，检查连接到服务器是否成功。

#include "napi/native\_api.h"
#include "network/netstack/net\_websocket.h"
#include "network/netstack/net\_websocket\_type.h"
#include "hilog/log.h"

#include <cstring>

#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x3200 // 全局domain宏，标识业务领域
#define LOG\_TAG "WSDEMO"  // 全局tag宏，标识模块日志tag

// WebSocket客户端全局变量
static struct WebSocket \*g\_client = nullptr;

static void onOpen(struct WebSocket \*wsClient, WebSocket\_OpenResult openResult)
{
    (void)wsClient;
    OH\_LOG\_INFO(LOG\_APP, "onOpen: code: %{public}u, reason: %{public}s", openResult.code, openResult.reason);
}

static void onMessage(struct WebSocket \*wsClient, char \*data, uint32\_t length)
{
    (void)wsClient;
    char \*tmp = new char\[length + 1\];
    for (uint32\_t i = 0; i < length; i++) {
        tmp\[i\] = data\[i\];
    }
    tmp\[length\] = '\\0';
    OH\_LOG\_INFO(LOG\_APP, "onMessage: len: %{public}u, data: %{public}s", length, tmp);
}

static void onError(struct WebSocket \*wsClient, WebSocket\_ErrorResult errorResult)
{
    (void)wsClient;
    OH\_LOG\_INFO(LOG\_APP, "onError: code: %{public}u, message: %{public}s", errorResult.errorCode,
                errorResult.errorMessage);
}

static void onClose(struct WebSocket \*wsClient, WebSocket\_CloseResult closeResult)
{
    (void)wsClient;
    OH\_LOG\_INFO(LOG\_APP, "onClose: code: %{public}u, reason: %{public}s", closeResult.code, closeResult.reason);
}

static napi\_value ConnectWebsocket(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_value result;

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    size\_t length = 0;
    napi\_status status = napi\_get\_value\_string\_utf8(env, args\[0\], nullptr, 0, &length);
    if (status != napi\_ok) {
        napi\_get\_boolean(env, false, &result);
        return result;
    }

    if (g\_client != nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "there is already one websocket client running.");
        napi\_get\_boolean(env, false, &result);
        return result;
    }
    char \*buf = new char\[length + 1\];
    std::memset(buf, 0, length + 1);
    napi\_get\_value\_string\_utf8(env, args\[0\], buf, length + 1, &length);
    // 创建WebSocket Client对象指针
    g\_client = OH\_WebSocketClient\_Constructor(onOpen, onMessage, onError, onClose);
    if (g\_client == nullptr) {
        delete\[\] buf;
        napi\_get\_boolean(env, false, &result);
        return result;
    }
    // 连接buf存放的URL对应的WebSocket服务器
    int connectRet = OH\_WebSocketClient\_Connect(g\_client, buf, {});

    delete\[\] buf;
    napi\_get\_boolean(env, connectRet == 0, &result);
    return result;
}

static napi\_value SendMessage(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_value result;

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    size\_t length = 0;
    napi\_status status = napi\_get\_value\_string\_utf8(env, args\[0\], nullptr, 0, &length);
    if (status != napi\_ok) {
        napi\_create\_int32(env, -1, &result);
        return result;
    }

    if (g\_client == nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "websocket client not connected.");
        napi\_create\_int32(env, WebSocket\_ErrCode::WEBSOCKET\_CLIENT\_NULL, &result);
        return result;
    }
    char \*buf = new char\[length + 1\];
    std::memset(buf, 0, length + 1);
    napi\_get\_value\_string\_utf8(env, args\[0\], buf, length + 1, &length);
    // 发送buf中的消息给服务器
    int ret = OH\_WebSocketClient\_Send(g\_client, buf, length);

    delete\[\] buf;
    napi\_create\_int32(env, ret, &result);
    return result;
}

static napi\_value CloseWebsocket(napi\_env env, napi\_callback\_info info)
{
    napi\_value result;
    if (g\_client == nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "websocket client not connected.");
        napi\_create\_int32(env, -1, &result);
        return result;
    }
    // 关闭WebSocket连接
    int ret = OH\_WebSocketClient\_Close(g\_client, {
                                                   .code = 0,
                                                   .reason = "Actively Close",
                                               });
    // 释放WebSocket资源并置空
    OH\_WebSocketClient\_Destroy(g\_client);
    g\_client = nullptr;
    napi\_create\_int32(env, ret, &result);
    return result;
}

ConnectWebsocket函数接收一个WebSocket URL并尝试连接，连接成功返回true，否则返回false。在创建代表WebSocket客户端的WebSocket结构体指针前，需要定义以下回调函数：连接开启时的onOpen回调、接收普通消息的onMessage回调、接收错误消息的onError回调、接收关闭消息的onClose回调。在示例代码中，还调用了[OH\_WebSocketClient\_Send](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h#oh_websocketclient_send)、[OH\_WebSocketClient\_Close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h#oh_websocketclient_close)等函数向服务器发送消息，主动关闭WebSocket连接。

2、将通过napi封装好的napi\_value类型对象初始化导出，通过外部函数接口，将函数暴露给JavaScript使用。示例代码中，ConnectWebsocket函数就会作为外部函数Connect暴露出去；SendMessage函数作为外部函数Send暴露出去；CloseWebsocket函数作为外部函数Close暴露出去。

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"Connect", nullptr, ConnectWebsocket, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"Send", nullptr, SendMessage, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"Close", nullptr, CloseWebsocket, nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

3、将上一步中初始化成功的对象通过RegisterEntryModule函数，使用napi\_module\_register函数将模块注册到 Node.js 中。

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }

4、在工程的index.d.ts文件中定义函数的类型。比如，Connect函数接受一个string参数作为入参，并返回boolean值指示WebSocket连接是否能成功建立。

export const Connect: (url: string) => boolean;
export const Send: (data: string) => number;
export const Close: () => number;

5、在index.ets文件中对上述封装好的接口进行调用。

import testWebsocket from 'libentry.so';

@Entry
@Component
struct Index {
  @State wsUrl: string = '';
  @State content: string = '';
  @State connecting: boolean = false;

  build() {
    Navigation() {
      Column() {
        Column() {
          Text($r('app.string.WebSocket\_address'))
            .fontColor(Color.Gray)
            .textAlign(TextAlign.Start)
            .width('100%')
          TextInput()
            .width('100%')
            .id('textInput\_address')
            .onChange((value) => {
              this.wsUrl = value;
            })
        }
        .margin({
          bottom: 16 // 与底间隔
        })
        .padding({
          left: 16, // 与左间隔
          right: 16 // 与右间隔
        })

        Column() {
          Text($r('app.string.Content'))
            .fontColor(Color.Gray)
            .textAlign(TextAlign.Start)
            .width('100%')
          TextInput()
            .width('100%')
            .id('textInput\_content')
            .enabled(this.connecting)
            .onChange((value) => {
              this.content = value;
            })
        }
        .margin({
          bottom: 16 // 与底间隔
        })
        .padding({
          left: 16, // 与左间隔
          right: 16 // 与右间隔
        })

        Blank()

        Column({
          space: 12 // 占位空间
        }) {
          Button($r('app.string.Connect'))
            .id('Connect')
            .enabled(!this.connecting)
            .onClick(() => {
              let connRet = testWebsocket.Connect(this.wsUrl);
              if (connRet) {
                this.connecting = true;
                // ···
              }
            // ···
            })
          Button($r('app.string.Send'))
            .id('Send')
            .enabled(this.connecting)
            .onClick(() => {
              testWebsocket.Send(this.content);
            // ···
            })
          Button($r('app.string.Close'))
            .id('Close')
            .enabled(this.connecting)
            .onClick(() => {
              let closeResult = testWebsocket.Close();
              if (closeResult != -1) {
                this.connecting = false;
                // ···
              }
            // ···
            })
        }
      }
    }
  }
}

6、配置CMakeLists.txt，本模块需要用到的共享库是libnet\_websocket.so，在工程自动生成的CMakeLists.txt中的target\_link\_libraries中添加此共享库。

注意：如图所示，在add\_library中的entry是工程自动生成的modename，若要做修改，需和步骤3中.nm\_modname保持一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/_NtV6AmoSjOzRVxx9JFvTA/zh-cn_image_0000002538019362.png?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=5939180290CCA5670D43B48D507F6DD847FCF37292727FE4D0A8EDD2151B2D88)

7、调用WebSocket C API接口要求应用拥有ohos.permission.INTERNET权限，在module.json5中的requestPermissions项添加该权限。

经过以上步骤，整个工程的搭建已经完成，接下来就可以连接设备运行工程进行日志查看了。

#### 测试步骤

1、连接设备，使用DevEco Studio打开搭建好的工程。

2、运行工程，设备上会弹出以下图片所示界面：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/bk60-JGQQa6DXZ3w4ILx2A/zh-cn_image_0000002538179292.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=7E8341CBB9B47D40646D7B09080C99B11B71D458143D2DAB15675324B2D94B6D)

简要说明：

-   在第一行的输入框中，输入ws://或wss://开头的WebSocket URL。
    
-   在输入完WebSocket URL，点击Connect按钮后，如果访问成功，会触发onOpen的回调，打印日志。
    
-   在Content输入框里输入要发送给服务器的内容，点击Send按钮发送。如果服务器返回消息，会触发onMessage回调，打印日志。
    
-   点击Close按钮，WebSocket连接释放，可以重新输入新的WebSocket URL。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Y2Si0tjbSiiUfdguc7ngLA/zh-cn_image_0000002569019079.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=602095CEA71AE0BF30826B6B8CF783F0C21501F16CBFBBAC3F4CCBE3A2BCCF2B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/50KyH1JkTGm9IkAWB_1GEQ/zh-cn_image_0000002568899069.png?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=CD279B97C4E4809286B77493BBE2F1AD3747A8D22D8FAB5BB2E82C598B57FEEB)
