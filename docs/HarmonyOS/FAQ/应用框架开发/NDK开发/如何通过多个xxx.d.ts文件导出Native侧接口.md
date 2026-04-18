---
title: "如何通过多个xxx.d.ts文件导出Native侧接口"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-63"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何通过多个xxx.d.ts文件导出Native侧接口"
captured_at: "2026-04-17T02:03:02.306Z"
---

# 如何通过多个xxx.d.ts文件导出Native侧接口

**问题现象**

由于底层C++库规模较大，向外暴露的接口数量较多，建议将其拆分成多个.d.ts文件以便归类。

**解决措施**

在oh-package.json5中的types字段只能指定一个出口。如果需要封装多个.d.ts文件中的接口，可以使用重导出的方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/ehiIsTwFTqi43b7pMJhiyA/zh-cn_image_0000002194318472.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=1A225B7765F8321F787F3B183430A0D4C1BCE5F0AADDF7899132F2C4A14118CA "点击放大")

实现方式：

在index1.d.ts文件中声明Native侧导出接口，然后通过index.d.ts文件重导出到ArkTS侧使用。

在index1.d.ts文件中导出接口。

export const sub: (a: number, b: number) => number;

在index.d.ts文件中重导出这些接口。

export {sub} from './index1'
export const add: (a: number, b: number) => number;
