---
title: "pdd.cross.cabinet.recycle.order - 快递柜包裹回收订单"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cross.cabinet.recycle.order"
menu_path:
  - "物流API"
  - "pdd.cross.cabinet.recycle.order"
captured_at: "2026-04-09T15:14:53.025Z"
---

# pdd.cross.cabinet.recycle.order

## 快递柜包裹回收订单

更新时间：2025-07-23 15:04:00

¥免费API

不需用户授权

方舟

本接⼝请求成功仅代表我⽅服务端向柜⼦推送开箱指令成功，并不代表实际格⼝开箱结果

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

lockerNo

STRING

必填

快递柜编号

orderNo

STRING

必填

物流单号

providerCode

STRING

必填

供应商code

### 返回参数说明

参数接口

参数类型

例子

说明

errmsg

STRING

成功

错误描述

errno

INTEGER

0

状态码 0成功 其他值为失败

time

LONG

1744161350268

响应时间戳

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCrossCabinetRecycleOrderRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCrossCabinetRecycleOrderResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCrossCabinetRecycleOrderRequest request = new PddCrossCabinetRecycleOrderRequest();
        request.setLockerNo("1000L01");
        request.setOrderNo("JT8772665523");
        request.setProviderCode("PDD");
        request.setTargetClientId("your target client id");
        PddCrossCabinetRecycleOrderResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "errmsg": "成功",
  "errno": 0,
  "time": 1744161350268
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

偏远集运权限包

重抛货快运权限包

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

接口总限流频次：5000次/1秒

### API工具
