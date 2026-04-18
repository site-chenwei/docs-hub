---
title: "@ohos.systemTime (系统时间、时区)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-time"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.systemTime (系统时间、时区)"
captured_at: "2026-04-17T01:48:28.607Z"
---

# @ohos.systemTime (系统时间、时区)

本模块主要由系统时间和系统时区功能组成。开发者可以设置、获取系统时间及系统时区。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/l57sbNM2Qq6MvOvM9QVtSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=77F47447200D1CF88A64C9523EF83E1C7CBAAFF04397176834D7B272C04E4395)

-   从API Version 9 开始，该模块接口不再维护，推荐使用新模块接口[@ohos.systemDateTime (系统时间、时区)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time)。
-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { systemTime } from '@kit.BasicServicesKit';
```

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/YkgAUWuLQ0GgaoDdcn-_fg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=BB83C3FE3EA6568F515D2CDF3A97FC7CC30303EC7293F4D2203571E5A0852E4F)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 是 | 
返回结果是否为纳秒数。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime: ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/AJTjPab2QVCz_8qgko96SA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=B0A518A100A32ACCCDA9A2BC9C82B314751F6A8225D3B6AAFBE307B4ED04F1EE)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间（ms）。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(isNano?: boolean): Promise<number>

获取自Unix纪元以来经过的时间，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/IzApHRQLTXOrdX0t9eqgIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=05B71F09810BA3B595819E3BB6A55228B95D072C1A509B3046E804AEF889DDA0)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 否 | 
返回结果是否为纳秒数，默认值为false。

默认值为false。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回自Unix纪元以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime().then((time: number) => {
    console.info(`Succeeded in getting currentTime : ${time}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/pMsI6nXJSCarRwCybKi13g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=A59765C6FF9345421565B024B7F2E333D102DD1B108DE5068795E2C862C8A63D)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 是 | 
返回结果是否为纳秒数。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/z6WzUVKdQd6CEgZ_G3u_7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=73C62381F4E1A3C25418B4844F4F028615730479C36392347ECA1A8DCF995393)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/tjjUH9txRLydwwZ5T4Md1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=27D6308FB438F9E60262893EF278A6BAD40C52AE06D1FE858F5571009B7046BC)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 否 | 
返回结果是否为纳秒数，默认值为false。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealTime8+(deprecated)

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/BQ1M_zKDR-WeNlZGTUfkhg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=082A19C3B334074C66740A456B4502A79A756028F3AA291E8D1813D35575B546)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegetuptime10)替代。

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

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealTime8+(deprecated)

getRealTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/HAuyEIByQOeYdOaBTKNrAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=31418DB2E0D1A2DE4649046B3A6362EA25E549F4579C64BCB6A644F2079E342F)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealTime8+(deprecated)

getRealTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，包括深度睡眠时间，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/pf1EhlTjQ_-fIqscjptZaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=142164C450688B7A62BA9E47DC5F0F58EEC424BA3806CB8F253ADF93CE50E814)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isNano | boolean | 否 | 
返回结果是否为纳秒数，默认值为false。

默认值为false。

\- true：表示返回结果为纳秒数（ns）。

\- false：表示返回结果为毫秒数（ms）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime().then((time: number) => {
    console.info(`Succeeded in getting real time : ${time}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getDate8+(deprecated)

getDate(callback: AsyncCallback<Date>): void

获取当前系统日期，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/B7xwn1MrQv6DZz17KqLZ_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=7FC192D39B73AFB51C863B97E57C2BC0E97F8CCE351FB1F07773EBF74E742014)

从API version 8开始支持，从API version 9开始废弃。建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Date> | 是 | 回调函数，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting date : ${date}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getDate8+(deprecated)

getDate(): Promise<Date>

获取当前系统日期，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/rxFJK4CNRwOesLmxoqW5dw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=E1DD807CFD15461B4E8DE27E6491923F09D0F3988C877EAE9AB614968F53D5ED)

从API version 8开始支持，从API version 9开始废弃。建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Date> | Promise对象，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate().then((date: Date) => {
    console.info(`Succeeded in getting date : ${date}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getTimezone8+(deprecated)

getTimezone(callback: AsyncCallback<string>): void

获取系统时区，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/GYpjbbgdSi6ATYxBEipUEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=0DCE97D8F285AB1BA529472CA3FE6E11D88DA5434E1F4EF8A278E92B0B35956C)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTimezone](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegettimezone)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回系统时区。具体可见[支持的系统时区](#支持的系统时区) 。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone((error: BusinessError, data: string) => {
    if (error) {
      console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting timezone : ${data}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getTimezone8+(deprecated)

getTimezone(): Promise<string>

获取系统时区，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/hdSpCcllRRWqaH3t1wtd-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=E0B7418E62928661C7DE2984266C52DA5164DB69651DB03B291E60377E7683D0)

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTimezone](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time#systemdatetimegettimezone-1)替代。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回系统时区。具体可见[支持的系统时区](#支持的系统时区) 。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone().then((data: string) => {
    console.info(`Succeeded in getting timezone: ${data}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTime(deprecated)

setTime(time : number, callback : AsyncCallback<void>) : void

设置系统时间，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/M2iO4XoZTlCK1YsZ35bfjw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=BB112242BD3F66068A31D0FC6608349AA39629D8B01B1D0B74564523C3A87780)

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| time | number | 是 | 目标时间戳（ms）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25
let time = 1611081385000;
try {
  systemTime.setTime(time, (error: BusinessError) => {
    if (error) {
      console.info(`Failed to setting time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting time`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTime(deprecated)

setTime(time : number) : Promise<void>

设置系统时间，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/01csXa03ScO2itaAPXPz7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=09C361CA0FC61667264EA8846D51AC2691C77D60499B9DED11F2A790CC453BF9)

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| time | number | 是 | 目标时间戳（ms）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25
let time = 1611081385000;
try {
  systemTime.setTime(time).then(() => {
    console.info(`Succeeded in setting time.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to setting time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setDate(deprecated)

setDate(date: Date, callback: AsyncCallback<void>): void

设置系统日期，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/uFZmIkU1SX6aogUuHc66Mw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=784B5FDFA7147EC6B4C0DAD5FBEAD684FDB54D053ECD95E051936E3FED04695F)

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| date | Date | 是 | 目标日期。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let date = new Date();
try {
  systemTime.setDate(date, (error: BusinessError) => {
    if (error) {
      console.info(`Failed to setting date. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting date.`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setDate(deprecated)

setDate(date: Date): Promise<void>

设置系统日期，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/NqLGX3b7RoiJWnLCiNlxcg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=1E0900142B1FF64210BDF31F5EFCC93A2CBBBD32EC7AFD40BC1175402953D6F2)

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| date | Date | 是 | 目标日期。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let date = new Date();
try {
  systemTime.setDate(date).then(() => {
    console.info(`Succeeded in setting date.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to setting date. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTimezone(deprecated)

setTimezone(timezone: string, callback: AsyncCallback<void>): void

设置系统时区，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/2SQ4cVqXQguOrV0W1RFBJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=9EC3AA8925ACF9BAF10BB486FADA99E68718E387D2C444EE2858C5641080239D)

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME\_ZONE

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timezone | string | 是 | 系统时区。具体可见[支持的系统时区](#支持的系统时区) 。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai', (error: BusinessError) => {
    if (error) {
      console.info(`Failed to setting timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting timezone.`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTimezone(deprecated)

setTimezone(timezone: string): Promise<void>

使用Promise异步回调设置系统时区。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/uRYVOqMWT5q2heTE2hbAyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=50A2F2D062460666A6AAFEBB2C5945B2DF5F361C6C6302006BAC674E30553C3A)

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME\_ZONE

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timezone | string | 是 | 系统时区。具体可见[支持的系统时区](#支持的系统时区) 。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai').then(() => {
    console.info(`Succeeded in setting timezone.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to setting timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### 支持的系统时区

支持的系统时区及各时区与0时区相比的偏移量（单位：h）可见下表。

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
