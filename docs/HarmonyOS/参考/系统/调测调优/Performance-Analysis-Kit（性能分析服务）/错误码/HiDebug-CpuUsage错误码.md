---
title: "HiDebug CpuUsage错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-cpuusage"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "错误码"
  - "HiDebug CpuUsage错误码"
captured_at: "2026-04-17T01:48:35.337Z"
---

# HiDebug CpuUsage错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/RZ2BeYUQSnmF9xkWqVOASQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=4F82D577C03A580FC2C63483C5605EA69D2E771905F9695ABDA5165DEB70D5A1)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 11400104 CpuUsage统计异常

**错误信息**

The status of the system CPU usage is abnormal.

**错误描述**

当前CPU使用率状态异常。

**可能原因**

hiview服务进程未正常启动。

**处理步骤**

检查hiview进程的运行状态，重启hiview服务或系统。
