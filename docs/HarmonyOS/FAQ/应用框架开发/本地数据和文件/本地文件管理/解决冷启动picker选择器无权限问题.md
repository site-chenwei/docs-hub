---
title: "解决冷启动picker选择器无权限问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-46"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "解决冷启动picker选择器无权限问题"
captured_at: "2026-04-17T02:03:14.946Z"
---

# 解决冷启动picker选择器无权限问题

在APP冷启动后，由于没有uri的读取权限，可以通过保存草稿操作将对应的文件复制到沙箱路径下，然后在冷启动时获取这些文件。

**参考链接**

[fs.copyFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fscopyfile)

[应用沙箱目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)
