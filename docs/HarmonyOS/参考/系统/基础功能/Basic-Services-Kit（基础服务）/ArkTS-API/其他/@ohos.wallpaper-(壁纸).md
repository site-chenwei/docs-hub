---
title: "@ohos.wallpaper (壁纸)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wallpaper"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "其他"
  - "@ohos.wallpaper (壁纸)"
captured_at: "2026-04-17T01:48:28.433Z"
---

# @ohos.wallpaper (壁纸)

壁纸管理服务为HarmonyOS系统服务，提供壁纸切换功能。从API 9开始壁纸管理的接口调整为系统API，壁纸的切换只能通过系统应用来完成。壁纸管理提供壁纸切换通道，使用壁纸的应用（如：桌面）需订阅壁纸变化通知并刷新壁纸显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Z5zSPyQYT8C7RfzvennBbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=49962DC709D52376BCF1514D3CC3018C14910C798E01A46A3DA529808DBA3C71)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { wallpaper } from '@kit.BasicServicesKit';
```

#### WallpaperType7+

定义壁纸的枚举类型。

**系统能力**: SystemCapability.MiscServices.Wallpaper

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| WALLPAPER\_SYSTEM | 0 | 主屏幕壁纸标识。 |
| WALLPAPER\_LOCKSCREEN | 1 | 锁屏壁纸标识。 |

#### RgbaColor(deprecated)

定义壁纸颜色信息结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/2t87Np4CR4CPGjtFTpBRqQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=243F14EC27718F0E86A430859C27037000F038F2A475905ED7E8D5DF6E654517)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| red | number | 否 | 否 | 表示红色值，范围为 0 到 255。 |
| green | number | 否 | 否 | 表示绿色值，范围为 0 到 255。 |
| blue | number | 否 | 否 | 表示蓝色值，范围为 0 到 255。 |
| alpha | number | 否 | 否 | 表示 alpha 值，范围为 0 到 255。 |

#### wallpaper.on('colorChange')(deprecated)

on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

订阅壁纸颜色变化结果上报事件。不支持多线程并发调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/1gE6CNcRQserEa2lhoOIdg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=E7E291181A0988EAFF76D60C54849C7E828C26FB0DF24BD1D2EF3BA81C117281)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取值为'colorChange'，表示壁纸颜色变化结果上报事件。 |
| callback | function | 是 | 
壁纸颜色变化触发该回调方法，返回壁纸类型和壁纸的主要颜色信息。

\- colors

壁纸的主要颜色信息，其类型见[RgbaColor](#rgbacolordeprecated)。

\- wallpaperType

壁纸类型。

 |

**示例：**

```ts
try {
    let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
        console.info(`wallpaper color changed.`);
    };
    wallpaper.on('colorChange', listener);
} catch (error) {
    console.error(`failed to on because: ${JSON.stringify(error)}`);
}
```

#### wallpaper.off('colorChange')(deprecated)

off(type: 'colorChange', callback?: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

取消订阅壁纸颜色变化结果上报事件。不支持多线程并发调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/CUgJdaJtQiyBqOliX5oDiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=8B7316CEE980F471FF871E92E1D49AFC3063FC57082D40FD58995AB758A1A02D)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取值为'colorChange'，表示取消订阅壁纸颜色变化结果上报事件。 |
| callback | function | 否 | 
表示要取消的壁纸颜色变化的回调，不填写该参数则取消订阅该type对应的所有回调。

\- colors

壁纸的主要颜色信息，其类型见[RgbaColor](#rgbacolordeprecated)。

\- wallpaperType

壁纸类型。

 |

**示例：**

```ts
let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
    console.info(`wallpaper color changed.`);
};
try {
    wallpaper.on('colorChange', listener);
} catch (error) {
    console.error(`failed to on because: ${JSON.stringify(error)}`);
}

try {
    // 取消订阅listener
    wallpaper.off('colorChange', listener);
} catch (error) {
    console.error(`failed to off because: ${JSON.stringify(error)}`);
}

try {
    // 取消所有'colorChange'类型的订阅
    wallpaper.off('colorChange');
} catch (error) {
    console.error(`failed to off because: ${JSON.stringify(error)}`);
}
```

#### wallpaper.getColors(deprecated)

getColors(wallpaperType: WallpaperType, callback: AsyncCallback<Array<RgbaColor>>): void

获取指定类型壁纸的主要颜色信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/gdenmtdwShOGPjshsasihA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=8BC504C767D964A9BB0FF654E9FCA5C3DA166CFFC5255C12669E457C01AD8A15)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<Array<[RgbaColor](#rgbacolordeprecated)\>> | 是 | 回调函数，返回壁纸的主要颜色信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: Array<wallpaper.RgbaColor>) => {
    if (error) {
        console.error(`failed to getColors because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getColors: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getColors(deprecated)

getColors(wallpaperType: WallpaperType): Promise<Array<RgbaColor>>

获取指定类型壁纸的主要颜色信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/X5OJ6fsSR9e2b65cklb94A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=7D0CECFB51AA94B4573F896DBF4DC8FB16C2669C346DB2F9DDDB1CD68DB5D736)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[RgbaColor](#rgbacolordeprecated)\>> | 返回壁纸的主要颜色信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: Array<wallpaper.RgbaColor>) => {
    console.info(`success to getColors: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getColors because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getId(deprecated)

getId(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

获取指定类型壁纸的ID。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/9QFt_28xQ0yJr6U-E51RiA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=B2C2DD4B2D385977B08C628A0E5A2793385151EC229861B0F25B23C3755D4FBB)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回壁纸的ID。如果配置了指定类型的壁纸就返回一个大于等于0的数，否则返回-1。取值范围是-1到（2^31-1）。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getId(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getId because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getId: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getId(deprecated)

getId(wallpaperType: WallpaperType): Promise<number>

获取指定类型壁纸的ID。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/UnfzMdWMR2WpHQo5KBaRRw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=E216D22A8E81201B5102E932440548596996D5D666D8A4D15F7857613F49A0F2)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 壁纸的ID。如果配置了这种壁纸类型的壁纸就返回一个大于等于0的数，否则返回-1。取值范围是-1到（2^31-1）。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getId(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: Number) => {
    console.info(`success to getId: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getId because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getMinHeight(deprecated)

getMinHeight(callback: AsyncCallback<number>): void

获取壁纸的最小高度值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/9ZR9sRs2SmyXN4L_WiDMyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C77BDC30B283CE22642739FF21482A023CCC9B37CD00E0A2D198FF6599000B27)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回壁纸的最小高度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的高度值代替。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight((error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getMinHeight(deprecated)

getMinHeight(): Promise<number>

获取壁纸的最小高度值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/rMLz_xZsSKmqm3-C2PTUyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=4C84736BE6CDBD36C5A29518EBB9A2AC5EE250BAD3A150EFBDAEF6FE5259385D)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 返回壁纸的最小高度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的高度值代替。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight().then((data: Number) => {
    console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getMinWidth(deprecated)

getMinWidth(callback: AsyncCallback<number>): void

获取壁纸的最小宽度值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/p3Drti0ZSJCgt8Nhnkl68Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=5A3E8AAD5A113D4DBB4BE013485388524D9919B08E58C8141A1AE6CA35BA1490)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，壁纸的最小宽度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的宽度值代替。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth((error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getMinWidth(deprecated)

getMinWidth(): Promise<number>

获取壁纸的最小宽度值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/PdmhlcgIR72B6rhOYIoB-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=31F79C1DFB4D58DB772349D0D829F1B69B604DA3B8BBCFFF84864A2F98D3A49A)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 壁纸的最小宽度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的宽度值代替。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth().then((data: Number) => {
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getFile(deprecated)

getFile(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

获取指定类型的壁纸文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/socFbjopTRWnPwgrwH7Hfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=492CC6A179FAFDAA55C3D4AEF1D06A2BF1E984521BBB8A2418CA2844D6A743A4)

从 API version 8开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.GET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wallpaper#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数，调用成功则返回壁纸文件描述符ID，调用失败则返回error信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: number) => {
    if (error) {
        console.error(`failed to getFile because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getFile: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getFile(deprecated)

getFile(wallpaperType: WallpaperType): Promise<number>

获取指定类型的壁纸文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/wQHNKVgJRK-7bI4KBhChOg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=AB05E22000EC6C64FDED993BE97B2FFF8A686053B01C03DC3B75087E658CC8D4)

从 API version 8开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.GET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wallpaper#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 调用成功则返回壁纸文件描述符ID，调用失败则返回error信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: number) => {
    console.info(`success to getFile: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getFile because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.isChangePermitted(deprecated)

isChangePermitted(callback: AsyncCallback<boolean>): void

是否允许应用改变当前用户的壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/HZX6Kl8FS2Wyh7QhSKBwjg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=98486E4DAA38E292D412815454CAF53C1C71C4C1DE044EDE558CA331735805A9)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回是否允许应用改变当前用户的壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
});
```

#### wallpaper.isChangePermitted(deprecated)

isChangePermitted(): Promise<boolean>

是否允许应用改变当前用户的壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/vu3qMgO9TJCxMcyncL2A_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=FBC8B0D73BCF5FDF8DE007A676D644C67B160EE576DFFCD241D181ACD600A976)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 返回是否允许应用改变当前用户的壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted().then((data: Boolean) => {
    console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.isOperationAllowed(deprecated)

isOperationAllowed(callback: AsyncCallback<boolean>): void

是否允许用户设置壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/l4xd5TrcTiqQEUtqadWEnQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=3D46B7872E1A49342F83F66B2351BE6E405984625F7B620F28B4861F09D91A2B)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回是否允许用户设置壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
});
```

#### wallpaper.isOperationAllowed(deprecated)

isOperationAllowed(): Promise<boolean>

是否允许用户设置壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/raOVLNGXRq-pUq5bbtvU7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=A5B382A35ED131DFB380A70092A4E886B4F3CDD5F4776A45E134DADBC3AA7BF5)

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 异步回调函数，返回是否允许用户设置壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed().then((data: Boolean) => {
    console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.reset(deprecated)

reset(wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

移除指定类型的壁纸，恢复为默认显示的壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/d1doGegYQ3Khpm-mi_GSrQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C746769C68C339BF662B6613728288D0BC29ACF0B35634E9F42C9B935BCD06CF)

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，移除壁纸成功，error为undefined，否则返回error信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.reset(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
    if (error) {
        console.error(`failed to reset because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to reset.`);
});
```

#### wallpaper.reset(deprecated)

reset(wallpaperType: WallpaperType): Promise<void>

移除指定类型的壁纸，恢复为默认显示的壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/rKCqYRztTO6auS7vv3HkKQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=479A3FEB29B41F36A65CED6A1E8375A6CA380505920B0DB0DC8E0059F5E37983)

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.reset(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
    console.info(`success to reset.`);
}).catch((error: BusinessError) => {
    console.error(`failed to reset because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.setWallpaper(deprecated)

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

将指定资源设置为指定类型的壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/u9LYd6Z9QFqwO8W90w3pLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=FB67A9394715FB6330BF936057D428BCC1C9AC3BE749DDD418DDE044DC6F83FC)

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| source | string | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | JPEG或PNG文件的Uri路径，或者PNG格式文件的位图。 |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，设置壁纸成功，error为undefined，否则返回error信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// source类型为string
let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
    if (error) {
        console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
       return;
       }
    console.info(`success to setWallpaper.`);
});

// source类型为image.PixelMap
let imageSource = image.createImageSource("file://" + wallpaperPath);
let opts: image.DecodingOptions = {
    desiredSize: {
        height: 3648,
        width: 2736
    }
};
imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
    wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
        if (error) {
            console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
            return;
        }
        console.info(`success to setWallpaper.`);
    });
}).catch((error: BusinessError) => {
    console.error(`failed to createPixelMap because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.setWallpaper(deprecated)

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType): Promise<void>

将指定资源设置为指定类型的壁纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/fYXfM7WEQr2euZS0jYV1Ug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=74887120B59D3E0D7E863BEE855A71382F2C62745076EE92A60A62711926EB30)

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| source | string | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | JPEG或PNG文件的Uri路径，或者PNG格式文件的位图。 |
| wallpaperType | [WallpaperType](#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// source类型为string
let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
    console.info(`success to setWallpaper.`);
  }).catch((error: BusinessError) => {
    console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
});
  
// source类型为image.PixelMap
let imageSource = image.createImageSource("file://" + wallpaperPath);
let opts: image.DecodingOptions = {
    desiredSize: {
        height: 3648,
        width: 2736
    }
};
imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
    wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
        console.info(`success to setWallpaper.`);
    }).catch((error: BusinessError) => {
        console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
    });
  }).catch((error: BusinessError) => {
    console.error(`failed to createPixelMap because: ${JSON.stringify(error)}`);
});
```
