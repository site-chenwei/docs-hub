---
title: "如何在ArkTS侧引用其他三方so库"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-21"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在ArkTS侧引用其他三方so库"
captured_at: "2026-04-17T02:03:01.864Z"
---

# 如何在ArkTS侧引用其他三方so库

**解决措施**

在ArkTS中引用三方库so需要具备以下三个文件：xxx.so、Index.d.ts和oh-package.json5。其中，Index.d.ts和oh-package.json5在C++模板中自带，也可以手动创建。在需要调用的模块根目录下的oh-package.json5中声明so库的根目录路径。然后在代码中使用import语句引用oh-package.json5中声明的依赖名称。此方案仅适用于已经适配了Native的so库。因此，在编译生成so库时，需要实现功能函数并注册其Native侧接口，同时提供对应的Native侧接口声明文件Index.d.ts和配置文件oh-package.json5。

1.  将so文件移动到libs文件夹下对应架构的目录。如果在纯ArkTS工程中，还需将编译三方库时生成的libc++\\\_xxx.so移动到该目录。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/pqHhJZE2R5yVVfn4iwuGPQ/zh-cn_image_0000002194318516.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=DFB5EBB9F4D810BD6D817773A03F9649E51FB1D61D5A914811929D535843C236 "点击放大")
    
2.  在src/main/cpp/types目录下创建新目录，并将Index.d.ts和oh-package.json5文件移动到该目录下。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/NM64YqieSJujieLzCaRP5w/zh-cn_image_0000002229604289.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=B379F5DACC7CBFF33CEB15F0469D9EE58C15AF9A0B170ABBEC7F5CA7E7A29D6E "点击放大")
    
3.  在模块级的oh-package.json5文件中声明该 so 库的根目录路径。
    
    "dependencies": {
      "libimportthirdpartylibraries.so": "file:./src/main/cpp/types/libimportthirdpartylibraries",
      "libapplication.so": "file:./src/main/cpp/types/libapplication"
    },
    
4.  在代码中引用并调用oh-package.json5中声明的依赖。
    
    import testNapi from 'libimportthirdpartylibraries.so';
    import myNapi from 'libapplication.so';
    
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
                console.info(\`MyTest NAPI 2 + 3 = ${myNapi.add(2, 3)}\`);
                console.info(\`MyTest NAPI 2 - 3 = ${testNapi.sub(2, 3)}\`);
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

运行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/bWxOILtdROS52YWKBrl6Dg/zh-cn_image_0000002229758785.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=670CA4908B5B634E960FEA44296FFA009D7C763EC5C431D73392C565E12CA658 "点击放大")

**参考链接**

[在ArkTS侧引用三方so库](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dynamic-link-library#section166546365376)
