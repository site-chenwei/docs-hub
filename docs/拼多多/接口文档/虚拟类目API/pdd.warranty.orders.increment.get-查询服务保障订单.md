---
title: "pdd.warranty.orders.increment.get - 查询服务保障订单"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.warranty.orders.increment.get"
menu_path:
  - "虚拟类目API"
  - "pdd.warranty.orders.increment.get"
captured_at: "2026-04-09T15:15:02.325Z"
---

# pdd.warranty.orders.increment.get

## 查询服务保障订单

更新时间：2026-02-02 19:58:47

¥免费API

必须用户授权

延保服务提供商导出订单信息

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
| end\_updated\_at | LONG | 必填 | 最后更新时间结束时间的 UNIX时间戳，指格林威治 时间 1970 年01 月 01 日 00 时 00 分 00 秒(北 京时间 1970 年 01 月 01 日 08 时00 分 00 秒)起至现在的总秒数，闭 区间，返回数据包含 startTime数据 |
| page\_no | INTEGER | 必填 | 页码 从1开始 |
| page\_size | INTEGER | 必填 | 页大小 最小1，最大100 |
| start\_updated\_at | LONG | 必填 | 最后更新时间结束时间的 UNIX时间戳，指格林威治时 间 1970 年01 月 01 日 00 时 00 分 00 秒(北京 时间 1970 年 01 月 01 日 08 时00 分 00 秒)起 至现在的总秒数，开始时间 结束时间不超过0.5小时， 不能查询最近1小时数据， 开区间，返回数据不包含 endTime数据 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| response | OBJECT |  | response |
| error\_code | INTEGER |  | errorCode |
| error\_msg | STRING |  | errorMsg |
| result | OBJECT |  | result |
| trade\_order\_infos | OBJECT\[\] |  | tradeOrderInfos |
| activation\_at | LONG |  | 激活时间 |
| created\_at | LONG |  | createdAt |
| enc\_imei\_list | STRING\[\] |  | 加密imei列表 |
| enc\_sn\_list | STRING\[\] |  | 加密sn列表 |
| goods\_id | LONG |  | goodsId |
| nums | INTEGER |  | 商品数量 |
| order\_sn | STRING |  | 订单号 |
| period\_type | INTEGER |  | 时效类型 1 1年 2 2年 3 3年 4 4年 5 5年 6 6年 8 8年 |
| primary\_brand\_name | STRING |  | 主品品牌 |
| primary\_goods\_name | STRING |  | 主品商品 |
| primary\_receive\_at | LONG |  | primaryReceiveAt |
| primary\_spec | STRING |  | 主品规格 |
| range\_type | INTEGER |  | 价格区间类型 1. 1-50元; 2. 50-100元; 3. 100-200元; 4. 200-300元; 5. 300-500元; 6. 400-600元; 7. 500-800元; 8. 600-800元; 9. 800-1000元; 10. 1000-1500元; 11. 1500-2000元; 12. 2000-2500元; 13. 2500-3000元; 14. 3000-4000元; 15. 4000-5000元; 16. 5000-6000元; 17. 5000-7000元; 18. 6000-7000元; 19. 7000-8000元; 20. 7000-10000元 |
| service\_status | INTEGER |  | 0.未生效 1.生效中 2.已失效 3.已结束 |
| service\_type | INTEGER |  | 服务类型 1 手机碎屏保障 2 手机电池保障 3 手机质保换新 4 数码-智能数码质保换新 ... |
| sku\_id | LONG |  | skuId |
| updated\_at | LONG |  | updatedAt |
| primary\_order\_sn\_enc | STRING |  | 主品订单号（加密） |
| success | BOOLEAN |  | success |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddWarrantyOrdersIncrementGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddWarrantyOrdersIncrementGetResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddWarrantyOrdersIncrementGetRequest.Request;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddWarrantyOrdersIncrementGetRequest request = new PddWarrantyOrdersIncrementGetRequest();

        Request request1 = new Request();
        request1.setEndUpdatedAt(1762325635000L);
        request1.setPageNo(1);
        request1.setPageSize(100);
        request1.setStartUpdatedAt(1762325535000L);
        request.setRequest(request1);
        PddWarrantyOrdersIncrementGetResponse response = client.syncInvoke(request, accessToken);
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
    "result": {
      "trade_order_infos": [
        {
          "activation_at": 0,
          "created_at": 0,
          "enc_imei_list": [
            "str"
          ],
          "enc_sn_list": [
            "str"
          ],
          "goods_id": 0,
          "nums": 0,
          "order_sn": "str",
          "period_type": 0,
          "primary_brand_name": "str",
          "primary_goods_name": "str",
          "primary_order_sn_enc": "str",
          "primary_receive_at": 0,
          "primary_spec": "str",
          "range_type": 0,
          "service_status": 0,
          "service_type": 0,
          "sku_id": 0,
          "updated_at": 0
        }
      ]
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
| 保修服务权限包 |  |

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
