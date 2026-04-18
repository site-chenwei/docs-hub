---
title: "通过EmbeddedComponent拉起EmbeddedUIExtensionAbility"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embedded-component"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (基于NDK构建UI)"
  - "通过EmbeddedComponent拉起EmbeddedUIExtensionAbility"
captured_at: "2026-04-17T01:35:39.952Z"
---

# 通过EmbeddedComponent拉起EmbeddedUIExtensionAbility

ArkUI在Native侧提供的能力是ArkTS的子集，某些能力不会在Native侧提供，例如声明式UI语法、自定义struct组件及UI系统预置UI组件库。

从API version 20开始，ArkUI开发框架提供了Native侧嵌入EmbeddedComponent组件的能力，此能力依赖于[EmbeddedComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component)机制。EmbeddedComponent用于支持在当前页面嵌入同一应用内其他[EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability)提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，负责页面布局和渲染。此功能主要用于有进程隔离需求的模块化开发场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/A7LLx-brTO6YsGxAOVv_Fw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=2B215B5229582CD7A429DB330B72A28E938B00E5D94B183F7622FCBD4A43BC77)

-   使用[OH\_ArkUI\_EmbeddedComponentOption\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_create)获取[ArkUI\_EmbeddedComponentOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-embeddedcomponentoption)后，可以使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_setonerror)设置onError回调，使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_setonterminated)设置onTerminated回调。可以使用[OH\_ArkUI\_NodeUtils\_MoveTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_moveto)迁移节点。
    
-   使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_setonterminated)设置onTerminated回调时，返回的want参数，只支持提供方返回的want参数的key，value解析，不支持嵌套解析。
    
-   在EmbeddedComponent销毁时，调用[OH\_ArkUI\_EmbeddedComponentOption\_Dispose](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_dispose)释放内存。
    
-   EmbeddedComponent组件需要使用[setAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute)设置宽高才能显示。
    

本示例展示EmbeddedComponent组件NDK的基础使用方式，ability相关使用请参考[EmbeddedComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component)。示例应用的bundleName为"com.example.embeddeddemo"，同一应用下被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。本示例仅支持在具有多进程权限的设备上运行，例如PC/2in1。

#include <arkui/native\_node.h>
#include <arkui/native\_type.h>
#include <AbilityKit/ability\_base/want.h> //引用元能力want头文件

// 注册事件
void onError(int32\_t code, const char \*name, const char \*message) {}
void onTerminated(int32\_t code, AbilityBase\_Want \*want) {}
const unsigned int LOG\_PRINT\_DOMAIN = 0xFF00;
#define SIZE\_300 300
#define SIZE\_401 401
#define SIZE\_480 480
// ···
    // 创建节点
    ArkUI\_NodeHandle embeddedNode = nodeAPI->createNode(ARKUI\_NODE\_EMBEDDED\_COMPONENT);
    // 设置属性
    AbilityBase\_Element Element = {.bundleName = "com.example.uiextensionandaccessibility",
                                   .abilityName = "ExampleEmbeddedAbility",
                                   .moduleName = "entry"};       // 由元能力提供接口
    AbilityBase\_Want \*want = OH\_AbilityBase\_CreateWant(Element); // 由元能力提供接口
    if (want == nullptr) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "AbilityBase\_Want", "~PluginManager");
    }
    ArkUI\_AttributeItem itemobjwant = {.object = want};
    nodeAPI->setAttribute(embeddedNode, NODE\_EMBEDDED\_COMPONENT\_WANT, &itemobjwant);

    auto embeddedNode\_option = OH\_ArkUI\_EmbeddedComponentOption\_Create();
    auto onErrorCallback = onError;
    auto onTerminatedCallback = onTerminated;
    OH\_ArkUI\_EmbeddedComponentOption\_SetOnError(embeddedNode\_option, onErrorCallback);
    OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated(embeddedNode\_option, onTerminatedCallback);

    ArkUI\_AttributeItem itemobjembeddedNode = {.object = embeddedNode\_option};
    nodeAPI->setAttribute(embeddedNode, NODE\_EMBEDDED\_COMPONENT\_OPTION, &itemobjembeddedNode);

    // 设置基本属性，如宽高
    ArkUI\_NumberValue value\[\] = {SIZE\_480};
    ArkUI\_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI\_NumberValue)};
    value\[0\].f32 = SIZE\_300;
    nodeAPI->setAttribute(embeddedNode, NODE\_WIDTH, &item);
    nodeAPI->setAttribute(embeddedNode, NODE\_HEIGHT, &item);

    // 创建Column
    ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
    nodeAPI->setAttribute(column, NODE\_WIDTH, &item);
    ArkUI\_NumberValue column\_bc\[\] = {{.u32 = 0xFFF00BB}};
    ArkUI\_AttributeItem column\_item = {column\_bc, 1};
    nodeAPI->setAttribute(column, NODE\_BACKGROUND\_COLOR, &column\_item);
    ArkUI\_AttributeItem column\_id = {.string = "Column\_CAPI"};
    nodeAPI->setAttribute(column, NODE\_ID, &column\_id);

    // 上树
    nodeAPI->addChild(column, embeddedNode);
