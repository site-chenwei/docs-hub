---
title: "1001502014 应用未申请scopes或permissions权限的可能原因和解决方法"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2"
menu_path:
  - "指南"
  - "应用服务"
  - "Account Kit（华为账号服务）"
  - "Account Kit常见问题"
  - "1001502014 应用未申请scopes或permissions权限的可能原因和解决方法"
captured_at: "2026-04-17T01:36:11.129Z"
---

# 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1.  没有申请对应的账号权限。
    
2.  权限申请成功后，最迟会在25小时后生效。
    
3.  使用[获取风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-introduction)能力，但未申请获取风险等级权限。
    

**解决措施**

1.  申请对应权限，请见[申请账号权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-config-permissions)章节。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/t7mkIjHURoyUco8M2EJCgw/zh-cn_image_0000002569019399.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=8357168114E377F7A139827887FBD673495731983BDDADBCB6591FBF446B2731)
    
2.  权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。
    
    **图1** 修改前
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/lIfPaCL-S_2zVhrMuf2Kjw/zh-cn_image_0000002538019686.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=335491AB968AFC94CA513A01A3694501881EDB417F5EA851760BACB60DC747CA)
    
    **图2** 修改后
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/eMOZmNauTo2urBZo3I9toQ/zh-cn_image_0000002538179614.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=1C597A3EB2EBB8AE34FA3CFEAA4A83128A241E7F04EAA3F1773C5CA6692B2719)
    
3.  确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-introduction)申请对应权限。
