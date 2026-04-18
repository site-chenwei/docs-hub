---
title: "管理网络连接(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-netmanager-guidelines"
menu_path:
  - "指南"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "连接网络"
  - "管理网络连接(C/C++)"
captured_at: "2026-04-17T01:35:53.526Z"
---

# 管理网络连接(C/C++)

#### 场景介绍

NetConnection模块提供了常用网络信息查询的能力。

#### 接口说明

NetConnection常用接口如下表所示，详细的接口说明请参考[net\_connection.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-h)。

| 接口名 | 描述 |
| :-- | :-- |
| OH\_NetConn\_HasDefaultNet(int32\_t \*hasDefaultNet) | 检查默认数据网络是否被激活，判断设备是否有网络连接，以便在应用程序中采取相应的措施。 |
| OH\_NetConn\_GetDefaultNet(NetConn\_NetHandle \*netHandle) | 获得默认激活的数据网络。 |
| OH\_NetConn\_IsDefaultNetMetered(int32\_t \*isMetered) | 检查当前网络上的数据流量使用是否被计量。 |
| OH\_NetConn\_GetConnectionProperties(NetConn\_NetHandle \*netHandle, NetConn\_ConnectionProperties \*prop) | 获取netHandle对应的网络的连接信息。 |
| OH\_NetConn\_GetNetCapabilities (NetConn\_NetHandle \*netHandle, NetConn\_NetCapabilities \*netCapacities) | 获取netHandle对应的网络的能力信息。 |
| OH\_NetConn\_GetDefaultHttpProxy (NetConn\_HttpProxy \*httpProxy) | 获取网络默认的代理配置信息。 如果设置了全局代理，则会返回全局代理配置信息。如果进程已经绑定到指定netHandle对应的网络，则返回网络句柄对应网络的代理配置信息。在其他情况下，将返回默认网络的代理配置信息。 |
| OH\_NetConn\_GetAddrInfo (char \*host, char \*serv, struct addrinfo \*hint, struct addrinfo \*\*res, int32\_t netId) | 通过netId获取DNS结果。 |
| OH\_NetConn\_FreeDnsResult(struct addrinfo \*res) | 释放DNS结果内存。 |
| OH\_NetConn\_GetAllNets(NetConn\_NetHandleList \*netHandleList) | 获取所有处于连接状态的网络列表。 |
| OHOS\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver) | 
注册自定义DNS解析器。

**弃用：** 从API version 13开始废弃。

**替代：** 推荐使用OH\_NetConn\_RegisterDnsResolver。

 |
| OHOS\_NetConn\_UnregisterDnsResolver(void) | 

取消注册自定义DNS解析器。

**弃用：** 从API version 13开始废弃。

**替代：** 推荐使用OH\_NetConn\_UnregisterDnsResolver。

 |
| OH\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver) | 注册自定义DNS解析器。 |
| OH\_NetConn\_UnregisterDnsResolver(void) | 取消注册自定义DNS解析器。 |
| OH\_NetConn\_SetPacUrl(const char \*pacUrl) | 设置系统级代理自动配置(PAC)脚本地址。 |
| OH\_NetConn\_GetPacUrl(char \*pacUrl) | 获取系统级代理自动配置(PAC)脚本地址。 |
| OH\_NetConn\_QueryProbeResult(char \*destination, int32\_t duration, NetConn\_ProbeResultInfo \*probeResultInfo) | 查询探测结果。 |
| OH\_NetConn\_QueryTraceRoute(char \*destination, NetConn\_TraceRouteOption \*option, NetConn\_TraceRouteInfo \*traceRouteInfo) | 查询跟踪路由。 |

#### 网络管理接口开发示例

#### \[h2\]开发步骤

使用本文档涉及接口获取网络相关信息时，需先创建Native C++工程，在源文件中将相关接口封装，再在ArkTS层对封装的接口进行调用，使用hilog或者console.log等手段选择打印在控制台或者生成设备日志。

本文以实现获取默认激活的数据网络为例，给出具体的开发指导。

其他接口开发请参考：[完整示例代码](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case)。

#### \[h2\]添加开发依赖

**添加动态链接库**

CMakeLists.txt中添加以下lib:

```txt
libace_napi.z.so
libnet_connection.so
```

**头文件**

#include "napi/native\_api.h"
#include "network/netmanager/net\_connection.h"
#include "network/netmanager/net\_connection\_type.h"

#### \[h2\]构建工程

1.  在源文件中编写调用该API的代码，并将结果封装成一个napi\_value类型的值返回给Node.js环境。
    
    // 获取默认网络的函数
    static napi\_value GetDefaultNet(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1; // 期望接收一个函数
        napi\_value args\[1\] = {nullptr}; // 存储接收到的参数
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        // ...
        int32\_t param;
        napi\_get\_value\_int32(env, args\[0\], &param); // 从 args\[0\] 获取整数值并存储到 param 中
        
        NetConn\_NetHandle netHandle;
        if (param == 0) { // 如果参数是0
            param = OH\_NetConn\_GetDefaultNet(NULL);
        } else {
            param = OH\_NetConn\_GetDefaultNet(&netHandle);
        }
    
        napi\_value result;
        napi\_create\_int32(env, param, &result);
        return result;
    }
    
    // 获取默认网络ID的函数
    static napi\_value NetId(napi\_env env, napi\_callback\_info info)
    {
        int32\_t defaultNetId;
        NetConn\_NetHandle netHandle;
        OH\_NetConn\_GetDefaultNet(&netHandle);
        defaultNetId = netHandle.netId; // 获取默认的 netId
        napi\_value result;
        napi\_create\_int32(env, defaultNetId, &result);
        return result;
    }
    
    简要说明：这两个函数用于获取系统默认网络连接的相关信息。其中，GetDefaultNet是接收ArkTS端传入的测试参数，返回调用接口后对应的返回值，param可以自行调整；如果返回值为0，代表获取成功，401代表参数错误，201代表没有权限；而NetId函数则用于获取默认网络连接的ID。这些信息可以用于进一步的网络操作。
    
2.  将通过napi封装好的napi\_value类型对象初始化导出，通过外部函数接口，将以上两个函数暴露给JavaScript使用。
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        // Information used to describe an exported attribute. Two properties are defined here: \`GetDefaultNet\` and \`NetId\`.
        napi\_property\_descriptor desc\[\] = {
            {"GetDefaultNet", nullptr, GetDefaultNet, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"NetId", nullptr, NetId, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // ...
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
3.  将上一步中初始化成功的对象通过RegisterEntryModule函数，使用napi\_module\_register函数将模块注册到Node.js中。
    
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
    
4.  在工程的index.d.ts文件中定义两个函数的类型。
    
    -   GetDefaultNet函数接受一个数字参数code，返回一个数字类型的值。
    -   NetId函数不接受参数，返回一个数字类型的值。
    
    export const GetDefaultNet: (code: number) => number;
    export const NetId: () => number;
    
5.  在index.ets文件中对上述封装好的接口进行调用。
    
    import testNetManager from 'libentry.so';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    enum ReturnCode {
      SUCCESS = 0, // 操作成功
      MISSING\_PERMISSION = 201, // 缺少权限
      PARAMETER\_ERROR = 401, // 参数错误
    }
    
    // ...
    @Entry
    @Component
    struct Index {
      @State message: string = ''; // 用于展示日志消息
      // ...
    
      build() {
        Column() { // 显示 Logger 输出的日志
          // ...
          Text(this.message)
            .fontSize(16)
            .fontColor(Color.Black)
            .margin({ bottom: 10 })
            .id('test-message') // 为测试消息设置 ID，便于测试获取内容
    
          Button($r('app.string.GetDefaultNet'))
            .onClick(() => {
              this.GetDefaultNet();
            })
              // ...
    
          Button($r('app.string.CodeNumber'))
            .onClick(() => {
              this.CodeNumber();
            })
              // ...
        }.width('100%').height('100%').justifyContent(FlexAlign.Center);
      }
      
      GetDefaultNet() {
        let netId = testNetManager.NetId();
        // ...
          hilog.info(0x0000, 'testTag', 'The defaultNetId is \[' + netId + '\]');
          // ...
      }
    
      CodeNumber() {
        let testParam = 1;
        // ...
          let codeNumber = testNetManager.GetDefaultNet(testParam);
          switch (codeNumber) {
            case ReturnCode.SUCCESS:
              hilog.info(0x0000, 'testTag', 'Test success. \[' + codeNumber + '\]');
              // ...
              break;
            case ReturnCode.MISSING\_PERMISSION:
              hilog.info(0x0000, 'testTag', 'Missing permissions. \[' + codeNumber + '\]');
              // ...
              break;
            case ReturnCode.PARAMETER\_ERROR:
              hilog.info(0x0000, 'testTag', 'Parameter error. \[' + codeNumber + '\]');
              // ...
              break;
            default:
              hilog.info(0x0000, 'testTag', 'Unexpected result: \[' + codeNumber + '\]');
              // ...
              break;
          }
        // ...
      }
      // ...
    }
    
6.  配置CMakeLists.txt，本模块需要用到的共享库是libnet\_connection.so，在工程自动生成的CMakeLists.txt中的target\_link\_libraries中添加此共享库。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ZIqsfv1RQ9S5tZsgEh8pxw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=6571139A5EB2A88CFCD87C8B42D6DA7CC9C4F3C79DC79D5CDE1AB2CC63A26E62)
    
    如图所示，在add\_library中的entry是工程自动生成的modname。若要做修改，需和步骤3中.nm\_modname保持一致。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/sihXXAuMSu6TGGxTFOri3Q/zh-cn_image_0000002538019364.png?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=B193973AA82E1093A239B0482C96DA05A077CF55311867A34FE664D5FAA9BA32)
    

经过以上步骤，整个工程的搭建已经完成，接下来就可以连接设备运行工程进行日志查看了。

#### 测试步骤

1.  连接设备，使用DevEco Studio打开搭建好的工程。
    
2.  运行工程，设备上会弹出以下所示图片。
    
    -   点击GetDefaultNet时获取的是默认网络ID。
    -   点击codeNumber时获取的是接口返回的响应状态码。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ruFXS7IyTxioDLEqpb9gCA/zh-cn_image_0000002538179294.png?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=2456CE066F52D42A77CCDF5D71EF36D770DD8284D405CBF09845B49D7A28885B)
    
3.  点击GetDefaultNet按钮，控制台会打印日志。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/GUrCN_EQTAitrSIfUHqQ9A/zh-cn_image_0000002569019081.png?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=2A6F1E6E82CD948B6AF5A4EEDD3C28FC074760A91BC955337EAE6FE93D3511AA)
    
4.  点击codeNumber按钮，控制台会打印相应的响应状态码。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/tLnAHqpcQMC2TbHQTlAvHQ/zh-cn_image_0000002568899073.png?HW-CC-KV=V1&HW-CC-Date=20260417T013555Z&HW-CC-Expire=86400&HW-CC-Sign=B7972978703DE7802938FFB53C914A71B26BEA14EBE72518EF2636D585245C21)
