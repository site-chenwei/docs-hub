---
title: "hilog日志如何落盘存储"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-1"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "hilog日志如何落盘存储"
captured_at: "2026-04-17T02:02:57.156Z"
---

# hilog日志如何落盘存储

运行命令：hilog -w start -f ckTest -l 1M -n 5 -m zlib -j 11

文件保存在目录：/data/log/hilog/

参数解释：

```text
-w 开启日志落盘任务,start表示开始，stop表示停止。 
-f 设置日志文件名 
-l 设置单个日志文件大小，单位可以是：B/K/M/G 
-n 设置最大日志文件编号，当文件计数超过此编号时，日志文件旋转。范围：[2,1000]
-m 设置日志文件压缩算法 
-j 任务ID，范围：[10,0xffffffffff) 
更多参数含义请使用hilog --help查看。
```
