---
title: "pdd.open.msg.send.result.receive - 短信回执"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.open.msg.send.result.receive"
menu_path:
  - "短信服务API"
  - "pdd.open.msg.send.result.receive"
captured_at: "2026-04-09T15:23:37.319Z"
---

# pdd.open.msg.send.result.receive

## 短信回执

更新时间：2026-02-05 14:13:37

¥免费API

不需用户授权

方舟

开平短信服务API

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

biz\_id

STRING

非必填

回执id

error\_code

STRING

非必填

错误码

error\_msg

STRING

非必填

错误信息

error\_reason

STRING

非必填

错误原因

mobile

STRING

非必填

手机号

out\_id

STRING

非必填

业务请求唯一标识

receipt\_time

STRING

非必填

接收时间

send\_time

STRING

非必填

发送时间

sms\_size

INTEGER

非必填

短信数量

success

BOOLEAN

非必填

是否成功

waybill\_code

STRING

非必填

物流单号

### 返回参数说明

参数接口

参数类型

例子

说明

code

INTEGER

200

返回码

msg

STRING

成功

返回信息

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddOpenMsgSendResultReceiveRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddOpenMsgSendResultReceiveResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddOpenMsgSendResultReceiveRequest request = new PddOpenMsgSendResultReceiveRequest();
        request.setBizId("abc01234");
        request.setErrorCode("500");
        request.setErrorMsg("failture");
        request.setErrorReason("目标手机已关机");
        request.setMobile("188********");
        request.setOutId("str");
        request.setReceiptTime("yyyy-MM-DD");
        request.setSendTime("yyyy-MM-DD");
        request.setSmsSize(10);
        request.setSuccess(false);
        request.setWaybillCode("PDD0123456");
        request.setTargetClientId("your target client id");
        PddOpenMsgSendResultReceiveResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "code": 200,
  "msg": "成功"
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

短信服务权限包

商家后台系统

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

接口总限流频次：22500次/10秒

### API工具
