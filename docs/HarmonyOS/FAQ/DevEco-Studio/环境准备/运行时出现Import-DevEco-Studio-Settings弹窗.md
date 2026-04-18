---
title: "运行时出现Import DevEco Studio Settings弹窗"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-16"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "运行时出现Import DevEco Studio Settings弹窗"
captured_at: "2026-04-17T02:03:20.287Z"
---

# 运行时出现Import DevEco Studio Settings弹窗

**问题现象**

问题出现包含两种场景：

场景一：首次运行DevEco Studio时，出现**Import DevEco Studio Settings**弹窗。

场景二：本地清理DevEco Studio缓存后再次下载安装运行时，可能出现**Import DevEco Studio Settings**弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/rBrIGd5XSKSOAOrqwYeKdQ/zh-cn_image_0000002474225988.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=54C1DF3788B7506B14F178BBB701E73BDA7648AFE0974B2C4D4DF9C555770903)

**解决措施**

方案一：建议保持默认勾选项**Do not import settings**。

方案二：勾选**Config or installation directory**，上传配置项压缩包（settings.zip）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/3kf4VfCCRAKB14bDU_ifSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=4DF8A3C2E38DB10820401BDBB593A816DBB99DC5DC346AA6898C5E5931CFB9EE)

-   点击**File** > **Manage IDE Settings** > **Export Settings**...将包含Ark插件等配置项导出，再次运行时可以将配置项直接导入。
-   DevEco Studio版本不同，支持导出的配置项不同。可导出的配置项需以具体版本为准。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/sef0G3zfQPeTw4YkbiSzYg/zh-cn_image_0000002509067411.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=0E76F0CA931F579AE0070E13DC5D325360727B4ABEBAD17985B50188EF47AC54)
