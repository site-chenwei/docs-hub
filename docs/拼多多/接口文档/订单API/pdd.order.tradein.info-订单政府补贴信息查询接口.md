---
title: "pdd.order.tradein.info - 订单政府补贴信息查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.order.tradein.info"
menu_path:
  - "订单API"
  - "pdd.order.tradein.info"
captured_at: "2026-04-09T15:13:35.534Z"
---

# pdd.order.tradein.info

## 订单政府补贴信息查询接口

更新时间：2026-03-25 11:32:33

¥免费API

必须用户授权

查询订单参与政府补贴活动的相关信息

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
| order\_sn\_list | STRING\[\] | 必填 | 订单号列表 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| response | OBJECT |  |  |
| error\_code | INTEGER |  |  |
| error\_msg | STRING |  |  |
| result | OBJECT |  |  |
| order\_activity\_info\_map | MAP |  |  |
| $key | STRING |  |  |
| $value | OBJECT |  |  |
| attachment\_upload\_rule\_list | OBJECT\[\] |  | 附件上传规则 |
| attachment\_type | INTEGER |  | 需要上传的附件类型. 可选值含义说明:\[1:签收轨迹图;2:核验图;3:签字面单;4:3C-外包装带SN码照片;5:3C-商品亮屏/激活照片;6:3C-合照：外包装+亮屏/激活;7:电脑-外包装带SN码照片;8:电脑-机身SN照片;9:电脑-合照：外包装+亮屏/激活/机身SN码照片;10:家电-外包装整体照片;12:家电-外包装或商品带SN码/条形码照片;13:家电-快递员与商品合照;15:商品能效图;16:电脑-商品亮屏/激活照片/机身SN码照片;17:家电-商品本体SN码照片;18:商品本体全貌照片;19:智能眼镜-外包装带SN码照片;20:智能眼镜-机身/扫码/连接设备SN照片;21:智能眼镜-外包装+机身/扫码/连接设备SN照片\] |
| max\_upload\_num | INTEGER |  | 单个订单该类型附件最大上传张数 |
| upload\_status | INTEGER |  | 当前上传状态.可选值含义说明:\[1:待上传;2:已上传;\] |
| brand\_name | STRING |  | 品牌名称 |
| cate\_code | STRING |  | 品类编码 |
| energy\_efficiency\_rate | STRING |  | 商品能效等级 |
| is\_one\_store\_multi\_region\_order | BOOLEAN |  | 是否是一店多地订单 |
| need\_bind\_sn\_code | BOOLEAN |  | 是否需要绑定SN码 |
| need\_upload\_sn\_code | BOOLEAN |  | 是否需要上传SN码 |
| pay\_transaction\_id | STRING |  | 支付流水号 |
| report\_audit\_info | OBJECT |  | 核销审计信息（目前仅限内测店铺获取） |
| audit\_error\_reason | STRING |  | 审计异常原因 |
| audit\_status | INTEGER |  | 审计状态，1：已推送审计，2：审计通过，3：审计异常，4：不满足上送条件，5：待上送审计，6：审计上送中 |
| report\_error\_reason | STRING |  | 核销异常原因 |
| report\_status | INTEGER |  | 核销状态，1：核销成功，2：核销异常；3：不满足上送条件，4：待上送核销 |
| sponsor\_city\_name | STRING |  | 补贴政府区信息 |
| sponsor\_district\_name | STRING |  | 补贴政府城市信息 |
| sponsor\_province\_name | STRING |  | 补贴政府省份信息 |
| sub\_mall\_id | LONG |  | 订单分店mallid |
| sub\_mall\_name | STRING |  | 订单分店名 |
| subsidy\_effective | BOOLEAN |  | 补贴是否生效 |
| success | BOOLEAN |  |  |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddOrderTradeinInfoRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddOrderTradeinInfoResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddOrderTradeinInfoRequest request = new PddOrderTradeinInfoRequest();
        List<String> orderSnList = new ArrayList<String>();
        orderSnList.add("str");
        request.setOrderSnList(orderSnList);
        PddOrderTradeinInfoResponse response = client.syncInvoke(request, accessToken);
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
      "order_activity_info_map": {
        "": {
          "attachment_upload_rule_list": [
            {
              "attachment_type": 0,
              "max_upload_num": 0,
              "upload_status": 0
            }
          ],
          "brand_name": "str",
          "cate_code": "str",
          "energy_efficiency_rate": "str",
          "is_one_store_multi_region_order": false,
          "need_bind_sn_code": false,
          "need_upload_sn_code": false,
          "pay_transaction_id": "str",
          "report_audit_info": {
            "audit_error_reason": "str",
            "audit_status": 0,
            "report_error_reason": "str",
            "report_status": 0
          },
          "sponsor_city_name": "str",
          "sponsor_district_name": "str",
          "sponsor_province_name": "str",
          "sub_mall_id": 0,
          "sub_mall_name": "str",
          "subsidy_effective": false
        }
      }
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
| 订单信息查询权限包 | 打单、进销存、虚拟商家后台系统、企业ERP、商家后台系统、订单处理、电子凭证商家后台系统、跨境企业ERP报关版 |

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

应用限流频次：50次/1秒

### API工具
