---
title: "同步方式动态加载Native模块"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-apis-load-native-module"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkTS（方舟编程语言）"
  - "ArkTS运行时"
  - "ArkTS模块化"
  - "同步方式动态加载Native模块"
captured_at: "2026-04-17T01:35:35.178Z"
---

# 同步方式动态加载Native模块

[loadNativeModule接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-common-load-native-module)用于同步动态加载Native模块，目的是按需加载所需要的模块。使用该接口会增加加载so文件的时间，开发者需评估其对功能的影响。

#### 函数说明

```js
loadNativeModule(moduleName: string): Object;
```

| 参数 | 说明 |
| :-- | :-- |
| moduleName | 加载的模块名。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/xhXb0vEzSiSmCKH2gDAwwQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013535Z&HW-CC-Expire=86400&HW-CC-Sign=A0D31702DA323FF67862AF03911CB47FD466C138D710C30632848CED16E082ED)

loadNativeModule加载的模块名是指依赖方oh-package.json5文件的dependencies中的名字。

loadNativeModule必须在UI主线程中调用。

该接口在加载常量字符串或变量表达式作为参数时，需要配置依赖。

#### loadNativeModule支持的场景

| 场景 | 示例 |
| :-- | :-- |
| 系统库模块 | 加载@ohos.或@system. |
| 应用内Native模块 | 加载libNativeLibrary.so |

#### 使用示例

-   **HAP加载系统库模块**

```js
let hilog: ESObject = loadNativeModule("@ohos.hilog");
hilog.info(0, "testTag", "loadNativeModule ohos.hilog success");
```

-   **HAP加载Native库**

libentry.so的index.d.ts文件如下：

```javascript
//index.d.ts
export const add: (a: number, b: number) => number;
```

1.加载本地so库时，需要在oh-package.json5文件中配置dependencies项。

```json
{
  "dependencies": {
    "libentry.so": "file:./src/main/cpp/types/libentry"
  }
}
```

2.在build-profile.json5中进行配置。

```json
{
  "buildOption": {
    "arkOptions": {
      "runtimeOnly": {
        "packages": [
          "libentry.so"
        ]
      }
    }
  }
}
```

3.使用loadNativeModule加载libentry.so，并调用add函数。

```js
let module: ESObject = loadNativeModule("libentry.so");
let sum: number = module.add(1, 2);
```
