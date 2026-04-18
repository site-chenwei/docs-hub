---
title: "使用HWASan检测内存错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "日志与故障分析"
  - "故障分析"
  - "使用HWASan检测内存错误"
captured_at: "2026-04-17T01:36:49.905Z"
---

# 使用HWASan检测内存错误

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[ASan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)的内存错误检测工具。 与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的检测。关于HWASan的检测原理请参考[HWASan检测原理](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-principle#section187526511146)。

#### 约束条件

-   HWASan检测仅适用于AArch64架构的硬件。
-   ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

#### 开启HWASan

DevEco Studio 6.1.0 Beta1之前的版本，仅支持对C++源码开启HWASan。

从DevEco Studio 6.1.0 Beta1版本开始，同时支持对C++编译生成的无源码so文件进行二进制插桩，进而开启HWASan功能。

#### \[h2\]方式一

1.  点击**Run > Edit Configurations > Diagnostics**，勾选**Hardware-Assisted Address Sanitizer**开启C++源码检测插桩。
    
    从DevEco Studio 6.1.0 Beta1版本开始，可以同时勾选**BinXO check**，开启无源码的so文件的HWASan检测插桩。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/SYRDoF4ZQQSGNi66zyhLXg/zh-cn_image_0000002561833227.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=49942E5780FFE89E7A4C24661AF139C44F005B92353257BD08D714466381012A)
    
2.  （可选）如果部分无源码so不需要进行HWASan检测插桩，可以在工程级或模块级build-profile.json5文件中，配置excludeSoFromBinXO字段，填写需要忽略的so列表，支持正则匹配。
    
    "buildOption": {
      "nativeLib": {
        "excludeSoFromBinXO": \["\*\*/liblibrary.so"\]
      }
    }
    

#### \[h2\]方式二

1.  修改工程目录下的AppScope/app.json5文件，添加HWASan配置开关。
    
    "hwasanEnabled": true
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/sfp9nzSZQNiEpGIwN1e7zw/zh-cn_image_0000002561753241.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=435CCACFD0D67E72B4085F5EC94995C0C2C471821B30C1DC9A3E455DAA853EE2)
    
2.  在需要开启HWASan的模块级build-profile.json5中，添加构建参数开启HWASan检测插桩。
    
    // DevEco Studio 6.1.0 Beta1以下版本
    "buildOption": {
      "externalNativeOptions": {
        "arguments": \["-DOHOS\_ENABLE\_HWASAN=ON"\]
      }
    // DevEco Studio 6.1.0 Beta1及以上版本，同时开启有源码和无源码的C++的HWASan检测插桩
    "buildOption": {
      "externalNativeOptions": {
        "arguments": \["-DOHOS\_ENABLE\_HWASAN=ON", "-DOHOS\_ENABLE\_BINXO=ON"\]
      }
    
3.  如果部分无源码so不需要进行HWASan检测插桩，可以在工程级或模块级build-profile.json5文件中，配置excludeSoFromBinXO字段，填写需要忽略的so列表，支持正则匹配。
    
    "buildOption": {
      "nativeLib": {
        "excludeSoFromBinXO": \["\*\*/liblibrary.so"\]
      }
    }
    

#### 使用HWASan

1.  运行或调试当前应用。
2.  当程序出现内存错误时，弹出HWASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[HWASan日志规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/address-sanitizer-guidelines#hwasan日志规格)，异常检测类型请参考[HWASan异常检测类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-hwasan-detection#section207321025115510)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/0hEF3_6LTwCrs_QZoryY_w/zh-cn_image_0000002530913298.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=F87325541CEC855D71008BC9EF95D743EFDC40A2D83602328C5BB12847342663)
    
3.  如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/d8p2IXKrSeOdCuDLn-JhKA/zh-cn_image_0000002530753308.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=C9EA83913133FC6437E85659141C6A4B779D073291BB8A3F78A6922F6C5A41CB)
