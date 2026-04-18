---
title: "pdd.logistics.onlinedelivery.receipt.list - 查询已寄件寄件单列表"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.logistics.onlinedelivery.receipt.list"
menu_path:
  - "商家寄件API"
  - "pdd.logistics.onlinedelivery.receipt.list"
captured_at: "2026-04-09T15:26:19.911Z"
---

# pdd.logistics.onlinedelivery.receipt.list

## 查询已寄件寄件单列表

更新时间：2025-10-30 23:21:17

¥免费API

必须用户授权

查询商家已经寄过件的运单列表，分状态展示（全部、待接单、待揽收、已取消、配送中、已完成）

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
| pageNo | INTEGER | 必填 | 分页查询页号 |
| pageSize | INTEGER | 必填 | 分页大小 |
| status | INTEGER | 非必填 | 寄件单状态枚举值（0待取件；100待揽收；200配送中、300、已完成、400已取消） |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| response | OBJECT |  | response |
| errorCode | INTEGER |  | errorCode |
| errorMsg | STRING |  | errorMsg |
| result | OBJECT |  | result |
| deliveryReceiptList | OBJECT\[\] |  | 寄件单列表 |
| cancelFlag | BOOLEAN | true | 是否可以取消（未核重下发‘是’） |
| courier | OBJECT |  | 小件员信息 |
| courierMobile | STRING |  | 快递员姓名（脱敏） |
| courierName | STRING |  | 快递员电话（脱敏） |
| shipCode | STRING |  | 快递公司code |
| shipName | STRING |  | 快递公司名称 |
| deliveryReceiptSn | STRING | 1234 | 寄件单号 |
| orderSn | STRING | 1234 | PDD订单号 |
| packageHintCode | STRING | 1234 | 包裹码 |
| payFailReason | STRING |  | 支付失败原因 |
| payStatus | INTEGER | 0 | 支付状态（0：待支付；10：已支付） |
| payStatusDesc | STRING | 待支付 | 支付状态描述 |
| predictPrice | LONG | 100 | 预估价格 |
| predictWeight | INTEGER | 10 | 预估重量 |
| realPrice | LONG | 10 | realWeight |
| realWeight | INTEGER | 10 | 实际重量 |
| receiver | OBJECT |  | 收件人联系信息 |
| addressDetail | STRING |  | 详细地址（脱敏） |
| cityCode | STRING |  | 城市ID |
| cityName | STRING |  | 城市名称 |
| contactMobile | STRING |  | 联系人手机号（脱敏） |
| contactName | STRING |  | 联系人姓名（脱敏） |
| districtCode | STRING |  | 区ID |
| districtName | STRING |  | 区名称 |
| provinceCode | STRING |  | 省份ID |
| provinceName | STRING |  | 省份名称 |
| townCode | STRING |  | 镇ID |
| townName | STRING |  | 镇名称 |
| sender | OBJECT |  | 发件人联系信息 |
| addressDetail | STRING |  | 详细地址（脱敏） |
| cityCode | STRING |  | 城市ID |
| cityName | STRING |  | 城市名称 |
| contactMobile | STRING |  | 联系人手机号（脱敏） |
| contactName | STRING |  | 联系人姓名（脱敏） |
| districtCode | STRING |  | 区ID |
| districtName | STRING |  | 区名称 |
| provinceCode | STRING |  | 省份ID |
| provinceName | STRING |  | 省份名称 |
| townCode | STRING |  | 镇ID |
| townName | STRING |  | 镇名称 |
| status | INTEGER | 100 | 寄件单状态枚举值（0待取件；100待揽收；200配送中、300、已完成、400已取消） |
| statusDesc | STRING |  | 寄件单状态描述（0待取件；100待揽收；200配送中、300、已完成、400已取消） |
| waybillCode | STRING |  | 运单号 |
| shipCode | STRING |  | 快递公司编码 |
| shipName | STRING |  | 快递公司名称 |
| total | LONG | 10 | 查询总数 |
| success | BOOLEAN |  | success |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddLogisticsOnlinedeliveryReceiptListRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddLogisticsOnlinedeliveryReceiptListResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddLogisticsOnlinedeliveryReceiptListRequest.Request;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddLogisticsOnlinedeliveryReceiptListRequest request = new PddLogisticsOnlinedeliveryReceiptListRequest();

        Request request1 = new Request();
        request1.setPageNo(1);
        request1.setPageSize(10);
        request1.setStatus(100);
        request.setRequest(request1);
        PddLogisticsOnlinedeliveryReceiptListResponse response = client.syncInvoke(request, accessToken);
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
      "deliveryReceiptList": [
        {
          "cancelFlag": true,
          "courier": {
            "courierMobile": "str",
            "courierName": "str",
            "shipCode": "str",
            "shipName": "str"
          },
          "deliveryReceiptSn": "1234",
          "orderSn": "1234",
          "packageHintCode": "1234",
          "payFailReason": "str",
          "payStatus": 0,
          "payStatusDesc": "待支付",
          "predictPrice": 100,
          "predictWeight": 10,
          "realPrice": 10,
          "realWeight": 10,
          "receiver": {
            "addressDetail": "str",
            "cityCode": "str",
            "cityName": "str",
            "contactMobile": "str",
            "contactName": "str",
            "districtCode": "str",
            "districtName": "str",
            "provinceCode": "str",
            "provinceName": "str",
            "townCode": "str",
            "townName": "str"
          },
          "sender": {
            "addressDetail": "str",
            "cityCode": "str",
            "cityName": "str",
            "contactMobile": "str",
            "contactName": "str",
            "districtCode": "str",
            "districtName": "str",
            "provinceCode": "str",
            "provinceName": "str",
            "townCode": "str",
            "townName": "str"
          },
          "shipCode": "str",
          "shipName": "str",
          "status": 100,
          "statusDesc": "str",
          "waybillCode": "str"
        }
      ],
      "total": 10
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
