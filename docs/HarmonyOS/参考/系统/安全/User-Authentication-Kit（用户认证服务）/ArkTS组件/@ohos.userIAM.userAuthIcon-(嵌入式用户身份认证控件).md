---
title: "@ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-useriam-userauthicon"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "User Authentication Kit（用户认证服务）"
  - "ArkTS组件"
  - "@ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)"
captured_at: "2026-04-17T01:48:21.047Z"
---

# @ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)

提供应用界面上展示的人脸、指纹认证图标，具体功能如下：

1.  提供嵌入式的人脸、指纹认证控件图标，可被应用集成。
    
2.  支持自定义图标的颜色和大小，但图标样式不可变更。
    
3.  点击控件图标后将以系统弹窗的方式，拉起人脸、指纹认证控件。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Uglug-mRQ6Kg5s6qXf0-NQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8440493DAB49A29D057501D5961DCA5C6BD6F3AC765C9936068B45C454CD44E8)

-   本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';
```

#### 子组件

无

#### 属性

不支持通用属性。

#### UserAuthIcon

```ts
UserAuthIcon({
  authParam: userAuth.AuthParam,
  widgetParam: userAuth.WidgetParam,
  iconHeight?: Dimension,
  iconColor?: ResourceColor,
  onIconClick?: ()=>void,
  onAuthResult: (result: userAuth.UserAuthResult)=>void
})
```

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authParam | [userAuth.AuthParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth#authparam10) | 是 | 用户认证相关参数。 |
| widgetParam | [userAuth.WidgetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth#widgetparam10) | 是 | 用户认证界面配置相关参数。 |
| iconHeight | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 设置icon的高度，宽高比1:1，默认64fp，不支持百分比字符串。 |
| iconColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 设置icon的颜色，默认值：$r('sys.color.ohos\_id\_color\_activated')。 |
| onIconClick | ()=>void | 否 | 用户点击icon回调接口。 |
| onAuthResult | (result: [userAuth.UserAuthResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth#userauthresult10))=>void | 是 | 
用户认证结果信息回调接口。

应用需要申请ohos.permission.ACCESS\_BIOMETRIC权限，否则应用将仅展示图标，无法正常拉起身份认证控件。

 |

#### 事件

不支持通用事件。

#### 示例

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';

@Entry
@Component
struct Index {
  rand = cryptoFramework.createRandom();
  len: number = 16;
  randData: Uint8Array = this.rand?.generateRandomSync(this.len)?.data;
  authParam: userAuth.AuthParam = {
    challenge: this.randData,
    authType: [userAuth.UserAuthType.FACE, userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3
  };
  widgetParam: userAuth.WidgetParam = {
    title: '请进行身份认证'
  };

  build() {
    Row() {
      Column() {
        UserAuthIcon({
          authParam: this.authParam,
          widgetParam: this.widgetParam,
          iconHeight: 200,
          iconColor: Color.Blue,
          onIconClick: () => {
            console.info('The user clicked the icon.');
          },
          onAuthResult: (result: userAuth.UserAuthResult) => {
            console.info(`Get user auth result, result = ${JSON.stringify(result)}`);
          }
        })
      }
    }
  }
}
```

调用onAuthResult可能会抛出错误码，错误码详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

**人脸认证图例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uXLID4yyRJSDQZjKVhMcLQ/zh-cn_image_0000002569021197.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=54B02D6601FA6572F464B6BDFB62B77853B3493F6919C784F3E497C605A92D90)

**指纹认证图例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/GKI_yi-7SKSCJUVaYP6SqQ/zh-cn_image_0000002568901187.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4C1509C4A43544EDAE543B491193E532D4C61E4E621B7DB4955717B444FDA3B2)
