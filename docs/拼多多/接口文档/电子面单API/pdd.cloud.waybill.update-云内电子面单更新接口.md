---
title: "pdd.cloud.waybill.update - 云内电子面单更新接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.waybill.update"
menu_path:
  - "pdd.cloud.waybill.update"
captured_at: "2026-04-15T03:33:12.193Z"
---

# pdd.cloud.waybill.update

## 云内电子面单更新接口

更新时间：2022-07-04 10:36:36

¥免费API

不需用户授权

方舟

云内电子面单更新接口

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

waybill\_cloud\_print\_update\_request

OBJECT

非必填

订单面单更新接口

ext\_fields

STRING

非必填

扩展字段

ext\_id

LONG

非必填

扩展字段

mall\_id

LONG

非必填

店铺ID

object\_id

STRING

非必填

请求表示id

order\_sn

STRING

非必填

订单号

package\_info

OBJECT

非必填

包裹信息

items

OBJECT\[\]

非必填

商品

count

INTEGER

非必填

数量

ext\_json

STRING

非必填

扩展

name

STRING

非必填

名称

volume

LONG

非必填

体积

weight

LONG

非必填

重量

recipient

OBJECT

非必填

收件信息

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

国家/地区

detail

STRING

非必填

详细地址

district

STRING

非必填

区地址

province

STRING

非必填

省

town

STRING

非必填

街道

mobile

STRING

非必填

手机号码

name

STRING

非必填

姓名

phone

STRING

非必填

固定电话

sender

OBJECT

非必填

发件信息

mobile

STRING

非必填

手机号码

name

STRING

非必填

姓名

phone

STRING

非必填

固定电话

template\_url

STRING

非必填

模板URL

token

STRING

非必填

第三方token

waybill\_code

STRING

非必填

面单号

wp\_code

STRING

非必填

物流公司CODE

### 返回参数说明

参数接口

参数类型

例子

说明

pdd\_waybill\_update\_response

OBJECT

响应

error\_code

INTEGER

子错误码

error\_msg

STRING

错误信息

is\_success

BOOLEAN

是否成功，false-失败，true-成功

print\_data

STRING

模板内容

sub\_code

INTEGER

错误码

sub\_msg

STRING

子错误信息

waybill\_code

STRING

面单号

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillUpdateRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudWaybillUpdateResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillUpdateRequest.WaybillCloudPrintUpdateRequest;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillUpdateRequest.WaybillCloudPrintUpdateRequestPackageInfo;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillUpdateRequest.WaybillCloudPrintUpdateRequestPackageInfoItemsItem;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillUpdateRequest.WaybillCloudPrintUpdateRequestRecipient;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillUpdateRequest.WaybillCloudPrintUpdateRequestRecipientAddress;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudWaybillUpdateRequest.WaybillCloudPrintUpdateRequestSender;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudWaybillUpdateRequest request = new PddCloudWaybillUpdateRequest();

        WaybillCloudPrintUpdateRequest waybillCloudPrintUpdateRequest = new WaybillCloudPrintUpdateRequest();
        waybillCloudPrintUpdateRequest.setExtFields("{"key":"value"}");
        waybillCloudPrintUpdateRequest.setExtId(0L);
        waybillCloudPrintUpdateRequest.setMallId(121L);
        waybillCloudPrintUpdateRequest.setObjectId("str");
        waybillCloudPrintUpdateRequest.setOrderSn("200815-81289219128");

        WaybillCloudPrintUpdateRequestPackageInfo packageInfo = new WaybillCloudPrintUpdateRequestPackageInfo();
        List<WaybillCloudPrintUpdateRequestPackageInfoItemsItem> items = new ArrayList<WaybillCloudPrintUpdateRequestPackageInfoItemsItem>();

        WaybillCloudPrintUpdateRequestPackageInfoItemsItem item = new WaybillCloudPrintUpdateRequestPackageInfoItemsItem();
        item.setCount(0);
        item.setExtJson("str");
        item.setName("str");
        items.add(item);
        packageInfo.setItems(items);
        packageInfo.setVolume(0L);
        packageInfo.setWeight(0L);
        waybillCloudPrintUpdateRequest.setPackageInfo(packageInfo);

        WaybillCloudPrintUpdateRequestRecipient recipient = new WaybillCloudPrintUpdateRequestRecipient();

        WaybillCloudPrintUpdateRequestRecipientAddress address = new WaybillCloudPrintUpdateRequestRecipientAddress();
        address.setCity("str");
        address.setCountry("str");
        address.setDetail("str");
        address.setDistrict("str");
        address.setProvince("str");
        address.setTown("str");
        recipient.setAddress(address);
        recipient.setMobile("str");
        recipient.setName("str");
        recipient.setPhone("str");
        waybillCloudPrintUpdateRequest.setRecipient(recipient);

        WaybillCloudPrintUpdateRequestSender sender = new WaybillCloudPrintUpdateRequestSender();
        sender.setMobile("str");
        sender.setName("str");
        sender.setPhone("str");
        waybillCloudPrintUpdateRequest.setSender(sender);
        waybillCloudPrintUpdateRequest.setTemplateUrl("str");
        waybillCloudPrintUpdateRequest.setToken("str");
        waybillCloudPrintUpdateRequest.setWaybillCode("str");
        waybillCloudPrintUpdateRequest.setWpCode("str");
        request.setWaybillCloudPrintUpdateRequest(waybillCloudPrintUpdateRequest);
        request.setTargetClientId("your target client id");
        PddCloudWaybillUpdateResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "pdd_waybill_update_response": {
    "error_code": 0,
    "error_msg": "str",
    "is_success": false,
    "print_data": "str",
    "sub_code": 0,
    "sub_msg": "str",
    "waybill_code": "str"
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
