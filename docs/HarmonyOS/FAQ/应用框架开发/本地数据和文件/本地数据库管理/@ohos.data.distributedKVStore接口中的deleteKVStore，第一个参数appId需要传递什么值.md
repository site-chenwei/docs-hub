---
title: "@ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-46"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地数据库管理"
  - "@ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值"
captured_at: "2026-04-17T02:03:09.357Z"
---

# @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值

appId是调用方应用的包名。通过调用[bundleManager.getBundleInfoForSelf()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)获取BundleInfo，然后通过BundleInfo对象的signatureInfo属性获取appId。
