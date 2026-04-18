---
title: "签名密钥库文件与JDK版本不兼容"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-12"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "签名服务"
  - "签名密钥库文件与JDK版本不兼容"
captured_at: "2026-04-17T02:03:23.712Z"
---

# 签名密钥库文件与JDK版本不兼容

**问题现象**

打包签名提示“**init keystore failed : parseAlgParameters failed:ObjectIdentifier()**”错误。

**可能原因**

使用高版本JDK生成签名密钥库文件，使用低版本的JDK执行签名，因为兼容性问题无法解析签名密钥库文件，导致签名失败。

**常见错误场景**

1.  DevEco Studio自动生成签名密钥库文件（\*.p12），使用DevEco Studio预置的JDK，用户使用本地的低版本JDK进行签名，导致签名失败。
2.  用户使用本地高版本JDK生成签名密钥库文件（\*.p12），使用DevEco Studio进行打包签名，DevEco Studio中预置的JDK版本低于用户的JDK，导致签名失败。

**解决措施**

请检查当前使用的JDK版本和生成签名证书文件使用的JDK版本，确保JDK版本一致，JDK版本信息查看方法如下：

1.  查看DevEco Studio预置的JDK版本信息，DevEco Studio Terminal窗口执行java -version命令，当前示例DevEco Studio预置的JDK版本为21.0.6。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/4n0zT6gXRA6refRa4c3mlA/zh-cn_image_0000002422340574.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=7F38A651C931F53E2D0B53912DF7E9ABA6633C88FC3AFF0D29536B172D2ED3FB)
    
2.  查看本地系统JDK版本信息，CMD窗口执行java -version命令，当前示例本地系统JDK版本为1.8.0\_292，与步骤1示例中DevEco Studio预置的JDK版本不一致。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/QZAGVKbIQ265CaAT1lxZhw/zh-cn_image_0000002342518430.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=3FB8FE882A445A16128C28BDC7E2FC512F29C994541728A84E3507FBFB11B1BF)
