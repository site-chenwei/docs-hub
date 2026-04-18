---
title: "HiDebug Trace错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-trace"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "错误码"
  - "HiDebug Trace错误码"
captured_at: "2026-04-17T01:48:35.341Z"
---

# HiDebug Trace错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/te_iFDZ1Q9OCZYrILCvcvg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=E3FB6DE690C0550EFD238547E9F0BAF3C8FC77F376A9925474E092362172B430)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 11400102 重复采集

**错误信息**

Capture trace already enabled.

**错误描述**

进程已开启trace采集。

**可能原因**

进程正在进行trace采集。

**处理步骤**

等待trace采集结束或调用hidebug.stopAppTraceCapture关闭正在运行的trace采集。

#### 11400103 权限校验失败

**错误信息**

No write permission on the file.

**错误描述**

当前目录没有权限写trace文件。

**可能原因**

目录不存在或被误操作删除。

**处理步骤**

重新运行采集接口，再次生成正确的目录文件。

#### 11400104 内部异常

**错误信息**

Abnormal trace status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/-H87p_z5QvSwhdvVfinACg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=BA9CE17F10B1FECEC27DB1F466429D6B9B66EF3431AAA2E17672960CF2ACA561)

错误信息请以接口实际返回内容为准。

**错误描述**

当前trace采集内部状态异常。

**可能原因**

系统内核崩溃或应用进程无响应。

**处理步骤**

建议重启应用或设备。

#### 11400105 未开启trace采集

**错误信息**

No capture trace running.

**错误描述**

当前没有trace正在采集。

**可能原因**

未开启trace采集。

**处理步骤**

开启trace采集，然后停止。

#### 11400106 接口调用配额已超出

**错误信息**

Quota exceeded.

**错误描述**

接口调用配额已超出。

**可能原因**

1.进程调用次数超出配额（1次/天）。

2.整机调用次数超出配额（5次/周）。

**处理步骤**

等待进程或整机的调用配额刷新。
