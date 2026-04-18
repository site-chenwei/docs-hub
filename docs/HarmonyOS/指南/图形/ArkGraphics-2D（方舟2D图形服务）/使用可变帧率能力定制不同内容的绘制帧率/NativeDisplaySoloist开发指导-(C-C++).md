---
title: "NativeDisplaySoloist开发指导 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysoloist-native-guidelines"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "使用可变帧率能力定制不同内容的绘制帧率"
  - "NativeDisplaySoloist开发指导 (C/C++)"
captured_at: "2026-04-17T01:36:08.427Z"
---

# NativeDisplaySoloist开发指导 (C/C++)

如果开发者想在独立线程中实现帧率控制的Native侧业务，可以通过DisplaySoloist来实现，如游戏、自绘制UI框架对接等场景。

开发者可以选择多个DisplaySoloist实例共享一个线程，也可以选择每个DisplaySoloist实例独占一个线程。

#### 接口说明

| 函数名称 | 说明 |
| :-- | :-- |
| OH\_DisplaySoloist\* OH\_DisplaySoloist\_Create (bool useExclusiveThread) | 创建一个OH\_DisplaySoloist实例。 |
| OH\_DisplaySoloist\_Destroy (OH\_DisplaySoloist \* displaySoloist) | 销毁一个OH\_DisplaySoloist实例。 |
| OH\_DisplaySoloist\_Start (OH\_DisplaySoloist \* displaySoloist, OH\_DisplaySoloist\_FrameCallback callback, void \* data ) | 设置每帧回调函数，每次VSync信号到来时启动每帧回调。 |
| OH\_DisplaySoloist\_Stop (OH\_DisplaySoloist \* displaySoloist) | 停止请求下一次VSync信号，并停止调用回调函数callback。 |
| OH\_DisplaySoloist\_SetExpectedFrameRateRange (OH\_DisplaySoloist\* displaySoloist, DisplaySoloist\_ExpectedRateRange\* range) | 设置期望帧率范围。 |

详细的接口说明请参考[NativeDisplaySoloist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaysoloist)。

#### 开发示例

本范例是通过Drawing在Native侧实现图形的绘制，通过异步线程设置期望的帧率，再根据帧率进行图形的绘制并将其呈现在NativeWindow上，图形绘制部分可参考[使用Drawing实现图形绘制与显示](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphic-drawing-overview)。

#### \[h2\]添加开发依赖

**添加动态链接库**

CMakeLists.txt中添加以下lib。

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libnative\_drawing.so libnative\_window.so libace\_ndk.z.so libnative\_display\_soloist.so)

**头文件**

#include <ace/xcomponent/native\_interface\_xcomponent.h>
#include <arpa/nameser.h>
#include <bits/alltypes.h>
#include <native\_window/external\_window.h>
#include <native\_drawing/drawing\_bitmap.h>
#include <native\_drawing/drawing\_color.h>
#include <native\_drawing/drawing\_canvas.h>
#include <native\_drawing/drawing\_pen.h>
#include <native\_drawing/drawing\_brush.h>
#include <native\_drawing/drawing\_path.h>
#include <cstdint>
#include <map>
#include <sys/mman.h>
#include <string>
#include "napi/native\_api.h"

#include <native\_display\_soloist/native\_display\_soloist.h>

#### \[h2\]开发步骤

1.  定义ArkTS接口文件XComponentContext.ts，用来对接Native层。
    
    export default interface XComponentContext {
      register(): void;
    
      unregister(): void;
    
      destroy(): void;
    };
    
2.  定义演示页面，包含两个XComponent组件。
    
    import XComponentContext from '../interface/XComponentContext';
    // ...
    
    @Entry
    @Component
    struct Index {
      private xComponentContext1: XComponentContext | undefined = undefined;
      private xComponentContext2: XComponentContext | undefined = undefined;
    
      // ...
    
      build() {
        Column() {
          Row() {
            // ...
    
            XComponent({
              id: 'xcomponentId\_30',
              type: XComponentType.SURFACE,
              libraryname: 'entry'
            })
              .onLoad((xComponentContext) => {
                this.xComponentContext1 = xComponentContext as XComponentContext;
              }).width('640px')
              // ...
          }.height('40%')
    
          Row() {
            // ...
    
            XComponent({
              id: 'xcomponentId\_120',
              type: XComponentType.SURFACE,
              libraryname: 'entry'
            })
              .onLoad((xComponentContext) => {
                this.xComponentContext2 = xComponentContext as XComponentContext;
              }).width('640px')
              // ...
          }.height('40%')
    
          // ...
        }
      }
    }
    
3.  在 Native C++层获取NativeXComponent。建议使用单例模式保存XComponent。此步骤需要在napi\_init的过程中处理。
    
    创建一个PluginManager单例类，用于管理NativeXComponent。
    
    class PluginManager {
    public:
        ~PluginManager();
    
        static PluginManager \*GetInstance();
    
        void SetNativeXComponent(std::string &id, OH\_NativeXComponent \*nativeXComponent);
        SampleXComponent \*GetRender(std::string &id);
        void Export(napi\_env env, napi\_value exports);
    
    private:
        std::unordered\_map<std::string, OH\_NativeXComponent \*> nativeXComponentMap\_;
        std::unordered\_map<std::string, SampleXComponent \*> pluginRenderMap\_;
    };
    
    SampleXComponent类会在后面的绘制图形中创建。
    
    void PluginManager::Export(napi\_env env, napi\_value exports)
    {
        nativeXComponentMap\_.clear();
        pluginRenderMap\_.clear();
        if ((env == nullptr) || (exports == nullptr)) {
            SAMPLE\_LOGE("Export: env or exports is null");
            return;
        }
    
        napi\_value exportInstance = nullptr;
        if (napi\_get\_named\_property(env, exports, OH\_NATIVE\_XCOMPONENT\_OBJ, &exportInstance) != napi\_ok) {
            SAMPLE\_LOGE("Export: napi\_get\_named\_property fail");
            return;
        }
    
        OH\_NativeXComponent \*nativeXComponent = nullptr;
        if (napi\_unwrap(env, exportInstance, reinterpret\_cast<void \*\*>(&nativeXComponent)) != napi\_ok) {
            SAMPLE\_LOGE("Export: napi\_unwrap fail");
            return;
        }
    
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {'\\0'};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        if (OH\_NativeXComponent\_GetXComponentId(nativeXComponent, idStr, &idSize) != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            SAMPLE\_LOGE("Export: OH\_NativeXComponent\_GetXComponentId fail");
            return;
        }
    
        std::string id(idStr);
        auto context = PluginManager::GetInstance();
        if ((context != nullptr) && (nativeXComponent != nullptr)) {
            context->SetNativeXComponent(id, nativeXComponent);
            auto render = context->GetRender(id);
            if (render != nullptr) {
                render->RegisterCallback(nativeXComponent);
                render->Export(env, exports);
            } else {
                SAMPLE\_LOGE("render is nullptr");
            }
        }
    }
    
4.  Native层配置帧率和注册回调函数。
    
    定义每帧回调函数内容。
    
    static void TestCallback(long long timestamp, long long targetTimestamp, void \*data)
    {
        // ...
        OH\_NativeXComponent \*component = nullptr;
        component = static\_cast<OH\_NativeXComponent \*>(data);
        if (component == nullptr) {
            SAMPLE\_LOGE("TestCallback: component is null");
            return;
        }
    
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {'\\0'};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        if (OH\_NativeXComponent\_GetXComponentId(component, idStr, &idSize) != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            SAMPLE\_LOGE("TestCallback: Unable to get XComponent id");
            return;
        }
    
        std::string id(idStr);
        auto render = SampleXComponent::GetInstance(id);
        OHNativeWindow \*nativeWindow = render->GetNativeWindow();
        uint64\_t width;
        uint64\_t height;
    
        int32\_t xSize = OH\_NativeXComponent\_GetXComponentSize(component, nativeWindow, &width, &height);
        if ((xSize == OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) && (render != nullptr)) {
            render->Prepare();
            render->Create();
            if (id == "xcomponentId\_30") {
                int offset = 16;
                render->ConstructPath(offset, offset, render->defaultOffsetY);
            }
            if (id == "xcomponentId\_120") {
                int offset = 4;
                render->ConstructPath(offset, offset, render->defaultOffsetY);
            }
            // ...
        }
    }
    
    使用DisplaySoloist接口配置帧率和注册每帧回调函数。如果使用OH\_DisplaySoloist\_Create创建DisplaySoloist实例时传入的参数useExclusiveThread为true，则OH\_DisplaySoloist\_FrameCallback以独占线程方式执行，否则OH\_DisplaySoloist\_FrameCallback以共享线程方式执行。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/ksiZ4LdcRfy7njpanJErXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013608Z&HW-CC-Expire=86400&HW-CC-Sign=A36004FEB3627555FF648543A34CD02954C7A0D65014C5768BDD7C6F2C1DB6DA)
    
    -   实例在调用NapiRegister后，在不需要进行帧率控制时，应进行NapiUnregister操作，避免内存泄漏问题。
    -   在页面跳转时，应进行NapiUnregister和NapiDestroy操作，避免内存泄漏问题。
    
    static std::unordered\_map<std::string, OH\_DisplaySoloist \*> g\_displaySync;
    
    // ...
    
    void ExecuteDisplaySoloist(std::string id, DisplaySoloist\_ExpectedRateRange range, bool useExclusiveThread,
                               OH\_NativeXComponent \*nativeXComponent)
    {
        OH\_DisplaySoloist \*nativeDisplaySoloist = nullptr;
        if (g\_displaySync.find(id) == g\_displaySync.end()) {
            g\_displaySync\[id\] = OH\_DisplaySoloist\_Create(useExclusiveThread);
        }
        nativeDisplaySoloist = g\_displaySync\[id\];
        OH\_DisplaySoloist\_SetExpectedFrameRateRange(nativeDisplaySoloist, &range);
        OH\_DisplaySoloist\_Start(nativeDisplaySoloist, TestCallback, nativeXComponent);
    }
    
    napi\_value SampleXComponent::NapiRegister(napi\_env env, napi\_callback\_info info)
    {
        // ...
    
        napi\_value thisArg;
        if (napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisArg, nullptr) != napi\_ok) {
            SAMPLE\_LOGE("NapiRegister: napi\_get\_cb\_info fail");
            return nullptr;
        }
    
        napi\_value exportInstance;
        if (napi\_get\_named\_property(env, thisArg, OH\_NATIVE\_XCOMPONENT\_OBJ, &exportInstance) != napi\_ok) {
            SAMPLE\_LOGE("NapiRegister: napi\_get\_named\_property fail");
            return nullptr;
        }
    
        OH\_NativeXComponent \*nativeXComponent = nullptr;
        if (napi\_unwrap(env, exportInstance, reinterpret\_cast<void \*\*>(&nativeXComponent)) != napi\_ok) {
            SAMPLE\_LOGE("NapiRegister: napi\_unwrap fail");
            return nullptr;
        }
    
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {'\\0'};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        if (OH\_NativeXComponent\_GetXComponentId(nativeXComponent, idStr, &idSize) != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            SAMPLE\_LOGE("NapiRegister: Unable to get XComponent id");
            return nullptr;
        }
        SAMPLE\_LOGI("RegisterID = %{public}s", idStr);
        std::string id(idStr);
        SampleXComponent \*render = SampleXComponent().GetInstance(id);
        if (render != nullptr) {
            DisplaySoloist\_ExpectedRateRange range;
            bool useExclusiveThread = false;
            if (id == "xcomponentId30") {
                range = {30, 120, 30};
            }
    
            if (id == "xcomponentId120") {
                range = {30, 120, 120};
            }
            ExecuteDisplaySoloist(id, range, useExclusiveThread, nativeXComponent);
        }
        return nullptr;
    }
    
    napi\_value SampleXComponent::NapiUnregister(napi\_env env, napi\_callback\_info info)
    {
        // ...
            OH\_DisplaySoloist\_Stop(g\_displaySync\[id\]);
            // ...
    }
    
    napi\_value SampleXComponent::NapiDestroy(napi\_env env, napi\_callback\_info info)
    {
        // ...
            OH\_DisplaySoloist\_Destroy(g\_displaySync\[id\]);
            g\_displaySync.erase(id);
            // ...
    }
    
    // ...
    
    void SampleXComponent::Export(napi\_env env, napi\_value exports)
    {
        if ((env == nullptr) || (exports == nullptr)) {
            SAMPLE\_LOGE("Export: env or exports is null");
            return;
        }
        napi\_property\_descriptor desc\[\] = {
            {"register", nullptr, SampleXComponent::NapiRegister, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"unregister", nullptr, SampleXComponent::NapiUnregister, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"destroy", nullptr, SampleXComponent::NapiDestroy, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    
        if (napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc) != napi\_ok) {
            SAMPLE\_LOGE("Export: napi\_define\_properties failed");
        }
    }
    
5.  TS层注册和取消注册每帧回调，销毁OH\_DisplaySoloist实例。
    
    aboutToDisappear(): void {
      // ...
      if (this.xComponentContext1) {
        this.xComponentContext1.unregister();
        this.xComponentContext1.destroy();
      }
      if (this.xComponentContext2) {
        this.xComponentContext2.unregister();
        this.xComponentContext2.destroy();
      }
    }
    
    // ...
    
        Row() {
          Button('Start')
            .id('Start')
            .fontSize(14)
            .fontWeight(500)
            .margin({ bottom: 20, right: 6, left: 6 })
            .onClick(() => {
              if (this.xComponentContext1) {
                this.xComponentContext1.register();
              }
              if (this.xComponentContext2) {
                this.xComponentContext2.register();
              }
            })
            .width('30%')
            .height(40)
            .shadow(ShadowStyle.OUTER\_DEFAULT\_LG)
    
          Button('Stop')
            .id('Stop')
            .fontSize(14)
            .fontWeight(500)
            .margin({ bottom: 20, left: 6 })
            .onClick(() => {
              if (this.xComponentContext1) {
                this.xComponentContext1.unregister();
              }
              if (this.xComponentContext2) {
                this.xComponentContext2.unregister();
              }
            })
            .width('30%')
            .height(40)
            .shadow(ShadowStyle.OUTER\_DEFAULT\_LG)
        }
