---
title: "在NDK中保证多实例场景功能正常"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-scope-task"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (基于NDK构建UI)"
  - "在NDK中保证多实例场景功能正常"
captured_at: "2026-04-17T01:35:39.959Z"
---

# 在NDK中保证多实例场景功能正常

API version 20开始，ArkUI开发框架新增了[OH\_ArkUI\_RunTaskInScope](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_runtaskinscope)接口，解决Native侧多实例场景下的组件操作问题。该功能通过动态切换执行上下文，确保跨实例组件属性设置的合法性，避免实例上下文不匹配导致的接口调用异常。

在NDK多窗口开发时，可能会涉及到组件的跨实例设置属性等场景，使用该能力可确保在调用跨实例组件设置属性时的上下文正确性，避免跨实例接口调用失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/FuqkvL1BS3yQu-EpqElruA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=BF48F49DF3DC92E4057559952AECCC9DBCE974A98D06F82E1E4B119497C36766)

-   适用于NDK多窗口开发中不同UI实例间的交互场景，例如在页面B中修改页面A创建的组件属性或未挂载到UI树的组件逻辑。
    
-   支持通过userData参数传递自定义数据结构（如组件指针、业务参数等），便于在回调任务中精准定位目标组件。
    
-   与[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getattachednodehandlebyid)等接口配合使用，有效规避跨实例访问导致的空指针或权限异常问题。
    

本示例展示OH\_ArkUI\_RunTaskInScope接口的基础使用方式，OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById用于获取前置实例页面内的组件，相关使用请参考[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getattachednodehandlebyid)，此处userData传入的数据类型为最终要设置的组件指针，便于设置对应组件属性。

const uint32\_t VALUE\_2 = 250;
const uint32\_t VALUE\_3 = 480;

//page1
ArkUI\_NodeHandle button = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
ArkUI\_AttributeItem LABEL\_Item = {.string = "pageOneButton"};
//设置id，用于在第二个页面内通过接口查找
ArkUI\_AttributeItem id = {.string = "pageOneButton"};
nodeAPI->setAttribute(button, NODE\_ID, &id);
nodeAPI->setAttribute(button, NODE\_BUTTON\_LABEL, &LABEL\_Item);
nodeAPI->addChild(textContainer, button);

//page2
//pageOneButton由前置页面创建，通过OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById在第二个页面获取。
ArkUI\_NodeHandle pageOneButton = nullptr;
auto errorCode = OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById("pageOneButton", &pageOneButton);
if (errorCode != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
    OH\_LOG\_ERROR(LOG\_APP, "test Failed to get pageOneButton handle, error code: %{public}d", errorCode);
    return nullptr;
}
auto uiContext = OH\_ArkUI\_GetContextByNode(pageOneButton);
if (uiContext == nullptr) {
    OH\_LOG\_ERROR(LOG\_APP, "test Failed to get UI context for pageOneButton");
    return nullptr;
}
OH\_ArkUI\_RunTaskInScope(uiContext, pageOneButton, \[\](void \*userData) {
    auto \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
    auto pageOneButton = (ArkUI\_NodeHandle)userData;
    ArkUI\_NumberValue value\[\] = {VALUE\_3};
    ArkUI\_AttributeItem LABEL\_Item = {.string = "success"};
    value\[0\].f32 = VALUE\_2;
    ArkUI\_AttributeItem button\_Item = {value, sizeof(value) / sizeof(ArkUI\_NumberValue)};
    nodeAPI->setAttribute(pageOneButton, NODE\_BUTTON\_LABEL, &LABEL\_Item);
    nodeAPI->setAttribute(pageOneButton, NODE\_WIDTH, &button\_Item);
});
