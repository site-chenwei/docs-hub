---
title: "并发场景下AES加密失败"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-3"
menu_path:
  - "FAQ"
  - "系统开发"
  - "安全"
  - "密钥管理（Universal Keystore）"
  - "并发场景下AES加密失败"
captured_at: "2026-04-17T02:03:16.742Z"
---

# 并发场景下AES加密失败

**原因**

使用HUKS重复导入相同的密钥时，[huks.importKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksimportkeyitem9)会判断密钥是否存在。如果存在，会删除并重新生成密钥，这可能导致其他线程的init操作失败。

**解决措施**

使用HUKS时，相同密钥只需导入一次，系统会安全存储密钥，并使用密钥别名进行密码学操作。如果不需要系统保存密钥，可以使用cryptoFramework。
