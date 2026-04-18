---
title: "Video组件错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-video"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "错误码"
  - "UI界面"
  - "Video组件错误码"
captured_at: "2026-04-17T01:48:11.329Z"
---

# Video组件错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/9EO1QuhGSVuj07dZUNCbjA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014811Z&HW-CC-Expire=86400&HW-CC-Sign=5828AD72CFD338855E8DB362230D4BBA3DB95240BAD615727C3B2244615093E1)

以下仅介绍本模块特有错误码，媒体错误码请参考[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 103601 播放器创建失败

**错误信息**

Failed to create the media player.

**错误描述**

播放器创建失败。

**可能原因**

媒体服务不存在，或因内存不足导致创建失败。

**处理步骤**

销毁当前实例，并重新创建，如果重新创建失败，则停止相关操作。

#### 103602 视频资源设置无效

**错误信息**

Not a valid source.

**错误描述**

视频资源设置无效。

**可能原因**

系统找不到资源文件，或资源文件异常。

**处理步骤**

确保资源文件存在且正常，再重新设置Video组件的视频源。
