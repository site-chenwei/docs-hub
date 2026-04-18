---
title: "2in1设备attach调试失败和增量调试失败"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-63"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "2in1设备attach调试失败和增量调试失败"
captured_at: "2026-04-17T02:03:24.837Z"
---

# 2in1设备attach调试失败和增量调试失败

**问题现象**

1、2in1设备应用调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/-hn4YFmaRsO6Jo9sgdzRLQ/zh-cn_image_0000002557414329.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=F274CD104B7C2143CAC1159AFB903CC8BDAACD361E678B54E459B16120266127)

2、2in1设备应用使用增量调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/bXg-m4d3SvGIhgLw15jXqQ/zh-cn_image_0000002526214500.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=6E9A4CD519E06635F280187E595B2F7AEBFDB7C39F2219958A1BBAD3317D5895)

**解决措施**

2in1设备报上述错误可能原因是应用开启了应用加速服务功能，请在设备的**设置 > 应用加速服务**中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/ahkeVIgKQpSKlaKcOImiKA/zh-cn_image_0000002557334361.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=9658B659731682A8261A0057BC46D0AE16DEC9525AFB1904287F8EE82EA28ED5)
