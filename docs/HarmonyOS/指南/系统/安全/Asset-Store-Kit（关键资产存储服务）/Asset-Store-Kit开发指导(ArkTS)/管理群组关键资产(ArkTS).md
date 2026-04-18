---
title: "管理群组关键资产(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-group-access-control"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "Asset Store Kit开发指导(ArkTS)"
  - "管理群组关键资产(ArkTS)"
captured_at: "2026-04-17T01:35:47.414Z"
---

# 管理群组关键资产(ArkTS)

以下为管理群组关键资产使用示例，请先查看开发指导：

-   [新增关键资产(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-add)
-   [删除关键资产(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-remove)
-   [更新关键资产(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-update)
-   [查询关键资产(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-query)

#### 前置条件

1.  在应用配置文件app.json5中，配置群组ID，如：demo\_group\_id。群组支持配置多个群组ID。
    
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
    
2.  引用头文件，定义工具函数。
    
    import { asset } from '@kit.AssetStoreKit';
    import { util } from '@kit.ArkTS';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function stringToArray(str: string): Uint8Array {
      let textEncoder = new util.TextEncoder();
      return textEncoder.encodeInto(str);
    }
    
    function arrayToString(arr: Uint8Array): string {
      let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
      let str = textDecoder.decodeToString(arr, { stream: false });
      return str;
    }
    

#### 新增群组关键资产

在群组中新增密码为demo\_pwd、别名为demo\_alias、附属信息为demo\_label的关键资产。

let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo\_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
attr.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label'));
attr.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
try {
  asset.add(attr).then(() => {
    console.info(\`Succeeded in adding Asset to the group.\`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(\`Failed to add Asset to the group. Code is ${err.code}, message is ${err.message}\`);
    // ...
  })
} catch (error) {
  let err = error as BusinessError;
  console.error(\`Failed to add Asset to the group. Code is ${err?.code}, message is ${err?.message}\`);
  // ...
}

#### 删除群组关键资产

在群组中删除别名为demo\_alias的关键资产。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // 此处指定别名删除单条群组关键资产，也可不指定别名删除多条群组关键资产。
query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
try {
  asset.remove(query).then(() => {
    console.info(\`Succeeded in removing Asset from the group.\`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(\`Failed to remove Asset from the group. Code is ${err.code}, message is ${err.message}\`);
    // ...
  });
} catch (err) {
  console.error(\`Failed to remove Asset from the group. Code is ${err?.code}, message is ${err?.message}\`);
  // ...
}

#### 更新群组关键资产

在群组中更新别名为demo\_alias的关键资产，明文更新为demo\_pwd\_new，附属属性更新为demo\_label\_new。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo\_pwd\_new'));
attrsToUpdate.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label\_new'));
try {
  asset.update(query, attrsToUpdate).then(() => {
    console.info(\`Succeeded in updating Asset in the group.\`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(\`Failed to update Asset in the group. Code is ${err.code}, message is ${err.message}\`);
    // ...
  });
} catch (err) {
  console.error(\`Failed to update Asset in the group. Code is ${err?.code}, message is ${err?.message}\`);
  // ...
}

#### 查询单条群组关键资产明文

在群组中查询别名为demo\_alias的关键资产明文。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ALL); // 此处表示需要返回群组关键资产的所有信息，即属性+明文。
query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
try {
  asset.query(query).then((res: Array<asset.AssetMap>) => {
    for (let i = 0; i < res.length; i++) {
      // 解析secret。
      let secret: Uint8Array = res\[i\].get(asset.Tag.SECRET) as Uint8Array;
      // 将Uint8Array转换为string类型。
      let secretStr: string = arrayToString(secret);
    }
    // ...
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query Asset plaintext from the group. Code is ${err.code}, message is ${err.message}\`);
    // ...
  });
} catch (err) {
  console.error(\`Failed to query Asset plaintext from the group. Code is ${err?.code}, message is ${err?.message}\`);
  // ...
}

#### 查询单条群组关键资产属性

在群组中查询别名为demo\_alias的关键资产属性。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ATTRIBUTES); // 此处表示仅返回群组关键资产属性，不包含群组关键资产明文。
query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
try {
  asset.query(query).then((res: Array<asset.AssetMap>) => {
    for (let i = 0; i < res.length; i++) {
      // 解析属性。
      let accessibility: number = res\[i\].get(asset.Tag.ACCESSIBILITY) as number;
      console.info(\`Succeeded in getting accessibility, which is: ${accessibility}.\`);
    }
    // ...
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query Asset attribute from the group. Code is ${err.code}, message is ${err.message}\`);
    // ...
  });
} catch (err) {
  console.error(\`Failed to query Asset attribute from the group. Code is ${err?.code}, message is ${err?.message}\`);
  // ...
}
