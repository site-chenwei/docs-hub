---
title: "Windows电脑上启动模拟器，提示可申请内存不足"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-39"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用运行"
  - "Windows电脑上启动模拟器，提示可申请内存不足"
captured_at: "2026-04-17T02:03:24.278Z"
---

# Windows电脑上启动模拟器，提示可申请内存不足

**问题现象**

启动模拟器时，如果系统提示“当前可申请的内存不足”，表示Windows电脑内存不足。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/RZsaCRuoSbi6QRAyxcSG_A/zh-cn_image_0000002229604313.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=1B8506E7D99E70D55588DBC095AB8A4E9BF2FCD34126239D9A2FB52FE4D9B07F)

**解决措施**

1.  打开任务管理器的详细信息页面，在列表表头右键选择列，勾选“提交大小”，然后点击“提交大小”列进行排序，关闭提交大小占用高的进程。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/LfSCe1-LSj-8l24qRBqztQ/zh-cn_image_0000002229758817.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=DAC884D4F9EBCCDC2C8D469CEBD19648AC20DF53DB13040A0BCEF92D87501C13 "点击放大")
    
2.  打开任务管理器的性能和内存页面，确保已提交内存的剩余量大于模拟器设置的RAM大小。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/9pZTrywVR_mMcfHLGnzdVQ/zh-cn_image_0000002194158932.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=E24A9258D36072E089E18E838BCACF5D9D8366873E256BF4F231EF96101309DA)
