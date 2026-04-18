---
title: "Native侧如何获取ArkTS侧的Uint8Array实例"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-52"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何获取ArkTS侧的Uint8Array实例"
captured_at: "2026-04-17T02:03:02.194Z"
---

# Native侧如何获取ArkTS侧的Uint8Array实例

ArkTS Uint8Array的传递方式与其他类型相同。

// ArkTS passes Uint8Array parameter
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
            let temp = new Uint8Array(2);
            temp\[0\] = 1;
            temp\[1\] = 2;
            console.info(\`Pure inputBuffer length: ${temp.length}\`);
            let res = testNapi.uintArr(temp);
            console.info(\`Pure outputBuffer: ${res}\`);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

Native侧使用napi\_get\_typedarray\_info方法获取Uint8Array的详细信息。

// Native side obtains Uint8Array parameter and returns it to ArkTS side 
#include "UintArr.h" 
napi\_value Demo1::UintArr(napi\_env env, napi\_callback\_info info) { 
    size\_t requireArgc = 1; 
    size\_t argc = 1; 
    napi\_value args\[1\] = {nullptr}; 
 
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
 
    napi\_value inputArray = args\[0\]; 
 
    // Get the ArrayBuffer type 
    napi\_typedarray\_type type; 
    napi\_value inArrayBuffer; 
    size\_t byteOffset; 
    size\_t length; 
    napi\_get\_typedarray\_info(env, inputArray, &type, &length, nullptr, &inArrayBuffer, &byteOffset); 
    if (type != napi\_uint8\_array) { 
        return nullptr; 
    } 
     
    // Retrieve information from the ArrayBuffer 
    void \*data = nullptr; 
    size\_t byte\_length; 
    napi\_get\_arraybuffer\_info(env, inArrayBuffer, &data, &byte\_length); 
 
    // Construct an ArrayBuffer and assign a value 
    napi\_value output\_buffer; 
    void \*output\_ptr = nullptr; 
    napi\_create\_arraybuffer(env, byte\_length, &output\_ptr, &output\_buffer); 
    napi\_value outputArray; 
    napi\_create\_typedarray(env, type, length, output\_buffer, byteOffset, &outputArray); 
    uint8\_t \*input\_bytes = (uint8\_t \*)(data) + byteOffset; 
    uint8\_t \*array = (uint8\_t \*)(output\_ptr); 
    for (size\_t idx = 0; idx < length; idx++) { 
        array\[idx\] = 3; 
    } 
 
    return outputArray; 
}

index.d.ts声明接口。

export const uintArr: (a: Uint8Array) => object;
