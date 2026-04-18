---
title: "使用剪贴板进行复制粘贴 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-use-pasteboard"
menu_path:
  - "指南"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "剪贴板服务"
  - "使用剪贴板进行复制粘贴 (C/C++)"
captured_at: "2026-04-17T01:35:55.193Z"
---

# 使用剪贴板进行复制粘贴 (C/C++)

#### 场景介绍

剪贴板为开发者提供数据的复制粘贴能力。支持对纯文本、超文本、URI等内容的操作。

#### 基本概念

-   [**OH\_PasteboardObserver**](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)：剪贴板数据变更观察者对象，用以监听剪贴板数据变更事件。
-   [**OH\_Pasteboard**](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)：剪贴板对象，用来进行查询、写入等操作。
-   [**OH\_UdmfData**](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdata)：统一数据对象。

#### 约束限制

-   剪贴板内容包含剪贴板系统服务元数据和应用设置的数据，总大小上限默认为128MB，PC/2in1设备可通过系统配置修改上限，有效范围为128MB~2GB。
-   为保证剪贴板数据的准确性，同一时间只能支持一个复制操作。
-   当前支持的数据类型：纯文本类型(OH\_UdsPlainText)、超文本标记语言类型(OH\_UdsHtml)、文件Uri类型(OH\_UdsFileUri)、像素图片类型(OH\_UdsPixelMap)、超链接类型(OH\_UdsHyperlink)、桌面图标类型(OH\_UdsAppItem)、自定义类型。ArkTS接口与NDK接口支持数据类型不完全一致，使用时须匹配接口支持类型，详情见[ArkTS接口与NDK接口数据类型对应关系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-pasteboard-to-copy-and-paste#arkts接口与ndk接口数据类型对应关系)。
-   自定义类型数据在复制粘贴时，指定的类型名称不能和已有的类型名称重复。
-   API version 12及之后，系统为提升用户隐私安全保护能力，剪贴板读取接口增加[权限管控](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。
-   API version 12中新增的复制、粘贴接口[setUnifiedData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard#setunifieddata12)/[getUnifiedData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard#getunifieddata12)与本文档中的复制、粘贴接口[OH\_Pasteboard\_SetData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_setdata)/[OH\_Pasteboard\_GetData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_getdata)当前相互独立，进行写入、读取操作时请使用对应配套接口。

#### 接口说明

详细接口见[Pasteboard文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard)。

| 接口名称 | 描述 |
| :-- | :-- |
| OH\_PasteboardObserver\* OH\_PasteboardObserver\_Create() | 创建一个剪贴板数据变更观察者对象。 |
| OH\_PasteboardObserver\_Destroy(OH\_PasteboardObserver\* observer) | 销毁剪贴板数据变更观察者对象。 |
| int OH\_PasteboardObserver\_SetData(OH\_PasteboardObserver\* observer, void\* context, const Pasteboard\_Notify callback, const Pasteboard\_Finalize finalize) | 将剪贴板变更回调函数设置到剪贴板数据变更观察者对象中。 |
| OH\_Pasteboard\* OH\_Pasteboard\_Create() | 创建一个剪贴板实例。 |
| void OH\_Pasteboard\_Destroy(OH\_Pasteboard\* pasteboard) | 销毁剪贴板实例。 |
| int OH\_Pasteboard\_Subscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer) | 订阅剪贴板的数据变更。 |
| int OH\_Pasteboard\_Unsubscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer) | 取消对剪贴板数据变更的订阅。 |
| bool OH\_Pasteboard\_IsRemoteData(OH\_Pasteboard\* pasteboard) | 判断剪贴板中的数据是否来自远端设备。 |
| int OH\_Pasteboard\_GetDataSource(OH\_Pasteboard\* pasteboard, char\* source, unsigned int len) | 获取剪贴板中数据的数据源。 |
| bool OH\_Pasteboard\_HasType(OH\_Pasteboard\* pasteboard, const char\* type) | 判断剪贴板中是否有指定类型的数据。 |
| bool OH\_Pasteboard\_HasData(OH\_Pasteboard\* pasteboard) | 检查剪贴板中是否有数据。 |
| OH\_UdmfData\* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status) | 获取剪贴板中的数据。 |
| int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data) | 向剪贴板中写入数据。 |
| int OH\_Pasteboard\_ClearData(OH\_Pasteboard\* pasteboard) | 清空剪贴板中的数据。 |
| void (\*Pasteboard\_Notify)(void\* context, Pasteboard\_NotifyType type) | 剪贴板中数据变更回调函数。 |
| void (\*Pasteboard\_Finalize)(void\* context) | 剪贴板数据变更观察者对象销毁时，释放context上下文资源。 |

#### 开发步骤

1.  添加动态链接库。
    
    ```cmake
    # CMakeLists.txt中添加以下lib
    libudmf.so
    libpasteboard.so
    ```
    
2.  引用头文件。
    
    #include <cstdio>
    #include <cstring>
    #include <hilog/log.h>
    #include <database/pasteboard/oh\_pasteboard.h>
    #include <database/udmf/udmf.h>
    #include <database/udmf/uds.h>
    
3.  定义剪贴板变化监听的回调函数。
    
    // 定义剪贴板数据内容变更时的通知回调函数
    static void PasteboardNotifyImpl2(void\* context, Pasteboard\_NotifyType type)
    {
        OH\_LOG\_INFO(LOG\_APP, "Pasteboard\_NotifyType, type: %d", type);
    }
    // 定义剪贴板数据变更观察者对象销毁时的通知回调函数
    static void PasteboardFinalizeImpl2(void\* context)
    {
        OH\_LOG\_INFO(LOG\_APP, "callback: Pasteboard\_Finalize");
    }
    
4.  订阅剪贴板变化。
    
    static void PasteboardTestObserver()
    {
        // 1. 创建一个剪贴板实例
        OH\_Pasteboard\* pasteboard = OH\_Pasteboard\_Create();
        // 2. 创建一个剪贴板数据变更观察者实例
        OH\_PasteboardObserver\* observer = OH\_PasteboardObserver\_Create();
        // 3. 将两个回调函数设置到观察者实例
        OH\_PasteboardObserver\_SetData(observer, (void\*)pasteboard, PasteboardNotifyImpl2, PasteboardFinalizeImpl2);
        // 4. 设置对剪贴板本端数据变化的订阅
        OH\_Pasteboard\_Subscribe(pasteboard, NOTIFY\_LOCAL\_DATA\_CHANGE, observer);
    }
    
5.  向剪贴板写入数据。
    
    static napi\_value NAPI\_Pasteboard\_set(napi\_env env, napi\_callback\_info info)
    {
        napi\_value args\[1\];
        size\_t argc = 1;
        napi\_status status = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        char text\[256\];
        size\_t value0Size;
        status = napi\_get\_value\_string\_utf8(env, args\[0\], text, sizeof(text), &value0Size);
    
        // 1. 创建一个剪贴板实例
        OH\_Pasteboard\* pasteboard = OH\_Pasteboard\_Create();
        if (pasteboard == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "Failed to create pasteboard instance.");
        };
        // 2. 创建OH\_UdmfRecord对象，并向OH\_UdmfRecord中添加文本类型数据
        OH\_UdsPlainText\* udsPlainText = OH\_UdsPlainText\_Create();
        OH\_UdsPlainText\_SetContent(udsPlainText, text);
        OH\_UdsHtml\* udsHtml = OH\_UdsHtml\_Create();
        OH\_UdsHtml\_SetContent(udsHtml, "hello world");
        OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
        OH\_UdmfRecord\_AddPlainText(record, udsPlainText);
        OH\_UdmfRecord\_AddHtml(record, udsHtml);
        // 3. 创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord
        OH\_UdmfData\* data = OH\_UdmfData\_Create();
        OH\_UdmfData\_AddRecord(data, record);
        // 4. 将数据写入剪贴板
        OH\_Pasteboard\_SetData(pasteboard, data);
        // 5. 使用完销毁指针
        OH\_UdsPlainText\_Destroy(udsPlainText);
        OH\_UdsHtml\_Destroy(udsHtml);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_Pasteboard\_Destroy(pasteboard);
        // ...
    }
    
6.  从剪贴板读取数据。
    
    static napi\_value NAPI\_Pasteboard\_get(napi\_env env, napi\_callback\_info info)
    {
        // 1. 创建一个剪贴板实例
        OH\_Pasteboard\* pasteboard = OH\_Pasteboard\_Create();
        if (pasteboard == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "Failed to create pasteboard instance.");
        };
        // 2. 判断剪贴板中是否有文本类型数据
        bool hasPlainTextData = OH\_Pasteboard\_HasType(pasteboard, "text/plain");
        if (hasPlainTextData) {
            // 3. 从剪贴板中获取统一类型数据OH\_UdmfData
            int ret = 0;
            OH\_UdmfData\* udmfData = OH\_Pasteboard\_GetData(pasteboard, &ret);
            if (udmfData == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to get data from pasteboard.");
            };
            // 4. 从OH\_UdmfData中获取第一个数据记录
            OH\_UdmfRecord\* record = OH\_UdmfData\_GetRecord(udmfData, 0);
            if (record == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to get record from udmfData.");
            };
            // 5. 从数据记录中获取文本数据内容
            OH\_UdsPlainText\* plainText = OH\_UdsPlainText\_Create();
            if (plainText == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to create plain text object.");
            };
            OH\_UdmfRecord\_GetPlainText(record, plainText);
            const char\* content = OH\_UdsPlainText\_GetContent(plainText);
            if (content == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to get content from plain text.");
            }
            napi\_value result;
            napi\_create\_string\_utf8(env, content, strlen(content), &result);
            // 6. 使用完销毁指针
            OH\_UdsPlainText\_Destroy(plainText);
            OH\_UdmfRecord\_Destroy(record);
            return result;
        } else {
            OH\_LOG\_INFO(LOG\_APP, "No plain text data in pasteboard.");
        }
        OH\_Pasteboard\_Destroy(pasteboard);
    }
