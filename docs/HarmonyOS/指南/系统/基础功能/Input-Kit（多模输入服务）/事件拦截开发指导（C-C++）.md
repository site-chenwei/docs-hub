---
title: "事件拦截开发指导（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/interceptor-guidelines"
menu_path:
  - "指南"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "事件拦截开发指导（C/C++）"
captured_at: "2026-04-17T01:35:55.814Z"
---

# 事件拦截开发指导（C/C++）

#### 功能介绍

从API version 12开始，多模为应用提供了创建和删除按键、输入事件（鼠标、触摸和轴事件）拦截的能力。使用场景例如：云桌面应用需要拦截按键、鼠标、触摸和轴事件。

#### 接口说明

创建和删除事件拦截相关接口如下表所示，接口详细介绍请参考[Input文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)。

| 接口名称 | 描述 |
| :-- | :-- |
| Input\_Result OH\_Input\_AddKeyEventInterceptor(Input\_KeyEventCallback callback, Input\_InterceptorOptions \*option) | 创建按键事件拦截。 |
| Input\_Result OH\_Input\_AddInputEventInterceptor(Input\_InterceptorEventCallback \*callback, Input\_InterceptorOptions \*option) | 创建输入事件拦截，包含鼠标、触摸和轴事件。 |
| Input\_Result OH\_Input\_RemoveKeyEventInterceptor() | 删除按键事件拦截。 |
| Input\_Result OH\_Input\_RemoveInputEventInterceptor() | 删除输入事件拦截，包含鼠标、触摸和轴事件。 |

#### 开发步骤

#### \[h2\]链接动态库

调用创建和删除事件拦截前，需链接相关动态库。链接动态库的方法是，在CMakeList.txt文件中做下面例子所示的配置：

```txt
target_link_libraries(entry PUBLIC libohinput.so)
```

#### \[h2\]申请所需权限

应用需要在module.json5中添加下面权限的配置，详细的配置方法参考[声明权限文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

```json
"requestPermissions": [
    {
        "name": "ohos.permission.INTERCEPT_INPUT_EVENT"
    }
]
```

#### \[h2\]创建事件拦截

-   **按键事件**

struct KeyEvent {
    int32\_t action;
    int32\_t keyCode;
    int64\_t actionTime { -1 };
};

//定义按键事件回调函数
void OnKeyEventCallback(const Input\_KeyEvent\* keyEvent)
{
    KeyEvent event;
    //Input\_KeyEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    event.action = OH\_Input\_GetKeyEventAction(keyEvent);
    event.keyCode = OH\_Input\_GetKeyEventKeyCode(keyEvent);
    event.actionTime = OH\_Input\_GetKeyEventActionTime(keyEvent);
    // ...
}

static napi\_value AddKeyEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddKeyEventInterceptor(OnKeyEventCallback, nullptr);
    // ...
}

static napi\_value RemoveKeyEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveKeyEventInterceptor();
    // ...
}

-   **输入拦截（鼠标、触摸和轴事件）**

struct MouseEvent {
    int32\_t action;
    int32\_t displayX;
    int32\_t displayY;
    int32\_t button { -1 };
    int32\_t axisType { -1 };
    float axisValue { 0.0f };
    int64\_t actionTime { -1 };
};

struct TouchEvent {
    int32\_t action;
    int32\_t id;
    int32\_t displayX;
    int32\_t displayY;
    int64\_t actionTime { -1 };
};

struct AxisEvent {
    int32\_t axisAction;
    float displayX;
    float displayY;
    std::map<int32\_t, double> axisValues;
    int64\_t actionTime { -1 };
    int32\_t sourceType;
    int32\_t axisEventType { -1 };
};

//定义鼠标事件回调函数
void OnMouseEventCallback(const Input\_MouseEvent\* mouseEvent)
{
    MouseEvent event;
    //Input\_MouseEvent的生命周期仅在回调函数内，出了回调函数会被销毁
    event.action = OH\_Input\_GetMouseEventAction(mouseEvent);
    event.displayX = OH\_Input\_GetMouseEventDisplayX(mouseEvent);
    event.displayY = OH\_Input\_GetMouseEventDisplayY(mouseEvent);
    event.button = OH\_Input\_GetMouseEventButton(mouseEvent);
    event.axisType = OH\_Input\_GetMouseEventAxisType(mouseEvent);
    event.axisValue = OH\_Input\_GetMouseEventAxisValue(mouseEvent);
    event.actionTime = OH\_Input\_GetMouseEventActionTime(mouseEvent);
    // ···
}

//定义触摸事件回调函数
void OnTouchEventCallback(const Input\_TouchEvent\* touchEvent)
{
    TouchEvent event;
    //Input\_TouchEvent的生命周期仅在回调函数内，出了回调函数会被销毁
    event.action = OH\_Input\_GetTouchEventAction(touchEvent);
    event.id = OH\_Input\_GetTouchEventFingerId(touchEvent);
    event.displayX = OH\_Input\_GetTouchEventDisplayX(touchEvent);
    event.displayY = OH\_Input\_GetTouchEventDisplayY(touchEvent);
    event.actionTime = OH\_Input\_GetTouchEventActionTime(touchEvent);
    // ···
}

//定义轴事件回调函数
void OnAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    
    //Input\_AxisEvent的生命周期仅在回调函数内，出了回调函数会被销毁
    InputEvent\_AxisAction action;
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType;
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType;
    ret = OH\_Input\_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    if (event.axisEventType == AXIS\_EVENT\_TYPE\_PINCH) {
        double value = 0;
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_PINCH, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_PINCH, value));
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_ROTATE, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_ROTATE, value));
    } else if (event.axisEventType == AXIS\_EVENT\_TYPE\_SCROLL) {
        double value = 0;
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_VERTICAL, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_VERTICAL, value));
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_HORIZONTAL, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_HORIZONTAL, value));
    }
    // ···
}

//输入事件回调函数结构体
Input\_InterceptorEventCallback g\_eventCallback;

static napi\_value AddEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    //设置鼠标事件回调函数
    g\_eventCallback.mouseCallback = OnMouseEventCallback;
    //设置触摸事件回调函数
    g\_eventCallback.touchCallback = OnTouchEventCallback;
    //设置轴事件回调函数
    g\_eventCallback.axisCallback = OnAxisEventCallback;
    Input\_Result ret = OH\_Input\_AddInputEventInterceptor(&g\_eventCallback, nullptr);
    // ···
}

static napi\_value RemoveEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveInputEventInterceptor();
    // ···
}

#### 完整示例

-   [输入事件拦截（C/C++）](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/InputKit/NDKInputEventInterceptor)
