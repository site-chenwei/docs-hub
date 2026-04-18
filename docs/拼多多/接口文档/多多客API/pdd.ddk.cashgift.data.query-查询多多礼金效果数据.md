---
title: "pdd.ddk.cashgift.data.query - 查询多多礼金效果数据"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ddk.cashgift.data.query"
menu_path:
  - "多多客API"
  - "pdd.ddk.cashgift.data.query"
captured_at: "2026-04-09T15:19:00.477Z"
---

# pdd.ddk.cashgift.data.query

## 查询多多礼金效果数据

更新时间：2025-02-27 19:52:31

¥免费API

不需用户授权

查询多多礼金效果数据

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
| cash\_gift\_id | LONG | 非必填 | 礼金ID，支持根据礼金ID查询 |
| end\_time | LONG | 非必填 | 礼金创建结束时间，查询该时间段内创建的所有礼金效果数据（礼金维度）。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |
| page | INTEGER | 非必填 | 分页数 |
| page\_size | INTEGER | 非必填 | 每页结果数 |
| start\_time | LONG | 非必填 | 礼金创建起始时间，查询该时间段内创建的所有礼金效果数据（礼金维度）。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| cashgift\_data\_response | OBJECT |  | response |
| available\_balance | LONG |  | 礼金账户余额，单位为分 |
| list | OBJECT\[\] |  | 多多礼金数据列表 |
| amount | LONG |  | 礼金券创建总金额，单位为分 |
| cash\_gift\_id | LONG |  | 礼金ID |
| cash\_gift\_name | STRING |  | 礼金名称 |
| couponAmount | INTEGER |  | 礼金券面额 |
| fetch\_amount | LONG |  | 已领取礼金券总金额，单位为分（实时数据） |
| fetch\_quantity | INTEGER |  | 已领取礼金券数量（实时数据） |
| goods\_info\_list | OBJECT\[\] |  | 商品列表信息 |
| coupon\_discount | LONG |  | 商品优惠券面额，单位为分 |
| goods\_name | STRING |  | 商品名称 |
| goods\_price | LONG |  | 商品原价，单位为分 |
| goods\_sign | STRING |  | 商品goodsSign，支持通过goodsSign查询商品。goodsSign是加密后的goodsId, goodsId已下线，请使用goodsSign来替代。使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252 |
| rate | INTEGER |  | 商品佣金比例，千分比 |
| is\_open\_renew | BOOLEAN |  | 是否开启续券 |
| order\_coupon\_amount | LONG |  | 礼金订单使用的券总金额，单位为分（实时数据） |
| order\_gmv | LONG |  | 礼金订单产生的总GMV，单位为分（实时数据） |
| order\_quantity | INTEGER |  | 礼金订单数量（实时数据） |
| pre\_promotion\_amount | LONG |  | 礼金订单预估佣金，单位为分（实时数据） |
| quantity | INTEGER |  | 礼金券创建总数量 |
| refund\_amount | LONG |  | 退回礼金券总金额，单位为分 |
| refund\_quantity | INTEGER |  | 退回礼金券数量 |
| remain\_count\_for\_renew | INTEGER |  | 触发续券的剩余券数量 |
| renew\_count\_today | INTEGER |  | 今日续券数量 |
| renew\_count\_total | INTEGER |  | 已续券总量 |
| renew\_max\_number\_per\_day | INTEGER |  | 单日续券上限，需要是每次续券的整数倍 |
| renew\_number\_per\_time | INTEGER |  | 每次续券上限 |
| status | INTEGER |  | 礼金状态：1-未生效；2-生效中；3-已过期；4-活动中止（用户主动停止）；5-活动中止（佣金降低）；6-活动中止（推广活动异常） |
| total | INTEGER |  | 请求到的结果数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkCashgiftDataQueryRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddDdkCashgiftDataQueryResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddDdkCashgiftDataQueryRequest request = new PddDdkCashgiftDataQueryRequest();
        request.setCashGiftId(0L);
        request.setEndTime(0L);
        request.setPage(1);
        request.setPageSize(20);
        request.setStartTime(0L);
        PddDdkCashgiftDataQueryResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "cashgift_data_response": {
    "available_balance": 0,
    "list": [
      {
        "amount": 0,
        "cash_gift_id": 0,
        "cash_gift_name": "str",
        "couponAmount": 0,
        "fetch_amount": 0,
        "fetch_quantity": 0,
        "goods_info_list": [
          {
            "coupon_discount": 0,
            "goods_name": "str",
            "goods_price": 0,
            "goods_sign": "str",
            "rate": 0
          }
        ],
        "is_open_renew": false,
        "order_coupon_amount": 0,
        "order_gmv": 0,
        "order_quantity": 0,
        "pre_promotion_amount": 0,
        "quantity": 0,
        "refund_amount": 0,
        "refund_quantity": 0,
        "remain_count_for_renew": 0,
        "renew_count_today": 0,
        "renew_count_total": 0,
        "renew_max_number_per_day": 0,
        "renew_number_per_time": 0,
        "status": 0
      }
    ],
    "total": 0
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
| 多多客权限包 | 多多客联盟 |

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

接口总限流频次：2500次/1秒

### API工具
