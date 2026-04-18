---
title: "开通Device Security服务"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Device Security Kit（设备安全服务）"
  - "开发准备"
  - "开通Device Security服务"
captured_at: "2026-04-17T01:35:49.795Z"
---

# 开通Device Security服务

在开通Device Security服务前，请先参考“[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)”完成基本准备工作，再继续进行以下开发活动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/V_QFx9uORnGXiXHSROBNXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=F257A0DA8D746DC5358F5062708972DB89688BD2F1BCF66483A69C8BAD6CD03E)

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测能力、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1.  登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/bBqPf4hvQliEanBHc5KiGw/zh-cn_image_0000002569019021.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=271C824CE021317FCF461E11D89AE47604FAE0E5CAB74872DE9EF54C135CF183)
    
2.  在项目列表中找到需要开通Device Security服务的项目。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/b-FFQNnATNW4EPWKt9SDnw/zh-cn_image_0000002568899013.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=7B9AE8A966094BFEEE5C89F508788543BBA9B01887C5971E8AE09145D58E2EBC)
    
3.  选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。
    
    -   **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/QIVOk8WySIW6oOwBgsVwBQ/zh-cn_image_0000002538019308.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=6C69D6E33570B7D83F33CC2DA7311DAC4E5114E6D065BC7C5F192D48C35C67B5)
        
    -   **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/w7SP5QG-S1yoKseQ0rdX7g/zh-cn_image_0000002538179238.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=E02CA4DE91A1430B9938CBF74B4498380B090B9BB1E58C02DEDA9BE25A36E96D)
        
    -   **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/AVRbi1xNQVa7ow0ezXgAvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=2D49932309D81C13CA9FB3676D31A0F28A1FA6266D95C35FA828BFF4C567F53D)
        
        开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/oNhugnGWS16ojlZ3lGF1Yg/zh-cn_image_0000002569019025.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=E99C19194D4773ADC1B8EE188ED3EC1B19E75149CCEC5B8573CCD2870422DC0C)
        
    -   **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。
        
        ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)。
        
        ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/39euM1YLStGvkjGFfum6GQ/zh-cn_image_0000002568899017.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=98615E5B24DAF87EC15FB18DAF196001ED82B7277CCCFCFBA6367C6609D9CE62)
        
        ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、使用场景、使用该服务的合法基础（应用使用该服务时需在其隐私声明中进行个人数据声明及用途说明，详细参考[个人数据处理说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-personal-data)，并将合法基础的相关证明上传至申请附件），然后点击“提交”按钮。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/8u9tLVXRR_isgK9bCZbsQQ/zh-cn_image_0000002538019312.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=DE2B7CB737411B915185AFAC3F55D690333CB303111D8945B6571DB090DAAB14)
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/ImVwL_Q7QvuLjg8CdLZvDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=92C2D482ABC4410A8A050F64AA2D9430BA98B75F333CA8C4CC7D90D1B69DD08A)
        
        提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
        
    -   **数字盾服务**：点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。
        
        ① 在申请“数字盾服务”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)。
        
        ② 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/zpgtDmokRWyxHeIVAWFWRw/zh-cn_image_0000002538179240.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=6E698CF6CBD0D35B987A1B5D11FFF0B1185FB170855C309AEE7B841D40E89D09)
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/DFs_WjKoRaK7OS9j6kuMrA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=381AADDECE3C810DAF0B00B54E4CDCD0B772BBA261BE0B2AC67BCA272007CD78)
        
        请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
        
4.  申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/y9CLnpXeQ4eXL4PSeQCbMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013551Z&HW-CC-Expire=86400&HW-CC-Sign=A214CDA810B0F1722E36ECB84BD89D29010F5A7183766CD996BE6E142E0C8BAC)
    
    在开通服务后，需要重新申请Profile（.p7b）文件。
