---
title: "pdd.service.aftersales.appoint.notify - 售后服务预约通知接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.service.aftersales.appoint.notify"
menu_path:
  - "旅游门票API"
  - "pdd.service.aftersales.appoint.notify"
captured_at: "2026-04-09T15:25:26.818Z"
---

# pdd.service.aftersales.appoint.notify

## 售后服务预约通知接口

更新时间：2026-03-11 21:59:15

¥免费API

不需用户授权

方舟

通知服务商需要预约用户

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

request

OBJECT

非必填

业务参数

appointServEndTime

STRING

非必填

预约结束时间

appointServTime

STRING

非必填

预约开始时间

attributes

STRING

非必填

扩展信息，json格式，商品属性信息kv的形式保存

bizStatus

STRING

非必填

服务预约

contactInfo

OBJECT

非必填

联系人信息

addrDetail

STRING

非必填

详细地址

cityId

LONG

非必填

市id

cityName

STRING

非必填

市

contactName

STRING

非必填

联系人姓名

degradeReal

BOOLEAN

非必填

是否降级真实号

districtId

LONG

非必填

区id

districtName

STRING

非必填

区

expiredTime

LONG

非必填

虚拟号过期时间戳(ms)

extensionNumber

STRING

非必填

分机号

mobile

STRING

非必填

手机号

provId

LONG

非必填

省id

provName

STRING

非必填

省

telephone

STRING

非必填

联系人电话号码

virtualNumber

STRING

非必填

虚拟号

estimatedSignDate

STRING

非必填

预计签收日期

logisticsStatus

STRING

非必填

状态

mailNo

STRING

非必填

运单号

servOrderSn

STRING

非必填

服务单号

serviceTradeOrderSn

STRING

非必填

服务商品交易单号

signDate

STRING

非必填

签收日期

tradeOrderSn

STRING

非必填

交易单号

### 返回参数说明

参数接口

参数类型

例子

说明

response

OBJECT

{"success":true}

成功标志

errorCode

INTEGER

errorMsg

STRING

success

BOOLEAN

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddServiceAftersalesAppointNotifyRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddServiceAftersalesAppointNotifyResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddServiceAftersalesAppointNotifyRequest.Request;
import com.pdd.pop.sdk.http.api.ark.request.PddServiceAftersalesAppointNotifyRequest.RequestContactInfo;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddServiceAftersalesAppointNotifyRequest request = new PddServiceAftersalesAppointNotifyRequest();

        Request request1 = new Request();
        request1.setAppointServEndTime("2020-06-01 12:12:22");
        request1.setAppointServTime("2020-06-01 12:12:22");
        request1.setAttributes("str");
        request1.setBizStatus("appoint");

        RequestContactInfo contactInfo = new RequestContactInfo();
        contactInfo.setAddrDetail("str");
        contactInfo.setCityId(0L);
        contactInfo.setCityName("str");
        contactInfo.setContactName("str");
        contactInfo.setDegradeReal(false);
        contactInfo.setDistrictId(0L);
        contactInfo.setDistrictName("str");
        contactInfo.setExpiredTime(0L);
        contactInfo.setExtensionNumber("str");
        contactInfo.setMobile("str");
        contactInfo.setProvId(0L);
        contactInfo.setProvName("str");
        contactInfo.setTelephone("str");
        contactInfo.setVirtualNumber("str");
        request1.setContactInfo(contactInfo);
        request1.setEstimatedSignDate("2020-06-01");
        request1.setLogisticsStatus("signed-签收");
        request1.setMailNo("str");
        request1.setServOrderSn("str");
        request1.setServiceTradeOrderSn("str");
        request1.setSignDate("2020-06-01");
        request1.setTradeOrderSn("str");
        request.setRequest(request1);
        request.setTargetClientId("your target client id");
        PddServiceAftersalesAppointNotifyResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "response": {
    "errorCode": 0,
    "errorMsg": "str",
    "success": false
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

无忧购服务下发权限包

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
