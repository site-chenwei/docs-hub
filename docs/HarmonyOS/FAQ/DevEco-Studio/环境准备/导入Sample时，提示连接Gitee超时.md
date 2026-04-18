---
title: "导入Sample时，提示连接Gitee超时"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-2"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "导入Sample时，提示连接Gitee超时"
captured_at: "2026-04-17T02:03:20.101Z"
---

# 导入Sample时，提示连接Gitee超时

**问题现象**

导入Sample时，如果连接gitee.com的443端口超时，会提示“Failed to connect to gitee.com port 443: Time out”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/yn5PiLUWQIK2M6yjgReRVw/zh-cn_image_0000002229758801.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=1F866265A67A9BA984FC9FB26A3005214E1A6D83819309025608014103CE0DF6)

**解决措施**

该问题可能是由于网络受限导致的，请检查网络连接状态。如果确实受限，需要通过代理服务器访问网络，请按照以下步骤配置git代理信息。

1.  打开Git安装目录（默认为C:\\\\Program Files\\\\Git），双击运行“git-cmd.exe”文件。
2.  在打开的命令行窗口中，执行以下命令配置代理服务器信息（将proxyUsername、proxyPassword、proxyServer和port按照实际代理服务器进行修改）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/YIE44JJ1SlmoEUATFI65VA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=E6E7A405B3241390CB8A99B582428F63BFE409E4AA8044744D219285B6D0C226)
    
    如果密码中包含特殊字符，如 @、#、\* 等，可能导致配置不生效。建议将这些特殊字符替换为 ASCII 码，并在 ASCII 码前加百分号 %。常用符号替换为 ASCII 码的对照表如下：
    
    -   !：%21
    -   @：%40
    -   #：%23
    -   $：%24
    -   &：%26
    -   \*：%2A
    
    ```powershell
    git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
    ```
    
3.  执行完成后，请重新尝试导入Sample。
