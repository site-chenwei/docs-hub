---
title: "pdd.erp.refund.list.get - 售后列表查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.erp.refund.list.get"
menu_path:
  - "方舟数据传输API"
  - "pdd.erp.refund.list.get"
captured_at: "2026-04-09T15:25:57.927Z"
---

# pdd.erp.refund.list.get

## 售后列表查询接口

更新时间：2025-12-10 17:10:18

¥免费API

必须用户授权

方舟

方舟 ERP - 自研数据传输场景

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

erp\_after\_sales\_id\_list

STRING\[\]

非必填

ERP 售后单号，最多100个

erp\_after\_sales\_status

INTEGER

非必填

ERP售后状态

erp\_mall\_no

STRING

非必填

erp 店铺编码

erp\_order\_sn\_list

STRING\[\]

非必填

ERP 订单号，最多100个

page

INTEGER

必填

返回页码

page\_size

INTEGER

必填

返回数量，最大 100

pdd\_after\_sales\_id\_list

STRING\[\]

非必填

拼多多售后单号，最多100个

pdd\_after\_sales\_status

INTEGER

非必填

拼多多售后状态

pdd\_mall\_id

LONG

非必填

拼多多店铺 id

pdd\_order\_sn\_list

STRING\[\]

非必填

拼多多订单号，最多100个

query\_time\_end

LONG

非必填

结束时间时间戳

query\_time\_start

LONG

非必填

开始时间时间戳

query\_time\_type

INTEGER

非必填

查询时间类型： 1-售后申请时间 2-售后更新时间

sid

STRING

非必填

商家唯一标识

### 返回参数说明

参数接口

参数类型

例子

说明

erp\_request\_id

STRING

唯一请求识别码

has\_next

DOUBLE

是否存在下一页

refund\_list

OBJECT\[\]

售后单列表

after\_sale\_reason

STRING

售后原因

after\_sales\_type

INTEGER

售后类型

common\_ext\_param

STRING

其他

created\_time

STRING

售后申请时间

erp\_after\_sales\_id

STRING

ERP 售后单号

erp\_after\_sales\_status

INTEGER

ERP售后状态

erp\_order\_sn

STRING

ERP 订单号

expire\_time

LONG

售后逾期时间，时间戳

item\_refund\_amount

DOUBLE

实退金额

items

OBJECT\[\]

明细列表

erp\_goods\_id

STRING

erp 商品编码

erp\_sku\_id

STRING

erp sku 编码

item\_common\_ext\_param

STRING

其他

item\_goods\_number

LONG

商品数量

item\_goods\_price

DOUBLE

商品单价

item\_part\_after\_sales\_value

INTEGER

部分退货件数 / 比例

pdd\_goods\_id

LONG

拼多多商品 ID

pdd\_sku\_id

LONG

拼多多 SKUID

pdd\_after\_sales\_id

LONG

拼多多售后单号

pdd\_after\_sales\_status

INTEGER

拼多多售后状态

pdd\_order\_sn

STRING

拼多多订单号

postage

DOUBLE

邮费

refund\_amount

DOUBLE

实退金额

refund\_reason

STRING

退款原因

speed\_refund\_flag

INTEGER

极速退款标志位 1：极速退款，0：非极速退款

tracking\_number

STRING

退货快递单号

updated\_time

STRING

售后更新时间

refund\_list\_get\_response

OBJECT

请求response

total\_count

INTEGER

1

售后单总数

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddErpRefundListGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddErpRefundListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddErpRefundListGetRequest request = new PddErpRefundListGetRequest();
        List<String> erpAfterSalesIdList = new ArrayList<String>();
        erpAfterSalesIdList.add("str");
        request.setErpAfterSalesIdList(erpAfterSalesIdList);
        request.setErpAfterSalesStatus(1);
        request.setErpMallNo("1");
        List<String> erpOrderSnList = new ArrayList<String>();
        erpOrderSnList.add("str");
        request.setErpOrderSnList(erpOrderSnList);
        request.setPage(1);
        request.setPageSize(1);
        List<String> pddAfterSalesIdList = new ArrayList<String>();
        pddAfterSalesIdList.add("str");
        request.setPddAfterSalesIdList(pddAfterSalesIdList);
        request.setPddAfterSalesStatus(1);
        request.setPddMallId(1L);
        List<String> pddOrderSnList = new ArrayList<String>();
        pddOrderSnList.add("str");
        request.setPddOrderSnList(pddOrderSnList);
        request.setQueryTimeEnd(1L);
        request.setQueryTimeStart(1L);
        request.setQueryTimeType(1);
        request.setSid("str");
        request.setTargetClientId("your target client id");
        PddErpRefundListGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "erp_request_id": "str",
  "has_next": 0.0,
  "refund_list": [
    {
      "after_sale_reason": "str",
      "after_sales_type": 0,
      "common_ext_param": "str",
      "created_time": "str",
      "erp_after_sales_id": "str",
      "erp_after_sales_status": 0,
      "erp_order_sn": "str",
      "expire_time": 0,
      "item_refund_amount": 0.0,
      "items": [
        {
          "erp_goods_id": "str",
          "erp_sku_id": "str",
          "item_common_ext_param": "str",
          "item_goods_number": 0,
          "item_goods_price": 0.0,
          "item_part_after_sales_value": 0,
          "pdd_goods_id": 0,
          "pdd_sku_id": 0
        }
      ],
      "pdd_after_sales_id": 0,
      "pdd_after_sales_status": 0,
      "pdd_order_sn": "str",
      "postage": 0.0,
      "refund_amount": 0.0,
      "refund_reason": "str",
      "speed_refund_flag": 0,
      "tracking_number": "str",
      "updated_time": "str"
    }
  ],
  "refund_list_get_response": {},
  "total_count": 1
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

方舟ERP-自研数据传输 自研权限包

虚拟商家后台系统、商家后台系统、电子凭证商家后台系统

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

接口总限流频次：5000次/1秒

应用限流频次：100次/1秒

商家限流频次：50次/1秒

### API工具
