---
title: "如何解决编译报错“Indexed access is not supported for fields(arkts"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-126"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题"
captured_at: "2026-04-17T02:03:22.642Z"
---

# 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题

**问题现象**

动态调用类或接口的字段会导致编译报错：Indexed access is not supported for fields (arkts-no-props-by-index)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/LxJRWRt6R1e11kw2ttRZ1Q/zh-cn_image_0000002229604089.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=7A2982F8B65B2E1ECB4B93E0110F9038AF0AF47D84456154E79531A35B50DDE9)

**解决方案**

修改代码：

getValue(breakpoint: string): T {
  return Reflect.get(this.options, breakpoint) as T;
}
