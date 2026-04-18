---
title: "setSessionId加入组网和on启动监听前后设置的区别"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-27"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地数据库管理"
  - "setSessionId加入组网和on启动监听前后设置的区别"
captured_at: "2026-04-17T02:03:08.673Z"
---

# setSessionId加入组网和on启动监听前后设置的区别

开发者应先启动监听再设置setSessionId加入组网，如果顺序相反，在setSessionId和启动监听之间的时间段内发生的数据变化将无法获取。具体影响需根据业务逻辑和代码确定。
