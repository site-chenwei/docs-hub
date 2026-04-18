---
title: "DECLARE_ERRORNO"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-declare-errorno"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "DECLARE_ERRORNO"
captured_at: "2026-04-17T01:36:38.337Z"
---

# DECLARE\_ERRORNO

错误码及描述注册宏，该宏对外提供如下四个错误码供开发者使用：

-   SUCCESS：成功。
    
-   FAILED：失败。
    
-   PARAM\_INVALID：参数不合法。
    
-   SCOPE\_NOT\_CHANGED：Scope融合规则未匹配到，忽略当前pass。
    

声明如下所示：

```cpp
DECLARE_ERRORNO(0, 0, SUCCESS, 0);
DECLARE_ERRORNO(0xFF, 0xFF, FAILED, 0xFFFFFFFF);
DECLARE_ERRORNO_COMMON(PARAM_INVALID, 1);  // 50331649
DECLARE_ERRORNO(SYSID_FWK, 1, SCOPE_NOT_CHANGED, 201);
```

开发者可以在“compiler安装目录/latest/compiler/include/register/register\_error\_codes.h”下查看错误码定义。
