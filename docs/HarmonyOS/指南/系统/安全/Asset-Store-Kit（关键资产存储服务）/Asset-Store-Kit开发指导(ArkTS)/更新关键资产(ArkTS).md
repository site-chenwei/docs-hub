---
title: "更新关键资产(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-update"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "Asset Store Kit开发指导(ArkTS)"
  - "更新关键资产(ArkTS)"
captured_at: "2026-04-17T01:35:47.424Z"
---

# 更新关键资产(ArkTS)

#### 接口介绍

可通过API文档查看更新关键资产的异步接口[update(query: AssetMap, attributesToUpdate: AssetMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#assetupdate)、同步接口[updateSync(query: AssetMap, attributesToUpdate: AssetMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#assetupdatesync12)的详细介绍。

在更新关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/_BGncd7qSl-p_Cmt8dtDHw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=09D24B9A75783AA547AB99397EDCBD0F33BC2EA8F7089D50AEAEB534A2B321B9)

下表中“ALIAS”和名称包含“DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

-   **query的参数列表：**
    
    | 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
    | :-- | :-- | :-- | :-- |
    | ALIAS | 类型为Uint8Array，长度为1-256字节。 | 必选 | 关键资产别名，每条关键资产的唯一索引。 |
    | ACCESSIBILITY | 类型为number，取值范围详见[Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
    | REQUIRE\_PASSWORD\_SET | 类型为boolean。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示更新仅用户设置了锁屏密码才允许访问的关键资产；为false时表示更新无论用户是否设置锁屏密码，均可访问的关键资产。 |
    | AUTH\_TYPE | 类型为number，取值范围详见[AuthType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
    | SYNC\_TYPE | 类型为number，取值范围详见[SyncType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#synctype)。 | 可选 | 关键资产支持的同步类型。 |
    | IS\_PERSISTENT | 类型为boolean。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示更新应用卸载后会被保留的关键资产；为false时表示更新应用卸载后会被删除的关键资产。 |
    | DATA\_LABEL\_CRITICAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    关键资产附属信息，内容由业务自定义且有完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_CRITICAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且有完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_CRITICAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且有完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_CRITICAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且有完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    | DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    | DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    | DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    | REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否更新业务自定义附属信息被加密的数据。为true时表示更新业务自定义附属信息加密存储的数据，为false时表示更新业务自定义附属信息不加密存储的数据。默认值为false。 |
    | GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待更新的关键资产所属群组，默认更新不属于任何群组的关键资产。 |
    
-   **attributesToUpdate的参数列表：**
    
    | 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
    | :-- | :-- | :-- | :-- |
    | SECRET | 类型为Uint8Array，长度为1-1024字节。 | 可选 | 关键资产明文。 |
    | DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 
    
    关键资产附属信息，内容由业务自定义且无完整性保护。
    
    **说明：** API12前长度为1-512字节。
    
     |
    | DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    | DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    | DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    | DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
    

#### 代码示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/4b2leQwTRrWyP2yNhiXNig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=C8A8E449689B4CCFDB9182C867FCF4EC3E6C724E759E8658629BD946630F5D26)

本模块提供了异步和同步两套接口，以下为异步接口的使用示例，同步接口详见[@ohos.security.asset (关键资产存储服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset)。

在指定群组中更新一条关键资产的使用示例详见[更新群组关键资产](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-group-access-control#更新群组关键资产)。

在更新前，需确保已有关键资产，可参考[指南文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-add)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

更新别名是demo\_alias的关键资产，将关键资产明文更新为demo\_pwd\_new，附属属性更新成demo\_label\_new。

1.  引用头文件，定义工具函数。
    
    import { asset } from '@kit.AssetStoreKit';
    import { util } from '@kit.ArkTS';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function stringToArray(str: string): Uint8Array {
      let textEncoder = new util.TextEncoder();
      return textEncoder.encodeInto(str);
    }
    
2.  参考如下示例代码，进行业务功能开发。
    
    let query: asset.AssetMap = new Map();
    query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
    let attrsToUpdate: asset.AssetMap = new Map();
    attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo\_pwd\_new'));
    attrsToUpdate.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label\_new'));
    try {
      asset.update(query, attrsToUpdate).then(() => {
        console.info(\`Succeeded in updating Asset.\`);
        // ...
      }).catch((err: BusinessError) => {
        console.error(\`Failed to update Asset. Code is ${err.code}, message is ${err.message}\`);
        // ...
      });
    } catch (error) {
      let err = error as BusinessError;
      console.error(\`Failed to update Asset. Code is ${err.code}, message is ${err.message}\`);
      // ...
    }
