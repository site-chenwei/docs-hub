---
title: "Canvas组件错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-canvas"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "错误码"
  - "UI界面"
  - "Canvas组件错误码"
captured_at: "2026-04-17T01:48:11.106Z"
---

# Canvas组件错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/LwIh286TRSOBtUPvsoP9tQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014811Z&HW-CC-Expire=86400&HW-CC-Sign=E19306C498E729D701FAE943600E7BE9E44702674C5B4959313555D9F2B57D2F)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 103701 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

参考报错接口的说明。

**处理步骤**

传入正确的参数。

#### 103702 绘制上下文未绑定Canvas组件

**错误信息**

The drawingContext is not bound to a canvas component.

**错误描述**

当前绘制上下文未绑定任何Canvas组件。

**可能原因**

当前绘制上下文没有绑定任何Canvas组件。

**处理步骤**

将绘制上下文绑定至一个Canvas组件后再调用[getContext2DFromDrawingContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#getcontext2dfromdrawingcontext23)方法。

#### 103704 OffscreenCanvas已经下树

**错误信息**

OffscreenCanvas object is detached.

**错误描述**

[OffscreenCanvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-offscreencanvas)已经下树。

**可能原因**

OffscreenCanvas已经下树，不支持当前操作。

**处理步骤**

将当前节点挂载到树上，再执行当前操作。
