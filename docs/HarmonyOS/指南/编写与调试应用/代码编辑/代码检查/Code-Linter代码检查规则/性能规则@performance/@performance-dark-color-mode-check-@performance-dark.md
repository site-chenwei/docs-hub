---
title: "@performance/dark"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-dark-color-mode-check"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "性能规则@performance"
  - "@performance/dark-color-mode-check"
captured_at: "2026-04-17T01:36:46.698Z"
---

# @performance/dark-color-mode-check

通过启用深色模式，可以进一步实现能耗的降低。应用需要根据当前设备状态来适配深色模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/e08dtyVyRv2xmhfF0n5uQQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013647Z&HW-CC-Expire=86400&HW-CC-Sign=4884BC767D5C020282EF5E356A973E98AD37ED09093A00B96C66009990EA8F02)

-   在检查整个工程时，该规则才生效。
-   code-linter.json5配置文件中的[overrides](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter#section19310459444)和[ignore](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter#section19310459444)字段对该规则不生效。
-   若想关闭该规则检查，可将code-linter.json5配置文件中[rules](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter#section19310459444)字段设置为off。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@performance/dark-color-mode-check": "suggestion",
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│               └── color.json     
│           
├── mock
│   └── mock-config.json5

#### 反例

src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│           
├── mock
│   └── mock-config.json5

#### 规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
