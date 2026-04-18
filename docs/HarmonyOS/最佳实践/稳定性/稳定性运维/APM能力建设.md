---
title: "APM能力建设"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-operate-apm"
menu_path:
  - "最佳实践"
  - "稳定性"
  - "稳定性运维"
  - "APM能力建设"
captured_at: "2026-04-17T01:54:20.025Z"
---

# APM能力建设

APM作为应用性能管理平台，可线上监控应用质量。系统提供采集质量数据的能力，开发者可以收集这类数据构建APM平台。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/XF6ej_mmTRO34aJ-ddH6dA/zh-cn_image_0000002404125277.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=5D0F5DDCB2983C91C0BBE42645DB5C6835C4BCB109785C3BE0B78FF708711AAD "点击放大")

本文主要介绍如何通过HiAppEvent订阅接口采集系统事件。其中，系统事件是指应用运行期间，应用进程发生的性能、功耗、稳定性等故障，HiAppEvent会将这些故障通过事件返回给开发者。

#### HiAppEvent系统事件订阅能力

当前HiAppEvent支持的各种系统事件介绍、检测原理、事件参数对象params包含的字段说明，具体请查阅各种系统事件的介绍。

[崩溃事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events)

[应用冻屏事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events)

[资源泄漏事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events)

[地址越界事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events)

[主线程超时事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events)

[任务执行超时事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events)

[应用查杀事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events)

[启动耗时事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-launch-event)

[滑动丢帧事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-scroll-jank-event)

[CPU高负载事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-cpu-usage-high-event)

[24h功耗器件分解统计事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-battery-usage-event)

[音频卡顿事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-audio-jank-event)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/F6xRNS_uT5qxF9_vficuCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=D41835EC5FAF91ADFBED0419B1B6A26B8132FE5BC49B6E2480309F6BBF0CB292)

external\_log返回的路径是沙箱目录，非真实物理路径，应用有权限访问自己的沙箱目录，参考[应用沙箱目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)。external\_log日志空间受限，应用处理完日志文件后请及时删除。

#### \[h2\]系统事件订阅机制

应用调用HiAppEvent接口订阅系统事件，并生成一个共享目录。当应用进程发生故障，DFX系统抓取相关信息生成事件和日志，分享到应用共享目录。HiAppEvent监听到有事件发生回调给应用。

原理如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/tDkdu7JGQRSvLqCklEv4Dg/zh-cn_image_0000002382129722.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=ED69F344E3826C02C25B0CBC559B54382A90F469695AA945F7583C20167BFA6A "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8U9HnOJcRKCu87gR6OJxeg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=EC8200FE5FB111F706C63B4A712BB050C39515594ADF1737F061F29B05CEBBCC)

发生崩溃、卡死和地址越界故障时，应用会退出，所以需要在应用下次启动时才能获取到相应系统事件。

#### HiAppEvent系统事件订阅方法

#### \[h2\]订阅接口使用方法

HiAppEvent提供addWatcher()接口可以订阅系统事件，支持三种订阅方式。

方式一：设置回调条件triggerCondition，实现onTrigger()回调，满足回调条件自动触发回调。

方式二：未设置回调条件参数，使用事件订阅返回的holder对象主动获取系统事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/kT1Wj1AHQpqYRGReVXTNFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=C5F1A68DAD89340BCBEC6A508BAA5F5CA515D1F2D4FEF8E57525AD2447A55E02)

主动获取系统事件，由于系统事件可能未生成或者日志信息未抓取完成，可能查询为空，可以尝试多次调用查询接口。

方式三：实现onReceive()回调，监听到订阅的事件生成后实时回调。

ArkTS接口参考[hiAppEvent.addWatcher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent#hiappeventaddwatcher)，C/C++接口参考[OH\_HiAppEvent\_AddWatcher()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h#oh_hiappevent_addwatcher)。

#### \[h2\]参数扩展接口使用方法

HiAppEvent提供setEventParam()接口可以在系统事件中添加自定义参数，当前支持在崩溃和卡死事件中增加自定义参数。ArkTS接口参考[hiAppEvent.setEventParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent#hiappeventseteventparam12)。

使用接口完成参数键值对赋值。以在订阅崩溃事件中添加自定义参数为例，ArkTS接口示例代码如下：

```screen
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let params: Record<string, hiAppEvent.ParamType> = {
  "test_data": 100,
};
/* 添加崩溃事件的自定义参数 */
// domain.OS表示操作系统级事件
// event.APP_CRASH指定订阅崩溃事件类型
hiAppEvent.setEventParam(params, hiAppEvent.domain.OS, hiAppEvent.event.APP_CRASH).then(() => {
  hilog.info(0x0000, 'testTag', `HiAppEvent success to set event param`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `HiAppEvent code: ${err.code}, message: ${err.message}`);
});
```

#### HiAppEvent系统事件订阅方案设计

以崩溃采集为例，可参考如下设计：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/QhAfFGiKR-q27XjDO8WfAg/zh-cn_image_0000002404045473.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=5E8F367ADB26E8AC1F477713C14F95F297D7D895A06991767AF83B6F0E5EF28C)

1.  APM代码早于业务代码。
2.  应用启动阶段注册ErrorManager，可以捕获JS异常，发生JsError崩溃时进程不会退出。参考[如何使用ErrorManager捕获异常](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs-V5/faqs-arkts-81-V5)。
3.  在ErrorManager回调中执行takeNext接口获取JsError崩溃事件。
4.  应用发生CPP Crash异常退出，下次启动获取NativeCrash崩溃事件。
5.  获取的崩溃信息可以持久化存储，上传后再删除，避免上传失败导致数据丢失。
6.  日志管理，external\_log日志处理后（比如上传后）及时清理。
