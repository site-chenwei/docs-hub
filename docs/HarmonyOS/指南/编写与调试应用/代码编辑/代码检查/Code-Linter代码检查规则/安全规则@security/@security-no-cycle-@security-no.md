---
title: "@security/no"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-cycle"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "安全规则@security"
  - "@security/no-cycle"
captured_at: "2026-04-17T01:36:46.359Z"
---

# @security/no-cycle

该规则禁止使用循环依赖。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-cycle": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';

#### 反例

// foo.ets
import {} from './bar';

// bar.ets
import {} from './foo';

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/GSf1-0gxRuKt5SOkSdgFeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013647Z&HW-CC-Expire=86400&HW-CC-Sign=967CF120C0F10EF33C2CF33613556835EE95FF7CDB471F6DB14B916ED3D256EE)

反例中foo.ets文件依赖了bar.ets文件，bar.ets文件同时依赖了foo.ets文件，造成了循环依赖。

#### 规则集

plugin:@security/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
