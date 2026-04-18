---
title: "编译报错“The required attribute: module"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-136"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The required attribute: module-name is missing”"
captured_at: "2026-04-17T02:03:22.741Z"
---

# 编译报错“The required attribute: module-name is missing”

**错误描述**

缺少必需属性：module-name。

**可能原因**

1.  build-profile.json5 文件中缺少模块名称。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/tWPYoqvVQ7WtUDV--DN9WQ/zh-cn_image_0000002229758649.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=C92457A87ED9AC02DA8747996493C571C3A7BE42B20B9C0CF7E6C46384AC7051)
    
2.  在hvigorconfig.ts中动态添加模块时未设置模块名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/yOnD52efSjqy-8rGpm_UOg/zh-cn_image_0000002194158776.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=4AB26AA8D812048439B1FC1D104A4C708CF9D47D05E972BAEBAFA3F83247C84A)

**解决措施**

1.  进入项目根目录下的build-profile.json5文件，确保module下有非空的name字段。
2.  进入项目根目录下的hvigorconfig.ts文件，确保includeNode方法的参数name字段存在且非空。

**参考链接**

[Hvigor脚本文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-life-cycle#section810245135914)
