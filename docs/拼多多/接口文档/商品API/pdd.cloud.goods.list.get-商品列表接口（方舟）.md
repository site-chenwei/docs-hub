---
title: "pdd.cloud.goods.list.get - 商品列表接口（方舟）"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.goods.list.get"
menu_path:
  - "pdd.cloud.goods.list.get"
captured_at: "2026-04-15T03:32:49.559Z"
---

# pdd.cloud.goods.list.get

## 商品列表接口（方舟）

更新时间：2025-10-22 20:29:22

¥免费API

不需用户授权

方舟

多多云外调用多多云内服务，通过此接口查询商品列表查询（方舟）

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

cost\_template\_id

LONG

非必填

模版id

ext\_param

LONG

非必填

非必填，扩展字段

extend\_props

STRING

非必填

扩展字段

goods\_name

STRING

非必填

商品名称模糊查询,outer\_id,is\_onsale,goods\_name三选一，优先级is\_onsale>outer\_id>goods\_name

is\_onsale

INTEGER

非必填

上下架状态，0-下架，1-上架,outer\_id,is\_onsale,goods\_name三选一，优先级is\_onsale>outer\_id>goods\_name

mall\_id

LONG

非必填

非必填，店铺id

outer\_goods\_id

STRING

非必填

商家外部商品编码，支持多个，用逗号隔开，最多10个

outer\_id

STRING

非必填

商品外部编码（sku），同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。outer\_id,is\_onsale,goods\_name三选一，优先级is\_onsale>outer\_id>goods\_name

page

INTEGER

非必填

返回页码 默认 1，页码从 1 开始PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值

page\_size

INTEGER

非必填

返回数量，默认 100，最大100。

query\_time\_end

LONG

非必填

非必填 ， 查询结束时间(实现方自己定义类型)

query\_time\_from

LONG

非必填

非必填 ，查询开始时间(实现方自己定义类型)

query\_time\_type

INTEGER

非必填

非必填，查询时间类型，0：创建时间 1：更新时间

### 返回参数说明

参数接口

参数类型

例子

说明

goods\_list\_get\_response

OBJECT

商品列表响应对象

error\_code

INTEGER

错误码

error\_msg

STRING

错误信息

goods\_list

OBJECT\[\]

商品列表对象

created\_at

LONG

商品创建时间的时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至商品创建时间的总秒数

goods\_id

LONG

商品编码

goods\_name

STRING

商品名称

goods\_quantity

LONG

商品总数量

goods\_reserve\_quantity

LONG

商品预扣库存

image\_url

STRING

商品图片

is\_more\_sku

INTEGER

是否多sku，0-单sku，1-多sku

is\_onsale

INTEGER

是否在架上，0-下架中，1-架上

sku\_list

OBJECT\[\]

sku列表对象

is\_sku\_onsale

INTEGER

sku是否在架上，0-下架中，1-架上

outer\_goods\_id

STRING

商家外部编码（商品），同其他接口中的outer\_goods\_id 、out\_goods\_id、out\_goods\_sn、outer\_goods\_sn 都为商家编码（goods维度）。

outer\_id

STRING

商家外部编码（sku），同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。

reserve\_quantity

LONG

sku预扣库存

sku\_id

LONG

sku编码

sku\_quantity

LONG

sku库存

spec

STRING

规格名称

spec\_details

OBJECT\[\]

规格信息

parent\_id

LONG

父规格id

parent\_name

STRING

父规格名

spec\_id

LONG

子规格id

spec\_name

STRING

子规格名称

spec\_note

STRING

规则备注

thumb\_url

STRING

商品缩略图

sub\_code

INTEGER

子错误码

sub\_msg

STRING

子错误信息

total\_count

INTEGER

返回商品总数

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudGoodsListGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudGoodsListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudGoodsListGetRequest request = new PddCloudGoodsListGetRequest();
        request.setCostTemplateId(1L);
        request.setExtParam(12123L);
        request.setExtendProps("{"key":"value"}");
        request.setGoodsName("str");
        request.setIsOnsale(1);
        request.setMallId(2301L);
        request.setOuterGoodsId("str");
        request.setOuterId("str");
        request.setPage(1);
        request.setPageSize(10);
        request.setQueryTimeEnd(1121L);
        request.setQueryTimeFrom(1112L);
        request.setQueryTimeType(1);
        request.setTargetClientId("your target client id");
        PddCloudGoodsListGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_list_get_response": {
    "error_code": 0,
    "error_msg": "str",
    "goods_list": [
      {
        "created_at": 0,
        "goods_id": 0,
        "goods_name": "str",
        "goods_quantity": 0,
        "goods_reserve_quantity": 0,
        "image_url": "str",
        "is_more_sku": 0,
        "is_onsale": 0,
        "sku_list": [
          {
            "is_sku_onsale": 0,
            "outer_goods_id": "str",
            "outer_id": "str",
            "reserve_quantity": 0,
            "sku_id": 0,
            "sku_quantity": 0,
            "spec": "str",
            "spec_details": [
              {
                "parent_id": 0,
                "parent_name": "str",
                "spec_id": 0,
                "spec_name": "str",
                "spec_note": "str"
              }
            ]
          }
        ],
        "thumb_url": "str"
      }
    ],
    "sub_code": 0,
    "sub_msg": "str",
    "total_count": 0
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

接口总限流频次：17500次/2秒

### API工具
