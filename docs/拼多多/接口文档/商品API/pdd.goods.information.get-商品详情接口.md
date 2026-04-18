---
title: "pdd.goods.information.get - 商品详情接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.information.get"
menu_path:
  - "商品API"
  - "pdd.goods.information.get"
captured_at: "2026-04-09T15:16:23.789Z"
---

# pdd.goods.information.get

## 商品详情接口

更新时间：2019-06-02 12:06:00

¥基础API

必须用户授权

商品详情（此接口后续不再维护，请使用pdd.goods.detail.get接口）

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
| goods\_id | LONG | 必填 | 商品编码 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_info\_get\_response | OBJECT |  | 商品详情响应对象 |
| goods\_info | OBJECT |  | 商品详情对象 |
| goods\_id | LONG |  | 商品编码 |
| goods\_sn | STRING |  | 商品序列编码 |
| goods\_type | INTEGER |  | 1-国内普通商品，2-进口，3-国外海淘，4-直邮 ,5-流量,6-话费,7,优惠券;8-QQ充值,9-加油卡,18-CC行邮 |
| goods\_category | STRING |  | 商品一级类目 |
| last\_category | STRING |  | 叶子类目 |
| is\_refundable | INTEGER |  | 是否七天无理由售后，0-不支持，1-支持 |
| shipment\_limit\_second | LONG |  | 承诺发货时间 |
| goods\_name | STRING |  | 商品名称 |
| image\_url | STRING |  | 商品图片 url |
| goods\_quantity | INTEGER |  | 商品库存 |
| is\_onsale | INTEGER |  | 商品是否上架，0-下架，1-上架； |
| second\_hand | INTEGER |  | 商品是否全新，0-全新商品，1-二手商品 |
| group\_required\_customer\_num | LONG |  | 成团人数 |
| sku\_list | OBJECT\[\] |  | sku列表对象 |
| spec | STRING |  | 商品规格名称 |
| sku\_id | LONG |  | 商品sku编码 |
| sku\_quantity | LONG |  | 商品sku库存 |
| outer\_id | STRING |  | 商家外部编码（sku），同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。 |
| outer\_goods\_id | STRING |  | 商家外部编码（商品），同其他接口中的outer\_goods\_id 、out\_goods\_id、out\_goods\_sn、outer\_goods\_sn 都为商家编码（goods维度）。 |
| sku\_img | STRING |  | sku预览图 |
| group\_price | STRING |  | 拼团价格（元） |
| single\_price | STRING |  | 单买价格（元） |
| is\_sku\_onsale | INTEGER |  | 商品sku是否上架，0-下架，1-上架 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsInformationGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsInformationGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsInformationGetRequest request = new PddGoodsInformationGetRequest();
        request.setGoodsId(0L);
        PddGoodsInformationGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_info_get_response": {
    "goods_info": {
      "goods_category": "str",
      "goods_id": 0,
      "goods_name": "str",
      "goods_quantity": 0,
      "goods_sn": "str",
      "goods_type": 0,
      "group_required_customer_num": 0,
      "image_url": "str",
      "is_onsale": 0,
      "is_refundable": 0,
      "last_category": "str",
      "second_hand": 0,
      "shipment_limit_second": 0,
      "sku_list": [
        {
          "group_price": "str",
          "is_sku_onsale": 0,
          "outer_goods_id": "str",
          "outer_id": "str",
          "single_price": "str",
          "sku_id": 0,
          "sku_img": "str",
          "sku_quantity": 0,
          "spec": "str"
        }
      ]
    }
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
| 商品查询 | 打单、进销存、商品优化分析、虚拟商家后台系统、企业ERP、商家后台系统、订单处理、电子凭证商家后台系统、跨境企业ERP报关版 |

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

商家限流频次：5000次/60秒

接口总限流频次：2500次/1秒

### API工具
