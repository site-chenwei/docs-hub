---
title: "pdd.waybill.search - 查询面单服务订购及面单使用情况"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.waybill.search"
menu_path:
  - "电子面单API"
  - "pdd.waybill.search"
captured_at: "2026-04-09T15:23:44.865Z"
---

# pdd.waybill.search

## 查询面单服务订购及面单使用情况

更新时间：2020-10-20 21:53:01

¥免费API

必须用户授权

查询面单服务订购及面单使用情况

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
| wp\_code | STRING | 非必填 | 物流公司code |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| pdd\_waybill\_search\_response | OBJECT |  | response |
| waybill\_apply\_subscription\_cols | OBJECT\[\] |  | WP网点信息及对应的商家的发货信息 |
| branch\_account\_cols | OBJECT\[\] |  | wp网点信息及对应的商家的发货信息 |
| allocated\_quantity | LONG |  | 已用面单数量 |
| branch\_code | STRING |  | 网点Code |
| branch\_name | STRING |  | 网点名称 |
| cancel\_quantity | LONG |  | 取消的面单总数 |
| quantity | LONG |  | 电子面单余额数量 |
| recycled\_quantity | LONG |  | 已回收用面单数量 |
| service\_info\_cols | OBJECT\[\] |  | 服务类型列表 |
| required | BOOLEAN |  | 是否必须 |
| service\_attributes | OBJECT\[\] |  | 服务属性类型列表 |
| attribute\_code | STRING |  | 属性code |
| attribute\_name | STRING |  | 属性名称 |
| attribute\_type | STRING |  | 属性类型 |
| type\_desc | STRING |  | 属性描述 |
| service\_code | STRING |  | 服务code |
| service\_desc | STRING |  | 服务描述 |
| service\_name | STRING |  | 服务名称 |
| shipp\_address\_cols | OBJECT\[\] |  | 当前网点下的发货地址 |
| city | STRING |  | 市名称（二级地址） |
| detail | STRING |  | 详细地址 |
| district | STRING |  | 区名称（三级地址） |
| province | STRING |  | 省名称（一级地址） |
| country | STRING |  | 国家/地区 |
| vas\_account\_cols | OBJECT\[\] |  | 增值服务账号 |
| account\_type\_desc | STRING |  | 账户类型描述 |
| quantity | LONG |  | 电子面单余额数量 |
| allocated\_quantity | LONG |  | 已用面单数量 |
| cancel\_quantity | LONG |  | 取消的面单总数 |
| recycled\_quantity | LONG |  | 已回收用面单数量 |
| wp\_code | STRING |  | 快递公司ID |
| wp\_type | INTEGER |  | 物流服务商业务类型 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillSearchRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddWaybillSearchResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddWaybillSearchRequest request = new PddWaybillSearchRequest();
        request.setWpCode("str");
        PddWaybillSearchResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "pdd_waybill_search_response": {
    "waybill_apply_subscription_cols": [
      {
        "branch_account_cols": [
          {
            "allocated_quantity": 0,
            "branch_code": "str",
            "branch_name": "str",
            "cancel_quantity": 0,
            "quantity": 0,
            "recycled_quantity": 0,
            "service_info_cols": [
              {
                "required": false,
                "service_attributes": [
                  {
                    "attribute_code": "str",
                    "attribute_name": "str",
                    "attribute_type": "str",
                    "type_desc": "str"
                  }
                ],
                "service_code": "str",
                "service_desc": "str",
                "service_name": "str"
              }
            ],
            "shipp_address_cols": [
              {
                "city": "str",
                "country": "str",
                "detail": "str",
                "district": "str",
                "province": "str"
              }
            ],
            "vas_account_cols": [
              {
                "account_type_desc": "str",
                "allocated_quantity": 0,
                "cancel_quantity": 0,
                "quantity": 0,
                "recycled_quantity": 0
              }
            ]
          }
        ],
        "wp_code": "str",
        "wp_type": 0
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

接口总限流频次：10000次/1秒

### API工具
