---
title: "取消订阅公共事件（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-unsubscription"
menu_path:
  - "指南"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "进程线程通信"
  - "使用公共事件进行进程间通信"
  - "取消订阅公共事件（C/C++）"
captured_at: "2026-04-17T01:35:54.850Z"
---

# 取消订阅公共事件（C/C++）

#### 场景介绍

订阅者在完成业务需求之后，需要取消订阅公共事件。

#### 接口说明

详细的API说明请参考[oh\_commonevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h)。

| 接口名 | 描述 |
| :-- | :-- |
| [CommonEvent\_ErrCode OH\_CommonEvent\_UnSubscribe(const CommonEvent\_Subscriber\* subscriber)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_unsubscribe) | 取消订阅公共事件。 |

#### 开发步骤

1.  引用头文件。
    
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
    
3.  取消订阅公共事件。
    
    订阅者订阅公共事件并完成业务需求后，可以通过[OH\_CommonEvent\_UnSubscribe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_unsubscribe)主动取消订阅事件。
    
    void Unsubscribe(CommonEvent\_Subscriber \*subscriber)
    {
        // 通过传入订阅者来退订事件
        int32\_t ret = OH\_CommonEvent\_UnSubscribe(subscriber);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_UnSubscribe ret <%{public}d>.", ret);
    }
