---
title: "animateMotion"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "svg组件"
  - "animateMotion"
captured_at: "2026-04-17T01:48:05.997Z"
---

# animateMotion

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/PoQF5gSRTiu1Jh6V6La6eQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=375087A4373A8C33CF115F7A98AA0BF4DE3677C2F6AA04B0CA942F6282F14D1F)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

路径动效。

#### 权限列表

无

#### 子组件

不支持。

#### 属性

支持animate属性（values不生效）和以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| :-- | :-- | :-- | :-- | :-- |
| keyPoints | string | \- | 是 | 一组关键帧的点位置，每帧的值为对象沿路径的距离比例。功能与animate属性中的values相同。 |
| path | string | \- | 是 | 定义运动的路径，使用与path组件d属性相同的语法。 |
| rotate | \[auto | auto-reverse | <number>\] | auto | 否 | 设置动画对象的旋转方向。 |
