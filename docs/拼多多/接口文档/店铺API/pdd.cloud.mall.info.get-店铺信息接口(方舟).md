---
title: "pdd.cloud.mall.info.get - 店铺信息接口(方舟)"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.mall.info.get"
menu_path:
  - "pdd.cloud.mall.info.get"
captured_at: "2026-04-15T03:32:55.958Z"
---

# pdd.cloud.mall.info.get

## 店铺信息接口(方舟)

更新时间：2022-06-27 22:53:24

¥免费API

不需用户授权

方舟

多多云外调用多多云内服务，通过此接口获取店铺信息(方舟)

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

mall\_id

LONG

必填

店铺ID

### 返回参数说明

参数接口

参数类型

例子

说明

mall\_info\_get\_response

OBJECT

response

logo

STRING

店铺logo

mall\_character

INTEGER

店铺身份,0:厂商 1:分销商 2:都不是 3:都是

mall\_desc

STRING

店铺描述

mall\_id

LONG

店铺id

mall\_name

STRING

店铺名称

merchant\_type

INTEGER

店铺类型,1:个人 2:企业 3:旗舰店 4:专卖店 5:专营店 6:普通店

error\_code

INTEGER

40001

错误码

error\_msg

STRING

错误信息

sub\_code

INTEGER

子错误码

sub\_msg

STRING

子错误信息

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudMallInfoGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudMallInfoGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudMallInfoGetRequest request = new PddCloudMallInfoGetRequest();
        request.setMallId(2301L);
        request.setTargetClientId("your target client id");
        PddCloudMallInfoGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "mall_info_get_response": {
    "error_code": 40001,
    "error_msg": "str",
    "logo": "str",
    "mall_character": 0,
    "mall_desc": "str",
    "mall_id": 0,
    "mall_name": "str",
    "merchant_type": 0,
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

接口总限流频次：7500次/1秒

### API工具
