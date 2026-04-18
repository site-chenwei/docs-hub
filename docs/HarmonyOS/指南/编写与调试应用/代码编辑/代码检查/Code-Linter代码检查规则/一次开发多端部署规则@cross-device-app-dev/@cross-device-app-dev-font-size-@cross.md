---
title: "@cross"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "一次开发多端部署规则@cross-device-app-dev"
  - "@cross-device-app-dev/font-size"
captured_at: "2026-04-17T01:36:47.839Z"
---

# @cross-device-app-dev/font-size

字体大小要求至少为8fp以便于阅读。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/font-size": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

const FONT\_SIZE = 12;

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('message').fontSize(12)
      Text('message').fontSize('12fp')
    }
  }
}

#### 反例

const FONT\_SIZE = 7;

@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontSize(FONT\_SIZE)
      Text('message').fontSize('7fp')
    }
  }
}

#### 规则集

plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
