---
title: "pdd.one.express.cost.template - 按id获取商品运费模版接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.one.express.cost.template"
menu_path:
  - "商品API"
  - "pdd.one.express.cost.template"
captured_at: "2026-04-09T15:17:54.911Z"
---

# pdd.one.express.cost.template

## 按id获取商品运费模版接口

更新时间：2018-12-18 15:53:58

¥免费API

必须用户授权

根据id获取拼多多商家的物流运费模板信息

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
| cost\_template\_id | LONG | 必填 | 运费模板id |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| one\_express\_cost\_template\_response | OBJECT |  | response |
| province\_id | INTEGER |  | 发货地省份ID |
| city\_id | INTEGER |  | 发货地城市ID |
| district\_id | INTEGER |  | 发货地区ID |
| additional\_service\_type | INTEGER |  | 送货入户并安装服务，0-不支持、1-支持送货入户、2-支持送货入户并安装 |
| sf\_free\_type | INTEGER |  | 是否顺丰包邮 |
| cost\_template\_list | OBJECT\[\] |  | 不包邮区域/需要买家付邮费区域 |
| cost\_province\_list | OBJECT\[\] |  | 不包邮的区域 |
| province | STRING |  | 省份 |
| province\_id | INTEGER |  | 不包邮区域的ID |
| first\_standard | LONG |  | 首件 |
| first\_cost | LONG |  | 首件或首重价格，单位为分 |
| add\_standard | LONG |  | 续重或续件 |
| add\_cost | LONG |  | 续件或续重价格，单位为分 |
| is\_have\_free\_min\_count | BOOLEAN |  | 对不包邮地区，true-若要包邮须满足件数包邮，false-不开启满足件数包邮 |
| have\_free\_min\_count | LONG |  | 对不包邮地区，满足指定件数包邮，该值为商家设置的指定件数，若为-1则商家没有开启满足件数包邮 |
| is\_have\_free\_min\_amount | BOOLEAN |  | 对不包邮地区，true-若要包邮须满足指定价格则可以包邮，false-不开启满足指定价格包邮 |
| have\_free\_min\_amount | LONG |  | 对不包邮地区，满足指定价格包邮，该值为商家设置的指定订单金额，若为-1则商家没有开启满足指定价格包邮，注意，单位为分 |
| template\_id | LONG |  | 运费模板id |
| template\_name | STRING |  | 运费模板名称 |
| cost\_type | INTEGER |  | 计费方式，0-按件计费，1-按重量计费 |
| free\_deliver\_house | BOOLEAN |  | 是否送货上门，对于包邮地区：true-商品包邮且送货上门，false-商品包邮但不送货上门 |
| free\_deliver\_house\_area\_list | OBJECT\[\] |  | 送货上门地区列表 |
| town\_id | INTEGER |  | 包邮送货上门的城区ID |
| city\_id | INTEGER |  | 包邮送货上门的城市ID |
| province\_id | INTEGER |  | 包邮送货上门的省份ID |
| province | STRING |  | 包邮送货上门的省份 |
| city | STRING |  | 包邮送货上门的城市 |
| town | STRING |  | 包邮送货上门的城区 |
| free\_province\_list | OBJECT\[\] |  | 包邮省份对象 |
| province\_id | LONG |  | 省份ID |
| province | STRING |  | 省份 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddOneExpressCostTemplateRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddOneExpressCostTemplateResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddOneExpressCostTemplateRequest request = new PddOneExpressCostTemplateRequest();
        request.setCostTemplateId(0L);
        PddOneExpressCostTemplateResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "one_express_cost_template_response": {
    "additional_service_type": 0,
    "city_id": 0,
    "cost_template_list": [
      {
        "add_cost": 0,
        "add_standard": 0,
        "cost_province_list": [
          {
            "province": "str",
            "province_id": 0
          }
        ],
        "first_cost": 0,
        "first_standard": 0,
        "have_free_min_amount": 0,
        "have_free_min_count": 0,
        "is_have_free_min_amount": false,
        "is_have_free_min_count": false
      }
    ],
    "cost_type": 0,
    "district_id": 0,
    "free_deliver_house": false,
    "free_deliver_house_area_list": [
      {
        "city": "str",
        "city_id": 0,
        "province": "str",
        "province_id": 0,
        "town": "str",
        "town_id": 0
      }
    ],
    "free_province_list": [
      {
        "province": "str",
        "province_id": 0
      }
    ],
    "province_id": 0,
    "sf_free_type": 0,
    "template_id": 0,
    "template_name": "str"
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

接口总限流频次：2500次/1秒

### API工具
