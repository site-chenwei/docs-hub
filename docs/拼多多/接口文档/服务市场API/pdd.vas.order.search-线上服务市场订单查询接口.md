---
title: "pdd.vas.order.search - 线上服务市场订单查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.vas.order.search"
menu_path:
  - "服务市场API"
  - "pdd.vas.order.search"
captured_at: "2026-04-09T15:23:49.672Z"
---

# pdd.vas.order.search

## 线上服务市场订单查询接口

更新时间：2021-04-05 11:01:05

¥免费API

不需用户授权

用于拉取回流完成的订单以及线上增量的订购订单

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
| create\_time\_end | LONG | 非必填 | 创建时间结束，UNIX时间戳（ms 级别），默认为当前时间，支持最大范围为7天。 |
| create\_time\_start | LONG | 非必填 | 创建时间开始，UNIX时间戳（ms级别），默认为当前时间往前推7天，支持最大范围为7天。 |
| mall\_id | LONG | 非必填 | 买家店铺id |
| order\_sn | STRING | 非必填 | 服务订单号 |
| order\_status | INTEGER | 非必填 | 订单状态，枚举值，0-未完成，1-已完成，2-已取消，空-全部 |
| page | INTEGER | 必填 | 分页页码 |
| page\_size | INTEGER | 必填 | 分页大小，最大支持100 |
| pay\_time\_end | LONG | 非必填 | 支付时间开始，UNIX时间戳（ms 级别） |
| pay\_time\_start | LONG | 非必填 | 支付时间开始，UNIX时间戳（ms 级别） |
| sku\_id | LONG | 非必填 | 服务sku\_id，可在服务详情页中获取 |
| refund\_status | INTEGER | 非必填 | 售后状态，0-未售后，1-已售后 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| vas\_order\_search\_response | OBJECT |  | response |
| orders | OBJECT\[\] |  | 订单列表 |
| amount | LONG | 10000 | 实付价格 |
| create\_time | LONG | 1588043682000 | 订单创建时间 |
| mall\_id | LONG | 461679218 | 店铺ID |
| order\_sn | STRING | 20200426-000007370036545 | 服务订单ID |
| pay\_status | INTEGER | 1 | 支付状态，枚举值，0-未支付，1-已支付 |
| pay\_time | LONG | 1588043682000 | 支付时间 |
| service\_id | LONG | 1 | 服务ID |
| service\_name | STRING | Dadan | 服务名称 |
| sku\_id | LONG | 1 | 服务SKUID |
| sku\_spec | STRING | 版本：基础版，周期：三个月 | 服务SKU名称 |
| source | INTEGER | 0 | 订单来源，0-线上订购，1-线下回流 |
| time\_length | LONG | 86400 | 订购时长 |
| refund\_finish\_time | LONG | 1569411706758 | 售后完成时间，如果没有申请过售后则为null |
| refund\_status | INTEGER | 0 | 售后状态，0-未售后，1-已售后 |
| mall\_name | STRING | 佐菲的小铺 | 店铺名称 |
| totalCount | INTEGER | 1 | 当前查询条件下所有订单总数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddVasOrderSearchRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddVasOrderSearchResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddVasOrderSearchRequest request = new PddVasOrderSearchRequest();
        request.setCreateTimeEnd(1588043682000L);
        request.setCreateTimeStart(1585192219000L);
        request.setMallId(461679218L);
        request.setOrderSn("20190820210851382487424");
        request.setOrderStatus(1);
        request.setPage(1);
        request.setPageSize(20);
        request.setPayTimeEnd(1588043682000L);
        request.setPayTimeStart(1585192219000L);
        request.setSkuId(1L);
        request.setRefundStatus(0);
        PddVasOrderSearchResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "vas_order_search_response": {
    "orders": [
      {
        "amount": 10000,
        "create_time": 1588043682000,
        "mall_id": 461679218,
        "mall_name": "佐菲的小铺",
        "order_sn": "20200426-000007370036545",
        "pay_status": 1,
        "pay_time": 1588043682000,
        "refund_finish_time": 1569411706758,
        "refund_status": 0,
        "service_id": 1,
        "service_name": "Dadan",
        "sku_id": 1,
        "sku_spec": "版本：基础版，周期：三个月",
        "source": 0,
        "time_length": 86400
      }
    ],
    "totalCount": 1
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
| 服务市场权限包 | 打单、进销存、商品优化分析、企业ERP、仓储管理系统、订单处理、跨境企业ERP报关版 |

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

应用限流频次：20次/1秒

接口总限流频次：2500次/1秒

### API工具
