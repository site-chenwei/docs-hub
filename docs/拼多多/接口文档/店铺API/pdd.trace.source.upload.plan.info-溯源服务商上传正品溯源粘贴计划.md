---
title: "pdd.trace.source.upload.plan.info - 溯源服务商上传正品溯源粘贴计划"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.trace.source.upload.plan.info"
menu_path:
  - "店铺API"
  - "pdd.trace.source.upload.plan.info"
captured_at: "2026-04-09T15:21:44.051Z"
---

# pdd.trace.source.upload.plan.info

## 溯源服务商上传正品溯源粘贴计划

更新时间：2021-03-10 17:37:09

¥免费API

必须用户授权

方舟

溯源服务商上传正品溯源粘贴计划, 用于正品溯源功能

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

### 请求参数说明

参数接口

参数类型

是否必填

说明

arrive\_time

STRING

非必填

到港日期

bill\_no

STRING

非必填

提单号

ciq\_date

STRING

非必填

报检日期

ciq\_no

STRING

非必填

报检单号

dealer\_org

STRING

非必填

境内收发货人

declare\_org

STRING

必填

申报单位

desp\_port\_name

STRING

必填

启运地

entry\_date

STRING

必填

报关日期

entry\_no

STRING

必填

报关单号

goods

OBJECT\[\]

必填

溯源码粘贴计划(商品维度)

code\_amount

LONG

必填

防伪溯源码粘贴数量

end\_serial\_no

STRING

必填

防伪溯源码结束顺序号

goods\_id

LONG

必填

商品ID

goods\_image\_url

STRING

非必填

商品备案图片

goods\_name

STRING

必填

商品备案名称

goods\_origin

STRING

必填

原产国(地)

goods\_property

STRING

必填

商品备案规格型号

goods\_sku\_no

STRING

必填

商品规格

hs\_code

STRING

必填

Hs编码

hs\_name

STRING

必填

Hs名称

start\_serial\_no

STRING

必填

防伪溯源码起始顺序号

list\_date

STRING

非必填

清单申报日期

list\_no

STRING

非必填

核注清单编号

load\_port

STRING

必填

装货港

mall\_id

LONG

必填

粘贴计划所属店铺ID

mall\_name

STRING

必填

粘贴计划所属店铺名

plan\_active\_time

STRING

必填

粘贴计划单激活时间

plan\_created\_time

STRING

必填

粘贴计划单创建时间

plan\_no

STRING

必填

粘贴计划单编号

port

STRING

必填

进口口岸

transport\_mode

STRING

必填

运输方式

warehouse\_name

STRING

必填

粘贴计划单所属保税仓名称

### 返回参数说明

参数接口

参数类型

例子

说明

response

OBJECT

status

INTEGER

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddTraceSourceUploadPlanInfoRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddTraceSourceUploadPlanInfoResponse;
import com.pdd.pop.sdk.http.api.ark.request.PddTraceSourceUploadPlanInfoRequest.GoodsItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddTraceSourceUploadPlanInfoRequest request = new PddTraceSourceUploadPlanInfoRequest();
        request.setArriveTime("str");
        request.setBillNo("str");
        request.setCiqDate("str");
        request.setCiqNo("str");
        request.setDealerOrg("str");
        request.setDeclareOrg("str");
        request.setDespPortName("str");
        request.setEntryDate("str");
        request.setEntryNo("str");
        List<GoodsItem> goods = new ArrayList<GoodsItem>();

        GoodsItem item = new GoodsItem();
        item.setCodeAmount(0L);
        item.setEndSerialNo("str");
        item.setGoodsId(0L);
        item.setGoodsImageUrl("str");
        item.setGoodsName("str");
        item.setGoodsOrigin("str");
        item.setGoodsProperty("str");
        item.setGoodsSkuNo("str");
        item.setHsCode("str");
        item.setHsName("str");
        item.setStartSerialNo("str");
        goods.add(item);
        request.setGoods(goods);
        request.setListDate("str");
        request.setListNo("str");
        request.setLoadPort("str");
        request.setMallId(0L);
        request.setMallName("str");
        request.setPlanActiveTime("str");
        request.setPlanCreatedTime("str");
        request.setPlanNo("str");
        request.setPort("str");
        request.setTransportMode("str");
        request.setWarehouseName("str");
        PddTraceSourceUploadPlanInfoResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "response": {
    "status": 0
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

方舟海淘溯源权限包

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

接口总限流频次：2500次/1秒

### API工具
