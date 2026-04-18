---
title: "接入ArkTS页面"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (基于NDK构建UI)"
  - "接入ArkTS页面"
captured_at: "2026-04-17T01:35:39.718Z"
---

# 接入ArkTS页面

#### 占位组件

使用NDK接口构建UI界面时，需要在ArkTS页面创建用于挂载NDK接口创建组件的占位组件。占位组件类型为[ContentSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-contentslot)，ContentSlot能够绑定一个[NodeContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontent)对象，该对象可通过Node-API传递到Native侧挂载显示Native组件。

-   NDK配置文件entry/src/main/cpp/types/libentry/oh-package.json5如下。
    
    {
      "name": "libentry.so",
      "types": "./Index.d.ts",
      "version": "1.0.0",
      "description": "Please describe the basic information."
    }
    
-   占位组件和其他ArkTS系统组件使用方法相同。详细代码请参考[示例](#示例)。
    
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct Index {
      // 初始化NodeContent对象。
      private rootSlot:NodeContent = new NodeContent();
      @State @Watch('changeNativeFlag') showNative: boolean = false;
    
      changeNativeFlag(): void {
        if (this.showNative) {
          // 传递NodeContent对象用于Native创建组件的挂载显示
          nativeNode.createNativeRoot(this.rootSlot)
        } else {
          // 销毁NativeModule组件
          nativeNode.destroyNativeRoot()
        }
      }
    
      build() {
        Column() {
          Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI')
            .onClick(() => {
            this.showNative = !this.showNative
          })
            .id('btn')
          Row() {
            // 将NodeContent和ContentSlot占位组件绑定
            ContentSlot(this.rootSlot)
          }.layoutWeight(1)
        }
        .width('100%')
        .height('100%')
      }
    }
    
-   占位组件可以通过相关接口在Native侧转化为挂载对象。
    
    ```c
    ArkUI_NodeContentHandle contentHandle;
    OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
    ```
    
-   挂载对象提供了相关挂载和卸载组件接口。
    
    ```c
    OH_ArkUI_NodeContent_AddNode(handle_, myNativeNode);
    OH_ArkUI_NodeContent_RemoveNode(handle_, myNativeNode);
    ```
    

#### NDK组件模块

NDK提供的UI组件能力如组件创建、树操作、属性设置、事件注册等是通过函数指针结构体（如[ArkUI\_NativeNodeAPI\_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1)）进行暴露，该函数指针结构体可以通过[模块查询接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface)获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/5nNRZP-iR_Omjc5tYRf2Dg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=6C4CB5883034945F540D18FE3E7B29222AFB8CE326635F893DFBC26F081A5F03)

-   [模块查询接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface)带有初始化NDK的逻辑，建议先调用该接口进行全局初始化，再使用NDK进行UI构造。

```c
ArkUI_NativeNodeAPI_1* arkUINativeNodeApi = nullptr;
OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, arkUINativeNodeApi);
```

在获取到函数指针结构体后，可以使用该结构体内的函数实现相关UI组件操作。

-   组件创建和销毁。
    
    ```c
    auto listNode = arkUINativeNodeApi->createNode(ARKUI_NODE_LIST);
    arkUINativeNodeApi->disposeNode(listNode);
    ```
    
    获取NDK接口支持的组件范围可以通过查询[ArkUI\_NodeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodetype)枚举值。
    
-   组件树操作。
    
    ```c
    auto parent = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
    auto child = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
    arkUINativeNodeApi->addChild(parent, child);
    arkUINativeNodeApi->removeChild(parent, child);
    ```
    
-   属性设置。
    
    ```c
    auto stack = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
    ArkUI_NumberValue value[] = {{.f32 = 100}};
    ArkUI_AttributeItem item = {value, 1};
    arkUINativeNodeApi->setAttribute(stack, NODE_WIDTH, &item);
    ArkUI_NumberValue value_color[] = {{.u32 = 0xff112233}};
    ArkUI_AttributeItem item_color = {value_color, 1};
    arkUINativeNodeApi->setAttribute(stack, NODE_BACKGROUND_COLOR, &item);
    ```
    
    获取NDK接口支持的属性范围可以通过查询[ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype)枚举值。
    
-   事件注册。
    
    ```c
    auto stack = arkUINativeNodeApi->createNode(ARKUI_NODE_STACK);
    arkUINativeNodeApi->addNodeEventReceiver(stack, [](ArkUI_NodeEvent* event){
        // process event
    });
    arkUINativeNodeApi->registerNodeEvent(stack, NODE_ON_CLICK, 0, nullptr);
    ```
    
    获取NDK接口支持的事件范围可以通过查询[ArkUI\_NodeEventType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype)枚举值。
    

#### 示例

下面的示例展示了如何使用ContentSlot挂载Native侧的文本列表。

示例代码的目录结构及其文件说明如下：

```c
.
|——cpp
|    |——types
|    |      |——libentry
|    |      |       |——index.d.ts 提供Native和ArkTS侧的桥接方法。
|    |——napi_init.cpp 与index.d.ts对应的桥接方法对接Native侧的定义处。
|    |——NativeEntry.cpp 桥接方法的Native侧实现。
|    |——NativeEntry.h 桥接方法的Native侧定义。
|    |——NativeModule.h 提供获取ArkUI在Native侧模块的封装接口。
|    |——CMakeLists.txt C语言库引用文件。
|    |——ArkUIBaseNode.h 节点封装扩展类。
|    |——ArkUINode.h 节点封装扩展类。
|    |——ArkUIListNode.h 节点封装扩展类。
|    |——ArkUIListItemNode.h 节点封装扩展类。
|    |——ArkUITextNode.h 节点封装扩展类。
|    |——NormalTextListExample.h 示例代码文件。
|
|——ets
|    |——pages
|         |——entry.ets 应用启动页，加载承载Native的容器。
|
```

**图1** Native文本列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/-aFQqEPER8-BzQkXS5TJYA/zh-cn_image_0000002569018701.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013540Z&HW-CC-Expire=86400&HW-CC-Sign=D22AF62FCD6E26F666567F33F64F8AAD8B23204EAEA8E93945FB0297474BC9DD)

1.  在ArkTS页面上声明用于Native页面挂载的占位组件，并在页面创建时通知Native侧创建文本列表。
    
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct Index {
      // 初始化NodeContent对象。
      private rootSlot:NodeContent = new NodeContent();
      @State @Watch('changeNativeFlag') showNative: boolean = false;
    
      changeNativeFlag(): void {
        if (this.showNative) {
          // 传递NodeContent对象用于Native创建组件的挂载显示
          nativeNode.createNativeRoot(this.rootSlot)
        } else {
          // 销毁NativeModule组件
          nativeNode.destroyNativeRoot()
        }
      }
    
      build() {
        Column() {
          Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI')
            .onClick(() => {
            this.showNative = !this.showNative
          })
            .id('btn')
          Row() {
            // 将NodeContent和ContentSlot占位组件绑定
            ContentSlot(this.rootSlot)
          }.layoutWeight(1)
        }
        .width('100%')
        .height('100%')
      }
    }
    
2.  使用Native模板创建工程，并在Native侧提供Node-API的桥接方法，实现ArkTS侧的NativeNode模块接口。
    
    接口声明。
    
    // entry/src/main/cpp/types/libentry/Index.d.ts
    export const createNativeRoot: (content: Object) => void;
    export const destroyNativeRoot: () => void;
    
    Native实现。
    
    // entry/src/main/cpp/napi\_init.cpp
    #include "napi/native\_api.h"
    #include "NativeEntry.h"
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        // 绑定Native侧的创建组件和销毁组件。
        napi\_property\_descriptor desc\[\] = {
            {"createNativeRoot", nullptr,
            NativeModule::CreateNativeRoot, nullptr, nullptr,
            nullptr, napi\_default, nullptr},
            {"destroyNativeRoot", nullptr,
            NativeModule::DestroyNativeRoot, nullptr, nullptr,
            nullptr, napi\_default, nullptr}};
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = ((void \*)0),
        .reserved = {0},
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }
    
3.  在NativeEntry.h文件中创建Native界面。
    
    // NativeEntry.h
    
    #ifndef MYAPPLICATION\_NATIVEENTRY\_H
    #define MYAPPLICATION\_NATIVEENTRY\_H
    
    #include <ArkUIBaseNode.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info);
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info);
    
    // 管理Native组件的生命周期和内存。
    class NativeEntry {
    public:
        static NativeEntry \*GetInstance()
        {
            static NativeEntry nativeEntry;
            return &nativeEntry;
        }
    
        void SetContentHandle(ArkUI\_NodeContentHandle handle)
        {
            handle\_ = handle;
        }
    
        void SetRootNode(const std::shared\_ptr<ArkUIBaseNode> &baseNode)
        {
            root\_ = baseNode;
            // 添加Native组件到NodeContent上用于挂载显示。
            OH\_ArkUI\_NodeContent\_AddNode(handle\_, root\_->GetHandle());
        }
        void DisposeRootNode()
        {
            // 从NodeContent上卸载组件并销毁Native组件。
            OH\_ArkUI\_NodeContent\_RemoveNode(handle\_, root\_->GetHandle());
            root\_.reset();
        }
    
    private:
        std::shared\_ptr<ArkUIBaseNode> root\_;
        ArkUI\_NodeContentHandle handle\_;
    };
    
    } // namespace NativeModule
    
    #endif  // MYAPPLICATION\_NATIVEENTRY\_H
    
    对应实现文件。
    
    // NativeEntry.cpp
    
    #include <arkui/native\_node\_napi.h>
    #include <js\_native\_api.h>
    #include "NativeEntry.h"
    #include "NormalTextListExample.h"
    
    namespace NativeModule {
    
    napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // 获取NodeContent
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
        // 创建文本列表
        auto list = CreateTextListExample();
    
        // 保持Native侧对象到管理类中，维护生命周期。
        NativeEntry::GetInstance()->SetRootNode(list);
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // 从管理类中释放Native侧对象。
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    } // namespace NativeModule
    
    使用NDK提供的C接口需要在CMakeLists.txt中增加libace\_ndk.z.so的引用，如下所示。其中entry为工程导出的动态库名称，如当前示例使用的是默认的名称libentry.so。新增cpp文件后，同样需要在CMakeLists.txt中添加相应的cpp文件。若未进行此配置，对应的文件将不会被编译。
    
    ```c
    add_library(entry SHARED napi_init.cpp NativeEntry.cpp)
    target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so)
    ```
    
4.  由于NDK接口提供的是C接口，为了使用面向对象的方式简化编程和工程管理，这里建议使用C++进行二次封装，下面示例代码展示了示例界面中所需的列表，文本组件封装类。
    
    1）获取ArkUI在NDK接口的入口模块[ArkUI\_NativeNodeAPI\_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1)，该结构体模块提供了一系列组件创建、树构建、属性设置和事件注册等函数指针。
    
    // NativeModule.h
    // 提供获取ArkUI在Native侧模块的封装接口
    
    #ifndef MYAPPLICATION\_NATIVEMODULE\_H
    #define MYAPPLICATION\_NATIVEMODULE\_H
    
    #include <arkui/native\_node.h>
    #include <cassert>
    
    #include <arkui/native\_interface.h>
    
    namespace NativeModule {
    
    class NativeModuleInstance {
    public:
        static NativeModuleInstance \*GetInstance()
        {
            static NativeModuleInstance instance;
            return &instance;
        }
        NativeModuleInstance()
        {
            OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, arkUINativeNodeApi\_);
        }
        // 暴露给其他模块使用。
        ArkUI\_NativeNodeAPI\_1 \*GetNativeNodeAPI() { return arkUINativeNodeApi\_; }
    
    private:
        ArkUI\_NativeNodeAPI\_1 \*arkUINativeNodeApi\_ = nullptr;
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_NATIVEMODULE\_H
    
    2）提供列表，文本组件的基类对象，用于封装通用属性和事件。
    
    // ArkUIBaseNode.h
    // 提供组件树操作的基类。
    #ifndef MYAPPLICATION\_ARKUIBASENODE\_H
    #define MYAPPLICATION\_ARKUIBASENODE\_H
    
    #include <arkui/native\_type.h>
    #include <list>
    #include <memory>
    
    #include "NativeModule.h"
    
    namespace NativeModule {
    
    class ArkUIBaseNode {
    public:
        explicit ArkUIBaseNode(ArkUI\_NodeHandle handle)
            : handle\_(handle), nativeModule\_(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()) {}
    
        virtual ~ArkUIBaseNode()
        {
            // 封装析构函数，实现子节点移除功能。
            if (!children\_.empty()) {
                for (const auto& child : children\_) {
                    nativeModule\_->removeChild(handle\_, child->GetHandle());
                }
                children\_.clear();
            }
            // 封装析构函数，统一回收节点资源。
            nativeModule\_->disposeNode(handle\_);
        }
    
        void AddChild(const std::shared\_ptr<ArkUIBaseNode> &child)
        {
            children\_.emplace\_back(child);
            OnAddChild(child);
        }
    
        void RemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child)
        {
            children\_.remove(child);
            OnRemoveChild(child);
        }
    
        void InsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index)
        {
            if (index >= children\_.size()) {
                AddChild(child);
            } else {
                auto iter = children\_.begin();
                std::advance(iter, index);
                children\_.insert(iter, child);
                OnInsertChild(child, index);
            }
        }
    
        ArkUI\_NodeHandle GetHandle() const { return handle\_; }
    
    protected:
        // 针对父容器子类需要重载下面的函数，实现组件挂载和卸载。
        virtual void OnAddChild(const std::shared\_ptr<ArkUIBaseNode> &child) {}
        virtual void OnRemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child) {}
        virtual void OnInsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index) {}
    
        ArkUI\_NodeHandle handle\_;
        ArkUI\_NativeNodeAPI\_1 \*nativeModule\_ = nullptr;
    
    private:
        std::list<std::shared\_ptr<ArkUIBaseNode>> children\_;
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIBASENODE\_H
    
    // ArkUINode.h
    // 提供通用属性和事件的封装。
    #ifndef MYAPPLICATION\_ARKUINODE\_H
    #define MYAPPLICATION\_ARKUINODE\_H
    
    #include "ArkUIBaseNode.h"
    #include "NativeModule.h"
    #include <arkui/native\_node.h>
    #include <arkui/native\_type.h>
    
    namespace NativeModule {
    
    class ArkUINode : public ArkUIBaseNode {
    public:
        explicit ArkUINode(ArkUI\_NodeHandle handle) : ArkUIBaseNode(handle) {}
    
        ~ArkUINode() override {}
        
        void SetWidth(float width)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = width}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_WIDTH, &item);
        }
        void SetPercentWidth(float percent)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = percent}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_WIDTH\_PERCENT, &item);
        }
        void SetHeight(float height)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = height}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_HEIGHT, &item);
        }
        void SetPercentHeight(float percent)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = percent}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_HEIGHT\_PERCENT, &item);
        }
        void SetBackgroundColor(uint32\_t color)
        {
            ArkUI\_NumberValue value\[\] = {{.u32 = color}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_BACKGROUND\_COLOR, &item);
        }
    
    protected:
        // 组件树操作的实现类对接。
        void OnAddChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            nativeModule\_->addChild(handle\_, child->GetHandle());
        }
        void OnRemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            nativeModule\_->removeChild(handle\_, child->GetHandle());
        }
        void OnInsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index) override
        {
            nativeModule\_->insertChildAt(handle\_, child->GetHandle(), index);
        }
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUINODE\_H
    
    3）实现列表组件。
    
    // ArkUIListNode.h
    // 提供列表组件的封装。
    #ifndef MYAPPLICATION\_ARKUILISTNODE\_H
    #define MYAPPLICATION\_ARKUILISTNODE\_H
    
    #include "ArkUINode.h"
    
    namespace NativeModule {
    class ArkUIListNode : public ArkUINode {
    public:
        ArkUIListNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_LIST)) {}
    
        ~ArkUIListNode() override {}
        
        void SetScrollBarState(bool isShow)
        {
            ArkUI\_ScrollBarDisplayMode displayMode =
                isShow ? ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_ON : ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF;
            ArkUI\_NumberValue value\[\] = {{.i32 = displayMode}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_SCROLL\_BAR\_DISPLAY\_MODE, &item);
        }
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUILISTNODE\_H
    
    4）实现列表项组件。
    
    // ArkUIListItemNode.h
    // 提供列表项的封装类。
    #ifndef MYAPPLICATION\_ARKUISTACKNODE\_H
    #define MYAPPLICATION\_ARKUISTACKNODE\_H
    
    #include "ArkUINode.h"
    
    namespace NativeModule {
    class ArkUIListItemNode : public ArkUINode {
    public:
        ArkUIListItemNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_LIST\_ITEM)) {}
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUISTACKNODE\_H
    
    5）实现文本组件。
    
    // ArkUITextNode.h
    // 实现文本组件的封装类。
    #ifndef MYAPPLICATION\_ARKUITEXTNODE\_H
    #define MYAPPLICATION\_ARKUITEXTNODE\_H
    
    #include "ArkUINode.h"
    
    #include <string>
    
    namespace NativeModule {
    class ArkUITextNode : public ArkUINode {
    public:
        ArkUITextNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_TEXT)) {}
        
        void SetFontSize(float fontSize)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = fontSize}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_FONT\_SIZE, &item);
        }
        void SetFontColor(uint32\_t color)
        {
            ArkUI\_NumberValue value\[\] = {{.u32 = color}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_FONT\_COLOR, &item);
        }
        void SetTextContent(const std::string &content)
        {
            ArkUI\_AttributeItem item = {nullptr, 0, content.c\_str()};
            nativeModule\_->setAttribute(handle\_, NODE\_TEXT\_CONTENT, &item);
        }
        void SetTextAlign(ArkUI\_TextAlignment align)
        {
            ArkUI\_NumberValue value\[\] = {{.i32 = align}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_TEXT\_ALIGN, &item);
        }
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUITEXTNODE\_H
    
5.  完善步骤3的CreateTextListExample函数，实现Native文本列表的创建和挂载显示。
    
    // NormalTextListExample.h
    
    #ifndef MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
    #define MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
    
    #include "ArkUIBaseNode.h"
    #include "ArkUIListItemNode.h"
    #include "ArkUIListNode.h"
    #include "ArkUITextNode.h"
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateTextListExample()
    {
        // 创建组件并挂载
        // 1：使用智能指针创建List组件。
        auto list = std::make\_shared<ArkUIListNode>();
        list->SetPercentWidth(1);
        list->SetPercentHeight(1);
        list->SetScrollBarState(true);
        const int itemCount = 30;
        const int fontSizes = 16;
        const float screenWidth = 1;
        const int defaultHeight = 100;
        // 2：创建ListItem子组件并挂载到List上。
        for (int32\_t i = 0; i < itemCount; ++i) {
            auto listItem = std::make\_shared<ArkUIListItemNode>();
            auto textNode = std::make\_shared<ArkUITextNode>();
            textNode->SetTextContent(std::to\_string(i));
            textNode->SetFontSize(fontSizes);
            textNode->SetFontColor(0xFF000000);
            textNode->SetPercentWidth(1);
            textNode->SetPercentWidth(screenWidth);
            textNode->SetHeight(defaultHeight);
            textNode->SetBackgroundColor(0xFFfffacd);
            textNode->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
            listItem->InsertChild(textNode, i);
            list->AddChild(listItem);
        }
        return list;
    }
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
