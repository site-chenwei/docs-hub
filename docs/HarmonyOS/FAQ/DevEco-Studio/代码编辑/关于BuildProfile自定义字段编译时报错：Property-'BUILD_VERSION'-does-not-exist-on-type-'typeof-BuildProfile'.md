---
title: "关于BuildProfile自定义字段编译时报错：Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-10"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "代码编辑"
  - "关于BuildProfile自定义字段编译时报错：Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'"
captured_at: "2026-04-17T02:03:20.750Z"
---

# 关于BuildProfile自定义字段编译时报错：Property 'BUILD\_VERSION' does not exist on type 'typeof BuildProfile'

**问题描述**

项目编译时，关于 BuildProfile 的自定义字段报错如下：

```text
Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
```

**解决措施**

获取构建参数并生成BuildProfile类文件后，在HSP中可以通过以下方式引入该文件：

```screen
import BuildProfile from '${packageName}/BuildProfile';
```

可参考[在代码中获取构建参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-guide#section195881502412)。
