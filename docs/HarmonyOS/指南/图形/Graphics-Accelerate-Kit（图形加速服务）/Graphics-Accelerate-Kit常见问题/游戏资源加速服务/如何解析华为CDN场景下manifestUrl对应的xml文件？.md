---
title: "如何解析华为CDN场景下manifestUrl对应的xml文件？"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-5"
menu_path:
  - "指南"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "Graphics Accelerate Kit常见问题"
  - "游戏资源加速服务"
  - "如何解析华为CDN场景下manifestUrl对应的xml文件？"
captured_at: "2026-04-17T01:36:10.016Z"
---

# 如何解析华为CDN场景下manifestUrl对应的xml文件？

推荐使用[@ifbear/fast-xml-parser](https://ohpm.openharmony.cn/#/cn/detail/@ifbear%2Ffast-xml-parser)。

执行如下命令行，安装依赖。

```typescript
To use as package dependency $ ohpm install @ifbear/fast-xml-parser
```

示例代码：

```typescript
const { XMLParser, XMLBuilder, XMLValidator} = require("fast-xml-parser");

const parser = new XMLParser();
let jObj = parser.parse(XMLdata);
```
