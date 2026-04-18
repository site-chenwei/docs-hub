---
title: "ValuesBucket是否有可动态添加字段的方式"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-48"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地数据库管理"
  - "ValuesBucket是否有可动态添加字段的方式"
captured_at: "2026-04-17T02:03:09.507Z"
---

# ValuesBucket是否有可动态添加字段的方式

**解决措施**

ValuesBucket的实现如下：

export type ValuesBucket = Record<string, ValueType | Uint8Array | null>;

若要动态添加字段，可以参考以下方法。

function set(): void {

  let value : ValuesBucket={};
  let name : string ='NAME';
  value\[name\]= 'cxx';
  value\['AGE'\]=18;
  value\['SALARY'\]=20000;
}
