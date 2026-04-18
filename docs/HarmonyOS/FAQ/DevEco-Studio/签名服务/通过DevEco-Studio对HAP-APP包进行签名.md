---
title: "通过DevEco Studio对HAP/APP包进行签名"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-17"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "签名服务"
  - "通过DevEco Studio对HAP/APP包进行签名"
captured_at: "2026-04-17T02:03:23.791Z"
---

# 通过DevEco Studio对HAP/APP包进行签名

通过DevEco Studio自带的签名工具，可以对已打包的HAP/APP包进行签名，具体步骤如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Sq9H9IvOSw6pZnzmBqVZ4Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=6C861F1C3677535108565A513AF1F82AE56B2C5D7D8F8C134D962E93C958AA82)

建议使用DevEco Studio 6.0.2 Beta1及以上的版本。

1.  通过DevEco Studio生成密钥和证书请求文件，并向AppGallery Connect申请发布证书和Profile文件，具体请参考[准备签名文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app#section793484619307)。
2.  准备好签名工具hap\_sign\_tool.jar，在${DevEco Studio安装目录}/sdk/default/openharmony/toolchains/lib下。
3.  在签名工具目录下，使用如下命令进行签名。详细的签名工具指导请参考[应用包签名工具](https://gitcode.com/openharmony/developtools_hapsigner)。
    
    ```powershell
    java -jar hap-sign-tool.jar sign-app -keyAlias "demo_key" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "D:\demo.cer" -profileFile "D:\demo.p7b" -inFile "D:\hap-unsigned.hap" -keystoreFile "D:\demo.p12" -outFile "D:\hap-signed.hap" -keyPwd "123456Abc" -keystorePwd "123456Abc"
    ```
    
    关于该命令中需要修改的参数说明如下，其余参数不需要修改：
    
    -   **keyAlias**：密钥别名。
    -   **appCertFile**：申请的发布证书文件，格式为.cer。
    -   **profileFile**：申请的发布Profile文件，格式为.p7b。
    -   **inFile**：通过Hvigor打包生成的未携带签名信息的HAP。
    -   **keystoreFile**：密钥库文件，格式为.p12。
    -   **outFile**：经过签名后生成的携带签名信息的HAP。
    -   **keyPwd**：密钥密码。
    -   **keystorePwd**：密钥库密码。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/F9iGbaw-Tja7Q21hsVhpTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=64DFC9B53DB40108DBAB6AF26861D69F6F37381A04EFB9C0203F22D68DF2FAC5)
    
    如果要对APP进行签名，只需将**inFile**和**outFile**参数修改为APP包即可。
