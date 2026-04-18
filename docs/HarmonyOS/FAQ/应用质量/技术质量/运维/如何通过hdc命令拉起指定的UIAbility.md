---
title: "如何通过hdc命令拉起指定的UIAbility"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-45"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何通过hdc命令拉起指定的UIAbility"
captured_at: "2026-04-17T02:02:57.452Z"
---

# 如何通过hdc命令拉起指定的UIAbility

使用命令拉起指定UIAbility：

```powershell
hdc shell aa start -a <UIAbility Name> -b <Bundle Name>
```

启动成功时，返回"start ability successfully."，启动失败时，返回"error: failed to start ability"，同时会包含相应的失败信息。

示例如下：

```powershell
hdc shell aa start -a EntryAbility -b com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/zjhJc_z6QjCz3ZXIv0ggqw/zh-cn_image_0000002229758597.png?HW-CC-KV=V1&HW-CC-Date=20260417T020259Z&HW-CC-Expire=86400&HW-CC-Sign=858E72D4A890175591258A209933B86A73FABCCE780E278FF50FC1F44915A3F0 "点击放大")

**参考链接**

[aa工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aa-tool)
