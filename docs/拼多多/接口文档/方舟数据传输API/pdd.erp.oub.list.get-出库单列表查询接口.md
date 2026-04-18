---
title: "pdd.erp.oub.list.get - 出库单列表查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.erp.oub.list.get"
menu_path:
  - "方舟数据传输API"
  - "pdd.erp.oub.list.get"
captured_at: "2026-04-09T15:25:54.784Z"
---

# pdd.erp.oub.list.get

## 出库单列表查询接口

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

erp 店铺编码

erp\_order\_sn\_list

STRING\[\]

非必填

ERP 订单号，最多100个

oub\_order\_code\_list

STRING\[\]

非必填

出库单号，最多100个

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

查询时间类型： 1-创建时间 2-修改时间 3-审核时间 4-出库时间

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

BOOLEAN

true

是否存在下一页

oub\_list

OBJECT\[\]

出库单列表

ClusterInfos

OBJECT\[\]

子母单信息

oub\_order\_code

STRING

出库单号

sub\_logistics\_company

STRING

子单物流公司

sub\_logistics\_id

LONG

子单物流公司编码

sub\_tracking\_number

STRING

子单物流单号

Inspector

STRING

验货员

Packer

STRING

打包员

Picker

STRING

拣货员

audit\_time

STRING

出库单审核时间

buyer\_memo

STRING

买家留言

buyer\_tax\_no

STRING

发票税号

common\_ext\_param

STRING

其他

created\_at

STRING

出库单创建时间

delivery\_print\_status

INTEGER

发货单打印状态

delivery\_time

STRING

出库时间

discount\_amount

DOUBLE

优惠金额

distributor\_id

STRING

分销商编号

document

STRING

审单员

erp\_mall\_no

STRING

erp 店铺编码

erp\_order\_sn

STRING

ERP 订单号

estimated\_weight

DOUBLE

预估重量

freight

DOUBLE

运费

invoice\_title

STRING

发票抬头

is\_cod

BOOLEAN

是否货到付款

items

OBJECT\[\]

明细列表

SN

STRING

SN 码

batch\_no

STRING

批次号

bu\_id

STRING

虚拟仓编码

combine\_sku\_id

STRING

组合装商品编码

expiration\_date

STRING

有效期至

is\_gift

DOUBLE

是否赠品

item\_common\_ext\_param

STRING

其他

name

STRING

名称

product\_date

STRING

批次日期

properties\_value

STRING

属性

quantity

INTEGER

商品数量

sale\_amount

DOUBLE

总金额

sale\_base\_price

DOUBLE

原价

sale\_price

DOUBLE

单价

sku\_id

STRING

商品编码

status

INTEGER

批次状态

sub\_order\_id

STRING

子订单号

supplier\_id

STRING

供应商编号

supplier\_name

STRING

供应商名称

labels

STRING

出库单标签

logistics\_company

STRING

快递公司名称

logistics\_id

LONG

快递公司编码

logistics\_print\_status

INTEGER

物流单打印状态

merge\_pdd\_order\_sn

STRING

拼多多合并订单号

node

STRING

线下备注

order\_type

INTEGER

订单类型

oub\_order\_code

STRING

出库单号

paid\_amount

DOUBLE

已支付金额

pay\_amount

DOUBLE

应付金额

pay\_time

STRING

付款时间

pdd\_mall\_id

LONG

拼多多店铺 id

pdd\_order\_sn

STRING

拼多多订单号

preparer

STRING

制单人

preparer\_name

STRING

制单人名称

printer

STRING

打单员

remark

STRING

卖家备注

remark\_tag

STRING

卖家旗帜

seller\_flag

STRING

旗帜

sorting\_print\_status

INTEGER

分拣单打印状态

status

INTEGER

出库单状态

tracking\_number

STRING

快递单号

updated\_at

STRING

修改时间

warehouse

STRING

仓库名称

wave\_id

STRING

拣货批次号

weight

DOUBLE

实际重量

wms\_co\_id

STRING

分仓编号

oub\_list\_get\_response

OBJECT

请求response

total\_count

INTEGER

10

出库单总数

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddErpOubListGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddErpOubListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddErpOubListGetRequest request = new PddErpOubListGetRequest();
        request.setErpMallNo("str");
        List<String> erpOrderSnList = new ArrayList<String>();
        erpOrderSnList.add("str");
        request.setErpOrderSnList(erpOrderSnList);
        List<String> oubOrderCodeList = new ArrayList<String>();
        oubOrderCodeList.add("str");
        request.setOubOrderCodeList(oubOrderCodeList);
        request.setPage(1);
        request.setPageSize(100);
        request.setPddMallId(1L);
        List<String> pddOrderSnList = new ArrayList<String>();
        pddOrderSnList.add("str");
        request.setPddOrderSnList(pddOrderSnList);
        request.setQueryTimeEnd(1L);
        request.setQueryTimeStart(1L);
        request.setQueryTimeType(1);
        request.setSid("str");
        request.setTargetClientId("your target client id");
        PddErpOubListGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "erp_request_id": "str",
  "has_next": true,
  "oub_list": [
    {
      "ClusterInfos": [
        {
          "oub_order_code": "str",
          "sub_logistics_company": "str",
          "sub_logistics_id": 0,
          "sub_tracking_number": "str"
        }
      ],
      "Inspector": "str",
      "Packer": "str",
      "Picker": "str",
      "audit_time": "str",
      "buyer_memo": "str",
      "buyer_tax_no": "str",
      "common_ext_param": "str",
      "created_at": "str",
      "delivery_print_status": 0,
      "delivery_time": "str",
      "discount_amount": 0.0,
      "distributor_id": "str",
      "document": "str",
      "erp_mall_no": "str",
      "erp_order_sn": "str",
      "estimated_weight": 0.0,
      "freight": 0.0,
      "invoice_title": "str",
      "is_cod": false,
      "items": [
        {
          "SN": "str",
          "batch_no": "str",
          "bu_id": "str",
          "combine_sku_id": "str",
          "expiration_date": "str",
          "is_gift": 0.0,
          "item_common_ext_param": "str",
          "name": "str",
          "product_date": "str",
          "properties_value": "str",
          "quantity": 0,
          "sale_amount": 0.0,
          "sale_base_price": 0.0,
          "sale_price": 0.0,
          "sku_id": "str",
          "status": 0,
          "sub_order_id": "str",
          "supplier_id": "str",
          "supplier_name": "str"
        }
      ],
      "labels": "str",
      "logistics_company": "str",
      "logistics_id": 0,
      "logistics_print_status": 0,
      "merge_pdd_order_sn": "str",
      "node": "str",
      "order_type": 0,
      "oub_order_code": "str",
      "paid_amount": 0.0,
      "pay_amount": 0.0,
      "pay_time": "str",
      "pdd_mall_id": 0,
      "pdd_order_sn": "str",
      "preparer": "str",
      "preparer_name": "str",
      "printer": "str",
      "remark": "str",
      "remark_tag": "str",
      "seller_flag": "str",
      "sorting_print_status": 0,
      "status": 0,
      "tracking_number": "str",
      "updated_at": "str",
      "warehouse": "str",
      "wave_id": "str",
      "weight": 0.0,
      "wms_co_id": "str"
    }
  ],
  "oub_list_get_response": {},
  "total_count": 10
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
