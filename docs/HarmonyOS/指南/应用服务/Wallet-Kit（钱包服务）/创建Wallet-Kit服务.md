---
title: "创建Wallet Kit服务"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-preparations"
menu_path:
  - "指南"
  - "应用服务"
  - "Wallet Kit（钱包服务）"
  - "创建Wallet Kit服务"
captured_at: "2026-04-17T01:36:23.198Z"
---

# 创建Wallet Kit服务

请先参考“[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)”完成基本准备工作和指纹配置，再继续以下开发活动。

1.  登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“我的项目”。
    
2.  点击进入对应的项目，在左侧“项目设置”页签，上侧导航选择“开放能力管理”，打开华为钱包的开关。用于钱包对车钥匙管理台向钱包服务器发起http/https请求时的权限控制。关闭状态下，开发者服务器将访问不了钱包服务器。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/dhFBthmuS-OMP_HT7qGOyQ/zh-cn_image_0000002538020138.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=1956510418A883192B0D0B90709E1607D1054EBDCE6D4AAE6551632C4741AC43)
    
3.  在“项目设置”页签，左侧导航选择“盈利 > 华为钱包”，点击“申请Wallet Kit服务”，进入申请Wallet Kit服务。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Usape7J4RV-P687yiLmBRA/zh-cn_image_0000002538180066.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=2851855B2C903FFEBF50B9DA753E71D57D8D0F026A82E98B6C9F06DEB5DAED9F)
    
4.  点击“产品接入华为钱包服务”的“点击申请”按钮。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/L5L8KrwbSSC3BzkCZnEprA/zh-cn_image_0000002569019853.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=5E9AA7A9876A70DF1986A4D56DD984DDCC77E353D64D96938CAAE9F993201E24)
    
5.  各业务场景对应的参数有差异，具体参数请参考各业务的Wallet Kit服务基本信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/WywvQ15NSgOECwbodICjVQ/zh-cn_image_0000002568899845.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=45821F6C4CE94BFE5AFA0BA4F66D016F7EC0FEC789BBD5D5CACA2F5102C09B0D)
    
    | Wallet Kit服务参数名称 | 参数值 |
    | :-- | :-- |
    | 服务类型 | 分为卡、票、券、钥匙等，暂时只支持车钥匙，交通卡服务接入请参考[接入交通卡](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transport-overview)。 |
    | 服务项目 | 服务项目依赖所选择的服务类型，不同的服务类型，有不同的服务项目。例如当服务类型选择“卡”时，对应的服务项目有：“会员卡”、“礼品卡”等。 |
    | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。 |
    | 服务号 | 用于Wallet Kit服务器区分不同的服务且保证唯一性。 |
    | 接入方式 | 国内支持三种接入方式，App接入，云端接入，代理接入。商户可以根据自己的需求选择适合自己类型的接入方式。选择云端接入时用户需要填写“回调地址”、“用户公钥”二项资料，选择App接入则只需要上传证书请求文件生成证书即可，选择代理接入时用户需要填写“回调地址”一项资料，而用户公钥则会发送默认值到Wallet Kit服务器。 |
    | 回调地址 | 
    开发者提供给Wallet Kit的地址，用于Wallet Kit回调开发者，用户领卡成功或删卡时回调开发者。
    
    注：如果不需要Wallet Kit通知开发者用户领卡或删卡的状态，可以不填该字段。
    
     |
    | 用户公钥 | 开发者将生成的公钥复制粘贴到此处，后续该公钥将作为Wallet Kit服务器认证开发者身份的方式，参考如下公钥生成方式。 |
    
    **公钥生成方式：**
    
    （1）配置好node执行环境并使用文本编辑器新建文件，拷贝以下代码到文件中并保存命名为generateKeyPair.js。
    
    ```typescript
    const crypto = require('crypto');
    // 生成密钥对
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
      modulusLength: 4096, // 密钥长度，不少于4096
      publicKeyEncoding: {
        type: 'spki', // 公钥编码格式
        format: 'der' // 公钥输出格式
      },
      privateKeyEncoding: {
        type: 'pkcs8', // 私钥编码格式
        format: 'der' // 私钥输出格式
      }
    });
    console.info('生成的公钥：');
    console.info(publicKey.toString('base64'));
    console.info('生成的私钥：');
    console.info(privateKey.toString('base64'));
    ```
    
    （2）打开命令行工具，执行**node generateKeyPair.js**命令。
    
    （3）从结果中拷贝生成的公私钥并保存。结果如下图所示：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/--A_TPhKR4itRMhPCdyiMQ/zh-cn_image_0000002538020140.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=4FCD124CEC5D43E776A733D1E98415ADEE285094B50944C36858E08D63F197E9)
    
6.  点击“下一步”，进入NFC参数设置页面，各业务场景对应的参数有差异，具体参数请参考各业务的NFC参数。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/vEmbbvpqSdWhwCzBTY2Rrg/zh-cn_image_0000002538180068.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=108FB5CB94C89822C8E994BC870A5B81ACA6BF407FFA155A4B1F5F1CA2170ED2)
    
    | NFC参数名称 | 参数值 |
    | :-- | :-- |
    | 是否支持跨移动设备同步 | 用户领取卡券后可通过此能力在同一账号下的多设备中共享此卡券。商户默认选择“否”即可。 |
    | 是否开通NFC能力 | 服务类型为门钥匙、一卡通、门禁卡、社会保障卡、港澳通行证、护照时，需要开通NFC能力，同时需要配置应用号和文件参数。其余的服务类型可以选择不开通NFC能力。 |
    | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位），建议以“A000000048575041590100”开头。 |
    | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
    | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
    
7.  点击“下一步”，创建完成后，返回Wallet Kit服务创建页面，可对所创建的服务进行查看、修改和删除。
