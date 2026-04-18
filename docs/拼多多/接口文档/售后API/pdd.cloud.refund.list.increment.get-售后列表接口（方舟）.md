---
title: "pdd.cloud.refund.list.increment.get - 售后列表接口（方舟）"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.refund.list.increment.get"
menu_path:
  - "pdd.cloud.refund.list.increment.get"
captured_at: "2026-04-15T03:33:04.965Z"
---

# pdd.cloud.refund.list.increment.get

## 售后列表接口（方舟）

更新时间：2025-10-22 20:29:22

¥免费API

不需用户授权

方舟

多多云外调用多多云内服务，售后列表增量查询（方舟）

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

after\_sales\_status

INTEGER

必填

必填，售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货

after\_sales\_type

INTEGER

必填

必填，售后类型 1：全部 2：仅退款 3：退货退款 4：换货 5：缺货补寄

end\_updated\_at

LONG

必填

必填，最后更新时间结束时间的UNIX时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时00 分 00 秒)起至现在的总秒数 PS：开始时间结束时间间距不超过 30 分钟

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

非必填

订单号。若入参含订单号，则可查询订单下的全部售后单。且入参中除订单号，page，page\_size外的其他查询条件不起作用（标记必填的仍旧需要输入）。

page

INTEGER

非必填

返回页码 默认 1，页码从 1 开始 PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值

page\_size

INTEGER

非必填

返回数量，默认 100。最大 100

start\_updated\_at

LONG

必填

必填，最后更新时间开始时间的UNIX时间戳，指格林威治时间 1970 年01月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00分 00 秒)起至现在的总秒数

### 返回参数说明

参数接口

参数类型

例子

说明

refund\_increment\_get\_response

OBJECT

售后增量订单列表对象

error\_code

INTEGER

错误码

error\_msg

STRING

错误信息

refund\_list

OBJECT\[\]

售后列表对象

after\_sale\_reason

STRING

不想要了

售后原因

after\_sales\_status

INTEGER

1

售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货

after\_sales\_type

INTEGER

1

售后类型

confirm\_time

STRING

1551612204

成团时间

created\_time

STRING

1551612204

创建时间

discount\_amount

STRING

1

订单折扣金额（元）

dispute\_refund\_status

INTEGER

1纠纷退款 0非纠纷退款

good\_image

STRING

1

商品图片

goods\_id

LONG

1

商品编码

goods\_name

STRING

1

商品名称

goods\_number

STRING

1

商品数量

goods\_price

STRING

1

商品单价

id

LONG

1

售后编号

order\_amount

STRING

1

订单金额（元）

order\_sn

STRING

190228-355530178612389

订单编号

outer\_goods\_id

STRING

1

商家外部编码（商品）

outer\_id

STRING

1

商家外部编码（sku）

refund\_amount

STRING

1

退款金额（元）

shipping\_name

STRING

退货物流公司名称

sku\_id

STRING

1

商品规格ID

speed\_refund\_flag

INTEGER

极速退款标志位 1：极速退款，0：非极速退款

speed\_refund\_status

STRING

1

极速退款状态，"1"：有极速退款资格，"2"：极速退款失败, "3" 表示极速退款成功，其他表示非极速退款

tracking\_number

STRING

1

快递运单号

updated\_time

STRING

1551612204

更新时间

user\_shipping\_status

STRING

0-未勾选 1-消费者选择的收货状态为未收到货 2-消费者选择的收货状态为已收到货

refund\_operator\_role

INTEGER

同意退款操作人角色0:"默认",1:"用户",2:"商家",3:"平台",4:"系统",5:"团长",6:"司机",7:"代理人"

sub\_code

INTEGER

子错误码

sub\_msg

STRING

子错误信息

total\_count

INTEGER

1

返回的售后订单列表总数

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudRefundListIncrementGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudRefundListIncrementGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudRefundListIncrementGetRequest request = new PddCloudRefundListIncrementGetRequest();
        request.setAfterSalesStatus(1);
        request.setAfterSalesType(1);
        request.setEndUpdatedAt(1551612046L);
        request.setExtendProps("{"key":"value"}");
        request.setMallId(2301L);
        request.setOrderSn("str");
        request.setPage(1);
        request.setPageSize(100);
        request.setStartUpdatedAt(1551612046L);
        request.setTargetClientId("your target client id");
        PddCloudRefundListIncrementGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "refund_increment_get_response": {
    "error_code": 0,
    "error_msg": "str",
    "refund_list": [
      {
        "after_sale_reason": "不想要了",
        "after_sales_status": 1,
        "after_sales_type": 1,
        "confirm_time": "1551612204",
        "created_time": "1551612204",
        "discount_amount": "1",
        "dispute_refund_status": 0,
        "good_image": "1",
        "goods_id": 1,
        "goods_name": "1",
        "goods_number": "1",
        "goods_price": "1",
        "id": 1,
        "order_amount": "1",
        "order_sn": "190228-355530178612389",
        "outer_goods_id": "1",
        "outer_id": "1",
        "refund_amount": "1",
        "shipping_name": "str",
        "sku_id": "1",
        "speed_refund_flag": 0,
        "speed_refund_status": "1",
        "tracking_number": "1",
        "updated_time": "1551612204",
        "user_shipping_status": "str"
      }
    ],
    "refund_operator_role": 0,
    "sub_code": 0,
    "sub_msg": "str",
    "total_count": 1
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

接口总限流频次：42500次/10秒

### API工具
