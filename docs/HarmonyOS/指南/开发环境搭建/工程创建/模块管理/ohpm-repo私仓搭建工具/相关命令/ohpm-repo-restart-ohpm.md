---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "ohpm-repo restart"
captured_at: "2026-04-17T01:36:42.427Z"
---

# ohpm-repo restart

重新启动ohpm-repo服务。

#### 前提条件

已成功执行[install命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install)，并按要求刷新环境变量。

#### 命令格式

ohpm-repo restart 

#### 功能描述

停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/mCTieitgRNaBKsDG7VgZAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=BB65127C9EA6BA30366650C5C43721B3C54DB760E6E339BF033937B71072DA3B)

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件，其中<deploy\_root>为[ohpm-repo私仓部署目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration#zh-cn_topic_0000001745376470_关于-deploy_root)。

#### 示例

执行以下命令：

ohpm-repo restart

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/vUx-VscCRl6zPtWz-YdY8g/zh-cn_image_0000002561751491.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=7B99F8E50799C82C030AA397A19A3EE0BCC8DFBFA1E1BF54495F68C6457E905E "点击放大")
