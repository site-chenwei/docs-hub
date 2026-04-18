---
title: "fs.write返回的长度和本身content长度不一致"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-39"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "fs.write返回的长度和本身content长度不一致"
captured_at: "2026-04-17T02:03:14.810Z"
---

# fs.write返回的长度和本身content长度不一致

fs.write返回的是实际写入的数据长度，单位字节。String.length返回的是字符串的长度，两者返回的单位不一样，所以在比较长度时也是不一致的。String.length返回UTF-16编码单元数，当字符串包含非ASCII字符时，其字节长度可能大于该值（如中文通常占3字节）。

参考文档：[fs.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fswrite)
