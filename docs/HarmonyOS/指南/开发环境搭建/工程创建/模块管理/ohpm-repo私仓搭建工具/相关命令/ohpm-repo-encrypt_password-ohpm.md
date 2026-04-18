---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-encrypt_password"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "ohpm-repo encrypt_password"
captured_at: "2026-04-17T01:36:42.472Z"
---

# ohpm-repo encrypt\_password

对键入的密码类型字符串进行加密。

#### 命令格式

ohpm-repo encrypt\_password \[options\]

#### 功能描述

使用指定的加密组件加密从标准输入读取的数据，并在标准输出中输出密文。

#### 选项

#### \[h2\]crypto\_path

-   类型：String
-   必填参数

必须在encrypt\_password命令后面配置--crypto\_path <string>参数，指定加密组件的路径。如果是完整组件，将用该组件对键入的密码内容进行加密。如果是一个空目录，则命令将生成新的加密组件并对键入的密码内容进行加密。

#### 示例

执行以下命令：

ohpm-repo encrypt\_password --crypto\_path D:\\encryptPath

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DDTgmu62SHKN3kr6jIruPQ/zh-cn_image_0000002561831189.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=57C70766EA4558FC945D080C017DC897111E364FA56CB5B99C0F5D56522EC2BE)
