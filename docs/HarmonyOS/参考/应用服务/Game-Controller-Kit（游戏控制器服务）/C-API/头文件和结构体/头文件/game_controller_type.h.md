---
title: "game_controller_type.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller-type"
menu_path:
  - "参考"
  - "应用服务"
  - "Game Controller Kit（游戏控制器服务）"
  - "C API"
  - "头文件和结构体"
  - "头文件"
  - "game_controller_type.h"
captured_at: "2026-04-17T01:48:57.583Z"
---

# game\_controller\_type.h

#### 概述

定义GameController模块的通用枚举类型。

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：**[GameController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller)

#### 汇总

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef enum [GameController\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller#gamecontroller_errorcode) [GameController\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller#gamecontroller_errorcode) | 此枚举定义游戏控制器的错误码。 |

#### \[h2\]枚举

| 名称 | 描述 |
| :-- | :-- |
| 
[GameController\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller#gamecontroller_errorcode) {

GAME\_CONTROLLER\_SUCCESS = 0,

GAME\_CONTROLLER\_PARAM\_ERROR = 401,

GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR = 32200001,

GAME\_CONTROLLER\_NO\_MEMORY = 32200002

}

 | 游戏控制器错误码。 |
