---
title: "@ohos.net.sharing (网络共享管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-sharing"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.net.sharing (网络共享管理)"
captured_at: "2026-04-17T01:48:22.640Z"
---

# @ohos.net.sharing (网络共享管理)

网络共享管理模块用于将设备网络连接共享给其他连接设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/hjl4Hf8uRP-oYlbDkmw6vA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A7471B4E499F69BA0E0AA7C86C5F992ABA66AD377CAE31CF732CCB3481FAADF8)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { sharing } from '@kit.NetworkKit';
```

#### NetHandle

type NetHandle = connection.NetHandle

数据网络的句柄。在调用NetHandle的方法之前，需要先获取NetHandle对象。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| :-- | :-- |
| [connection.NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#nethandle) | 网络链路信息。 |
