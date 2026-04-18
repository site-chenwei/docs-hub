---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restore"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "ohpm-repo restore"
captured_at: "2026-04-17T01:36:42.512Z"
---

# ohpm-repo restore

将ohpm-repo pack打包产物替换<deploy\_root>目录下相应文件，重启服务。

#### 前提条件

-   已成功执行[start 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start)或者[restart 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart)，ohpm-repo服务启动成功。
-   已获得由[pack 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-pack)打包的.zip 文件。

#### 命令格式

ohpm-repo restore <file\_path>

#### 功能描述

该命令会停止当前ohpm-repo服务，并用打包文件<file\_path>中的内容替换ohpm-repo部署根目录<deploy\_root>的相应文件，然后重启ohpm-repo服务。该命令执行前必须已执行过ohpm-repo实例启动命令ohpm-repo start。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ZEWDl8jhRFaxH89Fl3qEcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=8662C77E033F67171D0145F1EED12378C397D27E456B89707A4F0FAC0C744409)

-   <file\_path>：由ohpm-repo pack命令得到的打包产物。

支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。

-   <deploy\_root>：ohpm-repo部署根目录 执行install命令后，会创建一个名为OHPM\_REPO\_DEPLOY\_ROOT的环境变量，记录的是[ohpm-repo私仓部署目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration#zh-cn_topic_0000001745376470_关于-deploy_root)。

#### 参数

#### \[h2\]<file\_path>

-   类型：String
-   必填参数

指定待解压的打包文件路径。

#### 示例

执行以下命令：

ohpm-repo restore "D:\\pack\_1702625827995.zip"

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/9pdyV3AsTZK201eCGjeJEg/zh-cn_image_0000002561831217.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=4D0B2917CC8CAB9CF5235248130A3F267456DB1B757D2DB3A1763AD7BBD25CBD "点击放大")
