---
title: "如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-13"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象"
captured_at: "2026-04-17T02:03:01.738Z"
---

# 如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象

**问题详情**

ArkTS层创建的ArrayBuffer和Uint8Array对象在Native层无法正确区分。

**解决措施**

1.  使用[napi\_is\_arraybuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-arraybuffer#napi_is_arraybuffer)接口判断数据是否为ArrayBuffer类型，若类型符合则结果为true。
2.  使用[napi\_is\_typedarray](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-array#napi_is_typedarray)接口判断Uint8Array类型数据，若类型符合则结果为true。
