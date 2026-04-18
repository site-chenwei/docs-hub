---
title: "RunningLock锁错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-runninglock"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "错误码"
  - "RunningLock锁错误码"
captured_at: "2026-04-17T01:48:29.563Z"
---

# RunningLock锁错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/CxdsyEqIRhiP2i8RfvvzCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=A4D352EED22C8E705918675B85AE2184DDC0238D661943FB5B601D1980BA2FCE)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 4900101 连接服务失败

**错误信息**

Failed to connect to the service.

**错误描述**

操作失败，连接系统服务发生异常。

**可能原因**

1.  系统服务停止运行。
    
2.  系统服务内部通讯发生异常。
    

**处理步骤**

检查系统服务是否正常运行。

1.  在控制台中输入如下命令，查看当前的系统服务列表。
    
    ```bash
    > hdc shell hidumper -ls
    ```
    
2.  查看系统服务列表中是否包含PowerManagerService系统服务。
