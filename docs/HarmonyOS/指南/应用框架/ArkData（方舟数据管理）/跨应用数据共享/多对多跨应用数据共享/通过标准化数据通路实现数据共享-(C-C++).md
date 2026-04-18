---
title: "通过标准化数据通路实现数据共享 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unified-data-channels-c"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "跨应用数据共享"
  - "多对多跨应用数据共享"
  - "通过标准化数据通路实现数据共享 (C/C++)"
captured_at: "2026-04-17T01:35:33.911Z"
---

# 通过标准化数据通路实现数据共享 (C/C++)

#### 场景介绍

在多对多跨应用数据共享的场景下，需要提供一条数据通路，能够写入多个不同应用的数据，并共享给其他应用进行读取。

UDMF针对多对多跨应用数据共享的不同业务场景，提供了标准化的数据通路和数据写入与读取接口。

#### 标准化数据通路的定义和实现

标准化数据通路是为各种业务场景提供的跨应用数据写入与读取通路。它能够暂存应用需要共享的、符合标准化数据定义的统一数据对象，并提供给其他应用访问。同时，它按照一定策略对暂存数据的修改、删除权限及生命周期进行管理。

标准化数据通路通过UDMF提供的系统服务实现。应用（数据提供方）需要共享公共数据时，可以通过UDMF提供的插入接口将数据写入UDMF的数据通路中，并且可以通过UDMF提供的更新和删除接口对已存入的数据进行更新和删除操作。目标应用（数据访问方）可以通过UDMF提供的读取接口访问数据。

标准化数据通路相关接口应不推荐多线程调用。

统一数据对象UnifiedData在UDMF数据通路中具有全局唯一URI标识，其定义为udmf://intention/bundleName/groupId，其中各组成部分的含义分别为：

-   **udmf:** 协议名，表示使用UDMF提供的数据通路。
    
-   **intention:** UDMF已经支持的数据通路类型枚举值，对应不同的业务场景。
    
-   **bundleName:** 数据来源应用的包名称。
    
-   **groupId:** 分组名称，支持批量数据分组管理。
    

当前UDMF中的跨应用数据共享通路有：**公共数据通路**

**公共数据通路**：应用共享的公用数据通路，所有应用均可向通路中写入数据。写入方可以根据写入数据时生成的数据唯一标识符进行数据的更新、删除、查询指定数据标识符或全量查询。数据读取方可以通过唯一标识符读取指定数据，也可以设置Intention枚举类型为DATA\_HUB来读取当前数据通路中的全量数据。公共数据通路仅用于传输应用间的过程数据，不能用于传输沙箱目录下文件等有权限管控的数据。UDMF会统一对数据的生命周期进行管理，每小时定期清理存入时长超过一小时的数据。

#### 接口说明

详细的接口说明请参考[UDMF接口文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-h)。

| 接口名称 | 描述 |
| :-- | :-- |
| OH\_UdsHyperlink\* OH\_UdsHyperlink\_Create() | 创建超链接类型对象的指针。 |
| int OH\_UdsHyperlink\_SetDescription(OH\_UdsHyperlink\* pThis, const char\* description) | 设置超链接类型实例中的描述参数。 |
| OH\_UdmfRecord\* OH\_UdmfRecord\_Create() | 创建一个指向统一数据记录OH\_UdmfRecord的指针。 |
| int OH\_UdmfRecord\_AddHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink) | 向OH\_UdmfRecord添加超链接类型数据。 |
| OH\_UdmfData\* OH\_UdmfData\_Create() | 创建一个指向统一数据对象OH\_UdmfData的指针。 |
| int OH\_UdmfData\_AddRecord(OH\_UdmfData\* pThis, OH\_UdmfRecord\* record) | 向OH\_UdmfData中增加一条OH\_UdmfRecord数据记录。 |
| int OH\_Udmf\_SetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData \*unifiedData, char \*key, unsigned int keyLen) | 从统一数据管理框架数据库中写入统一数据对象OH\_UdmfData数据。 |
| void OH\_UdsHyperlink\_Destroy(OH\_UdsHyperlink\* pThis) | 销毁超链接类型指针指向的实例对象。 |
| void OH\_UdmfRecord\_Destroy(OH\_UdmfRecord\* pThis) | 销毁指向统一数据记录OH\_UdmfRecord的指针。 |
| void OH\_UdmfData\_Destroy(OH\_UdmfData\* pThis) | 销毁指向统一数据对象OH\_UdmfData的指针。 |
| char\*\* OH\_UdmfRecord\_GetTypes(OH\_UdmfRecord\* pThis, unsigned int\* count) | 获取OH\_UdmfRecord中全部的数据类型。 |
| int OH\_UdmfRecord\_GetHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink) | 获取OH\_UdmfRecord中超链接类型数据。 |
| int OH\_Udmf\_GetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize) | 通过数据通路类型从统一数据管理框架数据库中获取统一数据对象数据。 |
| int OH\_Udmf\_UpdateUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\* unifiedData) | 对统一数据管理框架数据库中的统一数据对象数据进行数据更改。 |
| int OH\_Udmf\_DeleteUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize) | 删除统一数据管理框架数据库中的统一数据对象数据。 |
| bool OH\_UdmfData\_HasType(OH\_UdmfData\* pThis, const char\* type) | 判断统一数据对象OH\_UdmfData是否存在指定类型。 |
| OH\_UdmfRecord\*\* OH\_UdmfData\_GetRecords(OH\_UdmfData\* pThis, unsigned int\* count) | 获取OH\_UdmfData中全部的数据记录。 |
| OH\_UdmfRecordProvider\* OH\_UdmfRecordProvider\_Create() | 创建一个指向统一数据提供者的指针。 |
| int OH\_UdmfRecordProvider\_SetData(OH\_UdmfRecordProvider\* provider, void\* context, const OH\_UdmfRecordProvider\_GetData callback, const UdmfData\_Finalize finalize) | 设置统一数据提供者的回调函数。 |
| int OH\_UdmfRecord\_SetProvider(OH\_UdmfRecord\* pThis, const char\* const\* types, unsigned int count, OH\_UdmfRecordProvider\* provider) | 将统一数据提供者配置到OH\_UdmfRecord中。 |
| OH\_UdmfOptions\* OH\_UdmfOptions\_Create() | 创建一个指向数据操作选项的指针。 |
| void OH\_UdmfOptions\_Destroy(OH\_UdmfOptions\* pThis) | 销毁指向数据操作选项的指针。 |

#### 添加动态链接库

CMakeLists.txt中添加以下库。

```txt
libudmf.so, libhilog_ndk.z.so
```

#### 引用头文件

#include <cstdio>
#include <cstring>
#include <database/udmf/utd.h>
#include <database/udmf/uds.h>
#include <database/udmf/udmf.h>
#include <database/udmf/udmf\_meta.h>
#include <database/udmf/udmf\_err\_code.h>
#include <hilog/log.h>

#undef LOG\_TAG
#define LOG\_TAG "MY\_LOG"

#### 使用UDMF写入UDS数据

下面以写入超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1.  创建hyperlink的UDS数据结构。
2.  设置hyperlink中的URL和描述信息。
3.  创建OH\_UdmfRecord对象，并向OH\_UdmfRecord中添加超链接类型数据。
4.  创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord。
5.  构建数据操作选项。
6.  构建数据，将数据写入数据库中，得到返回的key值。
7.  使用完成后销毁指针。

int32\_t SetHyperlinkData(OH\_UdsHyperlink\* hyperlink, OH\_UdmfRecord\* record, OH\_UdmfData\* data)
{
    // 2.设置hyperlink中的URL和描述信息。
    int ret = OH\_UdsHyperlink\_SetUrl(hyperlink, "www.demo.com");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set url error!");
        return ret;
    }
    ret = OH\_UdsHyperlink\_SetDescription(hyperlink, "This is the description.");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set description error!");
        return ret;
    }
    // 3. 向OH\_UdmfRecord中添加超链接类型数据。
    ret = OH\_UdmfRecord\_AddHyperlink(record, hyperlink);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add hyperlink to record error!");
        return ret;
    }
    // 4. 并向OH\_UdmfData中添加OH\_UdmfRecord。
    ret = OH\_UdmfData\_AddRecord(data, record);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add record to data error!");
        return ret;
    }
    return UDMF\_E\_OK;
}

int32\_t CreateDataTest()
{
    // 1.创建hyperlink的UDS数据结构、OH\_UdmfRecord对象及OH\_UdmfData对象。
    OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
    OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
    OH\_UdmfData\* data = OH\_UdmfData\_Create();
    int32\_t ret = SetHyperlinkData(hyperlink, record, data);
    if (ret != UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Create data error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        return ret;
    }
    // 构建数据操作选项。
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 6. 构建数据，将数据写入数据库中，得到返回的key值。
    char key\[UDMF\_KEY\_BUFFER\_LEN\] = {0};
    ret = OH\_Udmf\_SetUnifiedDataByOptions(options, data, key, sizeof(key));
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set data error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_LOG\_INFO(LOG\_APP, "key = %{public}s", key);
    // 7. 使用完成后销毁指针。
    OH\_UdsHyperlink\_Destroy(hyperlink);
    OH\_UdmfRecord\_Destroy(record);
    OH\_UdmfData\_Destroy(data);
    OH\_UdmfOptions\_Destroy(options);
    return UDMF\_E\_OK;
}

#### 使用UDMF获取UDS数据

下面继续以获取超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1.  构建数据操作选项。
2.  通过数据操作选项获取数据。
3.  判断OH\_UdmfData是否有对应的类型。
4.  获取数据记录和hyperlink数据。
5.  销毁指针。

int32\_t ProcessHyperlinks(OH\_UdmfRecord\* record, unsigned int recordTypeIdCount, char\*\* typeIdsFromRecord)
{
    for (unsigned int k = 0; k < recordTypeIdCount; k++) {
         // 从OH\_UdmfRecord中获取超链接类型数据。
        if (strcmp(typeIdsFromRecord\[k\], UDMF\_META\_HYPERLINK) == 0) {
             // 创建hyperlink的UDS，用来承载record中读取出来的hyperlink数据。
            OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
            int32\_t ret = OH\_UdmfRecord\_GetHyperlink(record, hyperlink);
            if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "Fail get hyperlink from record!");
                return ret;
            }
            // 读取OH\_UdsHyperlink中的各项信息。
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink type id is : %{public}s", OH\_UdsHyperlink\_GetType(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink url is : %{public}s", OH\_UdsHyperlink\_GetUrl(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink description is : %{public}s",
                OH\_UdsHyperlink\_GetDescription(hyperlink));
            OH\_UdsHyperlink\_Destroy(hyperlink);
        }
    }
    return UDMF\_E\_OK;
}

int32\_t ProcessData(OH\_UdmfData\* data)
{
    unsigned int recordsCount = 0;
    OH\_UdmfRecord\*\* records = OH\_UdmfData\_GetRecords(data, &recordsCount);
    OH\_LOG\_INFO(LOG\_APP, "the count of records count is %{public}u", recordsCount);
    for (unsigned int j = 0; j < recordsCount; j++) {
        // 获取OH\_UdmfRecord类型列表。
        unsigned int recordTypeIdCount = 0;
        char\*\* typeIdsFromRecord = OH\_UdmfRecord\_GetTypes(records\[j\], &recordTypeIdCount);
        int32\_t ret = ProcessHyperlinks(records\[j\], recordTypeIdCount, typeIdsFromRecord);
        if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "ProcessRecordHyperlinks error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t HandleUdmfHyperlinkData(OH\_UdmfData\* readData, unsigned int dataSize, OH\_UdmfData\*\* dataArray)
{
    for (unsigned int i = 0; i < dataSize; i++) {
        OH\_UdmfData\* data = OH\_UDMF\_GetDataElementAt(dataArray, i);
         // 3. 判断OH\_UdmfData是否有对应的类型。
        if (!OH\_UdmfData\_HasType(data, UDMF\_META\_HYPERLINK)) {
            OH\_LOG\_INFO(LOG\_APP, "There is no hyperlink type in data\[%{public}u\].", i);
            continue;
        }
        // 4. 获取数据记录和hyperlink数据。
        int32\_t ret = ProcessData(data);
        if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Process data error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t GetDataTest()
{
    // 1. 构建数据操作选项。
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    int32\_t ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 2. 通过数据操作选项获取数据。
    unsigned int dataSize = 0;
    OH\_UdmfData\* readData = nullptr;
    ret = OH\_Udmf\_GetUnifiedDataByOptions(options, &readData, &dataSize);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Get Data error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_UdmfOptions\_Destroy(options);
    OH\_LOG\_INFO(LOG\_APP, "the size of data is %{public}u", dataSize);
    OH\_UdmfData\*\* dataArray = &readData;
    ret = HandleUdmfHyperlinkData(readData, dataSize, dataArray);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Get Data error!");
        return ret;
    }
    // 5.销毁指针。
    OH\_Udmf\_DestroyDataArray(dataArray, dataSize);
    return UDMF\_E\_OK;
}

#### 使用UDMF更新UDS数据

下面以更新超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1.  创建hyperlink的UDS数据结构。
2.  设置hyperlink中的URL和描述信息。
3.  创建OH\_UdmfRecord对象，并向OH\_UdmfRecord中添加超链接类型数据。
4.  创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord。
5.  构建数据操作选项。
6.  更新数据，将数据写入数据库中。
7.  使用完成后销毁指针。

int32\_t AddHyperlinkToUdmfRecord(OH\_UdsHyperlink\* hyperlink, OH\_UdmfRecord\* record, OH\_UdmfData\* data)
{
    // 2. 设置hyperlink中的URL和描述信息。
    int32\_t ret = OH\_UdsHyperlink\_SetUrl(hyperlink, "www.demo2.com");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set url error!");
        return ret;
    }
    ret = OH\_UdsHyperlink\_SetDescription(hyperlink, "This is the new description.");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set description error!");
        return ret;
    }
    // 3. 向OH\_UdmfRecord中添加超链接类型数据。
    ret = OH\_UdmfRecord\_AddHyperlink(record, hyperlink);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add hyperlink to record error!");
        return ret;
    }
    // 4. 向OH\_UdmfData中添加OH\_UdmfRecord。
    ret = OH\_UdmfData\_AddRecord(data, record);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add record to data error!");
        return ret;
    }
    return UDMF\_E\_OK;
}

int32\_t UpdateDataTest()
{
    // 1.创建hyperlink的UDS数据结构、OH\_UdmfRecord对象及OH\_UdmfData对象。
    OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
    OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
    OH\_UdmfData\* data = OH\_UdmfData\_Create();
    int32\_t ret = AddHyperlinkToUdmfRecord(hyperlink, record, data);
    if (ret != UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Fail to create hyperlink!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        return ret;
    }
    // 5. 构建数据操作选项。
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    // 此处key为示例，不可直接使用，其值应与OH\_Udmf\_SetUnifiedDataByOptions接口中获取到的key值保持一致。
    char key\[\] = "udmf://DataHub/com.ohos.test/0123456789";
    ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK
        || OH\_UdmfOptions\_SetKey(options, key) != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 6. 更新数据，将数据写入数据库中。
    ret = OH\_Udmf\_UpdateUnifiedData(options, data);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Update data error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_LOG\_INFO(LOG\_APP, "update data success");
    // 7. 使用完成后销毁指针。
    OH\_UdsHyperlink\_Destroy(hyperlink);
    OH\_UdmfRecord\_Destroy(record);
    OH\_UdmfData\_Destroy(data);
    OH\_UdmfOptions\_Destroy(options);
    return UDMF\_E\_OK;
}

#### 使用UDMF删除UDS数据

下面继续以获取超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1.  构建数据操作选项。
2.  通过数据操作选项删除数据。
3.  判断OH\_UdmfData是否有对应的类型。
4.  获取数据记录和hyperlink数据。
5.  获取数据记录中的元素。
6.  销毁指针。

int32\_t ProcessRecordHyperlinks(OH\_UdmfRecord\* record, unsigned int recordTypeIdCount, char\*\* typeIdsFromRecord)
{
    for (unsigned int k = 0; k < recordTypeIdCount; k++) {
        // 从OH\_UdmfRecord中获取超链接类型数据。
        if (strcmp(typeIdsFromRecord\[k\], UDMF\_META\_HYPERLINK) == 0) {
            // 创建hyperlink的UDS，用来承载record中读取出来的hyperlink数据。
            OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
            int32\_t ret = OH\_UdmfRecord\_GetHyperlink(record, hyperlink);
            if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "Fail get hyperlink from record!");
                OH\_UdsHyperlink\_Destroy(hyperlink);
                return ret;
            }
            // 读取OH\_UdsHyperlink中的各项信息。
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink type id is : %{public}s", OH\_UdsHyperlink\_GetType(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink url is : %{public}s", OH\_UdsHyperlink\_GetUrl(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink description is : %{public}s",
                OH\_UdsHyperlink\_GetDescription(hyperlink));
            OH\_UdsHyperlink\_Destroy(hyperlink);
        }
    }
    return UDMF\_E\_OK;
}

int32\_t ProcessDataElement(OH\_UdmfData\* data)
{
    unsigned int recordsCount = 0;
    OH\_UdmfRecord\*\* records = OH\_UdmfData\_GetRecords(data, &recordsCount);
    OH\_LOG\_INFO(LOG\_APP, "the count of records count is %{public}u", recordsCount);
    // 5. 获取数据记录中的元素。
    for (unsigned int j = 0; j < recordsCount; j++) {
        // 获取OH\_UdmfRecord类型列表。
        unsigned int recordTypeIdCount = 0;
        char\*\* typeIdsFromRecord = OH\_UdmfRecord\_GetTypes(records\[j\], &recordTypeIdCount);
        int32\_t ret = ProcessRecordHyperlinks(records\[j\], recordTypeIdCount, typeIdsFromRecord);
        if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "ProcessRecordHyperlinks error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t ProcessHyperlinkDataFromArray(OH\_UdmfData\* readData, unsigned int dataSize, OH\_UdmfData\*\* dataArray)
{
    for (unsigned int i = 0; i < dataSize - 1; i++) {
        OH\_UdmfData\* data = OH\_UDMF\_GetDataElementAt(dataArray, i);
        // 3. 判断OH\_UdmfData是否有对应的类型。
        if (!OH\_UdmfData\_HasType(data, UDMF\_META\_HYPERLINK)) {
            OH\_LOG\_INFO(LOG\_APP, "There is no hyperlink type in data\[%{public}u\].", i);
            continue;
        }
        // 4. 获取数据记录和hyperlink数据。
        int32\_t ret = ProcessDataElement(data);
        if (ret != UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "processDataElement data error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t DeleteDataTest()
{
    // 1. 构建数据操作选项。
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    int32\_t ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 2. 通过数据操作选项删除数据。
    unsigned int dataSize = 0;
    OH\_UdmfData\* readData = nullptr;
    ret = OH\_Udmf\_DeleteUnifiedData(options, &readData, &dataSize);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Delete Data error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_UdmfOptions\_Destroy(options);
    if (dataSize == 0) {
        OH\_LOG\_INFO(LOG\_APP, "the size of data is %{public}u", dataSize);
        return UDMF\_E\_OK;
    }
    OH\_LOG\_INFO(LOG\_APP, "the size of data is %{public}u", dataSize);
    OH\_UdmfData\*\* dataArray = &readData;
    ret = ProcessHyperlinkDataFromArray(readData, dataSize, dataArray);
    if (ret != UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Process hyperlink data error!");
        return ret;
    }
    // 6. 销毁指针。
    OH\_Udmf\_DestroyDataArray(dataArray, dataSize);
    return UDMF\_E\_OK;
}

#### 使用UDMF延迟写入UDS数据

#### \[h2\]定义UDS数据提供函数

下面以超链接hyperlink类型数据场景为例，说明如何定义一个提供UDS数据的回调函数。

1.  定义OH\_UdmfRecordProvider的数据提供函数。
2.  在数据提供函数中，创建hyperlink类型的UDS数据结构。
3.  设置hyperlink的URL和描述信息。
4.  定义OH\_UdmfRecordProvider销毁时触发的回调函数。

// 为了代码可读性，代码中省略了各个步骤操作结果的校验，实际开发中需要确认每次调用的成功。
// 1. 获取数据时触发的提供UDS数据的回调函数。
static void\* GetDataCallback(void\* context, const char\* type)
{
    if (strcmp(type, UDMF\_META\_HYPERLINK) == 0) {
        // 2. 创建超链接hyperlink数据的UDS数据结构。
        OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
        // 3. 设置hyperlink中的URL和描述信息。
        OH\_UdsHyperlink\_SetUrl(hyperlink, "www.demo.com");
        OH\_UdsHyperlink\_SetDescription(hyperlink, "This is the description.");
        return hyperlink;
    }
    return nullptr;
}
// 4. OH\_UdmfRecordProvider销毁时触发的回调函数。
static void ProviderFinalizeCallback(void\* context) { OH\_LOG\_INFO(LOG\_APP, "OH\_UdmfRecordProvider finalize."); }

#### \[h2\]延迟写入UDS数据

下面以延迟写入超链接类型数据为例，说明如何使用OH\_UdmfRecordProvider与UDMF。此步骤完成后，超链接类型数据并未真正写入数据库。只有当数据使用者从OH\_UdmfRecord中获取OH\_UdsHyperlink时，才会触发上文定义的GetDataCallback数据提供函数，从中获取数据。

1.  创建OH\_UdmfRecordProvider对象，设置它的数据提供函数和销毁回调函数。
2.  创建OH\_UdmfRecord对象，并配置OH\_UdmfRecordProvider。
3.  创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord。
4.  构建数据并写入数据库中，获取返回的Key值。
5.  使用完成后销毁指针。

int32\_t ProviderSetDataTest()
{
    // 为了代码可读性，代码中省略了各个步骤操作结果的校验，实际开发中需要确认每次调用的成功。
    // 1. 创建一个OH\_UdmfRecordProvider，设置它的数据提供函数和销毁回调函数。
    OH\_UdmfRecordProvider\* provider = OH\_UdmfRecordProvider\_Create();
    OH\_UdmfRecordProvider\_SetData(provider, (void\*)provider, GetDataCallback, ProviderFinalizeCallback);

    // 2. 创建OH\_UdmfRecord对象，并配置OH\_UdmfRecordProvider。
    OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
    const char\* types\[1\] = {UDMF\_META\_HYPERLINK};
    OH\_UdmfRecord\_SetProvider(record, types, 1, provider);

    // 3. 创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord。
    OH\_UdmfData\* data = OH\_UdmfData\_Create();
    OH\_UdmfData\_AddRecord(data, record);

    // 4. 构建数据并写入数据库中，获取返回的Key值。
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    if (OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB) != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdmfOptions\_Destroy(options);
        return UDMF\_ERR;
    }
    char key\[UDMF\_KEY\_BUFFER\_LEN\] = {0};
    if (OH\_Udmf\_SetUnifiedDataByOptions(options, data, key, sizeof(key)) != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set data error!");
    }
    OH\_LOG\_INFO(LOG\_APP, "key = %{public}s", key);

    // 5. 使用完成后销毁指针。
    OH\_UdmfRecord\_Destroy(record);
    OH\_UdmfData\_Destroy(data);
    OH\_UdmfOptions\_Destroy(options);
    return UDMF\_E\_OK;
}
