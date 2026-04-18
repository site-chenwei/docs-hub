---
title: "pdd.ddk.oauth.cashgift.create - 创建多多礼金"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ddk.oauth.cashgift.create"
menu_path:
  - "多多客工具API"
  - "pdd.ddk.oauth.cashgift.create"
captured_at: "2026-04-09T15:19:32.267Z"
---

# pdd.ddk.oauth.cashgift.create

## 创建多多礼金

更新时间：2025-02-27 19:52:31

¥免费API

必须用户授权

创建多多礼金

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
| acquire\_end\_time | LONG | 必填 | 券批次领取结束时间。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |
| acquire\_start\_time | LONG | 必填 | 券批次领取开始时间。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |
| auto\_take | BOOLEAN | 非必填 | 是否自动领券，默认false不自动领券 |
| cashgift\_type | INTEGER | 非必填 | 创建礼金类型：1-普通满减礼金；2-不限商品满减礼金；3-免单礼金；4-灵活面额礼金。默认为普通满减礼金 |
| coupon\_amount | INTEGER | 非必填 | 礼金券面额，单位为分，创建普通满减礼金、不限商品满减礼金和免单礼金时，该字段必填；创建灵活面额礼金时，该字段传空，券面额 = 商品券后价 - 期望礼金券后价，由系统自动计算 |
| coupon\_threshold\_amount | INTEGER | 非必填 | 满减门槛，单位为分。对于普通满减礼金和不限商品满减礼金，满减门槛至少需为礼金券面额的2倍 |
| duration | INTEGER | 非必填 | 活动持续时间，validity\_time\_type为 1 时必填。相对时间类型为天级时，最大值为30，即领取后30天内有效；相对时间类型为小时级时，最大值为24，即领取后24小时内有效；相对时间类型为分钟级时，则最大值为60，即领取后60分钟内有效。 |
| except\_amount | INTEGER | 非必填 | 期望礼金券后价，单位为分，最小值为1。创建灵活面额礼金时必填 |
| fetch\_risk\_check | BOOLEAN | 非必填 | 是否打开风控保护开关，默认false关闭 |
| freeze\_condition | INTEGER | 非必填 | 收益保护开关开启(rate\_decrease\_monitor = true)时必填。0-监控项发生降低；1-监控项低于礼金面额，默认为0。 |
| freeze\_watch\_type | INTEGER | 非必填 | 收益保护开关开启(rate\_decrease\_monitor = true)时必填。0-佣金；1-补贴；2-佣金+补贴，默认为0。 |
| generate\_global | BOOLEAN | 非必填 | 是否开启全场景推广，默认false不开启全场景推广，仅支持普通满减礼金和免单礼金 |
| goods\_sign\_list | STRING\[\] | 非必填 | 商品goodsSign列表，例如：\["c9r2omogKFFAc7WBwvbZU1ikIb16\_J3CTa8HNN"\]，最多可支持传20个商品。创建普通满减礼金、免单礼金和灵活面额礼金时，该字段必填；创建不限商品满减礼金时，该字段传空。goodsSign使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252 |
| link\_acquire\_limit | LONG | 非必填 | 活动单链接可领券数量，默认无限制，最小值为1。 |
| name | STRING | 非必填 | 礼金名称 |
| p\_id\_list | OBJECT\[\] | 非必填 | 可使用推广位列表，例如：\["60005\_612"\]。(列表中的PID方可推广该礼金) |
| quantity | LONG | 非必填 | 礼金券数量，创建普通满减礼金、不限商品满减礼金或免单礼金时，该字段必填；创建灵活面额礼金时，礼金券数量不固定，礼金总预算用完为止，该字段不传 |
| rate\_decrease\_monitor | BOOLEAN | 非必填 | 收益保护开关，默认false关闭，仅支持普通满减礼金和免单礼金。开启状态下，系统将根据设置内容进行监控，当监控项满足冻结条件时，系统自动冻结礼金暂停推广，防止资金损失（您可通过多多礼金状态更新接口自行恢复推广） |
| relative\_time\_type | INTEGER | 非必填 | 相对时间类型：1-天级；2-小时级；3-分钟级，有效期类型validityTimeType = 1时必填，默认为1。 例如: relative\_time\_type = 2, duration = 15, 表示领取后15小时内有效。 |
| total\_amount | LONG | 非必填 | 礼金总预算，单位为分，创建灵活面额礼金时必填。其他情况，总金额 = 礼金券数量 \* 礼金券面额 |
| user\_limit | INTEGER | 非必填 | 单用户可领券数量，可设置范围为1~10张，默认为1张。 |
| is\_open\_renew | BOOLEAN | 非必填 | 是否开启自动续券功能，默认不开启 |
| remain\_count\_for\_renew | INTEGER | 非必填 | 触发续券的剩余券数量 |
| renew\_max\_number\_per\_day | INTEGER | 非必填 | 单日续券上限 |
| renew\_number\_per\_time | INTEGER | 非必填 | 每次续费上限 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| create\_cashgift\_response | OBJECT |  | response |
| cash\_gift\_id | LONG |  | 礼金ID |
| success | BOOLEAN |  | 创建结果 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthCashgiftCreateRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddDdkOauthCashgiftCreateResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkOauthCashgiftCreateRequest.PIdListItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddDdkOauthCashgiftCreateRequest request = new PddDdkOauthCashgiftCreateRequest();
        request.setAcquireEndTime(1636632854L);
        request.setAcquireStartTime(1636632854L);
        request.setAutoTake(false);
        request.setCashgiftType(1);
        request.setCouponAmount(100);
        request.setCouponThresholdAmount(10);
        request.setDuration(10);
        request.setExceptAmount(1);
        request.setFetchRiskCheck(true);
        request.setFreezeCondition(0);
        request.setFreezeWatchType(0);
        request.setGenerateGlobal(false);
        List<String> goodsSignList = new ArrayList<String>();
        goodsSignList.add("str");
        request.setGoodsSignList(goodsSignList);
        request.setLinkAcquireLimit(1L);
        request.setName("str");
        List<PIdListItem> pIdList = new ArrayList<PIdListItem>();

        PIdListItem item = new PIdListItem();
        pIdList.add(item);
        request.setPIdList(pIdList);
        request.setQuantity(10L);
        request.setRateDecreaseMonitor(false);
        request.setRelativeTimeType(1);
        request.setTotalAmount(100L);
        request.setUserLimit(1);
        request.setIsOpenRenew(false);
        request.setRemainCountForRenew(0);
        request.setRenewMaxNumberPerDay(0);
        request.setRenewNumberPerTime(0);
        PddDdkOauthCashgiftCreateResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "create_cashgift_response": {
    "cash_gift_id": 0,
    "success": false
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
