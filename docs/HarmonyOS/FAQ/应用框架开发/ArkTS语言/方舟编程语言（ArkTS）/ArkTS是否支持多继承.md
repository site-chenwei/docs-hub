---
title: "ArkTS是否支持多继承"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-95"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "ArkTS是否支持多继承"
captured_at: "2026-04-17T02:03:00.453Z"
---

# ArkTS是否支持多继承

接口支持多继承，类仅支持单继承。示例如下：

class TestClassA {
  address: string = '';
}

class TestClassB {
  name: string = '';
}

// report errors：Classes can only extend a single class.
// class TestClassC extends TestClassA, TestClassB {
// }

interface AreaSize {
  calculateAreaSize(): number;
}

interface Cal {
  Sub(a: number, b: number): number;
}

interface Area extends AreaSize, Cal {
  areaName: string;
  length: number;
  width: number;
}
