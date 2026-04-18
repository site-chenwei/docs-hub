---
title: "后台CPU占用峰值"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "开发自测试"
  - "应用与元服务体检"
  - "附录"
  - "体检规则"
  - "后台CPU占用峰值"
captured_at: "2026-04-17T01:36:50.389Z"
---

# 后台CPU占用峰值

#### 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

#### 检测逻辑

1.  执行hdc shell。
2.  执行hidumper --cpuusage <进程pid>命令，获取总的cpu使用率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/vRtrafBkSPeaqCPGcGKG_Q/zh-cn_image_0000002530753024.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=FDDBFEBEA650CCFC4B1D9D6C6B7F0C5347790809E940ADFBCDA883A86DF66E85)

#### 计算逻辑

执行多轮测试，取最大值为cpu占用峰值，cpu占用率须小于5%。
