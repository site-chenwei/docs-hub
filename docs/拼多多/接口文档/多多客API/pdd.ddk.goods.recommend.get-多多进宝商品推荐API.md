---
title: "pdd.ddk.goods.recommend.get - 多多进宝商品推荐API"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.recommend.get"
menu_path:
  - "多多客API"
  - "pdd.ddk.goods.recommend.get"
captured_at: "2026-04-09T15:19:09.966Z"
---

# pdd.ddk.goods.recommend.get

## 多多进宝商品推荐API

更新时间：2026-02-09 11:02:51

¥免费API

不需用户授权

多多进宝商品推荐API

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
| activity\_tags | INTEGER\[\] | 非必填 | 活动商品标记数组，例：\[4,7\]，4-秒杀，7-百亿补贴，10851-千万补贴，11879-千万神券，10913-招商礼金商品，31-品牌黑标，10564-精选爆品-官方直推爆款，10584-精选爆品-团长推荐，24-品牌高佣，其他的值请忽略 |
| cat\_id | LONG | 非必填 | 猜你喜欢场景的商品类目，商品类目ID，使用pdd.goods.cats.get接口获取 |
| channel\_type | INTEGER | 非必填 | 进宝频道推广商品: 1-今日销量榜,3-相似商品推荐,4-猜你喜欢(和进宝网站精选一致),5-实时热销榜,6-实时收益榜。默认值5 |
| custom\_parameters | STRING | 非必填 | 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 为用户唯一标识，可自行加密后传入，每个用户仅且对应一个标识，必填； sid 为上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key。 |
| goods\_img\_type | INTEGER | 非必填 | 商品主图类型：1-场景图，2-白底图，默认为0 |
| goods\_sign\_list | STRING\[\] | 非必填 | 商品goodsSign列表，相似商品推荐场景时必传，仅取数组的第一位，例如：\["c9r2omogKFFAc7WBwvbZU1ikIb16\_J3CTa8HNN"\]。goodsSign是加密后的goodsId, goodsId已下线，请使用goodsSign来替代。使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252 |
| limit | INTEGER | 非必填 | 一页请求数量；默认值 ： 20 |
| list\_id | STRING | 非必填 | 翻页时建议填写前页返回的list\_id值 |
| offset | INTEGER | 非必填 | 从多少位置开始请求；默认值 ： 0，offset需是limit的整数倍，仅支持整页翻页 |
| pid | STRING | 非必填 | 推广位id |
| risk\_params | MAP | 非必填 | 风控参数 |
| $key | STRING | 非必填 | 风控参数key |
| $value | STRING | 非必填 | 风控参数value |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_basic\_detail\_response | OBJECT |  | goods\_basic\_detail\_response |
| list | OBJECT\[\] |  | 列表 |
| activity\_promotion\_rate | LONG |  | 活动佣金比例，千分比（特定活动期间的佣金比例） |
| activity\_tags | INTEGER\[\] |  | 商品活动标记数组，例：\[4,7\]，4-秒杀 7-百亿补贴等 |
| brand\_name | STRING |  | 商品品牌词信息，如“苹果”、“阿迪达斯”、“李宁”等 |
| cash\_gift\_amount | LONG |  | 全局礼金金额，单位分 |
| cat\_id | STRING |  | 商品类目id |
| cat\_ids | LONG\[\] |  | 商品一~四级类目ID列表 |
| coupon\_discount | LONG |  | 优惠券面额,单位为分 |
| coupon\_end\_time | LONG |  | 优惠券失效时间,UNIX时间戳 |
| coupon\_min\_order\_amount | LONG |  | 优惠券门槛价格,单位为分 |
| coupon\_price | LONG |  | 优惠券金额 |
| coupon\_remain\_quantity | LONG |  | 优惠券剩余数量 |
| coupon\_start\_time | LONG |  | 优惠券生效时间,UNIX时间戳 |
| coupon\_total\_quantity | LONG |  | 优惠券总数量 |
| create\_at | LONG |  | 创建时间 |
| desc\_txt | STRING |  | 描述分 |
| extra\_coupon\_amount | LONG |  | 额外优惠券，单位为分 |
| goods\_desc | STRING |  | 商品描述 |
| goods\_image\_url | STRING |  | 商品主图 |
| goods\_labels | INTEGER\[\] |  | 商品特殊标签列表。例: \[1\]，1-APP专享 |
| goods\_name | STRING |  | 商品名称 |
| goods\_rate | LONG |  | 商品等级 |
| goods\_sign | STRING |  | 商品goodsSign，支持通过goodsSign查询商品。goodsSign是加密后的goodsId, goodsId已下线，请使用goodsSign来替代。使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252 |
| goods\_thumbnail\_url | STRING |  | 商品缩略图 |
| goods\_type | INTEGER |  | 商品类型 |
| has\_coupon | BOOLEAN |  | 商品是否带券,true-带券,false-不带券 |
| has\_material | BOOLEAN |  | 商品是否有素材(图文、视频) |
| lgst\_txt | STRING |  | 物流分 |
| mall\_id | LONG |  | 商家id |
| mall\_name | STRING |  | 店铺名称 |
| mall\_sn | STRING |  | 店铺sn，店铺id不存在时作为店铺唯一标识 |
| market\_fee | LONG |  | 市场服务费 |
| merchant\_type | STRING |  | 商家类型 |
| min\_group\_price | LONG |  | 最小成团价格，单位分 |
| min\_normal\_price | LONG |  | 最小单买价格，单位分 |
| opt\_id | STRING |  | 商品标签类目ID,使用pdd.goods.opt.get获取 |
| opt\_ids | LONG\[\] |  | 商品一~四级标签类目ID列表 |
| opt\_name | STRING |  | 商品标签名 |
| platform\_discount\_list | OBJECT\[\] |  | 进宝平台券信息 |
| coupon\_amount | LONG |  | 券面额，单位分 |
| coupon\_threshold | LONG |  | 券门槛，单位分 |
| discoun\_type | INTEGER |  | 优惠类型：17-千万神券 21-限时秒杀 22-超红大额券 28-爆品加补 |
| predict\_promotion\_rate | LONG |  | 比价行为预判定佣金，需要用户备案 |
| promotion\_rate | LONG |  | 佣金比例,千分比 |
| qr\_code\_image\_url | STRING |  | 二维码主图 |
| realtime\_sales\_tip | STRING |  | 商品近1小时在多多进宝的实时销量（仅实时热销榜提供） |
| sales\_tip | STRING |  | 销售量 |
| search\_id | STRING |  | 搜索id，建议生成推广链接时候填写，提高收益。 |
| serv\_txt | STRING |  | 服务分 |
| share\_desc | STRING |  | 分享描述 |
| share\_rate | INTEGER |  | 招商分成服务费比例，千分比 |
| subsidy\_amount | INTEGER |  | 优势渠道专属商品补贴金额，单位为分。针对优质渠道的补贴活动，指定优势渠道可通过推广该商品获取相应补贴。补贴活动入口：\[进宝网站-官方活动\] |
| subsidy\_duo\_amount\_ten\_million | INTEGER |  | 官方活动给渠道的收入补贴金额，不允许直接给下级代理展示，单位为分 |
| subsidy\_goods\_type | INTEGER |  | 补贴活动类型：0-无补贴，1-千万补贴，4-千万神券，6-佣金翻倍 21-限时秒杀 |
| subsidy\_rate | INTEGER |  | 进宝补贴比例，千分位 |
| unified\_tags | STRING\[\] |  | 优惠标签列表，包括："X元券","比全网低X元","服务费","精选素材","近30天低价","同款低价","同款好评","同款热销","旗舰店","一降到底","招商优选","商家优选","好价再降X元","全站销量XX","实时热销榜第X名","实时好评榜第X名","额外补X元"等 |
| subsidy\_list | OBJECT\[\] |  | 进宝商品预估补贴列表 |
| subsidy\_type | INTEGER |  | 进宝补贴类型 |
| subsidy\_amount | LONG |  | 进宝商品预估补贴金额 |
| subsidy\_rate | INTEGER |  | 进宝商品预估补贴比例 |
| list\_id | STRING |  | 翻页时必填前页返回的list\_id值 |
| search\_id | STRING |  | 搜索id，建议生成推广链接时候填写，提高收益。 |
| total | INTEGER |  | total |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkGoodsRecommendGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddDdkGoodsRecommendGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddDdkGoodsRecommendGetRequest request = new PddDdkGoodsRecommendGetRequest();
        List<Integer> activityTags = new ArrayList<Integer>();
        activityTags.add(0);
        request.setActivityTags(activityTags);
        request.setCatId(20100L);
        request.setChannelType(1);
        request.setCustomParameters("str");
        request.setGoodsImgType(1);
        List<String> goodsSignList = new ArrayList<String>();
        goodsSignList.add("str");
        request.setGoodsSignList(goodsSignList);
        request.setLimit(20);
        request.setListId("str");
        request.setOffset(0);
        request.setPid("str");
        Map<String, String> riskParams = new HashMap<String, String>();
        riskParams.put("", "str");
        request.setRiskParams(riskParams);
        PddDdkGoodsRecommendGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_basic_detail_response": {
    "list": [
      {
        "activity_promotion_rate": 0,
        "activity_tags": [
          0
        ],
        "brand_name": "str",
        "cash_gift_amount": 0,
        "cat_id": "str",
        "cat_ids": [
          0
        ],
        "coupon_discount": 0,
        "coupon_end_time": 0,
        "coupon_min_order_amount": 0,
        "coupon_price": 0,
        "coupon_remain_quantity": 0,
        "coupon_start_time": 0,
        "coupon_total_quantity": 0,
        "create_at": 0,
        "desc_txt": "str",
        "extra_coupon_amount": 0,
        "goods_desc": "str",
        "goods_image_url": "str",
        "goods_labels": [
          0
        ],
        "goods_name": "str",
        "goods_rate": 0,
        "goods_sign": "str",
        "goods_thumbnail_url": "str",
        "goods_type": 0,
        "has_coupon": false,
        "has_material": false,
        "lgst_txt": "str",
        "mall_id": 0,
        "mall_name": "str",
        "mall_sn": "str",
        "market_fee": 0,
        "merchant_type": "str",
        "min_group_price": 0,
        "min_normal_price": 0,
        "opt_id": "str",
        "opt_ids": [
          0
        ],
        "opt_name": "str",
        "platform_discount_list": [
          {
            "coupon_amount": 0,
            "coupon_threshold": 0,
            "discoun_type": 0
          }
        ],
        "predict_promotion_rate": 0,
        "promotion_rate": 0,
        "qr_code_image_url": "str",
        "realtime_sales_tip": "str",
        "sales_tip": "str",
        "search_id": "str",
        "serv_txt": "str",
        "share_desc": "str",
        "share_rate": 0,
        "subsidy_amount": 0,
        "subsidy_duo_amount_ten_million": 0,
        "subsidy_goods_type": 0,
        "subsidy_list": [
          {
            "subsidy_amount": 0,
            "subsidy_rate": 0,
            "subsidy_type": 0
          }
        ],
        "subsidy_rate": 0,
        "unified_tags": [
          "str"
        ]
      }
    ],
    "list_id": "str",
    "search_id": "str",
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
| 多多客 |  |

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

接口总限流频次：55750次/50秒

### API工具
