---
title: "pdd.voucher.ota.card.verification - 卡券（电子）核销接口（平台生成卡密）"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.voucher.ota.card.verification"
menu_path:
  - "卡券API"
  - "pdd.voucher.ota.card.verification"
captured_at: "2026-04-09T15:20:57.295Z"
---

# pdd.voucher.ota.card.verification

## 卡券（电子）核销接口（平台生成卡密）

更新时间：2021-01-18 14:19:25

¥免费API

必须用户授权

平台生成卡密类卡券核销

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
| card\_no | STRING | 必填 | 待核销的券码 |
| store\_id | LONG | 必填 | 核销门店id |
| store\_name | STRING | 必填 | 核销门店名称 |
| order\_sn | STRING | 非必填 | 拼多多订单编号 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| voucher\_ota\_card\_verification\_response | OBJECT |  |  |
| errorCode | INTEGER |  |  |
| errorMsg | STRING |  |  |
| result | OBJECT |  |  |
| card\_no | STRING |  | 券码 |
| mall\_id | LONG |  | 店铺编码 |
| order\_sn | STRING |  | 订单号 |
| status | INTEGER |  | 核销状态（1-未核销，2-已核销， 3-已过期，4-已销毁，99-核销中） |
| store\_id | LONG |  | 门店编码 |
| store\_name | STRING |  | 门店名称 |
| verification\_time | STRING |  | 核销时间（yyyy-MM-dd HH:mm:ss格式） |
| success | BOOLEAN |  |  |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddVoucherOtaCardVerificationRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddVoucherOtaCardVerificationResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddVoucherOtaCardVerificationRequest request = new PddVoucherOtaCardVerificationRequest();
        request.setCardNo("str");
        request.setStoreId(0L);
        request.setStoreName("str");
        request.setOrderSn("str");
        PddVoucherOtaCardVerificationResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "voucher_ota_card_verification_response": {
    "errorCode": 0,
    "errorMsg": "str",
    "result": {
      "card_no": "str",
      "mall_id": 0,
      "order_sn": "str",
      "status": 0,
      "store_id": 0,
      "store_name": "str",
      "verification_time": "str"
    },
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
| 卡券商工具权限包 | 商家后台系统 |
| 电子凭证权限包 | 电子凭证商家后台系统 |

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
| 50001 | 业务服务错误 | 100001 | 该卡券不是OTA卡 | 请核实订单 |
| 1000010 | 为保证一致性，该卡券此刻不允许核销 | 重试 |
| 1000012 | 券码已过期 | 请核实订单 |
| 100002 | 非本店铺商品，请核对订单 | 请核实订单 |
| 100004 | 消费者已发起售后，请退款后重新购买 | 请核实订单 |
| 100005 | 查询售后信息失败 | 重试 |
| 100006 | 券码错误 | 请核实订单 |
| 100007 | 店铺编码不准确 | 请核实订单 |
| 60004 | 卡券待核销单子不存在，请核实 | 请核实订单 |
| 60005 | 该卡券已经过期，无法核销 | 请核实订单 |
| 60006 | 该卡券已经被销毁，无法核销 | 请核实订单 |
| 60008 | 当前待核销订单状态不合法 | 请核实订单 |
| 60009 | 核销订单信息不存在 | 请核实订单 |
| 60010 | 该卡券已经被核销成功，请确认 | 请核实订单 |
| 60011 | 订单已发起退款，无法核销 | 请核实订单 |
| 60012 | 订单可能存在售后问题，请核实 | 请核实订单 |

### 限流规则

接口总限流频次：10000次/3600秒

### API工具
