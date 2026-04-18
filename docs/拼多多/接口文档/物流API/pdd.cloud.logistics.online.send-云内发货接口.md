---
title: "pdd.cloud.logistics.online.send - 云内发货接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.logistics.online.send"
menu_path:
  - "pdd.cloud.logistics.online.send"
captured_at: "2026-04-15T03:32:52.576Z"
---

# pdd.cloud.logistics.online.send

## 云内发货接口

更新时间：2025-10-11 11:27:21

¥免费API

不需用户授权

方舟

服务部署在云内，通过方舟调用云内发货接口

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

ext\_param

STRING

非必填

扩展字段

ext\_token

STRING

非必填

第三方token

feature

STRING

非必填

发货个性内容，支持imei（手机串号），imei2（手机串号2），deviceSn（设备序列号），overseaTracing（海淘溯源码id）内容，appraisalCert（商品证书编号）。形如：“imei=识别码1,识别码2;”、“imei2=识别码;”、“ deviceSn=序列号1,序列号2;”、“ organicCode=有机码1,有机码2;”、“overseaTracing=溯源码1,溯源码2;”、“appraisalCert=商品证书编号1;”。以英文逗号“,”分割串号，以英文分号“;”分割不同参数内容。上传时请严格区分imei，deviceSn，organicCode，overseaTracing和appraisalCert，其中overseaTracing（海淘溯源码id）要求海淘商品在支持溯源的情况下必传，appraisalCert（商品证书编号）要求珠宝类商品在支持专业鉴定的情况下必传；deviceSn、imei（手机串号）、imei2（手机串号2）要求国补订单在此码已报送国家平台的情况下必传（形如：deviceSn=28978862659;imei=868904040681771;imei2=868904046817891;）；以上错传/漏传将会导致发货失败

logistics\_id

LONG

必填

快递公司编号

mall\_id

LONG

非必填

店铺ID

order\_sn

STRING

必填

订单号。形如：20150909-452750051

redelivery\_type

INTEGER

非必填

修改发货模式：不传则默认为首次发货 1=首次发货：用于订单首次发货，仅待发货订单可传入； 2=修改发货：用于订单修改发货，调用成功后将会覆盖原发货信息，仅已发货订单可传入

refund\_address\_id

STRING

非必填

退货地址的id，不填则取商家默认地址

sequence\_id

INTEGER

非必填

发货批次：普通订单无需传入，当前仅限 分批发货订单(考研图书等场景) 传入

tracking\_number

STRING

必填

快递单号

ship\_info\_list

OBJECT\[\]

非必填

发货凭证信息列表。以发货物流底单举例，形如：\[{ "type":1, "url":"XXXXXX" }\]，其中url需要通过【发货底单图片上传接口】上传对应图片获取。

type

INTEGER

非必填

发货凭证类型：1=发货物流底单

url

STRING

非必填

发货凭证链接，需要通过【发货底单图片上传接口】上传对应图片获取。

### 返回参数说明

参数接口

参数类型

例子

说明

logistics\_online\_send\_response

OBJECT

发货通知响应对象

error\_code

INTEGER

子错误码

error\_msg

STRING

错误信息

is\_success

BOOLEAN

true

是否成功，false-失败，true-成功

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
import com.pdd.pop.sdk.http.api.ark.request.PddCloudLogisticsOnlineSendRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudLogisticsOnlineSendResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudLogisticsOnlineSendRequest.ShipInfoListItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudLogisticsOnlineSendRequest request = new PddCloudLogisticsOnlineSendRequest();
        request.setExtParam("str");
        request.setExtToken("str");
        request.setFeature("str");
        request.setLogisticsId(200012L);
        request.setMallId(129L);
        request.setOrderSn("20150909-452750051");
        request.setRedeliveryType(1);
        request.setRefundAddressId("121");
        request.setSequenceId(1);
        request.setTrackingNumber("288781902");
        List<ShipInfoListItem> shipInfoList = new ArrayList<ShipInfoListItem>();

        ShipInfoListItem item = new ShipInfoListItem();
        item.setType(0);
        item.setUrl("str");
        shipInfoList.add(item);
        request.setShipInfoList(shipInfoList);
        request.setTargetClientId("your target client id");
        PddCloudLogisticsOnlineSendResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "logistics_online_send_response": {
    "error_code": 0,
    "error_msg": "str",
    "is_success": true,
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

接口总限流频次：62500次/10秒

### API工具
