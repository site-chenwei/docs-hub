---
title: "pdd.promotion.merchant.coupon.list.get - 店铺优惠券批次列表接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.promotion.merchant.coupon.list.get"
menu_path:
  - "营销API"
  - "pdd.promotion.merchant.coupon.list.get"
captured_at: "2026-04-09T15:20:44.733Z"
---

# pdd.promotion.merchant.coupon.list.get

## 店铺优惠券批次列表接口

更新时间：2018-11-01 17:14:56

¥免费API

必须用户授权

店铺优惠券批次列表接口

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
| page | INTEGER | 非必填 | 页码，默认1 |
| page\_size | INTEGER | 非必填 | 每页数量，默认100 |
| batch\_start\_time\_from | LONG | 非必填 | 批次开始时间（范围开始） |
| batch\_start\_time\_to | LONG | 非必填 | 批次开始时间（范围结束） |
| batch\_status | INTEGER | 非必填 | 批次状态 1 领取中，2 已领完，3 已结束 |
| sort\_by | INTEGER | 非必填 | 排序 1 创建时间正序，2 创建时间倒序，3 开始时间正序，4 开始时间倒序，5 初始数量正序， 6 初始数量倒序，7 领取数量正序，8 领取数量倒序；默认2 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| merchant\_coupon\_batch\_list\_response | OBJECT |  | 返回店铺优惠券批次列表 |
| total\_size | INTEGER |  | 返回店铺优惠券批次数量 |
| coupon\_batch\_list | OBJECT\[\] |  | 返回店铺优惠券批次对象 |
| id | LONG |  | 批次ID |
| batch\_name | STRING |  | 批次名 |
| batch\_desc | STRING |  | 批次描述 |
| discount\_type | INTEGER |  | 折扣类型，1 代表满减券，2 代表折扣券 |
| discount\_param | LONG |  | 折扣参数，为请求中传入的discount\_amount，表示折扣金额，单位: 分 |
| init\_quantity | LONG |  | 初始数量 |
| remain\_quantity | LONG |  | 剩余数量 |
| used\_quantity | LONG |  | 已使用数量 |
| user\_limit | LONG |  | 用户限领张数，-1 代表不限制 |
| max\_discount\_amount | LONG |  | 最大折扣金额 |
| duration | LONG |  | 券有效时长 |
| period\_type | INTEGER |  | 券有效期时长的单位，0 代表天，2 代表小时 |
| batch\_start\_time | LONG |  | 批次开始时间 |
| batch\_end\_time | LONG |  | 批次结束时间 |
| source\_type | INTEGER |  | 券来源类型，16 店铺直接领券，41 店铺精选评价优惠券，66 商家短信营销优惠券 |
| type | INTEGER |  | 券类型，固定为8，代表商家券 |
| status | INTEGER |  | 批次状态，1 领取中，2 已领完，3 已结束 |
| rules | STRING |  | 用券条件 |
| display\_type | INTEGER |  | 券展示类型，固定为8，代表商家券 |
| created\_at | LONG |  | 批次创建时间 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddPromotionMerchantCouponListGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddPromotionMerchantCouponListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddPromotionMerchantCouponListGetRequest request = new PddPromotionMerchantCouponListGetRequest();
        request.setPage(0);
        request.setPageSize(0);
        request.setBatchStartTimeFrom(0L);
        request.setBatchStartTimeTo(0L);
        request.setBatchStatus(0);
        request.setSortBy(0);
        PddPromotionMerchantCouponListGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "merchant_coupon_batch_list_response": {
    "coupon_batch_list": [
      {
        "batch_desc": "str",
        "batch_end_time": 0,
        "batch_name": "str",
        "batch_start_time": 0,
        "created_at": 0,
        "discount_param": 0,
        "discount_type": 0,
        "display_type": 0,
        "duration": 0,
        "id": 0,
        "init_quantity": 0,
        "max_discount_amount": 0,
        "period_type": 0,
        "remain_quantity": 0,
        "rules": "str",
        "source_type": 0,
        "status": 0,
        "type": 0,
        "used_quantity": 0,
        "user_limit": 0
      }
    ],
    "total_size": 0
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
| 营销卡券权限包 | 商家后台系统 |

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
