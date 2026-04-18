---
title: "pdd.logistics.onlinedelivery.predict.price - 查询快递公司预估金额"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.logistics.onlinedelivery.predict.price"
menu_path:
  - "商家寄件API"
  - "pdd.logistics.onlinedelivery.predict.price"
captured_at: "2026-04-09T15:26:07.380Z"
---

# pdd.logistics.onlinedelivery.predict.price

## 查询快递公司预估金额

更新时间：2025-10-29 14:43:17

¥免费API

必须用户授权

在前端支持商家查看商家寄件快递公司预估运费金额

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
| request | OBJECT | 必填 | request |
| addressId | LONG | 非必填 | 地址id(没填，则省市区详细地址必填) |
| predictOrders | OBJECT\[\] | 必填 | 商品信息 |
| orderSn | STRING | 必填 | 订单号 |
| predictWeight | INTEGER | 必填 | 预估重量（单位：克） |
| sendCityName | STRING | 非必填 | 发件地城市名称(没填，则addressId必填) |
| sendDetail | STRING | 非必填 | 详细地址(没填，则addressId必填) |
| sendDistrictName | STRING | 非必填 | 发件地区县名称(没填，则addressId必填) |
| sendProvinceName | STRING | 非必填 | 发件地省名称(没填，则addressId必填) |
| shipCode | STRING | 必填 | 快递公司编码 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| response | OBJECT |  | response |
| errorCode | INTEGER |  | errorCode |
| errorMsg | STRING |  | errorMsg |
| result | OBJECT |  | result |
| needCount | INTEGER | 100 | 到达下一阶段所需单量 |
| nextStageBasePrice | LONG | 10 | 下一阶段首重(分) |
| nextStageBasePriceStr | STRING | 10 | 下一阶段首重(元) |
| priceDetail | OBJECT\[\] |  | 每单价格明细 |
| additionalCalculatePrice | LONG | 10 | 续重金额（分） |
| additionalCalculatePriceStr | STRING | 10 | 续重金额（元） |
| additionalCount | INTEGER | 10 | 1kg以上3kg以下续重数量 |
| additionalWeightPrice | LONG | 10 | 1kg以上3kg以下续重价格（分） |
| additionalWeightPriceStr | STRING | 10 | 1kg以上3kg以下续重价格（元） |
| firstWeightPrice | LONG | 10 | 首重价格（分） |
| firstWeightPriceStr | STRING | 10 | 首重价格（元） |
| orderSn | STRING | 1234 | 订单号 |
| receiverProvince | STRING | 上海市 | 收件省 |
| secondAdditionalCount | INTEGER | 10 | 3kg以上续重数量 |
| secondAdditionalWeightPrice | LONG | 10 | 3kg以上续重价格（分） |
| secondAdditionalWeightPriceStr | STRING | 10 | 3kg以上续重价格（元） |
| senderProvince | STRING | 上海市 | 发件省 |
| sumPrice | LONG | 10 | 首重加续重总金额（分） |
| sumPriceStr | STRING | 10 | 首重加续重总金额（元） |
| totalWeight | INTEGER | 10 | 订单商品重量 |
| totalPrice | LONG | 10 | 总计价格(分) |
| totalPriceStr | STRING | 10 | 总计价格(元) |
| success | BOOLEAN |  | success |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddLogisticsOnlinedeliveryPredictPriceRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddLogisticsOnlinedeliveryPredictPriceResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddLogisticsOnlinedeliveryPredictPriceRequest.Request;
import com.pdd.pop.sdk.http.api.pop.request.PddLogisticsOnlinedeliveryPredictPriceRequest.RequestPredictOrdersItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddLogisticsOnlinedeliveryPredictPriceRequest request = new PddLogisticsOnlinedeliveryPredictPriceRequest();

        Request request1 = new Request();
        request1.setAddressId(9999L);
        List<RequestPredictOrdersItem> predictOrders = new ArrayList<RequestPredictOrdersItem>();

        RequestPredictOrdersItem item = new RequestPredictOrdersItem();
        item.setOrderSn("123456");
        item.setPredictWeight(10);
        predictOrders.add(item);
        request1.setPredictOrders(predictOrders);
        request1.setSendCityName("上海市");
        request1.setSendDetail("天山路街道555号");
        request1.setSendDistrictName("长宁区");
        request1.setSendProvinceName("上海市");
        request1.setShipCode("JTSD");
        request.setRequest(request1);
        PddLogisticsOnlinedeliveryPredictPriceResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "response": {
    "errorCode": 0,
    "errorMsg": "str",
    "result": {
      "needCount": 100,
      "nextStageBasePrice": 10,
      "nextStageBasePriceStr": "10",
      "priceDetail": [
        {
          "additionalCalculatePrice": 10,
          "additionalCalculatePriceStr": "10",
          "additionalCount": 10,
          "additionalWeightPrice": 10,
          "additionalWeightPriceStr": "10",
          "firstWeightPrice": 10,
          "firstWeightPriceStr": "10",
          "orderSn": "1234",
          "receiverProvince": "上海市",
          "secondAdditionalCount": 10,
          "secondAdditionalWeightPrice": 10,
          "secondAdditionalWeightPriceStr": "10",
          "senderProvince": "上海市",
          "sumPrice": 10,
          "sumPriceStr": "10",
          "totalWeight": 10
        }
      ],
      "totalPrice": 10,
      "totalPriceStr": "10"
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
| 电子面单权限包 | 打单、进销存、虚拟商家后台系统、电子面单、企业ERP、商家后台系统、仓储管理系统、快团团、快团团团长后台系统、跨境企业ERP报关版 |

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

### API工具
