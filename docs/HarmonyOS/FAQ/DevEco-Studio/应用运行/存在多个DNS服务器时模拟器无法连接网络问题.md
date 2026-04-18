---
title: "存在多个DNS服务器时模拟器无法连接网络问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-41"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用运行"
  - "存在多个DNS服务器时模拟器无法连接网络问题"
captured_at: "2026-04-17T02:03:24.330Z"
---

# 存在多个DNS服务器时模拟器无法连接网络问题

**问题现象**

计算机网络环境中配置了多个DNS服务器地址，HarmonyOS模拟器启动时只会选择其中一个地址用于DNS解析。当该地址无法解析某域名，但是主机备用DNS可以解析该域名时，这可能导致宿主机能够解析的域名，在模拟器中解析失败。

**解决措施**

-   Windows：打开**控制面板**，选择**网络和Internet设置** > **本地连接/查看网络状态和任务**，在活动网络中点击当前正在使用的网络 > **属性**，在弹出的对话框中找到并双击**Internet 协议版本4（TCP/IPv4）**，进入属性设置页面，选择**使用下面的DNS服务器地址**，并在DNS服务器地址栏中输入114.114.114.114。
-   Mac：打开**系统偏好****设置**，进入**网络/Wi-Fi**，点击当前使用网络的**详细信息**，修改DNS为114.114.114.114。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/yTPjMyTsTq-JyQTqJ1p46A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=49F77FCCD6F611666743384FE6359D99401ABAF48A01072B850D2D0A3F43C4A8)

114.114.114.114是中国国内广泛使用的公共DNS服务器，可用于解析大多数国内公共域名。但是需要注意的是，公共DNS可能存在隐私风险，企业环境建议使用内部DNS服务器。
