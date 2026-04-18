---
title: "pdd.ticket.sku.rule.add - 旅游门票商品履约规则新增"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ticket.sku.rule.add"
menu_path:
  - "旅游门票API"
  - "pdd.ticket.sku.rule.add"
captured_at: "2026-04-09T15:25:14.362Z"
---

# pdd.ticket.sku.rule.add

## 旅游门票商品履约规则新增

更新时间：2020-08-03 18:01:56

¥免费API

必须用户授权

供应商新增商品规则

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
| booker\_info\_limitation | OBJECT | 必填 | 下单人信息设置 |
| booker\_required | INTEGER | 必填 | 需要下单人信息 |
| mobile | INTEGER | 非必填 | 下单人手机 |
| booking\_notice | OBJECT | 必填 | 预定须知 |
| enter\_address | STRING | 必填 | 入园地址 |
| enter\_time | OBJECT\[\] | 非必填 | 入园时间 |
| comment | STRING | 非必填 | 备注 |
| end\_at | STRING | 必填 | 入园结束时间 |
| start\_at | STRING | 必填 | 入园开始时间 |
| enter\_ways | STRING | 非必填 | 入园方式 |
| extra\_desc | STRING | 非必填 | 补充说明 |
| fee\_include | STRING | 非必填 | 费用包含 |
| fee\_not\_include | STRING | 非必填 | 费用不包含 |
| important\_notice | STRING | 非必填 | 重要提示 |
| pass\_time\_limit | INTEGER | 非必填 | 通关限制时间 |
| ticket\_place | STRING | 必填 | 换票地址 |
| ticket\_time | OBJECT\[\] | 非必填 | 换票时间 |
| comment | STRING | 非必填 | 备注 |
| end\_at | STRING | 非必填 | 换票结束时间 |
| start\_at | STRING | 非必填 | 换票开始时间 |
| order\_limitation | OBJECT | 非必填 | 下单限制 |
| cycle\_length | INTEGER | 非必填 | 周期长度 |
| limitation\_type | INTEGER | 非必填 | 限制类型 |
| limit\_cycle | INTEGER | 非必填 | 周期类型 |
| limit\_num | INTEGER | 非必填 | 限购数量 |
| out\_rule\_id | STRING | 非必填 | 商户rule ID |
| provider\_contact\_info | OBJECT | 必填 | 服务商联系方式 |
| provider\_business\_hour | OBJECT\[\] | 非必填 | 服务时间 |
| close\_at | STRING | 非必填 | 结束时间 |
| open\_at | STRING | 非必填 | 开始时间 |
| time\_info | STRING | 非必填 | 描述 |
| provider\_name | STRING | 必填 | 服务商名称 |
| provider\_telephone | STRING | 必填 | 服务商联系电话 |
| refund\_limitations | OBJECT | 必填 | 退款规则 |
| is\_refundable | INTEGER | 必填 | 是否可退 |
| refund\_rules | OBJECT\[\] | 非必填 | 退款规则 |
| ahead\_time | INTEGER | 非必填 | 游玩日 0 点提前 或之后分钟数 |
| deduction\_fee | INTEGER | 必填 | 扣费值 |
| deduction\_unit | INTEGER | 必填 | 费率单位 |
| type | INTEGER | 必填 | 规则类型 |
| rule\_name | STRING | 必填 | 商户rule 名称 |
| traveler\_info\_limitation | OBJECT | 必填 | 游玩人信息 |
| credential | INTEGER | 非必填 | 游玩人证件 |
| name | INTEGER | 非必填 | 游玩人名字 |
| traveler\_required | INTEGER | 必填 | 出游人信息设置 |
| valid\_limitation | OBJECT | 必填 | 卡券有效期设置 |
| days\_time | INTEGER | 非必填 | 天数内有效 |
| end\_time | LONG | 非必填 | 结束时间 |
| start\_time | LONG | 非必填 | 开始时间 |
| time\_type | INTEGER | 必填 | 有效期时间类型 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| response | OBJECT |  |  |
| rule\_id | STRING |  | 规则 ID |
| rule\_version | STRING |  | 版本 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddTicketSkuRuleAddResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.BookerInfoLimitation;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.BookingNotice;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.BookingNoticeEnterTimeItem;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.BookingNoticeTicketTimeItem;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.OrderLimitation;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.ProviderContactInfo;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.ProviderContactInfoProviderBusinessHourItem;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.RefundLimitations;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.RefundLimitationsRefundRulesItem;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.TravelerInfoLimitation;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketSkuRuleAddRequest.ValidLimitation;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddTicketSkuRuleAddRequest request = new PddTicketSkuRuleAddRequest();

        BookerInfoLimitation bookerInfoLimitation = new BookerInfoLimitation();
        bookerInfoLimitation.setBookerRequired(0);
        bookerInfoLimitation.setMobile(0);
        request.setBookerInfoLimitation(bookerInfoLimitation);

        BookingNotice bookingNotice = new BookingNotice();
        bookingNotice.setEnterAddress("str");
        List<BookingNoticeEnterTimeItem> enterTime = new ArrayList<BookingNoticeEnterTimeItem>();

        BookingNoticeEnterTimeItem item = new BookingNoticeEnterTimeItem();
        item.setComment("str");
        item.setEndAt("str");
        item.setStartAt("str");
        enterTime.add(item);
        bookingNotice.setEnterTime(enterTime);
        bookingNotice.setEnterWays("str");
        bookingNotice.setExtraDesc("str");
        bookingNotice.setFeeInclude("str");
        bookingNotice.setFeeNotInclude("str");
        bookingNotice.setImportantNotice("str");
        bookingNotice.setPassTimeLimit(0);
        bookingNotice.setTicketPlace("str");
        List<BookingNoticeTicketTimeItem> ticketTime = new ArrayList<BookingNoticeTicketTimeItem>();

        BookingNoticeTicketTimeItem item1 = new BookingNoticeTicketTimeItem();
        item1.setComment("str");
        item1.setEndAt("str");
        item1.setStartAt("str");
        ticketTime.add(item1);
        bookingNotice.setTicketTime(ticketTime);
        request.setBookingNotice(bookingNotice);

        OrderLimitation orderLimitation = new OrderLimitation();
        orderLimitation.setCycleLength(0);
        orderLimitation.setLimitationType(0);
        orderLimitation.setLimitCycle(0);
        orderLimitation.setLimitNum(0);
        request.setOrderLimitation(orderLimitation);
        request.setOutRuleId("str");

        ProviderContactInfo providerContactInfo = new ProviderContactInfo();
        List<ProviderContactInfoProviderBusinessHourItem> providerBusinessHour = new ArrayList<ProviderContactInfoProviderBusinessHourItem>();

        ProviderContactInfoProviderBusinessHourItem item2 = new ProviderContactInfoProviderBusinessHourItem();
        item2.setCloseAt("str");
        item2.setOpenAt("str");
        item2.setTimeInfo("str");
        providerBusinessHour.add(item2);
        providerContactInfo.setProviderBusinessHour(providerBusinessHour);
        providerContactInfo.setProviderName("str");
        providerContactInfo.setProviderTelephone("str");
        request.setProviderContactInfo(providerContactInfo);

        RefundLimitations refundLimitations = new RefundLimitations();
        refundLimitations.setIsRefundable(0);
        List<RefundLimitationsRefundRulesItem> refundRules = new ArrayList<RefundLimitationsRefundRulesItem>();

        RefundLimitationsRefundRulesItem item3 = new RefundLimitationsRefundRulesItem();
        item3.setAheadTime(0);
        item3.setDeductionFee(0);
        item3.setDeductionUnit(0);
        item3.setType(0);
        refundRules.add(item3);
        refundLimitations.setRefundRules(refundRules);
        request.setRefundLimitations(refundLimitations);
        request.setRuleName("str");

        TravelerInfoLimitation travelerInfoLimitation = new TravelerInfoLimitation();
        travelerInfoLimitation.setCredential(0);
        travelerInfoLimitation.setName(0);
        travelerInfoLimitation.setTravelerRequired(0);
        request.setTravelerInfoLimitation(travelerInfoLimitation);

        ValidLimitation validLimitation = new ValidLimitation();
        validLimitation.setDaysTime(0);
        validLimitation.setEndTime(0L);
        validLimitation.setStartTime(0L);
        validLimitation.setTimeType(0);
        request.setValidLimitation(validLimitation);
        PddTicketSkuRuleAddResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "response": {
    "rule_id": "str",
    "rule_version": "str"
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

接口总限流频次：2500次/1秒

### API工具
