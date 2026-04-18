---
title: "pdd.cloud.refund.information.get - 售后单详情接口(方舟)"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.refund.information.get"
menu_path:
  - "pdd.cloud.refund.information.get"
captured_at: "2026-04-15T03:33:01.946Z"
---

# pdd.cloud.refund.information.get

## 售后单详情接口(方舟)

更新时间：2025-11-20 11:10:43

¥免费API

不需用户授权

方舟

多多云外调用多多云内服务，查询单个售后单详情(方舟)

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

after\_sales\_id

LONG

非必填

售后单id

extend\_props

STRING

非必填

扩展字段

mall\_id

LONG

必填

店铺ID

order\_sn

STRING

必填

订单号

### 返回参数说明

参数接口

参数类型

例子

说明

after\_sales\_reason

STRING

售后原因

after\_sales\_status

INTEGER

0

售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货

after\_sales\_type

INTEGER

1

售后类型 1-仅退款，2-退货退款，3-换货，4-补寄，5-维修

confirm\_time

LONG

1638792640659

订单成团时间

discount\_amount

INTEGER

0

订单折扣金额

dispute\_refund\_status

INTEGER

0

1纠纷退款 0非纠纷退款

error\_code

INTEGER

40001

错误码

error\_msg

STRING

错误信息

exchange\_shipping\_detail

OBJECT

换货详情,售后类型是换货才有值

customer\_send\_back\_ship\_id

INTEGER

消费者回寄的物流id

customer\_send\_back\_trunk\_number

STRING

消费者回寄的物流单号

exchange\_goods\_name

STRING

换货发货的物品名称

exchange\_goods\_number

INTEGER

换货发货的物品数量

exchange\_goods\_price

LONG

换货的物品价格(单位分)

exchange\_receiver\_city

STRING

商家换货发货的城市（消费者地址）

exchange\_receiver\_city\_id

LONG

商家换货发货的城市编码（消费者地址）

exchange\_receiver\_province

STRING

商家换货发货的省份（消费者地址）

exchange\_receiver\_province\_id

LONG

商家换货发货的省份编码（消费者地址）

exchange\_receiver\_town

STRING

商家换货发货的区县（消费者地址）

exchange\_receiver\_town\_id

LONG

商家换货发货的区县编码（消费者地址）

fast\_exchange\_expire\_time

LONG

1762401156

极速换货履约逾期时间（秒）

is\_fast\_exchange

BOOLEAN

是否是极速换货

merchant\_exchange\_detail\_address

STRING

商家换货发货的详细地址

merchant\_exchange\_detail\_address\_mask

STRING

商家换货发货的详细地址（打码）

merchant\_exchange\_detail\_phone

STRING

商家换货发货的收货人手机号

merchant\_exchange\_detail\_phone\_mask

STRING

商家换货发货的收货人手机号（打码）

merchant\_exchange\_detail\_receiver

STRING

商家换货发货的收货人名字

merchant\_exchange\_detail\_receiver\_mask

STRING

商家换货发货的收货人名字（打码）

merchant\_exchange\_ship\_id

INTEGER

商家换货发货的物流id

merchant\_exchange\_trunk\_number

STRING

商家换货发货的物流单号

sku\_id\_exchange

STRING

换货商品规格ID

exist\_images

BOOLEAN

false

是否存在用户申请售后时提交的图片凭证

expire\_time

LONG

1638792640659

售后逾期时间（只提供待商家处理状态下的，其余的状态为null）

express\_no

STRING

退货物流单号

goods\_number

INTEGER

1

商品数量

goods\_price

INTEGER

100

商品单价

id

LONG

10

售后单id

images

STRING\[\]

用户申请售后上传的图片列表

join\_or\_not

STRING

是否介入 1介入 0未介入

order\_amount

LONG

100

交易金额

order\_sn

STRING

订单号

part\_after\_sales\_type

INTEGER

1

部分售后类型：0：无意义、1：件数/件、2：比例/%；注意只有退货退款类型才有意义

part\_after\_sales\_value

INTEGER

1

部分售后件数/比例；注意只有退货退款类型才有意义

recreated\_at

LONG

1638792640659

售后单创建时间（重新申请时间）

refund\_amount

INTEGER

1

退款金额

refund\_operator\_role

INTEGER

1

同意退款操作人角色0:"默认",1:"用户",2:"商家",3:"平台",4:"系统",5:"团长",6:"司机",7:"代理人"

remark

STRING

联系卖家多次，一直不发货，申请仅退款处理

用户申请输入的描述信息

shipping\_name

STRING

退货物流名称

shipping\_status

INTEGER

0

订单发货状态 0:未发货， 1:已发货（包含：已发货，已揽收）

sku\_id

STRING

商品规格ID

speed\_refund\_flag

INTEGER

0

极速退款标志位 1：极速退款，0：非极速退款

sub\_code

INTEGER

50001

子错误码

sub\_msg

STRING

子错误信息

updated\_time

STRING

更新时间

user\_shipping\_status

STRING

0-未勾选 1-消费者选择的收货状态为未收到货 2-消费者选择的收货状态为已收到货

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudRefundInformationGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudRefundInformationGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudRefundInformationGetRequest request = new PddCloudRefundInformationGetRequest();
        request.setAfterSalesId(1L);
        request.setExtendProps("{"key":"value"}");
        request.setMallId(2021L);
        request.setOrderSn("str");
        request.setTargetClientId("your target client id");
        PddCloudRefundInformationGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "after_sales_reason": "str",
  "after_sales_status": 0,
  "after_sales_type": 1,
  "confirm_time": 1638792640659,
  "discount_amount": 0,
  "dispute_refund_status": 0,
  "error_code": 40001,
  "error_msg": "str",
  "exchange_shipping_detail": {
    "customer_send_back_ship_id": 0,
    "customer_send_back_trunk_number": "str",
    "exchange_goods_name": "str",
    "exchange_goods_number": 0,
    "exchange_goods_price": 0,
    "exchange_receiver_city": "str",
    "exchange_receiver_city_id": 0,
    "exchange_receiver_province": "str",
    "exchange_receiver_province_id": 0,
    "exchange_receiver_town": "str",
    "exchange_receiver_town_id": 0,
    "fast_exchange_expire_time": 1762401156,
    "is_fast_exchange": false,
    "merchant_exchange_detail_address": "str",
    "merchant_exchange_detail_address_mask": "str",
    "merchant_exchange_detail_phone": "str",
    "merchant_exchange_detail_phone_mask": "str",
    "merchant_exchange_detail_receiver": "str",
    "merchant_exchange_detail_receiver_mask": "str",
    "merchant_exchange_ship_id": 0,
    "merchant_exchange_trunk_number": "str",
    "sku_id_exchange": "str"
  },
  "exist_images": false,
  "expire_time": 1638792640659,
  "express_no": "str",
  "goods_number": 1,
  "goods_price": 100,
  "id": 10,
  "images": [
    "str"
  ],
  "join_or_not": "str",
  "order_amount": 100,
  "order_sn": "str",
  "part_after_sales_type": 1,
  "part_after_sales_value": 1,
  "recreated_at": 1638792640659,
  "refund_amount": 1,
  "refund_operator_role": 1,
  "remark": "联系卖家多次，一直不发货，申请仅退款处理",
  "shipping_name": "str",
  "shipping_status": 0,
  "sku_id": "str",
  "speed_refund_flag": 0,
  "sub_code": 50001,
  "sub_msg": "str",
  "updated_time": "str",
  "user_shipping_status": "str"
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
