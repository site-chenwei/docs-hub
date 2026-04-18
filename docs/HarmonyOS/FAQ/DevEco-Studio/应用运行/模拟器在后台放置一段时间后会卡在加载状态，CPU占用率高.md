---
title: "模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用运行"
  - "模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高"
captured_at: "2026-04-17T02:03:23.995Z"
---

# 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/mxUS0Xc9RraqAiO04VEv6w/zh-cn_image_0000002229603801.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=CECD9D67D45C91078A2C863E8B537F0BAAA387930A4DC0C1770C49DED9058DB7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/l7oQJzMKRWW8OTVXyoi9uQ/zh-cn_image_0000002194318016.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=EB829B9652B4A1BBE4445D352EE5E398C6779474EC475AE2183106D09C5541A7)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/d_emXZ8iTS261PNih0xtHA/zh-cn_image_0000002229603789.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=89A54A26351ED668545236A9836EB74FD1BE45DBE5C339D13EAED390ED0BB322)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/FX48mmbES1W0PB9pic-exA/zh-cn_image_0000002194158400.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=214DAAA65CDBBF608D2BC2E76ACD5B3C821D2339E7404A370ABA848D04225A47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/68hagD57SjqPE6uIxnYAsg/zh-cn_image_0000002229758273.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=E389190CC0AB2764F203A5A0EB7FB564A4D14C053BB9FCE8F597B36C1CF08ACD)

3.复制路径并用文件夹打开system-image\\HarmonyOS-NEXT-DB1\\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/F_U0sxUES4a_X7Slxm9dkQ/zh-cn_image_0000002229758269.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=CF4740569984A9E4D3F6C9730BA55D1CB944884BE883A5498D64888B7D0D51A6)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/2RGjlQTpT3yk9imXWo06Pg/zh-cn_image_0000002194158396.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=CC8CCB314D8BF6E671B3379BE8A5C40E2D460F5EC688AB37AD143FEEABA6473A)
