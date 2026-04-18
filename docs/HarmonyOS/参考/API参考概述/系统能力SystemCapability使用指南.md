---
title: "系统能力SystemCapability使用指南"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap"
menu_path:
  - "参考"
  - "API参考概述"
  - "系统能力SystemCapability使用指南"
captured_at: "2026-04-17T01:47:45.969Z"
---

# 系统能力SystemCapability使用指南

#### 概述

#### \[h2\]系统能力与 API

SysCap，全称SystemCapability，即系统能力，指操作系统中每一个相对独立的特性，如蓝牙，WIFI，NFC，摄像头等，都是系统能力之一。每个系统能力对应多个API，随着目标设备是否支持该系统能力共同存在或消失，也会随着DevEco Studio一起提供给开发者做联想。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/XGjo1PzhSb-xracJT_fg1Q/zh-cn_image_0000002538020336.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=3910AE53460D806E697F5AB3F6506D4C756A05526F36208DF8A0B6C232CD2A24)

#### \[h2\]支持能力集，联想能力集与要求能力集

支持能力集，联想能力集与要求能力集都是系统能力的集合。

支持能力集描述的是设备能力，要求能力集描述的是应用能力。若应用A的要求能力集是设备N的支持能力集的子集，则应用A可分发到设备N上安装运行，否则不能分发。

联想能力集是该应用开发时，DevEco Studio可联想的API所在的系统能力集合。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/f75XmbG7Q6a6fAhkbrOqXQ/zh-cn_image_0000002538180262.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=32D9A533C0D09D8240AF99214A8253D2E8A4B075FFC08153E30FE78803E494C4)

#### \[h2\]设备与支持能力集

每个设备根据其硬件能力，对应不同的支持能力集。

SDK将设备分为两组，典型设备和自定义设备，典型设备的支持能力集由HarmonyOS来定义，自定义设备由设备厂商给出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/vtNJP_EaTkKl5kI46hXeiA/zh-cn_image_0000002569020049.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=186444850C62DE17EE5DDD311579A74AF1314288E2CA48D162A4C473EAF2FBCD)

#### \[h2\]设备与SDK能力的对应

SDK向DevEco Studio提供全量API，DevEco Studio识别开发者项目中选择的设备形态，找到该设备的支持能力集，筛选支持能力集包含的API并提供API联想。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/MN1IXIv4ThCxgnUdGobRHA/zh-cn_image_0000002568900043.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=88CC3F6D48327B2137BB3E17D4EAA9D813EE2BBC9F87B47E6AB2FC7CA0BE9D03)

#### SysCap开发指导

#### \[h2\]加入自定义SysCap

在某具体的设备型号上，能力可能超出工程默认设备定义的能力集范围，如果需要使用此部分能力，需要额外配置自定义的SysCap。

请在DevEco Studio工程的模块/src/main目录下，手动创建syscap.json文件。如在entry/src/main目录右键，点击New > File。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/PM_oJt_tRZ6Nlqj3ikj-dA/zh-cn_image_0000002538020338.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=0653CC10C59D4FE6D5BF8430EF83E07E7BFEED628715D072B868C224A64568C9)

新建文件命名为syscap.json。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/BmDVulLKR0q4wtbpJvYC8A/zh-cn_image_0000002538180264.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=7BE5901C54BF7C9596C9EA47475B3272D78E30A94BFEFF39DC8EC6EFD3DDD1EC)

打开新建的syscap.json文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/qAEpAEMuTCieObDJ33nd8Q/zh-cn_image_0000002569020051.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=DAC5A9AC8329CD63E30C86D692CB6143665A6CD9A2D8D5DAC5B17EDC48C0D14F)

按如下格式填入所需要使用的SysCaps。以使用NFC能力为例，syscap.json文件示例如下。

```json
{
  "devices": {
    "general": [
      // 每一个典型设备对应一个SysCap支持能力集，可配置多个典型设备，应与工程所选择的设备一致
      "phone"
    ]
  },
  "development": {
    // addedSysCaps内的SysCap集合与devices中配置的各设备支持的SysCap集合的并集共同构成联想能力集。
    "addedSysCaps": [
      "SystemCapability.Communication.NFC.Core",
      "SystemCapability.Communication.NFC.CardEmulation",
      "SystemCapability.Communication.NFC.Tag"
    ]
  }
}
```

#### \[h2\]单设备应用开发

默认应用的联想能力集，要求系统能力集和设备的支持系统能力集相等，开发者修改要求能力集需要慎重。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/T7XOR3lxRuCMBq66cPxfjA/zh-cn_image_0000002568900045.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=1631D86DFAC74FCA2DE4E9B98C2F1D252FBE1691D12155059D02BF3D6CFAC64E)

#### \[h2\]跨设备应用开发

默认应用的联想能力集是多个设备支持能力集的并集，要求能力集则是交集。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/GSkslxoDQCiq1XjMijaoJQ/zh-cn_image_0000002538020340.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=A611D01AC37524A09DD89F792F9072EA45D8D15F047D5ED3BA88FF63F5A3C2B8)

#### \[h2\]判断 API 是否可以使用

当前提供了ArkTS API和Native API用于帮助判断某个API是否可以使用。

-   ArkTS API
    
    -   方法1：HarmonyOS定义了API canIUse帮助开发者来判断该设备是否支持某个特定的SysCap。
        
        ```ts
        if (canIUse("SystemCapability.ArkUI.ArkUI.Full")) {
        console.info("该设备支持SystemCapability.ArkUI.ArkUI.Full");
        } else {
           console.info("该设备不支持SystemCapability.ArkUI.ArkUI.Full");
        }
        ```
        
    -   方法2：开发者可通过import的方式将模块导入，若当前设备不支持该模块，import的结果为undefined，开发者在使用其API时，需要判断其是否存在。
        
        ```ts
        import { geoLocationManager } from '@kit.LocationKit';
        
        try {
        geoLocationManager.getCurrentLocation((location) => {
            console.info('current location: ' + JSON.stringify(location));
        });
        } catch(err) {
            console.error('该设备不支持位置信息' + err);
        }
        ```
        
-   Native API
    
    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include "syscap_ndk.h"
    
    char syscap[] = "SystemCapability.ArkUI.ArkUI.Full";
    bool result = canIUse(syscap);
    if (result) {
        printf("SysCap: %s is supported!\n", syscap);
    } else {
        printf("SysCap: %s is not supported!\n", syscap);
    }
    ```
    

除此之外，开发者可以通过API参考文档查询API接口所属的SysCap。

#### \[h2\]不同设备相同能力的差异检查

即使是相同的系统能力，在不同的设备下，也会有能力的差异。比如同是摄像头的能力，平板设备优于智能穿戴设备。

以下示例通过人脸识别功能进行举例：

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

const authParam : userAuth.AuthParam = {
  challenge: new Uint8Array(),
  authType: [userAuth.UserAuthType.PIN],
  authTrustLevel: userAuth.AuthTrustLevel.ATL1,
};
const widgetParam :userAuth.WidgetParam = {
  title: '请输入密码',
};

// 在使用接口时可通过try...catch捕获异常。如果接口的SysCap不支持当前设备，将返回801错误码。
try {
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  userAuthInstance.start();
    console.info('设备认证成功');
} catch (error) {
    console.error('auth catch error: ' + JSON.stringify(error));
}
```

#### \[h2\]设备间的SysCap差异如何产生的

设备的SysCap因产品解决方案厂商拼装的部件组合不同而不同，整体流程如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/FqmCqCTtSVqx5K2Q6j4C2g/zh-cn_image_0000002538180266.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=BA67E51F6893E6EABEE7BE7EADDF3AB353F572C2E4F6342E4E69B6EF16E7A956)

1.  一套操作系统源码由可选和必选部件集组成，不同的部件为对外体现的系统能力不同，即部件与 SysCap 之间映射关系。
    
2.  发布归一化的SDK，API与SysCap之间存在映射关系。
    
3.  产品解决方案厂商按硬件能力和产品诉求，可按需拼装部件。
    
4.  产品配置的部件可以是系统部件，也可以是三方开发的私有部件，由于部件与SysCap间存在映射，所有拼装后即可得到该产品的SysCap集合。
    
5.  SysCap集编码生成 PCID (Product Compatibility ID， 产品兼容性标识)，应用开发者可将PCID导入IDE解码成SysCap，开发时对设备的SysCap差异做兼容性处理。
    
6.  部署到设备上的系统参数中包含了SysCap集，系统提供了native的接口和应用接口，可供系统内的部件和应用查询某个SysCap是否存在。
    
7.  应用开发过程中，应用必要的SysCap将被编码成RPCID（Required Product Compatibility ID），并写入应用安装包中。应用安装时，包管理器将解码RPCID得到应用需要的 SysCap，与设备当前具备的SysCap比较，若应用要求的SysCap都被满足，则安装成功。
    
8.  应用运行时，可通过canIUse接口查询设备的SysCap，保证在不同设备上的兼容性。
