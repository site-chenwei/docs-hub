---
title: "pdd.logistics.onlinedelivery.subsiby.shipbill.send - 商家寄件补贴活动快递公司账单下发接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.logistics.onlinedelivery.subsiby.shipbill.send"
menu_path:
  - "商家寄件API"
  - "pdd.logistics.onlinedelivery.subsiby.shipbill.send"
captured_at: "2026-04-09T15:26:38.665Z"
---

# pdd.logistics.onlinedelivery.subsiby.shipbill.send

## 商家寄件补贴活动快递公司账单下发接口

更新时间：2026-01-20 15:42:24

¥免费API

不需用户授权

方舟

针对商家寄件补贴活动下发快递公司账单,用于包裹重量核对以及对账

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

billDate

STRING

必填

账期，若一个寄件单T月重量未对齐，未参与结算，再次下发时，账期会调整为T+1月

billPrice

LONG

必填

账单金额，单位分

bizBillType

INTEGER

必填

账单类型。方便后续扩展 1：拼多多商家寄件补贴活动

deliveryReceiptSn

STRING

必填

寄件单号

mallPayPrice

LONG

必填

商家支付金额，单位分

mallPaySuccessTime

STRING

必填

商家支付成功时间

maxQuantityInclusive

INTEGER

必填

算价依赖单量区间上限(包含)

minQuantityInclusive

INTEGER

必填

算价依赖单量区间下限(包含)

pddWeight

INTEGER

必填

pdd推荐重量，单位：g

reviewFirstPrice

LONG

必填

首重价格（单价），单位分

reviewWeight

INTEGER

必填

快递侧核重重量，单位：g

reviewWeightPrice

LONG

必填

续重价格（单价），单位分

shipCode

STRING

必填

快递公司编码

technicalServiceAmount

LONG

必填

技术服务费，单位分

totalPrice

LONG

必填

总金额，单位分

waybillCode

STRING

必填

运单号

weightStatus

INTEGER

必填

双方重量是否一致 0：不一致，1：一致

### 返回参数说明

参数接口

参数类型

例子

说明

result

OBJECT

结果实体

result

BOOLEAN

true

是否下发成功

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddLogisticsOnlinedeliverySubsibyShipbillSendRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddLogisticsOnlinedeliverySubsibyShipbillSendResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddLogisticsOnlinedeliverySubsibyShipbillSendRequest request = new PddLogisticsOnlinedeliverySubsibyShipbillSendRequest();
        request.setBillDate("2025-11");
        request.setBillPrice(498L);
        request.setBizBillType(1);
        request.setDeliveryReceiptSn("OD25110812345678901200001");
        request.setMallPayPrice(1L);
        request.setMallPaySuccessTime("2025-11-18 12:34:56");
        request.setMaxQuantityInclusive(1);
        request.setMinQuantityInclusive(0);
        request.setPddWeight(2000);
        request.setReviewFirstPrice(300L);
        request.setReviewWeight(3000);
        request.setReviewWeightPrice(200L);
        request.setShipCode("JTSD");
        request.setTechnicalServiceAmount(1L);
        request.setTotalPrice(500L);
        request.setWaybillCode("JT123456789");
        request.setWeightStatus(0);
        request.setTargetClientId("your target client id");
        PddLogisticsOnlinedeliverySubsibyShipbillSendResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "result": {
    "result": true
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

方舟扫码寄件权限包

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

### API工具
