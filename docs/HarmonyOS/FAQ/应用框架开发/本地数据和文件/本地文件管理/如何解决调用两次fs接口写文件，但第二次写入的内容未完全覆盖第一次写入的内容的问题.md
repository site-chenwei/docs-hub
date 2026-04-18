---
title: "如何解决调用两次fs接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-25"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "如何解决调用两次fs接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题"
captured_at: "2026-04-17T02:03:14.237Z"
---

# 如何解决调用两次fs接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题

清空文件时必须要设置OpenMode.TRUNC，默认覆盖模式(WRITE\_ONLY)只是覆盖不会清除,TRUNC模式会先清空文件内容。参考代码如下：

```typescript
fs.openSync(dst, fs.OpenMode.WRITE_ONLY | fs.OpenMode.TRUNC | fs.OpenMode.CREATE);
```
