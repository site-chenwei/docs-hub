---
title: "使用云存储上传文件失败，app日志提示“\"state\":65”，upload进程日志提示“403 Forbidden”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2"
menu_path:
  - "指南"
  - "应用服务"
  - "Cloud Foundation Kit（云开发服务）"
  - "Cloud Foundation Kit常见问题"
  - "云存储"
  - "使用云存储上传文件失败，app日志提示“\"state\":65”，upload进程日志提示“403 Forbidden”"
captured_at: "2026-04-17T01:36:13.888Z"
---

# 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

-   app日志提示“"state":65”
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/XB2YaqZ7R72irfEbRldM-Q/zh-cn_image_0000002569019535.png?HW-CC-KV=V1&HW-CC-Date=20260417T013614Z&HW-CC-Expire=86400&HW-CC-Sign=F1BA5B4ABF13C44D9B7F9C344CE0390F02CB634CB4D72569BAC4382C929B8567)
    
-   upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/LL63AuwvR9GnmWD8SRZRTQ/zh-cn_image_0000002568899527.png?HW-CC-KV=V1&HW-CC-Date=20260417T013614Z&HW-CC-Expire=86400&HW-CC-Sign=3C28057D0D4C74E2F290EF3EE11F0B7F9A09062B33B9141638482EB410E58A3E)
    

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1.  请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section20943184413328)和[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)两种方式。
    
2.  请确认已通过[AuthProvider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudcommon#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
