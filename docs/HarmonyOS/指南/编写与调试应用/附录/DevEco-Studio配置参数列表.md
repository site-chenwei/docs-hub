---
title: "DevEco Studio配置参数列表"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-configuration-parameter"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "附录"
  - "DevEco Studio配置参数列表"
captured_at: "2026-04-17T01:36:50.454Z"
---

# DevEco Studio配置参数列表

DevEco Studio基于IntelliJ平台开发，在原生的IntelliJ参数的基础上新增了部分参数，这些参数可在idea.properties中进行配置，参数列表如下：

| 
参数

 | 

参数说明

 |
| :-- | :-- |
| 

grs\_url

 | 

设置DevEco Studio连接的云端环境。

 |
| 

npm\_config\_strict\_ssl

 | 

设置是否开启npm的https证书校验。默认为true，表示开启证书校验。

 |
| 

ohpm\_config\_strict\_ssl

 | 

设置是否开启ohpm的https证书校验。默认为true，表示开启证书校验。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/cFLxDS8vStarHyweMNtrzw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=E2B29CBBB72C88429023DE2095F403B453E843ECA75489C5811F60EDE3C3B3F1)

关闭证书校验，可能会带来安全风险，请谨慎使用。
