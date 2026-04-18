---
title: "导入Sample工程"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-sample"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "导入Sample工程"
captured_at: "2026-04-17T01:36:43.772Z"
---

# 导入Sample工程

DevEco Studio支持Sample工程的导入功能，通过对接Gitee开源社区中的Sample资源，可一键导入Sample工程到DevEco Studio中。下面介绍导入Sample的方法。

#### 约束与限制

#### \[h2\]支持的国家/地区

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

#### 操作步骤

1.  在DevEco Studio的欢迎页，进入**Customize** **> All Settings... > Version Control > Git**界面，单击**Test**按钮检测是否安装Git工具。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/mgPnwcZsQVuRtyK1p1OEgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=957C77AF96715EE360D552C8EEB54CFBDBA62FB5F3E047F9E521E68F5A86EE77)
    
    在打开工程的情况下，可以单击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）进入设置界面。
    
    -   已安装，请根据[2](#li1599692216194)开始导入Sample。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/IZBe7WC2SvmWF1fw35QzHg/zh-cn_image_0000002530913250.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=48CA6F9378A748B8E777E702420D3ADEAC4AEE4A04B910C1D5EE524ACC972987)
        
    -   未安装，请单击**Download and Install**，DevEco Studio会自动下载并安装。安装完成后，请根据[2](#li1599692216194)开始导入Sample。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/9E-G82iiT7K-affgLHxuKA/zh-cn_image_0000002530753254.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=483024ACB6F876CC5633602E012AB1A7F37FA2DCAB4268A9CF267C5E27FDE3FC)
        
    
2.  在DevEco Studio的欢迎页，在**Projects**页签下，单击**M****ore Action >** **Import Sample**按钮，导入Sample工程。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/BHAXtr3RTJe_q9FhYs1d-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=379A3A660C43ECD53D32F5FC88EA035A1018E942E1A8CDB5ECECF1BEC0B146EB)
    
    在打开工程的情况下，可以单击**File > New > Import > Import Sample**来进行导入。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/3mlT4EnnQSacNLQ18CvpqA/zh-cn_image_0000002530753260.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=A93E5DF778BCD60A7AE724120A8C6A0BD4E1DE4346BF748054C929DEA1FEA681)
    
3.  选择需要导入的Sample工程，然后单击**Next**。
4.  设置**Project name**和**Project location**，然后单击**Finish**，等待Sample工程导入完成。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/LrrMTm1qRJy-8ZPW0EJxMQ/zh-cn_image_0000002532477844.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=C46639DF62257A09BA7E28F4954E2D477EA02D04E95EEE864D7E01DE397AF2DB)
    
5.  导入Sample后，等待工程同步完成即可。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Z7nHr9z1SD-JQs9X3dqCMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=DEB89DCAA6C0FFEBED1FF7DA08676654DD4B84BEA85A99D37F47CA23588E8ABB)
    
    如果网络受限，导入时会提示“Failed to connect to gitee.com port 443: Time out”连接超时错误，请[配置Git代理信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-2)。
