---
title: "Subpass Shading"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-subpass-shading"
menu_path:
  - "指南"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "Subpass Shading"
captured_at: "2026-04-17T01:36:10.407Z"
---

# Subpass Shading

随着游戏场景的复杂化，越来越多的光照效果被应用到游戏场景中，随之也带来大量的光照计算以及带宽消耗。目前通过Tile-Based Deferred Rendering（TBDR）和Forward+等方法可以解决大量光照的渲染时间消耗，但是大量带宽的占用问题还是没有解决，Subpass Shading能力主要减少计算过程中的读写从而减少带宽的占用。

下图说明Subpass Shading节省渲染通道1和Compute Pass从Device memory上面的一次读写带宽。

**图1** Forward+读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/qW30xAVtQcKaO7faMMV76g/zh-cn_image_0000002568899389.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=0A695EA8F4C5FA1D181B4A8B4BA7D48024B7EED91B313F534C06A93D5762A0E0)

**图2** Subpass Shading读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/GiKPFc0DRH6tgnQDygLJhA/zh-cn_image_0000002538019684.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=1D804EAE3606C6F0A93CBB7981855E0C7D8FB6CCE05E41D0CB5A727B8C3FCBA4)

#### 约束与限制

支持的设备类型：Phone，从5.0.2(14)版本开始，新增支持Tablet、PC/2in1设备，从5.1.0(18)版本开始新增支持TV设备。

#### 接口说明

通过Vulkan扩展接口[VK\_HUAWEI\_subpass\_shading](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_HUAWEI_subpass_shading.html)提供Subpass Shading API，该扩展支持在Subpass中使用Compute Shader，并在Compute Shader中使用SubpassLoad从Tile buffer中直接读取数据，可用于降低DDR带宽，适用于TBDR和Forward+管线。

Subpass Shading能力具体使用请参见[Demo（GPU加速引擎-Subpass Shading）](https://gitcode.com/harmonyos_samples/xengine-samplecode-subpass-shading-demo-cpp)。
