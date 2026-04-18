---
title: "pdd.ddk.all.order.list.increment.get - 查询所有授权的多多客订单"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ddk.all.order.list.increment.get"
menu_path:
  - "多多客工具API"
  - "pdd.ddk.all.order.list.increment.get"
captured_at: "2026-04-09T15:19:29.167Z"
---

# pdd.ddk.all.order.list.increment.get

## 查询所有授权的多多客订单

更新时间：2026-02-09 11:02:51

¥免费API

不需用户授权

按照时间段获取授权多多客下面所有多多客的推广订单信息

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
| end\_update\_time | LONG | 必填 | 查询结束时间，和开始时间相差不能超过24小时。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |
| page | INTEGER | 非必填 | 第几页，从1到10000，默认1，注：使用最后更新时间范围增量同步时，必须采用倒序的分页方式（从最后一页往回取）才能避免漏单问题。 |
| page\_size | INTEGER | 非必填 | 返回的每页结果订单数，默认为100，范围为10到100，建议使用40~50，可以提高成功率，减少超时数量。 |
| query\_order\_type | INTEGER | 非必填 | 订单类型：1-推广订单；2-直播间订单 |
| start\_update\_time | LONG | 必填 | 最近90天内多多进宝商品订单更新时间--查询时间开始。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| order\_list\_get\_response | OBJECT |  | order\_list\_get\_response |
| order\_list | OBJECT\[\] |  | 多多进宝推广位对象列表 |
| activity\_tags | INTEGER\[\] |  | 商品活动标记数组，例：\[4,7\]，4-秒杀 7-百亿补贴等 |
| auth\_duo\_id | LONG |  | 多多客工具id |
| auth\_duo\_id\_service\_fee | LONG |  | 场景工具商软件服务费，单位为分 |
| bandan\_risk\_consult | INTEGER |  | 预判断是否为代购订单，-1（默认）表示未出结果，0表示预判不是代购订单，1表示代购订单，具体请以最后审核状态为准 |
| batch\_no | STRING |  | 结算批次号 |
| cash\_gift\_id | LONG |  | 订单关联礼金活动Id |
| cat\_ids | LONG\[\] |  | 商品一~四级类目ID列表 |
| cpa\_new | INTEGER |  | 是否是 cpa 新用户，1表示是，0表示否 |
| cps\_level | INTEGER |  | 0-普通订单 3-限时补贴订单 |
| custom\_parameters | STRING |  | 自定义参数 |
| duo\_id\_service\_fee | LONG |  | 软件服务费，为基础佣金及奖励佣金之和所对应的软件服务费，单位为分 |
| fail\_reason | STRING |  | 订单审核失败/惩罚原因 |
| goods\_category\_name | STRING |  | 商品一级类目名称 |
| goods\_id | LONG |  | 商品ID |
| goods\_name | STRING |  | 商品标题 |
| goods\_price | LONG |  | 订单中sku的单件价格，单位为分 |
| goods\_quantity | LONG |  | 购买商品的数量 |
| goods\_sign | STRING |  | goodsSign是加密后的goodsId，goodsId已下线，请使用goodsSign来替代。需要注意的是：推广链接带有goodsSign信息时，订单会返回原goodsSign；反之，会生成新的goodsSign返回。 |
| goods\_thumbnail\_url | STRING |  | 商品缩略图 |
| group\_id | LONG |  | 成团编号 |
| is\_direct | INTEGER |  | 是否直推 ，1表示是，0表示否 |
| mall\_id | LONG |  | 店铺id |
| mall\_name | STRING |  | 店铺名称 |
| no\_subsidy\_reason | STRING |  | 非补贴订单原因，例如："商品补贴达上限"，"达到单个用户下单上限"，"非指定落地页直推订单"，"订单超过2个月未审核成功"等 |
| order\_amount | LONG |  | 实际支付金额，单位为分 |
| order\_create\_time | LONG |  | 订单生成时间，UNIX时间戳 |
| order\_group\_success\_time | LONG |  | 成团时间 |
| order\_modify\_at | LONG |  | 最后更新时间 |
| order\_pay\_time | LONG |  | 支付时间 |
| order\_receive\_time | LONG |  | 确认收货时间 |
| order\_settle\_time | LONG |  | 结算时间 |
| order\_sn | STRING |  | 推广订单编号 |
| order\_status | INTEGER |  | 订单状态：0-已支付；1-已成团；2-确认收货；3-审核成功；4-审核失败（不可提现）；5-已经结算 ;10-已处罚 |
| order\_status\_desc | STRING |  | 订单状态描述 |
| order\_verify\_time | LONG |  | 审核时间 |
| p\_id | STRING |  | 推广位ID |
| platform\_discount | LONG |  | 平台券金额，表示该订单使用的平台券金额，单位分 |
| price\_compare\_status | INTEGER |  | 比价状态：0：正常，1：比价 |
| promotion\_amount | LONG |  | 佣金金额，包含软件服务费，单位为分 |
| promotion\_rate | LONG |  | 佣金比例，千分比 |
| red\_packet\_type | INTEGER |  | 超级红包补贴类型：0-非红包补贴订单，1-季度新用户补贴 |
| scene\_at\_market\_fee | INTEGER |  | 场景工具商佣金，包含场景工具商软件服务费，单位为分 |
| sep\_duo\_id | LONG |  | 直播间订单推广duoId |
| sep\_market\_fee | INTEGER |  | 直播间推广佣金 |
| sep\_parameters | STRING |  | 直播间推广自定义参数 |
| sep\_pid | STRING |  | 直播间订单推广位 |
| sep\_rate | INTEGER |  | 直播间推广佣金比例 |
| share\_amount | INTEGER |  | 招商分成服务费金额，单位为分 |
| share\_rate | INTEGER |  | 招商分成服务费比例，千分比 |
| subsidy\_amount | INTEGER |  | 优势渠道专属商品补贴金额，单位为分。针对优质渠道的补贴活动，指定优势渠道可通过推广该商品获取相应补贴。补贴活动入口：\[进宝网站-官方活动\] |
| subsidy\_duo\_amount\_level | INTEGER |  | V3/V4等级权益给渠道的奖励佣金，包含软件服务费，不允许直接给下级代理展示，单位为分 |
| subsidy\_duo\_amount\_ten\_million | INTEGER |  | 官方活动给渠道的收入补贴金额，不允许直接给下级代理展示，单位为分 |
| subsidy\_type | INTEGER |  | 订单补贴类型：0-非补贴订单，1-千万补贴，2-社群补贴，3-多多星选，4-品牌优选，5-千万神券 6-QQ小世界 7-新商家补贴 8-拼团享多多 9-超级红包 10-超红大额券 |
| type | LONG |  | 下单场景类型：0-单品推广，1-红包活动推广，4-多多进宝商城推广，7-今日爆款，8-品牌清仓，9-1.9包邮，77-刮刮卡活动推广，94-充值中心，101-品牌黑卡，103-百亿补贴频道，104-内购清单频道，105-超级红包 |
| zs\_duo\_id | LONG |  | 招商多多客id |
| subsidy\_list | OBJECT\[\] |  | 进宝订单补贴列表 |
| subsidy\_amount | LONG |  | 进宝订单补贴金额 |
| subsidy\_type | INTEGER |  | 进宝补贴类型 |
| subsidy\_order\_remark | STRING |  | 进宝订单补贴备注 |
| total\_count | LONG |  | 请求到的结果数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkAllOrderListIncrementGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddDdkAllOrderListIncrementGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddDdkAllOrderListIncrementGetRequest request = new PddDdkAllOrderListIncrementGetRequest();
        request.setEndUpdateTime(1634711715L);
        request.setPage(1);
        request.setPageSize(100);
        request.setQueryOrderType(1);
        request.setStartUpdateTime(1634711715L);
        PddDdkAllOrderListIncrementGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "order_list_get_response": {
    "order_list": [
      {
        "activity_tags": [
          0
        ],
        "auth_duo_id": 0,
        "auth_duo_id_service_fee": 0,
        "bandan_risk_consult": 0,
        "batch_no": "str",
        "cash_gift_id": 0,
        "cat_ids": [
          0
        ],
        "cpa_new": 0,
        "cps_level": 0,
        "custom_parameters": "str",
        "duo_id_service_fee": 0,
        "fail_reason": "str",
        "goods_category_name": "str",
        "goods_id": 0,
        "goods_name": "str",
        "goods_price": 0,
        "goods_quantity": 0,
        "goods_sign": "str",
        "goods_thumbnail_url": "str",
        "group_id": 0,
        "is_direct": 0,
        "mall_id": 0,
        "mall_name": "str",
        "no_subsidy_reason": "str",
        "order_amount": 0,
        "order_create_time": 0,
        "order_group_success_time": 0,
        "order_modify_at": 0,
        "order_pay_time": 0,
        "order_receive_time": 0,
        "order_settle_time": 0,
        "order_sn": "str",
        "order_status": 0,
        "order_status_desc": "str",
        "order_verify_time": 0,
        "p_id": "str",
        "platform_discount": 0,
        "price_compare_status": 0,
        "promotion_amount": 0,
        "promotion_rate": 0,
        "red_packet_type": 0,
        "scene_at_market_fee": 0,
        "sep_duo_id": 0,
        "sep_market_fee": 0,
        "sep_parameters": "str",
        "sep_pid": "str",
        "sep_rate": 0,
        "share_amount": 0,
        "share_rate": 0,
        "subsidy_amount": 0,
        "subsidy_duo_amount_level": 0,
        "subsidy_duo_amount_ten_million": 0,
        "subsidy_list": [
          {
            "subsidy_amount": 0,
            "subsidy_order_remark": "str",
            "subsidy_type": 0
          }
        ],
        "subsidy_type": 0,
        "type": 0,
        "zs_duo_id": 0
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
| 多多客工具权限包 | 多多客联盟 |

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
