---
title: "应用自动签名失败，提示“calibrate the system time and sign again”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-29"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "应用自动签名失败，提示“calibrate the system time and sign again”"
captured_at: "2026-04-17T02:03:24.691Z"
---

# 应用自动签名失败，提示“calibrate the system time and sign again”

**问题现象**

应用在进行自动签名时，签名失败，提示“The signature does not take effect or has expired. The current system time may be inaccurate. Please calibrate the system time and sign again.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/drAPcGHkTaSSiXIt2RFDxw/zh-cn_image_0000002229758773.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=6618103BAF71AC4C62C8E6D1FDF97BDE0D34860D08E0BD6BBF04D8AF0F2A27C5 "点击放大")

**解决措施**

出现报错是因为电脑的系统时间与北京时间不一致。请在系统设置中将时间设置为北京时间。

Windows：

1.  在开始菜单中搜索并打开“控制面板”。
2.  点击“时钟和区域”> “日期和时间”。
3.  在弹出的窗口中点击“更改日期和时间”。
4.  修改后点击“确定”保存。

macOS：

1.  在桌面点击左上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/DSA5XfdtRtaprBBg2D1keg/zh-cn_image_0000002347874002.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=875C6C86D0B32480483F59B0894D1CCA29E6044A8CECA51C8D625CB66337D6C0 "点击放大")菜单，选择“系统设置”。
2.  在侧边栏点击“通用”> “日期与时间”。
3.  点击时间旁边的“设置”按钮，手动输入日期和时间。

如果您使用的是公司或学校管理的设备，可能会受到MDM（移动设备管理）限制，无法更改时间设置，这种情况下需要联系公司或学校的IT管理员。
