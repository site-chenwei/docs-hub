---
title: "如何通过hdc命令关闭整个应用"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-47"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何通过hdc命令关闭整个应用"
captured_at: "2026-04-17T02:02:57.447Z"
---

# 如何通过hdc命令关闭整个应用

可以通过以下命令结束应用：

```powershell
hdc shell aa force-stop <bundleName>
```

返回“force stop process successfully”，表示应用已成功结束。

示例如下：

```powershell
hdc shell aa force-stop com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/kqiQTeccSyqsfH0GIBCZiA/zh-cn_image_0000002194158796.png?HW-CC-KV=V1&HW-CC-Date=20260417T020259Z&HW-CC-Expire=86400&HW-CC-Sign=3D9DE9D1783A46C14E0384F75E81088EB6471E20B8D637A5163084C20ABD5EA4 "点击放大")

**参考链接**

[aa工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aa-tool)
