---
title: "HSP包编译之后的.har文件的作用是什么"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-33"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序包结构"
  - "HSP包编译之后的.har文件的作用是什么"
captured_at: "2026-04-17T02:02:58.174Z"
---

# HSP包编译之后的.har文件的作用是什么

HSP包编译后会生成.hsp文件和.har文件。.hsp文件用于安装，.har文件仅暴露接口，不包含具体实现。

HSP包中导出的方法头文件位于.har文件中，实现在.hsp文件中。
