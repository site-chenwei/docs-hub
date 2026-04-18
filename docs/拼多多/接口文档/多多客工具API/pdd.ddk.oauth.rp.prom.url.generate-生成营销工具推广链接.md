---
title: "pdd.ddk.oauth.rp.prom.url.generate - 生成营销工具推广链接"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ddk.oauth.rp.prom.url.generate"
menu_path:
  - "多多客工具API"
  - "pdd.ddk.oauth.rp.prom.url.generate"
captured_at: "2026-04-09T15:20:39.452Z"
---

# pdd.ddk.oauth.rp.prom.url.generate

## 生成营销工具推广链接

更新时间：2026-02-09 11:02:51

¥免费API

必须用户授权

生成营销工具推广链接

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
| amount | LONG | 非必填 | 初始金额（单位分），有效金额枚举值：300、500、700、1100和1600，默认300 |
| channel\_type | INTEGER | 非必填 | 营销工具类型，必填：-1-活动列表，0-红包(需申请推广权限)，2–新人红包，3-刮刮卡，5-员工内购，10-生成绑定备案链接，12-砸金蛋，14-千万补贴B端页面，15-充值中心B端页面，16-千万补贴C端页面，17-千万补贴投票页面，23-超级红包，24-礼金全场N折活动B端页面，27-带货赢千万，30-免单B端页面，31-免单C端页面，32-转盘得现金B端页面，33-转盘得现金C端页面，34-千万神券C端页面，35-千万神券B端页面，36-爆品日历B端页面，37-超级红包B端推品页，39-母婴馆C端页面，40-母婴馆B端页面，41-限时折扣B端页面，42-超级红包9.9C端活动页 45-大促会场集合B端页面 46-大促会场集合C端页面 47-类目排位赛B端页面 48-惊喜价B端页面 49-惊喜价C端页面 50-单单返券页面 51-新代理扶持活动页面 52-超红大额券选品页面 53-超红大额券C端会场 54-拼多多超级折扣页面 55-限时秒杀B端会场 56-限时秒杀C端会场 57-超级补贴推手活动页 58-超级补贴C端会场页 |
| custom\_parameters | STRING | 非必填 | 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 用户唯一标识，可自行加密后传入，每个用户仅且对应一个标识，必填； sid 上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key。（如果使用GET请求，请使用URLEncode处理参数） |
| diy\_coupon\_rebate\_param | OBJECT | 非必填 | 单单返券参数 |
| goods\_sign | STRING | 非必填 | 商品编码 |
| diy\_one\_yuan\_param | OBJECT | 非必填 | 一元购自定义参数，json格式，例如:{"goods\_sign":"Y9b2\_0uSWMFPGSaVwvfZAlm\_y2ADLWZl\_JQ7UYaS80K"} |
| goods\_sign | STRING | 非必填 | 商品goodsSign，支持通过goodsSign查询商品。goodsSign是加密后的goodsId, goodsId已下线，请使用goodsSign来替代。使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252 |
| diy\_promo\_act\_collection\_param | OBJECT | 非必填 | 大促会场集合页参数 |
| collection\_id | LONG | 非必填 | 集合id 不传默认使用最新的大促会场集合 |
| diy\_red\_packet\_param | OBJECT | 非必填 | 红包自定义参数，json格式 |
| amount\_probability | LONG\[\] | 非必填 | 红包金额列表，200、300、500、1000、2000，单位分。红包金额和红包抵后价设置只能二选一，默认设置了红包金额会忽略红包抵后价设置 |
| dis\_text | BOOLEAN | 非必填 | 设置玩法，false-现金红包, true-现金券 |
| not\_show\_background | BOOLEAN | 非必填 | 推广页设置，false-红包开启页, true-红包领取页 |
| opt\_id | INTEGER | 非必填 | 优先展示类目 |
| range\_items | OBJECT\[\] | 非必填 | 自定义红包抵后价和商品佣金区间对象数组 |
| range\_from | LONG | 非必填 | 区间的开始值 |
| range\_id | INTEGER | 非必填 | range\_id为1表示红包抵后价（单位分）， range\_id为2表示佣金比例（单位千分之几) |
| range\_to | LONG | 非必填 | 区间的结束值 |
| diy\_sp\_red\_packet\_param | OBJECT | 非必填 | 超级红包自定义参数，json格式 |
| goods\_sign | STRING | 非必填 | 商品goodsSign，支持通过goodsSign置顶落地页商品。使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252 |
| sku\_id\_code | STRING | 非必填 | 商品skuId密文，支持自动选中对应sku |
| ext\_params | MAP | 非必填 | 扩展参数 |
| $key | STRING | 非必填 | 扩展参数Key |
| $value | STRING | 非必填 | 扩展参数Value |
| force\_duo\_id | INTEGER | 非必填 | 是否强制走duoId专属推广计划，不传或传0为不强制，传1为强制 |
| generate\_schema\_url | BOOLEAN | 非必填 | 是否返回 schema URL |
| generate\_short\_link | BOOLEAN | 非必填 | 是否生成微信shortLink，该字段支持超红c端活动页、超红二合一、b端推品页，单个渠道每天生成的shortLink数量有限，请合理生成shortLink链接 |
| generate\_short\_url | BOOLEAN | 非必填 | 是否生成短链接。true-是，false-否，默认false |
| generate\_we\_app | BOOLEAN | 非必填 | 是否生成拼多多福利券微信小程序推广信息 |
| p\_id\_list | STRING\[\] | 必填 | 推广位列表，长度最大为1，例如：\["60005\_612"\]。活动页生链要求传入授权备案信息，不支持批量生链。 |
| resource\_url\_page | INTEGER | 非必填 | 查询资源位活动列表分页 |
| resource\_url\_size | INTEGER | 非必填 | 查询资源位活动列表分页大小，不能超过200 |
| scratch\_card\_amount | LONG | 非必填 | 刮刮卡指定金额（单位分），可指定2-100元间数值，即有效区间为：\[200,10000\] |
| tmcc\_param | OBJECT | 非必填 | 千万神券C端生链扩展参数 支持置顶活动ID 和 置顶商品(品牌活动才支持) |
| goods\_signs | STRING\[\] | 非必填 | 置顶商品的goodsSign列表 |
| tmc\_config\_id | LONG | 非必填 | 指定活动id |
| zs\_duo\_id | LONG | 非必填 | 招商DuoID |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| rp\_promotion\_url\_generate\_response | OBJECT |  | 推广链接返回对象 |
| resource\_list | OBJECT\[\] |  | resource\_list |
| desc | STRING |  | 活动描述 |
| url | STRING |  | 活动地址 |
| url\_list | OBJECT\[\] |  | url\_list |
| mobile\_short\_url | STRING |  | 推广移动短链接，对应出参mobile\_url的短链接，与mobile\_url功能一致。 |
| mobile\_url | STRING |  | 推广移动链接，用户安装拼多多APP的情况下会唤起APP，否则唤起H5页面 |
| multi\_group\_mobile\_short\_url | STRING |  | 推广多人团移动短链接 |
| multi\_group\_mobile\_url | STRING |  | 推广多人团移动链接，用户安装拼多多APP的情况下会唤起APP，否则唤起H5页面 |
| multi\_group\_short\_url | STRING |  | 推广多人团短链接 |
| multi\_group\_url | STRING |  | 推广多人团链接，唤起H5页面 |
| schema\_url | STRING |  | schema链接，用户安装拼多多APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| short\_url | STRING |  | 推广短链接，对应出参url的短链接，与url功能一致。 |
| tz\_schema\_url | STRING |  | 使用此推广链接，用户安装多多团长APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| url | STRING |  | 推广长链接，唤起H5页面 |
| we\_app\_info | OBJECT |  | 拼多多福利券微信小程序信息 |
| app\_id | STRING |  | 小程序id |
| banner\_url | STRING |  | Banner图 |
| desc | STRING |  | 描述 |
| page\_path | STRING |  | 小程序path值 |
| source\_display\_name | STRING |  | 来源名 |
| title | STRING |  | 小程序标题 |
| user\_name | STRING |  | 用户名 |
| we\_app\_icon\_url | STRING |  | 小程序icon |
| weixin\_short\_link | STRING |  | 微信shortLink，该字段支持超红c端活动页、超红二合一、b端推品页，单个渠道每天生成的shortLink数量有限，请合理生成shortLink链接 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddDdkOauthRpPromUrlGenerateResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest.DiyCouponRebateParam;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest.DiyOneYuanParam;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest.DiyPromoActCollectionParam;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest.DiyRedPacketParam;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest.DiyRedPacketParamRangeItemsItem;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest.DiySpRedPacketParam;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthRpPromUrlGenerateRequest.TmccParam;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddDdkOauthRpPromUrlGenerateRequest request = new PddDdkOauthRpPromUrlGenerateRequest();
        request.setAmount(300L);
        request.setChannelType(14);
        request.setCustomParameters("str");

        DiyCouponRebateParam diyCouponRebateParam = new DiyCouponRebateParam();
        diyCouponRebateParam.setGoodsSign("str");
        request.setDiyCouponRebateParam(diyCouponRebateParam);

        DiyOneYuanParam diyOneYuanParam = new DiyOneYuanParam();
        diyOneYuanParam.setGoodsSign("str");
        request.setDiyOneYuanParam(diyOneYuanParam);

        DiyPromoActCollectionParam diyPromoActCollectionParam = new DiyPromoActCollectionParam();
        diyPromoActCollectionParam.setCollectionId(0L);
        request.setDiyPromoActCollectionParam(diyPromoActCollectionParam);

        DiyRedPacketParam diyRedPacketParam = new DiyRedPacketParam();
        List<Long> amountProbability = new ArrayList<Long>();
        amountProbability.add(0L);
        diyRedPacketParam.setAmountProbability(amountProbability);
        diyRedPacketParam.setDisText(false);
        diyRedPacketParam.setNotShowBackground(false);
        diyRedPacketParam.setOptId(0);
        List<DiyRedPacketParamRangeItemsItem> rangeItems = new ArrayList<DiyRedPacketParamRangeItemsItem>();

        DiyRedPacketParamRangeItemsItem item = new DiyRedPacketParamRangeItemsItem();
        item.setRangeFrom(0L);
        item.setRangeId(0);
        item.setRangeTo(0L);
        rangeItems.add(item);
        diyRedPacketParam.setRangeItems(rangeItems);
        request.setDiyRedPacketParam(diyRedPacketParam);

        DiySpRedPacketParam diySpRedPacketParam = new DiySpRedPacketParam();
        diySpRedPacketParam.setGoodsSign("str");
        diySpRedPacketParam.setSkuIdCode("str");
        request.setDiySpRedPacketParam(diySpRedPacketParam);
        Map<String, String> extParams = new HashMap<String, String>();
        extParams.put("", "str");
        request.setExtParams(extParams);
        request.setForceDuoId(0);
        request.setGenerateSchemaUrl(false);
        request.setGenerateShortLink(false);
        request.setGenerateShortUrl(false);
        request.setGenerateWeApp(false);
        List<String> pIdList = new ArrayList<String>();
        pIdList.add("str");
        request.setPIdList(pIdList);
        request.setResourceUrlPage(1);
        request.setResourceUrlSize(20);
        request.setScratchCardAmount(200L);

        TmccParam tmccParam = new TmccParam();
        List<String> goodsSigns = new ArrayList<String>();
        goodsSigns.add("str");
        tmccParam.setGoodsSigns(goodsSigns);
        tmccParam.setTmcConfigId(0L);
        request.setTmccParam(tmccParam);
        request.setZsDuoId(10000L);
        PddDdkOauthRpPromUrlGenerateResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "rp_promotion_url_generate_response": {
    "resource_list": [
      {
        "desc": "str",
        "url": "str"
      }
    ],
    "url_list": [
      {
        "mobile_short_url": "str",
        "mobile_url": "str",
        "multi_group_mobile_short_url": "str",
        "multi_group_mobile_url": "str",
        "multi_group_short_url": "str",
        "multi_group_url": "str",
        "schema_url": "str",
        "short_url": "str",
        "tz_schema_url": "str",
        "url": "str",
        "we_app_info": {
          "app_id": "str",
          "banner_url": "str",
          "desc": "str",
          "page_path": "str",
          "source_display_name": "str",
          "title": "str",
          "user_name": "str",
          "we_app_icon_url": "str"
        },
        "weixin_short_link": "str"
      }
    ]
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
