---
title: "如何将Native侧的函数封装到类中导出到ArkTS侧使用"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-15"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何将Native侧的函数封装到类中导出到ArkTS侧使用"
captured_at: "2026-04-17T02:03:01.732Z"
---

# 如何将Native侧的函数封装到类中导出到ArkTS侧使用

**问题详情**

现有一个C++库，提供的接口以类方法形式提供。Native侧可以封装成普通函数的形式供上层调用，也可以保持原有类方法的形式。

**解决措施**

Native侧提供以下类方法供上层调用。

具体代码如下：

1.  Native侧封装类方法。
    
    #include "napi/native\_api.h" 
    #include <string> 
     
    static napi\_value Sub(napi\_env env, napi\_callback\_info info) { 
        size\_t requireArgc = 2; 
        size\_t argc = 2; 
        napi\_value args\[2\] = {nullptr}; 
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
        napi\_valuetype valuetype0; 
        napi\_typeof(env, args\[0\], &valuetype0); 
        napi\_valuetype valuetype1; 
        napi\_typeof(env, args\[1\], &valuetype1); 
        double value0; 
        napi\_get\_value\_double(env, args\[0\], &value0); 
        double value1; 
        napi\_get\_value\_double(env, args\[1\], &value1); 
        napi\_value sub; 
        napi\_create\_double(env, value0 - value1, &sub); 
        return sub; 
    } 
    static napi\_value Sum(napi\_env env, napi\_callback\_info info) { 
        size\_t requireArgc = 2; 
        size\_t argc = 2; 
        napi\_value args\[2\] = {nullptr}; 
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
        napi\_valuetype valuetype0; 
        napi\_typeof(env, args\[0\], &valuetype0); 
        napi\_valuetype valuetype1; 
        napi\_typeof(env, args\[1\], &valuetype1); 
        double value0; 
        napi\_get\_value\_double(env, args\[0\], &value0); 
        double value1; 
        napi\_get\_value\_double(env, args\[1\], &value1); 
        napi\_value sum; 
        napi\_create\_double(env, value0 + value1, &sum); 
        return sum; 
    } 
    napi\_value Constructor(napi\_env env, napi\_callback\_info info) { return nullptr; } 
    EXTERN\_C\_START 
    static napi\_value Init(napi\_env env, napi\_value exports) { 
        std::string class\_name = "TestEntryA"; 
        napi\_property\_descriptor desc\[\] = {{"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi\_static, nullptr}, 
                                           {"sum", nullptr, Sum, nullptr, nullptr, nullptr, napi\_static, nullptr}}; 
        napi\_value defined\_class = nullptr; 
        napi\_define\_class(env, class\_name.c\_str(), class\_name.length(), Constructor, nullptr, 2, desc, &defined\_class); 
        const napi\_property\_descriptor exports\_desc\[\] = { 
            {class\_name.c\_str(), nullptr, nullptr, nullptr, nullptr, defined\_class, napi\_default, nullptr}, 
        }; 
        napi\_define\_properties(env, exports, 2, exports\_desc); 
        return exports; 
    } 
    EXTERN\_C\_END
    
2.  在Index.d.ts文件中导出类及其方法。
    
    export declare class TestEntryA {
      static sub (a: number, b: number) : number;
      static sum (a: number, b: number) : number;
    }
    
3.  在ArkTS侧通过类调用方法。
    
    import { TestEntryA } from 'libfuncencapsulation.so';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Function Encapsulation';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                console.info(\`Test NAPI 2 + 3 = ${TestEntryA.sum(2, 3)}\`);
                console.info(\`Test NAPI 2 - 3 = ${TestEntryA.sub(2, 3)}\`);
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
