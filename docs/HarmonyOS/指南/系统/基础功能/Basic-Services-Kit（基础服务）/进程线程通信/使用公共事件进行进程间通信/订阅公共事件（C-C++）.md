---
title: "订阅公共事件（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-subscription"
menu_path:
  - "指南"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "进程线程通信"
  - "使用公共事件进行进程间通信"
  - "订阅公共事件（C/C++）"
captured_at: "2026-04-17T01:35:54.836Z"
---

# 订阅公共事件（C/C++）

#### 场景介绍

通过[OH\_CommonEvent\_CreateSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createsubscriber)创建的订阅者可以对某个公共事件进行订阅，如果有订阅的事件发布那么订阅了这个事件的订阅者将会收到该事件及其传递的参数，也可以通过订阅者对象进一步处理有序公共事件。

#### 接口说明

详细的API说明请参考[oh\_commonevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h)。

| 接口名 | 描述 |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo\* OH\_CommonEvent\_CreateSubscribeInfo(const char\* events\[\], int32\_t eventsNum)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createsubscribeinfo) | 创建订阅者信息。 |
| [void OH\_CommonEvent\_DestroySubscribeInfo(CommonEvent\_SubscribeInfo\* info)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_destroysubscribeinfo) | 销毁订阅者信息。 |
| [CommonEvent\_Subscriber\* OH\_CommonEvent\_CreateSubscriber(const CommonEvent\_SubscribeInfo\* info, CommonEvent\_ReceiveCallback callback)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createsubscriber) | 创建订阅者。 |
| [void OH\_CommonEvent\_DestroySubscriber(CommonEvent\_Subscriber\* subscriber)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_destroysubscriber) | 销毁订阅者。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Subscribe(const CommonEvent\_Subscriber\* subscriber)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_subscribe) | 订阅事件。 |
| [bool OH\_CommonEvent\_AbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_abortcommonevent) | 中止当前的有序公共事件。 |
| [bool OH\_CommonEvent\_ClearAbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_clearabortcommonevent) | 取消当前有序公共事件的中止状态。 |
| [bool OH\_CommonEvent\_FinishCommonEvent(CommonEvent\_Subscriber\* subscriber)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_finishcommonevent) | 结束对当前有序公共事件的处理。 |

#### 开发步骤

1.  引用头文件。
    
    #include <cstdint>
    #include <cstring>
    #include "hilog/log.h"
    #include "BasicServicesKit/oh\_commonevent.h"
    
2.  在CMake脚本中添加动态链接库。
    
    ```txt
    target_link_libraries(entry PUBLIC
        libace_napi.z.so
        libhilog_ndk.z.so
        libohcommonevent.so
    )
    ```
    
3.  创建订阅者信息。
    
    通过[OH\_CommonEvent\_CreateSubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createsubscribeinfo)创建订阅者信息。
    
    CommonEvent\_SubscribeInfo \*CreateSubscribeInfo(const char \*events\[\], int32\_t eventsNum, const char \*permission,
                                                   const char \*bundleName)
    {
        int32\_t ret = -1;
        // 创建订阅者信息
        CommonEvent\_SubscribeInfo \*info = OH\_CommonEvent\_CreateSubscribeInfo(events, eventsNum);
    
        // 设置发布者权限
        ret = OH\_CommonEvent\_SetPublisherPermission(info, permission);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetPublisherPermission ret <%{public}d>.", ret);
    
        // 设置发布者包名称
        ret = OH\_CommonEvent\_SetPublisherBundleName(info, bundleName);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetPublisherBundleName ret <%{public}d>.", ret);
        return info;
    }
    
    // 销毁订阅者信息
    void DestroySubscribeInfo(CommonEvent\_SubscribeInfo \*info)
    {
        OH\_CommonEvent\_DestroySubscribeInfo(info);
        info = nullptr;
    }
    
4.  创建订阅者。
    
    创建订阅者时需传入公共事件的回调函数[CommonEvent\_ReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_receivecallback)。待事件发布时，订阅者会接收到回调数据[CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#结构体)。
    
    // 公共事件回调函数
    void OnReceive(const CommonEvent\_RcvData \*data)
    {
        // 获取回调公共事件名称
        const char \*event = OH\_CommonEvent\_GetEventFromRcvData(data);
    
        // 获取回调公共事件结果代码
        int code = OH\_CommonEvent\_GetCodeFromRcvData(data);
    
        // 获取回调公共事件自定义结果数据
        const char \*retData = OH\_CommonEvent\_GetDataStrFromRcvData(data);
    
        // 获取回调公共事件包名称
        const char \*bundle = OH\_CommonEvent\_GetBundleNameFromRcvData(data);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST",
                     "event: %{public}s, code: %{public}d, data: %{public}s, bundle: %{public}s", event, code, retData,
                     bundle);
    }
    
    通过[CommonEvent\_Parameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#变量)传入key来获取附加信息内容。
    
    void GetParameters(const CommonEvent\_RcvData \*data)
    {
        // 获取回调公共事件附件信息
        bool exists = false;
        const CommonEvent\_Parameters \*parameters = OH\_CommonEvent\_GetParametersFromRcvData(data);
    
        // 检查公共事件附加信息中是否包含某个键值对信息
        exists = OH\_CommonEvent\_HasKeyInParameters(parameters, "intKey");
        // 获取公共事件附加信息中int数据信息
        int intValue = OH\_CommonEvent\_GetIntFromParameters(parameters, "intKey", 10);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "exists = %{public}d, intValue = %{public}d", exists, intValue);
    
        // 补充说明：除int类型外，还支持获取以下多种类型的公共事件附加信息，调用对应鸿蒙API即可：
        // - 基础数据类型：bool（OH\_CommonEvent\_GetBoolFromParameters）、long（OH\_CommonEvent\_GetLongFromParameters）、
        // double（OH\_CommonEvent\_GetDoubleFromParameters）、char（OH\_CommonEvent\_GetCharFromParameters）
        // -
        // 数组数据类型：int数组（OH\_CommonEvent\_GetIntArrayFromParameters）、long数组（OH\_CommonEvent\_GetLongArrayFromParameters）、
        // double数组（OH\_CommonEvent\_GetDoubleArrayFromParameters）、char数组（OH\_CommonEvent\_GetCharArrayFromParameters）、
        // bool数组（OH\_CommonEvent\_GetBoolArrayFromParameters）
        // 所有类型均支持通过OH\_CommonEvent\_HasKeyInParameters先校验键是否存在，避免获取失败
    }
    
    通过[OH\_CommonEvent\_CreateSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createsubscriber)创建订阅者，传入订阅者信息[CommonEvent\_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#结构体)和步骤4公共事件回调函数OnReceive。
    
    // 创建订阅者
    CommonEvent\_Subscriber \*CreateSubscriber(CommonEvent\_SubscribeInfo \*info)
    {
        return OH\_CommonEvent\_CreateSubscriber(info, OnReceive);
    }
    
    // 销毁订阅者
    void DestroySubscriber(CommonEvent\_Subscriber \*Subscriber)
    {
        OH\_CommonEvent\_DestroySubscriber(Subscriber);
        Subscriber = nullptr;
    }
    
5.  订阅事件。
    
    通过[OH\_CommonEvent\_Subscribe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_subscribe)订阅事件。
    
    void Subscribe(CommonEvent\_Subscriber \*subscriber)
    {
        // 通过传入订阅者来订阅事件
        int32\_t ret = OH\_CommonEvent\_Subscribe(subscriber);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_Subscribe ret <%{public}d>.", ret);
    }
    
6.  （可选）当订阅的事件为有序公共事件时，可以选择进一步处理有序公共事件。
    
    根据订阅者设置的优先级等级，优先将公共事件发送给优先级较高的订阅者，等待其成功接收该公共事件之后再将事件发送给优先级较低的订阅者。如果有多个订阅者具有相同的优先级，则他们将随机接收到公共事件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/gpqWOXcfS02Jdohgt5yr_g/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=77E96F5639F763E0BAC9DC68F700F0BA574D5DCE6B30EB2022AA2D9EEA1268A7)
    
    在订阅者收到公共事件之后，才能通过以下接口进一步处理有序公共事件。
    
    -   中止当前的有序公共事件。
        
        通过[OH\_CommonEvent\_AbortCommonEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_abortcommonevent)与[OH\_CommonEvent\_FinishCommonEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。
        
        void AbortCommonEvent(CommonEvent\_Subscriber \*subscriber)
        {
            // 判断是否为有序公共事件
            if (!OH\_CommonEvent\_IsOrderedCommonEvent(subscriber)) {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "Not ordered common event.");
                return;
            }
            // 中止有序事件
            if (OH\_CommonEvent\_AbortCommonEvent(subscriber)) {
                if (OH\_CommonEvent\_FinishCommonEvent(subscriber)) {
                    // 获取当前有序公共事件是否处于中止状态
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "Abort common event success, Get abort <%{public}d>.",
                                 OH\_CommonEvent\_GetAbortCommonEvent(subscriber));
                }
            } else {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 1, "CES\_TEST", "Abort common event failed.");
            }
        }
        
    -   取消当前有序公共事件的中止状态。
        
        通过[OH\_CommonEvent\_ClearAbortCommonEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_clearabortcommonevent)与[OH\_CommonEvent\_FinishCommonEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。
        
        void ClearAbortCommonEvent(CommonEvent\_Subscriber \*subscriber)
        {
            // 判断是否为有序公共事件
            if (!OH\_CommonEvent\_IsOrderedCommonEvent(subscriber)) {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "Not ordered common event.");
                return;
            }
            // 中止有序事件
            if (!OH\_CommonEvent\_AbortCommonEvent(subscriber)) {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 1, "CES\_TEST", "Abort common event failed.");
                return;
            }
            // 取消中止有序事件
            if (OH\_CommonEvent\_ClearAbortCommonEvent(subscriber)) {
                if (OH\_CommonEvent\_FinishCommonEvent(subscriber)) {
                    // 获取当前有序公共事件是否处于中止状态
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "Clear abort common event success, Get abort <%{public}d>.",
                                 OH\_CommonEvent\_GetAbortCommonEvent(subscriber));
                }
            } else {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 1, "CES\_TEST", "Clear abort common event failed.");
            }
        }
        
    -   修改有序公共事件的内容。
        
        通过[OH\_CommonEvent\_SetCodeToSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_setcodetosubscriber)与[OH\_CommonEvent\_SetDataToSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_setdatatosubscriber)设置有序公共事件的代码和数据。
        
        void SetToSubscriber(CommonEvent\_Subscriber \*subscriber, const int32\_t code, const char \*data)
        {
            // 设置有序公共事件的代码
            if (!OH\_CommonEvent\_SetCodeToSubscriber(subscriber, code)) {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 1, "CES\_TEST", "OH\_CommonEvent\_SetCodeToSubscriber failed.");
                return;
            }
            // 设置有序公共事件的数据
            size\_t dataLength = strlen(data);
            if (!OH\_CommonEvent\_SetDataToSubscriber(subscriber, data, dataLength)) {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 1, "CES\_TEST", "OH\_CommonEvent\_SetDataToSubscriber failed.");
                return;
            }
        }
        
        void GetFromSubscriber(CommonEvent\_Subscriber \*subscriber)
        {
            // 获取有序公共事件的数据和代码
            const char \*data = OH\_CommonEvent\_GetDataFromSubscriber(subscriber);
            int32\_t code = OH\_CommonEvent\_GetCodeFromSubscriber(subscriber);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "Subscriber data <%{public}s>, code <%{public}d>.", data, code);
        }
