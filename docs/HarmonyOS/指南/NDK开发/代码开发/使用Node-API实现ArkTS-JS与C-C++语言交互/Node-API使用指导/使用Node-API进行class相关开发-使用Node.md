---
title: "使用Node"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class"
menu_path:
  - "指南"
  - "NDK开发"
  - "代码开发"
  - "使用Node-API实现ArkTS/JS与C/C++语言交互"
  - "Node-API使用指导"
  - "使用Node-API进行class相关开发"
captured_at: "2026-04-17T01:36:40.545Z"
---

# 使用Node-API进行class相关开发

#### 简介

使用Node-API接口进行class相关开发，处理ArkTS中的类，例如定义类、构造实例等。

#### 基本概念

在使用Node-API接口进行class相关开发时，需要理解以下基本概念：

-   **类**：类是用于创建对象的模板。它提供了一种封装数据和行为的方式，以便于对数据进行处理和操作。类在ArkTS中是建立在原型（prototype）的基础上的，并且还引入了一些类独有的语法和语义。
-   **实例**：实例是通过类创建具体的对象。类定义了对象的结构和行为，而实例则是类的具体表现。通过实例化类，我们可以访问类中定义的属性和方法，并且每个实例都具有自己的属性值。
-   **原型**：ArkTS也采用Class的概念来实现类型之间的继承，早期EcmaScript规范定义了原型的概念，对象通过原型链的方式来实现继承的。原型的概念可以参考[EcmaScript的社区规范](https://262.ecma-international.org/#sec-terms-and-definitions-prototype)。

#### 场景和功能介绍

以下Node-API接口主要用于处理class。他们的使用场景如下：

| 接口 | 描述 |
| :-- | :-- |
| napi\_new\_instance | 需要通过给定的构造函数构建一个实例时，可以使用这个函数。 |
| napi\_get\_new\_target | 使用此函数获取构造函数调用的new.target。 |
| napi\_define\_class | 在Node-API模块定义与ArkTS类相对应的类。这个函数允许将Node-API模块类绑定到ArkTS类。 |
| napi\_wrap | 在ArkTS对象上绑定一个Node-API模块对象实例。这个函数通常在将Node-API模块对象与ArkTS对象进行绑定时使用，以便在ArkTS中使用本地对象的方法和属性。 |
| napi\_unwrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例。 |
| napi\_remove\_wrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例，并解除绑定。 |

#### 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process)，本文仅对接口对应C++及ArkTS相关代码进行展示。

#### \[h2\]napi\_new\_instance

通过给定的构造函数实例化一个对象，将这个对象返回ArkTS侧使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/y8b01ML_RA-zzirSB7mNxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013640Z&HW-CC-Expire=86400&HW-CC-Sign=E00B9927D7F8B1766868FF50FBAA555988736C290933DD1E3A88DDA794DD4095)

参数constructor不是function类型则返回napi\_function\_expected。

cpp部分代码

```
// napi_new_instance
static napi_value NewInstance(napi_env env, napi_callback_info info)
{
    // 传入并解析参数，第一个参数为传入的构造函数，第二个参数为需要传入构造函数的参数
    size_t argc = 2;
    napi_value args[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    // 调用napi_new_instance接口，实例化一个对象，将这个对象返回
    napi_value result = nullptr;
    napi_new_instance(env, args[0], 1, &args[1], &result);
    return result;
}
```

接口声明

```typescript
export const newInstance: (obj: Object, param: string) => Object; // napi_new_instance
```

ArkTS侧示例代码

```typescript
class Fruit {
  name: string;

  constructor(name: string) {
    this.name = name;
  }
}
```

```typescript
// napi_new_instance
// 调用函数，用变量obj接收函数返回的实例化对象
let obj = testNapi.newInstance(Fruit, 'test');
// 打印实例化对象obj的信息
hilog.info(0x0000, 'Node-API', 'napi_new_instance %{public}s', JSON.stringify(obj));
```

#### \[h2\]napi\_get\_new\_target

用于获取构造函数的new.target值。在ArkTS中，new.target是一个特殊的元属性，用于在构造函数中判断是否通过new关键字调用了该构造函数。

示例代码可以参考链接：

[Native与ArkTS对象绑定](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-object-wrap)

#### \[h2\]napi\_define\_class

用于定义一个ArkTS类。该函数允许在Node-API模块中创建一个ArkTS类，并将类的方法和属性与相应的Node-API模块关联起来。

示例代码可以参考链接：

[Native与ArkTS对象绑定](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-object-wrap)

#### \[h2\]napi\_wrap

在ArkTS object上绑定一个native对象实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/K0yF_5O6TZS8BGfXd-ulyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013640Z&HW-CC-Expire=86400&HW-CC-Sign=9E2347ECE3511B872D961EABEA09C5DAD59E51E6907F5EDFD3AEEC7A12B079E3)

参数js\_object不为object类型或function类型时返回napi\_object\_expected。

#### \[h2\]napi\_unwrap

从一个被包装的对象中获取与之关联的数据指针。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/RMrVVYY2RXeOg2nJXePdgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013640Z&HW-CC-Expire=86400&HW-CC-Sign=EBFB63F6DB4713401FD8E1B9D52693434A7C917AE19A0D1C4080E400F6B3CE36)

参数js\_object不为object类型或function类型时返回napi\_object\_expected。

#### \[h2\]napi\_remove\_wrap

从ArkTS object上获取先前绑定的native对象实例，并解除绑定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/We2AWXljTYue7W-y8I0kxQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013640Z&HW-CC-Expire=86400&HW-CC-Sign=FA003597DD44AB9B3BD2A65B3DEAE4467A7D79119E54784877D13A1FB676F696)

参数js\_object不为object类型或function类型时返回napi\_object\_expected。

cpp部分代码

```
struct Object {
    std::string name;
    int32_t age;
};

static void DerefItem(napi_env env, void *data, void *hint)
{
    // 可选的原生回调，用于在ArkTS对象被垃圾回收时释放原生实例
    OH_LOG_INFO(LOG_APP, "Node-API DerefItem");
    Object *obj = reinterpret_cast<Object *>(data);
    if (obj != nullptr) {
        delete obj;
    }
}

// napi_wrap
static napi_value Wrap(napi_env env, napi_callback_info info)
{
    OH_LOG_INFO(LOG_APP, "Node-API wrap");
    // 初始化Node-API模块的object
    struct Object *obj = new struct Object();
    obj->name = "liLei";
    obj->age = INT_ARG_18;
    size_t argc = 1;
    napi_value toWrap;
    // 调用napi_wrap将Node-API模块的object绑定到ArkTS object上
    napi_status status_cb = napi_get_cb_info(env, info, &argc, &toWrap, NULL, NULL);
    if (status_cb != napi_ok) {
        OH_LOG_ERROR(LOG_APP, "napi_get_cb_info failed");
        delete obj;
        return nullptr;
    }
    napi_status status = napi_wrap(env, toWrap, reinterpret_cast<void *>(obj), DerefItem, NULL, NULL);
    if (status != napi_ok) {
        // 主动释放内存
        delete obj;
    }

    return toWrap;
}

// napi_remove_wrap
static napi_value RemoveWrap(napi_env env, napi_callback_info info)
{
    OH_LOG_INFO(LOG_APP, "Node-API removeWrap");
    size_t argc = 1;
    napi_value wrapped = nullptr;
    void *data = nullptr;
    // 调用napi_remove_wrap从一个被包装的对象中解除包装
    napi_get_cb_info(env, info, &argc, &wrapped, nullptr, nullptr);
    napi_status status = napi_remove_wrap(env, wrapped, &data);
    if (status != napi_ok || data == nullptr) {
        OH_LOG_ERROR(LOG_APP, "Node-API napi_remove_wrap failed or data is nullptr");
        return nullptr;
    }

    return nullptr;
}

// napi_unwrap
static napi_value UnWrap(napi_env env, napi_callback_info info)
{
    OH_LOG_INFO(LOG_APP, "Node-API unWrap");
    size_t argc = 1;
    napi_value wrapped = nullptr;
    napi_get_cb_info(env, info, &argc, &wrapped, nullptr, nullptr);
    // 调用napi_unwrap取出绑定在ArkTS object中的数据并打印
    struct Object *data = nullptr;
    napi_status status = napi_unwrap(env, wrapped, reinterpret_cast<void **>(&data));
    if (status != napi_ok || data == nullptr) {
        OH_LOG_ERROR(LOG_APP, "Node-API napi_unwrap failed or data is nullptr");
        return nullptr;
    }
    OH_LOG_INFO(LOG_APP, "Node-API name: %{public}s", data->name.c_str());
    OH_LOG_INFO(LOG_APP, "Node-API age: %{public}d", data->age);
    return nullptr;
}
```

接口声明

```typescript
export const wrap: (obj: Object) => Object; // napi_wrap

export const unWrap: (obj: Object) => void; // napi_unwrap

export const removeWrap: (obj: Object) => void; // napi_remove_wrap
```

ArkTS侧示例代码

```typescript
try {
  class Obj {
  }

  let obj: Obj = {};
  testNapi.wrap(obj); // napi_wrap
  testNapi.unWrap(obj); // napi_unwrap
  testNapi.removeWrap(obj); // napi_remove_wrap
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API error: %{public}s', error.message);
  // ...
}
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```text
// CMakeLists.txt
add_definitions( "-DLOG_DOMAIN=0xd0d0" )
add_definitions( "-DLOG_TAG=\"testTag\"" )
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
