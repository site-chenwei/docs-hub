---
title: "流水线场景使用命令行工具sdkmgr下载Linux SDK失败"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-11"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "流水线场景使用命令行工具sdkmgr下载Linux SDK失败"
captured_at: "2026-04-17T02:03:20.220Z"
---

# 流水线场景使用命令行工具sdkmgr下载Linux SDK失败

**问题现象**

在Linux上使用命令行工具sdkmgr时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/lZ8u6u8GQbyQg9T7xiVNsw/zh-cn_image_0000002194158336.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=74D397FD548ABE91DE95D19DDA0D3053EAC166BC6B4918590AE7C76B923E3CD7)

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区。

1.  进入sdkmgr所在的目录。
    
    ```powershell
    cd ${命令行工具根目录}/sdkmanager/bin
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/7lw5E__OQ_29HSqFPlapZQ/zh-cn_image_0000002229603729.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=69E9C2FBF01A1941288A1CA871D92306152E037382E60591F7A9B9324B2385ED)
    
2.  打开sdkmgr文件。
    
    ```powershell
    vim sdkmgr
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/B5FOIDZDSzGHGDRV9cMvzQ/zh-cn_image_0000002229758205.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=6414D2FFBAEC36D5A482C79E723443DB47344CE64E9CBC9FA28F9F366E423984)
    
3.  在sdkmgr文件的最后一行“-Dfile.encoding=UTF-8”后添加国家码“-Duser.country=CN”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/k02nBiQuTsC03gPM2ZxHbg/zh-cn_image_0000002194317952.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=BEF4E6642EDEE927C7EB36259C1EB4F0D15D4DB7067702CEEC1336663566BFAB)
    
4.  ​保存修改后，再次执行sdkmgr相关命令即可正常下载Linux SDK。
