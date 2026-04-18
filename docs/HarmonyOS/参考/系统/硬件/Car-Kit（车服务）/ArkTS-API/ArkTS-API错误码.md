---
title: "ArkTS API错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-error-code"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Car Kit（车服务）"
  - "ArkTS API"
  - "ArkTS API错误码"
captured_at: "2026-04-17T01:48:32.198Z"
---

# ArkTS API错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/r8BzxONPSpKlTgxNXl9FCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=F650371B99B54EB1A5CE2FF1C02A3BDF98844DFF5A9A733F5BF31E71C099B998)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 1003810001 参数值无效

**错误信息**

Invalid parameter value.

**错误描述**

无效的参数值。

**可能原因**

1.  设置导航状态时目的地名称长度或途经点名称长度超出1024字节。
    
2.  设置导航元数据时当前道路名或下一次进入的道路名的长度超出1024字节。
    
3.  参数值超出范围，比如设置导航状态时经纬度值不在有效范围（纬度值的数值范围是\[-90, 90\]，经度值的有效范围是\[-180, 180\]）内。
    

**处理步骤**

在设置导航状态、导航元数据时请确保参数传递正确。

#### 1003810002 所有参数总大小超出限制

**错误信息**

The total size of all parameters exceeds the limit.

**错误描述**

所有参数总大小超出了限制。

**可能原因**

1.  设置导航状态时添加的途经点太多。
    
2.  设置导航元数据时当传入路口放大图时参数总大小可能会超出限制（200Kbytes）。
    

**处理步骤**

1.  设置导航状态时检查添加途经点的数量，确保途经点的数量不超出20个。
    
2.  设置导航元数据时如果要传入路口放大图，并且图片较大时，建议对图片做压缩处理。
