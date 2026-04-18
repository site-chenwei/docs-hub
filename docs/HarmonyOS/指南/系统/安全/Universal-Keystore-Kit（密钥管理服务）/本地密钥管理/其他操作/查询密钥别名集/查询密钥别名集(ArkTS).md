---
title: "查询密钥别名集(ArkTS)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-list-aliases-arkts"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "其他操作"
  - "查询密钥别名集"
  - "查询密钥别名集(ArkTS)"
captured_at: "2026-04-17T01:35:51.962Z"
---

# 查询密钥别名集(ArkTS)

HUKS提供了接口供应用查询密钥别名集。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/YjESCNaLRkueD5E75bE1ig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013554Z&HW-CC-Expire=86400&HW-CC-Sign=3FBC9EE92B9B3E2002DB8D3EB923F98675C507D6475B3ACFDA61934B9D444434)

轻量级智能穿戴不支持查询密钥别名集功能。

从API 23开始支持[群组密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview)特性。

#### 开发步骤

1.  初始化密钥属性集，用于查询指定密钥别名集TAG。TAG仅支持[HUKS\_TAG\_AUTH\_STORAGE\_LEVEL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukstag)。
    
2.  调用接口[listAliases](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukslistaliases12)，查询密钥别名集。
    

/\*
 \* 以下查询密钥别名集Promise操作使用为例
 \*/
import { huks } from '@kit.UniversalKeystoreKit'

async function testListAliases() {
  /\* 1.初始化密钥属性集 \*/
  let queryProperties: Array<huks.HuksParam> = \[
    {
      tag: huks.HuksTag.HUKS\_TAG\_AUTH\_STORAGE\_LEVEL,
      value: huks.HuksAuthStorageLevel.HUKS\_AUTH\_STORAGE\_LEVEL\_DE
    }
  \];
  let queryOptions: huks.HuksOptions = {
    properties: queryProperties
  };

  try {
    /\* 2.查询密钥别名集 \*/
    let result: huks.HuksListAliasesReturnResult = await huks.listAliases(queryOptions);
    console.info(\`promise: listAliases success\`);
  } catch (error) {
    console.error(\`promise: listAliases fail\`);
    throw (error as Error);
  }
}
