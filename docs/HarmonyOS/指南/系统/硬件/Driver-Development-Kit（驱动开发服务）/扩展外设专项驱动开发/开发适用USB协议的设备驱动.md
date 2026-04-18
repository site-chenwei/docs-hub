---
title: "开发适用USB协议的设备驱动"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usb-ddk-guidelines"
menu_path:
  - "指南"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "扩展外设专项驱动开发"
  - "开发适用USB协议的设备驱动"
captured_at: "2026-04-17T01:35:56.249Z"
---

# 开发适用USB协议的设备驱动

#### 简介

UsbDdk（USB Driver Development Kit）是为开发者提供的USB驱动程序开发套件，支持开发者基于用户态，在应用层开发USB设备驱动。提供了一系列主机侧访问设备的接口，包括主机侧打开和关闭接口、管道同步异步读写通信、控制传输、中断传输等。

凡是采用USB总线，通过USB协议传输数据的设备都可以使用UsbDdk开发设备驱动。特别是内核标准驱动不支持的扩展外设，可以通过UsbDdk开发的扩展外设驱动应用实现其独特的设备能力。

#### \[h2\]基本概念

在进行UsbDdk开发前，开发者应了解以下基本概念：

-   **USB**
    
    USB（Universal Serial Bus，通用串行总线）是一种广泛使用的接口技术，用于连接计算机与各种外部设备，如键盘、鼠标、打印机、存储设备、智能手机等。USB 的设计目标是提供一种标准化、高效且易于使用的连接方式，以替代传统的串行和并行接口。
    
-   **DDK**
    
    DDK（Driver Development Kit）是HarmonyOS基于扩展外设框架，为开发者提供的驱动应用开发的工具包，可针对非标USB设备，开发对应的驱动。
    

#### \[h2\]实现原理

非标外设应用通过扩展外设管理服务获取USB设备的ID，通过RPC将ID和要操作的动作下发给USB驱动应用。USB驱动应用通过调用UsbDdk接口，可获取设备描述符与配置描述符，以及发送控制传输和中断传输等请求，DDK接口使用HDI服务将指令下发至内核驱动，内核驱动使用指令与设备通信。

**图1** UsbDdk调用原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/pHgSpAcbTsaGP8PujvIf7g/zh-cn_image_0000002568899125.png?HW-CC-KV=V1&HW-CC-Date=20260417T013558Z&HW-CC-Expire=86400&HW-CC-Sign=3B801DB524911DA0A80CFAAD73C29DB8AC208EFF9DF444D38E4E4F44C6C9A19A)

#### 约束与限制

-   UsbDdk开放API支持USB接口非标外设扩展驱动开发场景。
    
-   UsbDdk开放API仅允许DriverExtensionAbility生命周期内使用。
    
-   使用UsbDdk开放API需要在module.json5中声明匹配的ACL权限，例如ohos.permission.ACCESS\_DDK\_USB。
    

#### 环境搭建

请参考[环境准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/environmental-preparation)完成开发前的准备工作。

#### 开发指导

#### \[h2\]接口说明

| 名称 | 描述 |
| :-- | :-- |
| OH\_Usb\_Init(void) | 初始化DDK。 |
| OH\_Usb\_Release(void) | 释放DDK。 |
| OH\_Usb\_GetDeviceDescriptor(uint64\_t deviceId, struct UsbDeviceDescriptor \*desc) | 获取设备描述符。 |
| OH\_Usb\_GetConfigDescriptor(uint64\_t deviceId, uint8\_t configIndex, struct UsbDdkConfigDescriptor \*\*const config) | 获取配置描述符。请在描述符使用完后使用OH\_Usb\_FreeConfigDescriptor()释放描述符，否则会造成内存泄漏。 |
| OH\_Usb\_FreeConfigDescriptor(const struct UsbDdkConfigDescriptor \*const config) | 释放配置描述符，请在描述符使用完后释放描述符，否则会造成内存泄漏。 |
| OH\_Usb\_ClaimInterface(uint64\_t deviceId, uint8\_t interfaceIndex, uint64\_t \*interfaceHandle) | 声明接口。 |
| OH\_Usb\_SelectInterfaceSetting(uint64\_t interfaceHandle, uint8\_t settingIndex) | 激活接口的备用设置。 |
| OH\_Usb\_GetCurrentInterfaceSetting(uint64\_t interfaceHandle, uint8\_t \*settingIndex) | 获取接口当前激活的备用设置。 |
| OH\_Usb\_SendControlReadRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup, uint32\_t timeout, uint8\_t \*data, uint32\_t \*dataLen) | 发送控制读请求，该接口为同步接口。 |
| OH\_Usb\_SendControlWriteRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup, uint32\_t timeout, const uint8\_t \*data, uint32\_t dataLen) | 发送控制写请求，该接口为同步接口。 |
| OH\_Usb\_ReleaseInterface(uint64\_t interfaceHandle) | 释放接口。 |
| OH\_Usb\_SendPipeRequest(const struct UsbRequestPipe \*pipe, UsbDeviceMemMap \*devMmap) | 发送管道请求，该接口为同步接口。中断传输和批量传输都使用该接口发送请求。 |
| OH\_Usb\_CreateDeviceMemMap(uint64\_t deviceId, size\_t size, UsbDeviceMemMap \*\*devMmap) | 创建缓冲区。请在缓冲区使用完后，调用OH\_Usb\_DestroyDeviceMemMap()销毁缓冲区，否则会造成资源泄漏。 |
| OH\_Usb\_DestroyDeviceMemMap(UsbDeviceMemMap \*devMmap) | 销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄漏。 |
| OH\_Usb\_GetDevices(struct Usb\_DeviceArray \*devices) | 获取USB设备ID列表。请保证传入的指针参数是有效的，申请的设备ID数组的大小建议不超过128，以避免过度占用内存。在使用完结构之后，释放成员内存，否则造成资源泄漏。获取到的USB设备ID，已通过驱动配置信息中的vid进行筛选过滤。 |

详细的接口说明请参考[UsbDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk)。

#### \[h2\]开发步骤

以下步骤描述了如何使用 **UsbDdk**开发USB驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```txt
libusb_ndk.z.so
```

**头文件**

```
#include <usb/usb_ddk_api.h>
#include <usb/usb_ddk_types.h>
```

1.  获取设备描述符。
    
    使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_Init** 接口初始化DDK，并使用 **OH\_Usb\_GetDeviceDescriptor**获取到设备描述符。
    
    // 初始化USB DDK
    int32\_t ret = OH\_Usb\_Init();
    OH\_LOG\_INFO(LOG\_APP, "OH\_Usb\_Init ret=:%{public}d\\n", ret);
    // ...
    struct UsbDeviceDescriptor devDesc;
    // 获取设备描述符
    ret = OH\_Usb\_GetDeviceDescriptor(g\_devHandle, &devDesc);
    
2.  获取配置描述符及声明接口。
    
    使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_GetConfigDescriptor** 接口获取配置描述符 **config**，并使用 **OH\_Usb\_ClaimInterface** 声明"认领"接口。
    
    struct UsbDdkConfigDescriptor \*config = nullptr;
    // 获取配置描述符
    auto ret = OH\_Usb\_GetConfigDescriptor(g\_devHandle, 1, &config);
    OH\_LOG\_INFO(LOG\_APP, "OH\_Usb\_GetConfigDescriptor ret = %{public}d", ret);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "get config desc failed:%{public}d", ret);
        return false;
    }
    // 从配置描述符中找到手写板相关的接口和端点
    auto \[res, interface, endpoint, maxPktSize\] = GetInterfaceAndEndpoint(config);
    OH\_LOG\_INFO(LOG\_APP, "OH\_Usb\_GetConfigDescriptor ret = %{public}d", res);
    if (!res) {
        OH\_LOG\_ERROR(LOG\_APP, "GetInterfaceAndEndpoint failed");
        return false;
    }
    // 释放配置描述符，防止内存泄露
    OH\_Usb\_FreeConfigDescriptor(config);
    g\_dataEp = endpoint;
    g\_maxPktSize = maxPktSize;
    g\_interface = interface;
    // 占用接口，同时也会卸载内核键盘驱动
    ret = OH\_Usb\_ClaimInterface(g\_devHandle, g\_interface, &g\_interfaceHandle);
    
3.  获取当前激活接口的备用设置及激活备用设置（可选）。
    
    使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_GetCurrentInterfaceSetting** 获取备用设置，并使用 **OH\_Usb\_SelectInterfaceSetting** 激活备用设置。
    
    uint8\_t settingIndex = 0;
    // 接口获取备用设置
    int32\_t ret = OH\_Usb\_GetCurrentInterfaceSetting(g\_interfaceHandle, &settingIndex);
    if (ret != USB\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Usb\_GetCurrentInterfaceSetting failed, ret=%{public}d", ret);
    }
    
    // 激活备用设置
    ret = OH\_Usb\_SelectInterfaceSetting(g\_interfaceHandle, settingIndex);
    if (ret != USB\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Usb\_SelectInterfaceSetting failed, ret=%{public}d", ret);
    }
    
4.  发送控制读请求、发送控制写请求（可选）。
    
    使用 **usb\_ddk\_api.h** 的**OH\_Usb\_SendControlReadRequest**发送控制读请求，或者使用**OH\_Usb\_SendControlWriteRequest**发送控制写请求。
    
    uint8\_t strDesc\[100\] = {0};
    // 获取产品字符串描述符
    uint32\_t len = 100;
    struct UsbControlRequestSetup strDescSetup;
    strDescSetup.bmRequestType = 0x80;
    strDescSetup.bRequest = 0x06;
    strDescSetup.wValue = (0x03 << BIT\_EIGHT) | (iProduct); // desc Index
    strDescSetup.wIndex = 0x409;                    // language Id
    strDescSetup.wLength = len;
    auto ret = OH\_Usb\_SendControlReadRequest(g\_interfaceHandle, &strDescSetup, UINT32\_MAX, strDesc, &len);
    
    // 设置feature
    uint32\_t timeout = 5000;
    struct UsbControlRequestSetup strDescSetup;
    strDescSetup.bmRequestType = 0x21;
    strDescSetup.bRequest = 0x09;
    strDescSetup.wValue = ((0x03 << BIT\_EIGHT) | 0x02); // desc Index
    strDescSetup.wIndex = 0x0;
    strDescSetup.wLength = 0x02;
    uint8\_t data\[128\] = {0x02, 0x02};
    uint32\_t dataLen = 2;
    int32\_t ret = OH\_Usb\_SendControlWriteRequest(g\_interfaceHandle, &strDescSetup, timeout, data, dataLen);
    
5.  创建内存映射缓冲区及发送请求（可选）。
    
    使用 **usb\_ddk\_api.h** 的**OH\_Usb\_CreateDeviceMemMap**接口创建内存映射缓冲区**devMmap**，并使用**OH\_Usb\_SendPipeRequest**发送请求。
    
    // 占用接口，同时也会卸载内核键盘驱动
    // 创建用于存放数据的缓冲区
    int32\_t ret = OH\_Usb\_CreateDeviceMemMap(g\_devHandle, bufferLen, &devMmap);
    
    struct UsbRequestPipe pipe;
    pipe.interfaceHandle = g\_interfaceHandle;
    pipe.endpoint = g\_dataEp;
    pipe.timeout = 4; // 中断传输超时时间，保持和手写板bInterval保持一致
    // 读取手写板数据
    // 通过USB中断传输方式，读取键值
    ret = OH\_Usb\_SendPipeRequest(&pipe, devMmap);
    
6.  释放资源。
    
    在所有请求处理完毕，程序退出前，使用 **usb\_ddk\_api.h** 的 **OH\_Usb\_DestroyDeviceMemMap** 接口销毁缓冲区。使用**OH\_Usb\_ReleaseInterface**释放接口。使用**OH\_Usb\_Release**释放UsbDdk。
    
    // 销毁缓冲区
    OH\_Usb\_DestroyDeviceMemMap(devMmap);
    // 释放接口
    int32\_t ret = OH\_Usb\_ReleaseInterface(g\_interfaceHandle);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "ReleaseInterface failed %{public}d", ret);
    }
    // 释放USB DDK
    OH\_Usb\_Release();
    
7.  获取可识别的USB设备列表（独立步骤，可选）。
    
    驱动拉起后调用**OH\_Usb\_GetDevices**接口获取驱动配置信息中匹配vid（vid是设备厂商的vendor id，在驱动应用里面配置，表示驱动适配哪些设备，查询到的设备ID都需要通过vid进行过滤）的设备ID，以供后续应用开发使用。
    
    constexpr size\_t maxUsbDeviceNum = 128;
    struct Usb\_DeviceArray deviceArray;
    deviceArray.deviceIds = new uint64\_t\[maxUsbDeviceNum\];
    // 获取设备列表
    int32\_t ret = OH\_Usb\_GetDevices(&deviceArray);
    if (ret != USB\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Usb\_GetDevices failed, ret=%{public}d", ret);
    }
