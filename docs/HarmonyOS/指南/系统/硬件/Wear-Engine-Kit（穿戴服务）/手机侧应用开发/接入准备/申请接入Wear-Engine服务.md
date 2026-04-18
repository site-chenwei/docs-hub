---
title: "申请接入Wear Engine服务"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_apply"
menu_path:
  - "指南"
  - "系统"
  - "硬件"
  - "Wear Engine Kit（穿戴服务）"
  - "手机侧应用开发"
  - "接入准备"
  - "申请接入Wear Engine服务"
captured_at: "2026-04-17T01:35:59.615Z"
---

# 申请接入Wear Engine服务

申请Wear Engine服务前，请先参考[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)（开发者需实名认证为个人开发者或者企业开发者，认证前，请先了解二者的[权益区别](https://developer.huawei.com/consumer/cn/doc/start/dbiae-0000001336403980)），确认开发环境并完成创建项目、创建HarmonyOS应用等基本准备工作，再继续进行以下开发活动。

1.  进入华为开发者联盟的“管理中心”，点击“[应用服务](https://developer.huawei.com/consumer/cn/console/service/AppService)”页签下的“Wear Engine”卡片。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/5LUfxH5DR3evl8_qG8YZpw/zh-cn_image_0000002568899137.png?HW-CC-KV=V1&HW-CC-Date=20260417T013559Z&HW-CC-Expire=86400&HW-CC-Sign=9E678E1909DB6956D6D4F3187A72A28B71F64F2ED34DA143BCB233374274F154)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/EfjLUG9kSyWdeUixDAPqvQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013559Z&HW-CC-Expire=86400&HW-CC-Sign=268207BD5FD120855A882566BEE066364D38A63C1A74F7C88B65A19C082787DA)
    
    如果无“Wear Engine”卡片，请点击右上角“自定义桌面”添加卡片。
    
2.  点击“申请Wear Engine服务”，同意协议后，进入权限申请页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/yxnepbDZTi-0rbLwQxp4ew/zh-cn_image_0000002538019432.png?HW-CC-KV=V1&HW-CC-Date=20260417T013559Z&HW-CC-Expire=86400&HW-CC-Sign=B1DAD729DCC8085D5793F0154B21D0FE1657293B75B660AE306BB7C32B182001)
    
3.  点击“HarmonyOS应用”并选择产品后，勾选必需申请的权限（个人开发者当前只可申请设备基础信息、消息通知两个基本的权限）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/fd0dzujUTtKoH0rr2_HMdA/zh-cn_image_0000002538179360.png?HW-CC-KV=V1&HW-CC-Date=20260417T013559Z&HW-CC-Expire=86400&HW-CC-Sign=5C23F53314677B749FB52DC61226447DB606E2D23F2AA6E0E63281ECCF402C5D)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/j7kQL6EqT4O602eL8X9yFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013559Z&HW-CC-Expire=86400&HW-CC-Sign=FB2787C99681C32E101BB448ABDE1DD2FAECA1B511F8E8CF9AD1F22313E81B36)
    
    -   如选中兼容按钮，通信会将本地包名和指纹转换为兼容应用在云端存储的包名和指纹。
        
    -   若选择需要兼容与旧版本穿戴应用通信的手机移动应用，则需填写归属于同账户下的**待兼容应用**与**待兼容应用包名**。
        
    -   人体传感器相关权限受限开放，仅限专业研究机构使用。如未提前与华为确认，请勿申请该权限。
        
    -   设备标识符权限受限开放，仅限专业合作企业使用。如未提前与华为确认，请勿申请该权限。
        
    
    **权限和设备能力类：**
    
    **设备基础信息**（权限）
    
    -   穿戴设备状态管理
        -   穿戴设备基础信息查询：获取已配对穿戴设备列表并选定设备；支持查询穿戴设备可用空间。
        -   穿戴设备基础信息查询：支持查询电量状态；订阅低电量告警；查询或订阅穿戴设备连接状态、设备模式、充电状态。
    -   通信能力管理
        -   发送点对点消息/文件：手机侧“xxx(应用名)”向穿戴设备侧“xxx(应用名)”发送消息/文件。
        -   接收点对点消息/文件：手机侧“xxx(应用名)”接收穿戴设备侧“xxx(应用名)”消息/文件。
    
    **消息通知**（权限）
    
    -   消息通知能力管理
        -   向穿戴设备侧发送通知：手机侧应用向穿戴设备发送通知，并在穿戴设备上按模板显示；支持设置消息标题、内容、按钮。
    
    **穿戴用户状态[USER\_STATUS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api#permission)** （权限）
    
    -   穿戴用户状态管理
        -   查询和订阅用户佩戴状态和订阅用户心率告警。
    
    **人体传感器[HEALTH\_SENSOR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api#permission)** （权限）
    
    -   人体传感器
        -   获取穿戴设备侧支持的传感器信息列表。
        -   读取穿戴设备ECG、PPG、HR传感器数据。
        -   停止读取穿戴设备侧人体传感器。
    
    **运动传感器[MOTION\_SENSOR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api#permission)** （权限）
    
    -   运动传感器
        -   获取穿戴设备侧支持的传感器信息列表。
        -   读取穿戴设备ACC、GYRO、MAG传感器数据。
        -   停止读取穿戴设备侧运动传感器。
    
    **设备标识符[DEVICE\_IDENTIFIER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api#permission)** （权限）
    
    -   设备标识符
        -   获取设备序列号：获取已连接穿戴设备序列号。
4.  上传申请数据权限及使用说明、用户授权路径说明，选择授权入口是否展示华为品牌LOGO后提交。
    
    **申请数据权限及使用说明**
    
    -   权限：提供申请的数据权限，每个权限一行。
    -   数据使用：供使用数据权限的需求、场景、目的和方式等。
    -   数据展示路径：供所申请权限的使用场景的界面截图。可选。
    
    **用户授权路径说明**
    
    -   提供获取用户授权的界面截图及界面操作路径的文字描述。
    -   如果应用内提供了修改授权的功能，请提供修改授权的界面截图及界面操作路径的文字描述。可选。
5.  等待申请通过。
    
    权限审批一般需要1到2周，具体时间取决于申请的权限类型和应用发布地区。我们将视应用发布地区的相关要求进行权限开放的评估。
    
    如果提交的材料不满足要求，审批将不能通过。如果审批通过，即可进入开发测试阶段，完成开发测试后即可发布。
    
    若您的业务范围发生变动，需要修改相应的数据权限，您可以点击“修改”重新提交申请。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/9SLPEYHqR_WFqx77LzDtLQ/zh-cn_image_0000002569019147.png?HW-CC-KV=V1&HW-CC-Date=20260417T013559Z&HW-CC-Expire=86400&HW-CC-Sign=DF0703C53D7CE199DF78907F6688FAEA62A9565421C5596F64B7C4D24608B784)
