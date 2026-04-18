---
title: "pdd.cloud.websession.send - 会话同步接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.websession.send"
menu_path:
  - "pdd.cloud.websession.send"
captured_at: "2026-04-15T03:33:15.221Z"
---

# pdd.cloud.websession.send

## 会话同步接口

更新时间：2020-07-08 20:14:49

¥免费API

不需用户授权

方舟

同步友商云的会话信息

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

target\_client\_id

String

必填

目标应用client\_id

### 请求参数说明

参数接口

参数类型

是否必填

说明

cache\_type

STRING

非必填

缓存类型

session\_info\_list

OBJECT\[\]

非必填

会话列表

key

STRING

非必填

建名称

value

STRING

非必填

值

expir\_time

LONG

非必填

过期时间

function

STRING

非必填

操作

### 返回参数说明

参数接口

参数类型

例子

说明

send\_response

OBJECT

响应

res\_list

OBJECT\[\]

响应列表

key

STRING

jsessionid

健名

success

BOOLEAN

true

是否成功

error\_info

STRING

put time out

错误异常

is\_success

BOOLEAN

是否成功，false-失败，true-成功

error\_msg

STRING

错误信息

sub\_msg

STRING

子错误信息

sub\_code

INTEGER

错误码

error\_code

INTEGER

子错误码

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWebsessionSendRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudWebsessionSendResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWebsessionSendRequest.SessionInfoListItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudWebsessionSendRequest request = new PddCloudWebsessionSendRequest();
        request.setCacheType("redis");
        List<SessionInfoListItem> sessionInfoList = new ArrayList<SessionInfoListItem>();

        SessionInfoListItem item = new SessionInfoListItem();
        item.setKey("jseesionid");
        item.setValue("User00001");
        item.setExpirTime(60000L);
        item.setFunction("PUT");
        sessionInfoList.add(item);
        request.setSessionInfoList(sessionInfoList);
        request.setTargetClientId("your target client id");
        PddCloudWebsessionSendResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "send_response": {
    "error_code": 0,
    "error_msg": "str",
    "is_success": false,
    "res_list": [
      {
        "error_info": "put time out",
        "key": "jsessionid",
        "success": true
      }
    ],
    "sub_code": 0,
    "sub_msg": "str"
  }
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

暂无数据

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

接口总限流频次：17500次/2秒

### API工具
