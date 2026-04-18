---
title: "Native侧跨HAR/HSP模块接口调用"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-module-reference"
menu_path:
  - "最佳实践"
  - "应用框架"
  - "程序包结构"
  - "Native侧跨HAR/HSP模块接口调用"
captured_at: "2026-04-17T01:54:14.233Z"
---

# Native侧跨HAR/HSP模块接口调用

#### 概述

在大型应用开发中，应用通常会分为多个业务模块，业务模块常会以HSP或HAR包的形式提供SDK能力，这些SDK往往会提供Native接口给HAP模块的Native层直接调用，从而实现应用的复杂功能。而如何在Native侧跨HAR/HSP模块进行接口调用，是开发者经常遇到的问题。本文将介绍Native侧跨HAR/HSP模块调用两种典型场景，包括调用Native方法和调用ArkTS方法，以方便开发者更好的掌握Native侧跨模块调用的能力。

-   [Native侧跨HAR/HSP模块调用Native方法](#section470062115417)
-   [Native侧跨HAR/HSP模块调用ArkTS方法](#section1485574818153)

#### 实现原理

如图1所示，Native侧跨HAR/HSP模块调用原理主要包括以下步骤。

1.  在Module1（HAP）模块中，ArkTS侧通过Node-API调用Native接口。
2.  Module1（HAP）模块Native侧调用Module2（HSP/HAR）模块Native方法。
    1.  被调用方
        1.  在Module2（HSP/HAR）模块中，创建头文件，并在build-profile.json5中配置头文件导出。
        2.  在Module2（HSP/HAR）模块的CMakeLists.txt中进行配置，将源文件配置到so中。
    2.  调用方
        1.  在Module1（HAP）模块的oh-package.json5文件配置引入Module2（HSP/HAR）模块。
        2.  在Module1（HAP）模块的CMakeLists.txt中，配置引入Module2的so文件。
        3.  引入Module2（HSP/HAR）模块的头文件后，就可以调用Module2（HSP/HAR）模块的Native方法。
3.  在Module2（HSP/HAR）模块中，Native侧通过Node-API接口进行模块加载，从而调用ArkTS方法。

**图1** Native侧跨HAR/HSP模块调用原理图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/uxITzdV_RqW_z8ofbr6eNg/zh-cn_image_0000002229450825.png?HW-CC-KV=V1&HW-CC-Date=20260417T015416Z&HW-CC-Expire=86400&HW-CC-Sign=25C53A963A64078C9384B5086E69147CC0E2DC62F38C360974D12186C6DB0D10 "点击放大")

#### Native侧跨HAR/HSP模块调用Native方法

如下图所示，Native侧跨HAR/HSP模块调用Native方法的调用链路为Module1 ArkTS -> Module1 Native -> Module2 Native。在HarmonyOS项目中，Native侧跨模块调用Native方法实际就是C++侧调用，需要配置编译链接依赖。其实现的关键是在Module2（HSP/HAR）模块的build-profile.json5中，配置头文件导出，并在CMakeLists.txt中进行配置，将源文件配置到so中。

**图2** Native侧跨HAR/HSP模块调用Native方法  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/NsziXW7vST-_nxSa7QDGnA/zh-cn_image_0000002229450829.png?HW-CC-KV=V1&HW-CC-Date=20260417T015416Z&HW-CC-Expire=86400&HW-CC-Sign=D93A7BC1755A979FAB26F2BA160C19C0BB52AAAE84139CF005CBEC9251DE3B2A "点击放大")

#### \[h2\]开发流程

Native侧跨HAR/HSP模块调用Native方法时，需要实现Module1（HAP）的ArkTS 侧调用Module1（HSP/HAR）的Native 侧、Module1（HAP）的Native 侧调用Module2（HSP/HAR）的Native 侧。在当前场景下，跨模块调用HAR模块和HSP模块的方式相同，当前以跨模块调用HAR模块为例，详细流程如下所示。

1.  开发者需要创建Module2（HAR）模块staticModule，详细创建流程可以参考[创建库模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har#section643521083015)。

2.  在Module2中新建C++文件napi\_har.cpp，再新建其头文件napi\_har.h，并定义Native方法。
    
    napi\_har.cpp代码如下所示。
    
    #include "napi/native\_api.h"
    #include "napi\_har.h"
    
    double harNativeAdd(double a, double b) {
        return a + b;
    }
    
    napi\_har.h代码如下所示。
    
    // staticModule\\src\\main\\cpp\\napi\_har.h
    #ifndef CROSSMODULEREFERENCE\_NAPI\_HAR\_H
    #define CROSSMODULEREFERENCE\_NAPI\_HAR\_H
    #include <js\_native\_api\_types.h>
    // ...
    double harNativeAdd(double a, double b);
    napi\_value harArkTSAdd(double a, double b);
    #endif //CROSSMODULEREFERENCE\_NAPI\_HAR\_H
    

3.  在Module2中的build-profile.json5中配置头文件导出。如果不做当前headerPath的配置，会导致Module1引用不到Module2的头文件。
    
    {
      "apiType": "stageMode",
      "buildOption": {
        "externalNativeOptions": {
          "path": "./src/main/cpp/CMakeLists.txt",
          "arguments": "",
          "cppFlags": "",
          "abiFilters": \["x86\_64", "arm64-v8a"\]
        },
        "nativeLib": {
          "headerPath": "./src/main/cpp"
        },
        // ...
    }
    

4.  在Module2的CMakeLists.txt中配置将源文件打包到so。
    
    \# staticModule\\src\\main\\cpp\\CMakeLists.txt
    add\_library(add SHARED napi\_init.cpp napi\_har.cpp)
    

5.  在Module2模块创建后，需要在Module1的oh-package.json5文件中配置对应的依赖。如下所示，staticModule为新创建的HAR模块的文件名，static\_module为HAR模块的名称。
    
    {
      "name": "entry",
      "version": "1.0.0",
      "description": "Please describe the basic information.",
      "main": "",
      "author": "",
      "license": "",
      "dependencies": {
        "libentry.so": "file:./src/main/cpp/types/libentry",
        "static\_module": "file:../staticModule",
        // ...
      }
    }
    

6.  在Module1中的CMakeLists.txt中配置so依赖。
    
    \# entry\\src\\main\\cpp\\CMakeLists.txt
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so static\_module::add shared\_module::calc)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/LRe2UlwGTHqNXo7Iv0va7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015416Z&HW-CC-Expire=86400&HW-CC-Sign=C0B70F8E69E624E9EEB6DFEAE96618A8BF8C3FEB4BD2F45E4EDF891E950DDB35)
    
    static\_module::add中第一个参数static\_module是module2的模块名称，第二个参数add是module2编译出来的so名称（不需要带上lib）。默认情况下，module2的模块名称与so名称相同，为了方便说明，在本案例中将so名称修改成了add。
    

7.  在Module1的napi\_init.cpp中导入Module2的头文件napi\_har.h，并调用其Native方法harNativeAdd()。

8.  在Module1的Native侧调用Module2的invokeHarNative()方法。
    
    // entry\\src\\main\\cpp\\napi\_init.cpp
    static napi\_value invokeHarNative(napi\_env env, napi\_callback\_info info)
    {
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
    
        napi\_create\_double(env, harNativeAdd(value0, value1), &sum);
    
        return sum;
    }
    

9.  在Module1的ArkTS侧调用Native侧的invokeHarNative()方法。
    
    Button($r('app.string.call\_har\_native\_method'))
      .fontSize(16)
      .width('100%')
      .margin({ top: 12 })
      .onClick(() => {
        this.getUIContext().getPromptAction().showToast({
          message: 'HarNative method call succeed, result is ' + napi.invokeHarNative(2, 3).toString()
        });
      })
    

#### \[h2\]实现效果

**图3** Native侧调用HAR模块的Native方法  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/0reNYm0tT9CjCOubVxz8LQ/zh-cn_image_0000002229450809.gif?HW-CC-KV=V1&HW-CC-Date=20260417T015416Z&HW-CC-Expire=86400&HW-CC-Sign=48E93531E191C9E4B675297E9C9E3C0F073A8B5C84150818F71D8CEA572DEE77 "点击放大")

#### Native侧跨HAR/HSP模块调用ArkTS方法

如下图所示，Native侧跨HAR/HSP模块调用ArkTS方法是[Native侧跨HAR/HSP模块调用Native方法](#section470062115417)的基础上调用ArkTS方法。其关键是在Module2中获取Module1中的上下文napi\_env，并根据上下文napi\_env加载模块、调用对应的ArkTS方法。

**图4** Native侧跨HAR/HSP模块调用ArkTS方法

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tftOS1mUTX2hIEIpeayV6g/zh-cn_image_0000002194010544.png?HW-CC-KV=V1&HW-CC-Date=20260417T015416Z&HW-CC-Expire=86400&HW-CC-Sign=3B6522379CEB91FC31D13A7D967F688AD5D342E35F460ECC8EC8928E28C84730 "点击放大")

#### \[h2\]开发流程

Native侧跨HAR/HSP模块调用ArkTS方法具体实现方法如下所示。

1.  在完成[Native侧跨HAR/HSP模块调用Native方法](#section470062115417)后，在Module1中新增invokeHarArkTS()方法以准备调用HAR模块的ArkTS方法。
2.  在Module2的Native侧，新增setHarEnv()方法，用以传递napi\_env，并在头文件中进行配置，代码如下所示。
    
    napi\_har.h代码如下所示。
    
    // staticModule\\src\\main\\cpp\\napi\_har.h
    #ifndef CROSSMODULEREFERENCE\_NAPI\_HAR\_H
    #define CROSSMODULEREFERENCE\_NAPI\_HAR\_H
    #include <js\_native\_api\_types.h>
    napi\_env g\_main\_env;
    void setHarEnv(napi\_env env);
    double harNativeAdd(double a, double b);
    napi\_value harArkTSAdd(double a, double b);
    #endif //CROSSMODULEREFERENCE\_NAPI\_HAR\_H
    
    napi\_har.cpp代码如下所示。
    
    // staticModule\\src\\main\\cpp\\napi\_har.cpp
    void setHarEnv(napi\_env env) {
        g\_main\_env = env;
    }
    

3.  在Module1中的napi\_init.cpp中的Init()方法中调用setHarEnv()方法将Module1中的napi\_env传递到Module2中。
    
    // entry\\src\\main\\cpp\\napi\_init.cpp
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "invokeHarNative", nullptr, invokeHarNative, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "invokeHarArkTS", nullptr, invokeHarArkTS, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "invokeHspNative", nullptr, invokeHspNative, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "invokeHspArkTS", nullptr, invokeHspArkTS, nullptr, nullptr, nullptr, napi\_default, nullptr }
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        setHarEnv(env);
         // ...
        return exports;
    }
    EXTERN\_C\_END
    

4.  在Module2中创建ArkTS方法，提供给Module2的Native侧调用。
    
    // staticModule\\src\\main\\ets\\utils\\Util.ets
    export function add(a: number, b: number): number {
      return a + b;
    }
    

5.  在Module2模块的build-profile.json5文件中进行以下配置。
    
    {
      "apiType": "stageMode",
      "buildOption": {
        // ...
        "arkOptions" : {
          "runtimeOnly" : {
            "sources": \[
              "./src/main/ets/utils/Util.ets"
            \]
          }
        }
      },
      // ...
    }
    

6.  在Module2的Native侧调用ArkTS方法，并配置到头文件中。详细步骤如下所示。
    
    1.  通过napi\_load\_module\_with\_info()加载模块，其中，第二个参数是待加载的ets文件的路径，第三个参数是bundleName+模块名。
    2.  使用napi\_get\_named\_property()获取模块导出的add()方法。
    3.  使用napi\_call\_function()调用add()方法。
    
    napi\_har.cpp代码如下所示。
    
    // staticModule\\src\\main\\cpp\\napi\_har.cpp
    napi\_value harArkTSAdd(double a, double b) {
        napi\_env env = g\_main\_env;
        napi\_value module;
        napi\_status status = napi\_load\_module\_with\_info(env, "static\_module/src/main/ets/utils/Util", "com.example.crossmodulereference/entry", &module);
        if (napi\_ok != status) {
            return 0;
        }
        
        napi\_value addFunc;
        napi\_get\_named\_property(env, module, "add", &addFunc);
        
        napi\_value addResult;
        napi\_value argv\[2\] = {nullptr, nullptr};
        napi\_create\_double(env, a, &argv\[0\]);
        napi\_create\_double(env, b, &argv\[1\]);
        napi\_call\_function(env, module, addFunc, 2, argv, &addResult);
        
        return addResult;
    }
    

7.  在module1的Native侧调用module2的harArkTSAdd()方法。
    
    // entry\\src\\main\\cpp\\napi\_init.cpp
    static napi\_value invokeHarArkTS(napi\_env env, napi\_callback\_info info)
    {
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
        
        return harArkTSAdd(value0, value1);
    }
    

8.  在Module1的ArkTS侧调用Native侧的invokeHarArkTS()方法。
    
    Button($r('app.string.call\_har\_ArkTS\_method'))
      .fontSize(16)
      .width('100%')
      .margin({ top: 12 })
      .onClick(() => {
        this.getUIContext().getPromptAction().showToast({ message: 'HarArkTS method call succeed, result is '
          + napi.invokeHarArkTS(2, 3).toString() });
      })
    

#### \[h2\]实现效果

**图5** Native侧调用HAR模块的ArkTS方法  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/gnx4OrwHQiSZfvBK9TUBRQ/zh-cn_image_0000002194010540.gif?HW-CC-KV=V1&HW-CC-Date=20260417T015416Z&HW-CC-Expire=86400&HW-CC-Sign=84F822C303CBE393E7B3A7BD9EDC283EEC219F9FFB950D30AA2E559CFA99928B "点击放大")

#### 常见问题

#### \[h2\]跨HSP模块调用和跨HAR模块调用的区别

HSP模块和HAR模块被调用时，主要的区别在Module2 Native调用Module2 ArkTS中，在调用napi\_load\_module\_with\_info加载模块时的入参有一些区别，其他的流程都是一样的。

1.  被调用模块Module2是HAR

如图所示，编译构建后，HAR模块被打包到各个模块之中，所以其入口模块仍然是HAP模块，napi\_load\_module\_with\_info中第2个参数的模块名称要填HAP模块中oh-package.json5中定义的依赖HAR的名称，而不是HAR模块的实际名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/KRBwMGirTl-tj46DS0QQHA/zh-cn_image_0000002194010548.png?HW-CC-KV=V1&HW-CC-Date=20260417T015416Z&HW-CC-Expire=86400&HW-CC-Sign=7005FD266C55E8D3AB688A5869DB31F008C76A535F46D4A781D6BEE50BFAFBAB "点击放大")

2.  被调用模块Module2是HSP

当被调用模块Module2是HSP，HSP是独立的模块，其入口模块就是HSP本模块，所以napi\_load\_module\_with\_info第2个参数的模块名就是它自己的模块名。

#### \[h2\]是否支持直接依赖HAR模块和HSP模块的三方so（即依赖传递问题）？

当前HAR模块和HSP模块都不支持依赖传递。

#### \[h2\]多包依赖同一so时，最终打包后的so有多少份？

如果多个HAR模块同时依赖commonHar的so，同一模块的同名so在打包后可以通过覆盖策略只保留一份。

如果多个HSP模块同时依赖commonHar的so，在编译构建时，会将依赖的so编译打包到最终的编译产物里，所以每一个.hsp文件都会有一个so。

#### \[h2\]报错找不到HAR/HSP模块的ArkTS文件

**问题现象**

调用HAR/HSP模块的ArkTS文件时，可能会遇到以下报错：

```screen
Error message:Cannot find module 'staticModule/src/main/ets/utils/Util' imported from 'com.xxxx.crossmodulereference/entry'.
```

**可能原因**

可能原因是工程级的build-profile.json5中的useNormalizedOHMUrl设置参数为false。

**解决措施**

在调用模块Module1的build-profile.json5里面添加如下配置。

// ...
  "buildOption": {
    // ...
    "arkOptions" : {
      "runtimeOnly" : {
        "packages": \[
          "static\_module"
        \]
      }
    }
  },
  // ...

#### 示例代码

-   [Native侧跨HAR/HSP模块调用](https://gitcode.com/harmonyos_samples/CrossModuleReference)
