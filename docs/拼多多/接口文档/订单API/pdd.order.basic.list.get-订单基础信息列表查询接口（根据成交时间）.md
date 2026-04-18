---
title: "pdd.order.basic.list.get - 订单基础信息列表查询接口（根据成交时间）"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.order.basic.list.get"
menu_path:
  - "订单API"
  - "pdd.order.basic.list.get"
captured_at: "2026-04-09T15:12:48.398Z"
---

# pdd.order.basic.list.get

## 订单基础信息列表查询接口（根据成交时间）

更新时间：2020-07-14 20:01:15

¥免费API

必须用户授权

根据成团时间查询订单列表，只有订单基础信息，不包含消费者信息

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
| end\_confirm\_at | INTEGER | 必填 | 必填，成交时间结束时间的时间戳，指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 PS：开始时间结束时间间距不超过 24 小时 |
| order\_status | INTEGER | 必填 | 发货状态，1：待发货，2：已发货待签收，3：已签收 5：全部 |
| page | INTEGER | 必填 | 返回页码 默认 1，页码从 1 开始 PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值 |
| page\_size | INTEGER | 必填 | 返回数量，默认 100。最大 100 |
| refund\_status | INTEGER | 必填 | 售后状态 1：无售后或售后关闭，2：售后处理中，3：退款中，4： 退款成功 5：全部 |
| start\_confirm\_at | INTEGER | 必填 | 必填，成交时间开始时间的时间戳，指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |
| trade\_type | INTEGER | 非必填 | 订单类型 0-普通订单 ，1- 定金订单 |
| use\_has\_next | BOOLEAN | 非必填 | 是否启用has\_next的分页方式，如果指定true,则返回的结果中不包含总记录数，但是会新增一个是否存在下一页的的字段，通过此种方式获取增量交易，效率在原有的基础上有80%的提升。 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| order\_basic\_list\_get\_response | OBJECT | 1 | 请求response |
| has\_next | BOOLEAN |  | 是否存在下一页 |
| order\_list | OBJECT\[\] | 1 | 订单信息列表 |
| cat\_id\_1 | LONG | 1 | 商品一级分类 |
| cat\_id\_2 | LONG | 1 | 商品二级分类 |
| cat\_id\_3 | LONG | 1 | 商品三级分类 |
| cat\_id\_4 | LONG | 1 | 商品四级分类 |
| confirm\_time | STRING | 1 | 成交时间 |
| delivery\_home\_value | DOUBLE | 1 | 送货入户费用 单位：元 |
| delivery\_install\_value | DOUBLE | 1 | 送货入户并安装费用 单位：元 |
| discount\_amount | DOUBLE | 1 | 折扣金额，单位：元，折扣金额=平台优惠+商家优惠+团长免单优惠金额 |
| goods\_amount | DOUBLE | 1 | 商品金额，单位：元，商品金额=商品销售价格\*商品数量-改价金额（接口暂无该字段） |
| home\_delivery\_type | INTEGER | 1 | 送货入户并安装服务 0-不支持送货，1-送货入户不安装，2-送货入户并安装 |
| home\_install\_value | DOUBLE | 1 | 上门安装费用 单位：元 |
| is\_lucky\_flag | INTEGER | 1 | 是否是抽奖订单，1-非抽奖订单，2-抽奖订单 |
| item\_list | OBJECT\[\] | 1 | 订单商品列表 |
| goods\_count | INTEGER | 1 | 商品数量 |
| goods\_id | STRING | 1 | 商品编码 |
| goods\_img | STRING | 1 | 商品图片 |
| goods\_name | STRING | 1 | 商品名称 |
| goods\_price | DOUBLE | 1 | 商品单件 单价：元 |
| goods\_spec | STRING | 1 | 商品规格 |
| outer\_goods\_id | STRING | 1 | 商品维度外部编码，注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。 |
| outer\_id | STRING | 1 | sku维度商家外部编码，注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。 |
| sku\_id | STRING | 1 | 商品sku编码 |
| order\_sn | STRING | 1 | 订单编号 |
| order\_status | INTEGER | 1 | 订单状态 |
| pay\_amount | DOUBLE | 1 | 支付金额，单位：元，支付金额=商品金额-折扣金额+邮费 |
| platform\_discount | DOUBLE | 1 | 平台优惠金额，单位：元 |
| postage | DOUBLE | 1 | 邮费，单位：元 |
| refund\_status | INTEGER | 1 | 售后状态 |
| risk\_control\_status | INTEGER |  | 订单审核状态（0-正常订单， 1-审核中订单） |
| seller\_discount | DOUBLE | 1 | 商家优惠金额，单位：元 |
| step\_order\_info | OBJECT | 1 | { "step\_discount\_amount":4, "advanced\_paid\_fee":1, "step\_paid\_fee":1.1, "step\_trade\_status":2 } |
| advanced\_paid\_fee | DOUBLE | 1 | 已付定金 单位：元 |
| step\_discount\_amount | DOUBLE | 1 | 膨胀金额 单位：元 |
| step\_paid\_fee | DOUBLE | 1 | 分阶段已付金额 单位：元 |
| step\_trade\_status | INTEGER | 1 | 定金订单状态：step\_trade\_status 枚举：0-定金未付尾款未付、1-定金已付尾款未付、2-定金已付尾款已付 |
| trade\_type | INTEGER | 1 | 订单类型 0-普通订单 ，1- 定金订单 |
| updated\_at | STRING | 1 | 订单的更新时间 |
| total\_count | INTEGER | 1 | 订单总数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddOrderBasicListGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddOrderBasicListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddOrderBasicListGetRequest request = new PddOrderBasicListGetRequest();
        request.setEndConfirmAt(1);
        request.setOrderStatus(1);
        request.setPage(1);
        request.setPageSize(1);
        request.setRefundStatus(1);
        request.setStartConfirmAt(1);
        request.setTradeType(1);
        request.setUseHasNext(false);
        PddOrderBasicListGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "order_basic_list_get_response": {
    "has_next": false,
    "order_list": [
      {
        "cat_id_1": 1,
        "cat_id_2": 1,
        "cat_id_3": 1,
        "cat_id_4": 1,
        "confirm_time": "1",
        "delivery_home_value": 1.0,
        "delivery_install_value": 1.0,
        "discount_amount": 1.0,
        "goods_amount": 1.0,
        "home_delivery_type": 1,
        "home_install_value": 1.0,
        "is_lucky_flag": 1,
        "item_list": [
          {
            "goods_count": 1,
            "goods_id": "1",
            "goods_img": "1",
            "goods_name": "1",
            "goods_price": 1.0,
            "goods_spec": "1",
            "outer_goods_id": "1",
            "outer_id": "1",
            "sku_id": "1"
          }
        ],
        "order_sn": "1",
        "order_status": 1,
        "pay_amount": 1.0,
        "platform_discount": 1.0,
        "postage": 1.0,
        "refund_status": 1,
        "risk_control_status": 0,
        "seller_discount": 1.0,
        "step_order_info": {
          "advanced_paid_fee": 1.0,
          "step_discount_amount": 1.0,
          "step_paid_fee": 1.0,
          "step_trade_status": 1
        },
        "trade_type": 1,
        "updated_at": "1"
      }
    ],
    "total_count": 1
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
| 订单基础信息查询权限包 | 进销存、商品优化分析 |

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

接口总限流频次：3750次/1秒

### API工具
