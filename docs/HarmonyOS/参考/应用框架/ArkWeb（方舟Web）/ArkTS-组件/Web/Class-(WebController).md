---
title: "Class (WebController)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontroller"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (WebController)"
captured_at: "2026-04-17T01:48:12.763Z"
---

# Class (WebController)

通过WebController可以控制Web组件各种行为。一个WebController对象只能控制一个Web组件，且必须在Web组件和WebController绑定后，才能调用WebController上的方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/L2yvxfFyTweCm7Q1nEizOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=3928709571692E3EA2381369C347490DC90C6E057A417400D62C6F79D3E4699A)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 8开始支持。
    
-   该组件从API version 9开始废弃，建议使用[WebviewController9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller)代替。
    
-   示例效果请以真机运行为准。
    

#### 创建对象

```ts
let webController: WebController = new WebController()
```

#### constructor(deprecated)

constructor()

WebController的构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/0sbEj927Sq-14RWtj1SLgg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=C3A00D158921A91FD463E95E757AE36D71519F47F73121317E903ACDC8E8D5EE)

从API version 8开始支持，从API version 9开始废弃，建议使用[constructor11+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#constructor11)代替。

**系统能力：** SystemCapability.Web.Webview.Core

#### getCookieManager(deprecated)

getCookieManager(): WebCookie

获取Web组件cookie管理对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/lBP5NkLCR2uAcDteJKixGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=BDB0AB098732036D020CE78E4BE9A124766856196C75B4B7CCC9ED147A8C9969)

从API version 9开始支持，从API version 9开始废弃，建议使用[getCookie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#getcookiedeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| WebCookie | Web组件cookie管理对象，参考[WebCookie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcookie)定义。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('getCookieManager')
        .onClick(() => {
          let cookieManager = this.controller.getCookieManager()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### requestFocus(deprecated)

requestFocus()

使当前Web页面获取焦点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/cXbEXOBgQtSQ5_c_F3thuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=97C86F385DC573B75047D0255C1B00F02FF39D7D374601882CCF8A969B722AF8)

从API version 8开始支持，从API version 9开始废弃，建议使用[requestFocus9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#requestfocus)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('requestFocus')
        .onClick(() => {
          this.controller.requestFocus()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### accessBackward(deprecated)

accessBackward(): boolean

当前页面是否可后退，即当前页面是否有返回历史记录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/ajmDs7neRk6xjIonW_vyKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=E8E185575CF9BAE33D66A144FBA4E94BC91A29E7AA74877694AF7F4202E94A1A)

从API version 8开始支持，从API version 9开始废弃，建议使用[accessBackward9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#accessbackward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 可以后退返回true，否则返回false。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('accessBackward')
        .onClick(() => {
          let result = this.controller.accessBackward()
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### accessForward(deprecated)

accessForward(): boolean

当前页面是否可前进，即当前页面是否有前进历史记录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/xp_efFSsQCK6-67gMI3J_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=5031548877087A3F60502B5B011ED9753556086796FF89B826135F099663127F)

从API version 8开始支持，从API version 9开始废弃，建议使用[accessForward9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#accessforward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回true表示当前页面可以前进，返回false表示当前页面不可以前进。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('accessForward')
        .onClick(() => {
          let result = this.controller.accessForward()
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### accessStep(deprecated)

accessStep(step: number): boolean

当前页面是否可前进或者后退给定的step步。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/st8JN8qqScCT3zEn4w0xUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=99A95C8C69896DB28E1E4094CF7A8620B0DF24D54FC45089388075BA30BEFCE0)

从API version 8开始支持，从API version 9开始废弃，建议使用[accessStep9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#accessstep)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| step | number | 是 | 要跳转的步数，正数代表前进，负数代表后退。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 页面是否前进或后退 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State steps: number = 2

  build() {
    Column() {
      Button('accessStep')
        .onClick(() => {
          let result = this.controller.accessStep(this.steps)
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### backward(deprecated)

backward()

按照历史栈，后退一个页面。一般结合accessBackward一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/yec6zkKvSYujw1hRBCHdtg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=CD746DBAD27178656EF03C6FB07F87ADE7302EF9590DB7505E028D4E98553353)

从API version 8开始支持，从API version 9开始废弃，建议使用[backward9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#backward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('backward')
        .onClick(() => {
          this.controller.backward()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### forward(deprecated)

forward()

按照历史栈，前进一个页面。一般结合accessForward一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/FIfLs999T9qmN1VP3P2H_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=BA7FD4CA8158FCA6F5F1A9EE0C53C5FCEDEB88B964A43422C12346B835631634)

从API version 8开始支持，从API version 9开始废弃，建议使用[forward9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#forward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('forward')
        .onClick(() => {
          this.controller.forward()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### deleteJavaScriptRegister(deprecated)

deleteJavaScriptRegister(name: string)

删除通过registerJavaScriptProxy注册到window上的指定name的应用侧JavaScript对象。删除后立即生效，无须调用[refresh](#refreshdeprecated)接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/TNmBvstpSVmC4reFC_q8Tg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=0A5864A2F49497120482D425AC031EACADB41A6BCD5EA8F3ED7CFC7F16433D18)

从API version 8开始支持，从API version 9开始废弃，建议使用[deleteJavaScriptRegister9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#deletejavascriptregister)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 注册对象的名称，可在网页侧JavaScript中通过此名称调用应用侧JavaScript对象。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State name: string = 'Object'

  build() {
    Column() {
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          this.controller.deleteJavaScriptRegister(this.name)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### getHitTest(deprecated)

getHitTest(): HitTestType

获取当前被点击区域的元素类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/3wvBN-jMSvCnNYjBw3dp_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=25FB108A6E7990372B1935AFA710FDC74E18F6E7C6B6697B747F581CCDF79C9B)

从API version 8开始支持，从API version 9开始废弃，建议使用[getHitTest9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#gethittestdeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [HitTestType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#hittesttypedeprecated) | 被点击区域的元素类型。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('getHitTest')
        .onClick(() => {
          let hitType = this.controller.getHitTest()
          console.info("hitType: " + hitType)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### loadData(deprecated)

loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })

baseUrl为空时，通过”data“协议加载指定的一段字符串。

当baseUrl为”data“协议时，编码后的data字符串将被Web组件作为”data"协议加载。

当baseUrl为“http/https"协议时，编码后的data字符串将被Web组件以类似loadUrl的方式以非编码字符串处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/mJIXIzCTQ_Gof7b5jYLMFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=25A5796FAD6BB740A7B8ABA41CD0DD71A926553FD0D35B5FEF0B4BEC21294339)

从API version 8开始支持，从API version 9开始废弃，建议使用[loadData9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loaddata)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | 是 | 按照”Base64“或者”URL"编码后的一段字符串。 |
| mimeType | string | 是 | 媒体类型（MIME）。 |
| encoding | string | 是 | 编码类型，具体为“Base64"或者”URL编码。 |
| baseUrl | string | 否 | 指定的一个URL路径（“http”/“https”/"data"协议），并由Web组件赋值给window.origin。默认值为空字符串。 |
| historyUrl | string | 否 | 历史记录URL。默认值为空字符串。非空时，可被历史记录管理，实现前进后退功能。当baseUrl为空时，此属性无效。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          this.controller.loadData({
            data: "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
            mimeType: "text/html",
            encoding: "UTF-8"
          })
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### loadUrl(deprecated)

loadUrl(options: { url: string | Resource, headers?: Array<Header> })

使用指定的http头加载指定的URL。

通过loadUrl注入的对象只在当前document有效，即通过loadUrl导航到新的页面会无效。

而通过registerJavaScriptProxy注入的对象，在loadUrl导航到新的页面也会有效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/RsIzddlWSKGEy6oqt0ZFbg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=0F9DAFCF9A258A3E878F658D91C69661D3A8CBEAF3505A822FD6446DEF2F131D)

从API version 8开始支持，从API version 9开始废弃，建议使用[loadUrl9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| url | string | Resource | 是 | 需要加载的 URL。 |
| headers | Array<[Header](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#header)\> | 否 | 
URL的附加HTTP请求头。

默认值：\[\]。

 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          this.controller.loadUrl({ url: 'www.example.com' })
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### onActive(deprecated)

onActive(): void

调用此接口通知Web组件进入前台激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ZW012TgLTAqz0jXW7V_64A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=FF4193D05F5AF9EFC51C234183F6754A708B1745B9115A97CCA51F6620477433)

从API version 8开始支持，从API version 9开始废弃，建议使用[onActive9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#onactive)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('onActive')
        .onClick(() => {
          this.controller.onActive()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### onInactive(deprecated)

onInactive(): void

调用此接口通知Web组件进入未激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/k-LGi7LkT16VMxJAeyLwyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=16BF694F086BF5E1C529525DADD279957F3431B51ED266173A10BE633B62B76A)

从API version 8开始支持，从API version 9开始废弃，建议使用[onInactive9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oninactive)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('onInactive')
        .onClick(() => {
          this.controller.onInactive()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### zoom(deprecated)

zoom(factor: number): void

调整当前网页的缩放比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Go6brXpqSnyL6J_3lhDXlw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=5AB148724D914991D398BCF4161EF9B7424BF49B79C4EE4BFDE2269C8E14C4A4)

从API version 8开始支持，从API version 9开始废弃，建议使用[zoom9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#zoom)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| factor | number | 是 | 基于当前网页所需调整的相对缩放比例，当入参为1时为默认加载网页的缩放比例，小于1为缩小，大于1为放大。取值范围(0, 100\]。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State factor: number = 1

  build() {
    Column() {
      Button('zoom')
        .onClick(() => {
          this.controller.zoom(this.factor)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### refresh(deprecated)

refresh()

调用此接口通知Web组件刷新网页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/itbp5Ng2RCO1QY4dDOffZw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=0F77C1D6DF3A368466BCC52C45E24DBB14B0B2C3246BF1DED013EE9EB547BED5)

从API version 8开始支持，从API version 9开始废弃，建议使用[refresh9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#refresh)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          this.controller.refresh()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### registerJavaScriptProxy(deprecated)

registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })

注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。注册后，须调用[refresh](#refreshdeprecated)接口生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/faAJV48jSaKDbITCwQXcCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=C7265A1D9145DB93DB7203125BA4F63ADA336FAD28174FE7110F08961E3A2C78)

从API version 8开始支持，从API version 9开始废弃，建议使用[registerJavaScriptProxy9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#registerjavascriptproxy)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| object | object | 是 | 参与注册的应用侧JavaScript对象。可以声明方法，也可以声明属性，但是不支持h5直接调用。其中方法的参数和返回类型只能为string，number，boolean |
| name | string | 是 | 注册对象的名称，与window中调用的对象名一致。注册后window对象可以通过此名字访问应用侧JavaScript对象。 |
| methodList | Array<string> | 是 | 参与注册的应用侧JavaScript对象的方法。 |

**示例：**

```ts
// xxx.ets
class TestObj {
  constructor() {
  }

  test(): string {
    return "ArkUI Web Component"
  }

  toString(): void {
    console.info('Web Component toString')
  }
}

@Entry
@Component
struct Index {
  controller: WebController = new WebController()
  testObj = new TestObj();
  build() {
    Column() {
      Row() {
        Button('Register JavaScript To Window').onClick(() => {
          this.controller.registerJavaScriptProxy({
            object: this.testObj,
            name: "objName",
            methodList: ["test", "toString"],
          })
        })
      }
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}
```

加载的html文件。

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        Hello world!
        <script type="text/javascript">
            function htmlTest() {
                str = objName.test("test function")
                console.info('objName.test result:'+ str)
            }
        </script>
    </body>
</html>
```

#### runJavaScript(deprecated)

runJavaScript(options: { script: string, callback?: (result: string) => void })

异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScript需要在loadUrl完成后，比如onPageEnd中调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/laFjl-ykTn2hFpelGmwbXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=5189BEE7C32D608842904302B62212B37A1BBBEBC7412FD6401FD6A3DD27B7E6)

从API version 8开始支持，从API version 9开始废弃，建议使用[runJavaScript9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| script | string | 是 | JavaScript脚本。 |
| callback | (result: string) => void | 否 | 回调执行JavaScript脚本结果。JavaScript脚本若执行失败或无返回值时，返回null。不传入时不进行回调。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State webResult: string = ''
  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
      .javaScriptAccess(true)
      .onPageEnd((event) => {
        this.controller.runJavaScript({
          script: 'test()',
          callback: (result: string)=> {
            this.webResult = result
            console.info(`The test() return value is: ${result}`)
          }})
        if (event) {
          console.info('url: ', event.url)
        }
      })
    }
  }
}
```

加载的html文件。

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8">
  </head>
  <body>
      Hello world!
      <script type="text/javascript">
          function test() {
              console.info('Ark WebComponent')
              return "This value is from index.html"
          }
      </script>
  </body>
</html>
```

#### stop(deprecated)

stop()

停止页面加载。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/rg0zBRQ3TJOaGgAmH5A81A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=4142F3E62A060179EAD918987DB2CE7617BF1C57C980AF4919CA01A09828303E)

从API version 8开始支持，从API version 9开始废弃，建议使用[stop9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#stop)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('stop')
        .onClick(() => {
          this.controller.stop()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

#### clearHistory(deprecated)

clearHistory(): void

删除所有前进后退记录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/92pBIGrCQVSMcS8Q0u-4Cg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=E7AB14FA57B6D183D002035E56E545D56DE98BDF674C80ECF503A5D7CD4992BA)

从API version 8开始支持，从API version 9开始废弃，建议使用[clearHistory9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#clearhistory)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('clearHistory')
        .onClick(() => {
          this.controller.clearHistory()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
