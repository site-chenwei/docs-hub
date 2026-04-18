---
title: "js标签配置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-tag"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Lite）"
  - "框架说明"
  - "js标签配置"
captured_at: "2026-04-17T01:48:06.151Z"
---

# js标签配置

js标签中包含了实例名称、页面路由信息。

| 标签 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | default | 是 | 标识JS实例的名字。 |
| pages | Array | \- | 是 | 路由信息，详见“[pages](#pages)”。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/fSQU2Ih0SfW6vEeCvlG37w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=2D39786BA4009ED9B52D36AF85596F6E4DEA35013DE4BF85E35FA81BDA36045C)

name、pages标签配置需在配置文件中的“js”标签中完成设置。

#### pages

定义每个页面的路由信息，每个页面由页面路径和页面名组成，页面的文件名即为页面名，例如：

```json
{
  // ...
  "pages": [
    "pages/index/index",
    "pages/detail/detail"
  ]
  // ...
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/q_q2iEFsQxW-GCS6t0Ajuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=FA2DF396DB89D9025ECDB7C6A6A7E4A9493D0F4CEE6E2016EB2BE3E480349F48)

-   应用首页固定为"pages/index/index"。
    
-   页面文件名不能使用组件名称，比如：text.hml、button.hml等。
    

#### 示例

```json
{
  "app": {
    "bundleName": "com.example.player",
    "version": {
        "code": 1,
        "name": "1.0"
    },
    "vendor": "example"
  },
  "module": {
    // ...
    "js": [
      {
        "name": "default",
        "pages": [
          "pages/index/index",
          "pages/detail/detail"
        ]
      }
    ],
    "abilities": [
      {
        // ...
      }
    ]
  }
}
```
