---
title: "嵌入ArkTS组件"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embed-arkts-components"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (基于NDK构建UI)"
  - "嵌入ArkTS组件"
captured_at: "2026-04-17T01:35:39.967Z"
---

# 嵌入ArkTS组件

ArkUI在Native侧提供的能力作为ArkTS的子集，部分能力不会在Native侧提供，如声明式UI语法，自定义struct组件，UI高级组件。

针对需要使用ArkTS侧独立能力的场景，ArkUI开发框架提供了Native侧嵌入ArkTS组件的能力，该能力依赖[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent)机制，通过ComponentContent完成对ArkTS组件的封装，然后将封装对象传递到Native侧，通过Native侧的[OH\_ArkUI\_GetNodeHandleFromNapiValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-napi-h#oh_arkui_getnodehandlefromnapivalue)接口转化为ArkUI\_NodeHandle对象用于Native侧组件挂载使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/cyDQHlw9TyG3X3qODxQ7Rg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=DC2135667BB7B5A95D13CFE8C9ADF92F9160BD3A0620572129BE73CFC2179EE8)

-   通过OH\_ArkUI\_GetNodeHandleFromNapiValue接口获得的ArkUI\_NodeHandle对象只能作为子组件参数使用，如[addChild](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addchild)接口的第二个参数，将该对象使用在其他场景下，如[setAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute)设置属性将不生效并返回错误码。
    
-   针对Native侧修改ArkTS组件的场景，需要在Native侧通过Node-API方式构建ArkTS侧的更新数据，再通过ComponentContent的[update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#update)接口更新。
    
-   [构建自定义组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-custom-components)时，相关函数如measureNode等无法对ArkTS模块内部的组件进行调用。
    

以下示例代码在[接入ArkTS页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)章节基础上引入ArkTS的Refresh组件。

**图1** Refresh组件挂载文本列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/64vpQco7RgeH52hv10Fg7w/zh-cn_image_0000002569018709.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=DCB0937F429C73727D7BE4246DBF4D444293222EF839C9F607AFD38E49E524CD)

1.  注册ArkTS组件创建函数给Native侧，以便Native侧调用，创建函数使用ComponentContent能力进行封装。
    
    // 使用ComponentContent能力创建ArkTS组件
    
    import { NodeContent, UIContext, RefreshModifier, ComponentContent } from '@kit.ArkUI';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const DOMAIN = 0x0000;
    
    // 定义Native侧和ArkTS进行交互的数据对象。
    interface NativeRefreshAttribute {
      isRefreshing: boolean;
      width?: number;
      height?: number;
      backgroundColor?: number;
      refreshOffset?: number;
      pullToRefresh?: boolean;
      onRefreshing?: () => void;
      onOffsetChange?: (offset: number) => void;
    }
    
    // 定义@Builder函数的入参格式。
    interface RefreshAttribute {
      isRefreshing: boolean;
      // 属性设置通过Modifier优化性能
      modifier?: RefreshModifier;
      slot?: NodeContent;
      onRefreshing?: () => void;
      onOffsetChange?: (offset: number) => void;
    }
    
    // ComponentContent封装ArkTS组件依赖全局@Builder函数，涉及复杂自定义组件场景，可以在@Builder函数中嵌套@Component自定义组件。
    // @Builder函数提供入参方式，方便后续通过ComponentContent的update接口进行参数更新。
    @Builder
    function mixedRefresh(attribute: RefreshAttribute) {
      Refresh({ refreshing: attribute.isRefreshing }) {
        // Refresh作为容器组件，需要使用ContentSlot机制预留子组件占位
        ContentSlot(attribute.slot);
      }.attributeModifier(attribute.modifier)
      .onRefreshing(() => {
        hilog.info(DOMAIN, 'testTag', 'on onRefreshing');
        if (attribute.onRefreshing) {
          hilog.info(DOMAIN, 'testTag', 'on native onRefreshing');
          attribute.onRefreshing();
        }
      })
      .onOffsetChange((value: number) => {
        hilog.info(DOMAIN, 'testTag', 'on offset change: ' + value);
        if (attribute.onOffsetChange) {
          hilog.info(DOMAIN, 'testTag', 'on native onOffsetChange');
          attribute.onOffsetChange(value);
        }
      });
    }
    
    // 定义创建函数的返回值，用于ArkTS侧和Native侧的交互。
    interface MixedModuleResult {
      // 定义针对Refresh构建函数的封装对象，用于Native侧转化为ArkUI\_NodeHandle对象。
      content?: ComponentContent<RefreshAttribute>;
      // Refresh作为容器组件，需要使用ContentSlot机制挂载Native侧的子组件。
      childSlot?: NodeContent;
    }
    
    // 提供创建ArkTS组件的入口函数。
    export function createMixedRefresh(value: NativeRefreshAttribute): MixedModuleResult {
      hilog.info(DOMAIN, 'testTag', 'createMixedRefresh');
      // 通过AppStorage对象在Ability启动的时候保持UI上下文对象。
      let uiContent = AppStorage.get<UIContext>('context');
      let modifier = new RefreshModifier();
      if (value.width) {
        modifier.width(value.width);
      }
      if (value.height) {
        modifier.height(value.height);
      }
      if (value.backgroundColor) {
        modifier.backgroundColor(value.backgroundColor);
      }
      if (value.pullToRefresh) {
        modifier.pullToRefresh(value.pullToRefresh);
      }
      if (value.refreshOffset) {
        modifier.refreshOffset(value.refreshOffset);
      }
      // 创建NodeContent插槽对象用于Refresh子组件挂载。
      let nodeSlot = new NodeContent();
      // 通过ComponentContent创建Refresh组件并将它封装起来。
      let content = new ComponentContent<RefreshAttribute>(uiContent!, wrapBuilder<\[RefreshAttribute\]>(mixedRefresh),
        {
          isRefreshing: value.isRefreshing,
          modifier: modifier,
          slot: nodeSlot,
          onRefreshing: value.onRefreshing,
          onOffsetChange: value.onOffsetChange
        });
      // 将Refresh组件的封装对象及其子组件插槽对象传递给Native侧。
      return { content: content, childSlot: nodeSlot };
    }
    
    // 定义Refresh组件的更新函数，用于Native侧更新。
    // 在更新场景下，需要将Refresh组件的封装对象及其子组件插槽对象返回，防止组件重新创建。
    export function updateMixedRefresh(refresh: ComponentContent<RefreshAttribute>, childSlot: NodeContent,
      value: NativeRefreshAttribute): void {
      let modifier = new RefreshModifier();
      if (value.width) {
        modifier.width(value.width);
      }
      if (value.height) {
        modifier.height(value.height);
      }
      if (value.backgroundColor) {
        modifier.backgroundColor(value.backgroundColor);
      }
      if (value.pullToRefresh) {
        modifier.pullToRefresh(value.pullToRefresh);
      }
      if (value.refreshOffset) {
        modifier.refreshOffset(value.refreshOffset);
      }
      // 调用ComponentContent的update接口进行更新。
      refresh.update({
        isRefreshing: value.isRefreshing,
        modifier: modifier,
        slot: childSlot,
        onRefreshing: value.onRefreshing,
        onOffsetChange: value.onOffsetChange
      });
    }
    
2.  将创建和更新函数注册给Native侧。
    
    //  Index.ets
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    import { createMixedRefresh, updateMixedRefresh } from './MixedModule';
    
    @Entry
    @Component
    struct Index {
      private rootSlot = new NodeContent();
      @State @Watch('changeNativeFlag') showNative: boolean = false;
    
      aboutToAppear(): void {
        // 设置uiContext;
        AppStorage.setOrCreate<UIContext>('context', this.getUIContext());
        // 设置混合模式下的builder函数。
        nativeNode.registerCreateMixedRefreshNode(createMixedRefresh);
        nativeNode.registerUpdateMixedRefreshNode(updateMixedRefresh);
      }
    
      changeNativeFlag(): void {
        if (this.showNative) {
          // 创建NativeModule组件挂载
          nativeNode.createNativeRoot(this.rootSlot);
        } else {
          // 销毁NativeModule组件
          nativeNode.destroyNativeRoot();
        }
      }
    
      build() {
        Column() {
          Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI').onClick(() => {
            this.showNative = !this.showNative;
          });
          Row() {
            // ArkTS插入Native组件。
            ContentSlot(this.rootSlot);
          }.layoutWeight(1)
          .id('row\_');
        }
        .width('100%')
        .height('100%');
      }
    }
    
    // native\_init.cpp
    #include "napi/native\_api.h"
    #include "ArkUIMixedRefresh.h"
    #include "NativeEntry.h"
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"createNativeRoot", nullptr, NativeModule::CreateNativeRoot, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"registerCreateMixedRefreshNode", nullptr, NativeModule::ArkUIMixedRefresh::RegisterCreateRefresh, nullptr,
             nullptr, nullptr, napi\_default, nullptr},
            {"registerUpdateMixedRefreshNode", nullptr, NativeModule::ArkUIMixedRefresh::RegisterUpdateRefresh, nullptr,
             nullptr, nullptr, napi\_default, nullptr},
            {"destroyNativeRoot", nullptr, NativeModule::DestroyNativeRoot, nullptr, nullptr, nullptr, napi\_default,
             nullptr}};
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
    
3.  Native侧通过Node-API保存创建和更新函数，用于后续调用。
    
    // 混合模式交互类。
    
    #ifndef MYAPPLICATION\_ARKUIMIXEDREFRESHTEMPLATE\_H
    #define MYAPPLICATION\_ARKUIMIXEDREFRESHTEMPLATE\_H
    
    #include "ArkUIMixedNode.h"
    
    #include <optional>
    
    #include <arkui/native\_node\_napi.h>
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    class ArkUIMixedRefresh : public ArkUIMixedNode {
    public:
        static napi\_value RegisterCreateAndUpdateRefresh(napi\_env env, napi\_callback\_info info);
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIMIXEDREFRESHTEMPLATE\_H
    
    相关实现类说明：
    
    // 混合模式交互类。
    
    #include "ArkUIMixedRefreshTemplate.h"
    
    namespace NativeModule {
    namespace {
    napi\_env g\_env;
    napi\_ref g\_createRefresh;
    napi\_ref g\_updateRefresh;
    } // namespace
    
    napi\_value ArkUIMixedRefresh::RegisterCreateAndUpdateRefresh(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        g\_env = env;
        napi\_ref refer;
        // 创建引用之后保存，防止释放。
        napi\_create\_reference(env, args\[0\], 1, &refer);
    
        g\_createRefresh = refer;
        return nullptr;
    }
    
    } // namespace NativeModule
    
    相关的CMakeLists的配置：
    
    ```cpp
      # CMakeLists.txt
     
      # the minimum version of CMake.
      cmake_minimum_required(VERSION 3.4.1)
      project(testndk)
      
      # optional依赖C++17
      set(CMAKE_CXX_STANDARD 17)
      set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
      
      include_directories(${NATIVERENDER_ROOT_PATH}
                           ${NATIVERENDER_ROOT_PATH}/include)
      
      add_library(entry SHARED NativeEntry.cpp ArkUIMixedRefresh.cpp napi_init.cpp)
      # target_link_libraries(entry PUBLIC libace_napi.z.so, libace_ndk.z.so, libhilog_ndk.z.so)
      
      find_library(
           # Sets the name of the path variable.
           hilog-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           hilog_ndk.z
       )
      
      find_library(
           # Sets the name of the path variable.
           libace-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           ace_ndk.z
       )
      
      find_library(
           # Sets the name of the path variable.
           libnapi-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           ace_napi.z
       )
      
       find_library(
            # Sets the name of the path variable.
            libuv-lib
            uv
        )
      
      target_link_libraries(entry PUBLIC
           ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} )
    ```
    
4.  抽象混合模式下组件的基类，用于通用逻辑管理。
    
    // ArkUIMixedNode.h
    // 混合模式基类。
    
    #ifndef MYAPPLICATION\_ARKUIMIXEDNODE\_H
    #define MYAPPLICATION\_ARKUIMIXEDNODE\_H
    
    #include <js\_native\_api.h>
    #include <js\_native\_api\_types.h>
    
    #include "ArkUIBaseNode.h"
    #include "NativeModule.h"
    
    namespace NativeModule {
    
    // Wrap ArkTS Node
    class ArkUIMixedNode : public ArkUIBaseNode {
    public:
        ArkUIMixedNode(ArkUI\_NodeHandle handle, napi\_env env, napi\_ref componentContent)
            : ArkUIBaseNode(handle), env\_(env), componentContent\_(componentContent) {}
    
        // 在基类析构的时候需要把混合模式在ArkTS侧的对象释放掉。
        ~ArkUIMixedNode() override { napi\_delete\_reference(env\_, componentContent\_); }
    
    protected:
        napi\_env env\_;
        napi\_ref componentContent\_;
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIMIXEDNODE\_H
    
5.  实现Refresh组件的混合模式封装对象。
    
    // ArkUIMixedRefresh.h
    // Refresh混合模式在Native侧的封装对象。
    
    #ifndef MYAPPLICATION\_ARKUIMIXEDREFRESH\_H
    #define MYAPPLICATION\_ARKUIMIXEDREFRESH\_H
    
    #include "ArkUIMixedNode.h"
    #include "ArkUIBaseNode.h"
    
    #include <optional>
    
    #include <arkui/native\_node\_napi.h>
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    // 定义Native侧和ArkTS侧的交互数据结构。
    struct NativeRefreshAttribute {
        std::optional<bool> isRefreshing;
        std::optional<float> width;
        std::optional<float> height;
        std::optional<uint32\_t> backgroundColor;
        std::optional<float> refreshOffset;
        std::optional<bool> pullToRefresh;
        std::function<void()> onRefreshing;
        std::function<void(float)> onOffsetChange;
    };
    
    class ArkUIMixedRefresh : public ArkUIMixedNode {
    public:
        // 调用ArkTS的方法创建Refresh组件。
        static const std::shared\_ptr<ArkUIMixedRefresh> Create(const NativeRefreshAttribute &attribute);
    
        ArkUIMixedRefresh(ArkUI\_NodeHandle handle, ArkUI\_NodeContentHandle contentHandle, napi\_env env,
                          napi\_ref componentContent, napi\_ref nodeContent)
            : ArkUIMixedNode(handle, env, componentContent), contentHandle\_(contentHandle), nodeContent\_(nodeContent) {}
    
        ArkUIMixedRefresh() : ArkUIMixedNode(nullptr, nullptr, nullptr) {}
    
        ~ArkUIMixedRefresh() override { napi\_delete\_reference(env\_, nodeContent\_); } // 释放子节点占位组件插槽对象。
    
        void SetWidth(float width) { attribute\_.width = width; }
    
        void SetHeight(float height) { attribute\_.height = height; }
    
        void SetBackgroundColor(uint32\_t color) { attribute\_.backgroundColor = color; }
    
        void SetRefreshState(bool isRefreshing) { attribute\_.isRefreshing = isRefreshing; }
    
        void SetPullToRefresh(bool pullToRefresh) { attribute\_.pullToRefresh = pullToRefresh; }
    
        void SetRefreshOffset(float offset) { attribute\_.refreshOffset = offset; }
    
        void SetRefreshCallback(const std::function<void()> &callback) { attribute\_.onRefreshing = callback; }
    
        void SetOnOffsetChange(const std::function<void(float)> &callback) { attribute\_.onOffsetChange = callback; }
    
        // 避免频繁跨语言，在Native侧缓存属性事件，批量通知。
        void FlushMixedModeCmd();
    
        static napi\_value RegisterCreateRefresh(napi\_env env, napi\_callback\_info info);
        static napi\_value RegisterUpdateRefresh(napi\_env env, napi\_callback\_info info);
    
    protected:
        void OnAddChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            // 使用NodeContent挂载组件（可以使用ArkTS在Native侧通过ComponentContent的转化对象，也可以是纯Native组件）到ArkTS组件下面。
            OH\_ArkUI\_NodeContent\_AddNode(contentHandle\_, child->GetHandle());
        }
    
        void OnRemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            // 使用NodeContent卸载组件。
            OH\_ArkUI\_NodeContent\_RemoveNode(contentHandle\_, child->GetHandle());
        }
    
        void OnInsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index) override
        {
            // 使用NodeContent插入组件。
            OH\_ArkUI\_NodeContent\_InsertNode(contentHandle\_, child->GetHandle(), index);
        }
    
    private:
        // 使用napi接口创建ArkTS侧的数据结构。
        static napi\_value CreateRefreshAttribute(const NativeRefreshAttribute &attribute, void \*userData);
        
        static void Attribute2Descriptor(const NativeRefreshAttribute &attribute, napi\_property\_descriptor \*desc);
    
        ArkUI\_NodeContentHandle contentHandle\_;
        napi\_ref nodeContent\_;
        NativeRefreshAttribute attribute\_;
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIMIXEDREFRESH\_H
    
    相关实现类说明：
    
    // ArkUIMixedRefresh.cpp
    
    #include "ArkUIMixedRefresh.h"
    #include <hilog/log.h>
    
    namespace NativeModule {
    namespace {
    napi\_env g\_env;
    napi\_ref g\_createRefresh;
    napi\_ref g\_updateRefresh;
    const int REFRESH\_OFFSET\_INDEX0 = 0;
    const int REFRESH\_OFFSET\_INDEX1 = 1;
    const int REFRESH\_OFFSET\_INDEX2 = 2;
    const int REFRESH\_OFFSET\_INDEX3 = 3;
    const int REFRESH\_OFFSET\_INDEX4 = 4;
    const int REFRESH\_OFFSET\_INDEX5 = 5;
    const int REFRESH\_OFFSET\_INDEX6 = 6;
    const int REFRESH\_OFFSET\_INDEX7 = 7;
    } // namespace
    
    void ArkUIMixedRefresh::Attribute2Descriptor(const NativeRefreshAttribute &attribute, napi\_property\_descriptor \*desc)
    {
        if (attribute.width) {
            napi\_value width;
            napi\_create\_double(g\_env, attribute.width.value(), &width);
            desc\[REFRESH\_OFFSET\_INDEX0\].value = width;
        }
        if (attribute.height) {
            napi\_value height;
            napi\_create\_double(g\_env, attribute.height.value(), &height);
            desc\[REFRESH\_OFFSET\_INDEX1\].value = height;
        }
        if (attribute.backgroundColor) {
            napi\_value backgroundColor;
            napi\_create\_uint32(g\_env, attribute.backgroundColor.value(), &backgroundColor);
            desc\[REFRESH\_OFFSET\_INDEX2\].value = backgroundColor;
        }
        if (attribute.pullToRefresh) {
            napi\_value pullToRefresh;
            napi\_create\_int32(g\_env, attribute.pullToRefresh.value(), &pullToRefresh);
            desc\[REFRESH\_OFFSET\_INDEX3\].value = pullToRefresh;
        }
        if (attribute.isRefreshing) {
            napi\_value isRefreshing;
            napi\_create\_int32(g\_env, attribute.isRefreshing.value(), &isRefreshing);
            desc\[REFRESH\_OFFSET\_INDEX4\].value = isRefreshing;
        }
        if (attribute.refreshOffset) {
            napi\_value refreshOffset;
            napi\_create\_double(g\_env, attribute.refreshOffset.value(), &refreshOffset);
            desc\[REFRESH\_OFFSET\_INDEX5\].value = refreshOffset;
        }
        if (attribute.onRefreshing) {
            OH\_LOG\_INFO(LOG\_APP, "onRefreshing start");
            desc\[REFRESH\_OFFSET\_INDEX6\].method = \[\](napi\_env env, napi\_callback\_info info) -> napi\_value {
                OH\_LOG\_INFO(LOG\_APP, "onRefreshing callback");
                size\_t argc = 0;
                napi\_value args\[0\];
                void \*data;
                napi\_get\_cb\_info(env, info, &argc, args, nullptr, &data);
                auto refresh = reinterpret\_cast<ArkUIMixedRefresh \*>(data);
                if (refresh && refresh->attribute\_.onRefreshing) {
                    refresh->attribute\_.onRefreshing();
                }
                return nullptr;
            };
        }
    }
    
    // 使用Napi接口创建与ArkTS侧交互的数据结构，用于Refresh组件的创建和更新。
    napi\_value ArkUIMixedRefresh::CreateRefreshAttribute(const NativeRefreshAttribute &attribute, void \*userData)
    {
        napi\_property\_descriptor desc\[\] = {
            {"width", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"height", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"backgroundColor", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"pullToRefresh", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"isRefreshing", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"refreshOffset", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"onRefreshing", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"onOffsetChange", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
        };
        Attribute2Descriptor(attribute, desc);
        if (attribute.onOffsetChange) {
            OH\_LOG\_INFO(LOG\_APP, "onOffsetChange start");
            desc\[REFRESH\_OFFSET\_INDEX7\].method = \[\](napi\_env env, napi\_callback\_info info) -> napi\_value {
                OH\_LOG\_INFO(LOG\_APP, "onOffsetChange callback");
                size\_t argc = 1;
                napi\_value args\[1\] = {nullptr};
                void \*data;
                napi\_get\_cb\_info(env, info, &argc, args, nullptr, &data);
                double offset = 0.0;
                napi\_get\_value\_double(env, args\[0\], &offset);
                auto refresh = reinterpret\_cast<ArkUIMixedRefresh \*>(data);
                if (refresh && refresh->attribute\_.onOffsetChange) {
                    refresh->attribute\_.onOffsetChange(offset);
                }
                return nullptr;
            };
        }
        napi\_value refreshAttribute = nullptr;
        auto result = napi\_create\_object\_with\_properties(g\_env, &refreshAttribute, sizeof(desc) / sizeof(desc\[0\]), desc);
        if (result != napi\_ok) {
            return nullptr;
        }
        return refreshAttribute;
    }
    
    // 创建ArkTS侧的组件并保存在Native侧的封装对象中。
    const std::shared\_ptr<ArkUIMixedRefresh> ArkUIMixedRefresh::Create(const NativeRefreshAttribute &attribute)
    {
        napi\_handle\_scope scope;
        napi\_open\_handle\_scope(g\_env, &scope);
        auto refresh = std::make\_shared<ArkUIMixedRefresh>();
        auto refreshAttribute = CreateRefreshAttribute(attribute, refresh.get());
        if (refreshAttribute == nullptr) {
            napi\_close\_handle\_scope(g\_env, scope);
            return nullptr;
        }
        napi\_value result = nullptr;
        napi\_value argv\[1\] = {refreshAttribute};
        napi\_value createRefresh = nullptr;
        napi\_get\_reference\_value(g\_env, g\_createRefresh, &createRefresh);
        // 调用ArkTS的Create函数创建ArkTS的ComponentContent。
        napi\_call\_function(g\_env, nullptr, createRefresh, 1, argv, &result);
    
        // 获取ArkTS的Refresh组件。
        napi\_value componentContent = nullptr;
        napi\_get\_named\_property(g\_env, result, "content", &componentContent);
        ArkUI\_NodeHandle handle;
        OH\_ArkUI\_GetNodeHandleFromNapiValue(g\_env, componentContent, &handle);
        // 获取ArkTS的Refresh组件的子组件插槽。
        napi\_value nodeContent = nullptr;
        napi\_get\_named\_property(g\_env, result, "childSlot", &nodeContent);
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(g\_env, nodeContent, &contentHandle);
        // 保存ArkTS的ComponentContent用于防止ArkTS侧对象释放以及后续的更新。
        napi\_ref componentContentRef;
        napi\_create\_reference(g\_env, componentContent, 1, &componentContentRef);
        // 保存ArkTS的NodeContent用于防止ArkTS侧对象释放以及后续的更新。
        napi\_ref nodeContentRef;
        napi\_create\_reference(g\_env, nodeContent, 1, &nodeContentRef);
        // 更新Refresh组件相关参数。
        refresh->handle\_ = handle;
        refresh->env\_ = g\_env;
        refresh->componentContent\_ = componentContentRef;
        refresh->nodeContent\_ = nodeContentRef;
        refresh->contentHandle\_ = contentHandle;
        refresh->attribute\_ = attribute;
        return refresh;
    }
    // 更新函数实现。
    void ArkUIMixedRefresh::FlushMixedModeCmd()
    {
        napi\_handle\_scope scope;
        napi\_open\_handle\_scope(g\_env, &scope);
        // 创建调用ArkTS接口入参。
        auto refreshAttribute = CreateRefreshAttribute(attribute\_, this);
        if (refreshAttribute == nullptr) {
            napi\_close\_handle\_scope(g\_env, scope);
            return;
        }
        // 获取更新接口的剩余两个接口参数。
        napi\_value componentContent = nullptr;
        napi\_get\_reference\_value(g\_env, componentContent\_, &componentContent);
        napi\_value nodeContent = nullptr;
        napi\_get\_reference\_value(g\_env, nodeContent\_, &nodeContent);
    
        napi\_value argv\[3\] = {componentContent, nodeContent, refreshAttribute};
        napi\_value updateRefresh = nullptr;
        napi\_get\_reference\_value(g\_env, g\_updateRefresh, &updateRefresh);
        // 调用ArkTS的Update函数进行更新。
        napi\_value result = nullptr;
        napi\_call\_function(g\_env, nullptr, updateRefresh, sizeof(argv) / sizeof(argv\[0\]), argv, &result);
    }
    
    napi\_value ArkUIMixedRefresh::RegisterCreateRefresh(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        g\_env = env;
        napi\_ref refer;
        napi\_create\_reference(env, args\[0\], 1, &refer);
    
        g\_createRefresh = refer;
        return nullptr;
    }
    
    napi\_value ArkUIMixedRefresh::RegisterUpdateRefresh(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        g\_env = env;
        napi\_ref refer;
        napi\_create\_reference(env, args\[0\], 1, &refer);
    
        g\_updateRefresh = refer;
        return nullptr;
    }
    
    } // namespace NativeModule
    
6.  定时器模块相关简单实现。
    
    // UITimer.h
    // 定时器模块。
    
    #ifndef MYAPPLICATION\_UITIMER\_H
    #define MYAPPLICATION\_UITIMER\_H
    
    #include <hilog/log.h>
    #include <js\_native\_api.h>
    #include <js\_native\_api\_types.h>
    #include <node\_api.h>
    #include <node\_api\_types.h>
    #include <string>
    #include <thread>
    #include <uv.h>
    
    namespace NativeModule {
    
    struct UIData {
        void \*userData = nullptr;
        int32\_t count = 0;
        int32\_t totalCount = 0;
        void (\*func)(void \*userData, int32\_t count) = nullptr;
    };
    
    napi\_threadsafe\_function threadSafeFunction = nullptr;
    
    void CreateNativeTimer(napi\_env env, void \*userData, int32\_t totalCount, void (\*func)(void \*userData, int32\_t count))
    {
        napi\_value name;
        std::string str = "UICallback";
        napi\_create\_string\_utf8(env, str.c\_str(), str.size(), &name);
        // UI主线程回调函数。
        napi\_create\_threadsafe\_function(
            env, nullptr, nullptr, name, 0, 1, nullptr, nullptr, nullptr,
            \[\](napi\_env env, napi\_value value, void \*context, void \*data) {
                auto userdata = reinterpret\_cast<UIData \*>(data);
                userdata->func(userdata->userData, userdata->count);
                delete userdata;
            },
            &threadSafeFunction);
        // 启动定时器，模拟数据变化。
        std::thread timerThread(\[data = userData, totalCount, func\]() {
            uv\_loop\_t \*loop = uv\_loop\_new();
            uv\_timer\_t \*timer = new uv\_timer\_t();
            uv\_timer\_init(loop, timer);
            timer->data = new UIData{data, 0, totalCount, func};
            uint64\_t timeout = 4000;
            uint64\_t repeat = 4000;
            uv\_timer\_start(
                timer,
                \[\](uv\_timer\_t \*handle) {
                    OH\_LOG\_INFO(LOG\_APP, "on timeout");
                    napi\_acquire\_threadsafe\_function(threadSafeFunction);
                    auto \*customData = reinterpret\_cast<UIData \*>(handle->data);
                    // 创建回调数据。
                    auto \*callbackData =
                        new UIData{customData->userData, customData->count, customData->totalCount, customData->func};
                    napi\_call\_threadsafe\_function(threadSafeFunction, callbackData, napi\_tsfn\_blocking);
                    customData->count++;
                    if (customData->count > customData->totalCount) {
                        uv\_timer\_stop(handle);
                        delete handle;
                        delete customData;
                    }
                },
                timeout, repeat);
            uv\_run(loop, UV\_RUN\_DEFAULT);
            uv\_loop\_delete(loop);
        });
        timerThread.detach();
    }
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_UITIMER\_H
    
7.  使用[接入ArkTS页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)章节的页面结构，将Refresh组件作为文本列表的父组件。
    
    // MixedRefreshExample.h
    // 混合模式示例代码。
    
    #ifndef MYAPPLICATION\_MIXEDREFRESHEXAMPLE\_H
    #define MYAPPLICATION\_MIXEDREFRESHEXAMPLE\_H
    
    #include "ArkUIBaseNode.h"
    #include "ArkUIMixedRefresh.h"
    #include "NormalTextListExample.h"
    #include "UITimer.h"
    
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateMixedRefreshList(napi\_env env)
    {
        auto list = CreateTextListExample();
        // 混合模式创建Refresh组件并挂载List组件。
        NativeRefreshAttribute nativeRefreshAttribute{
            .backgroundColor = 0xFF89CFF0, .refreshOffset = 64, .pullToRefresh = true};
        auto refresh = ArkUIMixedRefresh::Create(nativeRefreshAttribute);
        refresh->AddChild(list);
    
        // 设置混合模式下的事件。
        refresh->SetOnOffsetChange(
            \[\](float offset) { OH\_LOG\_INFO(LOG\_APP, "on refresh offset changed: %{public}f", offset); });
        refresh->SetRefreshCallback(\[refreshPtr = refresh.get(), env\]() {
            OH\_LOG\_INFO(LOG\_APP, "on refreshing");
            // 启动定时器，模拟数据获取。
            CreateNativeTimer(env, refreshPtr, 1, \[\](void \*userData, int32\_t count) {
                // 数据获取后关闭刷新。
                auto refresh = reinterpret\_cast<ArkUIMixedRefresh \*>(userData);
                refresh->SetRefreshState(false);
                refresh->FlushMixedModeCmd();
            });
        });
    
        // 更新事件到ArkTS侧。
        refresh->FlushMixedModeCmd();
        return refresh;
    }
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_MIXEDREFRESHEXAMPLE\_H
    
    替换入口组件创建为下拉刷新文本列表。
    
    // NativeEntry.cpp
    
    #include "NativeEntry.h"
    
    #include "ArkUIMixedRefresh.h"
    #include "MixedRefreshExample.h"
    #include "NormalTextListExample.h"
    
    #include <arkui/native\_node\_napi.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api.h>
    #include <uv.h>
    
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
    
        // 创建Refresh文本列表
        auto refresh = CreateMixedRefreshList(env);
    
        // 保持Native侧对象到管理类中，维护生命周期。
        NativeEntry::GetInstance()->SetRootNode(refresh);
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // 从管理类中释放Native侧对象。
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    
    } // namespace NativeModule
    
8.  在Native侧提供Node-API的桥接方法，实现ArkTS侧的NativeNode模块接口。
    
    export const createNativeRoot: (content: Object) => void;
    export const destroyNativeRoot: () => void;
    
    export const registerCreateMixedRefreshNode: (content: Object) => void;
    export const registerUpdateMixedRefreshNode: (content: Object) => void;
