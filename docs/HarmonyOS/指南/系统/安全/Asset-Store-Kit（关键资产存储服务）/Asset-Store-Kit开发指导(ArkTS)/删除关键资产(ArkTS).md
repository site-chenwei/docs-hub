---
title: "删除关键资产(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-remove"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "Asset Store Kit开发指导(ArkTS)"
  - "删除关键资产(ArkTS)"
captured_at: "2026-04-17T01:35:47.343Z"
---

# 删除关键资产(ArkTS)

#### 接口介绍

可通过API文档查询删除关键资产的异步接口[remove(query: AssetMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#assetremove)、同步接口[removeSync(query: AssetMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#assetremovesync12)的详细介绍。

在删除关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/e-TpzMoWSS-8IZ0G2axa3g/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=6760B8876EC8A3A0C64A23A1F29EA3FAF9E1717AA8070F8D6EECD883421AD829)

下表中“ALIAS”和名称包含“DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

| 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
| :-- | :-- | :-- | :-- |
| ALIAS | 类型为Uint8Array，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
| ACCESSIBILITY | 类型为number，取值范围详见[Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
| REQUIRE\_PASSWORD\_SET | 类型为boolean。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示删除仅用户设置了锁屏密码才允许访问的关键资产；为false时表示删除无论用户是否设置锁屏密码，均可访问的关键资产。 |
| AUTH\_TYPE | 类型为number，取值范围详见[AuthType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
| SYNC\_TYPE | 类型为number，取值范围详见[SyncType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#synctype)。 | 可选 | 关键资产支持的同步类型。 |
| IS\_PERSISTENT | 类型为boolean。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示删除应用卸载后会被保留的关键资产；为false时表示删除应用卸载后会被删除的关键资产。 |
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
| REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否删除业务自定义附属信息被加密的数据。为true时表示删除业务自定义附属信息加密存储的数据，为false时表示删除业务自定义附属信息不加密存储的数据。默认值为false。 |
| GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待删除的关键资产所属群组，默认删除不属于任何群组的关键资产。 |

#### 代码示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/2if-EhDqRFyJSH5bvsmgVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=2E69D415F3ECE03BBAAE9E7A0F89FEC4A9B23687E06337BFE9153BBB46794905)

本模块提供了异步和同步两套接口，以下为异步接口的使用示例，同步接口详见[@ohos.security.asset (关键资产存储服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset)。

在指定群组中删除一条关键资产的使用示例详见[删除群组关键资产](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-group-access-control#删除群组关键资产)。

在删除前，需确保已有关键资产，可参考[指南文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-add)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

删除一条别名是demo\_alias的关键资产。

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
    query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // 此处指定别名删除单条关键资产，也可不指定别名删除多条关键资产。
    try {
      asset.remove(query).then(() => {
        console.info(\`Succeeded in removing Asset.\`);
        // ...
      }).catch((err: BusinessError) => {
        console.error(\`Failed to remove Asset. Code is ${err.code}, message is ${err.message}\`);
        // ...
      });
    } catch (error) {
      let err = error as BusinessError;
      console.error(\`Failed to remove Asset. Code is ${err.code}, message is ${err.message}\`);
      // ...
    }
