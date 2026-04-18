---
title: "pdd.goods.list.get - 商品列表接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.list.get"
menu_path:
  - "商品API"
  - "pdd.goods.list.get"
captured_at: "2026-04-09T15:16:33.390Z"
---

# pdd.goods.list.get

## 商品列表接口

更新时间：2022-07-14 20:50:40

¥基础API

必须用户授权

商品列表查询

### 公共参数

#### 请求地址（目前只提供正式环境，暂无沙箱环境）

| 环境 | HTTP地址 | HTTPS地址 |
| --- | --- | --- |
| 正式环境 | http://gw-api.pinduoduo.com/api/router | https://gw-api.pinduoduo.com/api/router |

#### 公共请求参数

| 参数名称 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | --- | --- |
| type | String | 必填 | API接口名称 |
| client\_id | String | 必填 | POP分配给应用的client\_id |
| access\_token | String | 非必填 | 通过code获取的access\_token |
| timestamp | String | 必填 | UNIX时间戳，单位秒，需要与拼多多服务器时间差值在10分钟内 |
| data\_type | String | 非必填 | 响应格式，即返回数据的格式，JSON或者XML（二选一），默认JSON，注意是大写 |
| version | String | 非必填 | API协议版本号，默认为V1，可不填 |
| sign | String | 必填 | API输入参数签名结果，签名算法参考开放平台接入指南第三部分底部。 |

### 请求参数说明

| 参数接口 | 参数类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| cost\_template\_id | LONG | 非必填 | 模版id |
| created\_at\_end | LONG | 非必填 | 商品创建时间结束时间的时间戳，指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至结束时间的总秒数 PS：开始时间结束时间间距不超过7天 |
| created\_at\_from | LONG | 非必填 | 商品创建时间开始时间的时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至开始时间的总秒数 |
| goods\_name | STRING | 非必填 | 商品名称模糊查询,outer\_id,is\_onsale,goods\_name三选一，优先级is\_onsale>outer\_id>goods\_name |
| is\_onsale | INTEGER | 非必填 | 上下架状态，0-下架，1-上架,outer\_id,is\_onsale,goods\_name三选一，优先级is\_onsale>outer\_id>goods\_name |
| outer\_goods\_id | STRING | 非必填 | 商家外部商品编码，支持多个，用逗号隔开，最多10个 |
| outer\_id | STRING | 非必填 | 商品外部编码（sku），同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。outer\_id,is\_onsale,goods\_name三选一，优先级is\_onsale>outer\_id>goods\_name |
| page | INTEGER | 非必填 | 返回页码 默认 1，页码从 1 开始PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值 |
| page\_size | INTEGER | 非必填 | 返回数量，默认 100，最大100。 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_list\_get\_response | OBJECT |  | 商品列表响应对象 |
| goods\_list | OBJECT\[\] |  | 商品列表对象 |
| created\_at | LONG |  | 商品创建时间的时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至商品创建时间的总秒数 |
| goods\_id | LONG |  | 商品编码 |
| goods\_name | STRING |  | 商品名称 |
| goods\_quantity | LONG |  | 商品总数量 |
| goods\_reserve\_quantity | LONG |  | 商品预扣库存 |
| image\_url | STRING |  | 商品图片 |
| is\_more\_sku | INTEGER |  | 是否多sku，0-单sku，1-多sku |
| is\_onsale | INTEGER |  | 是否在架上，0-下架中，1-架上 |
| sku\_list | OBJECT\[\] |  | sku列表对象 |
| is\_sku\_onsale | INTEGER |  | sku是否在架上，0-下架中，1-架上 |
| outer\_goods\_id | STRING |  | 商家外部编码（商品），同其他接口中的outer\_goods\_id 、out\_goods\_id、out\_goods\_sn、outer\_goods\_sn 都为商家编码（goods维度）。 |
| outer\_id | STRING |  | 商家外部编码（sku），同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。 |
| reserve\_quantity | LONG |  | sku预扣库存 |
| sku\_id | LONG |  | sku编码 |
| sku\_quantity | LONG |  | sku库存 |
| spec | STRING |  | 规格名称 |
| spec\_details | OBJECT\[\] |  | 规格信息 |
| parent\_id | LONG |  | 父规格id |
| parent\_name | STRING |  | 父规格名 |
| spec\_id | LONG |  | 子规格id |
| spec\_name | STRING |  | 子规格名称 |
| spec\_note | STRING |  | 规则备注 |
| thumb\_url | STRING |  | 商品缩略图 |
| total\_count | INTEGER |  | 返回商品总数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsListGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsListGetRequest request = new PddGoodsListGetRequest();
        request.setCostTemplateId(1L);
        request.setCreatedAtEnd(1654099200L);
        request.setCreatedAtFrom(1654012800L);
        request.setGoodsName("str");
        request.setIsOnsale(1);
        request.setOuterGoodsId("1");
        request.setOuterId("str");
        request.setPage(1);
        request.setPageSize(100);
        PddGoodsListGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_list_get_response": {
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

| 拥有此接口的权限包 | 可获得/可申请此权限包的应用类型 |
| --- | --- |
| 商品查询 | 打单、进销存、商品优化分析、虚拟商家后台系统、企业ERP、商家后台系统、订单处理、电子凭证商家后台系统、跨境企业ERP报关版 |

### 返回错误码说明

| 主错误码 | 主错误描述 | 子错误码 | 子错误描述 | 解决办法 |
| --- | --- | --- | --- | --- |
| 10000 | 参数错误 | 10000 | 参数错误 | 参数值有误，按照文档要求填写请求参数 |
| 10001 | 公共参数错误 | 10001 | 公共参数错误 | 请检查请求的公共参数 |
| 10016 | client下线或者clientId不正确 | 10016 | client下线或者clientId不正确 | 请核查您的client\_id是否正确 |
| 10017 | type不正确 | 10017 | type不正确 | 检查type是否正确 |
| 10018 | target\_client\_id下线或者target\_client\_id不正确 | 10018 | target\_client\_id下线或者target\_client\_id不正确 | 检查target\_client\_id 是否正确 |
| 10019 | access\_token已过期 | 10019 | access\_token已过期 | 刷新access\_token或者重新授权再次获取access\_token |
| 20004 | 签名sign校验失败 | 20004 | 签名sign校验失败 | 请按照接入指南第三部分指导，生成签名 |
| 20005 | ip无权访问接口，请加入ip白名单 | 20005 | ip无权访问接口，请加入ip白名单 | 把ip白名单加入白名单 |
| 20031 | 用户没有授权访问此接口 | 20031 | 用户没有授权访问此接口 | 您创建的应用中不包含此接口，请查看API文档，了解相关权限包 |
| 20032 | access\_token或client\_id错误 | 20032 | access\_token或client\_id错误 | 检查access\_token或client\_id |
| 20034 | 接口处于下线状态 | 20034 | 接口处于下线状态 | 检查接口状态 |
| 20035 | 接口不属于当前网关 | 20035 | 接口不属于当前网关 | 判断调用网关url 是否正确 |
| 21001 | 请求参数错误 | 21001 | 请求参数错误 | 业务参数输入错误 |
| 21002 | 请求参数不能为空 | 21002 | 请求参数不能为空 | 检查业务参数必填是否已填 |
| 30000 | 没有调用此target接口权限 | 30000 | 没有调用此target接口权限 | 检查是否获得调用此target接口权限 |
| 30001 | client\_id和partner\_id不匹配 | 30001 | client\_id和partner\_id不匹配 | 检查partner\_id是否正确 |
| 50000 | 系统内部错误 | 50000 | 系统内部错误 | 系统内部错误，请加群联系相关负责人 |
| 50002 | 业务系统内部异常 | 50002 | 业务系统内部异常 | 请加群联系相关负责人 |
| 52001 | 网关业务服务错误 | 52001 | 网关业务服务错误 | 联系技术支持解决 |
| 52002 | 网关系统内部异常 | 52002 | 网关系统内部异常 | 联系技术支持解决 |
| 52004 | 请求body 太大 | 52004 | 请求body 太大 | 检查请求体是否过大 |
| 52101 | 当前接口被限流，请稍后重试 | 52101 | 当前接口被限流，请稍后重试 | 当前接口被限流，请稍后重试 |
| 52102 | 当前接口暂时不可用，请稍后重试 | 52102 | 当前接口暂时不可用，请稍后重试 | 当前接口被降级，请稍后重试 |
| 52103 | 服务暂时不可用，请稍后重试 | 52103 | 服务暂时不可用，请稍后重试 | 当前接口被降级，请稍后重试 |
| 70031 | 调用过于频繁，请调整调用频率 | 70031 | 调用过于频繁，请调整调用频率 | 调用过于频繁，请调整调用频率 |
| 70032 | 当前请求被禁止调用 | 70032 | 当前请求被禁止调用 | 当前请求被禁止调用 |
| 70033 | 当前接口因系统维护，暂时下线，请稍后再试！ | 70033 | 当前接口因系统维护，暂时下线，请稍后再试！ | 当前接口因系统维护，暂时下线，请稍后再试！ |
| 70034 | 当前用户或应用存在风险，禁止调用！ | 70034 | 当前用户或应用存在风险，禁止调用！ | 当前用户或应用存在风险，禁止调用！ |
| 70035 | 当前用户或应用存在风险，禁止调用。请联系ddjb@pinduoduo.com | 70035 | 当前用户或应用存在风险，禁止调用。请联系ddjb@pinduoduo.com | 当前用户或应用存在风险，禁止调用。请联系ddjb@pinduoduo.com |
| 70036 | 应用处于测试状态，调用次数被限制 | 70036 | 应用处于测试状态，调用次数被限制 | 应用处于测试状态，调用次数达到上限被限制 |
| 50001 | 业务服务错误 |  |  |  |

### 限流规则

商家限流频次：1000次/60秒

接口总限流频次：7500次/1秒

### API工具
