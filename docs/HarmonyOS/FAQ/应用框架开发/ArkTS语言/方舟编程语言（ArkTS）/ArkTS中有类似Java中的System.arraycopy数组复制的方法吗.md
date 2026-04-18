---
title: "ArkTS中有类似Java中的System.arraycopy数组复制的方法吗"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-15"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "ArkTS中有类似Java中的System.arraycopy数组复制的方法吗"
captured_at: "2026-04-17T02:02:59.830Z"
---

# ArkTS中有类似Java中的System.arraycopy数组复制的方法吗

可以通过 buffer.concat() 方法，将数组中的内容复制到新的 Buffer 对象中并返回。参考代码如下：

import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from("1234");
let buf2 = buffer.from("abcd");
let buf = buffer.concat(\[buf1, buf2\]);
console.info(buf.toString('hex'));
// Output result:3132333461626364

**参考链接**

[buffer.concat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer#bufferconcat)
