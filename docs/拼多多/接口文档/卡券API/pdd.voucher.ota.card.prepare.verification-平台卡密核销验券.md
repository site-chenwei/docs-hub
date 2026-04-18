---
title: "pdd.voucher.ota.card.prepare.verification - 平台卡密核销验券"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.voucher.ota.card.prepare.verification"
menu_path:
  - "卡券API"
  - "pdd.voucher.ota.card.prepare.verification"
captured_at: "2026-04-09T15:20:54.127Z"
---

# pdd.voucher.ota.card.prepare.verification

## 平台卡密核销验券

更新时间：2021-01-31 14:28:52

¥免费API

必须用户授权

查询平台生成卡密对应的卡券信息、商品信息和订单信息

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
| request | OBJECT | 必填 | 请求体 |
| card\_no | STRING | 必填 | 卡密 |
| store\_id | LONG | 非必填 | 门店id |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| response | OBJECT |  | 响应体 |
| errorCode | INTEGER | 1000000 |  |
| errorMsg | STRING |  |  |
| result | OBJECT |  | 卡密和订单信息 |
| card\_vo | OBJECT |  | 卡券信息 |
| available\_end\_time | LONG | 1611145572 | 卡券有效期结束时间，单位秒 |
| available\_start\_time | LONG | 1611045540 | 卡券有效期开始时间，单位秒 |
| mask\_card\_no | STRING | 1234\*\*\*1233 | 打码卡密 |
| remain\_times | INTEGER | 1 | 剩余可用次数 |
| status | INTEGER | 1 | 券状态码。1-未核销，2-已核销， 3-已过期，4-已销毁 |
| status\_tips | STRING | 未核销 | 状态文案 |
| total\_times | INTEGER | 2 | 总次数 |
| order\_goods\_vo | OBJECT |  | 商品信息 |
| goods\_name | STRING | 抱枕兑换券 | 商品标题 |
| goods\_number | INTEGER | 1 | 购买商品数 |
| out\_goods\_sn | STRING | 4231 | 外部商品编码 |
| out\_sku\_sn | STRING | 1234 | 外部sku编码 |
| spec | STRING | 黑色抱枕兑换券 | 规格 |
| order\_vo | OBJECT |  | 订单信息 |
| order\_amount\_fen | LONG | 100 | 用户实付金额 |
| order\_sn | STRING | 200804-659071959240704 | 订单编号 |
| success | BOOLEAN | true |  |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddVoucherOtaCardPrepareVerificationRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddVoucherOtaCardPrepareVerificationResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddVoucherOtaCardPrepareVerificationRequest.Request;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddVoucherOtaCardPrepareVerificationRequest request = new PddVoucherOtaCardPrepareVerificationRequest();

        Request request1 = new Request();
        request1.setCardNo("str");
        request1.setStoreId(0L);
        request.setRequest(request1);
        PddVoucherOtaCardPrepareVerificationResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "response": {
    "errorCode": 1000000,
    "errorMsg": "str",
    "result": {
      "card_vo": {
        "available_end_time": 1611145572,
        "available_start_time": 1611045540,
        "mask_card_no": "1234***1233",
        "remain_times": 1,
        "status": 1,
        "status_tips": "未核销",
        "total_times": 2
      },
      "order_goods_vo": {
        "goods_name": "抱枕兑换券",
        "goods_number": 1,
        "out_goods_sn": "4231",
        "out_sku_sn": "1234",
        "spec": "黑色抱枕兑换券"
      },
      "order_vo": {
        "order_amount_fen": 100,
        "order_sn": "200804-659071959240704"
      }
    },
    "success": true
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
| 50001 | 业务服务错误 |  |  |  |

### 限流规则

接口总限流频次：500次/1秒

### API工具
