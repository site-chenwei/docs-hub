---
title: "在Native侧如何集成三方SO库"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-5"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "在Native侧如何集成三方SO库"
captured_at: "2026-04-17T02:03:01.634Z"
---

# 在Native侧如何集成三方SO库

开发过程可分为两个部分：

1.  系统编译生成so库。
    
    有关如何编译so库，请参考以下链接：
    
    [使用命令行CMake构建NDK工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-cmake)
    
2.  系统集成SO库
    -   方式一：直接集成
    -   方式二：通过dlopen集成

参考代码如下：

1.  系统编译SO库
    
    // sub.h 
    extern "C" {
    double sub(double a, double b); 
    }
    
    // sub.cpp 
    #include <iostream> 
    #include "sub.h" 
    double sub(double a, double b) 
    { 
        return a - b; 
    }
    
    \# CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(libSub)
    # Compile source code 
    add\_library(nativeSub SHARED sub.cpp)
    
2.  系统集成SO库
    -   Native侧直接集成
        
        将上步生成的so库置于entry/libs对应架构的目录下，将头文件放置到cpp目录下。修改CMakeLists.txt，将so库加入工程编译引用。在native侧引入头文件使用。
        
        \# CMakeLists.txt
        # the minimum version of CMake.
        cmake\_minimum\_required(VERSION 3.5.0)
        project(ndk1)
        
        set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
        
        if(DEFINED PACKAGE\_FIND\_FILE)
            include(${PACKAGE\_FIND\_FILE})
        endif()
        
        include\_directories(${NATIVERENDER\_ROOT\_PATH}
                            ${NATIVERENDER\_ROOT\_PATH}/include)
        
        add\_library(entry SHARED napi\_init.cpp)
        target\_link\_libraries(entry PUBLIC libace\_napi.z.so  libhilog\_ndk.z.so)
        target\_link\_libraries(entry PUBLIC ${NATIVERENDER\_ROOT\_PATH}/../../../libs/arm64-v8a/libnativeSub.so)
        
        #include "sub.h"
        
        static napi\_value Sub(napi\_env env, napi\_callback\_info info)
        {
            size\_t requireArgc = 2;
            size\_t argc = 2;
            napi\_value args\[2\] = {nullptr};
            napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
            napi\_valuetype valuetype0;
            napi\_typeof(env, args\[0\], &valuetype0);
            napi\_valuetype valuetype1;
            napi\_typeof(env, args\[1\], &valuetype1);
            double value0;
            napi\_get\_value\_double(env, args\[0\], &value0);
            double value1;
            napi\_get\_value\_double(env, args\[1\], &value1);
            napi\_value sum;
            napi\_create\_double(env, sub(value0, value1), &sum);
            return sum;
        }
        
    -   Native侧通过dlopen方式集成
        
        将上步生成的so库置于entry/libs目录下，通过ArkTS侧传递沙箱路径到native侧，然后直接在native侧使用dlopen方式调用。注意：该方式引用的so库源码在编译时必须使用extern "C" {}包裹起来，即函数必须是使用C编译模式编译的。
        
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
                    let path = this.getUIContext().getHostContext()!.bundleCodeDir; // Get project path
                    hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.subSobyDlOpenSo(2, 3, path + '/libs/arm64/libnativeSub.so')); // Transfer parameter path information to the native side
                  })
              }
              .width('100%')
            }
            .height('100%')
          }
        }
        
        #include <dlfcn.h>
        typedef double (\*Sub)(double, double);
        static napi\_value SubSobyDlOpenSo(napi\_env env, napi\_callback\_info info) {
            size\_t requireArgc = 3;
            size\_t argc = 3;
            napi\_value args\[3\] = {nullptr};
            napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
            double value0;
            napi\_get\_value\_double(env, args\[0\], &value0);    
            double value1;
            napi\_get\_value\_double(env, args\[1\], &value1);
            char\* path = new char\[1024\];
            size\_t size = 1024;
            napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size); // Obtain dynamic library path information
            void \*handle = dlopen(path, RTLD\_LAZY);                     // Open the dynamic link library with path as path
            napi\_value result;
            Sub sub\_func = (Sub)dlsym(handle, "sub");                   // Get the function named sub
            napi\_create\_double(env, sub\_func(value0, value1), &result);
            dlclose(handle);                                            // Finally, close the dynamic library
            return result;
        }
