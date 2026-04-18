---
title: "配置Client ID"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id"
menu_path:
  - "指南"
  - "应用服务"
  - "Health Service Kit（运动健康服务）"
  - "开发接入"
  - "开发准备"
  - "配置Client ID"
captured_at: "2026-04-17T01:36:15.226Z"
---

# 配置Client ID

1.  登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5ma7mxOYRgGRZ2s7YjNBkQ/zh-cn_image_0000002568899561.png?HW-CC-KV=V1&HW-CC-Date=20260417T013616Z&HW-CC-Expire=86400&HW-CC-Sign=5F164B4FB4784CA36D0BA69D830F76BC41AA847830F8E4345F9D26850E063A7E)
    
2.  在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：
    
    ```json
    "module": {
      "name": "xxxx",
      "type": "entry",
      "description": "xxxx",
      "mainElement": "xxxx",
      "deviceTypes": [],
      "pages": "xxxx",
      "abilities": [],
      "metadata": [ // 配置如下信息
        {
          "name": "client_id",
          "value": "xxxxxx"
        }
      ]
    }
    ```
