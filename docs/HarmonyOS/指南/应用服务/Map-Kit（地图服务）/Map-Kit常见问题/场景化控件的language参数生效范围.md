---
title: "场景化控件的language参数生效范围"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-5"
menu_path:
  - "指南"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "Map Kit常见问题"
  - "场景化控件的language参数生效范围"
captured_at: "2026-04-17T01:36:19.038Z"
---

# 场景化控件的language参数生效范围

1.  不传language：UI界面、底图、逆地理结果都是follow系统语言。
    
2.  传language：UI界面和地图follow系统语言，请求云侧的结果根据language获取；不同的接口所支持的语言数据不同，存在不支持语言的接口返回的数据默认使用英文兜底。
