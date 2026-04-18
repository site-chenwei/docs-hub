---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "ohpm-repo install"
captured_at: "2026-04-17T01:36:42.386Z"
---

# ohpm-repo install

安装ohpm-repo服务。

#### 命令格式

ohpm-repo install \[options\]

#### 功能描述

在启动服务之前做好准备工作，包括：检查ohpm-repo配置文件的合法性和数据库的初始化等。

#### 选项

#### \[h2\]config

-   默认值："<binary\_root>/conf/config.yaml"
    
    <binary\_root>：ohpm-repo私仓解压根目录。
    
-   类型： String
    

可以在install命令后面配置--config <string>参数，指定配置文件路径。支持相对路径，以当前命令行工作路径作为根目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/fxxdO7vpRSWcqtdH18unuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=56F7F2A78C177B80BE9F6682E7C84F45D75154FFDB22FFF85296294ED4B66649)

执行install成功后，会在<deploy\_root>/conf中生成一个运行时配置文件config.yaml，作为后续命令的配置文件，其中<deploy\_root>为[ohpm-repo部署目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration#zh-cn_topic_0000001745376470_关于-deploy_root)。

#### \[h2\]skip-db

-   默认值：false
-   类型：Boolean
-   别名：s

在install命令后面配置-s或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/bDDlK5JkRaefwitNkrTOvQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=2AE80D0E6CD9514AC069D08F0416BA0985A2B2D83285220C2E49E30D97F02D12)

1\. 在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。

2\. 从ohpm-repo 5.2.0 版本起，旧参数 -sd 已被标记为弃用。请将配置中的 -sd 替换为 -s，旧参数将在未来版本中彻底移除。

#### \[h2\]diagnosis-and-repair

-   默认值：false
-   类型：Boolean
-   别名：dr

在install命令后面配置--dr或者--diagnosis-and-repair，诊断并修复包权限表；默认不诊断和不修复包权限表。

#### 示例

执行以下命令：

ohpm-repo install  --config D:\\config.yaml

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/xgdlrGHKRUqqTnaLMsvbUg/zh-cn_image_0000002530911294.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=D15355E98D772D1999CD6F1B52F9801AFE0B81B122567E3899F4410131BBAADA "点击放大")

#### 注意

安装成功后，必须根据给出的提示信息刷新环境变量，针对Windows系统和Linux/Mac系统，有不同处理方式：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/_ZElX8-bTbuiq_s1h-Pc0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=8F21DE0D3A9366A6AFF7935E9EA8F85FB49C01D77DF7C679DBC9DD81C7BE366C)

-   Windows系统： 关闭当前窗口，重新开启一个窗口。
-   Linux系统或Mac系统： 在命令行中执行环境变量刷新命令：source ~/.bashrc或者 . ~/.bashrc。
