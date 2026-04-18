---
title: "pdd.fds.waybill.get - 电子面单取号"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.fds.waybill.get"
menu_path:
  - "电子面单代打API"
  - "pdd.fds.waybill.get"
captured_at: "2026-04-09T15:24:08.415Z"
---

# pdd.fds.waybill.get

## 电子面单取号

更新时间：2020-08-16 15:09:24

¥免费API

必须用户授权

使用商家订单上的收件人信息电子面单取号

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
| param\_fds\_waybill\_get\_request | OBJECT | 必填 | 入参信息 |
| sender | OBJECT | 必填 | 发货人信息 |
| address | OBJECT | 必填 | 发货地址，需要入参与 search 接口中的发货人地址信息一致 |
| city | STRING | 必填 | 市 |
| country | STRING | 非必填 | 国家/地区 |
| detail | STRING | 必填 | 详细地址 |
| district | STRING | 必填 | 区 |
| province | STRING | 必填 | 省 |
| town | STRING | 非必填 | 街道 |
| mobile | STRING | 必填 | 手机号码 |
| name | STRING | 必填 | 姓名 |
| phone | STRING | 必填 | 固定电话 |
| trade\_order\_info\_dtos | OBJECT\[\] | 必填 | 取号列表 |
| logistics\_services | STRING | 非必填 | 物流服务内容链接 |
| object\_id | STRING | 必填 | 请求id |
| order\_info | OBJECT | 必填 | 订单信息 |
| order\_channels\_type | STRING | 必填 | 订单渠道平台编码 |
| trade\_order\_list | OBJECT\[\] | 必填 | 订单列表，限制100个 |
| mall\_mask\_id | STRING | 必填 | 代打店铺id |
| order\_mask\_sn | STRING | 必填 | 代打订单号 |
| package\_info | OBJECT | 必填 | 包裹信息 |
| goods\_description | STRING | 非必填 | 快运货品描述 |
| id | STRING | 非必填 | 包裹id,拆合单使用 |
| items | OBJECT\[\] | 必填 | 商品信息,数量限制为100 |
| count | INTEGER | 必填 | 数量 |
| name | STRING | 必填 | 商品名称 |
| packaging\_description | STRING | 非必填 | 快运包装方式描述 |
| total\_packages\_count | STRING | 非必填 | 子母件总包裹数 |
| volume | INTEGER | 非必填 | 体积, 单位 ml |
| weight | INTEGER | 非必填 | 重量,单位 g |
| template\_url | STRING | 必填 | 标准模板模板URL |
| user\_id | LONG | 必填 | 使用者ID |
| wp\_code | STRING | 必填 | 物流公司 Code ，枚举： YTO- 圆通，ZTO-中通，YUNDA-韵达，STO-申通 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| pdd\_fds\_waybill\_get\_response | OBJECT |  | response |
| modules | OBJECT\[\] |  | 系统自动生成 |
| object\_id | STRING | 123 | 请求 id |
| parent\_waybill\_code | STRING |  | 快运母单号 |
| print\_data | STRING |  | 模板内容（模板内容加密，只需透传至打印组件 |
| waybill\_code | STRING | 39083710 | 面单号 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddFdsWaybillGetResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequest;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequestSender;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequestSenderAddress;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequestTradeOrderInfoDtosItem;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfo;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfoTradeOrderListItem;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfo;
import com.pdd.pop.sdk.http.api.pop.request.PddFdsWaybillGetRequest.ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfoItemsItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddFdsWaybillGetRequest request = new PddFdsWaybillGetRequest();

        ParamFdsWaybillGetRequest paramFdsWaybillGetRequest = new ParamFdsWaybillGetRequest();

        ParamFdsWaybillGetRequestSender sender = new ParamFdsWaybillGetRequestSender();

        ParamFdsWaybillGetRequestSenderAddress address = new ParamFdsWaybillGetRequestSenderAddress();
        address.setCity("上海市");
        address.setCountry("str");
        address.setDetail("金虹桥");
        address.setDistrict("长宁区");
        address.setProvince("上海市");
        address.setTown("天山街道");
        sender.setAddress(address);
        sender.setMobile("18811211111");
        sender.setName("xiaoye");
        sender.setPhone("18178111155");
        paramFdsWaybillGetRequest.setSender(sender);
        List<ParamFdsWaybillGetRequestTradeOrderInfoDtosItem> tradeOrderInfoDtos = new ArrayList<ParamFdsWaybillGetRequestTradeOrderInfoDtosItem>();

        ParamFdsWaybillGetRequestTradeOrderInfoDtosItem item = new ParamFdsWaybillGetRequestTradeOrderInfoDtosItem();
        item.setLogisticsServices("str");
        item.setObjectId("str");

        ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfo orderInfo = new ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfo();
        orderInfo.setOrderChannelsType("PDD");
        List<ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfoTradeOrderListItem> tradeOrderList = new ArrayList<ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfoTradeOrderListItem>();

        ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfoTradeOrderListItem item1 = new ParamFdsWaybillGetRequestTradeOrderInfoDtosItemOrderInfoTradeOrderListItem();
        item1.setMallMaskId("978623a8d9d7425f8c7ff08d2af2875e");
        item1.setOrderMaskSn("4956c0af9ce548ccb7d9c8c3d2c7cce2");
        tradeOrderList.add(item1);
        orderInfo.setTradeOrderList(tradeOrderList);
        item.setOrderInfo(orderInfo);

        ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfo packageInfo = new ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfo();
        packageInfo.setGoodsDescription("str");
        packageInfo.setId("str");
        List<ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfoItemsItem> items = new ArrayList<ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfoItemsItem>();

        ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfoItemsItem item2 = new ParamFdsWaybillGetRequestTradeOrderInfoDtosItemPackageInfoItemsItem();
        item2.setCount(1);
        item2.setName("str");
        items.add(item2);
        packageInfo.setItems(items);
        packageInfo.setPackagingDescription("str");
        packageInfo.setTotalPackagesCount("str");
        packageInfo.setVolume(0);
        packageInfo.setWeight(0);
        item.setPackageInfo(packageInfo);
        item.setTemplateUrl("str");
        item.setUserId(0L);
        tradeOrderInfoDtos.add(item);
        paramFdsWaybillGetRequest.setTradeOrderInfoDtos(tradeOrderInfoDtos);
        paramFdsWaybillGetRequest.setWpCode("YTO");
        request.setParamFdsWaybillGetRequest(paramFdsWaybillGetRequest);
        PddFdsWaybillGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "pdd_fds_waybill_get_response": {
    "modules": [
      {
        "object_id": "123",
        "parent_waybill_code": "str",
        "print_data": "str",
        "waybill_code": "39083710"
      }
    ]
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

接口总限流频次：1000次/1秒

### API工具
