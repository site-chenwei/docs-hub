---
title: "受限ACL权限申请"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application"
menu_path:
  - "指南"
  - "应用服务"
  - "Screen Time Guard Kit（屏幕时间守护服务）"
  - "开发准备"
  - "受限ACL权限申请"
captured_at: "2026-04-17T01:36:22.317Z"
---

# 受限ACL权限申请

1.  在 [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)和[发布Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)之前，需要[申请相应的ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。
    
2.  登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Wc4CkmhSSj2Q9NaHFcsW1g/zh-cn_image_0000002538180032.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=AE13D39E7F66931DEA7662CAB208D27BFBC23E855AF7B30F61C987734AC7F33E)
    
3.  在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，查找并勾选权限，提交申请。
    
4.  根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/YIRw6M2iQlGYNDoAyD3KDA/zh-cn_image_0000002569019819.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=C613B4B659E913EFF5FA6F6041A522768AD31BE45BB8DDC3EB42A340C5A9EC2B)
    
5.  权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/z5-CZJYlTD2CkG3OieKgyg/zh-cn_image_0000002568899811.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=83A5408B574A5EA5B87E7415C161B664595ACD57233C211570D8B6128D768791)
    
6.  在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/5Inx7xHOTIetTE8bCQlLyg/zh-cn_image_0000002538020106.png?HW-CC-KV=V1&HW-CC-Date=20260417T013624Z&HW-CC-Expire=86400&HW-CC-Sign=2E417AE9D1DFA99CC4EEAFDE65F142443C5EC898E0F02FD9151B62457FE141CF)
    
7.  选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)替换profile文件。
    
8.  在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限，如下所示：
    
    ```typescript
    "requestPermissions": [{
       "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
    }]
    ```
