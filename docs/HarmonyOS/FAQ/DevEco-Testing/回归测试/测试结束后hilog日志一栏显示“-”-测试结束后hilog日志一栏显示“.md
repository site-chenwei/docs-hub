---
title: "测试结束后hilog日志一栏显示“"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-16"
menu_path:
  - "FAQ"
  - "DevEco Testing"
  - "回归测试"
  - "测试结束后hilog日志一栏显示“-”"
captured_at: "2026-04-17T02:03:26.886Z"
---

# 测试结束后hilog日志一栏显示“-”

用户手动停止任务后，Hypium进程会直接关闭，不会生成hilog。如果任务正常结束时缺少hilog，请确认test包中config文件夹下的user\_config.xml文件中的devicelog参数设置为ON。如果没有，请添加该参数，重新打包即可解决。
