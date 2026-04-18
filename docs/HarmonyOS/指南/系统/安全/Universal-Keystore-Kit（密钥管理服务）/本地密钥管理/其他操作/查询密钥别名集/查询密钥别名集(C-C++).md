---
title: "查询密钥别名集(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-list-aliases-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "其他操作"
  - "查询密钥别名集"
  - "查询密钥别名集(C/C++)"
captured_at: "2026-04-17T01:35:51.971Z"
---

# 查询密钥别名集(C/C++)

HUKS提供了接口供应用查询密钥别名集。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Zc9v4D1uQJer6LNxxcirTg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013554Z&HW-CC-Expire=86400&HW-CC-Sign=4D65C68F393B04892ABBCCBF4D2293F8CEF5DEF7CEDFB4FBA1F79D212F8FF396)

轻量级智能穿戴不支持查询密钥别名集功能。

从API 23开始支持[群组密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview)特性。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

1.  初始化密钥属性集。用于查询指定密钥别名集TAG，TAG仅支持[OH\_HUKS\_TAG\_AUTH\_STORAGE\_LEVEL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_tag)。
    
2.  调用接口[OH\_Huks\_ListAliases](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_listaliases)，查询密钥别名集。
    

/\* 以下查询密钥别名集为例 \*/
#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <string.h>

OH\_Huks\_Result InitParamSet(
   struct OH\_Huks\_ParamSet \*\*paramSet,
   const struct OH\_Huks\_Param \*params,
   uint32\_t paramCount)
{
   OH\_Huks\_Result ret = OH\_Huks\_InitParamSet(paramSet);
   if (ret.errorCode != OH\_HUKS\_SUCCESS) {
       return ret;
   }
   ret = OH\_Huks\_AddParams(\*paramSet, params, paramCount);
   if (ret.errorCode != OH\_HUKS\_SUCCESS) {
       OH\_Huks\_FreeParamSet(paramSet);
       return ret;
   }
   ret = OH\_Huks\_BuildParamSet(paramSet);
   if (ret.errorCode != OH\_HUKS\_SUCCESS) {
       OH\_Huks\_FreeParamSet(paramSet);
       return ret;
   }
   return ret;
}

struct OH\_Huks\_Param g\_testQueryParam\[\] = {
   {
       .tag = OH\_HUKS\_TAG\_AUTH\_STORAGE\_LEVEL,
       .uint32Param = OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_DE
   },
};

static napi\_value ListAliases(napi\_env env, napi\_callback\_info info)
{
   struct OH\_Huks\_ParamSet \*testQueryParamSet = nullptr;
   struct OH\_Huks\_KeyAliasSet \*outData = nullptr;
   struct OH\_Huks\_Result ohResult;
   do {
       /\* 1.初始化密钥属性集 \*/
       ohResult = InitParamSet(&testQueryParamSet, g\_testQueryParam,
           sizeof(g\_testQueryParam) / sizeof(OH\_Huks\_Param));
       if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
           break;
       }
       /\* 2.查询密钥别名集 \*/
       ohResult = OH\_Huks\_ListAliases(testQueryParamSet, &outData);
   } while (0);

   OH\_Huks\_FreeParamSet(&testQueryParamSet);
   OH\_Huks\_FreeKeyAliasSet(outData);
   napi\_value ret;
   napi\_create\_int32(env, ohResult.errorCode, &ret);
   return ret;
}
