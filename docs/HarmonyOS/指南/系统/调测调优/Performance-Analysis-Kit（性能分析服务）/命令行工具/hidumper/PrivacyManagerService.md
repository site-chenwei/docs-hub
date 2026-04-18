---
title: "PrivacyManagerService"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper-privacymanagerservice"
menu_path:
  - "指南"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "命令行工具"
  - "hidumper"
  - "PrivacyManagerService"
captured_at: "2026-04-17T01:36:02.650Z"
---

# PrivacyManagerService

PrivacyManagerService是访问控制基于[hidumper](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper)增强开发的命令行能力，可显示访问控制基础信息，获取敏感权限使用记录。

#### 环境准备

根据hidumper工具指导，完成[环境准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#环境要求)。

#### 获取帮助信息

如果需要查看帮助信息，可以通过下列命令实现。

```shell
hidumper -s PrivacyManagerService -a '-h'
```

**使用样例：**

```text
-------------------------------[ability]-------------------------------

----------------------------------PrivacyManagerService----------------------------------
Privacy Dump:
Usage:
       -h: command help
       -t <TOKEN_ID>: according to specific token id dump permission used records
```

#### 获取敏感权限使用记录信息

支持通过应用进程的tokenid，查看敏感权限使用记录的信息，可以通过下列命令实现。

```shell
hidumper -s PrivacyManagerService -a '-t <tokenId>'
```

命令所需的tokenId可以通过[atm-tool](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/atm-tool#查询命令)进行查询。

**使用样例：**

```text
hidumper -s PrivacyManagerService -a '-t 536992218'

-------------------------------[ability]-------------------------------

----------------------------------PrivacyManagerService----------------------------------
Privacy Dump:
{
  "permissionRecord": [
    {
      "bundleName": "com.ohos.camera",
      "isRemote": false,
      "permissionName": "ohos.permission.READ_IMAGEVIDEO",
      "lastAccessTime": 1508577149393,
      "lastAccessDuration": 0,
      "accessCount": 2
    }
  ]
}
```
