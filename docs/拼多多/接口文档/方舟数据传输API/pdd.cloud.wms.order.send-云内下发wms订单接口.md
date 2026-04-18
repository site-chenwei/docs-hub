---
title: "pdd.cloud.wms.order.send - 云内下发wms订单接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.wms.order.send"
menu_path:
  - "pdd.cloud.wms.order.send"
captured_at: "2026-04-15T03:33:18.275Z"
---

# pdd.cloud.wms.order.send

## 云内下发wms订单接口

更新时间：2021-06-10 15:35:33

¥免费API

不需用户授权

方舟

云内下发wms订单接口

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

wms\_order\_send\_request

OBJECT

非必填

订单下发wms请求

owner\_code

STRING

非必填

货主编码

owner\_name

STRING

非必填

货主名称

warehouse\_code

STRING

非必填

仓库编码

warehouse\_type

STRING

非必填

仓库类型

order\_type

STRING

非必填

单据类型

delivery\_order\_code

STRING

非必填

出库单号

source\_order\_code

STRING

非必填

原始平台单号

source\_platform\_code

STRING

非必填

订单来源平台编码

shop\_nick

STRING

非必填

卖家店铺名称

seller\_nick

STRING

非必填

卖家名称

buyer\_nick

STRING

非必填

买家名称

create\_time

STRING

非必填

创建时间

order\_time

STRING

非必填

下单时间

pay\_time

STRING

非必填

付款时间

operate\_time

STRING

非必填

操作(审核)时间

order\_flag

STRING

非必填

订单标记(用字符串格式来表示订单标记列表

total\_amount

INTEGER

非必填

订单总金额

discount\_amount

INTEGER

非必填

订单折扣金额

freight

INTEGER

非必填

快递费

actual\_amount

INTEGER

非必填

实收金额

logistics\_code

STRING

非必填

快递公司编码

logistics\_no

STRING

非必填

快递单号

seller\_message

STRING

非必填

卖家留言

buyer\_message

STRING

非必填

买家留言

invoice\_flag

BOOLEAN

非必填

是否需要发票

invoice\_info

OBJECT

非必填

发票

invoice\_type

STRING

非必填

发票类型

invoice\_head

STRING

非必填

发票抬头

invoice\_content

STRING

非必填

发票内容

invoice\_tax\_number

STRING

非必填

税号

invoice\_ext\_fields

STRING

非必填

扩展字段

remark

STRING

非必填

备注信息

no\_stack\_tag

STRING

非必填

无库存标记 预售

senderInfo

OBJECT

非必填

发件人信息

address

OBJECT

非必填

地址信息

city

STRING

非必填

城市

detail

STRING

非必填

详细地址

district

STRING

非必填

街道

province

STRING

非必填

省

town

STRING

非必填

镇

country

STRING

非必填

地区/国家

mobile

STRING

非必填

电话

name

STRING

非必填

姓名

phone

STRING

非必填

手机

zipcode

STRING

非必填

邮编

receiverInfo

OBJECT

非必填

收件人信息

address

OBJECT

非必填

地址信息

city

STRING

非必填

城市

detail

STRING

非必填

详细地址

district

STRING

非必填

街道

province

STRING

非必填

省

town

STRING

非必填

镇

country

STRING

非必填

地区/国家

mobile

STRING

非必填

电话

name

STRING

非必填

姓名

phone

STRING

非必填

手机

zipcode

STRING

非必填

邮编

order\_line\_list

OBJECT\[\]

非必填

订单列表，商品明细

order\_line\_no

STRING

非必填

单据行号

source\_order\_code

STRING

非必填

交易平台订单

sub\_source\_order\_code

STRING

非必填

子交易单号

owner\_code

STRING

非必填

货主编码

item\_id

STRING

非必填

仓储系统商品编码

item\_code

STRING

非必填

商品编码

item\_name

STRING

非必填

商品名称

item\_quantity

INTEGER

非必填

应发商品数量

retail\_price

STRING

非必填

零售价

actual\_price

STRING

非必填

实际成交价

discount\_amount

STRING

非必填

单件商品折扣金额

batch\_code

STRING

非必填

批次编码

remark

STRING

非必填

备注

order\_ext\_fields

STRING

非必填

商品扩展字段

extendProps

STRING

非必填

自定义字段

token

STRING

非必填

第三方token

customerId

STRING

非必填

客户编码

### 返回参数说明

参数接口

参数类型

例子

说明

send\_response

OBJECT

响应

data

OBJECT

响应数据

delivery\_order\_id

STRING

出库单仓储系统编码

logistics\_code

STRING

物流公司编码

warehouse\_code

STRING

仓库编码

warehouse\_type

STRING

仓库类型

create\_time

STRING

订单创建时间(YYYY-MM-DD HH:MM:SS)

is\_success

BOOLEAN

fasle

是否成功，false-失败，true-成功

error\_msg

STRING

错误信息

sub\_msg

STRING

子错误信息

sub\_code

INTEGER

子错误码

error\_code

INTEGER

错误码

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudWmsOrderSendResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest.WmsOrderSendRequest;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest.WmsOrderSendRequestInvoiceInfo;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest.WmsOrderSendRequestSenderInfo;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest.WmsOrderSendRequestSenderInfoAddress;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest.WmsOrderSendRequestReceiverInfo;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest.WmsOrderSendRequestReceiverInfoAddress;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWmsOrderSendRequest.WmsOrderSendRequestOrderLineListItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudWmsOrderSendRequest request = new PddCloudWmsOrderSendRequest();

        WmsOrderSendRequest wmsOrderSendRequest = new WmsOrderSendRequest();
        wmsOrderSendRequest.setOwnerCode("str");
        wmsOrderSendRequest.setOwnerName("str");
        wmsOrderSendRequest.setWarehouseCode("str");
        wmsOrderSendRequest.setWarehouseType("str");
        wmsOrderSendRequest.setOrderType("str");
        wmsOrderSendRequest.setDeliveryOrderCode("str");
        wmsOrderSendRequest.setSourceOrderCode("str");
        wmsOrderSendRequest.setSourcePlatformCode("str");
        wmsOrderSendRequest.setShopNick("str");
        wmsOrderSendRequest.setSellerNick("str");
        wmsOrderSendRequest.setBuyerNick("str");
        wmsOrderSendRequest.setCreateTime("str");
        wmsOrderSendRequest.setOrderTime("str");
        wmsOrderSendRequest.setPayTime("str");
        wmsOrderSendRequest.setOperateTime("str");
        wmsOrderSendRequest.setOrderFlag("str");
        wmsOrderSendRequest.setTotalAmount(0);
        wmsOrderSendRequest.setDiscountAmount(0);
        wmsOrderSendRequest.setFreight(0);
        wmsOrderSendRequest.setActualAmount(0);
        wmsOrderSendRequest.setLogisticsCode("str");
        wmsOrderSendRequest.setLogisticsNo("str");
        wmsOrderSendRequest.setSellerMessage("str");
        wmsOrderSendRequest.setBuyerMessage("str");
        wmsOrderSendRequest.setInvoiceFlag(false);

        WmsOrderSendRequestInvoiceInfo invoiceInfo = new WmsOrderSendRequestInvoiceInfo();
        invoiceInfo.setInvoiceType("str");
        invoiceInfo.setInvoiceHead("str");
        invoiceInfo.setInvoiceContent("str");
        invoiceInfo.setInvoiceTaxNumber("str");
        invoiceInfo.setInvoiceExtFields("{"key":"value"}");
        wmsOrderSendRequest.setInvoiceInfo(invoiceInfo);
        wmsOrderSendRequest.setRemark("str");
        wmsOrderSendRequest.setNoStackTag("str");

        WmsOrderSendRequestSenderInfo senderInfo = new WmsOrderSendRequestSenderInfo();

        WmsOrderSendRequestSenderInfoAddress address = new WmsOrderSendRequestSenderInfoAddress();
        address.setCity("str");
        address.setDetail("str");
        address.setDistrict("str");
        address.setProvince("str");
        address.setTown("str");
        address.setCountry("str");
        senderInfo.setAddress(address);
        senderInfo.setMobile("str");
        senderInfo.setName("str");
        senderInfo.setPhone("str");
        senderInfo.setZipcode("str");
        wmsOrderSendRequest.setSenderInfo(senderInfo);

        WmsOrderSendRequestReceiverInfo receiverInfo = new WmsOrderSendRequestReceiverInfo();

        WmsOrderSendRequestReceiverInfoAddress address1 = new WmsOrderSendRequestReceiverInfoAddress();
        address1.setCity("str");
        address1.setDetail("str");
        address1.setDistrict("str");
        address1.setProvince("str");
        address1.setTown("str");
        address1.setCountry("str");
        receiverInfo.setAddress(address1);
        receiverInfo.setMobile("str");
        receiverInfo.setName("str");
        receiverInfo.setPhone("str");
        receiverInfo.setZipcode("str");
        wmsOrderSendRequest.setReceiverInfo(receiverInfo);
        List<WmsOrderSendRequestOrderLineListItem> orderLineList = new ArrayList<WmsOrderSendRequestOrderLineListItem>();

        WmsOrderSendRequestOrderLineListItem item = new WmsOrderSendRequestOrderLineListItem();
        item.setOrderLineNo("str");
        item.setSourceOrderCode("str");
        item.setSubSourceOrderCode("str");
        item.setOwnerCode("str");
        item.setItemId("str");
        item.setItemCode("str");
        item.setItemName("str");
        item.setItemQuantity(0);
        item.setRetailPrice("str");
        item.setActualPrice("str");
        item.setDiscountAmount("str");
        item.setBatchCode("str");
        item.setRemark("str");
        item.setOrderExtFields("str");
        orderLineList.add(item);
        wmsOrderSendRequest.setOrderLineList(orderLineList);
        wmsOrderSendRequest.setExtendProps("{"key":"value"}");
        wmsOrderSendRequest.setToken("str");
        wmsOrderSendRequest.setCustomerId("str");
        request.setWmsOrderSendRequest(wmsOrderSendRequest);
        request.setTargetClientId("your target client id");
        PddCloudWmsOrderSendResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "send_response": {
    "data": {
      "create_time": "str",
      "delivery_order_id": "str",
      "logistics_code": "str",
      "warehouse_code": "str",
      "warehouse_type": "str"
    },
    "error_code": 0,
    "error_msg": "str",
    "is_success": false,
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

接口总限流频次：5000次/1秒

### API工具
