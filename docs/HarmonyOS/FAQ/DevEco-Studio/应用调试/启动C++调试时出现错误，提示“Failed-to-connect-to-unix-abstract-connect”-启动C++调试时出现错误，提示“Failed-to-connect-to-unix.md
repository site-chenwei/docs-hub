---
title: "启动C++调试时出现错误，提示“Failed to connect to unix"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-25"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect”"
captured_at: "2026-04-17T02:03:24.633Z"
---

# 启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect”

**问题现象**

启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect://\\\*\\\*\\\*\\\*\\\*\\\*\\\*\\\*\\\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/G5HTZGx5STu5eWRmI5p-lQ/zh-cn_image_0000002194158920.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=E34A34642A171B309F5D41DD46FE9CC68111A4C2CA7C262502E9637899A89A83)

**解决措施**

1.  如果设备镜像与DevEco Studio版本不匹配，请尝试更换设备镜像版本以解决问题。
2.  签名使用了release证书，请更换为debug证书。
3.  到设备路径 /data/local/tmp/debugserver/ 下，删除与应用包名相同的文件夹。
