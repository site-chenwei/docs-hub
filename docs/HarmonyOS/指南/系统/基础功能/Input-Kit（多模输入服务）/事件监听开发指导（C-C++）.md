---
title: "事件监听开发指导（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/monitor-guidelines"
menu_path:
  - "指南"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "事件监听开发指导（C/C++）"
captured_at: "2026-04-17T01:35:55.774Z"
---

# 事件监听开发指导（C/C++）

#### 功能介绍

从API version 12开始，多模为应用提供了按键、输入事件（鼠标、触屏和轴事件）监听能力，当前仅支持录屏类应用。使用场景例如：用户在录屏应用开启录屏时，监听设备的按键、鼠标、触摸和轴事件。

#### 接口说明

创建和删除事件监听相关接口如下表所示，接口详细介绍请参考[Input文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)。

| 接口名称 | 描述 |
| :-- | :-- |
| Input\_Result OH\_Input\_AddKeyEventMonitor(Input\_KeyEventCallback callback) | 创建按键事件监听。 |
| Input\_Result OH\_Input\_AddMouseEventMonitor(Input\_MouseEventCallback callback) | 创建鼠标事件监听。 |
| Input\_Result OH\_Input\_AddTouchEventMonitor(Input\_TouchEventCallback callback) | 创建触摸事件监听。 |
| Input\_Result OH\_Input\_AddAxisEventMonitorForAll(Input\_AxisEventCallback callback) | 创建所有类型轴事件监听。 |
| Input\_Result OH\_Input\_AddAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback) | 创建指定类型轴事件监听。 |
| Input\_Result OH\_Input\_RemoveKeyEventMonitor(Input\_KeyEventCallback callback) | 删除按键事件监听。 |
| Input\_Result OH\_Input\_RemoveMouseEventMonitor(Input\_MouseEventCallback callback) | 删除鼠标事件监听。 |
| Input\_Result OH\_Input\_RemoveTouchEventMonitor(Input\_TouchEventCallback callback) | 删除触摸事件监听。 |
| Input\_Result OH\_Input\_RemoveAxisEventMonitorForAll(Input\_AxisEventCallback callback) | 删除所有类型轴事件监听。 |
| Input\_Result OH\_Input\_RemoveAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback) | 删除指定类型轴事件监听。 |

#### 开发步骤

#### \[h2\]链接动态库

调用创建和删除事件监听前，需链接相关动态库。链接动态库的方法是，在CMakeList.txt文件中新增如下配置：

```txt
target_link_libraries(entry PUBLIC libohinput.so)
```

#### \[h2\]申请所需权限

应用需要在module.json5中添加下面权限的配置，详细的配置方法参考声明[声明权限文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

```json
"requestPermissions": [
    {
        "name": "ohos.permission.INPUT_MONITORING"
    }
]
```

#### \[h2\]创建事件监听

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

static napi\_value AddKeyEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddKeyEventMonitor(OnKeyEventCallback);
    // ...
}

static napi\_value RemoveKeyEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveKeyEventMonitor(OnKeyEventCallback);
    // ...
}

-   **鼠标事件**

struct MouseEvent {
    int32\_t action;
    int32\_t displayX;
    int32\_t displayY;
    int32\_t button { -1 };
    int32\_t axisType { -1 };
    float axisValue { 0.0f };
    int64\_t actionTime { -1 };
};

//定义鼠标事件回调函数
void OnMouseEventCallback(const Input\_MouseEvent\* mouseEvent)
{
    MouseEvent event;
    //Input\_MouseEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    event.action = OH\_Input\_GetMouseEventAction(mouseEvent);
    event.displayX = OH\_Input\_GetMouseEventDisplayX(mouseEvent);
    event.displayY = OH\_Input\_GetMouseEventDisplayY(mouseEvent);
    event.button = OH\_Input\_GetMouseEventButton(mouseEvent);
    event.axisType = OH\_Input\_GetMouseEventAxisType(mouseEvent);
    event.axisValue = OH\_Input\_GetMouseEventAxisValue(mouseEvent);
    event.actionTime = OH\_Input\_GetMouseEventActionTime(mouseEvent);
    // ...
}

static napi\_value AddMouseEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddMouseEventMonitor(OnMouseEventCallback);
    // ...
}

static napi\_value RemoveMouseEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveMouseEventMonitor(OnMouseEventCallback);
    // ...
}

-   **触摸事件**

struct TouchEvent {
    int32\_t action;
    int32\_t id;
    int32\_t displayX;
    int32\_t displayY;
    int64\_t actionTime { -1 };
};

void OnTouchEventCallback(const Input\_TouchEvent\* touchEvent)
{
    TouchEvent event;
    //Input\_TouchEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    event.action = OH\_Input\_GetTouchEventAction(touchEvent);
    event.id = OH\_Input\_GetTouchEventFingerId(touchEvent);
    event.displayX = OH\_Input\_GetTouchEventDisplayX(touchEvent);
    event.displayY = OH\_Input\_GetTouchEventDisplayY(touchEvent);
    event.actionTime = OH\_Input\_GetTouchEventActionTime(touchEvent);
    // ...
}

static napi\_value AddTouchEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddTouchEventMonitor(OnTouchEventCallback);
    // ...
}

static napi\_value RemoveTouchEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveTouchEventMonitor(OnTouchEventCallback);
    // ...
}

-   **轴事件**

struct AxisEvent {
    int32\_t axisAction;
    float displayX;
    float displayY;
    std::map<int32\_t, double> axisValues;
    int64\_t actionTime { -1 };
    int32\_t sourceType;
    int32\_t axisEventType { -1 };
};

void OnAllAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    //Input\_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    InputEvent\_AxisAction action = static\_cast<InputEvent\_AxisAction>(0);
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType = static\_cast<InputEvent\_SourceType>(0);
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType = static\_cast<InputEvent\_AxisEventType>(-1);
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
    // ...
}

//定义捏合类型轴事件回调函数
void OnPinchAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    //Input\_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    InputEvent\_AxisAction action = static\_cast<InputEvent\_AxisAction>(0);
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType = static\_cast<InputEvent\_SourceType>(0);
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType = static\_cast<InputEvent\_AxisEventType>(-1);
    ret = OH\_Input\_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    double value = 0;
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_PINCH, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_PINCH, value));
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_ROTATE, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_ROTATE, value));
    // ...
}

void OnScrollAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    //Input\_AxisEvent的生命周期仅限于回调函数内，回调函数执行完毕后会被自动销毁
    InputEvent\_AxisAction action = static\_cast<InputEvent\_AxisAction>(0);
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType = static\_cast<InputEvent\_SourceType>(0);
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType = static\_cast<InputEvent\_AxisEventType>(-1);
    ret = OH\_Input\_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    double value = 0;
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_VERTICAL, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_VERTICAL, value));
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_HORIZONTAL, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_HORIZONTAL, value));
    // ...
}

static napi\_value AddAxisEventMonitorForAll(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddAxisEventMonitorForAll(OnAllAxisEventCallback);
    // ...
}

static napi\_value RemoveAxisEventMonitorForAll(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveAxisEventMonitorForAll(OnAllAxisEventCallback);
    // ...
}

static napi\_value AddPinchAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddAxisEventMonitor(AXIS\_EVENT\_TYPE\_PINCH, OnPinchAxisEventCallback);
    // ...
}

static napi\_value RemovePinchAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveAxisEventMonitor(AXIS\_EVENT\_TYPE\_PINCH, OnPinchAxisEventCallback);
    // ...
}

static napi\_value AddScrollAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddAxisEventMonitor(AXIS\_EVENT\_TYPE\_SCROLL, OnScrollAxisEventCallback);
    // ...
}

static napi\_value RemoveScrollAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret =  OH\_Input\_RemoveAxisEventMonitor(AXIS\_EVENT\_TYPE\_SCROLL, OnScrollAxisEventCallback);
    // ...
}
