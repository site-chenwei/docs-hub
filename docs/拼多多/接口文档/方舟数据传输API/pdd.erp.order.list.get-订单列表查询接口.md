---
title: "pdd.erp.order.list.get - 订单列表查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.erp.order.list.get"
menu_path:
  - "方舟数据传输API"
  - "pdd.erp.order.list.get"
captured_at: "2026-04-09T15:25:51.663Z"
---

# pdd.erp.order.list.get

## 订单列表查询接口

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

erp\_mall\_no

STRING

非必填

ERP 店铺编码

erp\_order\_sn\_list

STRING\[\]

非必填

ERP 订单号，最多100个

erp\_order\_status

INTEGER

非必填

ERP 订单状态

item\_order\_sn\_list

STRING\[\]

非必填

ERP 子订单号，最多100个

page

INTEGER

必填

返回页码

page\_size

INTEGER

必填

返回数量，最大 100

pdd\_mall\_id

LONG

非必填

拼多多店铺 id

pdd\_order\_sn\_list

STRING\[\]

非必填

拼多多订单号，最多100个

pdd\_order\_status

INTEGER

非必填

拼多多订单状态

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

查询时间类型： 1 - 支付时间 2 - 成交时间 3 - 订单创建时间 4 - 订单修改时间 5 - 平台发货时间 6 - 承诺发货时间

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

请求唯一识别码

has\_next

BOOLEAN

true

是否存在下一页

order\_list

OBJECT\[\]

订单信息列表

common\_ext\_param

STRING

其他

confirm\_time

STRING

成交时间

created\_time

STRING

订单创建时间

discount\_amount

DOUBLE

折扣金额

duo\_duo\_pay\_reduction

DOUBLE

多多支付立减金额

erp\_after\_sales\_id

STRING

ERP 售后单号

erp\_after\_sales\_status

INTEGER

ERP 售后状态

erp\_buyer\_memo

STRING

ERP买家留言

erp\_mall\_no

STRING

ERP店铺编码

erp\_order\_sn

STRING

ERP订单号

erp\_order\_status

INTEGER

ERP 订单状态

erp\_refund\_status

INTEGER

ERP 退款状态

erp\_remark

STRING

ERP卖家备注

erp\_remark\_tag

INTEGER

ERP卖家旗帜

income\_amount

DOUBLE

实收金额

items

OBJECT\[\]

明细列表

erp\_goods\_amount

DOUBLE

货品金额

erp\_goods\_count

LONG

货品数量

erp\_goods\_id

STRING

ERP商品编码

erp\_goods\_img

STRING

货品图片链接

erp\_goods\_price

DOUBLE

货品销售价格

erp\_sku\_id

STRING

ERP sku编码

income\_amount

DOUBLE

实收金额

item\_common\_ext\_param

STRING

其他

item\_order\_sn

STRING

ERP子订单号

pay\_amount

DOUBLE

实付金额

pdd\_goods\_amount

DOUBLE

商品金额

pdd\_goods\_count

LONG

商品数量

pdd\_goods\_id

LONG

拼多多商品 ID

pdd\_goods\_img

STRING

商品图片链接

pdd\_goods\_price

DOUBLE

商品销售价格

pdd\_order\_sn

STRING

拼多多订单号

pdd\_sku\_id

LONG

拼多多 SKUID

last\_ship\_time

STRING

承诺发货时间

logistics\_id

LONG

快递公司id

pay\_amount

DOUBLE

实付金额

pay\_time

STRING

支付时间

pdd\_after\_sales\_id

STRING

拼多多售后单号

pdd\_after\_sales\_status

INTEGER

拼多多售后状态

pdd\_buyer\_memo

STRING

拼多多买家留言

pdd\_mall\_id

LONG

拼多多店铺id

pdd\_order\_status

INTEGER

拼多多订单状态

pdd\_refund\_status

INTEGER

拼多多退款状态

pdd\_remark

STRING

拼多多卖家备注

pdd\_remark\_tag

INTEGER

拼多多卖家旗帜

platform\_discount

DOUBLE

平台优惠金额

postage

DOUBLE

邮费

receive\_time

STRING

确认收货时间

seller\_discount

DOUBLE

商家优惠金额

shipping\_time

STRING

平台发货时间

tracking\_number

STRING

快递运单号

updated\_at

STRING

修改时间

ware\_house\_id

STRING

发货仓库编号

ware\_house\_name

STRING

发货仓库名称

ware\_house\_type

LONG

发货仓库类型

order\_list\_get\_response

OBJECT

请求response

total\_count

INTEGER

1

订单总数

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddErpOrderListGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddErpOrderListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddErpOrderListGetRequest request = new PddErpOrderListGetRequest();
        request.setErpMallNo("str");
        List<String> erpOrderSnList = new ArrayList<String>();
        erpOrderSnList.add("str");
        request.setErpOrderSnList(erpOrderSnList);
        request.setErpOrderStatus(1);
        List<String> itemOrderSnList = new ArrayList<String>();
        itemOrderSnList.add("str");
        request.setItemOrderSnList(itemOrderSnList);
        request.setPage(1);
        request.setPageSize(1000);
        request.setPddMallId(1L);
        List<String> pddOrderSnList = new ArrayList<String>();
        pddOrderSnList.add("str");
        request.setPddOrderSnList(pddOrderSnList);
        request.setPddOrderStatus(1);
        request.setQueryTimeEnd(0L);
        request.setQueryTimeStart(0L);
        request.setQueryTimeType(1);
        request.setSid("str");
        request.setTargetClientId("your target client id");
        PddErpOrderListGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "erp_request_id": "str",
  "has_next": true,
  "order_list": [
    {
      "common_ext_param": "str",
      "confirm_time": "str",
      "created_time": "str",
      "discount_amount": 0.0,
      "duo_duo_pay_reduction": 0.0,
      "erp_after_sales_id": "str",
      "erp_after_sales_status": 0,
      "erp_buyer_memo": "str",
      "erp_mall_no": "str",
      "erp_order_sn": "str",
      "erp_order_status": 0,
      "erp_refund_status": 0,
      "erp_remark": "str",
      "erp_remark_tag": 0,
      "income_amount": 0.0,
      "items": [
        {
          "erp_goods_amount": 0.0,
          "erp_goods_count": 0,
          "erp_goods_id": "str",
          "erp_goods_img": "str",
          "erp_goods_price": 0.0,
          "erp_sku_id": "str",
          "income_amount": 0.0,
          "item_common_ext_param": "str",
          "item_order_sn": "str",
          "pay_amount": 0.0,
          "pdd_goods_amount": 0.0,
          "pdd_goods_count": 0,
          "pdd_goods_id": 0,
          "pdd_goods_img": "str",
          "pdd_goods_price": 0.0,
          "pdd_order_sn": "str",
          "pdd_sku_id": 0
        }
      ],
      "last_ship_time": "str",
      "logistics_id": 0,
      "pay_amount": 0.0,
      "pay_time": "str",
      "pdd_after_sales_id": "str",
      "pdd_after_sales_status": 0,
      "pdd_buyer_memo": "str",
      "pdd_mall_id": 0,
      "pdd_order_status": 0,
      "pdd_refund_status": 0,
      "pdd_remark": "str",
      "pdd_remark_tag": 0,
      "platform_discount": 0.0,
      "postage": 0.0,
      "receive_time": "str",
      "seller_discount": 0.0,
      "shipping_time": "str",
      "tracking_number": "str",
      "updated_at": "str",
      "ware_house_id": "str",
      "ware_house_name": "str",
      "ware_house_type": 0
    }
  ],
  "order_list_get_response": {},
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
