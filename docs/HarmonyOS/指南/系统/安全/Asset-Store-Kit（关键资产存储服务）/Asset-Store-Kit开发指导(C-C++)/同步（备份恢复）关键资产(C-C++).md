---
title: "同步（备份恢复）关键资产(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-sync"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "Asset Store Kit开发指导(C/C++)"
  - "同步（备份恢复）关键资产(C/C++)"
captured_at: "2026-04-17T01:35:47.525Z"
---

# 同步（备份恢复）关键资产(C/C++)

#### 添加依赖

在CMake脚本中链接相关动态库。

```txt
target_link_libraries(entry PUBLIC libasset_ndk.z.so)
```

引用头文件。

#include "napi/native\_api.h"
#include <string.h>
#include "asset/asset\_api.h"

#### 新增支持同步的关键资产

新增密码demo\_pwd（别名demo\_alias），附属信息为demo\_label，支持同步的关键资产。

static napi\_value AddSyncAsset(napi\_env env, napi\_callback\_info info)
{
    char \*secretStr = "demo\_pwd";
    char \*aliasStr = "demo\_alias";
    char \*labelStr = "demo\_label";

    Asset\_Blob secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_SECRET, .value.blob = secret},
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias},
        {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = label},
        {.tag = ASSET\_TAG\_SYNC\_TYPE, .value.u32 = ASSET\_SYNC\_TYPE\_TRUSTED\_DEVICE}, // 需指定在可信设备间同步（如新旧设备间克隆）。
    };

    int32\_t addResult = OH\_Asset\_Add(attr, sizeof(attr) / sizeof(attr\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, addResult, &ret);
    return ret;
}

#### 接入备份恢复扩展能力

为触发应用数据备份恢复，需要[应用接入数据备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-backup-extension)。

#### 查询关键资产同步结果

#### \[h2\]接口介绍

通过API文档查看查询关键资产同步结果接口OH\_Asset\_QuerySyncResult。

在查询关键资产时，关键资产属性的内容参数如下表所示。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| :-- | :-- | :-- | :-- |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 是 | 是否查询业务自定义附属信息被加密的关键资产同步结果。true表示查询业务自定义附属信息加密存储的关键资产同步结果，false表示查询业务自定义附属信息不加密存储的关键资产同步结果。默认值为false。 |
| ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8\[\]，长度为7-127字节。 | 是 | 待查询的关键资产所属群组，默认查询不属于任何群组的关键资产同步结果。 |

#### \[h2\]代码示例

static napi\_value QuerySyncResult(napi\_env env, napi\_callback\_info info)
{
    Asset\_SyncResult syncResult = {0};
    int32\_t queryResult = OH\_Asset\_QuerySyncResult(NULL, 0, &syncResult);
    napi\_value ret;
    napi\_create\_int32(env, queryResult, &ret);
    return ret;
}

#### 约束和限制

在可信设备间同步过程中，新旧设备的关键资产均需处于可访问的状态，否则可能出现关键资产无法同步的情况。

-   仅设置密码时可访问的关键资产，如果新旧设备中任意一台设备未设置锁屏密码，则无法同步成功。
    
-   仅屏幕处于解锁状态时可访问的关键资产，如果新旧设备中任意一台设备的屏幕未处于解锁状态，则无法同步成功。
    
-   仅用户认证通过后可访问的关键资产，如果旧设备未设置锁屏密码，则无法同步成功。
