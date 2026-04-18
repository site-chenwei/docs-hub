---
title: "如何解决自定义组件struct内不支持定义成员变量get/set方法的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-50"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决自定义组件struct内不支持定义成员变量get/set方法的问题"
captured_at: "2026-04-17T02:03:21.681Z"
---

# 如何解决自定义组件struct内不支持定义成员变量get/set方法的问题

**问题现象**

运行DevEco Studio的build编译构建功能后，产物中不会生成get/set方法的代码逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/0A_n-g84Qwaj_bHHKq92BQ/zh-cn_image_0000002229758625.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=F533CECA2996FCFA2CFEA7E145CAAB73BE259E487F0C14DC31419A3FD3F6C769)

错误示例如下：

```typescript
@Entry
@Component
struct GetSetDemo {
  private get value(): string {
    return "Hello";
  }
  private set value(value: string) {
    this.value = value;
  }

  build() {
    Row() {
      Column() {
        Text("Hello World")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
    }
  }
}
```

**解决措施**

1.可以使用以下方法替代get方法：

private value: string = "Hello";

2.可以使用以下方式替代 set方法：

this.value = "World"；
