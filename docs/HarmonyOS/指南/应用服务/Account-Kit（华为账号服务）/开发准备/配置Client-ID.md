---
title: "配置Client ID"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-client-id"
menu_path:
  - "指南"
  - "应用服务"
  - "Account Kit（华为账号服务）"
  - "开发准备"
  - "配置Client ID"
captured_at: "2026-04-17T01:36:10.624Z"
---

# 配置Client ID

#### 获取Client ID和APP ID

在 AppGallery Connect（简称AGC）的[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中，选择对应的项目和对应的应用，在“常规 > 应用 ”下，找到**应用**的Client ID和APP ID。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/CmzOZxyNRuGi8dsouCmkEg/zh-cn_image_0000002538019688.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=3F90F16823E52F87F347CB0159FE9D514375D6F8F1400A920103363F2ECAC3DD)

#### 确认是否需要配置Client ID

如果上一步获取到的Client ID和APP ID相同，则无需配置Client ID，否则需要按下一步配置Client ID。

#### 配置Client ID

在工程中**entry**模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/YkyhPeACSCuu8cgCCFM1Hg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=8E8B604208E676D885D432799A2B3119363EE49D4BDACB9DCC8F30E9CA1D7966)

1.若工程中存在多个模块，需要在"type"为"entry"模块中的module.json5文件配置应用的Client ID。

2.请确认获取的Client ID是**应用**Client ID，错配成项目Client ID将导致接口调用报错。

```json
"module": {
  "name": "<name>",
  "type": "entry",
  "description": "<description>",
  "mainElement": "<mainElement>",
  "deviceTypes": [],
  "pages": "<pages>",
  "abilities": [],
  "metadata": [ // 配置信息如下
    {
      "name": "client_id",
      "value": "xxxxx" // 将上一步获取到的Client ID赋值给value，请注意不要使用其他方式设置value值
    }
  ]
 }
```
