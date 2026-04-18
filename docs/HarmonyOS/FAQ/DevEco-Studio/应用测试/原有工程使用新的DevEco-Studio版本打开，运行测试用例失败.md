---
title: "原有工程使用新的DevEco Studio版本打开，运行测试用例失败"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用测试"
  - "原有工程使用新的DevEco Studio版本打开，运行测试用例失败"
captured_at: "2026-04-17T02:03:25.279Z"
---

# 原有工程使用新的DevEco Studio版本打开，运行测试用例失败

**问题现象**

如果工程是在DevEco Studio 3.1.0.400之前版本创建的，升级DevEco Studio至3.1.0.400及以上版本后，原有工程运行测试用例会失败，并提示“A page configured in 'test\_pages.json' must have one and only one '@Entry' decorator”。

**图1**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/uUYVKBXmTIuoTGzqPqUxmQ/zh-cn_image_0000002229604113.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=CD4119CCC16CE85E7D54D1B669934867EFF6E0972AD7FE1DF39147CE1AB8296B "点击放大")

**解决措施**

将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。

**图2**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/eM6rDw4nSiKixwJm_qBcjQ/zh-cn_image_0000002194158732.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=654B6A5B1C3A74014C1DB7F68E101CD3AEABA441DA7A5B411E831C47FCF44C48 "点击放大")
