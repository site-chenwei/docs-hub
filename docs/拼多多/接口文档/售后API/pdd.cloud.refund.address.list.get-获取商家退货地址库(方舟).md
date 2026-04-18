---
title: "pdd.cloud.refund.address.list.get - 获取商家退货地址库(方舟)"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.refund.address.list.get"
menu_path:
  - "pdd.cloud.refund.address.list.get"
captured_at: "2026-04-15T03:32:58.954Z"
---

# pdd.cloud.refund.address.list.get

## 获取商家退货地址库(方舟)

更新时间：2022-06-27 22:53:24

¥免费API

不需用户授权

方舟

多多云外调用多多云内服务，获取商家退货地址库(方舟)

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

refund\_address\_list\_get\_response

OBJECT

response

refund\_address\_list

OBJECT\[\]

退货地址列表

city\_id

INTEGER

退货地址所在城市ID

city\_name

STRING

退货地址所在城市名字

district\_id

INTEGER

退货地址所在区ID

district\_name

STRING

退货地址所在区名字

id

LONG

退货地址ID

is\_default

STRING

是否为默认退货地址

is\_legal

BOOLEAN

退货地址是否合法

is\_validated

BOOLEAN

退货地址是否有效

mall\_id

LONG

店铺ID

province\_id

INTEGER

退货地址所在省份ID

province\_name

STRING

退货地址所在省份名字

refund\_address

STRING

退货地址

refund\_address\_id

STRING

refund\_id

refund\_name

STRING

退货收件人名字

refund\_phone

STRING

退货收件人手机号

refund\_tel

STRING

退货收件人固定电话

error\_code

INTEGER

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
import com.pdd.pop.sdk.http.api.ark.request.PddCloudRefundAddressListGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudRefundAddressListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudRefundAddressListGetRequest request = new PddCloudRefundAddressListGetRequest();
        request.setMallId(2301L);
        request.setTargetClientId("your target client id");
        PddCloudRefundAddressListGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "refund_address_list_get_response": {
    "error_code": 0,
    "error_msg": "str",
    "refund_address_list": [
      {
        "city_id": 0,
        "city_name": "str",
        "district_id": 0,
        "district_name": "str",
        "id": 0,
        "is_default": "str",
        "is_legal": false,
        "is_validated": false,
        "mall_id": 0,
        "province_id": 0,
        "province_name": "str",
        "refund_address": "str",
        "refund_address_id": "str",
        "refund_name": "str",
        "refund_phone": "str",
        "refund_tel": "str"
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
