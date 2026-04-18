---
title: "构建报错“input module releaseType is different”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-110"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "构建报错“input module releaseType is different”"
captured_at: "2026-04-17T02:03:22.411Z"
---

# 构建报错“input module releaseType is different”

**问题现象**

在打包APP时，如果提示“input module releaseType is different”，请检查输入模块的发布类型是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/IMXduUzCRmGCMOpBZ4OS5Q/zh-cn_image_0000002194318432.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=13004CD59388675FF60A9431E323E9B37B89B549DB97200DB4E93DD58E5BC57A)

**解决措施**

根据报错日志中的Warning信息提示的模块名称，检查模块间的apiReleaseType字段是否一致。

apiReleaseType字段由编译构建工具自动生成并保存在HAP/HSP包的module.json文件中。请确认各模块间该字段是否一致。如果存在不一致，需使用相同版本的SDK重新打包应用的各个模块，然后重新打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/CaHP88zqTo-3_jIdYJT8fQ/zh-cn_image_0000002229604205.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=E05B93E6F8A3C63DB455515D26F24F4DC9DEA95DB20546DFD0CB433C7FFBA4E7)
