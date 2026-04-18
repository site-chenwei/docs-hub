---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-remove_instance"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "ohpm-repo remove_instance"
captured_at: "2026-04-17T01:36:42.545Z"
---

# ohpm-repo remove\_instance

删除本机实例信息。

#### 前提条件

-   已成功执行[start 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start)或者[restart 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart)，ohpm-repo服务启动成功。
-   数据存储db模块的类型必须为mysql，文件存储store模块的类型必须为sftp或custom。

#### 命令格式

ohpm-repo remove\_instance

#### 功能描述

该命令会停止当前运行的ohpm-repo服务，同时删除本机在mysql和sftp中的实例信息。命令要求数据存储db模块必须使用mysql，文件存储store模块必须使用sftp或custom。

#### 示例

执行以下命令：

ohpm-repo remove\_instance

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/2JJl1RHBRNec4iMQZwi4xQ/zh-cn_image_0000002561751221.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=AC58A16BF1992C8063F364EA852142C17C49D486C2AC1136D5C3D1BD772399D5 "点击放大")
