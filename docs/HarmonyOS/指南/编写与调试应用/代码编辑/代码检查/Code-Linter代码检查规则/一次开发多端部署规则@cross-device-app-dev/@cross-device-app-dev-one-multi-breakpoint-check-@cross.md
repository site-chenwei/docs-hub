---
title: "@cross"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-one-multi-breakpoint-check"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "一次开发多端部署规则@cross-device-app-dev"
  - "@cross-device-app-dev/one-multi-breakpoint-check"
captured_at: "2026-04-17T01:36:47.896Z"
---

# @cross-device-app-dev/one-multi-breakpoint-check

一多特性必须使用系统断点判断是否开启，不能通过设备类型、设备方向或是否可折叠等属性来判断。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/one-multi-breakpoint-check": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

@Entry
@Component
struct ItemComponent {
  private currentWidthBreakpoint: string = '';
  build() {
    // 必须使用断点进行判断
    if (this.currentWidthBreakpoint === 'lg') {
    }
  }
}

#### 反例

import { display } from '@kit.ArkUI';
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct ItemComponent {
  build() {
    // 使用设备类型、是否可折叠等属性进行判断，告警
    if (deviceInfo.deviceType === 'phone' && display.isFoldable()) {
    }
  }
}

#### 规则集

plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
