---
title: "pdd.goods.commit.detail.get - 获取商品提交的商品详情"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.commit.detail.get"
menu_path:
  - "商品API"
  - "pdd.goods.commit.detail.get"
captured_at: "2026-04-09T15:15:30.525Z"
---

# pdd.goods.commit.detail.get

## 获取商品提交的商品详情

更新时间：2025-03-04 20:45:00

¥免费API

必须用户授权

商品编辑或者提交之后，可以通过此接口查询提交后的编辑信息

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
| goods\_commit\_id | LONG | 必填 | 提交申请的序列id |
| goods\_id | LONG | 必填 | 商品id |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_commit\_detail\_response | OBJECT |  | 返回response |
| bad\_fruit\_claim | INTEGER |  | 坏果包赔 |
| buy\_limit | LONG |  | 限购次数 |
| carousel\_gallery\_list | STRING\[\] |  | 商品轮播图列表 |
| carousel\_video | OBJECT\[\] |  | 商品视频 |
| file\_id | LONG |  | 商品视频id |
| video\_url | STRING |  | 商品视频url |
| carousel\_video\_url | INTEGER |  | 轮播视频 |
| cat\_id | LONG |  | 类目id |
| commit\_message | STRING |  | 驳回原因，仅在status=2时返回，其余状态返回空值 |
| cost\_template\_id | LONG |  | 运费模版id |
| country\_id | LONG |  | 地区/国家id |
| customer\_num | LONG |  | 团购人数 |
| customs | STRING |  | 海关名称 |
| deleted | INTEGER |  | 是否删除 |
| delivery\_one\_day | INTEGER |  | 是否当日发货,0 否，1 是 |
| delivery\_type | INTEGER |  | 发货方式。0：无物流发货；1：有物流发货。 |
| detail\_gallery\_list | STRING\[\] |  | 商品详情图 |
| elec\_goods\_attributes | OBJECT |  | 卡券类商品属性 |
| begin\_time | LONG |  | 开始时间（timeType=1时必填表示核销的开始时间）（精确到毫秒） |
| days\_time | INTEGER |  | 天数内有效（timeType=3必填，表示发货后几天内核销） |
| end\_time | LONG |  | 截止时间（timeType=1,2时必填，表示发货后核销的截止时间）（精确到毫秒） |
| time\_type | INTEGER |  | 卡券核销类型（1：起始时间内有效，2：发货后后至截止时间内有效，3：发货后多少天内有效） |
| goods\_commit\_id | LONG |  | 提交申请的序列ID |
| goods\_desc | STRING |  | 商品描述， 字数限制：20-500，例如，新包装，保证产品的口感和新鲜度。单颗独立小包装，双重营养，1斤家庭分享装，更实惠新疆一级骏枣夹核桃仁。 |
| goods\_id | LONG |  | 商品id |
| goods\_name | STRING |  | 商品名称 |
| goods\_property\_list | OBJECT\[\] |  | 商品属性列表 |
| group\_id | INTEGER |  | 属性值分组ID |
| img\_url | STRING |  | 图片url |
| note | STRING |  | 备注 |
| parent\_spec\_id | LONG |  | 父规格ID |
| punit | STRING |  | 属性单位 |
| ref\_pid | LONG |  | 引用属性id |
| spec\_id | LONG |  | 规格ID |
| table\_info | OBJECT |  | 成分表表单信息 |
| table\_value\_list | OBJECT\[\] |  | 表单内容列表 |
| column\_type | INTEGER | 1 | 列类型 1-成分百分比 |
| unit | STRING | % | 表单单位，材质成分表时为% |
| value | STRING | 20.0 | 表单值，材质成分表时为占比百分值 |
| template\_pid | LONG |  | 模板属性Id |
| vid | LONG |  | 基础属性值Id |
| vvalue | STRING |  | 基础属性值 |
| goods\_status | INTEGER |  | 商品状态，枚举：0-编辑中，1-待审核，2-审核通过，3-审核驳回 |
| goods\_trade\_attr | OBJECT |  | 日历商品交易相关信息 |
| advances\_days | INTEGER |  | 提前预定天数 |
| life\_span | INTEGER |  | 卡券有效期，日历日期后多少天可用。默认值为0表示仅限日历日当天使用. |
| goods\_travel\_attr | OBJECT |  | 商品出行信息 |
| need\_tourist | BOOLEAN |  | 是否需要出行人信息 |
| type | INTEGER |  | 1:旅行类,2:住宿类,3:票务类 |
| goods\_type | INTEGER |  | 商品类型：1-国内普通商品，2-一般贸易，3-保税仓BBC直供，4-海外BC直邮 ,5-流量 ,6-话费 ,7-优惠券 ,8-QQ充值 ,9-加油卡，15-商家卡券，18-海外CC行邮 19-平台卡券 |
| image\_url | STRING |  | 商品主图 |
| invoice\_status | INTEGER |  | 是否支持正品发票；0-不支持、1-支持 |
| is\_customs | INTEGER |  | 是否需要上报海关 0:否 1:是 |
| is\_folt | INTEGER |  | 是否支持假一赔十，0-不支持，1-支持 |
| is\_group\_pre\_sale | INTEGER |  | 是否成团预售。0：不是；1:是。 |
| is\_pre\_sale | INTEGER |  | 是否预售,true-预售商品，false-非预售商品 |
| is\_refundable | INTEGER |  | 是否7天无理由退换货，1-支持，0-不支持 |
| is\_sku\_pre\_sale | INTEGER |  | 是否sku预售，0：否，1：是 |
| lack\_of\_weight\_claim | INTEGER |  | 缺重包退 |
| local\_service\_id\_list | INTEGER\[\] |  | 本地服务id |
| mai\_jia\_zi\_ti | STRING |  | 买家自提模版id |
| market\_price | LONG |  | 参考价格，单位为分 |
| order\_limit | LONG |  | 单次限量 |
| origin\_country\_id | INTEGER |  | 原产地id，是指海淘商品的生产地址 |
| out\_source\_goods\_id | STRING |  | 第三方商品Id |
| out\_source\_type | INTEGER |  | 第三方商品来源 |
| outer\_goods\_id | STRING |  | 商家编码（商品维度），同其他接口中的outer\_goods\_id 、out\_goods\_id、out\_goods\_sn、outer\_goods\_sn 都为商家编码（goods维度） |
| oversea\_goods | OBJECT |  | oversea\_goods |
| bonded\_warehouse\_key | STRING |  | 保税仓唯一标识 |
| consumption\_tax\_rate | INTEGER |  | 消费税率 |
| customs\_broker | STRING |  | 清关服务商 |
| hs\_code | STRING |  | 海关编号 |
| value\_added\_tax\_rate | INTEGER |  | 增值税率 |
| oversea\_type | INTEGER |  | oversea\_type |
| pre\_sale\_time | LONG |  | 预售时间 |
| privacy\_delivery | INTEGER |  | 保密发货，0：不支持，1：支持 |
| quan\_guo\_lian\_bao | INTEGER |  | 0：不支持全国联保；1：支持全国联保 |
| second\_hand | INTEGER |  | 是否二手 |
| shang\_men\_an\_zhuang | STRING |  | 上门安装模版id |
| shipment\_limit\_second | LONG |  | 承诺发货时间（ 秒） |
| shop\_group\_id | LONG |  | 门店组id |
| shop\_group\_name | STRING |  | 门店组名称 |
| sku\_list | OBJECT\[\] |  | sku列表 |
| is\_onsale | INTEGER |  | 上下架状态 1：上架 0 ：下架 |
| lengtj | LONG |  | sku送装参数：长度 |
| limit\_quantity | LONG |  | sku购买限制 |
| multi\_price | LONG |  | 商品团购价格 单位分 |
| out\_sku\_sn | STRING |  | 商家编码（sku维度），同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度） |
| out\_source\_sku\_id | STRING |  | 第三方sku Id |
| oversea\_sku | OBJECT |  | oversea\_sku |
| measurement\_code | STRING |  | 计量单位编码，从接口pdd.gooods.sku.measurement.list获取desc |
| specifications | STRING |  | 规格 |
| taxation | INTEGER |  | 税费 |
| price | LONG |  | 商品单买价格 单位分 |
| quantity | LONG |  | 库存 |
| sku\_id | LONG |  | sku编码 |
| sku\_pre\_sale\_time | INTEGER |  | sku预售时间，单位秒 |
| sku\_property\_list | OBJECT\[\] |  | sku属性 |
| punit | STRING |  | 属性单位 |
| ref\_pid | LONG |  | 属性id |
| value | STRING |  | 属性值 |
| vid | LONG |  | 属性值id |
| spec | OBJECT\[\] |  | 商品规格列表 |
| parent\_id | LONG |  | 商品规格对应的ID |
| parent\_name | STRING |  | 商品规格ID对应的规格名称 |
| spec\_id | LONG |  | 生成的自定义规格ID |
| spec\_name | STRING |  | 商家编辑的规格值，如颜色规格下设置白色属性 |
| spec\_note | STRING |  | 规格备注 |
| thumb\_url | STRING |  | sku预览图 |
| weight | LONG |  | 重量，单位为g |
| sku\_type | INTEGER |  | 日历商品库存方式（0：普通型，1：日历型） |
| song\_huo\_an\_zhuang | STRING |  | 送货入户并安装模版id |
| song\_huo\_ru\_hu | STRING |  | 送货入户模版id |
| tiny\_name | STRING |  | 新包装，保证产品的口感和新鲜度。单颗独立小包装，双重营养，1斤家庭分享装，更实惠新疆一级骏枣夹核桃仁。 |
| two\_pieces\_discount | INTEGER |  | 满2件折扣，可选范围0-100, 0表示取消，95表示95折，设置需先查询规则接口获取实际可填范围 |
| warehouse | STRING |  | 保税仓 |
| warm\_tips | STRING |  | 水果类目温馨提示 |
| zhi\_huan\_bu\_xiu | INTEGER |  | 只换不修的天数，目前只支持0和365 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsCommitDetailGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsCommitDetailGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsCommitDetailGetRequest request = new PddGoodsCommitDetailGetRequest();
        request.setGoodsCommitId(30010956120L);
        request.setGoodsId(239971533725L);
        PddGoodsCommitDetailGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_commit_detail_response": {
    "bad_fruit_claim": 0,
    "buy_limit": 0,
    "carousel_gallery_list": [
      "str"
    ],
    "carousel_video": [
      {
        "file_id": 0,
        "video_url": "str"
      }
    ],
    "carousel_video_url": 0,
    "cat_id": 0,
    "commit_message": "str",
    "cost_template_id": 0,
    "country_id": 0,
    "customer_num": 0,
    "customs": "str",
    "deleted": 0,
    "delivery_one_day": 0,
    "delivery_type": 0,
    "detail_gallery_list": [
      "str"
    ],
    "elec_goods_attributes": {
      "begin_time": 0,
      "days_time": 0,
      "end_time": 0,
      "time_type": 0
    },
    "goods_commit_id": 0,
    "goods_desc": "str",
    "goods_id": 0,
    "goods_name": "str",
    "goods_property_list": [
      {
        "group_id": 0,
        "img_url": "str",
        "note": "str",
        "parent_spec_id": 0,
        "punit": "str",
        "ref_pid": 0,
        "spec_id": 0,
        "table_info": {
          "table_value_list": [
            {
              "column_type": 1,
              "unit": "%",
              "value": "20.0"
            }
          ]
        },
        "template_pid": 0,
        "vid": 0,
        "vvalue": "str"
      }
    ],
    "goods_status": 0,
    "goods_trade_attr": {
      "advances_days": 0,
      "life_span": 0
    },
    "goods_travel_attr": {
      "need_tourist": false,
      "type": 0
    },
    "goods_type": 0,
    "image_url": "str",
    "invoice_status": 0,
    "is_customs": 0,
    "is_folt": 0,
    "is_group_pre_sale": 0,
    "is_pre_sale": 0,
    "is_refundable": 0,
    "is_sku_pre_sale": 0,
    "lack_of_weight_claim": 0,
    "local_service_id_list": [
      0
    ],
    "mai_jia_zi_ti": "str",
    "market_price": 0,
    "order_limit": 0,
    "origin_country_id": 0,
    "out_source_goods_id": "str",
    "out_source_type": 0,
    "outer_goods_id": "str",
    "oversea_goods": {
      "bonded_warehouse_key": "str",
      "consumption_tax_rate": 0,
      "customs_broker": "str",
      "hs_code": "str",
      "value_added_tax_rate": 0
    },
    "oversea_type": 0,
    "pre_sale_time": 0,
    "privacy_delivery": 0,
    "quan_guo_lian_bao": 0,
    "second_hand": 0,
    "shang_men_an_zhuang": "str",
    "shipment_limit_second": 0,
    "shop_group_id": 0,
    "shop_group_name": "str",
    "sku_list": [
      {
        "is_onsale": 0,
        "lengtj": 0,
        "limit_quantity": 0,
        "multi_price": 0,
        "out_sku_sn": "str",
        "out_source_sku_id": "str",
        "oversea_sku": {
          "measurement_code": "str",
          "specifications": "str",
          "taxation": 0
        },
        "price": 0,
        "quantity": 0,
        "sku_id": 0,
        "sku_pre_sale_time": 0,
        "sku_property_list": [
          {
            "punit": "str",
            "ref_pid": 0,
            "value": "str",
            "vid": 0
          }
        ],
        "spec": [
          {
            "parent_id": 0,
            "parent_name": "str",
            "spec_id": 0,
            "spec_name": "str",
            "spec_note": "str"
          }
        ],
        "thumb_url": "str",
        "weight": 0
      }
    ],
    "sku_type": 0,
    "song_huo_an_zhuang": "str",
    "song_huo_ru_hu": "str",
    "tiny_name": "str",
    "two_pieces_discount": 0,
    "warehouse": "str",
    "warm_tips": "str",
    "zhi_huan_bu_xiu": 0
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
| 商品查询 | 打单、进销存、商品优化分析、虚拟商家后台系统、企业ERP、商家后台系统、订单处理、电子凭证商家后台系统、跨境企业ERP报关版 |

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

接口总限流频次：7500次/1秒

### API工具
