---
title: "pdd.ddk.oauth.goods.prom.url.generate - 生成多多进宝推广链接"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ddk.oauth.goods.prom.url.generate"
menu_path:
  - "多多客工具API"
  - "pdd.ddk.oauth.goods.prom.url.generate"
captured_at: "2026-04-09T15:19:51.245Z"
---

# pdd.ddk.oauth.goods.prom.url.generate

## 生成多多进宝推广链接

更新时间：2025-10-29 15:59:36

¥免费API

必须用户授权

生成普通商品推广链接

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
| cash\_gift\_id | LONG | 非必填 | 多多礼金ID |
| cash\_gift\_name | STRING | 非必填 | 自定义礼金标题，用于向用户展示渠道专属福利，不超过12个字 |
| custom\_parameters | STRING | 非必填 | 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 用户唯一标识，可自行加密后传入，每个用户仅且对应一个标识，必填； sid 上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key。（如果使用GET请求，请使用URLEncode处理参数） |
| force\_duo\_id | BOOLEAN | 非必填 | 是否使用多多客专属推广计划 |
| generate\_authority\_url | BOOLEAN | 非必填 | 是否生成带授权的单品链接。如果未授权，则会走授权流程 |
| generate\_mall\_collect\_coupon | BOOLEAN | 非必填 | 是否生成店铺收藏券推广链接 |
| generate\_schema\_url | BOOLEAN | 非必填 | 是否返回 schema URL |
| generate\_short\_url | BOOLEAN | 非必填 | 是否生成短链接，true-是，false-否 |
| generate\_we\_app | BOOLEAN | 非必填 | 是否生成拼多多福利券微信小程序推广信息 |
| generate\_we\_app\_long\_link | BOOLEAN | 非必填 | 是否生成小程序schema长链 |
| goods\_sign\_list | STRING\[\] | 非必填 | 商品goodsSign列表，例如：\["c9r2omogKFFAc7WBwvbZU1ikIb16\_J3CTa8HNN"\]，支持批量生链。goodsSign是加密后的goodsId, goodsId已下线，请使用goodsSign来替代。使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252 |
| material\_id | STRING | 非必填 | 素材ID，可以通过商品详情接口获取商品素材信息 |
| multi\_group | BOOLEAN | 非必填 | true--生成多人团推广链接 false--生成单人团推广链接（默认false）1、单人团推广链接：用户访问单人团推广链接，可直接购买商品无需拼团。2、多人团推广链接：用户访问双人团推广链接开团，若用户分享给他人参团，则开团者和参团者的佣金均结算给推手 |
| p\_id | STRING | 必填 | 推广位ID |
| search\_id | STRING | 非必填 | 搜索id，建议填写，提高收益。来自pdd.ddk.goods.recommend.get、pdd.ddk.goods.search、pdd.ddk.top.goods.list.query等接口 |
| special\_params | MAP | 非必填 | 特殊参数 |
| $key | STRING | 必填 | 特殊参数key |
| $value | STRING | 必填 | 特殊参数value |
| url\_type | INTEGER | 非必填 | 生成商品链接类型 0-默认 1-百补相似品列表 |
| zs\_duo\_id | LONG | 非必填 | 招商多多客ID |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_promotion\_url\_generate\_response | OBJECT |  | response |
| goods\_promotion\_url\_list | OBJECT\[\] |  | 多多进宝推广链接对象列表 |
| mobile\_short\_url | STRING |  | 对应出参mobile\_url的短链接，与mobile\_url功能一致。 |
| mobile\_url | STRING |  | 使用此推广链接，用户安装微信的情况下，默认拉起拼多多福利券微信小程序，否则唤起H5页面 |
| schema\_url | STRING |  | 使用此推广链接，用户安装拼多多APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| short\_url | STRING |  | 对应出参url的短链接，与url功能一致 |
| tz\_schema\_url | STRING |  | 使用此推广链接，用户安装多多团长APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| url | STRING |  | 普通推广长链接，唤起H5页面 |
| we\_app\_info | OBJECT |  | 拼多多福利券微信小程序信息 |
| app\_id | STRING |  | 小程序id |
| banner\_url | STRING |  | Banner图 |
| desc | STRING |  | 描述 |
| page\_path | STRING |  | 小程序path值 |
| source\_display\_name | STRING |  | 来源名 |
| title | STRING |  | 小程序标题 |
| user\_name | STRING |  | 用户名 |
| we\_app\_icon\_url | STRING |  | 小程序图片 |
| weixin\_long\_link | STRING |  | 微信小程序schema长链 |
| weixin\_short\_link | STRING |  | 微信小程序短链 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthGoodsPromUrlGenerateRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddDdkOauthGoodsPromUrlGenerateResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddDdkOauthGoodsPromUrlGenerateRequest request = new PddDdkOauthGoodsPromUrlGenerateRequest();
        request.setCashGiftId(1000L);
        request.setCashGiftName("str");
        request.setCustomParameters("str");
        request.setForceDuoId(true);
        request.setGenerateAuthorityUrl(true);
        request.setGenerateMallCollectCoupon(true);
        request.setGenerateSchemaUrl(false);
        request.setGenerateShortUrl(true);
        request.setGenerateWeApp(true);
        request.setGenerateWeAppLongLink(false);
        List<String> goodsSignList = new ArrayList<String>();
        goodsSignList.add("str");
        request.setGoodsSignList(goodsSignList);
        request.setMaterialId("str");
        request.setMultiGroup(true);
        request.setPId("str");
        request.setSearchId("str");
        Map<String, String> specialParams = new HashMap<String, String>();
        specialParams.put("", "str");
        request.setSpecialParams(specialParams);
        request.setUrlType(0);
        request.setZsDuoId(21003L);
        PddDdkOauthGoodsPromUrlGenerateResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_promotion_url_generate_response": {
    "goods_promotion_url_list": [
      {
        "mobile_short_url": "str",
        "mobile_url": "str",
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
        "weixin_long_link": "str",
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

接口总限流频次：111500次/10秒

### API工具
