---
title: "pdd.cloud.waybill.get - 云内电子面单获取接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.waybill.get"
menu_path:
  - "pdd.cloud.waybill.get"
captured_at: "2026-04-15T03:33:08.158Z"
---

# pdd.cloud.waybill.get

## 云内电子面单获取接口

更新时间：2022-07-04 10:36:36

¥免费API

不需用户授权

方舟

友商云调用部署在云内的电子面单接口

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

param\_waybill\_cloud\_print\_apply\_new\_request

OBJECT

必填

入参信息

ext\_id

LONG

非必填

扩展字段

extendProps

STRING

非必填

扩展字段

need\_encrypt

BOOLEAN

非必填

设定取号返回的云打印报文是否加密

order\_sn

STRING

非必填

订单号

sender

OBJECT

必填

发货人信息

address

OBJECT

非必填

地址

city

STRING

非必填

城市

country

STRING

非必填

地区/国家

detail

STRING

必填

详细地址

district

STRING

非必填

街道

province

STRING

必填

省

town

STRING

非必填

街道

mobile

STRING

非必填

手机号

name

STRING

必填

姓名

phone

STRING

非必填

电话

token

STRING

非必填

第三方授权token

trade\_order\_info\_dtos

OBJECT\[\]

非必填

请求面单信息，数量限制为10

logistics\_services

STRING

非必填

物流服务内容链接

object\_id

STRING

非必填

请求id

order\_info

OBJECT

非必填

订单信息

order\_channels\_type

STRING

非必填

订单渠道平台编码

trade\_order\_list

STRING\[\]

非必填

订单号,数量限制100

package\_info

OBJECT

非必填

包裹信息

goods\_description

STRING

非必填

快运货品描述

id

STRING

非必填

包裹id,拆合单使用

items

OBJECT\[\]

非必填

商品信息,数量限制为100

count

INTEGER

非必填

数量

name

STRING

非必填

名称

packaging\_description

STRING

非必填

快运包装方式描述

total\_packages\_count

STRING

非必填

子母件总包裹数

volume

STRING

非必填

体积, 单位 ml

weight

STRING

非必填

重量,单位 g

recipient

OBJECT

非必填

收件人信息

address

OBJECT

非必填

地址

city

STRING

非必填

城市

country

STRING

非必填

地区/国家

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

mobile

STRING

非必填

手机号

name

STRING

非必填

姓名

phone

STRING

非必填

电话

template\_url

STRING

非必填

标准模板模板URL

user\_id

STRING

非必填

使用者ID

wp\_code

STRING

非必填

物流公司Code

mall\_id

LONG

非必填

店铺ID

### 返回参数说明

参数接口

参数类型

例子

说明

pdd\_waybill\_get\_response

OBJECT

响应结果

error\_code

INTEGER

子错误码

error\_msg

STRING

错误信息

is\_success

BOOLEAN

是否成功，false-失败，true-成功

modules

OBJECT\[\]

结果集

object\_id

STRING

请求id

parent\_waybill\_code

STRING

快运母单号

print\_data

STRING

面单信息

waybill\_code

STRING

面单号

sub\_code

INTEGER

错误码

sub\_msg

STRING

子错误信息

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudWaybillGetResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequest;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestSender;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestSenderAddress;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItem;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemOrderInfo;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfo;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfoItemsItem;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemRecipient;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillGetRequest.ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemRecipientAddress;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudWaybillGetRequest request = new PddCloudWaybillGetRequest();

        ParamWaybillCloudPrintApplyNewRequest paramWaybillCloudPrintApplyNewRequest = new ParamWaybillCloudPrintApplyNewRequest();
        paramWaybillCloudPrintApplyNewRequest.setExtId(0L);
        paramWaybillCloudPrintApplyNewRequest.setExtendProps("{"key":"value"}");
        paramWaybillCloudPrintApplyNewRequest.setNeedEncrypt(false);
        paramWaybillCloudPrintApplyNewRequest.setOrderSn("200815-781282178");

        ParamWaybillCloudPrintApplyNewRequestSender sender = new ParamWaybillCloudPrintApplyNewRequestSender();

        ParamWaybillCloudPrintApplyNewRequestSenderAddress address = new ParamWaybillCloudPrintApplyNewRequestSenderAddress();
        address.setCity("str");
        address.setCountry("str");
        address.setDetail("str");
        address.setDistrict("str");
        address.setProvince("str");
        address.setTown("str");
        sender.setAddress(address);
        sender.setMobile("str");
        sender.setName("str");
        sender.setPhone("str");
        paramWaybillCloudPrintApplyNewRequest.setSender(sender);
        paramWaybillCloudPrintApplyNewRequest.setToken("str");
        List<ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItem> tradeOrderInfoDtos = new ArrayList<ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItem>();

        ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItem item = new ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItem();
        item.setLogisticsServices("{ "SVC-COD": { "value": "200" } }");
        item.setObjectId("str");

        ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemOrderInfo orderInfo = new ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemOrderInfo();
        orderInfo.setOrderChannelsType("str");
        List<String> tradeOrderList = new ArrayList<String>();
        tradeOrderList.add("str");
        orderInfo.setTradeOrderList(tradeOrderList);
        item.setOrderInfo(orderInfo);

        ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfo packageInfo = new ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfo();
        packageInfo.setGoodsDescription("str");
        packageInfo.setId("str");
        List<ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfoItemsItem> items = new ArrayList<ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfoItemsItem>();

        ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfoItemsItem item1 = new ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemPackageInfoItemsItem();
        item1.setCount(0);
        item1.setName("str");
        items.add(item1);
        packageInfo.setItems(items);
        packageInfo.setPackagingDescription("str");
        packageInfo.setTotalPackagesCount("str");
        packageInfo.setVolume("str");
        packageInfo.setWeight("str");
        item.setPackageInfo(packageInfo);

        ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemRecipient recipient = new ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemRecipient();

        ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemRecipientAddress address1 = new ParamWaybillCloudPrintApplyNewRequestTradeOrderInfoDtosItemRecipientAddress();
        address1.setCity("str");
        address1.setCountry("str");
        address1.setDetail("str");
        address1.setDistrict("str");
        address1.setProvince("str");
        address1.setTown("str");
        recipient.setAddress(address1);
        recipient.setMobile("str");
        recipient.setName("str");
        recipient.setPhone("str");
        item.setRecipient(recipient);
        item.setTemplateUrl("str");
        item.setUserId("str");
        tradeOrderInfoDtos.add(item);
        paramWaybillCloudPrintApplyNewRequest.setTradeOrderInfoDtos(tradeOrderInfoDtos);
        paramWaybillCloudPrintApplyNewRequest.setWpCode("str");
        paramWaybillCloudPrintApplyNewRequest.setMallId(121L);
        request.setParamWaybillCloudPrintApplyNewRequest(paramWaybillCloudPrintApplyNewRequest);
        request.setTargetClientId("your target client id");
        PddCloudWaybillGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "pdd_waybill_get_response": {
    "error_code": 0,
    "error_msg": "str",
    "is_success": false,
    "modules": [
      {
        "object_id": "str",
        "parent_waybill_code": "str",
        "print_data": "str",
        "waybill_code": "str"
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

接口总限流频次：22500次/10秒

### API工具
