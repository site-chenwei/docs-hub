---
title: "打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-4"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "工程管理"
  - "打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”"
captured_at: "2026-04-17T02:03:20.378Z"
---

# 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”

**问题现象**

在DevEco Studio打开历史工程，依赖安装不成功，报错信息为“Install failed FetchPackageInfo: hypium failed”。

**解决措施**

导致该问题的原因是包名使用错误。在工程级**oh-package.json5**中，将**devDependencies**字段下"hypium"修改为"@ohos/hypium"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/3HbHtY3bRP-WHYlhCtVIZQ/zh-cn_image_0000002194158560.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=D59E87D9E07B7A0C8D3910E4100429106D5305F49A59D82AA75E1923F02B1284)

@ohos/hypium版本号可通过ohpm命令获取，在DevEco Studio中打开Terminal，输入**ohpm info @ohos/hypium**命令，输出结果中dist-tags下方即为版本号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/ZwW8ggrURYWY2IHSRN977w/zh-cn_image_0000002402257997.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=D8890686249FB6D8C9311902B149934F9E6529591E6E0DC80C3ED3D5D2F6C57B)
