---
title: "ArkTS组件错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-error-code"
menu_path:
  - "参考"
  - "应用服务"
  - "Scenario Fusion Kit（融合场景服务）"
  - "ArkTS组件"
  - "ArkTS组件错误码"
captured_at: "2026-04-17T01:49:04.010Z"
---

# ArkTS组件错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/3TpM2HWPRveISRwqlAm0Pg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014904Z&HW-CC-Expire=86400&HW-CC-Sign=681B4202ACEEDB35D671388B58AB3D568253345AF8AE8E4549A53BA4C3386305)

本模块错误码请参考以下链接。

[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)

[Map Kit错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-errorcode)

[Ability Kit错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-errcode)

[Account Kit错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-error-code)

[Live View Kit错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-error-code)

[Push Kit错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code)

[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)

[REST API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-server-error-code)

#### 10004 系统内部异常

**错误信息**

Internal error.

**错误描述**

系统内部异常。

**可能原因**

系统内部异常。

**处理步骤**

检查是否是网络问题, 如果是服务动态授权码Button报错，查看是否对子场景进行了邮件申请，详见[参考文档](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-timeline#section18702113217305)。

#### 10006 获取分享数据失败

**错误信息**

Failed to get data.

**错误描述**

获取分享数据失败。

**可能原因**

系统内部异常。

**处理步骤**

检查网络环境，如非网络环境影响需要结合具体日志分析。

#### 10008 调用方非元服务

**错误信息**

Not atomic service.

**错误描述**

调用方非元服务。

**可能原因**

非元服务调用了此接口。

**处理步骤**

通过元服务应用调用此接口。
