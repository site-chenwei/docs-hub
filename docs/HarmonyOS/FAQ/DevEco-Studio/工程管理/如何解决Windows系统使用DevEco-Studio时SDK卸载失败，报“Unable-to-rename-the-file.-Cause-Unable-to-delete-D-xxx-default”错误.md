---
title: "如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\\xxx\\default”错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-15"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "工程管理"
  - "如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\\xxx\\default”错误"
captured_at: "2026-04-17T02:03:20.501Z"
---

# 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\\xxx\\default”错误

**问题描述**

Windows系统使用DevEco Studio时，SDK卸载失败，提示错误信息。

Unable to rename the file. Cause: Unable to delete D:\\\\xxx\\\\default.

**解决方案**

1、启动任务管理器。

2、切换到“性能”选项卡。

3、点击下方“打开资源监视器”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/Sz5EEjSzTRGqlqJFUSFXkA/zh-cn_image_0000002194158616.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=5BE1B7C9A7F3F79B0D895B768019E7E0DAA1737D3B752E0F62D7BFF36C4EE75B)

4、将路径 D:\\xxx\\default 粘贴到关联句柄窗口右侧的搜索栏中，按回车键搜索占用的进程，然后结束该进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/MJWvW4mUTniwWw8PFAZ2pQ/zh-cn_image_0000002229758493.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=460D30408DC59CE120CE6C0C08ECF7B9A8C68F7D95655D434507B28B7BB744AB)
