---
title: "HarmonyOS应用自动化签名时提示“Provision number exceeds limit”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-4"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "HarmonyOS应用自动化签名时提示“Provision number exceeds limit”"
captured_at: "2026-04-17T02:03:24.457Z"
---

# HarmonyOS应用自动化签名时提示“Provision number exceeds limit”

**问题现象**

使用自动化签名功能对HarmonyOS进行签名时，提示“Provision number exceeds limit”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/bbPbw38NRAmA7Uf6VBzfZw/zh-cn_image_0000002194318424.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=E6A67530D6ABF69CD1B31671484250B41C5FA0163772B02281E893230347C73D)

**解决措施**

AGC（AppGallery Connect）限制了自动化签名的使用次数。同一开发者账号在最近30天内使用自动化签名功能的次数不能超过150次。

可通过如下几种方式进行解决：

-   方法1：建议相同BundleName的应用，如果设备无变化，请使用同一套签名文件信息，不要反复进行重签名操作。
-   方法2：更换其它开发者账号进行登录，然后进行签名。
-   方法3：AGC限制同一个账号在30天内使用自动化签名的次数不超过150次。等待一段时间后，可重新使用该账号签名。
