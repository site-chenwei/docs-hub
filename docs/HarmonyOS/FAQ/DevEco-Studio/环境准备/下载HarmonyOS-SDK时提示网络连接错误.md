---
title: "下载HarmonyOS SDK时提示网络连接错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-4"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "下载HarmonyOS SDK时提示网络连接错误"
captured_at: "2026-04-17T02:03:20.135Z"
---

# 下载HarmonyOS SDK时提示网络连接错误

**问题现象**

网络连接正常，但下载HarmonyOS SDK时提示网络连接错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/vOuYudaWQDGikB6mD-YWVg/zh-cn_image_0000002229758633.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=4530167FC0FF85673DF2747070BFD582DBC99884628B79563C9FEEA3DF67FE91)

**解决措施**

由于使用的PC系统语言为英文且区域码为US，可能导致问题。请按照以下步骤将区域码修改为CN，在修改前请确保已关闭DevEco Studio。

在C:\\Users\\\_username\_\\AppData\\Roaming\\Huawei\\DevEcoStudio4.1\\options路径下（MacOS 路径为/Users/\_username\_/Library/Application Support/Huawei/DevEcoStudio4.1/options），打开country.region.xml文件，将countryregion name修改为“CN”。

```xml
<application>
    <component name="CountryRegionSetting">
        <countryregion name="CN"/>
    </component>
</application>
```
