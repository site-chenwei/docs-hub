---
title: "多so相互依赖场景下如何解耦"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-71"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "多so相互依赖场景下如何解耦"
captured_at: "2026-04-17T02:03:02.430Z"
---

# 多so相互依赖场景下如何解耦

**问题现象**

A模块包含a.so，B模块包含b.so。a.so调用b.so的函数，b.so也调用a.so的函数。按照正常编译步骤，无论先编译哪个so，都会编译失败。

**解决措施**

通过dlopen和dlsym接口进行SO编译依赖解耦，将隐式依赖转换为显式依赖。具体示例代码如下：

1.  修改代码和CMakeLists.txt文件，利用Native侧dlopen方法编译出liba.so和libb.so。生成的.so文件位于build/default/intermediates/cmake/default/obj目录下。
    
    （注意一定要用extern "C" {}括起来、不然不能识别到对应的函数导致编译出错）
    
    // a.cpp
    extern "C" {     // Be sure to enclose it with extern 'C' {}
    #include "a.h"
    #include <dlfcn.h>
    #include "stdio.h"
    typedef int (\*FUNC\_SUB)(int, int);
    int add(int a, int b) { return a + b; }
    int getb(char \*path, int a, int b) {       // Path:The sandbox path for passing So files from ArkTS side (note that the path should be passed from ArkTS side, otherwise it may not be found, and the specific code will be listed later)
        void \*handle = dlopen(path, RTLD\_LAZY);  // Open the dynamic link library with path as path
        if (!handle) {
            return 0;
        }
        FUNC\_SUB sub\_func = (FUNC\_SUB)dlsym(handle, "sub"); // Get the function named sub
        int res = sub\_func(a, b);                           // caller function
        dlclose(handle);                                    // Close dynamic link library
        return res;
    }
    }
    
    // a.h
    extern "C" {
    #ifndef DemoSO\_a\_H
    #define DemoSO\_a\_H
    int add(int a, int b);
    int getb(char \*path, int a, int b);
    #endif // DemoSO\_a\_H
    }
    
    // b.cpp
    extern "C" {     // Be sure to enclose it with extern 'C' {}
    #include "b.h"
    #include <dlfcn.h>
    #include "stdio.h"
    typedef int (\*FUNC\_ADD)(int, int);
    int sub(int a, int b) { return a - b; }
    int geta(char \*path, int a, int b) {    // Path: The sandbox path for passing So files from ArkTS side (note that the path should be passed from ArkTS side, otherwise it may not be found, and the specific code will be listed later)
        void \*handle = dlopen(path, RTLD\_LAZY);    // Open the dynamic link library with path as path
        if (!handle) {
            return 0;
        }
        FUNC\_ADD add\_func = (FUNC\_ADD)dlsym(handle, "add");      // Get the function named sub
        int res = add\_func(a, b);                                // caller function
        dlclose(handle);                                         // Close dynamic link library
        return res;
    }
    }
    
    // b.h
    extern "C" {
    #ifndef DemoSO\_b\_H
    #define DemoSO\_b\_H
    int sub(int a, int b);
    int geta(char \*path, int a, int b);
    #endif // DemoSO\_b\_H
    }
    
    \# CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(liba)
    # Compile library liba.so
    add\_library(a SHARED a.cpp)
    target\_link\_libraries(a PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    project(libb)
    # Compile library libb.so
    add\_library(b SHARED b.cpp)
    target\_link\_libraries(b PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
2.  将生成的.so文件（相对路径：build/default/intermediates/cmake/default/obj）移动到libs目录。
    
    移动完成后，目录结构如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/OS305ebMS-axjTsK4Nfcew/zh-cn_image_0000002194158924.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=9B67D06B86E807F26A4C5A72E0BF0CE4A6589706E6C1268C4B4F5D05747CCE6A "点击放大")
    
3.  修改CMakeLists.txt文件，将编译生成的.so文件引入到工程中。
    
    \# CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(DemoSO)
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    # Add libdemoso. so file
    add\_library(demoso SHARED hello.cpp)
    # Add dependency libraries liba.so and libb.so. Please note to include the path, otherwise the corresponding SO library cannot be found
    target\_link\_libraries(demoso PUBLIC libace\_napi.z.so ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../libs/${OHOS\_ARCH}/liba.so ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../libs/${OHOS\_ARCH}/libb.so)
    
    // index.ets
    import testNapi from 'libdemoso.so';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
      private path: string = '';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                this.path = this.getUIContext().getHostContext()!.bundleCodeDir;   // get path
                hilog.info(0x0000, 'testTag', 'Test NAPI 5 + 3 = %{public}d', testNapi.add(5, 3, this.path + '/libs/arm64/liba.so'));  // Call the native side function
                hilog.info(0x0000, 'testTag', 'Test NAPI 5 - 3 = %{public}d', testNapi.sub(5, 3, this.path + '/libs/arm64/libb.so'));
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    // index.d.ts
    export const add: (a: number, b: number, path: string) => number;
    export const sub: (a: number, b: number, path: string) => number;
    
    // hello.cpp
    #include "a.h"
    #include "b.h"
    #include "napi/native\_api.h"
    
    static napi\_value Add(napi\_env env, napi\_callback\_info info) {
        size\_t requireArgc = 3;
        size\_t argc = 3;
        napi\_value args\[3\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_valuetype valuetype0;
        napi\_typeof(env, args\[0\], &valuetype0);
        napi\_valuetype valuetype1;
        napi\_typeof(env, args\[1\], &valuetype1);
        napi\_valuetype valuetype2;
        napi\_typeof(env, args\[2\], &valuetype2);
        int value0;
        napi\_get\_value\_int32(env, args\[0\], &value0);
        int value1;
        napi\_get\_value\_int32(env, args\[1\], &value1);
        char path\[255\];
        size\_t size = 255;
        napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size);
        int res = geta(path, value0, value1);                    // Call the function and pass the sandbox path
        napi\_value sum;
        napi\_create\_int32(env, res, &sum);
        return sum;
    }
    static napi\_value Sub(napi\_env env, napi\_callback\_info info) {
        size\_t requireArgc = 3;
        size\_t argc = 3;
        napi\_value args\[3\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_valuetype valuetype0;
        napi\_typeof(env, args\[0\], &valuetype0);
        napi\_valuetype valuetype1;
        napi\_typeof(env, args\[1\], &valuetype1);
        napi\_valuetype valuetype2;
        napi\_typeof(env, args\[2\], &valuetype2);
        int value0;
        napi\_get\_value\_int32(env, args\[0\], &value0);
        int value1;
        napi\_get\_value\_int32(env, args\[1\], &value1);
        char path\[255\];
        size\_t size = 255;
        napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size);
        int res = getb(path, value0, value1);                 // Call the function and pass the sandbox path
        napi\_value sum;
        napi\_create\_int32(env, res, &sum);
        return sum;
    }
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports) {
        napi\_property\_descriptor desc\[\] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr},
                                           {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi\_default, nullptr}};
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "demoso",
        .nm\_priv = ((void \*)0),
        .reserved = {0},
    };
    extern "C" \_\_attribute\_\_((constructor)) void RegisterDemosoModule(void) { napi\_module\_register(&demoModule); }
