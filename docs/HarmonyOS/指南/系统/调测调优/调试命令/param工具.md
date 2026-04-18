---
title: "param工具"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool"
menu_path:
  - "指南"
  - "系统"
  - "调测调优"
  - "调试命令"
  - "param工具"
captured_at: "2026-04-17T01:36:03.074Z"
---

# param工具

param是为开发人员提供用于操作系统参数的工具，该工具只支持标准系统。

#### 环境要求

-   获取hdc工具，执行hdc shell。
-   正常连接设备。

#### param工具命令列表

| 选项 | 说明 |
| :-- | :-- |
| \-h | 获取param支持的命令。 |
| ls \[-r\] \[name\] | 显示匹配name的系统参数信息。带"-r"则根据参数权限获取信息，不带"-r"则直接获取参数信息。 |
| get \[name\] | 获取指定name系统参数的值；若不指定任何name，则返回所有系统参数。 |
| set name value | 设置指定name系统参数的值为value。 |
| wait name \[value\] \[timeout\] | 同步等待指定name系统参数与指定值value匹配。value支持模糊匹配，如"\*"表示任何值，"val\*"表示只匹配前三个val字符。timeout为等待时间（单位：s），不设置则默认为30s。 |
| save | 保存persist参数到工作空间。 |

#### 获取param支持的命令

-   获取param支持的命令，命令格式如下：
    
    ```bash
    param -h
    ```
    

#### 获取系统参数信息

-   显示匹配name的系统参数信息，命令格式如下：
    
    ```bash
    param ls [-r] [name]
    ```
    
    **示例**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/CY7C6risSQu6T5Sg5st5sA/zh-cn_image_0000002538179398.png?HW-CC-KV=V1&HW-CC-Date=20260417T013603Z&HW-CC-Expire=86400&HW-CC-Sign=1BACED3CE6A54FAC372B653B55BC4A3934FBCFDC9773E5A53B843B8A399B31DB)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/wS2AthL7SOuUXxJaivDw-Q/zh-cn_image_0000002569019183.png?HW-CC-KV=V1&HW-CC-Date=20260417T013603Z&HW-CC-Expire=86400&HW-CC-Sign=B9167360084B4DC2A6DC5A4B6BED5B8664202B23470401DB1BE795B09010B825)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/gS8BQ-YMSeadZtDzdYNPzg/zh-cn_image_0000002568899175.png?HW-CC-KV=V1&HW-CC-Date=20260417T013603Z&HW-CC-Expire=86400&HW-CC-Sign=D0F28991356044A9B033F1C01CD52530C372E53E010726C49E8BED36FA11C34F)
    

#### 获取系统参数的值

-   获取指定name系统参数的值，命令格式如下：
    
    ```bash
    param get [name]
    ```
    
    **示例**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/-bK3ef25RYGuedYDXpYlNw/zh-cn_image_0000002538019470.png?HW-CC-KV=V1&HW-CC-Date=20260417T013603Z&HW-CC-Expire=86400&HW-CC-Sign=FD62C1C3EEEF55CEC9C5F34B3EB123B69BD6262D18179F3DBA52E9AED7A19602)
    

#### 设置系统参数的值

-   设置指定name系统参数的值为value，命令格式如下：
    
    ```bash
    param set name value
    ```
    
    **示例**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Rgwv6_xzTtmOZao1mtRC-g/zh-cn_image_0000002538179400.png?HW-CC-KV=V1&HW-CC-Date=20260417T013603Z&HW-CC-Expire=86400&HW-CC-Sign=F0C5C58E3422A786A28CAF6E980644B8C038866534563C22FD861F27970EFD5E)
    

#### 等待系统参数值匹配

-   同步等待指定name系统参数与指定值value匹配，命令格式如下：
    
    ```bash
    param wait name [value] [timeout]
    ```
    
    **示例**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/L-R0KiG8SF61HuHmh7hN1Q/zh-cn_image_0000002569019185.png?HW-CC-KV=V1&HW-CC-Date=20260417T013603Z&HW-CC-Expire=86400&HW-CC-Sign=BD862A75C1BC1F5AF8291CE0DE723E4078EAAE727C36C58D3533E1BE1ED40045)
    

#### 保存persist(可持久化)参数

-   保存persist(可持久化)参数到工作空间，命令格式如下：
    
    ```bash
    param save
    ```
    
    **示例**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Mq1u-rsfRI-4Bo1nH8JaEg/zh-cn_image_0000002568899177.png?HW-CC-KV=V1&HW-CC-Date=20260417T013603Z&HW-CC-Expire=86400&HW-CC-Sign=1596B65877D14391A5ABBECBBE8319B9E259CF1FB5A71CA6394F7027DB109359)
