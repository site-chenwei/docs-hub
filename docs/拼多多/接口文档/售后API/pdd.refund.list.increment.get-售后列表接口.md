---
title: "pdd.refund.list.increment.get - 售后列表接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.refund.list.increment.get"
menu_path:
  - "售后API"
  - "pdd.refund.list.increment.get"
captured_at: "2026-04-09T15:14:22.104Z"
---

# pdd.refund.list.increment.get

## 售后列表接口

更新时间：2023-10-22 15:46:30

¥基础API

必须用户授权

售后列表增量查询

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
| after\_sales\_status | INTEGER | 必填 | 必填，售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货 33：待商家召回 |
| after\_sales\_type | INTEGER | 必填 | 必填，售后类型 1：全部 2：仅退款 3：退货退款 4：换货 5：缺货补寄 6：维修 |
| end\_updated\_at | LONG | 必填 | 必填，最后更新时间结束时间的UNIX时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时00 分 00 秒)起至现在的总秒数 PS：开始时间结束时间间距不超过 30 分钟 |
| order\_sn | STRING | 非必填 | 订单号。若入参含订单号，则可查询订单下的全部售后单。且入参中除订单号，page，page\_size外的其他查询条件不起作用（标记必填的仍旧需要输入）。 |
| page | INTEGER | 非必填 | 返回页码 默认 1，页码从 1 开始 PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值 |
| page\_size | INTEGER | 非必填 | 返回数量，默认 100。最大 100 |
| start\_updated\_at | LONG | 必填 | 必填，最后更新时间开始时间的UNIX时间戳，指格林威治时间 1970 年01月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00分 00 秒)起至现在的总秒数 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| refund\_increment\_get\_response | OBJECT |  | 售后增量订单列表对象 |
| refund\_list | OBJECT\[\] |  | 售后列表对象 |
| after\_sale\_reason | STRING | 不想要了 | 售后原因 |
| after\_sales\_status | INTEGER | 1 | 售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货 |
| after\_sales\_type | INTEGER | 1 | 售后类型 |
| confirm\_time | STRING | 1551612204 | 成团时间 |
| created\_time | STRING | 1551612204 | 创建时间 |
| discount\_amount | STRING | 1 | 订单折扣金额（元） |
| dispute\_refund\_status | INTEGER |  | 1纠纷退款 0非纠纷退款 |
| good\_image | STRING | 1 | 商品图片 |
| goods\_id | LONG | 1 | 商品编码 |
| goods\_name | STRING | 1 | 商品名称 |
| goods\_number | STRING | 1 | 商品数量 |
| goods\_price | STRING | 1 | 商品单价 |
| id | LONG | 1 | 售后编号 |
| order\_amount | STRING | 1 | 订单金额（元） |
| order\_sn | STRING | 190228-355530178612389 | 订单编号 |
| outer\_goods\_id | STRING | 1 | 商家外部编码（商品） |
| outer\_id | STRING | 1 | 商家外部编码（sku） |
| refund\_amount | STRING | 1 | 退款金额（元） |
| refund\_operator\_role | INTEGER | 1 | 同意退款操作人角色0:"默认",1:"用户",2:"商家",3:"平台",4:"系统",5:"团长",6:"司机",7:"代理人" |
| shipping\_name | STRING |  | 退货物流公司名称 |
| sku\_id | STRING | 1 | 商品规格ID |
| speed\_refund\_flag | INTEGER |  | 极速退款标志位 1：极速退款，0：非极速退款 |
| speed\_refund\_status | STRING | 1 | 极速退款状态，"1"：有极速退款资格，"2"：极速退款失败, "3" 表示极速退款成功，其他表示非极速退款 |
| tracking\_number | STRING | 1 | 快递运单号 |
| updated\_time | STRING | 1551612204 | 更新时间 |
| user\_shipping\_status | STRING |  | 0-未勾选 1-消费者选择的收货状态为未收到货 2-消费者选择的收货状态为已收到货 |
| total\_count | INTEGER | 1 | 返回的售后订单列表总数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddRefundListIncrementGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddRefundListIncrementGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddRefundListIncrementGetRequest request = new PddRefundListIncrementGetRequest();
        request.setAfterSalesStatus(1);
        request.setAfterSalesType(1);
        request.setEndUpdatedAt(1551612046L);
        request.setOrderSn("str");
        request.setPage(1);
        request.setPageSize(100);
        request.setStartUpdatedAt(1551612046L);
        PddRefundListIncrementGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "refund_increment_get_response": {
    "refund_list": [
      {
        "after_sale_reason": "不想要了",
        "after_sales_status": 1,
        "after_sales_type": 1,
        "confirm_time": "1551612204",
        "created_time": "1551612204",
        "discount_amount": "1",
        "dispute_refund_status": 0,
        "good_image": "1",
        "goods_id": 1,
        "goods_name": "1",
        "goods_number": "1",
        "goods_price": "1",
        "id": 1,
        "order_amount": "1",
        "order_sn": "190228-355530178612389",
        "outer_goods_id": "1",
        "outer_id": "1",
        "refund_amount": "1",
        "refund_operator_role": 1,
        "shipping_name": "str",
        "sku_id": "1",
        "speed_refund_flag": 0,
        "speed_refund_status": "1",
        "tracking_number": "1",
        "updated_time": "1551612204",
        "user_shipping_status": "str"
      }
    ],
    "total_count": 1
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
| 售后管理权限包 | 打单、进销存、虚拟商家后台系统、企业ERP、商家后台系统、订单处理、电子凭证商家后台系统、跨境企业ERP报关版 |

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

商家限流频次：100次/10秒

接口总限流频次：5500次/1秒

应用限流频次：500次/1秒

### API工具
