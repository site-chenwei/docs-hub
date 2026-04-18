---
title: "pdd.fds.order.get - 订单详情"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.fds.order.get"
menu_path:
  - "电子面单代打API"
  - "pdd.fds.order.get"
captured_at: "2026-04-09T15:23:55.918Z"
---

# pdd.fds.order.get

## 订单详情

更新时间：2023-10-26 00:02:58

¥免费API

必须用户授权

收到分配，更新地址消息，使用该接口拉取订单详情

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
| param\_fds\_order\_get\_request | OBJECT | 必填 | 入参信息 |
| mall\_mask\_id | STRING | 必填 | 代打店铺id |
| order\_mask\_sn | STRING | 必填 | 代打订单号 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| pdd\_fds\_order\_get\_response | OBJECT |  | response |
| allow\_time | LONG | 1577836800000 | 分配时间,毫秒 |
| city | STRING | 上海市 | 市 |
| district | STRING | 长宁区 | 区 |
| goods\_name | STRING | 衣服 | 商品名称 |
| goods\_number | INTEGER | 2 | 商品数量 |
| goods\_spec | STRING | 绿色 小 | 规格 |
| mall\_mask\_id | STRING | 978623a8d9d7425f8c7ff08d2af2875e | 代打店铺id |
| mall\_mask\_name | STRING | xxx店 | 代打店铺自定义名称 |
| order\_mask\_sn | STRING | 4956c0af9ce548ccb7d9c8c3d2c7cce2 | 代打订单号 |
| out\_sku\_sn | STRING | A11 | 商家设置的sku编码 |
| product\_price | INTEGER | 990 | 结算价格，单位：分 |
| product\_sn | STRING | A11 | 货号 |
| province | STRING | 上海市 | 省 |
| receiver\_id | STRING | 4239E33B82F201A3D73D8DA2DDA21AD4 | 收件人姓名+电话+地址相同,receiver\_id字段相同，该功能上线前字段为"" |
| remark | STRING | 发xxx快递 | 卖家备注 |
| return\_status | INTEGER | 1 | 运单回传状态 0：未回传 1：已回传 |
| sf\_only | INTEGER | 1 | 加价发顺丰0：不是 1：是 |
| status | INTEGER | 1 | 分配状态 0：取消分配 1：已分配 |
| after\_sales\_status | INTEGER | 0 | 售后状态 0:初始化;1:待商家处理;2:待分配;3:待客服处理;4:退款中;5:退款成功;6:已撤销;7:客服驳回;9:商家拒绝，待用户处理;10:已同意退货退款;11:待商家处理;12:售后单失败;14:换货补寄待商家处理;15:换货补寄待用户处理;16:换货补寄成功;17:换货补寄失败;18:换货补寄待用户确认完成;21:待商家同意维修;22:待用户确认发货;24:维修关闭;25:维修成功;27:待用户确认收货;31:已同意拒收退款，待用户拒收;32:补寄待商家发货; |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsOrderGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddFdsOrderGetResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsOrderGetRequest.ParamFdsOrderGetRequest;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddFdsOrderGetRequest request = new PddFdsOrderGetRequest();

        ParamFdsOrderGetRequest paramFdsOrderGetRequest = new ParamFdsOrderGetRequest();
        paramFdsOrderGetRequest.setMallMaskId("978623a8d9d7425f8c7ff08d2af2875e");
        paramFdsOrderGetRequest.setOrderMaskSn("4956c0af9ce548ccb7d9c8c3d2c7cce2");
        request.setParamFdsOrderGetRequest(paramFdsOrderGetRequest);
        PddFdsOrderGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "pdd_fds_order_get_response": {
    "after_sales_status": 0,
    "allow_time": 1577836800000,
    "city": "上海市",
    "district": "长宁区",
    "goods_name": "衣服",
    "goods_number": 2,
    "goods_spec": "绿色 小",
    "mall_mask_id": "978623a8d9d7425f8c7ff08d2af2875e",
    "mall_mask_name": "xxx店",
    "order_mask_sn": "4956c0af9ce548ccb7d9c8c3d2c7cce2",
    "out_sku_sn": "A11",
    "product_price": 990,
    "product_sn": "A11",
    "province": "上海市",
    "receiver_id": "4239E33B82F201A3D73D8DA2DDA21AD4",
    "remark": "发xxx快递",
    "return_status": 1,
    "sf_only": 1,
    "status": 1
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
| 电子面单代打权限包 | 打单、进销存、企业ERP、商家后台系统、仓储管理系统、厂商代发货后台系统 |

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

商家限流频次：200次/1秒

接口总限流频次：2000次/1秒

### API工具
