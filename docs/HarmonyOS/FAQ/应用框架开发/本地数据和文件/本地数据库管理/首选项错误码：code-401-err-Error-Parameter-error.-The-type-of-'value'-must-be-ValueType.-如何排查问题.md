---
title: "首选项错误码：code:\"401\" err: Error: Parameter error. The type of 'value' must be ValueType. 如何排查问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-31"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地数据库管理"
  - "首选项错误码：code:\"401\" err: Error: Parameter error. The type of 'value' must be ValueType. 如何排查问题"
captured_at: "2026-04-17T02:03:08.781Z"
---

# 首选项错误码：code:"401" err: Error: Parameter error. The type of 'value' must be ValueType. 如何排查问题

优先排查value长度。如果value值为字符串类型，请使用UTF-8编码格式。value值可以为空，不为空时长度不超过8192个字节。

Parameter error问题的原因包括：参数值超出有效范围、参数类型不匹配、必填参数缺失等。

-   Mandatory parameters are not specified：未指定强制参数，未传入指定参数。
-   参数类型不正确：参数类型不匹配，需要检查并确保参数类型正确。
-   参数验证失败：参数无效或超出指定范围。
