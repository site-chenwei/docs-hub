---
title: "Native调试无法与lldb"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-34"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "Native调试无法与lldb-server连接"
captured_at: "2026-04-17T02:03:24.729Z"
---

# Native调试无法与lldb-server连接

**问题现象：**Native调试长时间没有启动，最后DevEco Studio超时报错"Attach request timeout after 600000 milliseconds"或Native调试启动后报错"Failed to connect port"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/C1e5wuobSMSKPKzmuR8fNQ/zh-cn_image_0000002229758601.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=BA728BADB91D71EF3B960CB19EF362F1B7D6A22AD7ED86BB68E77E93E478903E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/XKfuBYW1Rma_T6aejpETzA/zh-cn_image_0000002194318340.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=EB91AF8FA4FB165D8953C3340C6FC83AD57B4F7CB4C175E36D670CFDEC01B266)

**可能原因：**

linux或MacOS 下 /etc/hosts文件被修改。

**解决措施：**

1.  在/etc/hosts文件后添加如下内容：
    
    ```text
    127.0.0.1 localhost
    255.255.255.255 broadcasthost
    ::1 localhost
    ```
    
2.  重启电脑使修改生效。
