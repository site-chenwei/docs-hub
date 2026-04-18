---
title: "ArkTS侧与Native侧分别如何动态加载SO库"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-4"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "ArkTS侧与Native侧分别如何动态加载SO库"
captured_at: "2026-04-17T02:03:01.558Z"
---

# ArkTS侧与Native侧分别如何动态加载SO库

**解决措施**

1.ArkTS 可以通过动态 import 加载 so 库。

2.Native侧可以使用dlopen动态加载so库。

参考代码如下：

1.ArkTS 通过动态 import 加载 so 库。添加异步函数，在异步函数中通过let testNapi = await import ("libentry.so")实现动态加载so库。

import { hilog } from '@kit.PerformanceAnalysisKit';
// import testNapi from 'libentry.so';

@Entry
@Component
struct LoadSoLibrary {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(async() => {
            let testNapi = await import("libentry.so")            // Load so library
            hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.default.add(2, 3));   // Call library functions by default
            // hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

2.Native侧使用dlopen动态加载so库。

需要调用liba.so中的add函数。

-   将liba.so文件放到libs/arm64-v8a/路径下。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wItUXl0CSgiCUD1jMEoACw/zh-cn_image_0000002229603757.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=B89C9A28A6A0740FB4DAF64D5CA6D5CDACE2862E18D4FEFE63F7496D6E43E170 "点击放大")
    
-   需要在ArkTS侧传递so库路径信息到Native侧。
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import testNapi from 'libentry.so';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                let path = this.getUIContext().getHostContext()!.bundleCodeDir;     // Get project path
                hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.addByLibPath(2, 3, path + '/libs/arm64/liba.so'));   // Transfer parameter path information to the native side
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   在Native侧通过dlopen函数动态加载so库。
    
    #include "napi/native\_api.h" 
    #include <dlfcn.h> 
    typedef double (\*FUNC\_ADD)(int, int); 
    static napi\_value AddByLibPath(napi\_env env, napi\_callback\_info info) { 
        size\_t requireArgc = 3; 
        size\_t argc = 3; 
        napi\_value args\[3\] = {nullptr}; 
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
        double value0; 
        napi\_get\_value\_double(env, args\[0\], &value0); 
        double value1; 
        napi\_get\_value\_double(env, args\[1\], &value1); 
        char path\[255\]; 
        size\_t size = 255; 
        napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size); // Obtain dynamic library path information 
        void \*handle = dlopen(path, RTLD\_LAZY);                     // Open a dynamic link library, The path is "path".  
        dlerror(); 
        FUNC\_ADD add\_func = (FUNC\_ADD)dlsym(handle, "add"); // Retrieve the function named "add" 
        if (dlerror()) { 
            return nullptr; 
        } 
        double res = add\_func(value0, value1);              // Call add and pass the parameter information 
        dlclose(handle);                                    // Close the dynamic library 
        napi\_value sum; 
        napi\_create\_double(env, res, &sum); 
        return sum; 
    } 
    // ...
