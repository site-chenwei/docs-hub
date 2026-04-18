---
title: "pdd.ticket.goods.query - 门票商品查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ticket.goods.query"
menu_path:
  - "旅游门票API"
  - "pdd.ticket.goods.query"
captured_at: "2026-04-09T15:24:58.576Z"
---

# pdd.ticket.goods.query

## 门票商品查询接口

更新时间：2021-11-03 22:06:37

¥免费API

必须用户授权

门票商品查询

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
| goods\_commit\_id | LONG | 非必填 | 草稿id，入参草稿id时，表示查询该草稿的信息 |
| goods\_id | LONG | 必填 | 商品id入参商品id时，表示查询该商品的线上商品信息。。 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_detail\_get\_response | OBJECT |  | 草稿查询返回结果 |
| carousel\_gallery | STRING\[\] |  | 商品轮播图 |
| carousel\_video | OBJECT\[\] |  | 轮播视频 |
| file\_id | LONG |  | 轮播视频id |
| video\_url | STRING |  | 轮播视频url |
| cat\_id | INTEGER |  | 类目id，国内门票（含港澳台）9088，国外门票20042。 |
| code\_mode | INTEGER |  | 电子票发码方式，0=手动电子票；1=实时电子票，自动发货。 |
| commit\_status | INTEGER |  | 商品草稿状态，查询草稿id时返回。0=编辑中，1=待审核，2=审核通过，3=审核驳回 |
| detail\_gallery | STRING\[\] |  | 商品详情图 |
| goods\_desc | STRING |  | 商品描述 |
| goods\_name | STRING |  | 商品标题 |
| goods\_properties | OBJECT\[\] |  | 商品属性 |
| parent\_spec\_id | LONG |  | 父规格id，仅销售属性有 |
| ref\_pid | LONG |  | 引用属性id |
| spec\_id | LONG |  | 规格id，仅销售属性有和sku中的spec对应 |
| value | STRING |  | 属性值 |
| value\_unit | STRING |  | 属性值单位 |
| vid | LONG |  | 属性值id |
| goods\_status | INTEGER |  | 商品状态，查询商品id时返回。1=上架，2=下架，3=售罄，4=已删除 |
| market\_price | LONG |  | 商品参考价，单位为分。 |
| out\_goods\_sn | STRING |  | 商品goods外部编码，同其他接口中的outer\_goods\_id 、out\_goods\_id、out\_goods\_sn、outer\_goods\_sn 都为商品维度的商家编码。 |
| reserve\_limit\_rule | STRING |  | 预定时间限制，格式：1\_20\_00，含义：需要提前1天，且在20:00分之前才可预定那天的门票。若为空则表示不限制预定时间。0\_24\_00表示在当前的24点前预定都可以，等效于不限制预定时间。 |
| sku\_list | OBJECT\[\] |  | sku列表 |
| child\_skus | OBJECT\[\] |  | 子sku列表，仅当sku\_type为日历库存且父sku数小于等于10个时返回。若父sku多于10个，需要在pdd.goods.child.sku.detail.get接口中查询子sku信息。 |
| date | STRING |  | 日期。格式：2020-06-01 |
| group\_price | LONG |  | 拼团价，单位为分。 |
| quantity | LONG |  | 线上库存 |
| quantity\_delta | LONG |  | 库存增减，当查草稿时返回。 |
| reserve\_quantity | LONG |  | 线上预扣库存 |
| single\_price | LONG |  | 单买价，单位为分 |
| sku\_id | LONG |  | skuId |
| group\_price | LONG |  | 拼团价，单位为分。当sku\_type为日历库存时是可预定日期的拼团价最低价。 |
| is\_onsale | INTEGER |  | 上架状态。0=已下架，1=已上架。 |
| out\_sku\_sn | STRING |  | 商品sku外部编码，同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。 |
| quantity | LONG |  | 线上库存量 |
| quantity\_delta | LONG |  | 库存增减，当查草稿时返回。 |
| reserve\_quantity | LONG |  | 线上预扣库存量 |
| rule\_id | STRING |  | 调pdd.scenic.sku.rule.get得到的规则id |
| single\_price | LONG |  | 单买价，单位为分。当sku\_type为日历库存时是可预定日期的单买价最低价。 |
| sku\_id | STRING |  | skuId |
| spec | OBJECT\[\] |  | sku规格列表 |
| parent\_id | LONG |  | 父规格id |
| parent\_name | STRING |  | 父规格名称 |
| spec\_id | LONG |  | 规格id |
| spec\_name | STRING |  | 规格名称 |
| thumb\_url | STRING |  | SKU预览图 |
| sku\_type | INTEGER |  | 销售方式，0=普通库存，1=日历库存。 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketGoodsQueryRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddTicketGoodsQueryResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddTicketGoodsQueryRequest request = new PddTicketGoodsQueryRequest();
        request.setGoodsCommitId(1024L);
        request.setGoodsId(1024L);
        PddTicketGoodsQueryResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_detail_get_response": {
    "carousel_gallery": [
      "str"
    ],
    "carousel_video": [
      {
        "file_id": 0,
        "video_url": "str"
      }
    ],
    "cat_id": 0,
    "code_mode": 0,
    "commit_status": 0,
    "detail_gallery": [
      "str"
    ],
    "goods_desc": "str",
    "goods_name": "str",
    "goods_properties": [
      {
        "parent_spec_id": 0,
        "ref_pid": 0,
        "spec_id": 0,
        "value": "str",
        "value_unit": "str",
        "vid": 0
      }
    ],
    "goods_status": 0,
    "market_price": 0,
    "out_goods_sn": "str",
    "reserve_limit_rule": "str",
    "sku_list": [
      {
        "child_skus": [
          {
            "date": "str",
            "group_price": 0,
            "quantity": 0,
            "quantity_delta": 0,
            "reserve_quantity": 0,
            "single_price": 0,
            "sku_id": 0
          }
        ],
        "group_price": 0,
        "is_onsale": 0,
        "out_sku_sn": "str",
        "quantity": 0,
        "quantity_delta": 0,
        "reserve_quantity": 0,
        "rule_id": "str",
        "single_price": 0,
        "sku_id": "str",
        "spec": [
          {
            "parent_id": 0,
            "parent_name": "str",
            "spec_id": 0,
            "spec_name": "str"
          }
        ],
        "thumb_url": "str"
      }
    ],
    "sku_type": 0
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
| 旅游门票商品管理权限包 |  |

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

接口总限流频次：500次/1秒

### API工具
