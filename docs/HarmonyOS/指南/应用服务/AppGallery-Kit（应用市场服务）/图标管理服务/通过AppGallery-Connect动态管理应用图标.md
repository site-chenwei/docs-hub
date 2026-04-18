---
title: "通过AppGallery Connect动态管理应用图标"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-appinfo-manage"
menu_path:
  - "指南"
  - "应用服务"
  - "AppGallery Kit（应用市场服务）"
  - "图标管理服务"
  - "通过AppGallery Connect动态管理应用图标"
captured_at: "2026-04-17T01:36:12.142Z"
---

# 通过AppGallery Connect动态管理应用图标

通过图标管理服务，开发者可以在不升级应用版本的情况下，通过AGC页面动态管理应用的个性化图标，并在应用侧实现应用图标动态切换。

#### 申请开通服务

使用图标管理服务之前，请按如下格式向华为运营人员发送邮件申请开通服务。申请审核时间为1-3个工作日，审核结果请关注邮件信息或[互动中心](https://developer.huawei.com/consumer/cn/doc/app/agc-help-interaction-center-0000002276985946)通知。

-   请确保申请开通图标管理服务的应用处于正式上架状态，避免服务开通失败。
    
-   应用信息和开发者账号信息查询方法参见[查看应用信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-view-app-info-0000002282674569)。
    

**邮箱地址：** agconnect@huawei.com

**邮件标题：** HarmonyOS应用图标管理开通申请-应用名称

**邮件内容：**

开发者账号ID：\*\*\*\*\*\*\*\*

应用名称：\*\*\*\*\*\*\*

应用ID：\*\*\*\*\*\*\*

应用包名：\*\*\*\*\*\*\*\*

应用状态：\*\*\*\*\*\*\*\*

#### 通过AppGallery Connect配置应用图标

登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“APP与元服务”，在应用列表中选择已经开通图标管理服务的HarmonyOS应用，选择“分发 > 服务 > 图标管理”，进入图标管理页面，就可以管理HarmonyOS应用的个性化图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/F9wmjA7zTOqIIU007-NvtQ/zh-cn_image_0000002538179662.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=7700D4E63C9585F11E48771EA867DD2085EFCE3DFC756AA566E85B9EB8936FC8)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/VXRH1inJQZytRZ7DAXi_cg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=EADA89B8A01C9B99073CBEF0DB03CD881593B460C9CDC3DBAB48CD28E80169BA)

-   只有正式发布的HarmonyOS应用支持管理个性化图标。
    
-   在创建个性化图标前，您需要提前准备好需要上传的图标文件，图标文件需要满足应用市场的审核政策要求，详情参见《[应用审核指南](https://developer.huawei.com/consumer/cn/doc/app/50104)》。
    

#### 创建图标

1.  在图标管理页面点击“新增图标”按钮，进入创建图标页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-8_BJYYUTlqpzDWomexc1A/zh-cn_image_0000002569019449.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=70E51D8D5DC55103D20F7B2AC8557CA98D9A153B151A205EA71EC3DC13BCD50A)
    
2.  输入图标ID、图标名称，选择设备类型，上传图标文件，点击“保存”或者“提交”按钮，将图标保存为草稿状态或提交审核。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/pXSOmQ3mRfScs7n-GsdH4Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=B5EE94D3F0A827A3F5257BD8C10C5BA9AFF6D6ED29A70B5C072D0D15303FFD1D)

-   新创建的图标，需要经过应用市场审核通过，才能在客户端使用。
    
-   图标审核时间为1-3个工作日，审核状态和审核意见直接展示在图标信息查看页面，不会单独通知。
    

#### 编辑和更新图标

1.  在图标管理页面选择一个草稿或审核不通过的图标，点击“编辑”按钮，或选择一个审核通过的图标，点击“更新”按钮，进入图标编辑页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/z7MCU_HpSPeLPdSx1DuauA/zh-cn_image_0000002568899441.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=DF33DA0A987C2FCE5F0C568BAFA1158E58047E86E50535EDD3CADE131680B10A)
    
2.  输入图标ID、图标名称，选择设备类型，上传图标文件，点击“保存”或者“提交”按钮，将图标保存为草稿状态或提交审核。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/9sEoOzHqTiW9uZRrIuQ0FQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=B80BC5FE5E8C8F880743FB1BE0DF9F6450488FC4D27D9A4A8638808C88F43854)

-   草稿、审核不通过状态的图标支持编辑，审核中的图标不支持编辑，但是可以点击“撤销”按钮，将审核中的图标撤回草稿状态。
    
-   审核通过的图标支持更新，但只支持变更图标名称和图标文件，图标ID和设备类型不支持变更，图标更新也需要审核通过才能生效。
    

#### 删除图标

1.  在图标管理页面选择一个图标，点击“删除”按钮，再点击提示框中的“确认”按钮，就可以删除指定图标。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/EguF7mIJRNWkYxmgBxAdMw/zh-cn_image_0000002538019736.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=E547B58D673F035F27A5AAA617759BB364E1CF8C244D60B3FD20C2CAA847205B)
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/lot8HeUqQ1mGtfVaKvCc2A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013612Z&HW-CC-Expire=86400&HW-CC-Sign=0A241BA0AEA0629DFBF65BAFAFDCD375041673D8B09ADD2D82705D4669F51EA2)

-   图标删除不需要审批，删除之后不可恢复，请谨慎操作。
    
-   如果被删除的图标正在用户设备桌面上使用，图标删除后，桌面上的图标不会自动回退，需要客户端触发图标切换。
