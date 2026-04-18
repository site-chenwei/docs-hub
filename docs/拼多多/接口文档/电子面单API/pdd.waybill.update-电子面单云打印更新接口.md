---
title: "pdd.waybill.update - 电子面单云打印更新接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.waybill.update"
menu_path:
  - "电子面单API"
  - "pdd.waybill.update"
captured_at: "2026-04-09T15:23:27.996Z"
---

# pdd.waybill.update

## 电子面单云打印更新接口

更新时间：2021-06-10 15:35:33

¥免费API

必须用户授权

电子面单云打印更新接口

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
| param\_waybill\_cloud\_print\_update\_request | OBJECT | 必填 | param\_waybill\_cloud\_print\_update\_request |
| object\_id | STRING | 非必填 | 请求表示id |
| package\_info | OBJECT | 非必填 | 包裹信息 |
| items | OBJECT\[\] | 非必填 | 商品 |
| count | INTEGER | 非必填 | 数量 |
| name | STRING | 非必填 | 名称 |
| volume | INTEGER | 非必填 | 体积 |
| weight | INTEGER | 非必填 | 重量 |
| recipient | OBJECT | 非必填 | 收件信息 |
| address | OBJECT | 非必填 | 地址 |
| city | STRING | 非必填 | 城市 |
| country | STRING | 非必填 | 地区/国家 |
| detail | STRING | 非必填 | 详细地址 |
| district | STRING | 非必填 | 区地址 |
| province | STRING | 非必填 | 省 |
| town | STRING | 非必填 | 街道 |
| mobile | STRING | 非必填 | 手机号码 |
| name | STRING | 非必填 | 姓名 |
| phone | STRING | 非必填 | 固定电话 |
| sender | OBJECT | 非必填 | 发件信息 |
| mobile | STRING | 非必填 | 手机号码 |
| name | STRING | 非必填 | 姓名 |
| phone | STRING | 非必填 | 固定电话 |
| template\_url | STRING | 非必填 | 模板URL |
| waybill\_code | STRING | 必填 | 面单号 |
| wp\_code | STRING | 必填 | 物流公司CODE |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| pdd\_waybill\_update\_response | OBJECT |  | response |
| print\_data | STRING |  | 模板内容 |
| waybill\_code | STRING |  | 面单号 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillUpdateRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddWaybillUpdateResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillUpdateRequest.ParamWaybillCloudPrintUpdateRequest;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillUpdateRequest.ParamWaybillCloudPrintUpdateRequestPackageInfo;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillUpdateRequest.ParamWaybillCloudPrintUpdateRequestPackageInfoItemsItem;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillUpdateRequest.ParamWaybillCloudPrintUpdateRequestRecipient;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillUpdateRequest.ParamWaybillCloudPrintUpdateRequestRecipientAddress;
import com.pdd.pop.sdk.http.api.pop.request.PddWaybillUpdateRequest.ParamWaybillCloudPrintUpdateRequestSender;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddWaybillUpdateRequest request = new PddWaybillUpdateRequest();

        ParamWaybillCloudPrintUpdateRequest paramWaybillCloudPrintUpdateRequest = new ParamWaybillCloudPrintUpdateRequest();
        paramWaybillCloudPrintUpdateRequest.setObjectId("str");

        ParamWaybillCloudPrintUpdateRequestPackageInfo packageInfo = new ParamWaybillCloudPrintUpdateRequestPackageInfo();
        List<ParamWaybillCloudPrintUpdateRequestPackageInfoItemsItem> items = new ArrayList<ParamWaybillCloudPrintUpdateRequestPackageInfoItemsItem>();

        ParamWaybillCloudPrintUpdateRequestPackageInfoItemsItem item = new ParamWaybillCloudPrintUpdateRequestPackageInfoItemsItem();
        item.setCount(0);
        item.setName("str");
        items.add(item);
        packageInfo.setItems(items);
        packageInfo.setVolume(0);
        packageInfo.setWeight(0);
        paramWaybillCloudPrintUpdateRequest.setPackageInfo(packageInfo);

        ParamWaybillCloudPrintUpdateRequestRecipient recipient = new ParamWaybillCloudPrintUpdateRequestRecipient();

        ParamWaybillCloudPrintUpdateRequestRecipientAddress address = new ParamWaybillCloudPrintUpdateRequestRecipientAddress();
        address.setCity("str");
        address.setCountry("str");
        address.setDetail("str");
        address.setDistrict("str");
        address.setProvince("str");
        address.setTown("str");
        recipient.setAddress(address);
        recipient.setMobile("str");
        recipient.setName("str");
        recipient.setPhone("str");
        paramWaybillCloudPrintUpdateRequest.setRecipient(recipient);

        ParamWaybillCloudPrintUpdateRequestSender sender = new ParamWaybillCloudPrintUpdateRequestSender();
        sender.setMobile("str");
        sender.setName("str");
        sender.setPhone("str");
        paramWaybillCloudPrintUpdateRequest.setSender(sender);
        paramWaybillCloudPrintUpdateRequest.setTemplateUrl("str");
        paramWaybillCloudPrintUpdateRequest.setWaybillCode("str");
        paramWaybillCloudPrintUpdateRequest.setWpCode("str");
        request.setParamWaybillCloudPrintUpdateRequest(paramWaybillCloudPrintUpdateRequest);
        PddWaybillUpdateResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "pdd_waybill_update_response": {
    "print_data": "str",
    "waybill_code": "str"
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
| 50001 | 业务服务错误 | isv.invalid-parameter:waybill\_code | 没有该运单号或者运单号不是该授权商家取号的运单号 | 没有该运单号或者运单号不是该授权商家取号的运单号 |
| isv.send-address-can-not-be-updated | 不允许修改发货地 | 不允许修改发货地 |
| isv.service-error | 系统异常 | 系统异常 |
| isv.waybill-already-cancelled | 面单已取消 | 面单已取消 |
| isv.waybill-cancel-fail | 取消面单失败，面单已经被揽收、签收、或回收 | 取消面单失败，面单已经被揽收、签收、或回收 |
| isv.waybill-is-updating | 面单可能正在被其他人修改,请稍后重试 | 面单可能正在被其他人修改,请稍后重试 |
| isv.waybill-not-exist | 通过传入的快递公司编码和面单号，没能查询到面单存在记录 | 通过传入的快递公司编码和面单号，没能查询到面单存在记录 |

### 限流规则

接口总限流频次：2500次/1秒

### API工具
