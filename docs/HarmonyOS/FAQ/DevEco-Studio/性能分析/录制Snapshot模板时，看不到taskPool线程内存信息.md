---
title: "录制Snapshot模板时，看不到taskPool线程内存信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-15"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "性能分析"
  - "录制Snapshot模板时，看不到taskPool线程内存信息"
captured_at: "2026-04-17T02:03:25.129Z"
---

# 录制Snapshot模板时，看不到taskPool线程内存信息

**问题现象**

录制Snapshot模板时，无法看到taskPool线程的内存信息。

**可能原因**

Snapshot模板只支持dump主线程的虚拟机堆内存。

**解决措施**

可使用hidumper --mem-jsheap ${pid} -T ${tid}获取指定进程指定JS线程的虚拟机堆内存，文件生成后导入Profiler查看。详细信息参考[查询虚拟机堆内存](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询虚拟机堆内存)。
