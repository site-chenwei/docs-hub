---
title: "编译报错“keystore password was incorrect”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-19"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“keystore password was incorrect”"
captured_at: "2026-04-17T02:03:21.238Z"
---

# 编译报错“keystore password was incorrect”

**问题现象**

编译时出现错误，提示“ERROR - hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details: Init keystore failed: keystore password was incorrect”。请检查密钥库密码是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/LuBRvhgKS0qBdfaCkSbxZA/zh-cn_image_0000002229603737.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=CED498E219BCAEEAE1B02609F0D3F13B2ACCCFA2D3762180CAEBA07309F75D98)

**报错原因**

密钥库(p12)的密码错误。签名文件中的签名密码错误导致该问题出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/gj0nzn5aRSi1kuWl3or93A/zh-cn_image_0000002436501498.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=D214551030D6538156D659966A38674DEDAD03CCFE36A81F2443DCAAC0FD75C9)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Y8hrQZUORe6TTitejBWBtg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=B08105479EED9BFCD5896B925A10765CC2CAA7EDD1557C85E25FBF430E63279C)

密钥库密码和密钥密码在创建p12文件时由开发者输入，请牢记这些密码。build-profile.json5文件中记录了密码的密文，但签名工具需要输入密码明文，不能直接使用build-profile.json5中的值。

**常见场景**

1.  密码输入错误。
2.  在命令行中输入了密文。
3.  密钥（keyAlias）密码和密钥库（p12）密码混淆。

**解决措施**

重新自动签名可以解决该问题：

1\. 点击**File > Project Structure > Project > Signing Configs**，打开签名配置页面。

2\. 勾选“Automatically generate signing”（如果是HarmonyOS工程，还需勾选“Support HarmonyOS”），等待重新签名，点击**OK**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/HZ6cG3usQzOspACpFeZFmA/zh-cn_image_0000002229758209.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=101A9BB5A472601D225E34953A6FA9B30D63B54C8D8F0CCA8FFAB01A2A5AC3C2)
