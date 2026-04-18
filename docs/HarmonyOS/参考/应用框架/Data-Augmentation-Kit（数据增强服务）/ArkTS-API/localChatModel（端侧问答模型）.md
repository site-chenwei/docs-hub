---
title: "localChatModel（端侧问答模型）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-localchatmodel-api"
menu_path:
  - "参考"
  - "应用框架"
  - "Data Augmentation Kit（数据增强服务）"
  - "ArkTS API"
  - "localChatModel（端侧问答模型）"
captured_at: "2026-04-17T01:48:14.638Z"
---

# localChatModel（端侧问答模型）

本模块提供接入端侧问答模型问答的方法，实现数据不出端的智能问答能力。

**起始版本：** 6.0.0(20)

#### 导入模块

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';
```

#### Config

是否支持流式问答的配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| isStream | boolean | 否 | 否 | 表示是否支持流式问答。true表示支持，false表示不支持。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

let localConfig: localChatModel.Config = {
  isStream: true
}
```

#### QuestionInfo

与端侧问答模型交互的问题信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| questionId | number | 否 | 否 | 表示与端侧问答模型交互的问题ID，ID取值范围为\[0,65535\]，在同一应用运行时，questionId应保持唯一性。 |
| content | string | 否 | 否 | 表示与端侧问答模型交互的问题内容，由于受到端侧性能的限制，建议content长度不超过4500字节。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

let questionInfo: localChatModel.QuestionInfo = {
  questionId: 1,
  content: "问题内容"
}
```

#### Answer

与端侧问答模型交互的返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| questionId | number | 否 | 否 | 表示问答模型返回结果对应的问题ID，与请求的questionId一致。 |
| content | string | 否 | 否 | 表示问答模型对于questionId对应的问题的问答结果。 |
| isFinished | boolean | 否 | 否 | 表示问答结果是否完整，true表示所有结果已完整返回，false表示结果未完整返回。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

let answer: localChatModel.Answer = {
  questionId: 1,
  content: "回答内容",
  isFinished: true
}
```

#### init

init(): Promise<boolean>

初始化端侧问答模型，使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回模型初始化结果，true表示成功，false表示失败。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

async function init() {
  try {
    const result = await localChatModel.init();
    console.info('init result: ', result);
  } catch (err) {
    console.error('init err: ', err);
  }
}
```

#### chat

chat(info: QuestionInfo, config: Config, callback: AsyncCallback<Answer>): Promise<void>

对端侧问答模型进行问答，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/6Px7rkJaSOKfT7wkK_y4tQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=35009938DCFBEFD74609DBD67156EA6FDF58569FC1498BB221FA6EBE83893647)

调用chat方法前需要先调用init方法初始化端侧问答模型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| info | [QuestionInfo](#questioninfo) | 是 | 表示与端侧问答模型问答的问题信息。 |
| config | [Config](#config) | 是 | 表示问题的配置选项。 |
| callback | AsyncCallback<[Answer](#answer)\> | 是 | 表示将问答的结果返回给调用方的回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-error-code)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [1021900001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-error-code#section1021900001-调用端侧问答模型超时) | A timeout occurs when the local chat model is called. |
| [1021900002](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-error-code#section1021900002-端侧问答模型加载失败) | A loading failure occurs when the local chat model is called. |
| [1021900003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-error-code#section1021900003-端侧问答模型请求失败) | A request failure occurs when the local chat model is called. |
| [1021900004](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-error-code#section1021900004-端侧问答模型繁忙) | The local chat model is busy. |
| [1021900005](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-error-code#section1021900005-某些参数不满足指定的约束条件) | Some parameters do not meet the specified constraints. |

**示例：**

```typescript
import { BusinessError } from "@kit.BasicServicesKit";
import { localChatModel } from '@kit.DataAugmentationKit';

async function chat() {
  let questionInfo: localChatModel.QuestionInfo = {
    questionId: 100,
    content: "你是一个翻译助手，可以翻译多国语言，请将以下内容翻译成36国语言：PC模型管家"
  }
  let localConfig: localChatModel.Config = {
    isStream: true
  }
  let localChatCallback = async (err: BusinessError, ans: localChatModel.Answer): Promise<void> => {
    if (err) {
      // 模型运行相关错误码
      console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      return;
    }
    console.info('questionId: ' + ans.questionId + ', content: ' + ans.content + ', isFinished: ' + ans.isFinished);
  };
  try {
    await localChatModel.chat(questionInfo, localConfig, localChatCallback);
  } catch (err) {
    // 入参相关错误码
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  }
}
```
