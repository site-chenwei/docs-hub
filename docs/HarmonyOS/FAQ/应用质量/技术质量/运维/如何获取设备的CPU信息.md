---
title: "如何获取设备的CPU信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-22"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何获取设备的CPU信息"
captured_at: "2026-04-17T02:02:57.324Z"
---

# 如何获取设备的CPU信息

可以通过以下命令来查看CPU信息：

```powershell
// 查看CPU信息  
hdc shell param get const.product.cpu.abilist
```

返回结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/YGS4ep4hTsSzasv8XnzPHA/zh-cn_image_0000002229758737.png?HW-CC-KV=V1&HW-CC-Date=20260417T020258Z&HW-CC-Expire=86400&HW-CC-Sign=24B0BB2E98E0B9C3631DDC75254100822C7F3BFB36E63AA5F8BD49DF93B02047 "点击放大")
