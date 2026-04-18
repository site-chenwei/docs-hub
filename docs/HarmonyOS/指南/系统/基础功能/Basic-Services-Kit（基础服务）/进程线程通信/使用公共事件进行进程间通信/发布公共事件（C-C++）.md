---
title: "发布公共事件（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-publish"
menu_path:
  - "指南"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "进程线程通信"
  - "使用公共事件进行进程间通信"
  - "发布公共事件（C/C++）"
captured_at: "2026-04-17T01:35:54.854Z"
---

# 发布公共事件（C/C++）

#### 场景介绍

当需要发布某个公共事件时，可以通过[OH\_CommonEvent\_Publish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_publish)和[OH\_CommonEvent\_PublishWithInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_publishwithinfo)方法发布事件。发布的公共事件可以携带数据，供订阅者解析并进行下一步处理。

#### 接口说明

详细的API说明请参考[oh\_commonevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h)。

| 接口名 | 描述 |
| :-- | :-- |
| [struct CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo) | 发布公共事件时使用的公共事件属性对象。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Publish(const char\* event)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_publish) | 发布公共事件。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_PublishWithInfo(const char\* event, const CommonEvent\_PublishInfo\* info)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_publishwithinfo) | 发布带有指定属性的公共事件。 |
| [CommonEvent\_PublishInfo\* OH\_CommonEvent\_CreatePublishInfo(bool ordered)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createpublishinfo) | 创建公共事件属性对象。 |
| [void OH\_CommonEvent\_DestroyPublishInfo(CommonEvent\_PublishInfo\* info)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_destroypublishinfo) | 销毁公共事件属性对象。 |
| [CommonEvent\_Parameters\* OH\_CommonEvent\_CreateParameters()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createparameters) | 创建公共事件附加信息对象。 |
| [void OH\_CommonEvent\_DestroyParameters(CommonEvent\_Parameters\* param)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_destroyparameters) | 销毁公共事件附加信息对象。 |

#### 开发步骤

1.  引用头文件。
    
    #include <cstdint>
    #include <cstring>
    #include "hilog/log.h"
    #include "BasicServicesKit/oh\_commonevent.h"
    
    const long PARAM\_LONG\_VALUE1 = 2147483646;
    const long PARAM\_LONG\_VALUE2 = 2147483645;
    const long PARAM\_LONG\_VALUE3 = 555;
    const double PARAM\_DOUBLE\_VALUE1 = 11.22;
    const double PARAM\_DOUBLE\_VALUE2 = 33.44;
    const double PARAM\_DOUBLE\_VALUE3 = 55.66;
    const int PARAM\_INT\_VALUE1 = 10;
    const int PARAM\_INT\_VALUE2 = 123;
    const int PARAM\_INT\_VALUE3 = 234;
    const int PARAM\_INT\_VALUE4 = 567;
    
2.  在CMake脚本中添加动态链接库。
    
    ```txt
    target_link_libraries(entry PUBLIC
        libace_napi.z.so
        libhilog_ndk.z.so
        libohcommonevent.so
    )
    ```
    
3.  （可选）创建公共事件属性对象。
    
    发布携带数据的公共事件时，需要通过[OH\_CommonEvent\_CreatePublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createpublishinfo)创建公共事件属性对象，并通过以下接口设置公共事件属性。
    
    // 创建并添加公共事件属性附加信息
    CommonEvent\_Parameters \*CreateParameters()
    {
        int32\_t ret = -1;
        // 创建公共事件附加信息
        CommonEvent\_Parameters \*param = OH\_CommonEvent\_CreateParameters();
    
        // 设置int类型附加信息和key
        ret = OH\_CommonEvent\_SetIntToParameters(param, "intKey", PARAM\_INT\_VALUE1);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetIntToParameters ret <%{public}d>.", ret);
    
        // 设置int数组类型附加信息和key
        int intArray\[\] = {PARAM\_INT\_VALUE2, PARAM\_INT\_VALUE3, PARAM\_INT\_VALUE4};
        size\_t arraySize = sizeof(intArray) / sizeof(intArray\[0\]);
        ret = OH\_CommonEvent\_SetIntArrayToParameters(param, "intArrayKey", intArray, arraySize);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetIntArrayToParameters ret <%{public}d>.", ret);
    
        // 设置long类型附加信息和key
        ret = OH\_CommonEvent\_SetLongToParameters(param, "longKey", PARAM\_LONG\_VALUE1);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetLongToParameters ret <%{public}d>.", ret);
    
        // 设置long数组类型附加信息和key
        long longArray\[\] = {PARAM\_LONG\_VALUE1, PARAM\_LONG\_VALUE3, PARAM\_LONG\_VALUE2};
        ret = OH\_CommonEvent\_SetLongArrayToParameters(param, "longArrayKey", longArray, arraySize);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetLongArrayToParameters ret <%{public}d>.", ret);
    
        // 设置double类型附加信息和key
        ret = OH\_CommonEvent\_SetDoubleToParameters(param, "doubleKey", PARAM\_DOUBLE\_VALUE1);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetDoubleToParameters ret <%{public}d>.", ret);
    
        // 设置double数组类型附加信息和key
        double doubleArray\[\] = {PARAM\_DOUBLE\_VALUE1, PARAM\_DOUBLE\_VALUE2, PARAM\_DOUBLE\_VALUE3};
        ret = OH\_CommonEvent\_SetDoubleArrayToParameters(param, "doubleArrayKey", doubleArray, arraySize);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetDoubleArrayToParameters ret <%{public}d>.", ret);
    
        // 设置boolean类型附加信息和key
        ret = OH\_CommonEvent\_SetBoolToParameters(param, "boolKey", true);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetBoolToParameters ret <%{public}d>.", ret);
    
        // 设置boolean数组类型附加信息和key
        bool boolArray\[\] = {true, false, true};
        ret = OH\_CommonEvent\_SetBoolArrayToParameters(param, "boolArrayKey", boolArray, arraySize);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetBoolArrayToParameters ret <%{public}d>.", ret);
    
        // 设置char类型附加信息和key
        ret = OH\_CommonEvent\_SetCharToParameters(param, "charKey", 'A');
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetCharToParameters ret <%{public}d>.", ret);
    
        // 设置char数组类型附加信息和key
        const char \*value = "Char Array";
        size\_t valueLength = strlen(value);
        ret = OH\_CommonEvent\_SetCharArrayToParameters(param, "charArrayKey", value, valueLength);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetCharArrayToParameters ret <%{public}d>.", ret);
        return param;
    }
    
    // 设置公共事件属性
    void SetPublishInfo(const char \*bundleName, const char \*permissions\[\], int32\_t num, const int32\_t code,
                        const char \*data)
    {
        int32\_t ret = -1;
        // 创建publishInfo，设置是否为有序公共事件，取值为true，表示有序公共事件；取值为false，表示无序公共事件
        CommonEvent\_PublishInfo \*info = OH\_CommonEvent\_CreatePublishInfo(true);
    
        // 设置公共事件包名称
        ret = OH\_CommonEvent\_SetPublishInfoBundleName(info, bundleName);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetPublishInfoBundleName ret <%{public}d>.", ret);
    
        // 设置公共事件权限，参数为权限数组和权限的数量
        ret = OH\_CommonEvent\_SetPublishInfoPermissions(info, permissions, num);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetPublishInfoPermissions ret <%{public}d>.", ret);
    
        // 设置公共事件结果码
        ret = OH\_CommonEvent\_SetPublishInfoCode(info, code);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetPublishInfoCode ret <%{public}d>.", ret);
    
        // 设置公共事件结果数据
        size\_t dataLength = strlen(data);
        ret = OH\_CommonEvent\_SetPublishInfoData(info, data, dataLength);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetPublishInfoData ret <%{public}d>.", ret);
    
        // 设置公共事件附加信息
        CommonEvent\_Parameters \*param = CreateParameters();
        ret = OH\_CommonEvent\_SetPublishInfoParameters(info, param);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_SetPublishInfoParameters ret <%{public}d>.", ret);
    }
    
4.  发布公共事件。
    
    -   通过[OH\_CommonEvent\_Publish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_publish)发布不携带信息的公共事件。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/L_zHfLJoTiC6Zwe_8oCyKQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=4CE43EEADAD62DCD3F0ACC40D113DADA7230FD4CFDEEE8CBAB60437CE061E2FA)
        
        不携带信息的公共事件，只能发布为无序公共事件。
        
        void Publish(const char \*event)
        {
            int32\_t ret = OH\_CommonEvent\_Publish(event);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_Publish ret <%{public}d>.", ret);
        }
        
    -   通过[OH\_CommonEvent\_PublishWithInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_publishwithinfo)发布携带信息的公共事件。
        
        void PublishWithInfo(const char \*event, CommonEvent\_PublishInfo \*info)
        {
            // 创建时带入公共事件属性对象
            int32\_t ret = OH\_CommonEvent\_PublishWithInfo(event, info);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 1, "CES\_TEST", "OH\_CommonEvent\_PublishWithInfo ret <%{public}d>.", ret);
        }
        
5.  销毁公共事件对象。
    
    如果后续无需使用已创建的公共事件对象来发布公共事件，需要先通过[OH\_CommonEvent\_DestroyParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_destroyparameters)销毁CommonEvent\_Parameters对象，然后再通过[OH\_CommonEvent\_DestroyPublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_destroypublishinfo)销毁公共事件对象。
    
    void DestroyPublishInfo(CommonEvent\_Parameters \*param, CommonEvent\_PublishInfo \*info)
    {
        // 先销毁Parameters
        OH\_CommonEvent\_DestroyParameters(param);
        param = nullptr;
        // 销毁PublishInfo
        OH\_CommonEvent\_DestroyPublishInfo(info);
        info = nullptr;
    }
