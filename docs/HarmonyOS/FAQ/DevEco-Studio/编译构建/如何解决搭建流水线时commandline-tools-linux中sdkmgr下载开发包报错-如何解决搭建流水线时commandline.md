---
title: "如何解决搭建流水线时commandline"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-76"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错"
captured_at: "2026-04-17T02:03:21.994Z"
---

# 如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错

**问**

使用 commandline-tools 工具在 Linux 上时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”，请检查网络连接是否正常，确保可以访问该 URL。如果网络无问题，尝试更新 commandline-tools到最新版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/AIBtV4PYQayAJXBjYXCR5A/zh-cn_image_0000002229603881.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=79172D388E08013E1A674598A5D710B5F6AC8F61B536998E0576867D34D15291 "点击放大")

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区所致。

请参考以下方法解决：

1.  进入sdkmgr脚本所在的文件夹：${命令行工具根目录}/sdkmanager/bin。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/FuC_rMDyRQi0Aj1n_vt0Jw/zh-cn_image_0000002194158460.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=EF1E1B010173E88806DDCC5806C1757E40BC7361937D085746CAF71027669D4F "点击放大")
    
2.  打开sdkmgr文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/fi8lcbotSbaNOswJ3FIXng/zh-cn_image_0000002229603849.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=F419E3459E8D8245B383D9489125B82E8F86FF284825E7E146ADA9CB4810A3F0 "点击放大")
    
3.  在文件的最后一行，-Dfile.encoding=UTF-8 后面添加 -Duser.country=CN。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/xxBqhDnmQXmWBH33IqsraQ/zh-cn_image_0000002194318088.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=47ECE380688D5A0AC5979248BD496D5DDBB547BD0202AB53A26EFBC8D3BC60E7 "点击放大")
    
4.  保存修改，再次执行sdkmgr相关命令即可。
