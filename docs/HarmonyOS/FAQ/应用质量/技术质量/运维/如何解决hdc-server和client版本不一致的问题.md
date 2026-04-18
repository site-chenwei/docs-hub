---
title: "如何解决hdc server和client版本不一致的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-38"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何解决hdc server和client版本不一致的问题"
captured_at: "2026-04-17T02:02:57.364Z"
---

# 如何解决hdc server和client版本不一致的问题

**问题现象**

hdc.log 中的报错信息为“Daemon Session Handshake failed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/MwZJXs64RTWxok5GnkWvkw/zh-cn_image_0000002194318252.png?HW-CC-KV=V1&HW-CC-Date=20260417T020258Z&HW-CC-Expire=86400&HW-CC-Sign=C4DBFEC0439E4D069F39A16EC7D84B06BF26DD7ABEB51C588DD69E9D56C54F80 "点击放大")

**解决措施**

1.  通过以下命令检查server和client的版本是否匹配。
    
    hdc checkserver
    
2.  执行以下命令，终止其他版本的服务器。
    
    hdc kill
