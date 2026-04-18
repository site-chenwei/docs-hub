---
title: "@since"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-since"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "@since"
captured_at: "2026-04-17T01:36:48.594Z"
---

# @since

@since标签表示在特定版本中添加了类、方法或其他符号。

#### 语法

@since <versionDescription>

#### 示例

使用 @since：

/\*\*
 \* Provides access to user information.
 \* @since 1.0.1
 \*/
export function UserRecord(): void {}
