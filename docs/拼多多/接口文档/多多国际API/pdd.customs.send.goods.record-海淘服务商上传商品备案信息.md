---
title: "pdd.customs.send.goods.record - 海淘服务商上传商品备案信息"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.customs.send.goods.record"
menu_path:
  - "多多国际API"
  - "pdd.customs.send.goods.record"
captured_at: "2026-04-09T15:24:43.078Z"
---

# pdd.customs.send.goods.record

## 海淘服务商上传商品备案信息

更新时间：2022-07-12 15:57:39

¥免费API

必须用户授权

海淘服务商上传商品备案信息

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
| request | OBJECT | 必填 | 上传备案商品请求 |
| goods\_list | OBJECT\[\] | 非必填 | 备案商品列表 |
| bar\_code | STRING | 非必填 | 条形码 |
| bonded\_warehouse\_name | STRING | 非必填 | 保税仓名称 |
| brand\_chinese\_name | STRING | 非必填 | 品牌中文名称 |
| brand\_english\_name | STRING | 非必填 | 品牌英文名称 |
| category | STRING | 非必填 | 品类 |
| consumption\_tax\_rate | DOUBLE | 非必填 | 消费税率，单位% |
| cost\_price | DOUBLE | 非必填 | 成本价（RMB） |
| customs\_code | STRING | 非必填 | 海关关区代码 |
| ebc\_name | STRING | 非必填 | 备案电商企业的海关注册登记名称(备案的电商企业名称) |
| ems\_no | STRING | 非必填 | 账册编号 |
| expiration\_date | STRING | 非必填 | 保质期 |
| gross\_weight | DOUBLE | 非必填 | 毛重（KG） |
| hs\_code | STRING | 非必填 | 海关HS code |
| img\_url | STRING | 非必填 | 备案商品图片链接 |
| item\_no | STRING | 非必填 | 电商企业的商品编号(skuId非pdd skuId) |
| item\_record\_no | STRING | 非必填 | 物料号 |
| manufacturing\_company\_name | STRING | 非必填 | 生产企业名称 |
| manufacturing\_company\_registration\_no | STRING | 非必填 | 生产企业注册号 |
| manufacturing\_factory\_address | STRING | 非必填 | 生产厂家地址（奶制品必填） |
| net\_weight | DOUBLE | 非必填 | 净重（KG） |
| port\_code | STRING | 非必填 | 海关口岸代码 |
| producing\_country | STRING | 非必填 | 生产国代码 |
| product\_record\_no | STRING | 非必填 | 产品国检备案编号 |
| qty1 | DOUBLE | 非必填 | 法定第一数量 |
| qty2 | DOUBLE | 非必填 | 法定第二数量 |
| record\_chinese\_name | STRING | 非必填 | 备案商品中文名称 |
| record\_english\_name | STRING | 非必填 | 备案商品英文名称 |
| record\_model | STRING | 非必填 | 商品规格型号(报文gmodel) |
| specification | STRING | 非必填 | 型号 |
| stock | LONG | 非必填 | 库存数量 |
| stock\_time | STRING | 非必填 | 库存时间 |
| tariff\_rate | DOUBLE | 非必填 | 关税税率,单位% |
| unit | STRING | 非必填 | 申报单位代码 |
| unit1 | STRING | 非必填 | 法定第一单位代码 |
| unit2 | STRING | 非必填 | 法定第二单位代码 |
| unit\_price | DOUBLE | 非必填 | 单价（RMB） |
| value\_added\_tax\_rate | DOUBLE | 非必填 | 增值税率，单位% |
| vendor\_name | STRING | 非必填 | 供应商名称 |
| wc\_code | STRING | 非必填 | 备案仓储企业代码 |
| wc\_name | STRING | 非必填 | 备案仓储企业的海关注册登记名称 |
| website | STRING | 非必填 | 网络链接 |
| wrap\_type | STRING | 非必填 | 包装方式 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| response | OBJECT |  |  |
| error\_code | INTEGER |  |  |
| error\_msg | STRING |  |  |
| result | STRING |  |  |
| success | BOOLEAN |  |  |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddCustomsSendGoodsRecordRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddCustomsSendGoodsRecordResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddCustomsSendGoodsRecordRequest.Request;
import com.pdd.pop.sdk.http.api.pop.request.PddCustomsSendGoodsRecordRequest.RequestGoodsListItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCustomsSendGoodsRecordRequest request = new PddCustomsSendGoodsRecordRequest();

        Request request1 = new Request();
        List<RequestGoodsListItem> goodsList = new ArrayList<RequestGoodsListItem>();

        RequestGoodsListItem item = new RequestGoodsListItem();
        item.setBarCode("str");
        item.setBondedWarehouseName("str");
        item.setBrandChineseName("str");
        item.setBrandEnglishName("str");
        item.setCategory("str");
        item.setConsumptionTaxRate((double) 0.0);
        item.setCostPrice((double) 0.0);
        item.setCustomsCode("str");
        item.setEbcName("str");
        item.setEmsNo("str");
        item.setExpirationDate("str");
        item.setGrossWeight((double) 0.0);
        item.setHsCode("str");
        item.setImgUrl("str");
        item.setItemNo("str");
        item.setItemRecordNo("str");
        item.setManufacturingCompanyName("str");
        item.setManufacturingCompanyRegistrationNo("str");
        item.setManufacturingFactoryAddress("str");
        item.setNetWeight((double) 0.0);
        item.setPortCode("str");
        item.setProducingCountry("str");
        item.setProductRecordNo("str");
        item.setQty1((double) 0.0);
        item.setQty2((double) 0.0);
        item.setRecordChineseName("str");
        item.setRecordEnglishName("str");
        item.setRecordModel("str");
        item.setSpecification("str");
        item.setStock(0L);
        item.setStockTime("str");
        item.setTariffRate((double) 0.0);
        item.setUnit("str");
        item.setUnit1("str");
        item.setUnit2("str");
        item.setUnitPrice((double) 0.0);
        item.setValueAddedTaxRate((double) 0.0);
        item.setVendorName("str");
        item.setWcCode("str");
        item.setWcName("str");
        item.setWebsite("str");
        item.setWrapType("str");
        goodsList.add(item);
        request1.setGoodsList(goodsList);
        request.setRequest(request1);
        PddCustomsSendGoodsRecordResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "response": {
    "error_code": 0,
    "error_msg": "str",
    "result": "str",
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
| 跨境申报权限包 | 跨境企业ERP报关版 |

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
