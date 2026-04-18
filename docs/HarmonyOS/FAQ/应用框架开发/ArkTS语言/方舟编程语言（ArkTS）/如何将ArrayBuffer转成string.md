---
title: "如何将ArrayBuffer转成string"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-90"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "如何将ArrayBuffer转成string"
captured_at: "2026-04-17T02:03:00.389Z"
---

# 如何将ArrayBuffer转成string

可以通过util.TextDecoder.create()方法创建一个实例，再通过[decodeToString()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#decodetostring12)方法进行转换。

let decoder = util.TextDecoder.create('utf-8');
let str = decoder.decodeToString(new Uint8Array(arrayBuffer));

开发者可以将 proArrayBuffer 返回的 ArrayBuffer 类型的数据 arrayBufferVal 转换为字符串。

import { util, buffer } from '@kit.ArkTS';

let blobValue: buffer.Blob = new buffer.Blob(\['name', 'age', 'sex'\]);
let proArrayBuffer = blobValue.arrayBuffer();

proArrayBuffer.then((arrayBufferVal: ArrayBuffer) => {
  let decoder = util.TextDecoder.create('utf-8');
  let stringData = decoder.decodeToString(new Uint8Array(arrayBufferVal));
  console.log('stringData:', stringData);
});
