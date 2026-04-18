---
title: "使用模拟器发起HTTPS请求时如何安装数字证书"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-27"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用运行"
  - "使用模拟器发起HTTPS请求时如何安装数字证书"
captured_at: "2026-04-17T02:03:24.103Z"
---

# 使用模拟器发起HTTPS请求时如何安装数字证书

**问题现象**

在使用网络代理发送HTTPS请求时，需要安装网站服务器的数字证书。

**解决措施**

1.  将证书拖拽上传至模拟器，可在文件管理的“我的手机”>“下载”目录下查看上传的文件。
2.  安装证书的方式如下：
    -   点击**设置 > WLAN >**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/71lBwGCGRFKj-KVXC4kkCQ/zh-cn_image_0000002395407910.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=840B1563E20AC9BEE0A27D49A08FA6539733E3B582CE8375AB212353A8E76411)**\> 安装证书 > CA证书**，选择pem格式证书进行安装。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Hvc2yzSdRq6vNqSv5bti3Q/zh-cn_image_0000002229758177.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=1120FA40E48A52D9637573EA8BAE0189A4E504A592BF60BCC17E03A2731966C5) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/65rp0AiWSnWTMQAaJnGiug/zh-cn_image_0000002194317924.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=BB7CDEB1B7FD017150571240668D7C04A80C1E0B2832D3ABFAA6C3FF9F901622)
        
    -   在本机命令行窗口中使用以下命令打开证书管理。
        
        ```powershell
        hdc shell aa start -a MainAbility -b com.ohos.certmanager
        ```
        
        选择从存储设备安装，安装pem格式的证书。
