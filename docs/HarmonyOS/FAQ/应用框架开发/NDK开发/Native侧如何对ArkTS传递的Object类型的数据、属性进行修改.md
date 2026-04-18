---
title: "Native侧如何对ArkTS传递的Object类型的数据、属性进行修改"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-62"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何对ArkTS传递的Object类型的数据、属性进行修改"
captured_at: "2026-04-17T02:03:02.324Z"
---

# Native侧如何对ArkTS传递的Object类型的数据、属性进行修改

1.  ArkTS侧调用Native侧方法modifyObject，并传递参数。
    
    import testNapi from 'libentry.so';
    
    
    interface Obj1 {
      obj: Obj2,
      hello: String,
      arr: number\[\],
      typedArray: Uint8Array
    }
    
    
    interface Obj2 {
      str: string
    }
    
    
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
                const typedArr = new Uint8Array(3);
                typedArr\[0\] = 1;
                typedArr\[1\] = 2;
                typedArr\[2\] = 3;
                const obj: Obj1 = {
                  obj: { str: 'obj in obj' },
                  hello: 'world',
                  arr: \[94, 32, 43\],
                  typedArray: typedArr
                }
                console.info(\`Test NAPI modifyObject result is ${JSON.stringify(testNapi.modifyObject(obj))}\`)
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    index.d.ts声明导出接口。
    
    export const modifyObject: (a: object) => object;
    
2.  Native侧解析参数并修改数据、属性
    
    #include "RevArkTSObj.h"
    napi\_value RevArkTSObj::ModifyObject(napi\_env env, napi\_callback\_info info) {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
    
        napi\_value obj = args\[0\];
    
    
        napi\_value obj1;
        napi\_value hello1;
        napi\_value arr1;
        napi\_value typedArray1;
    
    
        napi\_get\_named\_property(env, obj, "obj", &obj1);
        char \*buf = "this is modified";
        napi\_value str1;
        napi\_create\_string\_utf8(env, buf, NAPI\_AUTO\_LENGTH, &str1);
        napi\_set\_named\_property(env, obj1, "str", str1);
        napi\_set\_named\_property(env, obj, "obj", obj1);
    
    
        napi\_create\_string\_utf8(env, "world0", NAPI\_AUTO\_LENGTH, &hello1);
        napi\_set\_named\_property(env, obj, "hello", hello1);
    
    
        napi\_get\_named\_property(env, obj, "arr", &arr1);
        uint32\_t arrLen;
        napi\_get\_array\_length(env, arr1, &arrLen);
        for (int i = 0; i < arrLen; i++) {
            napi\_value tmp;
            napi\_create\_uint32(env, i, &tmp);
            napi\_set\_element(env, arr1, i, tmp);
        }
        napi\_delete\_element(env, arr1, 2, nullptr);
    
    
    
    
        napi\_get\_named\_property(env, obj, "typedArray", &typedArray1);
        bool is\_typedArray;
        if (napi\_ok != napi\_is\_typedarray(env, typedArray1, &is\_typedArray)) {
            return nullptr;
        }
        napi\_typedarray\_type type;
        napi\_value input\_buffer;
        size\_t length;
        size\_t byte\_offset;
        napi\_get\_typedarray\_info(env, typedArray1, &type, &length, nullptr, &input\_buffer, &byte\_offset);
        // Retrieve the basic data buffer data of input\_fuffer and the length byte\_length of the basic data buffer.
        void \*data;
        size\_t byte\_length;
        napi\_get\_arraybuffer\_info(env, input\_buffer, &data, &byte\_length);
        // Create a new ArrayBuffer with a pointer pointing to the underlying data buffer of the ArrayBuffer, denoted as' output \_ptr '
        napi\_value output\_buffer;
        void \*output\_prt = nullptr;
        napi\_create\_arraybuffer(env, byte\_length, &output\_prt, &output\_buffer);
        // Create typedarray using output buffer
        napi\_value output\_array;
        napi\_create\_typedarray(env, type, length, output\_buffer, byte\_offset, &output\_array);
        // Data is composed of consecutive memory locations, where reinterpret\_cast<uint8\_t \*>(data) represents the memory address of its first element.
        // Data is the old arraybuffer data pointer
        uint8\_t \*input\_bytes = reinterpret\_cast<uint8\_t \*>(data) + byte\_offset;
        // Assign the 'outputting \_ptr' pointer to 'outputting: bytes'
        // Output\_ptr is a new array buffer data pointer
        uint8\_t \*output\_bytes = reinterpret\_cast<uint8\_t \*>(output\_prt);
        for (int i = 0; i < length; i++) {
            // Multiply each element of the old arraybuffer data by 2 and assign it to the new arraybuffer data
            output\_bytes\[i\] = input\_bytes\[i\] \* 2;
        }
        // Assign the new typedArray to obj \['typedArray '\]
        napi\_set\_named\_property(env, obj, "typedArray", output\_array);
        return obj;
    }
    
3.  输出结果：
    
    Test NAPI modifyObject result is {"obj":{"str":"this is modified"},"hello":"world0","arr":\[0,1,null\],"typedArray":{"0":2,"1":4,"2":6}}
