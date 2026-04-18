---
title: "pdd.stock.ware.detail.query - 查询货品详情"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.stock.ware.detail.query"
menu_path:
  - "仓储API"
  - "pdd.stock.ware.detail.query"
captured_at: "2026-04-09T15:22:15.575Z"
---

# pdd.stock.ware.detail.query

## 查询货品详情

更新时间：2023-10-25 11:08:39

¥免费API

必须用户授权

家电分仓库存-查看货品详情

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
| ware\_id | LONG | 必填 | 货品id |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| open\_api\_response | OBJECT |  | response |
| color | STRING |  | 颜色 |
| created\_at | LONG |  | 创建时间（毫秒） |
| gross\_weight | INTEGER |  | 毛重：kg，精确到两位小数 |
| height | INTEGER |  | 高：厘米，精确到一位小数 |
| id | LONG |  | 货品id |
| length | INTEGER |  | 长：厘米，精确到一位小数 |
| net\_weight | INTEGER |  | 净重：kg，精确到两位小数 |
| note | STRING |  | 备注 |
| packing | STRING |  | 包材 |
| price | INTEGER |  | 单价：元，精确到一位小数 |
| quantity | LONG |  | 库存 |
| service\_quality | INTEGER |  | 高低值服务，0低，1高 |
| tare\_weight | INTEGER |  | 皮重：kg，精确到两位小数 |
| type | INTEGER |  | 货品类型.0:单独货品 1:组合货品 |
| updated\_at | LONG |  | 更新时间毫秒） |
| volume | INTEGER |  | 体积：立方厘米，精确到一位小数 |
| ware\_infos | OBJECT\[\] |  | 组合货品中子货品的关联关系 |
| ware\_id | LONG |  | 子货品id |
| ware\_name | STRING |  | 子货品名称 |
| ware\_quantity | LONG |  | 子货品数量 |
| ware\_sn | STRING |  | 子货品编码 |
| ware\_name | STRING |  | 货品名称 |
| ware\_skus | OBJECT\[\] |  | 货品sku信息 |
| exist\_ware | BOOLEAN |  | 是否已经绑定货品false/true |
| goods\_id | LONG |  | 商品id |
| is\_onsale | BOOLEAN |  | 上下架状态，true表示上架 |
| sku\_id | LONG |  | skuid |
| specs | OBJECT\[\] |  | 规格信息 |
| spec\_id | LONG |  | 规格id |
| spec\_key | STRING |  | 规格名称 |
| spec\_value | STRING |  | 规格值 |
| ware\_id | LONG |  | 货品id |
| ware\_sn | STRING |  | 货品编码 |
| weight | INTEGER |  | 重量：kg，精确到两位小数 |
| width | INTEGER |  | 宽：厘米，精确到一位小数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddStockWareDetailQueryRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddStockWareDetailQueryResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddStockWareDetailQueryRequest request = new PddStockWareDetailQueryRequest();
        request.setWareId(100L);
        PddStockWareDetailQueryResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "open_api_response": {
    "color": "str",
    "created_at": 0,
    "gross_weight": 0,
    "height": 0,
    "id": 0,
    "length": 0,
    "net_weight": 0,
    "note": "str",
    "packing": "str",
    "price": 0,
    "quantity": 0,
    "service_quality": 0,
    "tare_weight": 0,
    "type": 0,
    "updated_at": 0,
    "volume": 0,
    "ware_infos": [
      {
        "ware_id": 0,
        "ware_name": "str",
        "ware_quantity": 0,
        "ware_sn": "str"
      }
    ],
    "ware_name": "str",
    "ware_skus": [
      {
        "exist_ware": false,
        "goods_id": 0,
        "is_onsale": false,
        "sku_id": 0,
        "specs": [
          {
            "spec_id": 0,
            "spec_key": "str",
            "spec_value": "str"
          }
        ],
        "ware_id": 0
      }
    ],
    "ware_sn": "str",
    "weight": 0,
    "width": 0
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
| 仓储库存查询权限包 | 企业ERP、商家后台系统 |

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
