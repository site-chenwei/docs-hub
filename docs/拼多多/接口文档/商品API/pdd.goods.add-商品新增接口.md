---
title: "pdd.goods.add - 商品新增接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.add"
menu_path:
  - "商品API"
  - "pdd.goods.add"
captured_at: "2026-04-09T15:15:11.830Z"
---

# pdd.goods.add

## 商品新增接口

更新时间：2026-02-11 10:25:16

¥免费API

必须用户授权

单个商品发布，需要配合pdd.goods.img.upload上传主图及商品详情图片。

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
| carousel\_gallery | STRING\[\] | 必填 | 商品轮播图，按次序上传，图片格式支持JPEG/JPG/PNG， 图片尺寸长宽比1：1且尺寸不低于480px，图片大小最高1MB |
| carousel\_video | OBJECT\[\] | 非必填 | 商品视频 |
| file\_id | LONG | 非必填 | 商品视频id |
| video\_url | STRING | 非必填 | 商品视频url |
| carousel\_video\_url | STRING | 非必填 | 轮播视频 |
| cat\_id | LONG | 必填 | 叶子类目ID |
| cost\_template\_id | LONG | 必填 | 物流运费模板ID，可使用pdd.goods.logistics.template.get获取 |
| country\_id | INTEGER | 必填 | 地区/国家ID，country\_id可以通过pdd.goods.country.get获取，仅在goods\_type为2、3时（海淘商品）入参生效，其余goods\_type传0 |
| customer\_num | LONG | 非必填 | 团购人数 |
| customs | STRING | 非必填 | 海关名称，只在goods\_type=3（直供商品）时入参且is\_customs=true，入参枚举值为：广州、杭州、宁波、郑州、郑州(保税物流中心)、重庆、西安、上海、郑州(综保区)、深圳、福建、天津 |
| delivery\_one\_day | INTEGER | 非必填 | 是否当日发货,0 否，1 是 |
| delivery\_type | INTEGER | 非必填 | 发货方式。0：无物流发货；1：有物流发货。 |
| detail\_gallery | STRING\[\] | 必填 | 商品详情图： a. 尺寸要求宽度处于480~1200px之间，高度0-1500px之间 b. 大小1M以内 c. 数量限制在20张之间 d. 图片格式仅支持JPG,PNG格式 e. 点击上传时，支持批量上传详情图 |
| elec\_goods\_attributes | OBJECT | 非必填 | 卡券类商品属性 |
| begin\_time | LONG | 非必填 | 开始时间（timeType=1时必填表示核销的开始时间）（精确到毫秒） |
| days\_time | INTEGER | 非必填 | 天数内有效（timeType=3必填，表示发货后几天内核销） |
| end\_time | LONG | 非必填 | 截止时间（timeType=1,2时必填，表示发货后核销的截止时间）（精确到毫秒） |
| time\_type | INTEGER | 非必填 | 卡券核销类型（1：起始时间内有效，2：发货后后至截止时间内有效，3：发货后多少天内有效） |
| goods\_desc | STRING | 非必填 | 商品描述， 字数限制：20-500，例如，新包装，保证产品的口感和新鲜度。单颗独立小包装，双重营养，1斤家庭分享装，更实惠新疆一级骏枣夹核桃仁。 |
| goods\_name | STRING | 必填 | 商品标题，例如，新疆特产 红满疆枣夹核桃500g |
| goods\_properties | OBJECT\[\] | 非必填 | 商品属性列表 |
| group\_id | INTEGER | 非必填 | 属性值分组ID，非销售属性不用传 |
| img\_url | STRING | 非必填 | 图片url，非销售属性不用传 |
| note | STRING | 非必填 | 备注，非销售属性不用传 |
| parent\_spec\_id | LONG | 非必填 | 父规格ID，非销售属性不用传 |
| ref\_pid | LONG | 非必填 | 引用属性id |
| spec\_id | LONG | 非必填 | 规格ID，非销售属性不用传 |
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
| goods\_type | INTEGER | 必填 | 1-国内普通商品，2-一般贸易，3-保税仓BBC直供，4-海外BC直邮 ,5-流量 ,6-话费 ,7-优惠券 ,8-QQ充值 ,9-加油卡，15-商家卡券，18-海外CC行邮 19-平台卡券 |
| ignore\_edit\_warn | BOOLEAN | 非必填 | 是否获取商品发布警告信息，默认为忽略 |
| image\_url | STRING | 非必填 | 商品主图，请参考拼多多首页大图，如果商品参加部分活动则必填，否则无法参加活动 a. 尺寸750 x 352px b. 大小100k以内 c. 图片格式仅支持JPG,PNG格式 d. 图片背景应以纯白为主, 商品图案居中显示 e. 图片不可以添加任何品牌相关文字或logo |
| invoice\_status | BOOLEAN | 非必填 | 是否支持开票（测试中） |
| is\_customs | BOOLEAN | 非必填 | 是否需要上报海关，false-无需上报海关，true-需上报海关 |
| is\_folt | BOOLEAN | 必填 | 是否支持假一赔十，false-不支持，true-支持 |
| is\_group\_pre\_sale | INTEGER | 非必填 | 是否成团预售。0：不是；1:是。 |
| is\_pre\_sale | BOOLEAN | 必填 | 是否预售,true-预售商品，false-非预售商品 |
| is\_refundable | BOOLEAN | 必填 | 是否7天无理由退换货，true-支持，false-不支持 |
| is\_sku\_pre\_sale | INTEGER | 非必填 | 是否sku预售，1：是，0：否 |
| lack\_of\_weight\_claim | INTEGER | 非必填 | 缺重包退 |
| local\_service\_id\_list | INTEGER\[\] | 非必填 | 本地服务id |
| mai\_jia\_zi\_ti | STRING | 非必填 | 买家自提模版id |
| market\_price | LONG | 必填 | 参考价格，单位为分 |
| order\_limit | INTEGER | 非必填 | 单次限量 |
| origin\_country\_id | INTEGER | 非必填 | 原产地id，是指海淘商品的生产地址，仅在goods type=3/4的时候必填，可以通过pdd.goods.country.get获取 |
| out\_goods\_id | STRING | 非必填 | 商品goods外部编码，同其他接口中的outer\_goods\_id 、out\_goods\_id、out\_goods\_sn、outer\_goods\_sn 都为商家编码（goods维度）。 |
| out\_source\_goods\_id | STRING | 非必填 | 第三方商品Id |
| out\_source\_type | INTEGER | 非必填 | 第三方商品来源 |
| oversea\_goods | OBJECT | 非必填 | { "consumption\_tax\_rate": 1, "value\_added\_tax\_rate": 9, "hs\_code": "2200", "customs\_broker": "sss", "bonded\_warehouse\_key": "pp" } |
| bonded\_warehouse\_key | STRING | 必填 | 保税仓唯一标识 |
| consumption\_tax\_rate | INTEGER | 非必填 | 消费税率 |
| customs\_broker | STRING | 非必填 | 清关服务商 |
| hs\_code | STRING | 非必填 | 海关编号 |
| value\_added\_tax\_rate | INTEGER | 非必填 | 增值税率 |
| oversea\_type | INTEGER | 非必填 | oversea\_type |
| pre\_sale\_time | LONG | 非必填 | 预售时间，is\_pre\_sale为true时必传，UNIX时间戳，只能为某一天的23:59:59 |
| privacy\_delivery | INTEGER | 非必填 | 保密发货，1: 支持，0: 不支持 |
| quan\_guo\_lian\_bao | INTEGER | 非必填 | 0：不支持全国联保；1：支持全国联保 |
| second\_hand | BOOLEAN | 必填 | 是否二手商品，true -二手商品 ，false-全新商品 |
| shang\_men\_an\_zhuang | STRING | 非必填 | 上门安装模版id |
| shipment\_limit\_second | LONG | 必填 | 承诺发货时间（秒），普通、进口商品可选48小时或24小时；直邮商品（goods\_type=4）只可入参120小时，直供商品（goods\_type=3）只可入参96小时；is\_pre\_sale为true时不必传 |
| shop\_group\_id | LONG | 非必填 | 门店组id |
| size\_spec\_id | LONG | 非必填 | 尺码表id |
| sku\_list | OBJECT\[\] | 必填 | sku对象列表,实例：\[{ "is\_onsale": 1, "limit\_quantity": 999, "price": "2200", "weight": 1000, "multi\_price": "1900", "thumb\_url": "http://t06img.yangkeduo.com/images/2018-04-15/ced035033b5d40b589140af882621c03.jpg", "out\_sku\_sn": "L", "quantity": 100, "spec\_id\_list": "\[25\]", "oversea\_sku": { "measurement\_code": "计量单位编码", "taxation": "税费", "specifications": "规格" } }\] |
| is\_onsale | INTEGER | 必填 | sku上架状态，0-已下架，1-上架中 |
| length | LONG | 非必填 | sku送装参数：长度 |
| limit\_quantity | LONG | 必填 | sku购买限制，只入参999 |
| multi\_price | LONG | 必填 | 商品团购价格 |
| out\_sku\_sn | STRING | 非必填 | 商品sku外部编码，同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。 |
| out\_source\_sku\_id | STRING | 非必填 | 第三方sku Id |
| oversea\_sku | OBJECT | 非必填 | oversea\_sku |
| measurement\_code | STRING | 必填 | 计量单位编码，从接口pdd.gooods.sku.measurement.list获取code |
| specifications | STRING | 必填 | 规格 |
| taxation | INTEGER | 必填 | 税费 |
| price | LONG | 必填 | 商品单买价格 |
| quantity | LONG | 必填 | 商品sku库存初始数量，后续库存update只使用stocks.update接口进行调用 |
| sku\_pre\_sale\_time | INTEGER | 非必填 | sku预售时间戳，单位秒 |
| sku\_properties | OBJECT\[\] | 必填 | sku属性 |
| punit | STRING | 必填 | 属性单位 |
| ref\_pid | LONG | 必填 | 属性id |
| value | STRING | 必填 | 属性值 |
| vid | LONG | 必填 | 属性值id |
| spec\_id\_list | STRING | 必填 | 商品规格列表，根据pdd.goods.spec.id.get生成的规格属性id，例如：颜色规格下商家新增白色和黑色，大小规格下商家新增L和XL，则由4种spec组合，入参一种组合即可，在skulist中需要有4个spec组合的sku，示例：\[20,5\] |
| thumb\_url | STRING | 必填 | sku 缩略图 |
| weight | LONG | 必填 | 重量，单位为g |
| sku\_type | INTEGER | 非必填 | 库存方式（0：普通型，1：日历型） |
| song\_huo\_an\_zhuang | STRING | 非必填 | 送货入户并安装模版id |
| song\_huo\_ru\_hu | STRING | 非必填 | 送货入户模版id |
| tiny\_name | STRING | 非必填 | 短标题，示例：新包装，保证产品的口感和新鲜度。单颗独立小包装，双重营养，1斤家庭分享装，更实惠新疆一级骏枣夹核桃仁。 |
| two\_pieces\_discount | INTEGER | 非必填 | 满2件折扣，可选范围0-100, 0表示取消，95表示95折，设置需先查询规则接口获取实际可填范围 |
| warehouse | STRING | 非必填 | 保税仓，只在goods\_type=3（直供商品）时入参，入参枚举值为：宁波保税仓、杭州保税仓、广州保税仓、深圳保税仓、重庆保税仓、郑州保税仓、福建保税仓、天津保税仓、上海保税仓、银川保税仓、成都保税仓 |
| warm\_tips | STRING | 非必填 | 水果类目温馨提示，只在水果类目商品才生效， 字数限制：商品描述goods\_desc+温馨提示总计不超过500字。 |
| zhi\_huan\_bu\_xiu | INTEGER | 非必填 | 只换不修的天数，目前只支持0和365 |
| medical\_device\_certificate\_gallery | STRING\[\] | 非必填 | 维护3个属性时需必填：842 注册证号、1144 安全套械（X）字号、1145 医疗器械注册证号，上传图格式要求宽高比例为1:1或3:4，且宽高均大于480px，大小3M内，仅支持一张图 |
| medical\_device\_confirm | INTEGER | 非必填 | 发布医疗器械相关商品，需接入此字段，根据医疗器械管理类别（属性ID：2677）填写结果，明确可提供消费者个人自行使用，0 不确认，1 确认，需商家确认才可发布 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_add\_response | OBJECT |  | response |
| goods\_commit\_id | LONG |  | 上传商品的上传序列ID |
| goods\_id | LONG |  | 商品ID |
| matched\_spu\_id | LONG |  | 商品匹配到的标品ID |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsAddResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.CarouselVideoItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.ElecGoodsAttributes;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.GoodsPropertiesItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.GoodsPropertiesItemTableInfo;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.GoodsPropertiesItemTableInfoTableValueListItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.GoodsTradeAttr;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.GoodsTradeAttrBookingNotes;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.GoodsTravelAttr;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.OverseaGoods;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.SkuListItem;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.SkuListItemOverseaSku;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsAddRequest.SkuListItemSkuPropertiesItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsAddRequest request = new PddGoodsAddRequest();
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
        item2.setColumnType(1);
        item2.setUnit("%");
        item2.setValue("20");
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
        request.setIgnoreEditWarn(true);
        request.setImageUrl("str");
        request.setInvoiceStatus(true);
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
        request.setOrderLimit(1);
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
        request.setMedicalDeviceConfirm(1);
        PddGoodsAddResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_add_response": {
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
| 50001 | 业务服务错误 | isv.good-service-error:cannot-update-goods\_type-in-5\_6\_7 | 其它商品类型不允许修改为流量、话费、虚拟优惠券 | 其它商品类型不允许修改为流量、话费、虚拟优惠券，请重新修改商品类型 |
| isv.good-service-error:goods\_type-is-7-cannot-update | 虚拟优惠券类型商品不允许修改商品类型 | 虚拟优惠券类型商品不允许修改商品类型，请检查入参goods\_type |
| isv.good-service-error:goods\_type-is-8 | QQ充值商品异常 | QQ充值商品异常 |
| isv.good-service-error:goods\_type-is-9 | 加油卡商品异常 | 加油卡商品异常 |
| isv.goods-activities-service-error:quantity-cannot-be-reduce | 参加流量券活动的商品不能减少库存 | 活动期间商品无法减库存 |
| isv.goods-service-error:cannot-support-regular-purchase-limitation | 该类目不允许设置定期限购 | 该类目不允许设置定期限购次数 |
| isv.goods-service-error:coupon-invaild | 该商品绑定的优惠券已过期，不可编辑！新增优惠券商品请联系运营 | 该商品绑定的优惠券已过期，不可编辑！新增优惠券商品请联系运营 |
| isv.goods-service-error:is\_refundable-cannot-be-false | 该商品为二手商品，是否二手请选择是后再重新操作 | 请检查入参second\_hand，必须选择true |
| isv.goods-service-error:is\_refundable-cannot-be-true | 二手商品无法修改为全新商品 | 请检查入参second\_hand，必须选择true |
| isv.goods-service-error:is\_refundable-must-be-false | 是否二手商品必须选择否 | 请检查入参second\_hand，必须选择false |
| isv.goods-service-error:is\_refundable-must-be-true | 是否二手商品必须选择是 | 请检查入参second\_hand，必须选择true |
| isv.goods-service-error:must-support-free\_sf-and-quan\_guo\_lian\_bao | 该商品需选择顺丰包邮和全国联保 | 该商品需选择顺丰包邮和全国联保，请检查入参cost\_template\_id、quan\_guo\_lian\_bao |
| isv.goods-service-error:must-support-quan\_guo\_lian\_bao | 该商品需选择全国联保 | 该商品需选择全国联保，请检查入参quan\_guo\_lian\_bao |
| isv.goods-service-error:must-support-quan\_guo\_lian\_bao-or-return\_freight\_payer | 该商品需选全国联保或店铺有自动续费的退货包运费服务 | 该商品需选全国联保或店铺有自动续费的退货包运费服务，请检查入参quan\_guo\_lian\_bao或确认商品是否加入退货包运费服务 |
| isv.goods-service-error:must-support-zhi\_huan\_bu\_xiu-or-quan\_guo\_lian\_bao | 该商品需选择只换不修或全国联保 | 该商品需选择只换不修或全国联保，请检查入参zhi\_huan\_bu\_xiu、quan\_guo\_lian\_bao |
| isv.goods-service-error:price-cannot-over-market\_price | SKU单买价格必须小于参考价格 | 请检查sku\_list中的price，必须小于market\_price |
| isv.goods-service-error:price-cannot-over-maximum | 您的商品sku\_id为%s正在参与流量券活动,修改的价格不能大于等于最高限价。 | 请检查入参sku\_list中价格设置，参加流量券活动的商品修改的价格不能高于最高限制价格 |
| isv.goods-service-error:price-must-over-multi\_price | 单买价格需要比团购价格高至少0元，请重新设置 | 请检查sku\_list中的price，必须高于multi\_price |
| isv.goods-service-error:price-must-over-multi\_price-10 | sku单买价格需要比团购价格高至少0.1元，请重新设置 | 请检查sku\_list中的price，必须高于multi\_price0.1元 |
| isv.goods-service-error:price-must-over-multi\_price-100 | SKU单买价格需要比团购价格高至少一元，请重新设置 | 请检查sku\_list中的price，必须高于multi\_price1元 |
| isv.goods-service-error:regular-purchase-limitation-over-range | 定期限购需介于0～999999 | 设置定期限购次数需介于0~999999之间 |
| isv.goods-service-error:sku-quantity-cannot-over-password-quantity | sku库存不能大于卡密数量 | 卡密商品设置的sku库存不能大于卡密数量，只能小于等于卡密数量，请检查入参sku\_list |
| isv.invalid-paramete:goods\_desc-include-invalid-arguments | 商品描述输入了目前不支持的内容，如表情等，请修改后再次操作 | 请检查入参goods\_desc，是否出现非法字符 |
| isv.invalid-paramete:goods\_name-include-invalid-arguments | 商品标题输入了目前不支持的内容，如表情等，请修改后再次操作 | 请检查入参goods\_name，是否出现非法字符 |
| isv.invalid-paramete:tiny\_name-include-invalid-arguments | 短标题输入了目前不支持的内容，如表情等，请修改后再次操作 | 请检查入参tiny\_name，是否出现非法字符 |
| isv.invalid-paramete:warm\_tips-include-invalid-arguments | 温馨提示输入了目前不支持的内容，如表情等，请修改后再次操作 | 请检查入参warm\_tips，是否出现非法字符 |
| isv.invalid-parameter:cat\_id | 分类不存在，请重新选择分类 | 请检查入参参数cat\_id是否为当前可用类目，可以通过pdd.goods.authorization.cats查询当前商家可发布商品的类目信息 |
| isv.invalid-parameter:cat\_id-cannot-be-allow | 当前商品分类不在店铺经营范围内，请重新选择商品分类 | 请检查入参cat\_id，重新选择授权店铺允许发布的商品分类 |
| isv.invalid-parameter:cat\_id-cannot-be-change | 虚拟商品不允许更换商品分类，若需更换，请重新发布商品 | 虚拟商品不允许更换商品分类，请检查入参cat\_id |
| isv.invalid-parameter:cat\_id-lever | 商品必须有三级或四级分类 | 请检查入参参数cat\_id是否为三级或四级类目 |
| isv.invalid-parameter:change-goods\_name | 【XX进口】【XX直邮】【XX直供】不可以填入商品标题中，请修改后重新操作 | 【XX进口】【XX直邮】【XX直供】不可以填入商品标题中，请检查入参goods\_name |
| isv.invalid-parameter:cost\_template\_id-cannot-support-free\_sf | 该类目暂时不支持顺丰包邮，请重新选择物流模板 | 该类目暂时不支持顺丰包邮，请重新选择物流模板cost\_template\_id |
| isv.invalid-parameter:customer\_num-is-over-range | 团购人数需介于2-9 | 请检查入参customer\_num，该类目商品成团人数至少2人以上10人以下 |
| isv.invalid-parameter:customer\_num-must-over-2 | 团购人数至少为2人 | 请检查入参customer\_num，至少2人以上 |
| isv.invalid-parameter:detail\_gallery-is-over-range | 商品详情图数量必须在1-20张之间,请重新操作 | 该店铺商品详情图数量必须在1-20张之间，请检查入参detail\_gallery |
| isv.invalid-parameter:forbidden-multi\_price-less-then-zero | SKU团购价格需大于0 | 请检查sku\_list中multi\_price，必须设置为正数 |
| isv.invalid-parameter:forbidden-update-quantity-less-then-zero | 预估当前库存加上库存增减值应该大于或等于0 | 请检查入参sku\_list的中库存设置，必须为正整数 |
| isv.invalid-parameter:goods\_descc-add-warm\_tips\_is-too-long | 商品描述+温馨提示字数超过500字上限 | 商品描述与温馨提示字数不能超过500字，请检查入参goods\_desc和warm\_tips |
| isv.invalid-parameter:goods\_descc-include-forbid-word | 商品标题中出现敏感词汇，请重新编辑 | 命中平台商品标题风控逻辑，请检查入参goods\_name |
| isv.invalid-parameter:goods\_descc-is-too-short | 商品描述过短，请重新编辑 | 商品描述过短，请检查入参goods\_desc |
| isv.invalid-parameter:goods\_descc\_is-too-long | 商品描述超过500字，请重新编辑 | 商品描述超过500字，请检查入参goods\_desc |
| isv.invalid-parameter:goods\_name-exclude-pre-sale | 预售信息不可以填入商品标题中，请修改后重新操作 | 预售信息不可以填入商品标题中，请检查入参goods\_name |
| isv.invalid-parameter:goods\_name-exclude-price | 价格信息不可以填入商品标题中，请修改后重新操作! | 商品标题goods\_name必须不包含任何价格信息，请检查入参goods\_name |
| isv.invalid-parameter:goods\_name-exclude-production-date | 商品描述中请勿填写生产日期 | 商品描述不允许填写生产日期，请检查入参goods\_desc |
| isv.invalid-parameter:goods\_name-exclude-shelf-life | 商品描述中请勿填写保质期 | 商品描述不允许填写保质期，请检查入参goods\_desc |
| isv.invalid-parameter:goods\_name-include-forbid-word | 商品描述中出现敏感词汇，请重新编辑 | 命中平台商品描述风控逻辑，请检查入参goods\_desc |
| isv.invalid-parameter:invoice\_status | 该类目/店铺/品牌不支持纸质发票 | 该类目/店铺/品牌不支持纸质发票，请检查入参invoice\_status |
| isv.invalid-parameter:invoice\_status-is-1 | 该类目/店铺/品牌不支持电子发票 | 该类目/店铺/品牌不支持电子发票，请检查入参invoice\_status |
| isv.invalid-parameter:market\_price-cannot-be-less-than-zero | 参考价不能小于等于0 | 请检查入参market\_price，必须为正数 |
| isv.invalid-parameter:market\_price-is-too-expensive | 参考价格太大 | 请检查入参market\_price，参考价格不大于1000000000 |
| isv.invalid-parameter:multi\_price-is-over-range | 商品规格中，团购价的范围过大，超出类目限制，请修改 | 该类目下sku设置的区间价格过大，请检查sku\_list中multi\_price |
| isv.invalid-parameter:multi\_price-is-too-expensive | SKU团购价格太大 | 请检查sku\_list中multi\_price，尝试减小sku团购价格后重试 |
| isv.invalid-parameter:multi\_price-is-too-high | 团购价最低值不符合该商品参考价格，请修改后重试 | 请检查sku\_list中multi\_price，与同类商品最低价格差距过大 |
| isv.invalid-parameter:multi\_price-is-too-low | 团购价最高值不符合该商品参考价格，请修改后重试 | 请检查sku\_list中multi\_price，与同类商品最高价格差距过大 |
| isv.invalid-parameter:multi\_price-must-over-activity-price | 商品价格必须高于多件优惠的优惠金额 | 请检查sku\_list中的multi\_price，不能高于提报多件优惠营销活动的优惠金额 |
| isv.invalid-parameter:onsale-sku-quantity-invalid | 已上架的SKU的预估库存加库存增减的总数需大于0 | 已上架的SKU的预估库存加库存增减的总数需大于0，请检查入参sku\_list |
| isv.invalid-parameter:order\_limit-is-over-range | 购买限次必须在1-999999之间 | 请检查入参order\_limit，购买限次必须在1-999999之间 |
| isv.invalid-parameter:out\_goods\_id\_is-too-long | 商家编码超出100个中文字符长度限制，请重新修改 | 请检查out\_goods\_id长度 |
| isv.invalid-parameter:out\_goods\_id\_is-too-long-1 | 商家编码超出100个中文字符长度限制，请重新修改1 | 请检查out\_goods\_id长度 |
| isv.invalid-parameter:pre\_sale\_time-over-7 | 预售时间超过7日，请修改后再提交或联系对接运营 | 预售时间超过7日，请修改后再提交或联系对接运营 |
| isv.invalid-parameter:price-gap-is-over-range | 商品规格中价格的范围过大，请调整价格。若实际价格差异很大的商品请分开发布，避免因低价sku违规。 | 请检查入参sku\_list中的价格设置，不允许同一商品价格差距过大，请酌情调整商品价格 |
| isv.invalid-parameter:price-is-too-expensive | SKU单买价格太大 | 请检查sku\_list中的price，值过大请减小后重新提交 |
| isv.invalid-parameter:price-or-multi\_price | SKU的价格和团价格不合法 | 请检查sku\_list中的price和multi\_price的格式 |
| isv.invalid-parameter:quantity-invalid | 单个sku预估库存+库存增减值需小于等于200000000 | 单个sku预估库存+库存增减值需小于等于200000000，请检查入参sku\_list |
| isv.invalid-parameter:quantity-is-over-range | sku的预估当前库存加上库存增减值太大 | 请检查入参sku\_list的中库存设置，必须需小于等于200000000且大于0 |
| isv.invalid-parameter:quan\_guo\_lian\_bao | 该类目/店铺/品牌暂时不支持全国联保 | 该类目/店铺/品牌暂时不支持全国联保，请检查入参quan\_guo\_lian\_bao |
| isv.invalid-parameter:quan\_guo\_lian\_bao-must-be-0or1 | 全国联保只能选0或1 | 全国联保只能选0或1，请检查入参quan\_guo\_lian\_bao |
| isv.invalid-parameter:shipment\_limit\_second | 商品承诺发货时间不合法 | 商品承诺时间不符合平台规则，对于普通商品，承诺发货时间为24或48小时，即86400或172800秒；对直邮直供商品，承诺发货时间为7天，即604800； |
| isv.invalid-parameter:spec\_name-is-too-long | 规格名称不能超过18个字符，请重新修改 | 请检查入参spec\_id\_list中的spec\_id，对应的规格名称不能超过18个字符 |
| isv.invalid-parameter:tiny\_name-include-forbid-word | 短标题出现敏感词汇，请重新编辑 | 请检查入参tiny\_name |
| isv.invalid-parameter:tiny\_name-is-over-range | 短标题长度需介于4~20个字之间 | 请检查入参tiny\_name，短标题长度需介于4~20个字之间 |
| isv.invalid-parameter:tiny\_name-is-too-lang | 短标题长度需小于20个字 | 请检查入参tiny\_name，短标题长度需介于4~20个字之间 |
| isv.invalid-parameter:update-quantity-invalid | 单个sku库存增减值不能超过100000000 | 单个sku库存增减值不能超过100000000，请检查入参sku\_list |
| isv.invalid-parameter:zhi\_huan\_bu\_xiu | 该类目/店铺/品牌暂时不支持只换不修 | 该类目/店铺/品牌暂时不支持只换不修，请检查入参zhi\_huan\_bu\_xiu |
| isv.invalid-parameter:zhi\_huan\_bu\_xiu-must-be-365 | 只换不修只能选365天 | 只换不修只能选365天，请检查入参zhi\_huan\_bu\_xiu |
| isv.invalid-permission:add-sku-invalid | 提交不成功，活动期间的商品不可以新增SKU | 活动期间商品无法sku |
| isv.invalid-permission:cannot-support-goods\_type-is-5\_6 | 非虚拟类目商家不可以创建和修改话费、流量商品 | 非虚拟类目商家不可以创建和修改话费、流量商品，请调整入参goods\_type |
| isv.invalid-permission:cat\_id-not-in-electric-city | 该商品类目不在电器城内 | 该类目商品不允许上架到电器城 |
| isv.invalid-permission:goods\_type-cannot-support-thousand-people-group | 暂时只有普通、进口、直邮、直供设置千人团活动 | 仅普通、进口、直邮、直供商品才能参加千人团活动 |
| isv.invalid-permission:goods\_type-is-15 | 当前分类不支持设置卡密商品 | 请检查入参cat\_id，该类目商品不支持设置卡密商品 |
| isv.invalid-permission:in-the-high-risk | 检测为高风险店铺禁止编辑，详情请到电脑端查看 | 检测为高风险店铺禁止编辑，详情请到电脑端查看 |
| isv.invalid-permission:in-the-punishment-2 | 店铺处于二级惩罚，不可编辑 | 店铺处于二级惩罚，不可编辑 |
| isv.invalid-permission:in-the-punishment-3 | 店铺处于三级惩罚，不可编辑 | 店铺处于三级惩罚，不可编辑 |
| isv.invalid-permission:mall-has-not-agree-protocol | 店铺不同意新协议，无法编辑商品 | 店铺不同意新协议，无法编辑商品，请登录商家后台mms.pinduoduo.com同意协议 |
| isv.invalid-permission:mall-info-is-not-perfect | 当前店铺资料未完善，无法发布商品，已为您存入草稿箱中，请完善资料并审核通过后提交 | 当前店铺资料未完善，无法发布商品，已为您存入草稿箱中，请完善资料并审核通过后提交 |
| isv.invalid-permission:mall-info-is-reject | 当前店铺资料被驳回，无法发布商品，已为您存入草稿箱中，请重新提交资料审核通过后提交 | 当前店铺资料被驳回，无法发布商品，已为您存入草稿箱中，请重新提交资料审核通过后提交 |
| isv.invalid-permission:mall-info-is-waitting-for-review | 当前店铺资料正在审核中，无法发布商品，已为您存入草稿箱中，请等待审核通过后提交 | 当前店铺资料正在审核中，无法发布商品，已为您存入草稿箱中，请等待审核通过后提交 |
| isv.invalid-permission:mall-is-apply-closed | 店铺已申请关店，无法编辑商品 | 店铺已申请关店，无法编辑商品 |
| isv.invalid-permission:mall-is-waitting-for-review | 店铺正在审核中，无法发商品 | 店铺正在审核中，无法发商品，待入驻成功后重新提交 |
| isv.invalid-permission:must-relieve-depot | sku需要先与库存中心解绑才能删除 | sku需要先与库存中心解绑才能删除，请检查入参sku\_list |
| isv.invalid-permission:thousand-people-group | 千人团活动类型提交没有权限 | 没有提交千人团活动的权限 |
| isv.invalid-permission:today-add-goods-num-is-over-range | 今日店铺创建商品数达到上限，请明天再试 | 今日店铺创建商品数达到上限，请明天再试 |
| isv.invalid-permissioncost\_template\_id | 店铺未允许使用运费模板 | 店铺未允许使用运费模板，请检查入参cost\_template\_id |
| isv.missing-parameter:image\_url | 该商品处于首页，请上传主图后再提交 | 请检查入参image\_url |
| isv.missing-parameter:must-support-electronic-certificate | 该商品需要设置电子凭证 | 该类目商品需设置电子凭证 |
| isv.missing-parameter:sku.thumb\_url | 请上传sku缩略图 | 缺失sku缩略图，请检查入参sku\_list |
| isv.missing-parameter:tiny\_name | 请填写短标题 | 必须入参tiny\_name |
| isv.parameters-mismatch:cat\_id-and-cost\_template\_id | 该分类不支持送货入户，请重新选择运费模板 | 该分类不支持送货入户，请重新选择运费模板，请检查入参cost\_template\_id |
| isv.parameters-mismatch:cat\_id-and-spec\_id\_list | 该分类暂不支持两种规格，请重新选择规格类型 | 该类目只允许单规格或单品，请检查入参spec\_id\_list |
| isv.parameters-mismatch:country\_id-and-goods\_type | 只有进口、直邮、直供商品，才需要输入地区/国家 | 普通商品请入参country\_id为0 |
| isv.parameters-mismatch:country\_id-and-goods\_type-is-2 | 进口商品请选择地区/国家 | 请检查入参country\_id，地区/国家ID可在pdd.logistics.address.get获取 |
| isv.parameters-mismatch:country\_id-and-goods\_type-is-3 | 直供商品请选择地区/国家 | 请检查入参country\_id，地区/国家ID可在pdd.logistics.address.get获取 |
| isv.parameters-mismatch:country\_id-and-goods\_type-is-4 | 直邮商品请选择地区/国家 | 请检查入参country\_id，地区/国家ID可在pdd.logistics.address.get获取 |
| isv.parameters-mismatch:goods\_name-and-goods\_type | 当前商品类型与主营类目或商品分类不符，请重新选择商品类型 | 请检查入参cat\_id，重新选择授权店铺允许发布的商品分类 |
| isv.parameters-mismatch:goods\_name-and-is\_folt | 商品中含有正品词或品牌词，请设置假一赔十 | 商品中含有正品词或品牌词，请检查入参假一赔十is\_folt是否为true |
| isv.parameters-mismatch:goods\_type-and-cost\_template\_id-postage | 虚拟商品必须包邮 | 虚拟商品必须包邮，请检查入参cost\_template\_id |
| isv.parameters-mismatch:warehouse-and-goods\_type-is-3 | 直供商品请选择国内保税仓 | 请检查入参is\_customs及customs字段 |
| isv.parameters-mismatch:weight-and-cost\_template\_id | 按重量算运费的商品,SKU必须填写重量 | 按重量算运费的商品,SKU必须填写重量，请检查入参cost\_template\_id、sku\_list |

### 限流规则

商家限流频次：20次/1秒

接口总限流频次：9500次/10秒

应用限流频次：2000次/10秒

### API工具
