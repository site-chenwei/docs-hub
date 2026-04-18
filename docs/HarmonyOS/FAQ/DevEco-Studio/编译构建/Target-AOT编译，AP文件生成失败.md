---
title: "Target AOT编译，AP文件生成失败"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-29"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "Target AOT编译，AP文件生成失败"
captured_at: "2026-04-17T02:03:21.348Z"
---

# Target AOT编译，AP文件生成失败

**问题现象**

Target AOT编译，AP文件生成失败，并报错提示“errno: 13”表示权限不足，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/z-mj2V2ERguuDuDJsqMYGA/zh-cn_image_0000002229758617.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=34CDE7D7889DA6D7E8ADF25F47C6F3905C5FB55061C9A9140077E05CD32D1D7B)

**解决措施**

errno: 13表示权限不足，请通过下述措施解决：

打开命令行工具，输入以下命令，关闭selinux权限管控。

```powershell
hdc shell
setenforce 0
```

以上设置重启将会失效，若设备重启请重新进行以上设置
