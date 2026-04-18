---
title: "entry引用本地library时，没有ASan日志输出"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-18"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "entry引用本地library时，没有ASan日志输出"
captured_at: "2026-04-17T02:03:24.571Z"
---

# entry引用本地library时，没有ASan日志输出

**问题现象**

entry引用本地library时，已经勾选ASan选择项，没有ASan日志输出。

**解决措施**

引用本地C++ library时，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

{
  // ...
      "arguments": "-DOHOS\_ENABLE\_ASAN=ON",
      // ...
    }
  },
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/qmZLzuJ7RDShJ1zqoiFlvQ/zh-cn_image_0000002194318360.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=ED23BC457E01AD4EB136437446F663B073B18B10DC838B0441174C0D3302A94D)
