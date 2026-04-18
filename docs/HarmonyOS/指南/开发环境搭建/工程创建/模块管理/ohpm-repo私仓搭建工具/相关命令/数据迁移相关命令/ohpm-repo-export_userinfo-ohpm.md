---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "数据迁移相关命令"
  - "ohpm-repo export_userinfo"
captured_at: "2026-04-17T01:36:42.633Z"
---

# ohpm-repo export\_userinfo

导出用户必要的DB数据。

#### 命令格式

ohpm-repo export\_userinfo

#### 功能描述

在当前的工作目录导出记录了DB数据的export\_userInfo\_xxx.zip文件，其中包含加密组件和下面的10张数据表。

-   user
-   group\_member
-   public\_key
-   access\_token
-   uplink
-   uplink\_proxy
-   repo
-   repo\_permission
-   validation\_config
-   system\_security

#### 示例

执行以下命令：

ohpm-repo export\_userinfo

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/gZXoVW__QZSSgBj4Ff5C1A/zh-cn_image_0000002530751298.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=9A7B47A4B8DED6C5D7EE3C11B7DB8A88BC8FD10B0BA4EC52FD8B62CBF905A43D "点击放大")

PS D:\\> ohpm-repo export\_userinfo
\[2025-08-09T19:14:16.721\] \[INFO\] default - initialize "file database" successfully.
\[2025-08-09T19:14:16.724\] \[INFO\] default - export the "user" table done.
\[2025-08-09T19:14:16.726\] \[INFO\] default - export the "group\_member" table done.
\[2025-08-09T19:14:16.728\] \[INFO\] default - export the "access\_token" table done.
\[2025-08-09T19:14:16.728\] \[INFO\] default - export the "public\_key" table done.
\[2025-08-09T19:14:16.730\] \[INFO\] default - export the "repo" table done.
\[2025-08-09T19:14:16.730\] \[INFO\] default - export the "repo\_permission" table done.
\[2025-08-09T19:14:16.731\] \[INFO\] default - export the "uplink" table done.
\[2025-08-09T19:14:16.732\] \[INFO\] default - export the "uplink\_proxy" table done.
\[2025-08-09T19:14:16.733\] \[INFO\] default - export the "validation\_config" table done.
\[2025-08-09T19:14:16.734\] \[INFO\] default - export the "system\_security" table done.
\[2025-08-09T19:14:16.761\] \[INFO\] default - userinfo exported completed, save the .zip file to : "D:\\export\_userInfo\_1754738056722.zip".

export\_userInfo\_1754738056722.zip文件结构

|   access\_token.json
|   group\_member.json
|   public\_key.json
|   repo.json
|   repo\_permission.json
|   system\_security.json
|   uplink.json
|   uplink\_proxy.json
|   user.json
|   validation\_config.json
\\---meta
    |   version.txt
    +---ac
    +---ce
    \\---fd
