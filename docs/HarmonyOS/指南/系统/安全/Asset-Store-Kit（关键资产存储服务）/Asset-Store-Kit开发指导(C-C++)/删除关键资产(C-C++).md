---
title: "删除关键资产(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-remove"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "Asset Store Kit开发指导(C/C++)"
  - "删除关键资产(C/C++)"
captured_at: "2026-04-17T01:35:47.514Z"
---

# 删除关键资产(C/C++)

#### 接口介绍

可通过API文档查看删除关键资产的接口[OH\_Asset\_Remove](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-api-h#oh_asset_remove)的详细介绍。

在删除关键资产时，关键资产属性的内容参数如下表所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/-u5dfRjWSqGP-4UlDf4pmQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=CB411B29056A344EA635CCFD693B1B1A74613881F45A96228603564A10B74501)

下表中“ASSET\_TAG\_ALIAS”和名称包含“ASSET\_TAG\_DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| :-- | :-- | :-- | :-- |
| ASSET\_TAG\_ALIAS | 类型为uint8\[\]，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
| ASSET\_TAG\_ACCESSIBILITY | 类型为uint32\_t，取值范围详见[Asset\_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h#asset_accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | 类型为bool。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示删除仅用户设置了锁屏密码才允许访问的关键资产；为false时表示删除无论用户是否设置锁屏密码，均可访问的关键资产。 |
| ASSET\_TAG\_AUTH\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_AuthType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h#asset_authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
| ASSET\_TAG\_SYNC\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_SyncType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h#asset_synctype)。 | 可选 | 关键资产支持的同步类型。 |
| ASSET\_TAG\_IS\_PERSISTENT | 类型为bool。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示删除应用卸载后会被保留的关键资产；为false时表示删除应用卸载后会被删除的关键资产。 |
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
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 可选 | 是否删除业务自定义附属信息被加密的数据。为true时表示删除业务自定义附属信息加密存储的数据，为false时表示删除业务自定义附属信息不加密存储的数据。默认值为false。 |
| ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8\[\]，长度为7-127字节。 | 可选 | 待删除的关键资产所属群组，默认删除不属于任何群组的关键资产。 |

#### 代码示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/jTSFS7X_RdOdtlmKmkZV-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=01934ACC156366C8EAC837DB4C9D04E5E2ACD10373A32E8CA4CDF444BEB029E7)

在删除前，需确保已有关键资产，可参考[指南文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-add)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

删除别名是demo\_alias的关键资产。

在指定群组中删除一条关键资产的示例代码详见[删除群组关键资产](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-group-access-control#删除群组关键资产)。

1.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC libasset_ndk.z.so)
    ```
    
2.  引用头文件。
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  参考如下示例代码，进行业务功能开发。
    
    static napi\_value RemoveAsset(napi\_env env, napi\_callback\_info info)
    {
        const char \*aliasStr = "demo\_alias";
        
        Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // 此处指定别名删除单条关键资产，也可不指定别名删除多条关键资产。
        };
    
        int32\_t removeResult = OH\_Asset\_Remove(attr, sizeof(attr) / sizeof(attr\[0\]));
        napi\_value ret;
        napi\_create\_int32(env, removeResult, &ret);
        return ret;
    }
