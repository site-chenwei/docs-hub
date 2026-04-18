---
title: "查询关键资产(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-query"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "Asset Store Kit开发指导(C/C++)"
  - "查询关键资产(C/C++)"
captured_at: "2026-04-17T01:35:47.531Z"
---

# 查询关键资产(C/C++)

#### 接口介绍

可通过API文档查看查询关键资产的接口[OH\_Asset\_Query](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-api-h#oh_asset_query)的详细介绍。

在查询关键资产时，关键资产属性的内容参数如下表所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ETHWD_CsSxyYXgt2N_pGuw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=21B2F51433A2346F046C506F50CBC8C66A361A11F167EBCD0C6049677F3B44AD)

下表中“ASSET\_TAG\_ALIAS”和名称包含“ASSET\_TAG\_DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

查询关键资产明文ASSET\_TAG\_SECRET需要解密，查询时间较长，需要将Asset\_ReturnType设置为ASSET\_RETURN\_ALL；只查询其他关键资产属性不需解密，查询时间较短，需要将Asset\_ReturnType设置为ASSET\_RETURN\_ATTRIBUTES。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| :-- | :-- | :-- | :-- |
| ASSET\_TAG\_ALIAS | 类型为uint8\[\]，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
| ASSET\_TAG\_ACCESSIBILITY | 类型为uint32\_t，取值范围详见[Asset\_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h#asset_accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | 类型为bool。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示查询仅用户设置了锁屏密码才允许访问的关键资产；为false时表示查询无论用户是否设置锁屏密码，均可访问的关键资产。 |
| ASSET\_TAG\_AUTH\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_AuthType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h#asset_authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
| ASSET\_TAG\_SYNC\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_SyncType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h#asset_synctype)。 | 可选 | 关键资产支持的同步类型。 |
| ASSET\_TAG\_IS\_PERSISTENT | 类型为bool。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示查询应用卸载后会被保留的关键资产；为false时表示查询应用卸载后会被删除的关键资产。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_1 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 
关键资产附属信息，内容由业务自定义且有完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_2 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 

关键资产附属信息，内容由业务自定义且有完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_3 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 

关键资产附属信息，内容由业务自定义且有完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_4 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 

关键资产附属信息，内容由业务自定义且有完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 

关键资产附属信息，内容由业务自定义且无完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 

关键资产附属信息，内容由业务自定义且无完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 

关键资产附属信息，内容由业务自定义且无完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 

关键资产附属信息，内容由业务自定义且无完整性保护。

**说明：** API12前长度为1-512字节。

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为uint8\[\]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| ASSET\_TAG\_RETURN\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_ReturnType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h#asset_returntype)。 | 可选 | 关键资产查询返回的结果类型。 |
| ASSET\_TAG\_RETURN\_LIMIT | 类型为uint32\_t。 | 可选 | 关键资产查询返回的结果数量。 |
| ASSET\_TAG\_RETURN\_OFFSET | 类型为uint32\_t，取值范围：1-65536。 | 可选 | 

关键资产查询返回的结果偏移量。

**说明：** 用于分批查询场景，指定从第几个开始返回。

 |
| ASSET\_TAG\_RETURN\_ORDERED\_BY | 类型为uint32\_t，取值范围：ASSET\_TAG\_DATA\_LABEL\_xxx。 | 可选 | 

关键资产查询返回的结果排序依据，仅支持按照附属信息排序。

**说明：** 默认按照关键资产新增的顺序返回。

 |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 可选 | 是否查询业务自定义附属信息被加密的数据。为true时表示查询业务自定义附属信息加密存储的数据，为false时表示查询业务自定义附属信息不加密存储的数据。默认值为false。 |
| ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8\[\]，长度为7-127字节。 | 可选 | 待查询的关键资产所属群组，默认查询不属于任何群组的关键资产。 |

#### 约束和限制

批量查询出的关键资产需要通过IPC通道传输给业务，受IPC缓冲区大小限制，建议对查询超过40条关键资产时，进行分批查询，且每次查询数量不超过40条。

#### 代码示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/nsjEmLFTT96f9hVXxvNuJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=6DBAB654E2CEEB4ED2149E7B5A761AC43FB01C84A97A97FD02DCFAC5BC509183)

在查询前，需确保已有关键资产，可参考[指南文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-add)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

#### \[h2\]查询单条关键资产明文

查询别名是demo\_alias的关键资产明文。

在指定群组中查询一条关键资产明文的示例代码详见[查询单条群组关键资产明文](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-group-access-control#查询单条群组关键资产明文)。

1.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC libasset_ndk.z.so)
    ```
    
2.  引用头文件。
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  参考如下示例代码，进行业务功能开发。
    
    static napi\_value QueryAssetPlaintext(napi\_env env, napi\_callback\_info info)
    {
        const char \*aliasStr = "demo\_alias";
        
        Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // 指定了关键资产别名，最多查询到一条满足条件的关键资产。
            {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ALL}, // 此处表示需要返回关键资产的所有信息，即属性+明文。返回明文需要解密，查询时间较长。
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
    

#### \[h2\]查询单条关键资产属性

查询别名是demo\_alias的关键资产属性。

在指定群组中查询一条关键资产属性的示例代码详见[查询单条群组关键资产属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-group-access-control#查询单条群组关键资产属性)。

1.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC libasset_ndk.z.so)
    ```
    
2.  引用头文件。
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  参考如下示例代码，进行业务功能开发。
    
    static napi\_value QueryAssetAttribute(napi\_env env, napi\_callback\_info info)
    {
        const char \*aliasStr = "demo\_alias";
        
        Asset\_Blob alias = { (uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr };
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // 指定了关键资产别名，最多查询到一条满足条件的关键资产。
            {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ATTRIBUTES}, // 此处表示仅返回关键资产属性。返回属性不需解密，查询时间较短。
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
    

#### \[h2\]批量查询关键资产属性

批量查询标签为demo\_label的关键资产属性，共返回10条符合条件的查询结果，结果按ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1属性内容排序。

1.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC libasset_ndk.z.so)
    ```
    
2.  引用头文件。
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  参考如下示例代码，进行业务功能开发。
    
    static napi\_value QueryBatchAssetAttributes(napi\_env env, napi\_callback\_info info)
    {
        const char \*labelStr = "demo\_label";
        
        Asset\_Blob label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ATTRIBUTES},
            {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = label},
            {.tag = ASSET\_TAG\_RETURN\_LIMIT, .value.u32 = 10},
            {.tag = ASSET\_TAG\_RETURN\_ORDERED\_BY, .value.u32 = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1},
        };
    
        Asset\_ResultSet resultSet = { 0 };
        int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
        if (queryResult == ASSET\_SUCCESS) {
            // 解析结果。
            for (uint32\_t i = 0; i < resultSet.count; i++) {
                // 解析数据别名：其中别名是label->blob.data，长度对应是label->blob.size。
                Asset\_Attr \*alias = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_ALIAS);
            }
        }
        OH\_Asset\_FreeResultSet(&resultSet);
     
        napi\_value ret;
        napi\_create\_int32(env, queryResult, &ret);
        return ret;
    }
