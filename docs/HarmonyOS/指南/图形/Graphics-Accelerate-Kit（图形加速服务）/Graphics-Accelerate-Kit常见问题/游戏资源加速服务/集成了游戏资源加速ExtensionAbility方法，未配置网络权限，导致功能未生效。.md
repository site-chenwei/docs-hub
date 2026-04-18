---
title: "集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效。"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-3"
menu_path:
  - "指南"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "Graphics Accelerate Kit常见问题"
  - "游戏资源加速服务"
  - "集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效。"
captured_at: "2026-04-17T01:36:09.945Z"
---

# 集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效。

未配置网络权限将出现如下异常日志：

```typescript
ohos.permission.INTERNET check failed
```

请开发者在“src/main/module.json5”的requestPermissions层级中添加网络权限。

```typescript
{
  "module": {
    // ...
    "requestPermissions": [
      {
        "name": "ohos.permission.INTERNET"
      }
    ]
  }
}
```
