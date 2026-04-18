---
title: "pdd.goods.cat.template.get - 获取商品类目属性(已废弃)"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.cat.template.get"
menu_path:
  - "商品API"
  - "pdd.goods.cat.template.get"
captured_at: "2026-04-09T15:15:21.185Z"
---

# pdd.goods.cat.template.get

## 获取商品类目属性(已废弃)

更新时间：2021-04-13 23:04:54

¥免费API

必须用户授权

商品发布前，需要查询该类目的商品发布需要的属性，获取商品发布需要的模板-属性-属性值。已废弃，建议使用pdd.goods.cat.rule.get代替

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
| cat\_id | LONG | 必填 | 类目id |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| open\_api\_response | OBJECT |  | 属性信息 |
| choose\_all\_qualify\_spec | BOOLEAN |  | 限定规格不支持部分选取，为true时限定规格要么全选要么全不选 |
| id | LONG |  | 模板id |
| input\_max\_spec\_num | LONG |  | 模板允许的最大的自定义规格数量 |
| is\_single\_item | BOOLEAN |  | is\_single\_item |
| max\_sku\_num | LONG |  | 最大sku数目上限 |
| properties | OBJECT\[\] |  | 属性信息 |
| can\_note | BOOLEAN |  | 是否允许填写备注 |
| choose\_max\_num | INTEGER |  | 最大可勾选数目,为0时代表不限 |
| control\_type | INTEGER |  | 控件类型（0-可输入、1-可勾选、3-可输入又可勾选、5-单项时间选择器-年月日、6-双项时间选择器-年月日、7-单项时间选择器-年月、8-双项时间选择器-年月）9-调色盘、10-尺码选择器、11-输入数值范围、12-输入数值乘积-2维、13-输入数值乘积-3维 |
| feature | INTEGER |  | 属性特性:0普通，1颜色，2尺码 |
| id | LONG |  | 模板属性id |
| input\_max\_num | INTEGER |  | 最大可输入数目,为0时代表不可输入，非销售属性为null |
| is\_condition\_show | BOOLEAN |  | 是否按条件展示 |
| is\_key | BOOLEAN |  | is\_key |
| is\_parent | BOOLEAN |  | 是否父属性 |
| is\_sale | BOOLEAN |  | 是否销售属性 |
| max\_value | STRING |  | 输入最大值：文本类型代表文本最长长度、 数值类型代表数字最大值、时间类型代表时间最大值 |
| min\_value | STRING |  | 输入最小值：文本类型代表文本最小长度、数值类型代表数字最小值、时间类型代表时间最小值 |
| name | STRING |  | 属性名称 |
| name\_alias | STRING |  | 属性别名 |
| parent\_id | LONG |  | 父属性id |
| ref\_pid | LONG |  | 引用属性id |
| required | BOOLEAN |  | 是否必填 |
| required\_rule | STRING |  | 必填规则具体内容，当required=true且required\_rule\_type=1时该字段有效，表示当出现哪些属性/属性值时，该属性需要必填，json格式，两层List结构，外层list代表"或"关系，内层list代表"且"关系，例如：\[\[{\\"ref\_pid\\":123,\\"vid\\":123}\]\] |
| required\_rule\_type | INTEGER |  | required=true时，该字段有效，为“0”时表示当前属性必填，不受其他属性影响，为“1”时表示当前属性是否必填由已填写的其他属性值决定 |
| show\_only\_standard | BOOLEAN |  | show\_only\_standard |
| show\_vids | LONG\[\] |  | 若属性按条件展示,则只有show\_vids中的值被选择时属性才可使用 |
| spec\_id | LONG |  | 销售属性规格id，非销售属性为null |
| values | OBJECT\[\] |  | 属性值列表 |
| extend\_info | STRING |  | 扩展信息，颜色的话色号在这里,ARGB，非销售属性为null |
| group | OBJECT |  | 分组信息，非销售属性为null |
| id | INTEGER |  | 组id |
| name | STRING |  | 组名称 |
| is\_parent | BOOLEAN |  | 是否父属性值 |
| parent\_vids | LONG\[\] |  | 对应的父属性值id |
| spec\_id | LONG |  | 规格id,非销售属性为null |
| value | STRING |  | 属性值 |
| vid | LONG |  | 基础属性值id |
| value\_precision | INTEGER |  | 小数点允许最大精度,为0时代表不允许输入小数 |
| value\_type | INTEGER |  | 属性值类型（0-文本、1-数值、4-绝对时间、5-相对时间） |
| value\_unit | STRING |  | 属性值单位 |
| single\_spec\_value\_num | LONG |  | 单个自定义规格值上限 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsCatTemplateGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsCatTemplateGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsCatTemplateGetRequest request = new PddGoodsCatTemplateGetRequest();
        request.setCatId(0L);
        PddGoodsCatTemplateGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "open_api_response": {
    "choose_all_qualify_spec": false,
    "id": 0,
    "input_max_spec_num": 0,
    "is_single_item": false,
    "max_sku_num": 0,
    "properties": [
      {
        "can_note": false,
        "choose_max_num": 0,
        "control_type": 0,
        "feature": 0,
        "id": 0,
        "input_max_num": 0,
        "is_condition_show": false,
        "is_key": false,
        "is_parent": false,
        "is_sale": false,
        "max_value": "str",
        "min_value": "str",
        "name": "str",
        "name_alias": "str",
        "parent_id": 0,
        "ref_pid": 0,
        "required": false,
        "required_rule": "str",
        "required_rule_type": 0,
        "show_only_standard": false,
        "show_vids": [
          0
        ],
        "spec_id": 0,
        "value_precision": 0,
        "value_type": 0,
        "value_unit": "str",
        "values": [
          {
            "extend_info": "str",
            "group": {
              "id": 0,
              "name": "str"
            },
            "is_parent": false,
            "parent_vids": [
              0
            ],
            "spec_id": 0,
            "value": "str",
            "vid": 0
          }
        ]
      }
    ],
    "single_spec_value_num": 0
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
| 商品类目属性权限包 | 进销存、商品优化分析、虚拟商家后台系统、企业ERP、商家后台系统、电子凭证商家后台系统、跨境企业ERP报关版 |

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

商家限流频次：2000次/10秒

接口总限流频次：2000次/10秒

### API工具
