---
title: "pdd.einvoice.info.query - 自动开票发票查询"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.einvoice.info.query"
menu_path:
  - "发票服务API"
  - "pdd.einvoice.info.query"
captured_at: "2026-04-09T15:21:19.290Z"
---

# pdd.einvoice.info.query

## 自动开票发票查询

更新时间：2021-07-11 14:05:15

¥免费API

必须用户授权

商家使用自动开票系统对订单进行开票，可通过此接口获取30天内已开发票对应的发票和订单信息

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
| end\_time | LONG | 必填 | 最后更新时间结束时间的时间戳，指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数。开始时间结束时间间距不超过1小时。不能查询最近5分钟内的数据。开区间，返回数据不包含end\_time |
| invoice\_type | INTEGER | 非必填 | 发票类型 0-蓝票，1-红票，不传为全部 |
| page | INTEGER | 必填 | 页码。页码从 1开始 |
| page\_size | INTEGER | 必填 | 返回数量。最小1，最大 50 |
| start\_time | LONG | 必填 | 最后更新时间开始时间的时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数。只能查询30天内的数据。闭区间，返回数据包含start\_time |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| einvoice\_info\_query\_response | OBJECT |  |  |
| invoice\_info\_list | OBJECT\[\] |  |  |
| buyer\_address | STRING |  | 购方地址 |
| buyer\_bank\_account | STRING |  | 购方银行账号 |
| buyer\_bank\_name | STRING |  | 购方银行名称 |
| buyer\_name | STRING |  | 购方名称(发票抬头) |
| buyer\_phone\_number | STRING |  | 购方电话 |
| buyer\_tax\_no | STRING |  | 购方税号 |
| checker | STRING |  | 复核人 |
| create\_time | LONG |  | 开票时间（毫秒，如：1594023438064），以服务商回传成功时间为准 |
| drawer | STRING |  | 开票人 |
| invoice\_code | STRING |  | 发票代码 |
| invoice\_item\_list | OBJECT\[\] |  |  |
| amount | LONG |  | 价税合计(放大100倍,单位分) |
| catalog\_code | STRING |  | 税收分类编码 |
| goods\_name | STRING |  | 商品名称 |
| no\_tax\_amount | LONG |  | 不含税金额(放大100倍，单位分) |
| price | LONG |  | 含税单价（放大1000000倍） |
| quantity | LONG |  | 数量（放大1000000倍） |
| specification | STRING |  | 规格型号 |
| tax\_rate | STRING |  | 税率 |
| total\_tax | LONG |  | 总税额(放大100倍，单位分) |
| unit | STRING |  | 单位 |
| zero\_tax\_rate\_flag | INTEGER |  | 零税率标识，1：免税，2：不征税，3：普通零税率 |
| invoice\_no | STRING |  | 发票号码 |
| invoice\_time | LONG |  | 发票开票日期（毫秒，如：1594023438064) |
| invoice\_type | INTEGER |  | 发票类型 0-蓝票，1-红票 |
| order\_sn | STRING |  | pdd订单号 |
| original\_invoice\_code | STRING |  | 原蓝票代码（红票时返回） |
| original\_invoice\_no | STRING |  | 原蓝票号码（红票时返回） |
| payee | STRING |  | 收款人 |
| pdf\_path | STRING |  | 发票下载地址，30分钟内有效 |
| remark | STRING |  | 发票备注信息 |
| seller\_address | STRING |  | 销方地址 |
| seller\_bank\_account | STRING |  | 销方银行账号 |
| seller\_bank\_name | STRING |  | 销方银行名称 |
| seller\_name | STRING |  | 销方名称 |
| seller\_phone\_number | STRING |  | 销方电话 |
| seller\_tax\_no | STRING |  | 销方税号 |
| total\_amount | LONG |  | 价税合计金额(放大100倍，单位分) |
| total\_price | LONG |  | 合计金额（不含税，放大100倍，单位分） |
| total\_tax\_amount | LONG |  | 合计税额(放大100倍，单位分) |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddEinvoiceInfoQueryRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddEinvoiceInfoQueryResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddEinvoiceInfoQueryRequest request = new PddEinvoiceInfoQueryRequest();
        request.setEndTime(0L);
        request.setInvoiceType(0);
        request.setPage(0);
        request.setPageSize(0);
        request.setStartTime(0L);
        PddEinvoiceInfoQueryResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "einvoice_info_query_response": {
    "invoice_info_list": [
      {
        "buyer_address": "str",
        "buyer_bank_account": "str",
        "buyer_bank_name": "str",
        "buyer_name": "str",
        "buyer_phone_number": "str",
        "buyer_tax_no": "str",
        "checker": "str",
        "create_time": 0,
        "drawer": "str",
        "invoice_code": "str",
        "invoice_item_list": [
          {
            "amount": 0,
            "catalog_code": "str",
            "goods_name": "str",
            "no_tax_amount": 0,
            "price": 0,
            "quantity": 0,
            "specification": "str",
            "tax_rate": "str",
            "total_tax": 0,
            "unit": "str",
            "zero_tax_rate_flag": 0
          }
        ],
        "invoice_no": "str",
        "invoice_time": 0,
        "invoice_type": 0,
        "order_sn": "str",
        "original_invoice_code": "str",
        "original_invoice_no": "str",
        "payee": "str",
        "pdf_path": "str",
        "remark": "str",
        "seller_address": "str",
        "seller_bank_account": "str",
        "seller_bank_name": "str",
        "seller_name": "str",
        "seller_phone_number": "str",
        "seller_tax_no": "str",
        "total_amount": 0,
        "total_price": 0,
        "total_tax_amount": 0
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
| 电子发票权限包 | 虚拟商家后台系统、企业ERP、商家后台系统、跨境企业ERP报关版 |

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

接口总限流频次：100次/1秒

### API工具
