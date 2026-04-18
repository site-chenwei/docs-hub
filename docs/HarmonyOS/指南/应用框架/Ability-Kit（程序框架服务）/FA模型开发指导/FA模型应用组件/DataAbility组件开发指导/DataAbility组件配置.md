---
title: "DataAbility组件配置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-configuration"
menu_path:
  - "指南"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "FA模型开发指导"
  - "FA模型应用组件"
  - "DataAbility组件开发指导"
  - "DataAbility组件配置"
captured_at: "2026-04-17T01:35:32.742Z"
---

# DataAbility组件配置

#### URI介绍

DataAbility的提供方和使用方都通过URI（Uniform Resource Identifier）来标识一个具体的数据，例如数据库中的某个表或磁盘上的某个文件。此处的URI仍基于URI通用标准，格式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/-VoWFLUSSnWC6UZsjFt_yQ/zh-cn_image_0000002538018428.png?HW-CC-KV=V1&HW-CC-Date=20260417T013533Z&HW-CC-Expire=86400&HW-CC-Sign=4280C948FFEBEF380CBF79D685E83825D020D2C0CAA123D0D6E4AB3822F077CF)

-   scheme：协议方案名，固定为"dataability"，代表Data Ability所使用的协议类型。
    
-   authority：设备ID。如果为跨设备场景，则为目标设备的ID；如果为本地设备场景，则不需要填写。
    
-   path：资源的路径信息，代表特定资源的位置信息。
    
-   query：查询参数。
    
-   fragment：可以用于指示要访问的子资源。
    

URI示例：

-   跨设备场景：dataability://device\_id/com.domainname.dataability.persondata/person/10
    
-   本地设备：dataability:///com.domainname.dataability.persondata/person/1
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/g5LJJYQlSKCsNYafUqqgIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013533Z&HW-CC-Expire=86400&HW-CC-Sign=E5C6CBE3DB53B1BEEF5BF07C5DC60DBC377F2D78F9D29156B636BB49A3FB03FB)

本地设备的"device\_id"字段为空，因此在"dataability:"后面有三个"/"。

#### 部分配置项介绍

与PageAbility类似，DataAbility的相关配置在config.json配置文件的"module"对象的"abilities"对象中，与PageAbility的区别在于"type"属性及"uri"属性。

**表1** DataAbility的部分配置项说明

| Json重要字段 | 备注说明 |
| :-- | :-- |
| "name" | Ability名称。 |
| "type" | UIAbility类型，DataAbility的类型为"data"。 |
| "uri" | 通信使用的URI。 |
| "visible" | 对其他应用是否可见，设置为true时，DataAbility才能与其他应用进行通信传输数据。 |

config.json配置样例

```json5
"abilities": [
  ...
  {
    "name": ".DataAbility",
    "srcLanguage": "ets",
    "srcPath": "DataAbility",
    "icon": "$media:icon",
    "description": "$string:DataAbility_desc",
    "type": "data",
    "visible": true,
    "uri": "dataability://com.samples.famodelabilitydevelop.DataAbility",
    "readPermission": "ohos.permission.READ_CONTACTS",
    "writePermission": "ohos.permission.WRITE_CONTACTS"
  },
  ...
]
```

DataAbility支持的配置项及详细说明详见[module对象内部结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-structure)。
