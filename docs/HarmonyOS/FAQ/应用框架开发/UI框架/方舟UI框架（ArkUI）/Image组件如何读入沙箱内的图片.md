---
title: "Image组件如何读入沙箱内的图片"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-154"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Image组件如何读入沙箱内的图片"
captured_at: "2026-04-17T02:03:04.272Z"
---

# Image组件如何读入沙箱内的图片

Image组件不能直接传入应用沙箱路径，需要传入应用沙箱URI。

1.  参考fileUri模块示例代码，获取文件的沙箱路径。
2.  然后调用fileUri.getUriFromPath方法将沙箱路径转化为沙箱URI，传入之后即可正常显示沙箱图片。

**参考链接**

[@ohos.file.fileuri (文件URI)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri)
