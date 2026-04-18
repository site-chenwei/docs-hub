---
title: "如何将Map转换为JSON字符串"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-86"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "如何将Map转换为JSON字符串"
captured_at: "2026-04-17T02:03:00.348Z"
---

# 如何将Map转换为JSON字符串

将Map转换为Record后，再通过JSON.stringify()方法转换为JSON字符串。示例如下：

let mapSource = new Map<string, string>();
mapSource.set('name', 'name1');
mapSource.set('width', '100');
mapSource.set('height', '50');

let jsonObject: Record<string, Object> = {};
mapSource.forEach((value, key) => {
  if (key !== undefined && value !== undefined) {
    jsonObject\[key\] = value;
  }
})
let jsonInfo: string = JSON.stringify(jsonObject);

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('Map to JSON')
        .onClick(() => {
          console.log('jsonInfo:', jsonInfo); // jsonInfo: {"name":"name1","width":"100","height":"50"}
        })
    }
  }
}
