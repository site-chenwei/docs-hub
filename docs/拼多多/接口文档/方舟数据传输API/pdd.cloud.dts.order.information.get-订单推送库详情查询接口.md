---
title: "pdd.cloud.dts.order.information.get - 订单推送库详情查询接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.cloud.dts.order.information.get"
menu_path:
  - "pdd.cloud.dts.order.information.get"
captured_at: "2026-04-15T03:32:40.224Z"
---

# pdd.cloud.dts.order.information.get

## 订单推送库详情查询接口

更新时间：2025-11-11 17:52:55

¥免费API

不需用户授权

方舟

订单推送库详情查询接口

### 公共参数

#### 请求地址（目前只提供正式环境，暂无沙箱环境）

环境

HTTPS地址

正式环境

https://ark-api.pinduoduo.com/ark/router

#### 公共请求参数

参数名称

参数类型

是否必填

参数描述

type

String

必填

API接口名称

client\_id

String

必填

POP分配给应用的client\_id

access\_token

String

非必填

通过code获取的access\_token

timestamp

String

必填

UNIX时间戳，单位秒，需要与拼多多服务器时间差值在10分钟内

data\_type

String

非必填

响应格式，即返回数据的格式，JSON或者XML（二选一），默认JSON，注意是大写

version

String

非必填

API协议版本号，默认为V1，可不填

sign

String

必填

API输入参数签名结果，签名算法参考开放平台接入指南第三部分底部。

target\_client\_id

String

必填

目标应用client\_id

### 请求参数说明

参数接口

参数类型

是否必填

说明

ext\_id

LONG

非必填

扩展字段

extend\_props

STRING

非必填

扩展字段

mall\_id

LONG

非必填

店铺ID

order\_sn

STRING

必填

订单号

token

STRING

非必填

token

### 返回参数说明

参数接口

参数类型

例子

说明

order\_info\_get\_response

OBJECT

response

order\_info

OBJECT

订单详情对象

address

加密

STRING

收件详细地址

address\_mask

STRING

详细地址（打码)

after\_sales\_status

INTEGER

售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款， 待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒 绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处 理，退款失败 13：买家逾期，超过有效期 14 : 换货补寄待商家处理 15:换货补寄待用户处理 16:换货补寄成功 17:换货补寄失败 18:换货补寄待用户确认完成

bonded\_warehouse

STRING

保税仓名称

bought\_from\_vegetable\_info

OBJECT

多多买菜次日达·送货上门信息

not\_sign

INTEGER

1-多多买菜次日达·送货上门 平台邀约测品订单

buyer\_memo

STRING

买家留言信息

capital\_free\_discount

DOUBLE

团长免单优惠金额，只在团长免单活动中才会返回优惠金额

card\_info\_list

OBJECT\[\]

卡号信息列表

card\_no

加密

STRING

卡号

mask\_password

加密

STRING

卡密

cat\_id\_1

LONG

商品一级分类

cat\_id\_2

LONG

商品二级分类

cat\_id\_3

LONG

商品三级分类

cat\_id\_4

LONG

商品四级分类

city

STRING

收件地城市

city\_id

INTEGER

城市编码

confirm\_status

INTEGER

成交状态：0：未成交、1：已成交、2：已取消

confirm\_time

STRING

成交时间

consolidate\_info

OBJECT

集运信息

consolidate\_type

INTEGER

集运类型 0-中国香港集运、1-中国新疆中转、2-哈萨克斯坦集运、3-中国西藏中转、5-日本集运、6-中国台湾集运、7-韩国集运、8-新加坡集运、9-马来西亚集运、10-泰国集运、11-越南集运、12-吉尔吉斯斯坦集运、13-乌兹别克斯坦集运、14-中国甘肃中转、15-中国内蒙古中转、16-中国宁夏中转、17-中国青海中转、18-中国澳门集运、19-柬埔寨集运、20-老挝集运、21-塔吉克斯坦集运、22-亚美尼亚集运、23-格鲁吉亚集运、24-蒙古集运、25-加拿大集运

contact\_mobile

加密

STRING

联系人电话。订单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串。

country

STRING

收件地国家

country\_id

INTEGER

国家编码

created\_time

STRING

创建时间

delivery\_home\_value

DOUBLE

送货入户费用 单位：元

delivery\_install\_value

DOUBLE

送货入户并安装 单位：元

delivery\_one\_day

INTEGER

是否当日发货，1-是，0-否

depot\_type

INTEGER

仓库类型，1：自有仓 2：订阅仓 两者都不是则传空

discount\_amount

DOUBLE

折扣金额（元）折扣金额=平台优惠+商家优惠+团长免单优惠金额

duo\_duo\_pay\_reduction

DOUBLE

多多支付立减金额，单位：元

duoduo\_wholesale

INTEGER

是否多多批发，1-是，0-否

extended\_warranty\_info

OBJECT

延保服务信息

extended\_warranty\_range

INTEGER

延保保障范围，0:整机，1:核心部件

extended\_warranty\_year

INTEGER

延保期年限

extra\_delivery\_list

OBJECT\[\]

分包发货额外运单列表

logistics\_id

LONG

快递ID

tracking\_number

STRING

运单号

free\_sf

INTEGER

是否顺丰包邮 1表示是 0表示否

gift\_delivery\_list

OBJECT\[\]

赠品额外运单列表

logistics\_id

LONG

快递ID

tracking\_number

STRING

运单号

gift\_list

OBJECT\[\]

赠品列表

goods\_count

INTEGER

赠品数量

goods\_id

LONG

赠品id

goods\_img

STRING

赠品图片

goods\_name

STRING

赠品名称

goods\_price

DOUBLE

赠品销售价格

goods\_spec

STRING

赠品规格

order\_sn

STRING

赠品订单号

outer\_goods\_id

STRING

商家外部商品编码

outer\_id

STRING

商家外部sku编码

sku\_id

LONG

赠品规格编码

gift\_order\_status

INTEGER

赠品订单创建状态 0-待创建，1-创建成功，2-未创建/创建失败（注意：建议赠品订单创建状态不为0时再发货，1-创建成功状态主商品需在主单发货，赠品需在主单对应赠品订单发货；2-未创建/创建失败状态请在主订单上携带赠品一同发货）

goods\_amount

DOUBLE

商品金额（元）商品金额=商品销售价格\*商品数量-改价金额（接口暂无该字段）

government\_subsidy\_settle\_details

OBJECT\[\]

政府补贴分摊明细

amount

DOUBLE

出资方承担金额（元）

funder

INTEGER

出资方 1-政府，2-平台，3-商家

group\_order\_id

LONG

团id

group\_role

INTEGER

团身份。0-团员，1-团长

group\_status

INTEGER

成团状态：0：拼团中、1：已成团、2：团失败

home\_delivery\_type

INTEGER

送货入户并安装服务 0-不支持送货，1-送货入户不安装，2-送货入户并安装

home\_install\_value

DOUBLE

上门安装费用 单位：元

id\_card\_name

加密

STRING

身份证姓名

id\_card\_num

加密

STRING

身份证号码

identification\_status

INTEGER

识别码校验状态。0-未上传 1-当前上传的识别码正在校验中 2-当前上传的识别码校验失败 3-当前上传的识别码的校验状态支持发货

inner\_transaction\_id

加密

STRING

支付申报订单号

invoice\_status

INTEGER

发票申请,1代表有 0代表无

is\_lucky\_flag

INTEGER

是否抽奖订单，1-非抽奖订单，2-抽奖订单

is\_pre\_sale

INTEGER

是否为预售商品 1表示是 0表示否

is\_stock\_out

INTEGER

是否缺货 0-无缺货处理 1： 有缺货处理

item\_list

OBJECT\[\]

订单中商品sku列表

goods\_count

INTEGER

商品数量

goods\_id

LONG

商品编号

goods\_img

STRING

商品图片

goods\_name

STRING

商品名称

goods\_price

DOUBLE

商品销售价格

goods\_spec

STRING

商品规格，使用（规格值1,规格值2）组合作为sku的表示，中间以英文逗号隔开

outer\_goods\_id

STRING

商家外部编码（商品），注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。

outer\_id

STRING

商家外部编码（sku），注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。

sku\_id

LONG

商品规格编码

last\_ship\_time

STRING

订单承诺发货时间

logistics\_id

LONG

快递公司编号

mkt\_biz\_type

INTEGER

市场业务类型，0-普通订单，1-拼内购订单

only\_support\_replace

INTEGER

只换不修，1:是，0:否

open\_address\_id

STRING

合单ID

open\_address\_id\_2

STRING

合单ID2

order\_change\_amount

DOUBLE

订单改价折扣金额，单位元

order\_depot\_info

OBJECT

仓库信息

depot\_code

STRING

仓库编码

depot\_id

STRING

仓库id

depot\_name

STRING

仓库名称

ware\_id

STRING

货品id

ware\_name

STRING

货品名称

ware\_sn

STRING

货品编码

ware\_sub\_info\_list

OBJECT\[\]

子货品列表（组合货品才会有子货品信息）

ware\_id

LONG

子货品id

ware\_name

STRING

子货品1编码

ware\_quantity

LONG

子货品数量

ware\_sn

STRING

子货品编码

ware\_type

INTEGER

货品类型（0：普通货品，1：组合货品）

order\_sn

STRING

订单编号

order\_status

INTEGER

发货状态，枚举值：1：待发货，2：已发货待签收，3：已签收

order\_tag\_list

OBJECT\[\]

订单标签列表，no\_trace\_delivery=无痕发货，only\_support\_replace=只换不修，duoduo\_wholesale=多多批发，return\_freight\_payer=退货包运费，free\_sf=顺丰包邮，support\_nationwide\_warranty=全国联保，self\_contained=门店自提，delivery\_one\_day=当日发货，oversea\_tracing=全球购溯源，distributional\_sale=分销订单，open\_in\_festival=不打烊，region\_black\_delay\_shipping=发货时间可延迟，same\_city\_distribution=同城配送，has\_subsidy\_postage=补贴运费红包，has\_sf\_express\_service=顺丰加价，community\_group=小区团购，has\_ship\_additional=加运费发顺丰，ship\_additional\_order=加运费补差价订单，conso\_order=集运订单，allergy\_refund=过敏包退，professional\_appraisal=专业鉴定，ship\_hold=暂停发货，home\_delivery\_door=送货上门，direct\_mail\_activity=直邮活动，local\_depot=本地仓订单，trade\_in\_national\_subsidy=以旧换新·国家补贴，bought\_from\_vegetable=多多买菜次日达·送货上门，delivery\_schedule=分批发货，government\_subsidy\_consumer\_voucher=政府消费券补贴，has\_weipai\_service=微派服务，support\_upload\_identification=支持单独上传识别码，quality\_check\_order=质检订单

name

STRING

return\_freight\_payer

标签名称

value

INTEGER

1

是否有标签：0=无标签，1=有标签

pay\_amount

DOUBLE

支付金额（元）支付金额=商品金额-折扣金额+邮费

pay\_no

加密

STRING

支付单号

pay\_time

STRING

支付时间

pay\_type

STRING

支付方式，枚举值：QQ,WEIXIN,ALIPAY,LIANLIANPAY

phone\_number\_chosen\_by\_user

STRING

用户购买手机号

platform\_discount

DOUBLE

平台优惠金额

postage

DOUBLE

邮费

pre\_sale\_time

STRING

预售时间

promise\_delivery\_time

STRING

promotion\_detail\_list

OBJECT\[\]

优惠券信息

discount\_amount

DOUBLE

优惠金额（元）

promotion\_type

INTEGER

优惠券类型。30-以旧换新优惠（优惠金额已包含平台优惠金额里）

province

STRING

收件地省份

province\_id

INTEGER

省份编码

receive\_time

STRING

确认收货时间

receiver\_address

加密

STRING

收件人地址

receiver\_address\_mask

STRING

收件人地址（打码）

receiver\_name

加密

STRING

收件人姓名

receiver\_name\_mask

STRING

收件人姓名（打码）

receiver\_phone

加密

STRING

收件人电话，仅订单状态为待发货状态下返回明文，其他状态下返回脱敏手机号，例如“1387677\*\*\*\*”

receiver\_phone\_mask

STRING

收件人手机号（打码）

refund\_status

INTEGER

退款状态，枚举值：1：无售后或售后关闭，2：售后处理中，3：退款中，4： 退款成功

related\_order\_list

OBJECT\[\]

关联的订单信息

order\_sn

STRING

订单号

relation\_type

INTEGER

关联类型 4-赠品单关联的商品主单

remark

STRING

商家订单备注

remark\_tag

INTEGER

订单备注标记，1-红色，2-黄色，3-绿色，4-蓝色，5-紫色

remark\_tag\_name

STRING

订单备注标记名称

resend\_delivery\_list

OBJECT\[\]

补寄额外运单列表

logistics\_id

LONG

快递ID

tracking\_number

STRING

运单号

return\_freight\_payer

INTEGER

退货包运费，1:是，0:否

risk\_control\_status

INTEGER

订单审核状态（0-正常订单， 1-审核中订单）

self\_contained

INTEGER

是否门店自提，1-是，0-否

seller\_discount

DOUBLE

店铺优惠金额

ship\_additional\_link\_order

STRING

关联的加运费发顺丰的补差价订单

ship\_additional\_origin\_order

STRING

加运费补差价订单的原单

shipping\_time

STRING

发货时间

shipping\_type

INTEGER

创建交易时的物流方式(1-预约配送，2-1小时达，3-消费者预约送达)

step\_order\_info

OBJECT

定金订单信息 ，非定金订单该字段为null

advanced\_paid\_fee

DOUBLE

已付定金 单位：元

step\_discount\_amount

DOUBLE

膨胀金额 （包含券减） 单位：元

step\_paid\_fee

DOUBLE

分阶段已付金额（定金+尾款） 单位：元

step\_trade\_status

INTEGER

定金订单状态：step\_trade\_status 枚举：0-定金未付尾款未付、1-定金已付尾款未付、2-定金已付尾款已付

stock\_out\_handle\_status

INTEGER

缺货处理状态 -1:无缺货处理 0: 缺货待处理 1缺货已处理

store\_info

OBJECT

门店信息

out\_store\_code

STRING

外部门店code

store\_id

LONG

门店id

store\_name

STRING

门店名称

store\_number

STRING

门店自定义编码

support\_nationwide\_warranty

INTEGER

全国联保，1:是，0:否

town

STRING

收件地区县

town\_id

INTEGER

区县编码

tracking\_number

STRING

快递运单号

trade\_in\_national\_subsidy\_amount

DOUBLE

旧换新国家补贴金额，单位：元

trade\_in\_national\_subsidy\_amount\_type

INTEGER

以旧换新国家补贴金额类型。1-支付优惠；2-商家优惠。国补支付优惠是指不同的支付渠道对应的补贴优惠。

trade\_type

INTEGER

订单类型 0-普通订单、1-定金订单

updated\_at

STRING

订单最近一次更新时间

urge\_shipping\_time

STRING

催发货时间

yyps\_date

STRING

预约配送日期

yyps\_time

STRING

预约配送时段

service\_fee\_detail

OBJECT\[\]

service\_fee

DOUBLE

service\_name

STRING

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.ark.request.PddCloudDtsOrderInformationGetRequest;
import com.pdd.pop.sdk.http.api.ark.response.PddCloudDtsOrderInformationGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddCloudDtsOrderInformationGetRequest request = new PddCloudDtsOrderInformationGetRequest();
        request.setExtId(1L);
        request.setExtendProps("{"key":"value"}");
        request.setMallId(1L);
        request.setOrderSn("1234");
        request.setToken("qwwq");
        request.setTargetClientId("your target client id");
        PddCloudDtsOrderInformationGetResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "order_info_get_response": {
    "order_info": {
      "address": "str",
      "address_mask": "str",
      "after_sales_status": 0,
      "bonded_warehouse": "str",
      "bought_from_vegetable_info": {
        "not_sign": 0
      },
      "buyer_memo": "str",
      "capital_free_discount": 0.0,
      "card_info_list": [
        {
          "card_no": "str",
          "mask_password": "str"
        }
      ],
      "cat_id_1": 0,
      "cat_id_2": 0,
      "cat_id_3": 0,
      "cat_id_4": 0,
      "city": "str",
      "city_id": 0,
      "confirm_status": 0,
      "confirm_time": "str",
      "consolidate_info": {
        "consolidate_type": 0
      },
      "contact_mobile": "str",
      "country": "str",
      "country_id": 0,
      "created_time": "str",
      "delivery_home_value": 0.0,
      "delivery_install_value": 0.0,
      "delivery_one_day": 0,
      "depot_type": 0,
      "discount_amount": 0.0,
      "duo_duo_pay_reduction": 0.0,
      "duoduo_wholesale": 0,
      "extended_warranty_info": {
        "extended_warranty_range": 0,
        "extended_warranty_year": 0
      },
      "extra_delivery_list": [
        {
          "logistics_id": 0,
          "tracking_number": "str"
        }
      ],
      "free_sf": 0,
      "gift_delivery_list": [
        {
          "logistics_id": 0,
          "tracking_number": "str"
        }
      ],
      "gift_list": [
        {
          "goods_count": 0,
          "goods_id": 0,
          "goods_img": "str",
          "goods_name": "str",
          "goods_price": 0.0,
          "goods_spec": "str",
          "order_sn": "str",
          "outer_goods_id": "str",
          "outer_id": "str",
          "sku_id": 0
        }
      ],
      "gift_order_status": 0,
      "goods_amount": 0.0,
      "government_subsidy_settle_details": [
        {
          "amount": 0.0,
          "funder": 0
        }
      ],
      "group_order_id": 0,
      "group_role": 0,
      "group_status": 0,
      "home_delivery_type": 0,
      "home_install_value": 0.0,
      "id_card_name": "str",
      "id_card_num": "str",
      "identification_status": 0,
      "inner_transaction_id": "str",
      "invoice_status": 0,
      "is_lucky_flag": 0,
      "is_pre_sale": 0,
      "is_stock_out": 0,
      "item_list": [
        {
          "goods_count": 0,
          "goods_id": 0,
          "goods_img": "str",
          "goods_name": "str",
          "goods_price": 0.0,
          "goods_spec": "str",
          "outer_goods_id": "str",
          "outer_id": "str",
          "sku_id": 0
        }
      ],
      "last_ship_time": "str",
      "logistics_id": 0,
      "mkt_biz_type": 0,
      "only_support_replace": 0,
      "open_address_id": "str",
      "open_address_id_2": "str",
      "order_change_amount": 0.0,
      "order_depot_info": {
        "depot_code": "str",
        "depot_id": "str",
        "depot_name": "str",
        "ware_id": "str",
        "ware_name": "str",
        "ware_sn": "str",
        "ware_sub_info_list": [
          {
            "ware_id": 0,
            "ware_name": "str",
            "ware_quantity": 0,
            "ware_sn": "str"
          }
        ],
        "ware_type": 0
      },
      "order_sn": "str",
      "order_status": 0,
      "order_tag_list": [
        {
          "name": "return_freight_payer",
          "value": 1
        }
      ],
      "pay_amount": 0.0,
      "pay_no": "str",
      "pay_time": "str",
      "pay_type": "str",
      "phone_number_chosen_by_user": "str",
      "platform_discount": 0.0,
      "postage": 0.0,
      "pre_sale_time": "str",
      "promise_delivery_time": "str",
      "promotion_detail_list": [
        {
          "discount_amount": 0.0,
          "promotion_type": 0
        }
      ],
      "province": "str",
      "province_id": 0,
      "receive_time": "str",
      "receiver_address": "str",
      "receiver_address_mask": "str",
      "receiver_name": "str",
      "receiver_name_mask": "str",
      "receiver_phone": "str",
      "receiver_phone_mask": "str",
      "refund_status": 0,
      "related_order_list": [
        {
          "order_sn": "str",
          "relation_type": 0
        }
      ],
      "remark": "str",
      "remark_tag": 0,
      "remark_tag_name": "str",
      "resend_delivery_list": [
        {
          "logistics_id": 0,
          "tracking_number": "str"
        }
      ],
      "return_freight_payer": 0,
      "risk_control_status": 0,
      "self_contained": 0,
      "seller_discount": 0.0,
      "ship_additional_link_order": "str",
      "ship_additional_origin_order": "str",
      "shipping_time": "str",
      "shipping_type": 0,
      "step_order_info": {
        "advanced_paid_fee": 0.0,
        "step_discount_amount": 0.0,
        "step_paid_fee": 0.0,
        "step_trade_status": 0
      },
      "stock_out_handle_status": 0,
      "store_info": {
        "out_store_code": "str",
        "store_id": 0,
        "store_name": "str",
        "store_number": "str"
      },
      "support_nationwide_warranty": 0,
      "town": "str",
      "town_id": 0,
      "tracking_number": "str",
      "trade_in_national_subsidy_amount": 0.0,
      "trade_in_national_subsidy_amount_type": 0,
      "trade_type": 0,
      "updated_at": "str",
      "urge_shipping_time": "str",
      "yyps_date": "str",
      "yyps_time": "str"
    }
  },
  "service_fee_detail": [
    {
      "service_fee": 0.0,
      "service_name": "str"
    }
  ]
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

拥有此接口的权限包

可获得/可申请此权限包的应用类型

暂无数据

### 返回错误码说明

主错误码

主错误描述

子错误码

子错误描述

解决办法

暂无数据

### 限流规则

接口总限流频次：7500次/1秒

### API工具
