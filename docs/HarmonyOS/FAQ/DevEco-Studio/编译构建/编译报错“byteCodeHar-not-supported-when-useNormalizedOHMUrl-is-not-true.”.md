---
title: "编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-166"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”"
captured_at: "2026-04-17T02:03:23.220Z"
---

# 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”

**错误描述**

当useNormalizedOHMUrl配置为false时，不支持编译字节码HAR。

**可能原因**

当HAR模块的build-profile.json5文件中的byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段未配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/aN9cOu6_SSuNBG2tmi3HTw/zh-cn_image_0000002194318416.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=27C7B075EDCAC54B78BF8A8F042AA22C7D0D8D42EBEB5083616CEEAA0D147DE7)

**解决措施**

当HAR模块的build-profile.json5文件中byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段也必须配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/1MEQsysaSsmtbRlsN5-1og/zh-cn_image_0000002308297297.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=618F5707C7E893AC0B9F8B4C5C15681AAE20F9F4D0442E0B7A3B96F37DE9E0A3)

**参考链接**

[strictMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app#section13181758123312)
