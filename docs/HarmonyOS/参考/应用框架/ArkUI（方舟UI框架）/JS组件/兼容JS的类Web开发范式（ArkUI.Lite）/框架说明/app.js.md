---
title: "app.js"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-file"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Lite）"
  - "框架说明"
  - "app.js"
captured_at: "2026-04-17T01:48:06.153Z"
---

# app.js

#### 应用生命周期4+

每个应用可以在app.js自定义应用级生命周期的实现逻辑，包括：

-   onCreate：在应用生成时被调用的生命周期函数。
    
-   onDestroy：在应用销毁时被调用的生命周期函数。
    

以下示例仅在生命周期函数中打印对应日志：

```js
// app.js
export default {
  onCreate() {
    console.info('Application onCreate');
  },
  onDestroy() {
    console.info('Application onDestroy');
  },
}
```

#### 应用对象10+

| 属性 | 类型 | 描述 |
| :-- | :-- | :-- |
| getApp | Function | 提供getApp()全局方法，可以在页面js文件中获取app.js中暴露的数据对象。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/dlq1EO5wQ0qymPhZmHm1Rg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=413AE9F332E8796B6F2382671F9827DFC8D66ADCDA28F1CF2A1459066F6C3B63)

应用对象是全局数据，其在整个应用消亡之前都会一直占用JS内存。尽管应用对象可为不同页面共享数据提供便利，但因为小型设备本身内存比较小，也应谨慎使用。如果过度使用，则容易造成应用在进入复杂page页面时，内存不够而出现异常。

示例如下：

在 app.js 中声明应用对象:

```javascript
// app.js
export default {
    data: {
        test: "by getApp"
    },
    onCreate() {
        console.info('Application onCreate');
    },
    onDestroy() {
        console.info('Application onDestroy');
    },
};
```

在具体的页面中访问应用对象：

```javascript
// index.js
export default {
    data: {
        title: ""
    },
    onInit() {
        if (typeof getApp !== 'undefined') {
            var appData = getApp().data;
            if (typeof appData !== 'undefined') {
                this.title = appData.name; // read from app data
            }
        }
    },
    clickHandler() {
        if (typeof getApp !== 'undefined') {
            var appData = getApp().data;
            if (typeof appData !== 'undefined') {
                appData.name = this.title; // write to app data
            }
        }
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/aSghEoGMR0qjIbjyCPNXYA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014806Z&HW-CC-Expire=86400&HW-CC-Sign=23A1782242DE584CC7175F513E1CB9868409E6FAF942685E4F8D86AEFCCCC84B)

为了应用可在不支持getApp的低版本上正常运行，代码中应进行兼容性处理，即在使用getApp前先判断其是否可用。
