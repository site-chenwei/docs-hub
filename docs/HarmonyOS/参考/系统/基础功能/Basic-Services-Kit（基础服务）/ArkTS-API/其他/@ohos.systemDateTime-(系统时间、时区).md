---
title: "@ohos.systemDateTime (系统时间、时区)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "其他"
  - "@ohos.systemDateTime (系统时间、时区)"
captured_at: "2026-04-17T01:48:28.447Z"
---

# @ohos.systemDateTime (系统时间、时区)

本模块主要由系统时间和系统时区功能组成。开发者可以获取系统时间及系统时区。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/tCZsHZaTSBKmjgqkp-L1Bw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=5CBD6D81EC3334D2DF2705233E101A9718C32A11A54A98529F2E85CFC66A8BE5)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { systemDateTime } from '@kit.BasicServicesKit';
```

#### TimeType10+

定义获取时间的枚举类型。

**系统能力**: SystemCapability.MiscServices.Time

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STARTUP | 0 | 自系统启动以来经过的毫秒数，包括深度睡眠时间。 |
| ACTIVE | 1 | 自系统启动以来经过的毫秒数，不包括深度睡眠时间。 |

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/spRTlZ1LShWs4ToyjwNvQQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=5021989DB9BA57962684D7A80866114A82B5C2F3B23559D36EC306337AD8407F)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getTime10+](#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 是 | 
返回结果是否为纳秒数。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间戳。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Vn75KK1RRuGR6y3sTqfmZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=F35959A540DEC538D8D24084E2FB4526932F5FBFB6AE4BF4B902C8A28115B676)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getTime10+](#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间戳（ms）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano?: boolean): Promise<number>

获取自Unix纪元以来经过的时间，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/btP6IzlTT_SgBDFXgvz4Zg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C0B4AC280C8C6FEC3DA5F8B42A3604CD7C570E719F1333B58B6CA613F987A423)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getTime10+](#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 否 | 
返回结果是否为纳秒数,默认值为false。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回自Unix纪元以来经过的时间戳。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime().then((time: number) => {
    console.info(`Succeeded in getting currentTime : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/lxHP3Rq2SEuQQ_ihsoEEsg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C5080FFB50F190EFB0BED532B7F6AEB7A3C2DD9BA3EBFCF7F9B6EF2918F0C288)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 是 | 
返回结果是否为纳秒数。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Tz-ugINmQua12Am5L31weQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=2209E9648975B57860F9A7A0BDDB957B440A21EBF639EB59E8BEA40358713570)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ah0YJiSlQt2HO9iJelITyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=CF161C93D64AAD355B2A8349F589266A8B28990EF740E352656DF92F02ACFEFC)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 否 | 
返回结果是否为纳秒数,默认值为false。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealTime(deprecated)

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/unvllV4zTweTOCF3ciyiLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=437AF41D7B55CA4BEC1A85F70885817F57707E5DD65688EFA356099FA8699210)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 是 | 
返回结果是否为纳秒数。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealTime(deprecated)

getRealTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/POZiBKxrTmmXT_6Dqal3VQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=D5D8B97AFDB1419AD0D1C9B766AC125C879C6CB63907C02ECD0989981A89E8ED)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealTime(deprecated)

getRealTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，包括深度睡眠时间，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/HFTDXZPfQOuJcTtrwEAvUQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=66F69E88B66B97F7E3819DE049B939A8F622C20A4327363D0D7D86E2CE096A0C)

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 否 | 
返回结果是否为纳秒数,默认值为false。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime().then((time: number) => {
    console.info(`Succeeded in getting real time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTime10+

getTime(isNanoseconds?: boolean): number

使用同步方式获取自Unix纪元以来到当前系统时间所经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNanoseconds | boolean | 否 | 
返回结果是否为纳秒数。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

默认值为false。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 自Unix纪元以来到当前系统时间所经过的时间。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getTime(true)
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getUptime10+

getUptime(timeType: TimeType, isNanoseconds?: boolean): number

使用同步方式获取自系统启动以来经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeType | [TimeType](#timetype10) | 是 | 获取时间的类型，仅能为STARTUP或者ACTIVE。 |
| isNanoseconds | boolean | 否 | 
返回结果是否为纳秒数。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

默认值为false。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 自系统启动以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification

failed.This error code was added due to missing issues.

 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getUptime(systemDateTime.TimeType.ACTIVE, false);
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get uptime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getDate(deprecated)

getDate(callback: AsyncCallback<Date>): void

获取当前系统日期，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/rep3cgKjSiCfGN5307SttQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=5B5F322EB7F0D54C79B75A819D3C20D7327031250454479AEB8009DBDB163889)

从API version 9开始支持，从API version 10开始废弃，建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Date> | 是 | 回调函数，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.System error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting date : ${date}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getDate(deprecated)

getDate(): Promise<Date>

获取当前系统日期，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/0KyhHx35SCS4Y06B0GBK4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=DBE8D4CAFE006BE40C97FF75C5A1F2A3C48B399DCF20E9577FC9608AD416F751)

从API version 9开始支持，从API version 10开始废弃，建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Date> | Promise对象，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.System error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate().then((date: Date) => {
    console.info(`Succeeded in getting date : ${date}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTimezone

getTimezone(callback: AsyncCallback<string>): void

获取系统时区，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回系统时区。具体可见[支持的系统时区](#支持的系统时区)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone((error: BusinessError, data: string) => {
    if (error) {
      console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in get timezone : ${data}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTimezone

getTimezone(): Promise<string>

获取系统时区，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回系统时区。具体可见[支持的系统时区](#支持的系统时区)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone().then((data: string) => {
    console.info(`Succeeded in getting timezone: ${data}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTimezoneSync10+

getTimezoneSync(): string

获取系统时区，使用同步方式。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回系统时区。具体可见[支持的系统时区](#支持的系统时区)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timezone: string = systemDateTime.getTimezoneSync();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### 支持的系统时区

支持的系统时区及各时区与0时区相比的偏移量(单位：h)可见下表。

| 时区 | 偏移量 |
| :-- | :-- |
| Antarctica/McMurdo | 12 |
| America/Argentina/Buenos\_Aires | \-3 |
| Australia/Sydney | 10 |
| America/Noronha | \-2 |
| America/St\_Johns | \-3 |
| Africa/Kinshasa | 1 |
| America/Santiago | \-3 |
| Asia/Shanghai | 8 |
| Asia/Nicosia | 3 |
| Europe/Berlin | 2 |
| America/Guayaquil | \-5 |
| Europe/Madrid | 2 |
| Pacific/Pohnpei | 11 |
| America/Godthab | \-2 |
| Asia/Jakarta | 7 |
| Pacific/Tarawa | 12 |
| Asia/Almaty | 6 |
| Pacific/Majuro | 12 |
| Asia/Ulaanbaatar | 8 |
| America/Mexico\_City | \-5 |
| Asia/Kuala\_Lumpur | 8 |
| Pacific/Auckland | 12 |
| Pacific/Tahiti | \-10 |
| Pacific/Port\_Moresby | 10 |
| Asia/Gaza | 3 |
| Europe/Lisbon | 1 |
| Europe/Moscow | 3 |
| Europe/Kiev | 3 |
| Pacific/Wake | 12 |
| America/New\_York | \-4 |
| Asia/Tashkent | 5 |

#### systemDateTime.getAutoTimeStatus21+

getAutoTimeStatus(): boolean

获取自动设置时间开关状态，使用同步方式。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 
返回自动设置时间开关状态。

\- true：表示自动设置时间开关状态为打开。

\- false：表示自动设置时间开关状态为关闭。

 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)和[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 13000001 | Network connection error or OS error. Possible causes: 1.System memory is insufficient; 2.Calls the underlying system interface failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let status: boolean = systemDateTime.getAutoTimeStatus();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get autotime status. message: ${error.message}, code: ${error.code}`);
}
```
