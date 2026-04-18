---
title: "{@link}"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-link"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "{@link}"
captured_at: "2026-04-17T01:36:48.604Z"
---

# {@link}

{@link} 用于创建指向指定namepath或网页的链接。使用 {@link} 标记时，可以使用不同格式提供链接文本。

#### 语法

-   {@link namepathOrURL}
-   \[link text\]{@link namepathOrURL}
-   {@link namepathOrURL|link text}
-   {@link namepathOrURL link text (after the first space)}

#### 示例

提供链接文本：

/\*\*
 \* See {@link MyClass}.
 \* Also, check out {@link https://www.example.com/cn/ | Example} and
 \* {@link https://www.example.com/cn/ Example}.
 \*/
export function myFunction() {}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/jyGDM7epQ2WT3wtnUrWx2w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=4199B330DF88FFAC4C8399C756C99B664306CBA21F62DDCA6FE945114279C6AA)

若namepath是类名，如例子中的MyClass，用户需要在当前模块中定义该类才能进行正确的跳转。暂不支持对类中属性和方法的跳转。
