---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-import-pkgpermission"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "数据迁移相关命令"
  - "ohpm-repo import_pkgPermission"
captured_at: "2026-04-17T01:36:42.638Z"
---

# ohpm-repo import\_pkgPermission

ohpm-repo 5.4.0版本开始，支持导入包权限数据。

#### 前提条件

已成功执行 [export\_userinfo 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo)、[import\_userinfo 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-import-userinfo)、[batch\_download 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-batch-download)、[batch\_publish 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-batch-publish)、[export\_pkgPermission 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-pkgpermission)，确保每个包指定的包文件、用户和组织都存在。

#### 命令格式

ohpm-repo import\_pkgPermission <pkg\_permission\_list> \[options\]

#### 功能描述

根据提供的记录着包权限数据的.json文件，向ohpm-repo导入包权限数据。

#### 参数

#### \[h2\]<pkg\_permission\_list>

-   类型： String
-   必填参数

在import\_pkgPermission命令后面配置<pkg\_permission\_list>参数，指定执行[export\_pkgPermission 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-pkgpermission)导出的.json文件。

#### 选项

#### \[h2\]--mode

-   类型：String
-   必填参数

用于指定包权限的导入模式，在import\_pkgPermission命令后通过--mode <mode>格式配置，mode有三种不同模式：merge-origin、merge-target、override。

**merge-origin模式**：保留源数据的可见性配置，合并源数据与ohpm-repo的包权限（以ohpm-repo权限为主），取权限并集。

| 
源数据可见性

 | 

ohpm-repo可见性

 | 

最终可见性

 | 

最终包权限

 |
| :-- | :-- | :-- | :-- |
| 

授权可读

 | 

授权可读

 | 

授权可读

 | 

源数据与ohpm-repo的所有者、维护者、查看者权限并集

 |
| 

公开可读

 |
| 

公开可读

 | 

授权可读

 | 

公开可读

 | 

源数据与ohpm-repo的所有者、维护者权限并集

 |
| 

公开可读

 |

**merge-target 模式：**处理规则：保留ohpm-repo的可见性配置，合并源数据与ohpm-repo的包权限（以ohpm-repo权限为主），取权限并集。

| 
源数据可见性

 | 

ohpm-repo可见性

 | 

最终可见性

 | 

最终包权限

 |
| :-- | :-- | :-- | :-- |
| 

授权可读

 | 

授权可读

 | 

授权可读

 | 

源数据与ohpm-repo的所有者、维护者、查看者权限并集

 |
| 

公开可读

 |
| 

授权可读

 | 

公开可读

 | 

公开可读

 | 

源数据与ohpm-repo的所有者、维护者权限并集

 |
| 

公开可读

 |

**override 模式：**删除ohpm-repo中对应包的所有包权限数据，完全使用源数据替代。

| 
源数据可见性

 | 

ohpm-repo可见性

 | 

最终可见性

 | 

最终包权限

 |
| :-- | :-- | :-- | :-- |
| 

授权可读

 | 

授权可读

 | 

授权可读

 | 

源数据中的所有者、维护者、查看者权限

 |
| 

公开可读

 |
| 

公开可读

 | 

授权可读

 | 

公开可读

 | 

源数据中的所有者、维护者权限

 |
| 

公开可读

 |

\--target-repo

-   默认值：无
-   类型： string

当[export\_pkgPermission命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-pkgpermission)导出的json文件中仅包含一个仓库的包权限数据时，可在import\_pkgPermission命令后面配置--target-repo <string>，用于指定待导入的仓库名称。

#### 示例

**以****merge-origin****模式导入包权限**

ohpm-repo import\_pkgPermission <pkg\_permission\_list> --mode merge-origin

结果示例：

PS D:\\> ohpm-repo import\_pkgPermission D:\\packagePermission\_1758008466123.json --mode merge-origin
...
\[2025-09-17T14:44:38.451\] \[INFO\] default - > start importing package permissions to the "ohpm" repository.
\[2025-09-17T14:44:38.459\] \[INFO\] default - import package permissions completed.
