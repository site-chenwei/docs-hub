---
title: "使用DevEco Testing进行稳定性测试"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-deveco-testing"
menu_path:
  - "最佳实践"
  - "稳定性"
  - "稳定性检测"
  - "开发态稳定性检测"
  - "稳定性测试"
  - "使用DevEco Testing进行稳定性测试"
captured_at: "2026-04-17T01:54:19.361Z"
---

# 使用DevEco Testing进行稳定性测试

本文介绍DevEco Testing为HarmonyOS NEXT应用开发者提供的稳定性测试服务，涵盖稳定性基础质量测试和应用探索测试。稳定性基础质量测试依据HarmonyOS NEXT稳定性测试建议，提供应用稳定性基础检测能力，帮助开发者快速上手稳定性测试。应用探索测试采用基于专家经验的智能遍历方法，驱动测试高效执行，构建应用专属测试模型，帮助开发者有效识别应用故障。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/4MdmjCsCQBCIbEUmUdSlCw/zh-cn_image_0000002441736772.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=87EDC333841330F31747BC0BCF9AD2A779DCC54E4032E30E8CF8208EB7A7419A)

#### 稳定性基础质量测试

**稳定性基础质量测试：**根据应用稳定性建议，检测应用运行过程中是否存在应用崩溃、资源过载、内存泄漏等异常情况。

**创建任务**

进入DevEco Testing客户端，在左侧菜单栏选择“稳定性基础质量测试”，点击“稳定性基础质量测试”服务卡片，即进入任务创建界面。按需配置任务参数，点击创建任务即开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/eEwaKGpKSh6sjFd9bNY5jQ/zh-cn_image_0000002475040597.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=DD199C4C5B746F28CADB60108DD1AAD6635E3A3BC9084F5E6FF96D1F06DB7DDD)

任务名称：用于标识任务，工具会根据时间生成默认任务名，支持自定义修改。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择一个待测设备和待测应用。系统版本支持 HarmonyOS 6.0 及以上版本。

选择应用：可选择测试设备上已安装的应用；或安装新的应用，即在测试设备上安装新的应用包。

是否卸载应用：选择卸载应用后，测试时会进行卸载无残留检测，测试任务结束后将自动卸载被测应用。

是否开启多线程检测：打开后，系统支持检测应用多线程安全问题（例如：多个线程并发写入操作）。

是否开启[MemDebug](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-hwasan-detection#section10791454125320)模式：打开开关以后，会打开被测应用的内存越界检测开关，可以辅助发现和定位内存越界类问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/hkKnSTy0QUma_o4gamlv1Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=B47BC9F68638245A40DF6330733424141ADFB0D7683DDD8B5D28163CA334E5D7)

**稳定性基础质量测试最佳测试时长建议设置为8****小时。**

**测试执行**

创建任务后，将会跳转到执行页，进入测试环境初始化阶段。待测试环境初始化完成，待测应用被启动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uXnmwVGdQw2Fm1HhFRnZUQ/zh-cn_image_0000002475126385.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=2A968642BB2778F701BD0C815C64C986D10CD0DE8EF0A026966D061F03F22E39)

测试过程中，在测试页面可以看到测试进度、检测状态、实时投屏及执行日志。

**查看报告**

测试完成后，自动生成测试报告。报告包含任务信息、结果统计、检测规则。

任务信息中，可查看当前应用信息、任务执行时长及详细的环境参数（配置信息及环境信息），点击打开目录按钮支持导出 HTML 的报告文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/NuEXpGU_QZ6K2_4bKh0mXw/zh-cn_image_0000002475127285.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=5C5A97C882FAFE95A5CB692A770C79B188456AE290568E3264203F012E17CA03)

测试概览中，包含结果统计及检测规则，可直观查看本次任务中，测试项检测结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/9pJwnwqjQOilRfZd7ojqHg/zh-cn_image_0000002441728014.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=3A873371BC9C26D2A8BEA96C8F92426E3E13DA0FEE36A2DAF69F3AACDD8D97A3)检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/BfK3lF29TJ29Q87Bt7u7GQ/zh-cn_image_0000002475048409.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=24F85CB2B5B2D628F52A780E65E84A0C66FDB1FED05F1D914D50EA46EAE46B67)点击查看按钮，支持查看测试过程中的日志，用户可结合问题描述及日志详情进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/a-5aoofnQY-fuCy8-bihgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015421Z&HW-CC-Expire=86400&HW-CC-Sign=4F631AED0FDC05D632E311D8AB71F2EAAB01CBCDCCBFC7DD3E831208DD62E375)

更多测试服务详情，请前往DevEco Testing客户端->专项测试->稳定性基础质量测试->任务创建页->测试指南中查询。

更多应用稳定性体验优化建议及问题定位，请查阅：[应用稳定性体验建议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/experience-suggestions-stability) 及 [CppCrash问题定位](https://developer.huawei.com/consumer/cn/doc/architecture-guides/common-v1_26-ts_c25-0000002324993158)

#### 其他专项测试

请参考：[专项测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specialized-testing)。

#### 探索测试

请参考：[应用探索测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/exploratory-testing#section12324184817324)。
