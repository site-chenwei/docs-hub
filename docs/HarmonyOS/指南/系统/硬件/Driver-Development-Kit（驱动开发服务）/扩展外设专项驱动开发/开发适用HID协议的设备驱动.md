---
title: "开发适用HID协议的设备驱动"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hid-ddk-guidelines"
menu_path:
  - "指南"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "扩展外设专项驱动开发"
  - "开发适用HID协议的设备驱动"
captured_at: "2026-04-17T01:35:56.251Z"
---

# 开发适用HID协议的设备驱动

#### 简介

HidDdk（HID Driver Development Kit）是为开发者提供的HID设备驱动程序开发套件，支持开发者基于用户态，在应用层开发HID设备驱动。提供了一系列主机侧访问设备的接口，包括创建设备、向设备发送事件、销毁设备、打开关闭设备、读取写入报告、获取设备信息等。

凡是采用USB总线，通过HID协议传输数据的设备，或者通过扩展外设驱动创建虚拟设备，来实现与非标设备的信息交互都可以使用HidDdk开发设备驱动。

#### \[h2\]基本概念

在进行HidDdk开发前，开发者应了解以下基本概念：

-   **HID**
    
    HID（Human Interface Device），中文意思是“人机接口设备”。它是一类用于实现人与计算机或其他电子设备交互的硬件设备。HID 设备的主要功能是将用户的输入（如按键、点击、移动等）转换为数据信号，并将这些信号发送给主机设备（如计算机、平板、游戏机等），从而实现用户对设备的控制和操作。
    
-   **DDK**
    
    DDK（Driver Development Kit）是HarmonyOS基于扩展外设框架，为开发者提供的驱动应用开发的工具包，可针对非标USB串口设备，开发对应的驱动。
    

#### \[h2\]实现原理

非标外设应用通过扩展外设管理服务获取HID设备的ID，通过RPC将ID和要操作的动作下发给HID设备驱动应用，驱动应用通过调用HidDdk接口可创建、销毁HID设备，以及对HID设备发送事件，获取HID报文，解析报文等，DDK接口使用HDI服务将指令下发至内核驱动，内核驱动使用指令与设备通信。

**图1** HidDdk调用原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/d2B8LVZQSfCcnWtbZsr_8A/zh-cn_image_0000002568899125.png?HW-CC-KV=V1&HW-CC-Date=20260417T013558Z&HW-CC-Expire=86400&HW-CC-Sign=DE9AC001E62E240A08E286D7F6926864882A170C6BF6E405AD4D9A52BF4F9C73)

#### 约束与限制

-   HidDdk开放API支持非标HID类外设扩展驱动开发场景。
    
-   HidDdk开放API仅允许DriverExtensionAbility生命周期内使用。
    
-   使用HidDdk开放API需要在module.json5中声明匹配的ACL权限，例如ohos.permission.ACCESS\_DDK\_HID。
    

#### 接口说明

| 名称 | 描述 |
| :-- | :-- |
| OH\_Hid\_CreateDevice(Hid\_Device \*hidDevice, Hid\_EventProperties \*hidEventProperties) | 创建HID设备。请在设备使用完后使用OH\_Hid\_DestroyDevice销毁设备。 |
| OH\_Hid\_EmitEvent(int32\_t deviceId, const Hid\_EmitItem items\[\], uint16\_t length) | 向指定deviceId的HID设备发送事件。 |
| OH\_Hid\_DestroyDevice(int32\_t deviceId) | 销毁指定deviceId的HID设备。 |
| int32\_t OH\_Hid\_Init(void) | 初始化HidDdk。 |
| int32\_t OH\_Hid\_Release(void) | 释放HidDdk。 |
| int32\_t OH\_Hid\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, Hid\_DeviceHandle \*\*dev) | 打开deviceId和interfaceIndex指定的设备。 |
| int32\_t OH\_Hid\_Close(Hid\_DeviceHandle \*\*dev) | 关闭设备。 |
| int32\_t OH\_Hid\_Write(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t length, uint32\_t \*bytesWritten) | 向设备写入报告。 |
| int32\_t OH\_Hid\_ReadTimeout(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize, int timeout, uint32\_t \*bytesRead) | 在指定的超时时间内从设备读取报告。 |
| int32\_t OH\_Hid\_Read(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize, uint32\_t \*bytesRead) | 从设备读取报告，默认为阻塞模式（阻塞等待直到有数据可读取），可以调用OH\_Hid\_SetNonBlocking改变模式。 |
| int32\_t OH\_Hid\_SetNonBlocking(Hid\_DeviceHandle \*dev, int nonblock) | 设置设备读取模式为非阻塞。 |
| int32\_t OH\_Hid\_GetRawInfo(Hid\_DeviceHandle \*dev, Hid\_RawDevInfo \*rawDevInfo) | 获取设备原始信息。 |
| int32\_t OH\_Hid\_GetRawName(Hid\_DeviceHandle \*dev, char \*data, uint32\_t buffSize) | 获取设备原始名称。 |
| int32\_t OH\_Hid\_GetPhysicalAddress(Hid\_DeviceHandle \*dev, char \*data, uint32\_t buffSize) | 获取设备物理地址。 |
| int32\_t OH\_Hid\_GetRawUniqueId(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize) | 获取设备原始唯一标识符。 |
| int32\_t OH\_Hid\_SendReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, const uint8\_t \*data, uint32\_t length) | 向设备发送报告。 |
| int32\_t OH\_Hid\_GetReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, uint8\_t \*data, uint32\_t buffSize) | 获取设备报告。 |
| int32\_t OH\_Hid\_GetReportDescriptor(Hid\_DeviceHandle \*dev, uint8\_t \*buf, uint32\_t buffSize, uint32\_t \*bytesRead) | 获取设备报告描述符。 |

详细的接口说明请参考[HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)。

#### 开发步骤

#### \[h2\]HID基础驱动能力开发

以下步骤描述了如何使用 **HidDdk**开发HID设备驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```txt
libhid.z.so
```

**头文件**

```
#include <hid/hid_ddk_api.h>
#include <hid/hid_ddk_types.h>
```

1.  创建设备。
    
    使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_CreateDevice** 接口创建HID设备，成功返回设备deviceId，失败返回[Hid\_DdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h#hid_ddkerrcode)。
    
    Hid\_Device hidDevice = {
        .deviceName = deviceName.c\_str(),
        .vendorId = 0x6006,
        .productId = 0x6008,
        .version = 1,
        .bustype = BUS\_USB
    };
    std::vector<Hid\_EventType> eventType = {HID\_EV\_KEY};
    Hid\_EventTypeArray eventTypeArray = {.hidEventType = eventType.data(), .length = (uint16\_t)eventType.size()};
    std::vector<Hid\_KeyCode> keyCode = {
        HID\_KEY\_1,          HID\_KEY\_SPACE,       HID\_KEY\_BACKSPACE,   HID\_KEY\_ENTER,     HID\_KEY\_ESC, HID\_KEY\_SYSRQ,
        HID\_KEY\_LEFT\_SHIFT, HID\_KEY\_RIGHT\_SHIFT, HID\_KEY\_VOLUME\_DOWN, HID\_KEY\_VOLUME\_UP, HID\_KEY\_0,   HID\_KEY\_2,
        HID\_KEY\_3,          HID\_KEY\_4,           HID\_KEY\_5,           HID\_KEY\_6,         HID\_KEY\_7,   HID\_KEY\_8,
        HID\_KEY\_9,          HID\_KEY\_A,           HID\_KEY\_B,           HID\_KEY\_C,         HID\_KEY\_D,   HID\_KEY\_E,
        HID\_KEY\_F,          HID\_KEY\_G,           HID\_KEY\_H,           HID\_KEY\_I,         HID\_KEY\_J,   HID\_KEY\_K,
        HID\_KEY\_L,          HID\_KEY\_M,           HID\_KEY\_N,           HID\_KEY\_O,         HID\_KEY\_P,   HID\_KEY\_Q,
        HID\_KEY\_R,          HID\_KEY\_S,           HID\_KEY\_T,           HID\_KEY\_U,         HID\_KEY\_V,   HID\_KEY\_W,
        HID\_KEY\_X,          HID\_KEY\_Y,           HID\_KEY\_Z,           HID\_KEY\_DELETE};
    Hid\_KeyCodeArray keyCodeArray = {.hidKeyCode = keyCode.data(), .length = (uint16\_t)keyCode.size()};
    Hid\_EventProperties hidEventProp = {.hidEventTypes = eventTypeArray, .hidKeys = keyCodeArray};
    int deviceId = OH\_Hid\_CreateDevice(&hidDevice, &hidEventProp);
    
2.  向指定deviceId的HID设备发送事件。
    
    使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_EmitEvent** 向指定的deviceId的设备发送事件。
    
    // 向指定deviceId的设备发送事件，事件来源于物理外设，通过InjectEvent方法注入
    int32\_t ret = OH\_Hid\_EmitEvent(item.first, item.second.data(), (uint16\_t)item.second.size());
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_EmitEvent failed, deviceId:%{public}d", item.first);
    }
    
3.  释放资源。
    
    在所有请求处理完毕，程序退出前，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_DestroyDevice** 接口销毁HID设备。
    
    // 销毁HID设备
    int32\_t res = OH\_Hid\_DestroyDevice(deviceId);
    

#### \[h2\]HID报文通信驱动能力开发

以下步骤描述了如何使用 **HidDdk** 开发HID报文通信驱动：

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```txt
libhid.z.so
```

**头文件**

```
#include <hid/hid_ddk_api.h>
#include <hid/hid_ddk_types.h>
```

1.  初始化DDK。
    
    使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Init** 初始化HidDdk。
    
    // 初始化HID DDK
    int32\_t ret = OH\_Hid\_Init();
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_Init() return failed: %{public}d", ret);
        return ret;
    }
    
2.  打开设备。
    
    初始化HidDdk后，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Open** 打开HID设备。
    
    uint32\_t bInterfaceNum1 = 0x00;
    // 打开deviceId和interfaceIndex1指定的HID设备（一般为/dev/hidraw0设备文件）
    ret = OH\_Hid\_Open(deviceID\_, bInterfaceNum1, &hid\_);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "Failed to open hid device, interface number:%{public}u ret:%{public}d",
            bInterfaceNum1, ret);
        return ret;
    }
    uint32\_t bInterfaceNum2 = 0x01;
    // 打开deviceId和interfaceIndex2指定的HID设备（一般为/dev/hidraw1设备文件）
    ret = OH\_Hid\_Open(deviceID\_, bInterfaceNum2, &hid2\_);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "Failed to open hid device, interface number:%{public}u ret:%{public}d",
            bInterfaceNum2, ret);
        return ret;
    }
    
3.  向HID设备写入/发送报告（HID设备与主机之间交换的数据包）（可选）。
    
    -   当报告类型为HID\_OUTPUT\_REPORT（输出报告）时，支持如下两种写入/发送方式。
        -   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Write** 向HID设备写入一个输出报告。
            
            uint32\_t bytesWritten;
            // 写入报告
            int32\_t ret = OH\_Hid\_Write(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff), &bytesWritten);
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_Write failed. ret: %{public}u", ret);
            }
            
        -   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_SendReport** 向HID设备发送一个输出报告。
            
            // 发送输出报告
            int32\_t ret = OH\_Hid\_SendReport(DataParser::GetInstance().getHidObject(), HID\_OUTPUT\_REPORT, dataBuff,
                                            sizeof(dataBuff));
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_SendReport failed. ret: %{public}u", ret);
            }
            
        -   当报告类型为HID\_FEATURE\_REPORT（特性报告）时，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_SendReport** 向HID设备发送一个特性报告。
            
            uint8\_t dataBuff\[NUM\_EIGHT\] = { 0x00 };
            string str(hexFormat);
            HexStringToUint8Array(str, dataBuff, sizeof(dataBuff));
            // 发送特性报告
            int32\_t ret = OH\_Hid\_SendReport(DataParser::GetInstance().getHid2Object(), HID\_FEATURE\_REPORT, dataBuff,
                                            sizeof(dataBuff));
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_SendReport failed. ret: %{public}u", ret);
            }
            
4.  从HID设备读取报告（可选）。
    
    -   当报告类型为HID\_INPUT\_REPORT（输入报告）时，支持如下三种读取方式。
        -   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_SetNonBlocking** 设置读取模式。
            
            // nonblock取值：1启用非阻塞，0禁用非阻塞
            ret = OH\_Hid\_SetNonBlocking(DataParser::GetInstance().getHidObject(), nonblockTag);
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_SetNonBlocking failed. ret: %{public}u", ret);
                return false;
            }
            
        -   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Read** 或者 **OH\_Hid\_ReadTimeout** 以非阻塞模式或者阻塞模式从HID设备读取一个输入报告。
            
            if (nonblock) {
                ret = OH\_Hid\_Read(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff), &bytesRead);
            } else {
                ret = OH\_Hid\_ReadTimeout(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff),
                                         CONST\_TIMEOUT, &bytesRead);
            }
            
        -   使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetReport** 从HID设备读取一个输入报告。
            
            uint8\_t dataBuff\[NUM\_NINE\] = { 0x00 };
            // 读取输入报告
            int32\_t ret = OH\_Hid\_GetReport(DataParser::GetInstance().getHidObject(), HID\_INPUT\_REPORT, dataBuff,
                                           sizeof(dataBuff));
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetReport failed. ret: %{public}u", ret);
                return nullptr;
            }
            
        -   当报告类型为HID\_FEATURE\_REPORT（特性报告）时，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetReport** 从HID设备读取一个特性报告。
            
            uint8\_t dataBuff\[NUM\_EIGHT\] = { 0x00 };
            // 指定报告编号
            dataBuff\[0\] = 0x07;
            // 读取特性报告
            int32\_t ret = OH\_Hid\_GetReport(DataParser::GetInstance().getHid2Object(), HID\_FEATURE\_REPORT, dataBuff,
                                           sizeof(dataBuff));
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetReport failed. ret: %{public}u", ret);
                return nullptr;
            }
            
5.  获取设备原始信息、原始名称、物理地址、原始唯一标识符（可选）。
    
    使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetRawInfo** 获取HID设备原始信息，使用 **OH\_Hid\_GetRawName** 获取HID设备原始名称，使用 **OH\_Hid\_GetPhysicalAddress** 获取HID设备物理地址，使用 **OH\_Hid\_GetRawUniqueId** 获取HID设备原始唯一标识符。这些信息可被上层应用引用，例如在界面中展示设备信息等。
    
    Hid\_RawDevInfo rawDevInfo;
    int32\_t ret = OH\_Hid\_GetRawInfo(DataParser::GetInstance().getHidObject(), &rawDevInfo);
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetRawInfo failed, ret:%{public}d", ret);
        return nullptr;
    }
    
    char dataBuff\[DATA\_BUFF\_SIZE\];
    int32\_t ret = OH\_Hid\_GetRawName(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetRawName failed, ret:%{public}d", ret);
        return nullptr;
    }
    
    char dataBuff\[DATA\_BUFF\_SIZE\];
    int32\_t ret = OH\_Hid\_GetPhysicalAddress(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetPhysicalAddress failed, ret:%{public}d", ret);
        return nullptr;
    }
    
    uint8\_t dataBuff\[NUM\_SIXTY\_FOUR\];
    int32\_t ret = OH\_Hid\_GetRawUniqueId(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetRawUniqueId failed, ret:%{public}d", ret);
        return nullptr;
    }
    
6.  获取报告描述符（可选）。
    
    使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_GetReportDescriptor** 获取HID设备报告描述符。
    
    uint8\_t dataBuff\[DATA\_BUFF\_SIZE1\];
    uint32\_t bytesRead;
    int32\_t ret = OH\_Hid\_GetReportDescriptor(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff),
                                             &bytesRead);
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetReportDescriptor failed, ret:%{public}d", ret);
        return nullptr;
    }
    
7.  关闭设备。
    
    在所有请求处理完毕后，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Close** 关闭设备。
    
    Hid\_DeviceHandle \*hid = DataParser::GetInstance().getHidObject();
    int32\_t ret1 = OH\_Hid\_Close(&hid);
    DataParser::GetInstance().UpdateHid(hid);
    
8.  释放DDK。
    
    在关闭HID设备后，使用 **hid\_ddk\_api.h** 的 **OH\_Hid\_Release** 释放HidDdk。
    
    ret1 = OH\_Hid\_Release();
    if (ret1 != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_Init() return failed: %{public}d", ret1);
    }
