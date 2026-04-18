---
title: "ohosTest测试文件引用了entry模块的方法，测试时报cppcrash"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-8"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用测试"
  - "ohosTest测试文件引用了entry模块的方法，测试时报cppcrash"
captured_at: "2026-04-17T02:03:25.326Z"
---

# ohosTest测试文件引用了entry模块的方法，测试时报cppcrash

**问题现象**

如果ohosTest测试文件引用了entry的方法，并且entry中存在以普通形式（例如"entry/ets/workers/Worker.ets"）加载worker时，测试执行期间会报cppcrash。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/AymKHS0XRUqu1DZbJRsMIQ/zh-cn_image_0000002194318400.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=E17AFDC563C178823350AA048FF5EF2F2C99A85C7670D55A643F16BD3691D190)

**解决措施**

修改entry中实例化worker的路径形式为带@标识的路径加载形式或相对路径加载形式，再次执行测试以确保可以正常通过。

-   @标识路径加载形式("@entry/ets/workers/Worker.ets")：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/T74iR6lnQgabfm25CAtVug/zh-cn_image_0000002194158792.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=50985C501FC749E25D76692456B69E65B9E04A3A5B75505060153B3F3E53BC8E)
    
-   相对路径加载形式("../workers/Worker.ets")：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/VBLQzrnNRtq4c5YVkK4hOg/zh-cn_image_0000002229758665.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=8C3B0EAC7DA45C7DDF20CB338FEE55D68E4E42E54660D254C36C5AE58FC5C09C)
