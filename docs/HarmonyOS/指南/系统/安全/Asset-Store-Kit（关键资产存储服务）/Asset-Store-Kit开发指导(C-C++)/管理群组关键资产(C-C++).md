---
title: "管理群组关键资产(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-group-access-control"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "Asset Store Kit开发指导(C/C++)"
  - "管理群组关键资产(C/C++)"
captured_at: "2026-04-17T01:35:47.516Z"
---

# 管理群组关键资产(C/C++)

以下为管理群组关键资产使用示例，请先查看开发指导：

-   [新增关键资产(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-add)
-   [删除关键资产(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-remove)
-   [更新关键资产(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-update)
-   [查询关键资产(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-query)

#### 前置条件

在应用配置文件app.json5中，配置群组ID，如：demo\_group\_id。群组支持配置多个群组ID。

```json5
{
  "app": {
    // 其他配置项此处省略。
    "assetAccessGroups": [
      "demo_group_id",
      // "another_group_id",
      // ...
    ]
  }
}
```

引用头文件。

#include "napi/native\_api.h"
#include <string.h>
#include "asset/asset\_api.h"

#### 新增群组关键资产

在群组中新增密码为demo\_pwd、别名为demo\_alias、附属信息为demo\_label的关键资产。

static napi\_value AddGroupAsset(napi\_env env, napi\_callback\_info info)
{
    const char \*secretStr = "demo\_pwd";
    const char \*aliasStr = "demo\_alias";
    const char \*labelStr = "demo\_label";
    const char \*groupIdStr = "demo\_group\_id";

    Asset\_Blob secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
    Asset\_Blob group\_id = { (uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_SECRET, .value.blob = secret},
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias},
        {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = label},
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    int32\_t addResult = OH\_Asset\_Add(attr, sizeof(attr) / sizeof(attr\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, addResult, &ret);
    return ret;
}

#### 删除群组关键资产

在群组中删除别名为demo\_alias的关键资产。

static napi\_value RemoveGroupAsset(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*groupIdStr = "demo\_group\_id";

    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob group\_id = {(uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // 此处指定别名删除单条群组关键资产，也可不指定别名删除多条群组关键资产。
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    int32\_t removeResult = OH\_Asset\_Remove(attr, sizeof(attr) / sizeof(attr\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, removeResult, &ret);
    return ret;
}

#### 更新群组关键资产

在群组中更新别名为demo\_alias的关键资产，将关键资产的明文更新为demo\_pwd\_new，附属信息更新为demo\_label\_new。

static napi\_value UpdateGroupAsset(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*secretStr = "demo\_pwd\_new";
    const char \*labelStr = "demo\_label\_new";
    const char \*groupIdStr = "demo\_group\_id";

    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob new\_secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
    Asset\_Blob new\_label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
    Asset\_Blob group\_id = {(uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr query\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias},
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };
    Asset\_Attr attributesToUpdate\[\] = {
        {.tag = ASSET\_TAG\_SECRET, .value.blob = new\_secret},
        {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = new\_label},
    };

    int32\_t updateResult = OH\_Asset\_Update(query, sizeof(query) / sizeof(query\[0\]), attributesToUpdate,
                                           sizeof(attributesToUpdate) / sizeof(attributesToUpdate\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, updateResult, &ret);
    return ret;
}

#### 查询单条群组关键资产明文

在群组中查询别名为demo\_alias的关键资产明文。

static napi\_value QueryGroupAssetPlaintext(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*groupIdStr = "demo\_group\_id";
    
    Asset\_Blob alias = { (uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr };
    Asset\_Blob group\_id = { (uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr };
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
        {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ALL}, // 此处表示需要返回群组关键资产的所有信息，即属性+明文。
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    Asset\_ResultSet resultSet = {0};
    int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
    if (queryResult == ASSET\_SUCCESS) {
        // 解析resultSet。
        for (uint32\_t i = 0; i < resultSet.count; i++) {
            // 解析secret属性：其中data数据对应是secret->blob.data，长度对应是secret->blob.size。
            Asset\_Attr \*secret = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_SECRET);
        }
    }
    OH\_Asset\_FreeResultSet(&resultSet);
    
    napi\_value ret;
    napi\_create\_int32(env, queryResult, &ret);
    return ret;
}

#### 查询单条群组关键资产属性

查询别名为demo\_alias的关键资产属性。

static napi\_value QueryGroupAssetAttribute(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*groupIdStr = "demo\_group\_id";
    
    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob group\_id = {(uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
        {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ATTRIBUTES}, // 此处表示仅返回群组关键资产属性，不包含群组关键资产明文。
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    Asset\_ResultSet resultSet = {0};
    int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
    if (queryResult == ASSET\_SUCCESS) {
        // 解析结果。
        for (uint32\_t i = 0; i < resultSet.count; i++) {
            // 解析数据标签：其中数据是label->blob.data，长度对应是label->blob.size。
            Asset\_Attr \*label = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1);
        }
    }
    OH\_Asset\_FreeResultSet(&resultSet);
    
    napi\_value ret;
    napi\_create\_int32(env, queryResult, &ret);
    return ret;
}
