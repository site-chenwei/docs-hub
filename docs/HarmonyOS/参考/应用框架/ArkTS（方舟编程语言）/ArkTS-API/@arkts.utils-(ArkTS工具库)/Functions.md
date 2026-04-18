---
title: "Functions"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-f"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkTS（方舟编程语言）"
  - "ArkTS API"
  - "@arkts.utils (ArkTS工具库)"
  - "Functions"
captured_at: "2026-04-17T01:47:51.604Z"
---

# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/C5dGOncRTW2JdnWy9AeEwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014753Z&HW-CC-Expire=86400&HW-CC-Sign=2C1660652C95B0394EAB0C7CEB1CF5137FA8D8ABD26BEEC0220CFAC9E3D60460)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

#### 导入模块

```ts
import { ArkTSUtils } from '@kit.ArkTS'
```

#### ArkTSUtils.isSendable

isSendable(value: Object | null | undefined): boolean

该方法用于判断value是否为Sendable数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | Object | null | undefined | 是 | 待校验的对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | value是否为Sendable数据类型，true表示value是Sendable数据类型，否则为false。 |

**示例：**

```ts
import { ArkTSUtils } from '@kit.ArkTS';

@Sendable
function sendableFunc() {
  console.info("sendableFunc");
}

if (ArkTSUtils.isSendable(sendableFunc)) {
  console.info("sendableFunc is Sendable");
} else {
  console.info("sendableFunc is not Sendable");
}
// 期望输出: 'SendableFunc is Sendable'
```
