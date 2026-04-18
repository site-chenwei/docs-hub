---
title: "pdd.order.list.get - 订单列表查询接口（根据成交时间）"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.order.list.get"
menu_path:
  - "订单API"
  - "pdd.order.list.get"
captured_at: "2026-04-09T15:12:54.612Z"
---

# pdd.order.list.get

## 订单列表查询接口（根据成交时间）

更新时间：2026-04-02 14:24:36

¥基础API

必须用户授权

根据成交时间查询订单列表（只能获取到成交时间三个月以内的交易信息） 注：虚拟订单充值手机号信息无法通过此接口获取，请联系虚拟类目运营人员。

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
| end\_confirm\_at | LONG | 必填 | 必填，成交时间结束时间的时间戳，指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 PS：开始时间结束时间间距不超过 24 小时 |
| order\_status | INTEGER | 必填 | 发货状态，1：待发货，2：已发货待签收，3：已签收 5：全部 |
| page | INTEGER | 必填 | 返回页码 默认 1，页码从 1 开始 PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值 |
| page\_size | INTEGER | 必填 | 返回数量，默认 100。最大 100 |
| refund\_status | INTEGER | 必填 | 售后状态 1：无售后或售后关闭，2：售后处理中，3：退款中，4： 退款成功 5：全部 |
| start\_confirm\_at | LONG | 必填 | 必填，成交时间开始时间的时间戳，指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数 |
| trade\_type | INTEGER | 非必填 | 订单类型 0-普通订单 ，1- 定金订单 |
| use\_has\_next | BOOLEAN | 非必填 | 是否启用has\_next的分页方式，如果指定true,则返回的结果中不包含总记录数，但是会新增一个是否存在下一页的的字段，通过此种方式获取增量交易，效率在原有的基础上有80%的提升。 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| order\_list\_get\_response | OBJECT | 1 | 请求response |
| has\_next | BOOLEAN |  | 是否存在下一页 |
| order\_list | OBJECT\[\] | 1 | 订单信息列表 |
| address
加密

 | STRING | 1 | 详细地址 |
| address\_mask | STRING |  | 详细地址（打码） |
| after\_sales\_status | INTEGER | 1 | 售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货 33：同意召回后退款，待商家召回 |
| bonded\_warehouse | STRING |  | 保税仓名称 |
| bought\_from\_vegetable\_info | OBJECT |  | 多多买菜次日达·送货上门信息 |
| not\_sign | INTEGER | 1 | 1-多多买菜次日达·送货上门 平台邀约测品订单 |
| buyer\_memo | STRING | 1 | 买家留言信息 |
| capital\_free\_discount | DOUBLE | 1 | 团长免单金额，单位：元 |
| card\_info\_list | OBJECT\[\] | 1 | 卡号信息列表 |
| card\_no

加密

 | STRING | 1 | 卡号 |
| mask\_password

加密

 | STRING | 1 | 卡密 |
| cat\_id\_1 | LONG | 1 | 商品一级分类 |
| cat\_id\_2 | LONG | 1 | 商品二级分类 |
| cat\_id\_3 | LONG | 1 | 商品三级分类 |
| cat\_id\_4 | LONG | 1 | 商品四级分类 |
| city | STRING | 1 | 城市 |
| city\_id | INTEGER | 1 | 城市编码 |
| confirm\_status | INTEGER | 1 | 成交状态：0：未成交、1：已成交、2：已取消 |
| confirm\_time | STRING | 1 | 成交时间 |
| contact\_mobile

加密

 | STRING |  | 联系人电话。订单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串。 |
| country | STRING | 1 | 国家或地区 |
| country\_id | INTEGER | 1 | 国家或地区编码 |
| created\_time | STRING | 1 | 订单创建时间 |
| delivery\_home\_value | DOUBLE | 1 | 送货入户费用 单位：元 |
| delivery\_install\_value | DOUBLE | 1 | 送货入户并安装费用 单位：元 |
| delivery\_one\_day | INTEGER |  | 是否当日发货，1-是，0-否 |
| discount\_amount | DOUBLE | 1 | 折扣金额，单位：元，折扣金额=平台优惠+商家优惠+团长免单优惠金额 |
| duo\_duo\_pay\_reduction | DOUBLE |  | 多多支付立减金额，单位：元 |
| duoduo\_wholesale | INTEGER | 1 | 是否多多批发，1-是，0-否 |
| express\_memos | OBJECT\[\] |  | 物流备注 |
| scene | INTEGER |  | 备注场景，1-消费者指定不想使用的物流 |
| tag | STRING |  | 备注标签 |
| extended\_warranty\_info | OBJECT |  | 延保服务信息 |
| extended\_warranty\_range | INTEGER | 1 | 延保保障范围，0:整机，1:核心部件 |
| extended\_warranty\_year | INTEGER | 1 | 延保期年限 |
| extra\_delivery\_list | OBJECT\[\] |  | 订单多包裹发货时使用的其他发货快递信息 |
| logistics\_id | INTEGER |  | 快递公司编号 |
| tracking\_number | STRING |  | 快递运单号 |
| free\_sf | INTEGER | 1 | 是否顺丰包邮，1-是 0-否 |
| gift\_delivery\_list | OBJECT\[\] |  | 赠品额外运单列表 |
| logistics\_id | INTEGER |  | 快递ID |
| tracking\_number | STRING |  | 运单号 |
| gift\_list | OBJECT\[\] |  | 赠品列表 |
| goods\_count | INTEGER |  | 赠品数量 |
| goods\_id | LONG |  | 赠品id |
| goods\_img | STRING |  | 赠品图片 |
| goods\_name | STRING |  | 赠品名称 |
| goods\_price | DOUBLE |  | 赠品销售价格 |
| goods\_spec | STRING |  | 赠品规格 |
| order\_sn | STRING |  | 赠品订单号 |
| outer\_goods\_id | STRING |  | 商家外部商品编码 |
| outer\_id | STRING |  | 商家外部sku编码 |
| sku\_id | LONG |  | 赠品规格编码 |
| gift\_order\_status | INTEGER |  | 赠品订单创建状态 0-待创建，1-创建成功，2-未创建/创建失败（注意：建议赠品订单创建状态不为0时再发货，1-创建成功状态主商品需在主单发货，赠品需在主单对应赠品订单发货；2-未创建/创建失败状态请在主订单上携带赠品一同发货） |
| goods\_amount | DOUBLE | 1 | 商品金额，单位：元，商品金额=商品销售价格\*商品数量-订单改价折扣金额 |
| government\_subsidy\_settle\_details | OBJECT\[\] |  | 政府补贴分摊明细 |
| amount | DOUBLE |  | 出资方承担金额（元） |
| funder | INTEGER |  | 出资方 1-政府，2-平台，3-商家 |
| group\_order\_id | LONG |  | 团id |
| group\_role | INTEGER |  | 团身份。0-团员，1-团长 |
| group\_status | INTEGER | 1 | 成团状态：0：拼团中、1：已成团、2：团失败 |
| home\_delivery\_type | INTEGER | 1 | 送货入户并安装服务 0-不支持送货，1-送货入户不安装，2-送货入户并安装 |
| home\_install\_value | DOUBLE | 1 | 上门安装费用 单位：元 |
| identification\_status | INTEGER |  | 识别码校验状态。0-未上传 1-当前上传的识别码正在校验中 2-当前上传的识别码校验失败 3-当前上传的识别码的校验状态支持发货 |
| inner\_transaction\_id

加密

 | STRING | 1 | 支付申报订单号 |
| invoice\_status | INTEGER | 1 | 发票申请,1代表有 0代表无 |
| is\_lucky\_flag | INTEGER | 1 | 是否是抽奖订单，1-非抽奖订单，2-抽奖订单 |
| is\_pre\_sale | INTEGER | 1 | 是否为预售商品 1表示是 0表示否 |
| is\_stock\_out | INTEGER | 1 | 是否缺货 0-无缺货处理 1： 有缺货处理 |
| item\_list | OBJECT\[\] | 1 | 订单商品列表 |
| goods\_count | INTEGER | 1 | 商品数量 |
| goods\_id | STRING | 1 | 商品编码 |
| goods\_img | STRING | 1 | 商品图片 |
| goods\_name | STRING | 1 | 商品名称 |
| goods\_price | DOUBLE | 1 | 商品单件 单价：元 |
| goods\_spec | STRING | 1 | 商品规格 |
| outer\_goods\_id | STRING | 1 | 商品维度外部编码，注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。 |
| outer\_id | STRING | 1 | sku维度商家外部编码，注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。 |
| sku\_id | STRING | 1 | 商品sku编码 |
| last\_ship\_time | STRING | 1 | 订单承诺发货时间 |
| logistics\_id | LONG | 1 | 快递公司在拼多多的代码 |
| mkt\_biz\_type | INTEGER | 1 | 市场业务类型，0-普通订单，1-拼内购订单 |
| only\_support\_replace | INTEGER | 1 | 只换不修，1:是，0:否 |
| open\_address\_id

加密

 | STRING |  | 合单ID |
| open\_address\_id\_2

加密

 | STRING |  | 合单ID2 |
| order\_change\_amount | DOUBLE |  | 订单改价折扣金额，单位元 |
| order\_depot\_info | OBJECT | 1 | 仓库信息 |
| depot\_code | STRING | 1 | 仓库编码 |
| depot\_id | LONG | 1 | 仓库id |
| depot\_name | STRING | 1 | 仓库名称 |
| depot\_type | INTEGER | 1 | 仓库类型，1：自有仓 2：订阅仓 5：共享仓 6：自管仓 |
| ware\_id | LONG | 1 | 货品id |
| ware\_name | STRING | 1 | 货品名称 |
| ware\_sn | STRING | 1 | 货品编码 |
| ware\_sub\_info\_list | OBJECT\[\] | 1 | 子货品列表（组合货品才会有子货品信息） |
| ware\_id | LONG | 1 | 子货品id |
| ware\_name | STRING | 1 | 子货品名称 |
| ware\_quantity | LONG | 1 | 子货品数量 |
| ware\_sn | STRING | 1 | 子货品编码 |
| ware\_type | INTEGER | 1 | 货品类型（0：普通货品:1：组合货品） |
| order\_sn | STRING | 1 | 订单编号 |
| order\_status | INTEGER | 1 | 订单状态 |
| order\_tag\_list | OBJECT\[\] |  | 订单标签列表，no\_trace\_delivery=无痕发货，only\_support\_replace=只换不修，duoduo\_wholesale=多多批发，return\_freight\_payer=退货包运费，free\_sf=顺丰包邮，support\_nationwide\_warranty=全国联保，self\_contained=门店自提，delivery\_one\_day=当日发货，oversea\_tracing=全球购溯源，distributional\_sale=分销订单，open\_in\_festival=不打烊，region\_black\_delay\_shipping=发货时间可延迟，same\_city\_distribution=同城配送，has\_subsidy\_postage=补贴运费红包，has\_sf\_express\_service=顺丰加价，community\_group=小区团购，has\_ship\_additional=加运费发顺丰，ship\_additional\_order=加运费补差价订单，allergy\_refund=过敏包退，professional\_appraisal=专业鉴定，ship\_hold=暂停发货，home\_delivery\_door=商家送货上门，direct\_mail\_activity=直邮活动，local\_depot=本地仓订单，trade\_in\_national\_subsidy=以旧换新·国家补贴，bought\_from\_vegetable=多多买菜次日达·送货上门，delivery\_schedule=分批发货，government\_subsidy\_consumer\_voucher=政府消费券补贴，has\_weipai\_service=物流核验服务（包含顺丰微派服务等由服务商提供的核验服务），support\_upload\_identification=支持单独上传识别码，quality\_check\_order=质检订单，promise\_delivery=商家承诺送达，platform\_promise\_arrive=平台承诺送达，promise\_timeline=发货时效权益，exclusive\_home\_delivery\_plan=消费者尊享上门计划 |
| name | STRING | return\_freight\_payer | 标签名称 |
| value | INTEGER | 1 | 是否有标签：0=无标签，1=有标签 |
| pay\_amount | DOUBLE | 1 | 支付金额，单位：元，支付金额=商品金额-折扣金额+邮费+服务费 |
| pay\_no

加密

 | STRING | 1 | 支付单号 |
| pay\_time | STRING | 1 | 支付时间 |
| pay\_type | STRING | 1 | 支付方式，枚举值：QQ,WEIXIN,ALIPAY,LIANLIANPAY |
| platform\_discount | DOUBLE | 1 | 平台优惠金额，单位：元 |
| postage | DOUBLE | 1 | 邮费，单位：元 |
| pre\_sale\_time | STRING | 1 | 预售时间 |
| promise\_delivery\_time | STRING |  | 承诺送达时间 |
| promotion\_detail\_list | OBJECT\[\] |  | 优惠券信息 |
| discount\_amount | DOUBLE |  | 优惠金额（元） |
| promotion\_type | INTEGER |  | 优惠券类型。30-以旧换新优惠（优惠金额已包含平台优惠金额里） |
| province | STRING | 1 | 省份 |
| province\_id | INTEGER | 1 | 省份编码 |
| receive\_time | STRING | 1 | 确认收货时间 |
| receiver\_address

加密

 | STRING | 1 | 收件人地址，不拼接省市区。订单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串。 |
| receiver\_address\_mask | STRING |  | 收件人地址（打码） |
| receiver\_name

加密

 | STRING | 1 | 收件人姓名。订单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串。 |
| receiver\_name\_mask | STRING |  | 收件人姓名（打码） |
| receiver\_phone

加密

 | STRING | 1 | 收件人电话。订单状态为待发货状态，且订单未在审核中的情况下返回密文数据；其余情况返回空字符串。 |
| receiver\_phone\_mask | STRING |  | 收件人手机号（打码） |
| refund\_status | INTEGER | 1 | 售后状态 |
| related\_order\_list | OBJECT\[\] |  | 关联的订单信息 |
| order\_sn | STRING |  | 订单号 |
| relation\_type | INTEGER |  | 关联类型 3-sku定制用户补差价订单关联的主单，4-赠品单关联的商品主单 |
| remark | STRING | 1 | 订单备注 |
| remark\_tag | INTEGER | 1 | 订单备注标记，1-红色，2-黄色，3-绿色，4-蓝色，5-紫色 |
| remark\_tag\_name | STRING | 红色 | 订单备注标记名称 |
| resend\_delivery\_list | OBJECT\[\] |  | 补寄额外运单列表 |
| logistics\_id | INTEGER |  | 快递ID |
| tracking\_number | STRING |  | 运单号 |
| return\_freight\_payer | INTEGER | 1 | 退货包运费，1:是，0:否 |
| risk\_control\_status | INTEGER |  | 订单审核状态（0-正常订单， 1-审核中订单） |
| self\_contained | INTEGER |  | 是否门店自提，1-是，0-否 |
| seller\_discount | DOUBLE | 1 | 商家优惠金额，单位：元 |
| service\_fee\_detail | OBJECT\[\] |  | 服务费明细列表，sf\_express\_fee=顺丰加价服务，install\_fee=上门安装服务，store\_install\_fee=到店安装服务，take\_to\_store\_install\_fee=携货到店安装，dismantle\_and\_home\_install\_fee=拆旧+上门安装，dismantle\_taken\_and\_home\_install\_fee=拆旧安装取旧服务，charge\_home\_delivery\_door=消费者付费送货上门 |
| service\_fee | DOUBLE |  | 服务费金额，单位：元 |
| service\_name | STRING |  | 服务费类型 |
| ship\_additional\_link\_order | STRING |  | 关联的加运费发顺丰的补差价订单 |
| ship\_additional\_origin\_order | STRING |  | 加运费补差价订单的原单 |
| shipping\_time | STRING | 1 | 发货时间 |
| shipping\_type | INTEGER |  | 创建交易时的物流方式(1-预约配送，2-1小时达，3-消费者预约送达) |
| step\_order\_info | OBJECT | 1 | { "step\_discount\_amount":4, "advanced\_paid\_fee":1, "step\_paid\_fee":1.1, "step\_trade\_status":2 } |
| advanced\_paid\_fee | DOUBLE | 1 | 已付定金 单位：元 |
| step\_discount\_amount | DOUBLE | 1 | 膨胀金额 单位：元 |
| step\_paid\_fee | DOUBLE | 1 | 分阶段已付金额 单位：元 |
| step\_trade\_status | INTEGER | 1 | 定金订单状态：step\_trade\_status 枚举：0-定金未付尾款未付、1-定金已付尾款未付、2-定金已付尾款已付 |
| stock\_out\_handle\_status | INTEGER | 1 | 缺货处理状态 -1:无缺货处理 0: 缺货待处理 1缺货已处理 |
| support\_nationwide\_warranty | INTEGER | 1 | 全国联保，1:是，0:否 |
| town | STRING | 1 | 区，乡镇 |
| town\_id | INTEGER | 1 | 区县编码 |
| tracking\_number | STRING | 1 | 快递单号 |
| trade\_in\_national\_subsidy\_amount | DOUBLE |  | 以旧换新国家补贴金额 或 政府消费券补贴金额，单位：元 （通过订单标签字段可知此金额对应种类） |
| trade\_in\_national\_subsidy\_amount\_type | INTEGER |  | 以旧换新国家补贴金额 或 政府消费券补贴金额 的类型。1-支付优惠；2-商家优惠。支付优惠是指不同的支付渠道对应的补贴优惠。 |
| trade\_type | INTEGER | 1 | 订单类型 0-普通订单 ，1- 定金订单 |
| updated\_at | STRING | 1 | 订单的更新时间 |
| urge\_shipping\_time | STRING |  | 催发货时间 |
| weipai\_initiator | INTEGER | 0 | 物流核验类型 0-平台发起、1-商家发起 |
| yyps\_date | STRING |  | 预约配送日期 |
| yyps\_time | STRING |  | 预约配送时段 |
| total\_count | INTEGER | 1 | 订单总数 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddOrderListGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddOrderListGetResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddOrderListGetRequest request = new PddOrderListGetRequest();
        request.setEndConfirmAt(1L);
        request.setOrderStatus(1);
        request.setPage(1);
        request.setPageSize(1);
        request.setRefundStatus(1);
        request.setStartConfirmAt(1L);
        request.setTradeType(1);
        request.setUseHasNext(true);
        PddOrderListGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "order_list_get_response": {
    "has_next": false,
    "order_list": [
      {
        "address": "1",
        "address_mask": "str",
        "after_sales_status": 1,
        "bonded_warehouse": "str",
        "bought_from_vegetable_info": {
          "not_sign": 1
        },
        "buyer_memo": "1",
        "capital_free_discount": 1.0,
        "card_info_list": [
          {
            "card_no": "1",
            "mask_password": "1"
          }
        ],
        "cat_id_1": 1,
        "cat_id_2": 1,
        "cat_id_3": 1,
        "cat_id_4": 1,
        "city": "1",
        "city_id": 1,
        "confirm_status": 1,
        "confirm_time": "1",
        "consolidate_info": {
          "consolidate_type": 0
        },
        "contact_mobile": "str",
        "country": "1",
        "country_id": 1,
        "created_time": "1",
        "delivery_home_value": 1.0,
        "delivery_install_value": 1.0,
        "delivery_one_day": 0,
        "discount_amount": 1.0,
        "duo_duo_pay_reduction": 0.0,
        "duoduo_wholesale": 1,
        "express_memos": [
          {
            "scene": 0,
            "tag": "str"
          }
        ],
        "extended_warranty_info": {
          "extended_warranty_range": 1,
          "extended_warranty_year": 1
        },
        "extra_delivery_list": [
          {
            "logistics_id": 0,
            "tracking_number": "str"
          }
        ],
        "free_sf": 1,
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
        "goods_amount": 1.0,
        "government_subsidy_settle_details": [
          {
            "amount": 0.0,
            "funder": 0
          }
        ],
        "group_order_id": 0,
        "group_role": 0,
        "group_status": 1,
        "home_delivery_type": 1,
        "home_install_value": 1.0,
        "identification_status": 0,
        "inner_transaction_id": "1",
        "invoice_status": 1,
        "is_lucky_flag": 1,
        "is_pre_sale": 1,
        "is_stock_out": 1,
        "item_list": [
          {
            "goods_count": 1,
            "goods_id": "1",
            "goods_img": "1",
            "goods_name": "1",
            "goods_price": 1.0,
            "goods_spec": "1",
            "outer_goods_id": "1",
            "outer_id": "1",
            "sku_id": "1"
          }
        ],
        "last_ship_time": "1",
        "logistics_id": 1,
        "mkt_biz_type": 1,
        "only_support_replace": 1,
        "open_address_id": "str",
        "open_address_id_2": "str",
        "order_change_amount": 0.0,
        "order_depot_info": {
          "depot_code": "1",
          "depot_id": 1,
          "depot_name": "1",
          "depot_type": 1,
          "ware_id": 1,
          "ware_name": "1",
          "ware_sn": "1",
          "ware_sub_info_list": [
            {
              "ware_id": 1,
              "ware_name": "1",
              "ware_quantity": 1,
              "ware_sn": "1"
            }
          ],
          "ware_type": 1
        },
        "order_sn": "1",
        "order_status": 1,
        "order_tag_list": [
          {
            "name": "return_freight_payer",
            "value": 1
          }
        ],
        "pay_amount": 1.0,
        "pay_no": "1",
        "pay_time": "1",
        "pay_type": "1",
        "platform_discount": 1.0,
        "postage": 1.0,
        "pre_sale_time": "1",
        "promise_delivery_time": "str",
        "promotion_detail_list": [
          {
            "discount_amount": 0.0,
            "promotion_type": 0
          }
        ],
        "province": "1",
        "province_id": 1,
        "receive_time": "1",
        "receiver_address": "1",
        "receiver_address_mask": "str",
        "receiver_name": "1",
        "receiver_name_mask": "str",
        "receiver_phone": "1",
        "receiver_phone_mask": "str",
        "refund_status": 1,
        "related_order_list": [
          {
            "order_sn": "str",
            "relation_type": 0
          }
        ],
        "remark": "1",
        "remark_tag": 1,
        "remark_tag_name": "红色",
        "resend_delivery_list": [
          {
            "logistics_id": 0,
            "tracking_number": "str"
          }
        ],
        "return_freight_payer": 1,
        "risk_control_status": 0,
        "self_contained": 0,
        "seller_discount": 1.0,
        "service_fee_detail": [
          {
            "service_fee": 0.0,
            "service_name": "str"
          }
        ],
        "ship_additional_link_order": "str",
        "ship_additional_origin_order": "str",
        "shipping_time": "1",
        "shipping_type": 0,
        "step_order_info": {
          "advanced_paid_fee": 1.0,
          "step_discount_amount": 1.0,
          "step_paid_fee": 1.0,
          "step_trade_status": 1
        },
        "stock_out_handle_status": 1,
        "support_nationwide_warranty": 1,
        "town": "1",
        "town_id": 1,
        "tracking_number": "1",
        "trade_in_national_subsidy_amount": 0.0,
        "trade_in_national_subsidy_amount_type": 0,
        "trade_type": 1,
        "updated_at": "1",
        "urge_shipping_time": "str",
        "weipai_initiator": 0,
        "yyps_date": "str",
        "yyps_time": "str"
      }
    ],
    "total_count": 1
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

商家限流频次：10000次/60秒

接口总限流频次：17500次/10秒

### API工具
