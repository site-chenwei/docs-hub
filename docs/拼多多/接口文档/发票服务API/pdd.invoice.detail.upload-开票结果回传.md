---
title: "pdd.invoice.detail.upload - 开票结果回传"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.invoice.detail.upload"
menu_path:
  - "发票服务API"
  - "pdd.invoice.detail.upload"
captured_at: "2026-04-09T15:21:28.584Z"
---

# pdd.invoice.detail.upload

## 开票结果回传

更新时间：2025-12-17 21:33:53

¥免费API

必须用户授权

第三方ERP在外部开票系统开完发票之后可以调用此接口回传开票结果

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
| application\_id | LONG | 非必填 | 申请流水号 |
| business\_type | INTEGER | 必填 | 抬头类型：0-个人，1-企业 |
| check\_code | STRING | 非必填 | 发票校验码，票面上有则填写，非必填 |
| invoice\_amount | LONG | 非必填 | 开票金额，整数，单位：分 |
| invoice\_category | INTEGER | 非必填 | 发票类型，即发票票面上标题对应的类型，枚举值如下： 1、增值税普通发票 2、增值税专用发票 3、增值税电子普通发票 4、增值税电子专用发票 5、数电普票 6、数电专票 99、其他(以旧换新·国家补贴订单必填) |
| invoice\_code | STRING | 非必填 | 发票代码 |
| invoice\_file\_content | STRING | 非必填 | 发票内容，pdf文件(电票回传)，图片文件(专票回传)，转码base64编码 |
| invoice\_item\_list | OBJECT\[\] | 非必填 | 发票列表(单张发票场景 只需传入1个item，拆票场景 可以传入多个item)； 【传参方式1（优先建议）：invoice\_item\_list字段传值（有值时优先使用），外层的字段（check\_code、invoice\_amount、invoice\_code、invoice\_file\_content、invoice\_no、original\_invoice\_code、original\_invoice\_no、product\_name、quantity、specification、unit）可不用传】； 【传参方式2：invoice\_item\_list字段未传值，系统默认取外层传的字段（check\_code、invoice\_amount、invoice\_code、invoice\_file\_content、invoice\_no、original\_invoice\_code、original\_invoice\_no、product\_name、quantity、specification、unit），其中invoice\_code、invoice\_no、invoice\_amount、invoice\_file\_content这四个字段必须填写】； 【其他要求：以旧换新国家补贴订单 参考公告 https://open.pinduoduo.com/application/document/announcement?id=327 】 |
| check\_code | STRING | 非必填 | 发票校验码，票面上有则填写，非必填 |
| invoice\_amount | LONG | 必填 | 开票金额 单位:分 |
| invoice\_code | STRING | 非必填 | 发票代码 |
| invoice\_file\_content | STRING | 必填 | 发票内容，pdf文件(电票回传)，图片文件(专票回传)，转码base64编码 |
| invoice\_no | STRING | 必填 | 发票号码 |
| original\_invoice\_code | STRING | 非必填 | 原蓝票代码（红票必填） |
| original\_invoice\_no | STRING | 非必填 | 原蓝票号码（红票必填） |
| product\_name | STRING | 非必填 | 项目名称，票面上对应的项目名称（每张票需注意仅能包含一个项目） |
| quantity | STRING | 非必填 | 数量，票面上项目对应的数量（每张票需注意仅能包含一个项目） |
| specification | STRING | 非必填 | 规格型号，票面上对应的规格型号（每张票需注意仅能包含一个项目） |
| unit | STRING | 非必填 | 单位 (比如：件、个、台等) |
| invoice\_kind | INTEGER | 必填 | 发票种类：0-电子发票，1-纸质发票，2-专票；目前只支持0 |
| invoice\_no | STRING | 非必填 | 发票号码 |
| invoice\_time | LONG | 必填 | 开票日期,时间戳（毫秒） |
| invoice\_type | INTEGER | 必填 | 开票类型：0-蓝票，1-红票；目前 只支持0 |
| memo | STRING | 非必填 | 发票备注，需与实际票面上的备注栏中内容保持一致（对于以旧换新·国家补贴订单的入参限制为必填，如旧换新·国家补贴订单实际票面无发票备注则可回传空字符串） |
| order\_sn | STRING | 必填 | 订单号 |
| original\_invoice\_code | STRING | 非必填 | 原蓝票代码（红票必填） |
| original\_invoice\_no | STRING | 非必填 | 原蓝票号码（红票必填） |
| paper\_shipping\_id | INTEGER | 非必填 | 专票回传必填，专票邮寄快递公司编码，见https://open.pinduoduo.com/application/document/api?id=pdd.logistics.companies.get返回的快递公司编码 |
| paper\_tracking\_number | STRING | 非必填 | 专票回传必填，专票邮寄运单号 |
| payee\_operator | STRING | 必填 | 开票人 |
| payer\_account | STRING | 非必填 | （企业抬头）开户账号 |
| payer\_address | STRING | 非必填 | （企业抬头）地址 |
| payer\_bank | STRING | 非必填 | （企业抬头）开户银行 |
| payer\_name | STRING | 必填 | 发票抬头 |
| payer\_phone | STRING | 非必填 | （企业抬头）电话 |
| payer\_register\_no | STRING | 非必填 | 税号，企业必填 |
| product\_name | STRING | 非必填 | 项目名称，票面上对应的项目名称（每张票需注意仅能包含一个项目） |
| quantity | STRING | 非必填 | 数量，票面上项目对应的数量（每张票需注意仅能包含一个项目） |
| seller\_name | STRING | 非必填 | 销方名称(以旧换新·国家补贴订单必填) |
| seller\_register\_no | STRING | 非必填 | 销方税号(以旧换新·国家补贴订单必填) |
| specification | STRING | 非必填 | 规格型号，票面上对应的规格型号（每张票需注意仅能包含一个项目） |
| sum\_price | LONG | 必填 | 不含税金额，整数，单位：分 |
| sum\_tax | INTEGER | 必填 | 总税额，整数，单位：分 |
| tax\_rate | INTEGER | 必填 | 税率,整数 |
| unit | STRING | 非必填 | 单位 (比如：件、个、台等) |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| invoice\_detail\_upload\_response | OBJECT |  | response |
| serial\_no | STRING |  | 发票流水号 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddInvoiceDetailUploadRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddInvoiceDetailUploadResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddInvoiceDetailUploadRequest.InvoiceItemListItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddInvoiceDetailUploadRequest request = new PddInvoiceDetailUploadRequest();
        request.setApplicationId(123456L);
        request.setBusinessType(0);
        request.setCheckCode("str");
        request.setInvoiceAmount(100L);
        request.setInvoiceCategory(5);
        request.setInvoiceCode("str");
        request.setInvoiceFileContent("str");
        List<InvoiceItemListItem> invoiceItemList = new ArrayList<InvoiceItemListItem>();

        InvoiceItemListItem item = new InvoiceItemListItem();
        item.setCheckCode("str");
        item.setInvoiceAmount(0L);
        item.setInvoiceCode("str");
        item.setInvoiceFileContent("str");
        item.setInvoiceNo("str");
        item.setOriginalInvoiceCode("str");
        item.setOriginalInvoiceNo("str");
        item.setProductName("str");
        item.setQuantity("str");
        item.setSpecification("str");
        item.setUnit("str");
        invoiceItemList.add(item);
        request.setInvoiceItemList(invoiceItemList);
        request.setInvoiceKind(0);
        request.setInvoiceNo("str");
        request.setInvoiceTime(1682577397330L);
        request.setInvoiceType(0);
        request.setMemo("str");
        request.setOrderSn("str");
        request.setOriginalInvoiceCode("str");
        request.setOriginalInvoiceNo("str");
        request.setPaperShippingId(132);
        request.setPaperTrackingNumber("str");
        request.setPayeeOperator("str");
        request.setPayerAccount("str");
        request.setPayerAddress("str");
        request.setPayerBank("str");
        request.setPayerName("str");
        request.setPayerPhone("str");
        request.setPayerRegisterNo("str");
        request.setProductName("str");
        request.setQuantity("str");
        request.setSellerName("str");
        request.setSellerRegisterNo("str");
        request.setSpecification("str");
        request.setSumPrice(100L);
        request.setSumTax(100);
        request.setTaxRate(100);
        request.setUnit("str");
        PddInvoiceDetailUploadResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "invoice_detail_upload_response": {
    "serial_no": "str"
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
| 50001 | 业务服务错误 | 2000000 | 错误code对应的errorMsg报错描述 | 按errorMsg提示传入正确参数 |
| 4000000 | 系统错误 | 稍后重试，多次重试不成功联系开发 |

### 限流规则

接口总限流频次：2500次/1秒

### API工具
