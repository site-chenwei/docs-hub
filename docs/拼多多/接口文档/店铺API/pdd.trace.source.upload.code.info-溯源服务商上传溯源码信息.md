---
title: "pdd.trace.source.upload.code.info - 溯源服务商上传溯源码信息"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.trace.source.upload.code.info"
menu_path:
  - "店铺API"
  - "pdd.trace.source.upload.code.info"
captured_at: "2026-04-09T15:21:40.946Z"
---

# pdd.trace.source.upload.code.info

## 溯源服务商上传溯源码信息

更新时间：2021-03-10 17:37:09

¥免费API

不需用户授权

方舟

溯源服务商上传溯源码信息

### 公共参数

#### 请求地址（目前只提供正式环境，暂无沙箱环境）

环境

HTTPS地址

正式环境

https://ark-api.pinduoduo.com/ark/router

#### 公共请求参数

参数名称

参数类型

是否必填

参数描述

type

String

必填

API接口名称

client\_id

String

必填

POP分配给应用的client\_id

access\_token

String

非必填

通过code获取的access\_token

timestamp

String

必填

UNIX时间戳，单位秒，需要与拼多多服务器时间差值在10分钟内

data\_type

String

非必填

响应格式，即返回数据的格式，JSON或者XML（二选一），默认JSON，注意是大写

version

String

非必填

API协议版本号，默认为V1，可不填

sign

String

必填

API输入参数签名结果，签名算法参考开放平台接入指南第三部分底部。

### 请求参数说明

参数接口

参数类型

是否必填

说明

serial\_num\_list

OBJECT\[\]

必填

溯源码列表

encoded\_serial\_num

STRING

必填

溯源码（处理后）

serial\_num

STRING

必填

溯源码

### 返回参数说明

参数接口

参数类型

例子

说明

status

INTEGER

1成功，0失败

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddTraceSourceUploadCodeInfoRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddTraceSourceUploadCodeInfoResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddTraceSourceUploadCodeInfoRequest.SerialNumListItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddTraceSourceUploadCodeInfoRequest request = new PddTraceSourceUploadCodeInfoRequest();
        List<SerialNumListItem> serialNumList = new ArrayList<SerialNumListItem>();

        SerialNumListItem item = new SerialNumListItem();
        item.setEncodedSerialNum("str");
        item.setSerialNum("str");
        serialNumList.add(item);
        request.setSerialNumList(serialNumList);
        PddTraceSourceUploadCodeInfoResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "status": 0
}
```

### 异常示例

JSON

XML

```

{
  "error_response": {
    "error_msg": "公共参数错误:type",
    "sub_msg": "",
    "sub_code": null,
    "error_code": 10001,
    "request_id": "15440104776643887"
  }
}
```

### 相关权限包

拥有此接口的权限包

可获得/可申请此权限包的应用类型

方舟海淘溯源权限包

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

接口总限流频次：2500次/1秒

### API工具
