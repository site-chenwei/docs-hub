---
title: "pdd.goods.cat.rule.get - 类目商品发布规则查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.cat.rule.get"
menu_path:
  - "商品API"
  - "pdd.goods.cat.rule.get"
captured_at: "2026-04-09T15:15:18.047Z"
---

# pdd.goods.cat.rule.get

## 类目商品发布规则查询接口

更新时间：2025-03-04 20:43:54

¥免费API

必须用户授权

通过叶子类目id获取该类目的发布规则，目前返回标品、商品服务、属性等规则。

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
| goods\_id | LONG | 非必填 | 商品id，编辑的时候需要传被编辑的商品id，发布商品时如果已有商品id也需要传 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| cat\_rule\_get\_response | OBJECT |  | 类目规则 |
| goods\_properties\_rule | OBJECT |  | 商品属性规则 |
| choose\_all\_qualify\_spec | BOOLEAN | true | 多个销售属性是否需要同时传 |
| input\_max\_spec\_num | LONG | 1 | 允许自定义的销售属性数量 |
| properties | OBJECT\[\] |  | 属性信息 |
| can\_note | BOOLEAN | true | 是否允许填写备注，仅当是销售属性时有意义 |
| choose\_max\_num | INTEGER | 1 | 可选择属性值数目，为0时代表不限。包括自定义的属性值和模版中给出的属性值。 |
| input\_max\_num | INTEGER | 0 | 可自定义属性值数目，为0时代表不可自定义。 |
| is\_important | BOOLEAN | true | 是否重要属性。填写重要属性有更多机会获取搜索、活动等场景流量。 |
| is\_sale | BOOLEAN | true | 是否销售属性。销售属性需要在发商品时，商品属性上的属性值与规格中中的spec对应。 |
| is\_sku | BOOLEAN | false | 是否sku属性，sku维度的属性在商品发布时入参在sku对象下 |
| max\_value | STRING | 10 | 最大值。在不同的属性值类型下有不同的含义。 文本类型时，代表文本最大长度； 数值类型时，代表数字最大值； 时间类型且最大值为时间时，代表时间最大值； 时间类型且最大值为数字时，代表距离今天或者本月往后的天数或月数。 |
| min\_value | STRING | 1 | 最小值。在不同的属性值类型下有不同的含义。 文本类型时，代表文本最小长度； 数值类型时，代表数字最小值； 时间类型且最小值为时间时，代表时间最小值； 时间类型且最小值为数字时，代表距离今天或者本月往前的天数或月数。 |
| name | STRING | 品牌 | 属性名称 |
| parent\_spec\_id | LONG | 111111 | 销售属性对应的父规格id。 |
| property\_value\_type | INTEGER | 0 | 属性值类型。在发商品时传自定义的属性值时，有不同的格式。 0=文本; 1=数值，如“100”; 2=数值范围，如“10,20”，表示10到20之间; 3=数值乘积-二维，如“10,10”，表示10\*10; 4=数值乘积-三维，如“10,10,10”，表示10\*10\*10; 5=单项时间选择-年月日，如“2020-05-20”; 6=双项时间选择-年月日，如“2020-05-20,2020-06-20”; 7=单项时间选择-年月，如“2020-05”; 8=双项时间选择-年月，如“2020-05,2020-06”;9=材质成分表，支持补充材质百分比，在table\_info字段。 |
| ref\_pid | LONG | 310 | 属性id |
| required | BOOLEAN | true | 是否必填 |
| required\_rule | STRING |  | 必填规则具体内容，当required=true且required\_rule\_type=1时该字段有效，表示当出现哪些属性/属性值时，该属性需要必填，json格式，两层List结构，外层list代表"或"关系，内层list代表"且"关系，例如：\[\[{\\"ref\_pid\\":123,\\"vid\\":123}\]\] |
| required\_rule\_type | INTEGER | 0 | required=true时，该字段有效，为“0”时表示当前属性必填，不受其他属性影响，为“1”时表示当前属性是否必填由已填写的其他属性值决定 |
| show\_condition | OBJECT\[\] |  | 该属性的父属性。只有parent\_pid下的show\_vids中的值被选择时才可入参该属性。有多组父属性时，为且的关系。 |
| parent\_ref\_pid | LONG | 1111 | 父属性id。 |
| parent\_vids | LONG\[\] |  | 父属性值id。多个值任选其一即可。若为空表示任意值都可以。 |
| value\_precision | INTEGER | 0 | 小数点允许最大精度，为0时代表不允许输入小数。对数值类属性值限制。 |
| value\_unit | STRING\[\] |  | 可选属性值单位，发商品填写自定义数值属性值时，选择其中之一作为单位。 |
| values | OBJECT\[\] |  | 属性值列表 |
| extend\_info | STRING | (255,255,255,1) | 扩展信息，表示颜色的色号。格式为ARGB |
| group | OBJECT |  | 分组信息 |
| id | INTEGER | 1 | 组id |
| name | STRING | 红色系 | 组名称 |
| parent\_vids | LONG\[\] |  | 表示对应父属性值id。当其中父属性值被选中时该子属性值才可选。为空则表示无此限制。 |
| spec\_id | LONG | 1122 | 规格id，发商品时需要和sku上的spec对应。 |
| value | STRING | aaa | 属性值 |
| vid | LONG | 1111 | 基础属性值id |
| goods\_service\_rule | OBJECT |  | 商品服务规则 |
| goods\_service\_rule\_map | MAP |  |  |
| $key | STRING |  | 商品类型 |
| $value | OBJECT |  |  |
| bad\_claim\_rule | INTEGER |  | 坏了包赔规则：0不可选、1可选、2必选 |
| can\_select\_delivery\_type | BOOLEAN |  | 是否可以选择物流方式 |
| delivery\_one\_day\_rule | INTEGER |  | 当日发货规则：0不可选、1可选 |
| folt\_rule | INTEGER |  | 假一赔十规则：0不可选、1可选、2必选 |
| lack\_of\_weight\_claim\_rule | INTEGER |  | 缺重包退规则：0不可选、1可选、2必选 |
| privacy\_delivery\_rule | INTEGER |  | 保密发货：0不可选、1可选 |
| quan\_guo\_lian\_bao\_rule | INTEGER |  | 全国联保规则：0不可选、1可选 |
| refundable\_rule | INTEGER |  | 7天无理由退换货规则：0不可选、1可选、2必选 |
| shipment\_limit\_second\_list | INTEGER\[\] |  | 可选承诺发货时间列表，单位：秒 |
| zhi\_huan\_bu\_xiu\_rule | INTEGER |  | 只换不修规则：0不可选、1可选 |
| goods\_type\_list | INTEGER\[\] |  | 可选的商品类型列表 |
| goods\_sku\_rule | OBJECT |  | sku规则 |
| price\_range\_ratio | DOUBLE |  | 团购价最高差倍率 |
| spec\_num\_limit | INTEGER |  | 同个商品下规格值的加和数量上限 |
| spu\_rule | OBJECT |  | 标品规则 |
| control\_type | INTEGER |  | 标品管控类型。0=不管控；1=管控，表示商品发布时必须命中标品，且发布成功后不可更改关键属性；2=不可换品，表示发布成功后不可更改关键属性。 |
| key\_prop | OBJECT\[\] |  | 关键属性 |
| pname | STRING |  | 关键属性名 |
| ref\_pid | LONG |  | 关键属性id |
| two\_pieces\_discount\_rule | OBJECT |  | 满2件折扣相关规则 |
| if\_must\_two\_pieces\_discount | BOOLEAN |  | 是否必须设置 |
| max\_two\_pieces\_discount | INTEGER |  | 允许的最大折扣 |
| min\_two\_pieces\_discount | INTEGER |  | 允许的最小折扣 |
| recommend\_two\_pieces\_discount | INTEGER |  | 推荐的折扣 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsCatRuleGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsCatRuleGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsCatRuleGetRequest request = new PddGoodsCatRuleGetRequest();
        request.setCatId(123L);
        request.setGoodsId(123123L);
        PddGoodsCatRuleGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "cat_rule_get_response": {
    "goods_properties_rule": {
      "choose_all_qualify_spec": true,
      "input_max_spec_num": 1,
      "properties": [
        {
          "can_note": true,
          "choose_max_num": 1,
          "input_max_num": 0,
          "is_important": true,
          "is_sale": true,
          "is_sku": false,
          "max_value": "10",
          "min_value": "1",
          "name": "品牌",
          "parent_spec_id": 111111,
          "property_value_type": 0,
          "ref_pid": 310,
          "required": true,
          "required_rule": "str",
          "required_rule_type": 0,
          "show_condition": [
            {
              "parent_ref_pid": 1111,
              "parent_vids": [
                1234
              ]
            }
          ],
          "value_precision": 0,
          "value_unit": [
            "kg"
          ],
          "values": [
            {
              "extend_info": "(255,255,255,1)",
              "group": {
                "id": 1,
                "name": "红色系"
              },
              "parent_vids": [
                12345
              ],
              "spec_id": 1122,
              "value": "aaa",
              "vid": 1111
            }
          ]
        }
      ]
    },
    "goods_service_rule": {
      "goods_service_rule_map": {
        "": {
          "bad_claim_rule": 0,
          "can_select_delivery_type": false,
          "delivery_one_day_rule": 0,
          "folt_rule": 0,
          "lack_of_weight_claim_rule": 0,
          "privacy_delivery_rule": 0,
          "quan_guo_lian_bao_rule": 0,
          "refundable_rule": 0,
          "shipment_limit_second_list": [
            0
          ],
          "zhi_huan_bu_xiu_rule": 0
        }
      },
      "goods_type_list": [
        0
      ]
    },
    "goods_sku_rule": {
      "price_range_ratio": 0.0,
      "spec_num_limit": 0
    },
    "spu_rule": {
      "control_type": 0,
      "key_prop": [
        {
          "pname": "str",
          "ref_pid": 0
        }
      ]
    },
    "two_pieces_discount_rule": {
      "if_must_two_pieces_discount": false,
      "max_two_pieces_discount": 0,
      "min_two_pieces_discount": 0,
      "recommend_two_pieces_discount": 0
    }
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
| 商品编辑 | 进销存、商品优化分析、虚拟商家后台系统、企业ERP、商家后台系统、电子凭证商家后台系统、跨境企业ERP报关版 |

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
| 50001 | 业务服务错误 | isv.###-not-exist:20002 | 类目不存在 | 输入正确的类目 |

### 限流规则

接口总限流频次：5000次/1秒

### API工具
