---
title: "控制后台进程CPU使用率"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-controlling-background-process-cpu"
menu_path:
  - "最佳实践"
  - "功耗"
  - "应用功耗优化"
  - "后台任务低功耗"
  - "后台硬件资源合理使用"
  - "控制后台进程CPU使用率"
captured_at: "2026-04-17T01:54:18.767Z"
---

# 控制后台进程CPU使用率

CPU使用率表示进程在CPU上的运行时间占总时间的百分比，计算公式为：CPU使用率 = 运行时间 / 总时间。单核CPU使用率的最大值为100%，多核CPU使用率的最大值为核数乘以100%。例如，8核CPU使用率的最大值为800%。

系统将进程的任务调度到多个CPU核上，进程在所有核上运行的时间总和与总时间的比值即为该进程的CPU使用率。例如，1秒内进程在所有核上运行的总时间为1.1秒，则该进程的CPU使用率为110%。

#### 约束

后台进程在10分钟内的单核CPU使用率不得超过80%。

短时任务后台进程CPU使用率约束：后台进程任务期间单核CPU使用率不得高于80%。

#### 调测验证

1.  连接设备，打开命令行窗口，输入hdc shell进入设备。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/C_CA-tEQRIO-kUMmKWrbEA/zh-cn_image_0000002229450601.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=ABA54D9FBF66E3437D8464C2F3737878C067636F1F0DE41533B14BEE44D8984F "点击放大")
    
2.  输入ps -ef | grep bundleName，查询应用使用率的进程号。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/gb0mOdlcT4eVulLcpBq5Tw/zh-cn_image_0000002229336117.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=EA0B470AEC8524598C124D4AF052FC5501785426A5CE6D16ADC1874F7DD63D5C "点击放大")
    
3.  输入：top -p xxx，查看对应进程的使用率。查询结果中，CPU列显示进程的实时使用率。其中，xxx是进程ID(PID)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/f_K9HvqRRR6wqWAJ7iyFCQ/zh-cn_image_0000002194010320.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=AEB808497BEE857CE052F18D90E9989FE41E3B71BCB70A913E90D6201E008BF6 "点击放大")
