---
title: "导入DevEco Testing的检测报告进行诊断"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-testing"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "开发自测试"
  - "应用与元服务体检"
  - "导入DevEco Testing的检测报告进行诊断"
captured_at: "2026-04-17T01:36:50.233Z"
---

# 导入DevEco Testing的检测报告进行诊断

从DevEco Studio 6.0.0 Beta3版本开始，支持在DevEco Testing中进行性能相关测试生成检测报告后，导入到AppAnalyzer进行诊断和分析，获得可能的故障原因并生成体检报告。

#### 前置操作

体检前，请先在DevEco Testing中测试并导出检测报告，具体操作方式请参考[性能基础质量测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specialized-testing#section12324184817324)或[场景化性能测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specialized-testing#section8642101711299)。

#### 进行体检

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/o7cc32eMRkeYw2G-OChM6Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=B9B1D9A4113AD2CDE6606A3ED68D56DA80F9B690A97A92451C9B8ECF7FEFE971)

由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

#### \[h2\]DevEco Studio 6.0.1 Beta1及以上版本

1.  点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**体检历史**按钮，点击右上角的**导入报告**按钮，根据界面提示，确保即将导入的检测报告满足相关要求。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/C51oOmqRRdClg1nEuaHEtw/zh-cn_image_0000002561752875.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=45BBAD4BE7A85F819B991291AFFE2B8F597233B53DF62A305E1207600E2D1EF6)
    
2.  选择从DevEco Testing导出的报告（zip文件），点击**确认**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](#section16156317171913)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/CtXlzDnIQSeEih-L3Et6eg/zh-cn_image_0000002530752944.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=638D8E9C6B9B6E15503F9D82EBCAE279F5311D37C11C9809D564E8AFAD9B51D4)
    
3.  诊断完成后，查看测试报告如下。
    
    -   **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
    -   **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
    -   **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。
    
    从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**用户反馈**向我们反馈。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/BpbQEIqyTOmqNXORZjm89Q/zh-cn_image_0000002561832869.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=4C36B63519BEAB0D607E802DCA7100F938CEAEB8344C752070A49FBF08E8BED8)
    

#### \[h2\]DevEco Studio 6.0.1 Beta1以下版本

1.  点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**历史记录**按钮，进入历史记录页面。
2.  点击右上角的**检测报告导入**按钮，首次测试时，请根据AppAnalyzer的指引，下载Python及三方库，并根据界面提示，确保即将导入的检测报告满足相关要求。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/wAu34TpLS_-aevRyYgkM6g/zh-cn_image_0000002561752877.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=497A88A14A0EBED67B239EAE3FB43F0295B60B036E11C89A674F5DAD683E162D)
    
3.  选择从DevEco Testing导出的报告（zip文件），点击**确认**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](#section16156317171913)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/N9aJuILcQYqI-MD1l-G4Gw/zh-cn_image_0000002530912948.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=ACBAFD141CBED3A8967C8D37D689B8088DFF4DF31C0EE04640348B0AA77CE7D9)
    
4.  诊断完成后，查看测试结果如下。
    
    -   测试报告：测试结果的汇总信息，点击**详情链接**可跳转到对应场景的详情报告。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/AIanSicwTgi8WHJAg4xkVg/zh-cn_image_0000002561752889.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=AF5377AD0E13A0FB4EB638F6951C30AC866999263BEED3C5C6719E4E2B559804)
        
    -   详情报告：给出详细的测试结果、可能的故障原因和对应的优化建议。
        
        -   **开始/结束页面、时间戳、调优文件（包含trace文件和调用栈文件）或snapshot文件等**：点击开始/结束页面可跳转到问题源码，点击时间戳可以打开性能分析工具Profiler并定位到问题发生的时间范围，点击调优文件或snapshot文件支持直接拉起Profiler并导入性能检测的问题数据进行调优分析。
        -   **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
        -   **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/qOgQJ5q0T2ClGra-Sl1AYw/zh-cn_image_0000002530752936.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=D07FEBB3AA3A6417DECF75C90D91AE9FEDD3BDECFCE1859A3F8F4EAB3C0FA92C)
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Uzih-gH6S4axRidpjLTX4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=F4F7377312DF093EEFF48765CF44828634FE87FBA1FBA22582EEFE0F45489341)
    
    由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。
    

#### 检测指标

AppAnalyzer会将DevEco Testing测试用例的操作归类为以下场景，仅支持对部分指标进行诊断，具体如下。

| 
场景

 | 

检测指标

 |
| :-- | :-- |
| 

页面间转场

 | 

点击响应时延

 |
| 

点击完成时延

 |
| 

转场卡顿率

 |
| 

页面滑动

 | 

滑动响应时延

 |
| 

滑动卡顿率

 |
| 

冷启动

 | 

完成时延

 |
| 

页面内转场

 | 

滑动响应时延

 |
| 

点击响应时延

 |
| 

点击完成时延

 |
| 

滑动卡顿率

 |
| 

起播时延

 |
