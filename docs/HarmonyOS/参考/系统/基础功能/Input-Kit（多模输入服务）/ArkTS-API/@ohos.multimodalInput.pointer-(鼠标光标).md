---
title: "@ohos.multimodalInput.pointer (鼠标光标)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pointer"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "ArkTS API"
  - "@ohos.multimodalInput.pointer (鼠标光标)"
captured_at: "2026-04-17T01:48:30.681Z"
---

# @ohos.multimodalInput.pointer (鼠标光标)

本模块提供鼠标光标管理能力，包括查询、设置鼠标光标属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/jDEJ9_sBT76RYGHO0HFw6w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=6B57D4EDE0CBA061AF62A6DFACE0064565656ACF8594FA3C04D921B11B978B0D)

-   本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { pointer } from '@kit.InputKit';
```

#### pointer.setPointerVisible

setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void

设置当前窗口的鼠标光标是否显示，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| visible | boolean | 是 | 当前窗口鼠标光标是否显示。true表示显示，false表示不显示。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisible(true, (error: BusinessError) => {
              if (error) {
                console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Set pointer visible success`);
            });
          } catch (error) {
            console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.setPointerVisible

setPointerVisible(visible: boolean): Promise<void>

设置当前窗口的鼠标光标是否显示，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| visible | boolean | 是 | 当前窗口鼠标光标是否显示。true表示显示，false表示不显示。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisible(false).then(() => {
              console.info(`Set pointer visible success`);
            }).catch((error: BusinessError) => {
              console.error(`Set pointer failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.setPointerVisibleSync10+

setPointerVisibleSync(visible: boolean): void

设置当前窗口鼠标光标的显示状态，使用同步方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| visible | boolean | 是 | 当前窗口鼠标光标是否显示。true表示显示，false表示不显示。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisibleSync(false);
            console.info(`Set pointer visible success`);
          } catch (error) {
            console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.isPointerVisible

isPointerVisible(callback: AsyncCallback<boolean>): void

获取鼠标光标显示状态，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回鼠标光标状态，true为显示，false为隐藏。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.isPointerVisible((error: BusinessError, visible: boolean) => {
              if (error) {
                console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
            });
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.isPointerVisible

isPointerVisible(): Promise<boolean>

获取鼠标光标显示状态，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回鼠标光标状态查询结果。true代表显示状态，false代表隐藏状态。 |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.isPointerVisible().then((visible: boolean) => {
              console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get pointer failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.isPointerVisibleSync10+

isPointerVisibleSync(): boolean

获取当前窗口鼠标光标的显示状态，使用同步方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回鼠标光标显示或隐藏状态。true代表显示状态，false代表隐藏状态。 |

**示例**：

```js
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let visible: boolean = pointer.isPointerVisibleSync();
            console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.getPointerStyle

getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void

获取指定窗口的鼠标样式类型，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 
窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。

窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。

如果通过[setPointerStyle](#pointersetpointerstyle)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。

 |
| callback | AsyncCallback<[PointerStyle](#pointerstyle)\> | 是 | 回调函数，返回鼠标样式类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.getPointerStyle(windowId, (error: BusinessError, style: pointer.PointerStyle) => {
                console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
              });
            } catch (error) {
              console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.getPointerStyle

getPointerStyle(windowId: number): Promise<PointerStyle>

获取鼠标样式类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 
窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。

窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。

如果通过[setPointerStyle](#pointersetpointerstyle-1)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。

 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[PointerStyle](#pointerstyle)\> | Promise对象，返回鼠标样式类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.getPointerStyle(windowId).then((style: pointer.PointerStyle) => {
                console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
              }).catch((error: BusinessError) => {
                console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
            } catch (error) {
              console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.getPointerStyleSync10+

getPointerStyleSync(windowId: number): PointerStyle

查询指定窗口的鼠标样式类型，如向东箭头、向西箭头、向南箭头、向北箭头等。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 
窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。

窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。

如果通过[setPointerStyleSync](#pointersetpointerstylesync10)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。

 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| [PointerStyle](#pointerstyle) | 返回鼠标样式类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let windowId = -1;
          try {
            let style: pointer.PointerStyle = pointer.getPointerStyleSync(windowId);
            console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
          } catch (error) {
            console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### pointer.setPointerStyle

setPointerStyle(windowId: number, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void

设置指定窗口的鼠标样式类型，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 
窗口ID。取值范围为大于等于0的整数。

窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。

设置结果可通过[getPointerStyle](#pointergetpointerstyle)获取。

 |
| pointerStyle | [PointerStyle](#pointerstyle) | 是 | 鼠标样式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS, error => {
                console.info(`Set pointer style success`);
              });
            } catch (error) {
              console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.setPointerStyle

setPointerStyle(windowId: number, pointerStyle: PointerStyle): Promise<void>

设置指定窗口的鼠标样式类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 
窗口ID。取值范围为大于等于0的整数。

窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。

设置结果可通过[getPointerStyle](#pointergetpointerstyle-1)获取。

 |
| pointerStyle | [PointerStyle](#pointerstyle) | 是 | 鼠标样式。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS).then(() => {
                console.info(`Set pointer style success`);
              }).catch((error: BusinessError) => {
               console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
            } catch (error) {
              console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### pointer.setPointerStyleSync10+

setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void

设置指定窗口的鼠标样式类型，使用同步方式返回结果。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 
窗口ID。取值范围为大于等于0的整数。

窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。

窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。

设置结果可通过[getPointerStyleSync](#pointergetpointerstylesync10)获取。

 |
| pointerStyle | [PointerStyle](#pointerstyle) | 是 | 鼠标样式。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyleSync(windowId, pointer.PointerStyle.CROSS);
              console.info(`Set pointer style success`);
            } catch (error) {
              console.error(`getPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

#### PrimaryButton10+

鼠标主键类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| LEFT | 0 | 鼠标左键。 |
| RIGHT | 1 | 鼠标右键。 |

#### RightClickType10+

右键菜单的触发方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| TOUCHPAD\_RIGHT\_BUTTON | 1 | 按压触控板右键区域。 |
| TOUCHPAD\_LEFT\_BUTTON | 2 | 按压触控板左键区域。 |
| TOUCHPAD\_TWO\_FINGER\_TAP | 3 | 双指轻击或双指按压触控板。 |
| TOUCHPAD\_TWO\_FINGER\_TAP\_OR\_RIGHT\_BUTTON20+ | 4 | 双指轻击或双指按压触控板、或按压触控板右键区域。 |
| TOUCHPAD\_TWO\_FINGER\_TAP\_OR\_LEFT\_BUTTON20+ | 5 | 双指轻击或双指按压触控板、或按压触控板左键区域。 |

#### PointerStyle

鼠标光标样式类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 值 | 说明 | 图示 |
| :-- | :-- | :-- | :-- |
| DEFAULT | 0 | 默认 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/d6Ziymh4Qqeeby1KzduGEQ/zh-cn_image_0000002538181424.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=7913403F2C2E5CF0EC4282E40BB8BB817B6943A978CBE0E650E6C5DD96F10BFF) |
| EAST | 1 | 向东箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QLprYfmZRRKN2DAUxkfBhg/zh-cn_image_0000002569021211.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=C1B9405E362DF61C55C91CF486E84B0320DC0AB3E6CD430B75C92E6CED5393E3) |
| WEST | 2 | 向西箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/U_t6wFbvQjSpNXB6Xo11Og/zh-cn_image_0000002568901201.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=D53E108FCA77D646CD12F137C2D2C3B7979E987DFBD9B6CB9041A81BFF1B40BD) |
| SOUTH | 3 | 向南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/v7WRD1CtTxCdVH0_HnuWjw/zh-cn_image_0000002538021500.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=918B2B077F1DCB17B9F3F827E9A7F66BA5FF0C68FE2CFE65FF8EF4CC8FBE9723) |
| NORTH | 4 | 向北箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/XE1B07vJQzO4RBVJwFEpYQ/zh-cn_image_0000002538181426.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=C9618797C93BD60F8E93A0C693F710EA6DBF6F87756ABAF0A2ABEDF7BC2A8975) |
| WEST\_EAST | 5 | 向西东箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/FIWVlZlaQZa6ryNFtz8Oaw/zh-cn_image_0000002569021213.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=3486DE6C202407C8C1CAC141BC866D27DF543A7797D7ED40B351CD82946DCA5B) |
| NORTH\_SOUTH | 6 | 向北南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/NAKI1tZ2TzCOWyUexKQJzg/zh-cn_image_0000002568901203.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=17226729E2B8BFC3A9171E220622A1E040534E4640E867374534A3C0CC033E23) |
| NORTH\_EAST | 7 | 向东北箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/r-xdZO7XTRqLQXWcwNq5GA/zh-cn_image_0000002538021502.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=9CECC21903A48E7317AB5F3F55C09238D0CE99C92C356721020091E976176104) |
| NORTH\_WEST | 8 | 向西北箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/TmwPmA8hTh-nlohKk0it2g/zh-cn_image_0000002538181428.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=8F08810F258B515A813A58A6E569703038528A529ADC1D7143296B375021DE3C) |
| SOUTH\_EAST | 9 | 向东南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Er_tpv8UQP6XlgA-pq4nug/zh-cn_image_0000002569021215.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=B6A5C1CCA3B2E1904C4E8D6461940389CAA4BF01B7F0A5F330E450CF0E8634D5) |
| SOUTH\_WEST | 10 | 向西南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/D14E2mcCRKmHsshu5Ru5Lg/zh-cn_image_0000002568901205.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=6994AB54880870FEE02B7C18D1BFF71FB7A03BD1112A63A7D17D9F4CE08908BC) |
| NORTH\_EAST\_SOUTH\_WEST | 11 | 东北西南调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/vfONy3pNQ7G8SLSXyPrAYw/zh-cn_image_0000002538021504.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=D9B811935453E4E2151F8CF24ADE96F54290D1FB9A5FB33A3280A24654D24649) |
| NORTH\_WEST\_SOUTH\_EAST | 12 | 西北东南调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/HAQFMb1lSx2_C_RVnp0BIA/zh-cn_image_0000002538181430.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=5425DFFFEA976BE4698A12860413EFA80976CE5C8F8DC149F55181E3F1DBDBD0) |
| CROSS | 13 | 准确选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/W5LTIgZFSZ2wph78ZmqVvQ/zh-cn_image_0000002569021217.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=C0405A56210422EE30AE393ECDF67E4507AE9CE7F863DE67666831C7CB0A0C12) |
| CURSOR\_COPY | 14 | 拷贝 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/qgMG8hVYSaihKEC6XDderw/zh-cn_image_0000002568901207.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=B95BF54808C65C4C33BC52DC35010CB0762B0DEE9102C1FE9EC6D9BA27FB3D7F) |
| CURSOR\_FORBID | 15 | 不可用 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/aQxyc1gYTVSqwJtZWGpSww/zh-cn_image_0000002538021506.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=20F4A99989070ED32698DFCA0F724590921AF233831CF4A2D5081ACFBD0E0F36) |
| COLOR\_SUCKER | 16 | 取色器 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/GjGfShpuTL2Cs1lPmrv4Rg/zh-cn_image_0000002538181432.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=CDF9E8EA6232369632196A1C45B8A72B912F0396DA5E7B0B9242218BC5FCEF7B) |
| HAND\_GRABBING | 17 | 并拢的手 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Sj_g9nppRZiqoLMtPuFB9Q/zh-cn_image_0000002569021219.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=C954C9B58133B1CE00868080726B78459360CCBDD9E7174342BEC87927E81912) |
| HAND\_OPEN | 18 | 张开的手 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/U8nh5uuqTGu2t287jDTKWw/zh-cn_image_0000002568901209.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=8B583AE41F42185990A1DCA049C3D25DE948F6518A4D2BE458C99FD21C5F124F) |
| HAND\_POINTING | 19 | 手形指针 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/nUOC-41kRuqSqgJJ1j3wAA/zh-cn_image_0000002538021508.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=C79A40FB1E269B336E26F96C162D8E13ED36162AB978C1822B482BAFEE6DDCAB) |
| HELP | 20 | 帮助选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/I3WmY9c3SvSYdN5de7N6Gw/zh-cn_image_0000002538181434.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=93B46DDD68C0DD73EF8A3811983BEBD742FB43576BDEDCB8E755D00E8C5DE48F) |
| MOVE | 21 | 移动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/jcFO4ywAQa6FHcazy85lkA/zh-cn_image_0000002569021221.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=72C40A9E3C64C5C87C2A38BF24EE0AE93E7619AD0690DBDC693CB36F295A9D88) |
| RESIZE\_LEFT\_RIGHT | 22 | 内部左右调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/cp1TLl0bTIC-Ofee0HszwQ/zh-cn_image_0000002568901211.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=8D515487E7CD520690E286061B6C180A9BC1711A8F84D77047E12907E25204E7) |
| RESIZE\_UP\_DOWN | 23 | 内部上下调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/D_6i4GRTShuc3VHGn7YqvA/zh-cn_image_0000002538021510.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=642C5A047D2F38A12FB80CC8834D827294190DCC7C0776A1905F58ED1C453CD1) |
| SCREENSHOT\_CHOOSE | 24 | 截图十字准星 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/iMr_Ni3tQ12ejDODw6kiVQ/zh-cn_image_0000002538181436.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=A88307F7355D57278848CC2935833F0876567B76AC3C2D5D3C13A1AA9AB7E813) |
| SCREENSHOT\_CURSOR | 25 | 截图 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/a6ira4buQp6_jL8FQl2MBA/zh-cn_image_0000002569021223.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=0247742BD47BCAA18873F3FF7086E328560F9812FA776CCEDFDB03CF5C1DE16D) |
| TEXT\_CURSOR | 26 | 文本选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/RWtM0Y2DT4-xdSgpro8_8Q/zh-cn_image_0000002568901213.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=7657E49CB29071D7F2A1BFA1461D2A2D048D75AA448FA2A1CFB10D6482362BC6) |
| ZOOM\_IN | 27 | 放大 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/diYKyyOOQi63eFZsOFGxtA/zh-cn_image_0000002538021512.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=B7A0D001DC7DAD5EAF2C46B017FF93B82ED9A6A4A6DCB18114385A79064F89AF) |
| ZOOM\_OUT | 28 | 缩小 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/V5pVNA-4RIGNBW-wOYPzfw/zh-cn_image_0000002538181438.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=905A0C8F50236B1B5D55157AC6E3708E155C1E7A9FF9423E3B907A7061375263) |
| MIDDLE\_BTN\_EAST | 29 | 向东滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/9JRBqvEAQhCuko15g3xtMQ/zh-cn_image_0000002569021225.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=1154D0D52BC8C5FE1B92288588C6F1B20199815E3D9872DE6C3383419891123C) |
| MIDDLE\_BTN\_WEST | 30 | 向西滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ji4ztQIeQ7ClPqa5bPveIQ/zh-cn_image_0000002568901215.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=0E053241EC071027D2B58FC012FD39DAD0A6B6E9F60E2569403D2D3937BA4233) |
| MIDDLE\_BTN\_SOUTH | 31 | 向南滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/6CRykLvoTdu0HeH0rBnfKQ/zh-cn_image_0000002538021514.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=D9DA8B7814C46C55B3DC4530220CB50DBDD5F5DD8CAF96554D61B658B12E2E87) |
| MIDDLE\_BTN\_NORTH | 32 | 向北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Ae-GCbKfS3qO9TCa0yNJOA/zh-cn_image_0000002538181440.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=30F7FCE0277F50624C87C414A3D5656463502D9E6CD13302074891DC4709824E) |
| MIDDLE\_BTN\_NORTH\_SOUTH | 33 | 向南北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/I5n54JLvRPaKD7hxa4Lw8g/zh-cn_image_0000002569021227.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=5DE0C350F03C0BAB9FDBC774FB6303EB1174AD03D4E2F464FCABD3BA73417ABC) |
| MIDDLE\_BTN\_NORTH\_EAST | 34 | 向东北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/tvrpETXYQCSMw8q_fg2JGA/zh-cn_image_0000002568901217.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=211B8FBBFBC4964FB51B81603AA504B5E88C27CA353103632C6EE97BF5809ACC) |
| MIDDLE\_BTN\_NORTH\_WEST | 35 | 向西北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/dSDLlWdyTN2ILX_E_dYavw/zh-cn_image_0000002538021516.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=3463943FC4359AB1E73A3F407EBC9194E4123A4A105AC6DE8E1DC1544B69A55B) |
| MIDDLE\_BTN\_SOUTH\_EAST | 36 | 向东南滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/AHo57ERwRLWjdym_OqQg0Q/zh-cn_image_0000002538181442.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=046F80E042BA6BF90AF55991E9632280A316741E19D93324EB3680136F16DAAD) |
| MIDDLE\_BTN\_SOUTH\_WEST | 37 | 向西南滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/q4F-iB6DSXm_YS8Kdl7XVg/zh-cn_image_0000002569021229.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=65300755CAA8225BE7836FD8185806E7EBFBF04FE1F378FB14D33CCD243533CA) |
| MIDDLE\_BTN\_NORTH\_SOUTH\_WEST\_EAST | 38 | 四向锥形移动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/4jl3j1sFQTCwgeyY0ddOMQ/zh-cn_image_0000002568901219.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=29A7E39E5ECAB93CA174AB81C5F8B2FF54949CBE44211A4A29EEA1E6AEAC82A8) |
| HORIZONTAL\_TEXT\_CURSOR10+ | 39 | 垂直文本选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/B1wDYh6pS0OfaLBpkGNjJA/zh-cn_image_0000002538021518.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=8614A364D5AB0AF73A8AE6C69DDFE6511ECB9060EFC0FE7E1639210A8BF3196B) |
| CURSOR\_CROSS10+ | 40 | 十字光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/3lIrGhH0SwyhlT7A2AmuHw/zh-cn_image_0000002538181444.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=083A15FF813DEC4508EFCD194B133D1F329FCFA2F6DADDDB7B33607308CB571F) |
| CURSOR\_CIRCLE10+ | 41 | 圆形光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/xC8aJfcrQ0eBQgcP57qWYQ/zh-cn_image_0000002569021231.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=98410D584BE26905A307903C1BF942D8E5A988B66598218F19996F6C05119FC6) |
| LOADING10+ | 42 | 
正在载入动画光标

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Yp2a1gnDRBmxzqjWCaRnVQ/zh-cn_image_0000002568901221.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=2DB2D68584912C57AA3B3420352F1B8E2F17DCF79D40A38927FCCF31A15B3758) |
| RUNNING10+ | 43 | 

后台运行中动画光标

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/5m1ds1LQSc-5FrPZH9mkRQ/zh-cn_image_0000002538021520.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=6C873429DC9F813213D9E98A2E757A47416D7D21D5C9E36B5735EC5FD9A1C02A) |
| MIDDLE\_BTN\_EAST\_WEST18+ | 44 | 向东西滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/aenOb6uPQl-pOjslbdVipQ/zh-cn_image_0000002538181446.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=69C466145CFCC5FB5FD325F69B8020D0AE890D81C1FFAE3E52AB92D186C97759) |
| RUNNING\_LEFT22+ | 45 | 后台运行中动画光标(拓展1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/arHvmw3rS52IIYhuK3gi1g/zh-cn_image_0000002569021233.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=562A24567B045318CF9A5204211DEA8AB55D4B2182481CB6D26960F0E83EBF3F) |
| RUNNING\_RIGHT22+ | 46 | 后台运行中动画光标(拓展2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/AuzwXhXMQkCXS_Ut8ZYJmA/zh-cn_image_0000002568901223.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=EDDFF5026C6C05418BF82EAF24347239B6A82C9DC29D3763E68FFE691B3A5A8B) |
| AECH\_DEVELOPER\_DEFINED\_ICON22+ | 47 | 圆形自定义光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/qa2DgNKhRaqksxkVi9kzDA/zh-cn_image_0000002538021522.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F449F03A87E48C48B8E3948E7793F3882955F9D3BB3F2D1A6D866B5C13AD2E80) |
| SCREENRECORDER\_CURSOR20+ | 48 | 录屏光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/DraLSYPnS3iJXOY9Ihhs3w/zh-cn_image_0000002538181448.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=CD9114376D859FB5F47304B7548701D35BB2AB1863F7D8F2BE5AE412CF3A9DBB) |
| LASER\_CURSOR22+ | 49 | 

悬浮光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/fAkdXssPQ7Kvy4ktEGuzmw/zh-cn_image_0000002569021235.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=1F22CE2945892F75D1335F0F607D0F1E5B9B4D097D6A56F9F45EFC5AFC142889) |
| LASER\_CURSOR\_DOT22+ | 50 | 

点击光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/a823RDteR8KyrbzuLO7vYg/zh-cn_image_0000002568901225.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=A7EA23C0CC2607D4838595B3C5687E5BD0682429FC98EBC9BB616140853172D2) |
| LASER\_CURSOR\_DOT\_RED22+ | 51 | 

激光笔光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/JeOpCV5LTr6olQwyDa78rQ/zh-cn_image_0000002538021524.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=896DDB2F05A60924B9F46272265E2E9407108C633A6B2EE5161AED5B1D304516) |
| DEVELOPER\_DEFINED\_ICON22+ | \-100 | 自定义光标，开发者可使用[setCustomCursor](#pointersetcustomcursor15)设置自定义光标，不支持使用[setPointerStyle](#pointersetpointerstyle-1)直接设置。 | 自定义光标样式，通过接口设置。 |

#### pointer.setCustomCursor11+

setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>

设置指定窗口的自定义光标样式，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 窗口ID。 |
| pixelMap | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | 自定义光标资源。 |
| focusX | number | 否 | 自定义光标焦点x，取值范围：大于等于0，默认为0。 |
| focusY | number | 否 | 自定义光标焦点y，取值范围：大于等于0，默认为0。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon为示例资源，请开发者根据实际需求配置资源文件。
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, pixelMap).then(() => {
                    console.info(`setCustomCursor success`);
                  });
                } catch (error) {
                  console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            }).catch((error: BusinessError) => {
                console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
          });
        })
    }
  }
}
```

#### CustomCursor15+

自定义光标资源。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| pixelMap | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 否 | 否 | 自定义光标。最小限制为资源图本身的最小限制。最大限制为256 x 256px。 |
| focusX | number | 否 | 是 | 自定义光标焦点的水平坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的宽度最大值，该参数缺省时默认为0。 |
| focusY | number | 否 | 是 | 自定义光标焦点的垂直坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的高度最大值，该参数缺省时默认为0。 |

#### CursorConfig15+

自定义光标配置。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| followSystem | boolean | 否 | 否 | 是否根据系统设置调整光标大小。false表示使用自定义光标样式大小，true表示根据系统设置调整光标大小，可调整范围为：\[光标资源图大小，256×256\]。 |

#### pointer.setCustomCursor15+

setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>

设置指定窗口的自定义光标样式，使用Promise异步回调。

应用窗口布局改变、热区切换、页面跳转、光标移出再回到窗口、光标在窗口不同区域移动，以上场景可能导致光标切换回系统样式，需要开发者重新设置光标样式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 窗口ID。 |
| cursor | [CustomCursor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pointer#customcursor15) | 是 | 自定义光标资源。 |
| config | [CursorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pointer#cursorconfig15) | 是 | 自定义光标配置，用于配置是否根据系统设置调整光标大小。如果CursorConfig中followSystem设置为true，则光标大小的可调整范围为：\[光标资源图大小，256×256\]。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[鼠标光标错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pointer)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Abnormal windowId parameter passed in. 2. Abnormal pixelMap parameter passed in; 3. Abnormal focusX parameter passed in.4. Abnormal focusY parameter passed in. |
| 26500001 | Invalid windowId. Possible causes: The window id does not belong to the current process. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon为示例资源，请开发者根据实际需求配置资源文件。
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, { pixelMap: pixelMap, focusX: 25, focusY: 25 },
                    { followSystem: false }).then(() => {
                    console.info(`setCustomCursor success`);
                  });
                } catch (error) {
                  console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            }).catch((error: BusinessError) => {
                console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
          });
        })
    }
  }
}
```

#### pointer.setCustomCursorSync11+

setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void

设置指定窗口的自定义光标样式，使用同步方式进行设置。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 窗口ID。取值为大于0的整数。 |
| pixelMap | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | 自定义光标资源。 |
| focusX | number | 否 | 自定义光标焦点x，取值范围：大于等于0，默认为0。 |
| focusY | number | 否 | 自定义光标焦点y，取值范围：大于等于0，默认为0。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon为示例资源，请开发者根据实际需求配置资源文件。
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer = svgFileData.buffer;
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursorSync(windowId, pixelMap, 25, 25);
                  console.info(`setCustomCursorSync success`);
                } catch (error) {
                  console.error(`setCustomCursorSync failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            }).catch((error: BusinessError) => {
              console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          });
        }
      )
    }
  }
}
```
