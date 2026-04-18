---
title: "导入Sample时，提示SSL证书校验错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-3"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "导入Sample时，提示SSL证书校验错误"
captured_at: "2026-04-17T02:03:20.133Z"
---

# 导入Sample时，提示SSL证书校验错误

**问题现象**

导入Sample时，导入失败，提示“SSL certificate problem: unable to get local issuer certificate”证书校验错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ooKDzcl7ROqKyZajxHcYeg/zh-cn_image_0000002194318052.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=2008D25F0A4B1EA8BD76AF76866AAAD0DB35DE435C5F09F040616F0D60AC4D48)

**解决措施**

出现这个错误可能是网络遭受了攻击，或者你的网络提供方网络策略阻止了相关操作，如果你确认所处的网络环境安全，可以临时关闭证书校验以获取Sample。

1.  进入Git安装目录（默认为C:\\Program Files\\Git），双击运行“git-cmd.exe”文件。
2.  在打开的命令行窗口中，执行如下命令关闭SSL证书校验功能。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/PxzI-g1hQjSvuOXcsZZe1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=729886621C915B03C37B5D92528FDDFF1E07FFDA304C6BAB845583A86961F23F)
    
    关闭SSL证书校验，可能会带来安全风险，建议导入完Sample后，及时开启。开启方法：将该命令中的false修改为true即可。
    
    ```powershell
    git config --global http.sslVerify false
    ```
    
3.  执行完成后，请重新尝试导入Sample。
