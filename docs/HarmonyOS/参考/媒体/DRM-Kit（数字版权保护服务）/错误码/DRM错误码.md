---
title: "DRM错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drm"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "错误码"
  - "DRM错误码"
captured_at: "2026-04-17T01:48:40.781Z"
---

# DRM错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/cl0HHtYlSkGaffOwFqBXaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014842Z&HW-CC-Expire=86400&HW-CC-Sign=C32F3CF7C402C5A1B0F335640C4EFA38BF97A1FEBC2B17BFD3F82F7EB9444EC7)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 24700101 未知错误

**错误信息**

Unknown error.

**错误描述**

未知错误。

**可能原因**

输入参数格式、数据类型错误，导致数据获取、数据转换失败等。

**处理步骤**

获取异常的描述，并检查系统错误日志，根据异常描述及日志中的错误描述处理。

#### 24700103 MediaKeySystem数量达到极限

**错误信息**

Too many MediaKeySystem instances.

**错误描述**

MediaKeySystem实例数量超过上限（64个）。

**可能原因**

无效的MediaKeySystem实例没有及时释放。

**处理步骤**

释放其他不再使用的MediaKeySystem资源。

#### 24700104 MediaKeySession数量达到极限

**错误信息**

Too many MediaKeySession instances.

**错误描述**

MediaKeySession实例数量超过上限（64个）。

**可能原因**

无效的MediaKeySession实例没有及时释放。

**处理步骤**

释放其他不再使用的MediaKeySession资源。

#### 24700201 服务异常

**错误信息**

Service error. For example, the service crashed.

**错误描述**

DRM服务异常。

**可能原因**

1.  底层DRM解决方案插件功能执行错误。
    
2.  DRM服务挂死等。
    

**处理步骤**

获取异常的描述，并检查系统错误日志，根据异常描述及日志中的错误描述处理。
