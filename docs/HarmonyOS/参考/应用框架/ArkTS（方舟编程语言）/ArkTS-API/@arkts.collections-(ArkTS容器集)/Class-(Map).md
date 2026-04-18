---
title: "Class (Map)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-map"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkTS（方舟编程语言）"
  - "ArkTS API"
  - "@arkts.collections (ArkTS容器集)"
  - "Class (Map)"
captured_at: "2026-04-17T01:47:51.206Z"
---

# Class (Map)

一种基于键值对存储的非线性数据结构。能够高效地通过唯一键来存取对应的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/aQ86YaZGT96NVa1ohX6OOA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014753Z&HW-CC-Expire=86400&HW-CC-Sign=2452E17B165B4536453F4A1EF9CAE3250EE9A466741D207EA66637C709645ED0)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

文档中存在泛型的使用，涉及以下泛型标记符：

-   K：Key，键
-   V：Value，值

K和V类型都需为[Sendable支持的数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable支持的数据类型)。

**装饰器类型：**@Sendable

#### 导入模块

```ts
import { collections } from '@kit.ArkTS';
```

#### 属性

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| size | number | 是 | 否 | Map的元素个数。 |

#### constructor

constructor(entries?: readonly (readonly \[K, V\])\[\] | null)

构造函数，用于创建ArkTS Map对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| entries | readonly (readonly \[K, V\])\[\] | null | 否 | 键值对数组或其它可迭代对象。默认值为null，创建一个空Map对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Map's constructor cannot be directly invoked. |

**示例：**

```ts
// 正例1：
const myMap = new collections.Map<number, number>();
```

```ts
// 正例2：
const myMap = new collections.Map<number, string>([
  [1, "one"],
  [2, "two"],
  [3, "three"]
]);
```

```ts
// 反例：
@Sendable
class SharedClass {
  constructor() {
  }
}
let sObj = new SharedClass();
const myMap1: collections.Map<number, SharedClass> = new collections.Map<number, SharedClass>([[1, sObj]]);
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
let obj = new Object();
const myMap2: collections.Map<number, Object> = new collections.Map<number, Object>([[1, obj]]);
```

#### constructor

constructor(iterable: Iterable<readonly \[K, V\]>)

创建ArkTS Map对象的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| iterable | Iterable<readonly \[K, V\]> | 是 | 用于构造ArkTS Map的对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Map's constructor cannot be directly invoked. |

**示例：**

```ts
const mapper = new Map([
  ['1', 'a'],
  ['2', 'b'],
]);
let newMap = new collections.Map<string, string>(mapper.entries());
console.info(newMap.get('1')); // 预期输出： a
console.info(newMap.get('2')); // 预期输出： b
```

#### entries

entries(): IterableIterator<\[K, V\]>

返回一个Map迭代器对象，该对象包含了此Map中的每个元素的\[key, value\]对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| IterableIterator<\[K, V\]> | 返回一个Map迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 10200011 | The entries method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
// 例1：
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);

const iterator = myMap.entries();
// Expected output: 0, foo
console.info(iterator.next().value);
// Expected output: 1, bar
console.info(iterator.next().value);
```

```ts
// 例2：
const myMap: collections.Map<number, string> = new collections.Map<number, string>([
  [0, "one"],
  [1, "two"],
  [2, "three"],
  [3, "four"]
]);
// 返回一个myMap迭代器对象，该对象包含了此myMap中的每个元素的[number, string]键值对。
const entriesIter: IterableIterator<[number, string]> = myMap.entries();
// 遍历entriesIter迭代器对象。
for (const entry of entriesIter) {
  if (entry[1].startsWith('t')) {
    myMap.delete(entry[0]);
  }
}
// Expected output: 2
console.info("size:" + myMap.size);
```

#### keys

keys(): IterableIterator<K>

返回一个Map迭代器对象，该对象包含了此Map中每个元素的键。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| IterableIterator<K> | 返回一个Map迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 10200011 | The keys method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);

const iterator = myMap.keys();
// Expected output: 0
console.info(iterator.next().value);
// Expected output: 1
console.info(iterator.next().value);
```

#### values

values(): IterableIterator<V>

返回一个Map迭代器对象，该对象包含此Map中每个元素的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| IterableIterator<V> | 返回一个Map迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 10200011 | The values method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);

const iterator = myMap.values();
// Expected output: "foo"
console.info(iterator.next().value);
// Expected output: "bar"
console.info(iterator.next().value);
```

#### clear

clear(): void

删除该Map中的所有元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 10200011 | The clear method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
const myMap = new collections.Map<number, string>([
  [0, "foo"],
  [1, "bar"]
]);
// Expected output: 2
console.info("size:" + myMap.size);
myMap.clear();
// Expected output: 0
console.info("size:" + myMap.size);
```

#### delete

delete(key: K): boolean

删除该Map中指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | K | 是 | 待删除元素的键。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 如果元素存在并已被删除，则为true；否则该元素不存在，返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The delete method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
const myMap = new collections.Map<string, string>([
  ["hello", "world"],
]);
// Expected result: true
console.info("result:" + myMap.delete("hello"));
// Expected result: false
console.info("result:" + myMap.has("hello"));
// Expected result: false
console.info("result:" + myMap.delete("hello"));
```

#### forEach

forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void

按插入顺序对该Map中的每个键/值对执行一次回调函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callbackFn | (value: V, key: K, map: Map<K, V>) => void | 是 | 回调函数。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | V | 否 | 当前遍历到的元素键值对的值。 |
| key | K | 否 | 当前遍历到的元素键值对的键。 |
| map | Map<K, V> | 否 | 当前map实例对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The forEach method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
// 正例：
new collections.Map<string, number>([
  ['foo', 0],
  ['bar', 1],
  ['baz', 2],
]).forEach((value, key, map) => {
  console.info(`m[${key}] = ${value}`);
});
```

```ts
// 反例：
new collections.Map<string, number>([
  ['foo', 0],
  ['bar', 1],
  ['baz', 2],
]).forEach((value, key, map) => {
  // Throw exception `Concurrent modification error.`
  map.delete(key);
});
```

#### get

get(key: K): V | undefined

返回该Map中的指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | K | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| V | undefined | 与指定键相关联的元素，如果键在Map对象中找不到，则返回undefined。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The get method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
const myMap = new collections.Map<string, string>([
  ["hello", "world"],
]);
// Expected output: "world"
console.info(myMap.get("hello"));
// Expected output: undefined
console.info(myMap.get("hel"));
```

#### has

has(key: K): boolean

判断该Map中是否存在指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | K | 是 | 待查找元素的值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 如果存在指定元素，则返回true，否则返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The has method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
const myMap = new collections.Map<string, string>([
  ["hello", "world"],
]);
// Expected output: true
console.info("result:" + myMap.has("hello"));
// Expected output: false
console.info("result:" + myMap.has("world"));
```

#### set

set(key: K, value: V): Map<K, V>

向该Map添加或更新一个指定的键值对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | K | 是 | 添加或更新指定元素的键。 |
| value | V | 是 | 添加或更新指定元素的值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Map<K, V> | Map对象 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The set method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
// 正例：
const myMap = new collections.Map<string, string>();
myMap.set("foo", "bar");
```

```ts
// 反例：
let obj = new Object();
const myMap: collections.Map<string, Object> = new collections.Map<string, Object>();
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
myMap.set("foo", obj);
```

#### \[Symbol.iterator\]

\[Symbol.iterator\](): IterableIterator<\[K, V\]>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象，并返回该对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/YSUyd_YuTWu0V6XgHHKSVA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014753Z&HW-CC-Expire=86400&HW-CC-Sign=A2EAEC7ED98F25F69EC7BD248F703671AB065F263FEED989D580A1D608A7A48C)

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| IterableIterator<\[K, V\]> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```ts
let map = new collections.Map<number, string>([
    [0, "one"],
    [1, "two"],
    [2, "three"],
    [3, "four"]
]);

let keys = Array.from(map.keys());
for (let key of keys) {
  console.info("key:" + key);
  console.info("value:" + map.get(key));
}
```
