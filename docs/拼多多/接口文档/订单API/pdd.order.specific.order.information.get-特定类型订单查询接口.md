---
title: "pdd.order.specific.order.information.get - 特定类型订单查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.order.specific.order.information.get"
menu_path:
  - "订单API"
  - "pdd.order.specific.order.information.get"
captured_at: "2026-04-09T15:13:22.781Z"
---

# pdd.order.specific.order.information.get

## 特定类型订单查询接口

更新时间：2026-03-26 15:17:16

¥免费API

必须用户授权

查询特定类型的订单详情（目前仅支持查询下单时间15个月内的分批发货订单）

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
| order\_sn | STRING | 必填 | 订单号 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| specific\_order\_info | OBJECT |  | response |
| after\_sales\_status | INTEGER |  | 售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货 33：同意召回后退款，待商家召回 |
| buyer\_memo | STRING |  | 买家留言信息 |
| created\_time | STRING |  | 创建时间 |
| delivery\_schedule\_sub\_order\_list | OBJECT\[\] |  | 分批发货子单信息列表 |
| city | STRING |  | 收件地城市 |
| city\_id | INTEGER |  | 城市编码 |
| goods\_entry\_list | OBJECT\[\] |  | 子单商品词条信息 |
| name | STRING |  | 词条名称 |
| last\_ship\_time | STRING |  | 子单承诺发货时间 |
| logistics\_id | INTEGER |  | 子单快递公司编号 |
| province | STRING |  | 收件地省份 |
| province\_id | INTEGER |  | 省份编码 |
| receiver\_address | STRING |  | 收件人地址，不拼接省市区。子单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串。 |
| receiver\_name | STRING |  | 收件人姓名。子单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串 |
| receiver\_phone | STRING |  | 收件人电话。子单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串。 |
| sequence\_id | INTEGER |  | 批次 |
| sub\_order\_status | INTEGER |  | 子单状态（1-待发货；2-已发货；31-已退款） |
| town | STRING |  | 收件地区县 |
| town\_id | INTEGER |  | 区县编码 |
| tracking\_number | STRING |  | 子单快递运单号 |
| express\_memos | OBJECT\[\] |  | 物流备注 |
| scene | INTEGER |  | 备注场景，1-消费者指定不想使用的物流 |
| tag | STRING |  | 备注标签 |
| item\_list | OBJECT\[\] |  | 订单中商品sku列表 |
| goods\_count | INTEGER |  | 商品数量 |
| goods\_id | LONG |  | 商品编号 |
| goods\_img | STRING |  | 商品图片 |
| goods\_name | STRING |  | 商品名称 |
| goods\_price | DOUBLE |  | 商品销售价格 |
| goods\_spec | STRING |  | 商品规格，使用（规格值1,规格值2）组合作为sku的表示，中间以英文逗号隔开 |
| outer\_goods\_id | STRING |  | 商家外部编码（商品），注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。 |
| outer\_id | STRING |  | 商家外部sku编码 |
| sku\_id | LONG |  | 商品规格编码 |
| order\_sn | STRING |  | 订单编号 |
| order\_status | INTEGER |  | 发货状态，枚举值：1：待发货，2：已发货待签收，3：已签收 |
| refund\_status | INTEGER |  | 退款状态，枚举值：1：无售后或售后关闭，2：售后处理中，3：退款中，4： 退款成功 |
| remark | STRING |  | 商家订单备注 |
| remark\_tag | INTEGER |  | 订单备注标记，1-红色，2-黄色，3-绿色，4-蓝色，5-紫色 |
| remark\_tag\_name | STRING |  | 订单备注标记名称 |
| risk\_control\_status | INTEGER |  | 订单审核状态（0-正常订单， 1-审核中订单） |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddOrderSpecificOrderInformationGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddOrderSpecificOrderInformationGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddOrderSpecificOrderInformationGetRequest request = new PddOrderSpecificOrderInformationGetRequest();
        request.setOrderSn("str");
        PddOrderSpecificOrderInformationGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "specific_order_info": {
    "after_sales_status": 0,
    "buyer_memo": "str",
    "created_time": "str",
    "delivery_schedule_sub_order_list": [
      {
        "city": "str",
        "city_id": 0,
        "goods_entry_list": [
          {
            "name": "str"
          }
        ],
        "last_ship_time": "str",
        "logistics_id": 0,
        "province": "str",
        "province_id": 0,
        "receiver_address": "str",
        "receiver_name": "str",
        "receiver_phone": "str",
        "sequence_id": 0,
        "sub_order_status": 0,
        "town": "str",
        "town_id": 0,
        "tracking_number": "str"
      }
    ],
    "express_memos": [
      {
        "scene": 0,
        "tag": "str"
      }
    ],
    "item_list": [
      {
        "goods_count": 0,
        "goods_id": 0,
        "goods_img": "str",
        "goods_name": "str",
        "goods_price": 0.0,
        "goods_spec": "str",
        "outer_goods_id": "str",
        "outer_id": "str",
        "sku_id": 0
      }
    ],
    "order_sn": "str",
    "order_status": 0,
    "refund_status": 0,
    "remark": "str",
    "remark_tag": 0,
    "remark_tag_name": "str",
    "risk_control_status": 0
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
| 订单信息查询权限包 | 打单、进销存、虚拟商家后台系统、企业ERP、商家后台系统、订单处理、电子凭证商家后台系统、跨境企业ERP报关版 |

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
