---
title: "LazyForEach"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "状态管理与渲染控制"
  - "LazyForEach"
captured_at: "2026-04-17T01:48:00.077Z"
---

# LazyForEach

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Xm_lr6bCT1SxlhZDDPCT-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=F1FCF377BE77AD17356ED23E3C41D879264C09274A17421FFB302BF0B14DD1B3)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[LazyForEach开发者指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)。

在大量子组件的场景下，LazyForEach与缓存列表项、动态预加载、组件复用等方法配合使用，可以进一步提升滑动帧率并降低应用内存占用。最佳实践请参考[优化长列表加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-long-list)。

#### 接口

LazyForEach(dataSource: IDataSource, itemGenerator: (item: any, index: number) => void, keyGenerator?: (item: any, index: number) => string)

LazyForEach从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataSource | [IDataSource](#idatasource) | 是 | LazyForEach数据源，需要开发者实现相关接口。 |
| itemGenerator | (item: any, index: number) => void | 是 | 
子组件生成函数，为数组中的每一个数据项创建一个子组件。

**说明：**

\- item是当前数据项（可选），index是数据项索引值（可选）。

\- itemGenerator的函数体必须使用大括号{...}。

\- itemGenerator每次迭代只能并且必须生成一个子组件。

\- itemGenerator中可以使用if语句，但是必须保证if语句每个分支都会创建一个相同类型的子组件。

 |
| keyGenerator | (item: any, index: number) => string | 否 | 

键值生成函数，用于给数据源中的每一个数据项生成唯一且固定的键值。修改数据源中的一个数据项若不影响其生成的键值，则对应组件不会被更新，否则此处组件就会被重建更新。keyGenerator参数是可选的，但是，为了使开发框架能够更好地识别数组更改并正确更新组件，建议提供。

默认值为空回调函数。

**说明：**

\- item是当前数据项（可选），index是数据项索引值（可选）。

\- keyGenerator缺省时，使用默认的键值生成函数，即(item: Object, index: number) => { return viewId + '-' + index.toString(); }，生成键值仅受索引值index影响（viewId在编译器转换过程中生成，同一个LazyForEach组件内的viewId一致）。

\- 为保证LazyForEach正确、高效地更新子组件，避免渲染结果异常、渲染效率降低等问题，键值应满足以下条件。

1\. 键值具有唯一性，每个数据项对应的键值互不相同。

2\. 键值具有一致性，数据项不变时对应的键值也不变。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/PMLYTWelQw6dNqCJFTuypw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=E6D41F394D38D94988D32DD0A88D1889DA765B6654FA044540B8E1BAF41682DD)

应避免在keyGenerator和itemGenerator函数中执行耗时操作，以此来减少应用滑动时卡顿丢帧问题，最佳实践请参考[主线程耗时操作优化-循环渲染](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread#section4551193714439)。例如，不推荐使用JSON.stringify函数。在复杂的业务场景中，使用JSON.stringify会对item对象进行序列化，该过程会消耗大量时间与计算资源，从而降低页面性能，最佳实践请参考[懒加载优化性能-键值生成规则](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lazyforeach-optimization#section68711519072)。

#### 属性

支持[拖拽排序](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-sorting)属性。

#### IDataSource

LazyForEach的数据源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]totalCount

totalCount(): number

获得数据总数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获得数据总数，由数据源决定实际大小。 |

#### \[h2\]getData

getData(index: number): any

获取索引值index对应的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 获取数据对应的索引值。取值范围是\[0, 数据源长度-1\]。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| any | 获取索引值index对应的数据，由数据源决定具体类型。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/wJy2wlJ2Q1CtXGDCUZJRNg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=675426B8EB95B2EBFC51670EC139B89655468333FEB286259EAB83F57A5138E5)

应避免在getData函数中执行耗时操作，以此来减少应用滑动时卡顿丢帧问题，最佳实践请参考[主线程耗时操作优化-循环渲染](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread#section4551193714439)。

#### \[h2\]registerDataChangeListener

registerDataChangeListener(listener: DataChangeListener): void

注册数据改变的监听器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| listener | [DataChangeListener](#datachangelistener) | 是 | 数据变化监听器。 |

#### \[h2\]unregisterDataChangeListener

unregisterDataChangeListener(listener: DataChangeListener): void

注销数据改变的监听器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| listener | [DataChangeListener](#datachangelistener) | 是 | 数据变化监听器。 |

#### DataChangeListener

数据变化监听器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/E1bwEQz7T_WOtpUEZcvghg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=8D6A61DDC6140EFD9EC1926F856D01F661EF3508E4334F6EF71F18A47A85D0D9)

DataChangeListener除onDatasetChange以外的方法中，当参数包含index且值为负数时，会默认用0来替换。onDatasetChange中，当单个DataOperation参数包含index且值在数据源索引范围之外（DataAddOperation中index可以等于数据源长度），则对应DataOperation不会生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]onDataReloaded

onDataReloaded(): void

通知组件重新加载所有数据。键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件。重新加载数据完成后调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]onDataAdded(deprecated)

onDataAdded(index: number): void

通知组件index的位置有数据添加。添加数据完成后调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/CDu7uFapRBGcXmzmuECbVg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=2ED01D11E0A8E6384C81D9D3882E3D5094845C1BE7ECCF8B101819A3CF9EBAC3)

从API version 7开始支持，从API version 8开始废弃，建议使用[onDataAdd](#ondataadd8)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 
数据添加位置的索引值。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDataMoved(deprecated)

onDataMoved(from: number, to: number): void

通知组件数据有移动。将from和to位置的数据进行交换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/LtpXTxs5S2mNu3tE_aoOuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=A5F0B6685B31D2A526F5C0264B1AD1FA7E190BD1929852782AE0F84E7D70F58B)

-   从API version 7开始支持，从API version 8开始废弃，建议使用[onDataMove](#ondatamove8)替代。
    
-   数据移动前后键值要保持不变，如果键值有变化，应使用删除数据和新增数据接口。数据移动起始位置与数据移动目标位置交换完成后调用。
    

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | number | 是 | 
数据移动起始位置。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |
| to | number | 是 | 

数据移动目标位置。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDataDeleted(deprecated)

onDataDeleted(index: number): void

通知组件删除index位置的数据并刷新LazyForEach的展示内容。删除数据完成后调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/KMNIBkVxROWzs9es6Twrhg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=09C1F5E31846760D375D6FB71BFEA7AAAFEDD2E8CBC2ECCC2EC639419D0A964B)

从API version 7开始支持，从API version 8开始废弃，建议使用[onDataDelete](#ondatadelete8)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 
数据删除位置的索引值。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDataChanged(deprecated)

onDataChanged(index: number): void

通知组件index的位置有数据变化。改变数据完成后调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/H7xMM5ZzTE6PqIFPvfR_rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=3A94B6B5E73928DCF5BF92AF1CBD600C71E2C0C74F75A11AF99223A736067A06)

从API version 7开始支持，从API version 8开始废弃，建议使用[onDataChange](#ondatachange8)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 
数据变化位置的索引值。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDataAdd8+

onDataAdd(index: number): void

通知组件index的位置有数据添加。添加数据完成后调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 
数据添加位置的索引值。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDataMove8+

onDataMove(from: number, to: number): void

通知组件数据有移动。将from和to位置的数据进行交换。数据移动起始位置与数据移动目标位置交换完成后调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/MK1bBrNfQjSQpRXMC-gPIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=1C8DAF92C19997D2EF806F662E722D8E817CCDC809FFD9BA2745F0208B430C46)

数据移动前后键值要保持不变，如果键值有变化，应使用删除数据和新增数据接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | number | 是 | 
数据移动起始位置。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |
| to | number | 是 | 

数据移动目标位置。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDataDelete8+

onDataDelete(index: number): void

通知组件删除index位置的数据并刷新LazyForEach的展示内容。删除数据完成后调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/CNUtqQyjSJKosBRZxQ52qw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=0A2E4D59C6408C7EAD0E597B5D5D1E9BFEE91DD3571A81282EE4D5D7D65FBF42)

需要保证dataSource中的对应数据已经在调用onDataDelete前删除，否则页面渲染将出现未定义的行为。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 
数据删除位置的索引值。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDataChange8+

onDataChange(index: number): void

通知组件index的位置有数据有变化。改变数据完成后调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 
数据变化位置的索引值。取值范围是\[0, 数据源长度-1\]。

小于0时取值为0，大于数据源长度-1时取值为数据源长度-1。

 |

#### \[h2\]onDatasetChange12+

onDatasetChange(dataOperations: DataOperation\[\]): void

进行批量的数据处理后，调用onDatasetChange接口通知组件按照dataOperations刷新组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/iuwoR-PcQHqAZg1QpsU2PA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=2114AEEB1A541F74591D10DA5E1B8E4292C1C2E67A7C13CEF4CABE48DF0206B8)

onDatasetChange接口不能与其他DataChangeListener的更新接口混用。例如，在同一个LazyForEach中，调用过onDataAdd接口后，不能再调用onDatasetChange接口；反之，调用过onDatasetChange接口后，也不能调用onDataAdd等其他更新接口。页面中不同LazyForEach之间互不影响。在同一个onDatasetChange批量处理数据时，如果多个DataOperation操作同一个index，只有第一个DataOperation生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataOperations | [DataOperation](#dataoperation12)\[\] | 是 | 一次处理数据的操作。 |

#### DataOperation12+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/GIv37Oe1ThSxLK9GaV7gbw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=974A2C227F79976383B1DCF4D2C5A64F74AC4BB5D9CDDD224C923919666CCC3B)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]DataAddOperation

添加数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype枚举说明).ADD | 否 | 否 | 数据添加类型。 |
| index | number | 否 | 否 | 插入数据索引值。取值范围是\[0, 数据源长度\]。 |
| count | number | 否 | 是 | 插入数量，默认为1。 |
| key | string | Array<string> | 否 | 是 | 为插入的数据分配键值，默认使用原键值。 |

#### \[h2\]DataDeleteOperation

删除数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype枚举说明).DELETE | 否 | 否 | 数据删除类型。 |
| index | number | 否 | 否 | 起始删除位置索引值。取值范围是\[0, 数据源长度-1\]。 |
| count | number | 否 | 是 | 删除数据数量，默认为1。 |

#### \[h2\]DataChangeOperation

改变数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype枚举说明).CHANGE | 否 | 否 | 数据改变类型。 |
| index | number | 否 | 否 | 改变的数据的索引值。取值范围是\[0, 数据源长度-1\]。 |
| key | string | 否 | 是 | 为改变的数据分配新的键值，默认使用原键值。 |

#### \[h2\]DataMoveOperation

移动数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype枚举说明).MOVE | 否 | 否 | 数据移动类型。 |
| index | [MoveIndex](#moveindex12) | 否 | 否 | 移动位置。取值范围是\[0, 数据源长度-1\]。 |
| key | string | 否 | 是 | 为被移动的数据分配新的键值，默认使用原键值。 |

#### \[h2\]DataExchangeOperation

交换数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype枚举说明).EXCHANGE | 否 | 否 | 数据交换类型。 |
| index | [ExchangeIndex](#exchangeindex12) | 否 | 否 | 交换位置。取值范围是\[0, 数据源长度-1\]。 |
| key | [ExchangeKey](#exchangekey12) | 否 | 是 | 分配新的键值，默认使用原键值。 |

#### \[h2\]DataReloadOperation

重载所有数据操作。当onDatasetChange含有DataOperationType.RELOAD操作时，其余操作全部失效，框架会自己调用keyGenerator进行键值比对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype枚举说明).RELOAD | 否 | 否 | 数据全部重载类型。 |

#### \[h2\]DataOperationType枚举说明

枚举类型，数据操作说明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ADD | add | 数据添加。 |
| DELETE | delete | 数据删除。 |
| CHANGE | change | 数据改变。 |
| MOVE | move | 数据移动。 |
| EXCHANGE | exchange | 数据交换。 |
| RELOAD | reload | 全部数据重载。 |

#### MoveIndex12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| from | number | 否 | 否 | 起始移动位置。取值范围是\[0, 数据源长度-1\]。 |
| to | number | 否 | 否 | 目的移动位置。取值范围是\[0, 数据源长度-1\]。 |

#### ExchangeIndex12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | number | 否 | 否 | 第一个交换位置。取值范围是\[0, 数据源长度-1\]。 |
| end | number | 否 | 否 | 第二个交换位置。取值范围是\[0, 数据源长度-1\]。 |

#### ExchangeKey12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | string | 否 | 否 | 为第一个交换的位置分配新的键值，默认使用原键值。 |
| end | string | 否 | 否 | 为第二个交换的位置分配新的键值，默认使用原键值。 |
