---
title: "Native如何调ArkTS的方法"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-30"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native如何调ArkTS的方法"
captured_at: "2026-04-17T02:03:01.891Z"
---

# Native如何调ArkTS的方法

1\. 在index.d.ts文件中提供 ArkTS 接口方法。

export const nativeCallArkTS: (a: object) => number;

2\. 实现Native侧的NativeCallArkTS接口，代码如下：

static napi\_value NativeCallArkTS(napi\_env env, napi\_callback\_info info) 
{     
    size\_t argc = 1; 
    // Declaring parameter array ARG
    napi\_value args\[1\] = { nullptr }; 
 
    // Retrieve the passed parameters and place them in the parameter array 'args'
    napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr); 
 
    // Create int as an input parameter for ArkTS
    napi\_value argv = nullptr;     
    napi\_create\_int32(env, 2, &argv ); 
 
    // Call the incoming callback and return the result
    napi\_value result = nullptr; 
    napi\_call\_function(env, nullptr, args\[0\], 1, &argv, &result); 
    return result; 
}

3\. 在ArkTS侧，通过nativeModule.nativeCallArkTS()方法传入回调函数。

entry/src/main/ets/pages/Index.ets

// Introduce native capabilities through import.
import nativeModule from 'libentry.so'

@Entry
@Component
struct InvokeArkTSMethod {
  @State message: string = 'Test Node-API nativeCallArkTS result: ';

  build() {
    Row() {
      Column() {
        // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message += nativeModule.nativeCallArkTS((a: number) => {
              return a \* 2;
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

**参考链接**

[Node-API典型使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-scenarios)
