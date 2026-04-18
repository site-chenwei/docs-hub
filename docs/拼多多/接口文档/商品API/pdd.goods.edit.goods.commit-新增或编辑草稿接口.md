---
title: "pdd.goods.edit.goods.commit - 新增或编辑草稿接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.edit.goods.commit"
menu_path:
  - "商品API"
  - "pdd.goods.edit.goods.commit"
captured_at: "2026-04-09T15:16:04.954Z"
---

# pdd.goods.edit.goods.commit

## 新增或编辑草稿接口

更新时间：2026-02-11 10:25:33

¥免费API

必须用户授权

新增或编辑草稿

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
| auto\_fill\_spu\_property | BOOLEAN | 非必填 | 是否自动补充标品属性 |
| bad\_fruit\_claim | INTEGER | 非必填 | 坏果包赔 |
| buy\_limit | LONG | 非必填 | 限购次数 |
| carousel\_gallery | STRING\[\] | 非必填 | 商品轮播图，按次序上传，图片格式支持JPEG/JPG/PNG， 图片尺寸长宽比1：1且尺寸不低于480px，图片大小最高1MB |
| carousel\_video | OBJECT\[\] | 非必填 | 商品视频 |
| file\_id | LONG | 非必填 | 商品视频id |
| video\_url | STRING | 非必填 | 商品视频url |
| carousel\_video\_url | STRING | 非必填 | 轮播视频 |
| cat\_id | LONG | 必填 | 叶子类目ID |
| cost\_template\_id | LONG | 非必填 | 物流运费模板ID，可使用pdd.logistics.template.get获取 |
| country\_id | INTEGER | 非必填 | 地区/国家ID，0-中国，暂时只传0（普通商品） |
| customer\_num | LONG | 非必填 | 团购人数 |
| customs | STRING | 非必填 | 海关名称，只在goods\_type为直供商品时有效（现阶段暂不支持） |
| delivery\_one\_day | INTEGER | 非必填 | 是否当日发货,0 否，1 是 |
| delivery\_type | INTEGER | 非必填 | 发货方式。0：无物流发货；1：有物流发货。 |
| detail\_gallery | STRING\[\] | 非必填 | 商品详情图： a. 尺寸要求宽度处于480~1200px之间，高度0-1500px之间 b. 大小1M以内 c. 数量限制在20张之间 d. 图片格式仅支持JPG,PNG格式 e. 点击上传时，支持批量上传详情图 |
| elec\_goods\_attributes | OBJECT | 非必填 | 卡券类商品属性 |
| begin\_time | LONG | 非必填 | 开始时间（timeType=1时必填表示核销的开始时间）（精确到毫秒） |
| days\_time | INTEGER | 非必填 | 天数内有效（timeType=3必填，表示发货后几天内核销） |
| end\_time | LONG | 非必填 | 截止时间（timeType=1,2时必填，表示发货后核销的截止时间）（精确到毫秒 |
| time\_type | INTEGER | 非必填 | 卡券核销类型（1：起始时间内有效，2：发货后后至截止时间内有效，3：发货后多少天内有效） |
| goods\_desc | STRING | 非必填 | 商品描述， 字数限制：20-500，例如，新包装，保证产品的口感和新鲜度。单颗独立小包装，双重营养，1斤家庭分享装，更实惠新疆一级骏枣夹核桃仁。 |
| goods\_name | STRING | 非必填 | 商品标题，例如，新疆特产 红满疆枣夹核桃500g |
| goods\_properties | OBJECT\[\] | 非必填 | 商品属性列表 |
| group\_id | INTEGER | 非必填 | 组id，非销售属性不用传 |
| img\_url | STRING | 非必填 | 图片url，非销售属性不用传 |
| note | STRING | 非必填 | 备注，非销售属性不用传 |
| parent\_spec\_id | LONG | 非必填 | 父属性id，非销售属性不用传 |
| ref\_pid | LONG | 非必填 | 引用属性ID |
| spec\_id | LONG | 非必填 | 属性id，非销售属性不用传 |
| table\_info | OBJECT | 非必填 | 成分表表单信息 |
| table\_value\_list | OBJECT\[\] | 非必填 | 表单内容列表 |
| column\_type | INTEGER | 非必填 | 列类型 1-材质成分百分比 |
| unit | STRING | 非必填 | 表单单位，材质成分表时为：% |
| value | STRING | 非必填 | 表单值，材质成分表时为：占比百分值 |
| template\_pid | LONG | 非必填 | 模板属性id |
| value | STRING | 非必填 | 属性值 |
| value\_unit | STRING | 非必填 | 属性单位 |
| vid | LONG | 非必填 | 属性值id |
| goods\_trade\_attr | OBJECT | 非必填 | 日历商品交易相关信息 |
| advances\_days | INTEGER | 非必填 | 提前预定天数，默认为0表示当天可预定 |
| booking\_notes | OBJECT | 非必填 | 预订须知 |
| url | STRING | 非必填 | 预定须知图片地址 |
| life\_span | INTEGER | 非必填 | 卡券有效期，日历日期后多少天可用。默认值为0表示仅限日历日当天使用 |
| goods\_travel\_attr | OBJECT | 非必填 | 商品出行信息 |
| need\_tourist | BOOLEAN | 非必填 | 出行人是否必填（默认是） |
| type | INTEGER | 非必填 | 日历商品类型1:旅行类,2:住宿类,3:票务类 |
| goods\_type | INTEGER | 非必填 | 1-国内普通商品，2-一般贸易，3-保税仓BBC直供，4-海外BC直邮 ,5-流量 ,6-话费 ,7-优惠券 ,8-QQ充值 ,9-加油卡，15-商家卡券，18-海外CC行邮 19-平台卡券 |
| image\_url | STRING | 非必填 | 商品主图，请参考拼多多首页大图，如果商品参加部分活动则必填，否则无法参加活动 a. 尺寸750 x 352px b. 大小100k以内 c. 图片格式仅支持JPG,PNG格式 d. 图片背景应以纯白为主, 商品图案居中显示 e. 图片不可以添加任何品牌相关文字或logo |
| invoice\_status | INTEGER | 非必填 | 是否支持正品发票；0-不支持、1-支持 |
| is\_customs | BOOLEAN | 非必填 | 是否需要上报海关，现阶段入参默认false，入参true会失败 |
| is\_folt | BOOLEAN | 非必填 | 是否支持假一赔十，false-不支持，true-支持 |
| is\_group\_pre\_sale | INTEGER | 非必填 | 是否成团预售。0：不是；1:是。 |
| is\_pre\_sale | BOOLEAN | 非必填 | 是否预售,true-预售商品，false-非预售商品 |
| is\_refundable | BOOLEAN | 非必填 | 是否7天无理由退换货，true-支持，false-不支持 |
| is\_sku\_pre\_sale | INTEGER | 非必填 | 是否sku预售，1：是，0：否 |
| lack\_of\_weight\_claim | INTEGER | 非必填 | 缺重包退 |
| local\_service\_id\_list | INTEGER\[\] | 非必填 | 本地服务id |
| mai\_jia\_zi\_ti | STRING | 非必填 | 买家自提模版id |
| market\_price | LONG | 非必填 | 参考价格，单位为分 |
| order\_limit | LONG | 非必填 | 单次限量 |
| origin\_country\_id | INTEGER | 非必填 | 原产地id，是指海淘商品的生产地址，仅在goods type=3/4的时候必填，可以通过pdd.goods.country.get获取 |
| out\_goods\_id | STRING | 非必填 | 商品goods外部编码 |
| out\_source\_goods\_id | STRING | 非必填 | 第三方商品Id |
| out\_source\_type | INTEGER | 非必填 | 第三方商品来源 |
| oversea\_goods | OBJECT | 非必填 | { "consumption\_tax\_rate": 1, "value\_added\_tax\_rate": 9, "hs\_code": "2200", "customs\_broker": "sss", "customs\_declaration\_method": 1, "bonded\_warehouse": "sss", "bonded\_warehouse\_key": "pp" } |
| bonded\_warehouse\_key | STRING | 必填 | 保税仓唯一标识 |
| consumption\_tax\_rate | INTEGER | 非必填 | 消费税率 |
| customs\_broker | STRING | 非必填 | 清关服务商 |
| hs\_code | STRING | 非必填 | 海关编号 |
| value\_added\_tax\_rate | INTEGER | 非必填 | 增值税率 |
| oversea\_type | INTEGER | 非必填 | oversea\_type |
| pre\_sale\_time | LONG | 非必填 | 预售时间，is\_pre\_sale为1时必传，UNIX时间戳 |
| privacy\_delivery | INTEGER | 非必填 | 保密发货，0:不支持，1:支持 |
| quan\_guo\_lian\_bao | INTEGER | 非必填 | 0：不支持全国联保；1：支持全国联保 |
| second\_hand | BOOLEAN | 非必填 | 是否二手商品，true -二手商品 ，false-全新商品 |
| shang\_men\_an\_zhuang | STRING | 非必填 | 上门安装模版id |
| shipment\_limit\_second | LONG | 非必填 | 承诺发货时间（ 秒），48小时或24小时，is\_pre\_sale为1时不必传 |
| shop\_group\_id | LONG | 非必填 | 门店组id |
| size\_spec\_id | LONG | 非必填 | 尺码表id |
| sku\_list | OBJECT\[\] | 非必填 | sku对象列表,实例：\[{ "is\_onsale": 1, "limit\_quantity": 999, "price": "2200", "weight": 1000, "multi\_price": "1900", "thumb\_url": "http://t06img.yangkeduo.com/images/2018-04-15/ced035033b5d40b589140af882621c03.jpg", "out\_sku\_sn": "L", "quantity": 100, "spec\_id\_list": "\[25\]", "oversea\_sku": { "measurement\_code": "计量单位编码", "taxation": "税费", "specifications": "规格" } }\] |
| is\_onsale | INTEGER | 必填 | sku上架状态，0-已下架，1-上架中 |
| length | LONG | 非必填 | sku送装参数：长度 |
| limit\_quantity | LONG | 必填 | sku购买限制，只入参999 |
| multi\_price | LONG | 必填 | 商品团购价格 |
| out\_sku\_sn | STRING | 非必填 | 商品sku外部编码 |
| out\_source\_sku\_id | STRING | 非必填 | 第三方sku Id |
| oversea\_sku | OBJECT | 非必填 | oversea\_sku |
| measurement\_code | STRING | 必填 | 计量单位编码，从接口pdd.gooods.sku.measurement.list获取code |
| specifications | STRING | 必填 | 规格 |
| taxation | INTEGER | 必填 | 税费 |
| price | LONG | 必填 | 商品单买价格 |
| quantity | LONG | 必填 | 商品sku库存初始数量，后续库存update只使用stocks.update接口进行调用 |
| sku\_pre\_sale\_time | INTEGER | 非必填 | sku预售时间戳，单位秒；不更新传null，取消传0，更新传实际值 |
| sku\_properties | OBJECT\[\] | 必填 | sku属性 |
| punit | STRING | 必填 | 属性单位 |
| ref\_pid | LONG | 必填 | 属性id |
| value | STRING | 必填 | 属性值 |
| vid | LONG | 必填 | 属性值id |
| spec\_id\_list | STRING | 必填 | 商品规格列表，根据pdd.goods.spec.id.get生成的规格属性id，例如：颜色规格下商家新增白色和黑色，大小规格下商家新增L和XL，则由4种spec组合，入参一种组合即可，在skulist中需要有4个spec组合的sku |
| thumb\_url | STRING | 必填 | sku预览图，预览图尺寸：等宽高，且高度不低于480px，现已支持1M大小，越清晰越好卖，SKU预览图格式：仅支持JPG,PNG格式 |
| weight | LONG | 必填 | 重量，单位为g |
| sku\_type | INTEGER | 非必填 | 库存方式（0：普通型，1：日历型） |
| song\_huo\_an\_zhuang | STRING | 非必填 | 送货入户并安装模版id |
| song\_huo\_ru\_hu | STRING | 非必填 | 送货入户模版id |
| tiny\_name | STRING | 非必填 | 商品短标题（仅在部分活动中生效），字数限制为4-20字 |
| two\_pieces\_discount | INTEGER | 非必填 | 满2件折扣，可选范围0-100, 0表示取消，95表示95折，设置需先查询规则接口获取实际可填范围 |
| warehouse | STRING | 非必填 | 保税仓，只在goods\_type为直供商品时有效（现阶段暂不支持） |
| warm\_tips | STRING | 非必填 | 水果类目温馨提示，只在水果类目商品才生效， 字数限制：商品描述goods\_desc+温馨提示总计不超过500字。 |
| zhi\_huan\_bu\_xiu | INTEGER | 非必填 | 只换不修的天数，目前只支持0和365 |
| medical\_device\_certificate\_gallery | STRING\[\] | 非必填 | 维护3个属性时需必填：842 注册证号、1144 安全套械（X）字号、1145 医疗器械注册证号，上传图格式要求宽高比例为1:1或3:4，且宽高均大于480px，大小3M内，仅支持一张图 |
| medical\_device\_confirm | INTEGER | 非必填 | 发布医疗器械相关商品，需接入此字段，根据医疗器械管理类别（属性ID：2677）填写结果，明确可提供消费者个人自行使用，0 不确认，1 确认，需商家确认才可发布 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_update\_response | OBJECT |  | response |
| goods\_commit\_id | LONG |  | 草稿id |
| goods\_id | LONG |  | 商品id |
| matched\_spu\_id | LONG |  | 商品匹配到的标品ID |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsEditGoodsCommitResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.CarouselVideoItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.ElecGoodsAttributes;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.GoodsPropertiesItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.GoodsPropertiesItemTableInfo;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.GoodsPropertiesItemTableInfoTableValueListItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.GoodsTradeAttr;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.GoodsTradeAttrBookingNotes;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.GoodsTravelAttr;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.OverseaGoods;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.SkuListItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.SkuListItemOverseaSku;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsEditGoodsCommitRequest.SkuListItemSkuPropertiesItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsEditGoodsCommitRequest request = new PddGoodsEditGoodsCommitRequest();
        request.setAutoFillSpuProperty(true);
        request.setBadFruitClaim(0);
        request.setBuyLimit(1L);
        List<String> carouselGallery = new ArrayList<String>();
        carouselGallery.add("str");
        request.setCarouselGallery(carouselGallery);
        List<CarouselVideoItem> carouselVideo = new ArrayList<CarouselVideoItem>();

        CarouselVideoItem item = new CarouselVideoItem();
        item.setFileId(0L);
        item.setVideoUrl("str");
        carouselVideo.add(item);
        request.setCarouselVideo(carouselVideo);
        request.setCarouselVideoUrl("str");
        request.setCatId(1L);
        request.setCostTemplateId(1L);
        request.setCountryId(1);
        request.setCustomerNum(10L);
        request.setCustoms("str");
        request.setDeliveryOneDay(1);
        request.setDeliveryType(1);
        List<String> detailGallery = new ArrayList<String>();
        detailGallery.add("str");
        request.setDetailGallery(detailGallery);

        ElecGoodsAttributes elecGoodsAttributes = new ElecGoodsAttributes();
        elecGoodsAttributes.setBeginTime(0L);
        elecGoodsAttributes.setDaysTime(0);
        elecGoodsAttributes.setEndTime(0L);
        elecGoodsAttributes.setTimeType(0);
        request.setElecGoodsAttributes(elecGoodsAttributes);
        request.setGoodsDesc("str");
        request.setGoodsName("str");
        List<GoodsPropertiesItem> goodsProperties = new ArrayList<GoodsPropertiesItem>();

        GoodsPropertiesItem item1 = new GoodsPropertiesItem();
        item1.setGroupId(0);
        item1.setImgUrl("str");
        item1.setNote("str");
        item1.setParentSpecId(0L);
        item1.setRefPid(0L);
        item1.setSpecId(0L);

        GoodsPropertiesItemTableInfo tableInfo = new GoodsPropertiesItemTableInfo();
        List<GoodsPropertiesItemTableInfoTableValueListItem> tableValueList = new ArrayList<GoodsPropertiesItemTableInfoTableValueListItem>();

        GoodsPropertiesItemTableInfoTableValueListItem item2 = new GoodsPropertiesItemTableInfoTableValueListItem();
        item2.setColumnType(0);
        item2.setUnit("str");
        item2.setValue("str");
        tableValueList.add(item2);
        tableInfo.setTableValueList(tableValueList);
        item1.setTableInfo(tableInfo);
        item1.setTemplatePid(0L);
        item1.setValue("str");
        item1.setValueUnit("str");
        item1.setVid(0L);
        goodsProperties.add(item1);
        request.setGoodsProperties(goodsProperties);

        GoodsTradeAttr goodsTradeAttr = new GoodsTradeAttr();
        goodsTradeAttr.setAdvancesDays(0);

        GoodsTradeAttrBookingNotes bookingNotes = new GoodsTradeAttrBookingNotes();
        bookingNotes.setUrl("str");
        goodsTradeAttr.setBookingNotes(bookingNotes);
        goodsTradeAttr.setLifeSpan(0);
        request.setGoodsTradeAttr(goodsTradeAttr);

        GoodsTravelAttr goodsTravelAttr = new GoodsTravelAttr();
        goodsTravelAttr.setNeedTourist(false);
        goodsTravelAttr.setType(0);
        request.setGoodsTravelAttr(goodsTravelAttr);
        request.setGoodsType(2);
        request.setImageUrl("str");
        request.setInvoiceStatus(0);
        request.setIsCustoms(true);
        request.setIsFolt(true);
        request.setIsGroupPreSale(1);
        request.setIsPreSale(true);
        request.setIsRefundable(true);
        request.setIsSkuPreSale(1);
        request.setLackOfWeightClaim(1);
        List<Integer> localServiceIdList = new ArrayList<Integer>();
        localServiceIdList.add(0);
        request.setLocalServiceIdList(localServiceIdList);
        request.setMaiJiaZiTi("str");
        request.setMarketPrice(10L);
        request.setOrderLimit(1L);
        request.setOriginCountryId(1);
        request.setOutGoodsId("str");
        request.setOutSourceGoodsId("str");
        request.setOutSourceType(1);

        OverseaGoods overseaGoods = new OverseaGoods();
        overseaGoods.setBondedWarehouseKey("str");
        overseaGoods.setConsumptionTaxRate(0);
        overseaGoods.setCustomsBroker("str");
        overseaGoods.setHsCode("str");
        overseaGoods.setValueAddedTaxRate(0);
        request.setOverseaGoods(overseaGoods);
        request.setOverseaType(1);
        request.setPreSaleTime(1634527822L);
        request.setPrivacyDelivery(0);
        request.setQuanGuoLianBao(0);
        request.setSecondHand(false);
        request.setShangMenAnZhuang("str");
        request.setShipmentLimitSecond(86400L);
        request.setShopGroupId(123L);
        request.setSizeSpecId(10L);
        List<SkuListItem> skuList = new ArrayList<SkuListItem>();

        SkuListItem item3 = new SkuListItem();
        item3.setIsOnsale(0);
        item3.setLength(0L);
        item3.setLimitQuantity(0L);
        item3.setMultiPrice(0L);
        item3.setOutSkuSn("str");
        item3.setOutSourceSkuId("str");

        SkuListItemOverseaSku overseaSku = new SkuListItemOverseaSku();
        overseaSku.setMeasurementCode("str");
        overseaSku.setSpecifications("str");
        overseaSku.setTaxation(0);
        item3.setOverseaSku(overseaSku);
        item3.setPrice(0L);
        item3.setQuantity(0L);
        item3.setSkuPreSaleTime(0);
        List<SkuListItemSkuPropertiesItem> skuProperties = new ArrayList<SkuListItemSkuPropertiesItem>();

        SkuListItemSkuPropertiesItem item4 = new SkuListItemSkuPropertiesItem();
        item4.setPunit("str");
        item4.setRefPid(0L);
        item4.setValue("str");
        item4.setVid(0L);
        skuProperties.add(item4);
        item3.setSkuProperties(skuProperties);
        item3.setSpecIdList("str");
        item3.setThumbUrl("str");
        item3.setWeight(0L);
        skuList.add(item3);
        request.setSkuList(skuList);
        request.setSkuType(0);
        request.setSongHuoAnZhuang("str");
        request.setSongHuoRuHu("str");
        request.setTinyName("str");
        request.setTwoPiecesDiscount(95);
        request.setWarehouse("str");
        request.setWarmTips("str");
        request.setZhiHuanBuXiu(0);
        List<String> medicalDeviceCertificateGallery = new ArrayList<String>();
        medicalDeviceCertificateGallery.add("str");
        request.setMedicalDeviceCertificateGallery(medicalDeviceCertificateGallery);
        request.setMedicalDeviceConfirm(0);
        PddGoodsEditGoodsCommitResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_update_response": {
    "goods_commit_id": 0,
    "goods_id": 0,
    "matched_spu_id": 0
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
| 50001 | 业务服务错误 |  |  |  |

### 限流规则

接口总限流频次：10000次/10秒

### API工具
