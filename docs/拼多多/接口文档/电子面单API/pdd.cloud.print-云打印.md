---
title: "pdd.cloud.print - 云打印"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.print"
menu_path:
  - "电子面单API"
  - "pdd.cloud.print"
captured_at: "2026-04-09T15:22:50.135Z"
---

# pdd.cloud.print

## 云打印

更新时间：2023-11-30 16:22:00

¥免费API

必须用户授权

云打印接口

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
| cloud\_print\_request | OBJECT | 必填 | 云打印请求 |
| print\_data\_list | OBJECT\[\] | 必填 | 打印数据列表 |
| custom\_area\_print\_data | OBJECT | 非必填 | 自定区打印数据 |
| data | STRING | 必填 | 打印数据 |
| template\_url | STRING | 必填 | 模板url |
| waybill\_printer\_data | OBJECT | 必填 | 面单打印数据 |
| add\_data | STRING | 非必填 | 追加数据,例如：{\\"sender\\":{\\"address\\":{\\"province\\":\\"辽宁\\",\\"city\\":\\"沈阳市\\",\\"district\\":\\"铁西区\\",\\"detail\\":\\"xxx\\"},\\"name\\":\\"xxx\\",\\"mobile\\":\\"139xxxx032\\"}} |
| data | STRING | 必填 | 打印数据 |
| encrypted | BOOLEAN | 非必填 | 是否加密 |
| signature | STRING | 非必填 | 签名 |
| template\_url | STRING | 必填 | 模板url |
| ver | STRING | 非必填 | 版本 |
| printer\_id | STRING | 必填 | 打印机id |
| printer\_setting | OBJECT | 非必填 | 打印机设置 |
| need\_bottom\_logo | BOOLEAN | 非必填 | 是否打印下联logo |
| need\_middle\_logo | BOOLEAN | 非必填 | 是否打印中联logo |
| need\_top\_logo | BOOLEAN | 非必填 | 是否打印上联logo |
| orientation | STRING | 非必填 | 打印方向 normal-正常 reverse-翻转 |
| share\_code | STRING | 必填 | 共享码 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| cloud\_print\_response | OBJECT |  | 云打印响应 |
| error\_code | INTEGER |  | 错误码 |
| error\_msg | STRING |  | 错误描述 |
| result | OBJECT |  | 结果 |
| print\_result\_list | OBJECT\[\] |  | 云打印结果列表 |
| fail\_reason | STRING |  | 失败原因 |
| print\_sequence | LONG |  | 序号 |
| print\_task\_id | STRING |  | 打印任务Id |
| result | BOOLEAN |  | 是否打印成功 |
| success | BOOLEAN |  | 请求是否成功 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddCloudPrintRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddCloudPrintResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddCloudPrintRequest.CloudPrintRequest;
import com.pdd.pop.sdk.http.api.pop.request.PddCloudPrintRequest.CloudPrintRequestPrintDataListItem;
import com.pdd.pop.sdk.http.api.pop.request.PddCloudPrintRequest.CloudPrintRequestPrintDataListItemCustomAreaPrintData;
import com.pdd.pop.sdk.http.api.pop.request.PddCloudPrintRequest.CloudPrintRequestPrintDataListItemWaybillPrinterData;
import com.pdd.pop.sdk.http.api.pop.request.PddCloudPrintRequest.CloudPrintRequestPrinterSetting;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudPrintRequest request = new PddCloudPrintRequest();

        CloudPrintRequest cloudPrintRequest = new CloudPrintRequest();
        List<CloudPrintRequestPrintDataListItem> printDataList = new ArrayList<CloudPrintRequestPrintDataListItem>();

        CloudPrintRequestPrintDataListItem item = new CloudPrintRequestPrintDataListItem();

        CloudPrintRequestPrintDataListItemCustomAreaPrintData customAreaPrintData = new CloudPrintRequestPrintDataListItemCustomAreaPrintData();
        customAreaPrintData.setData("str");
        customAreaPrintData.setTemplateUrl("str");
        item.setCustomAreaPrintData(customAreaPrintData);

        CloudPrintRequestPrintDataListItemWaybillPrinterData waybillPrinterData = new CloudPrintRequestPrintDataListItemWaybillPrinterData();
        waybillPrinterData.setAddData("str");
        waybillPrinterData.setData("str");
        waybillPrinterData.setEncrypted(false);
        waybillPrinterData.setSignature("str");
        waybillPrinterData.setTemplateUrl("str");
        waybillPrinterData.setVer("str");
        item.setWaybillPrinterData(waybillPrinterData);
        printDataList.add(item);
        cloudPrintRequest.setPrintDataList(printDataList);
        cloudPrintRequest.setPrinterId("str");

        CloudPrintRequestPrinterSetting printerSetting = new CloudPrintRequestPrinterSetting();
        printerSetting.setNeedBottomLogo(false);
        printerSetting.setNeedMiddleLogo(false);
        printerSetting.setNeedTopLogo(false);
        printerSetting.setOrientation("str");
        cloudPrintRequest.setPrinterSetting(printerSetting);
        cloudPrintRequest.setShareCode("str");
        request.setCloudPrintRequest(cloudPrintRequest);
        PddCloudPrintResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "cloud_print_response": {
    "error_code": 0,
    "error_msg": "str",
    "result": {
      "print_result_list": [
        {
          "fail_reason": "str",
          "print_sequence": 0,
          "print_task_id": "str",
          "result": false
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
| 50001 | 业务服务错误 | 1000 | 非法参数 | 非法参数 |
| 1001 | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
| 2002 | 云打印失败，请稍后再试 | 云打印失败，请稍后再试 |
| 2003 | 打印机未绑定，请重新申请绑定 | 打印机未绑定，请重新申请绑定 |
| 2006 | 共享码无效，请重新绑定 | 共享码无效，请重新绑定 |
| 2007 | 打印机不在线，请尝试重启设备 | 打印机不在线，请尝试重启设备 |
| 2008 | 打印机id无效 | 打印机id无效 |
| 2009 | 打印机被锁定，请联系技术人员 | 打印机被锁定，请联系技术人员 |
| 2200 | 追加数据错误 | 追加数据错误，请修改追加数据格式 |
| 2201 | 电子面单打印数据错误 | 电子面单打印数据错误，如果是打印数据是密文，请设置encrypted字段为true |
| 2202 | 电子面单数据解密失败 | 电子面单数据解密失败，请检查密文数据是否正确 |
| 2203 | 打印数据最多N条 | 打印数据最多N条，请减少打印数据条数 |
| 9999 | 系统异常 | 系统异常 |

### 限流规则

接口总限流频次：2500次/1秒

### API工具
