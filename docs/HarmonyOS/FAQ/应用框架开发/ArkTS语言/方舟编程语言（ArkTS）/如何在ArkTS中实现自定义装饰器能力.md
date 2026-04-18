---
title: "如何在ArkTS中实现自定义装饰器能力"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-78"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "如何在ArkTS中实现自定义装饰器能力"
captured_at: "2026-04-17T02:03:00.254Z"
---

# 如何在ArkTS中实现自定义装饰器能力

ArkTS支持TS5.0之前（如TS4.x及以下版本）的TS装饰器语法。关于装饰器的定义和运行时行为，可以参考[TS官方文档](https://www.typescriptlang.org/docs/handbook/decorators.html)。

注意，如果在.ets文件中定义装饰器，则需要同时满足[从TypeScript到ArkTS的适配规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typescript-to-arkts-migration-guide)，比如不能使用any等。

参考代码如下：

function MyDescriptor(target: Object, key: string, descriptor: PropertyDescriptor) {
  const originalMethod: Function = descriptor.value
  descriptor.value = (...args: Object\[\]) => {
    // Get the name, input parameters, and return value of the decorated method
    console.log(\`Calling ${target.constructor?.name} method ${key} with argument: ${args}\`)
    const result: Object = originalMethod(...args)
    console.log(\`Method ${key} returned: ${result}\`)
    return result
  }
  return descriptor
}

@Entry
@Component
export struct MyDescriptorCom {
  @State message: string = 'Hello World';

  @MyDescriptor
  demoFunc(str: string) {
    return str
  }

  aboutToAppear(): void {
    this.demoFunc('DemoTest')
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/yAITI3L7TsecmGUyxZrK_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020302Z&HW-CC-Expire=86400&HW-CC-Sign=79ED0C3F8C60F8B69843B8B3963B19C737D0C57FC85059CBDF77C316B25C2C93)

由于ArkTS当前运行时限制，当前版本暂不支持同时应用多个自定义装饰器。
