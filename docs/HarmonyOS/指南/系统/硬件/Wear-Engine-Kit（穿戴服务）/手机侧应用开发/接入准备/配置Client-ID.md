---
title: "配置Client ID"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/configuration_client_id"
menu_path:
  - "指南"
  - "系统"
  - "硬件"
  - "Wear Engine Kit（穿戴服务）"
  - "手机侧应用开发"
  - "接入准备"
  - "配置Client ID"
captured_at: "2026-04-17T01:35:59.585Z"
---

# 配置Client ID

1.  登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/WnLjuYC_STmFErfncG8KDw/zh-cn_image_0000002568899139.png?HW-CC-KV=V1&HW-CC-Date=20260417T013559Z&HW-CC-Expire=86400&HW-CC-Sign=146230246FF450C446109ACDCD4C8F6A123D684B2845D7140A44A6AC9D38CF09)
    
2.  在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：
    
    ```json
    {
      "module": {
        "name": "xxxx",
        "type": "entry",
        "description": "xxxx",
        "mainElement": "xxxx",
        "deviceTypes": [],
        "pages": "xxxx",
        "abilities": [],
        "metadata": [
          // 配置如下信息
          {
            "name": "client_id",
            "value": "xxxxxx"
          }
        ]
      }
    }
    ```
