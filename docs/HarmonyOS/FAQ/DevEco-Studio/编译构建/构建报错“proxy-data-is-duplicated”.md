---
title: "构建报错“proxy data is duplicated”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-112"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "构建报错“proxy data is duplicated”"
captured_at: "2026-04-17T02:03:22.416Z"
---

# 构建报错“proxy data is duplicated”

**问题现象**

打包APP时，出现“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”的提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/jCXi5f2hQ8C7lU1lsmXMIg/zh-cn_image_0000002229758777.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=30E9FACB52A982995EE24DBE9A27FB2F2E34E0E9A21C5BAEA7D98FC33C6C478F)

**解决措施**

proxyData 标识模块提供的数据代理列表，仅允许 entry 和 feature 配置，不同 proxyData 中配置的 URI 不得重复。遇到此问题，检查模块间是否配置了相同的 URI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/JCRUcKuZR3mUNB1qZeOL2w/zh-cn_image_0000002194158904.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=91CAEA9A87CDF49CFEE864A555AA58A879E57122337485342373849F84CA59ED)
