---
title: "在ArkTS的主线程中使用await会阻塞主线程吗"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-43"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "ArkTS线程模型和并发"
  - "在ArkTS的主线程中使用await会阻塞主线程吗"
captured_at: "2026-04-17T02:03:01.332Z"
---

# 在ArkTS的主线程中使用await会阻塞主线程吗

await会挂起当前异步任务，等待条件满足后唤醒执行，主线程可处理其他任务。
