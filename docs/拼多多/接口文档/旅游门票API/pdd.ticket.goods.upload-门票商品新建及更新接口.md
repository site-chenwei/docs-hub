---
title: "pdd.ticket.goods.upload - 门票商品新建及更新接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ticket.goods.upload"
menu_path:
  - "旅游门票API"
  - "pdd.ticket.goods.upload"
captured_at: "2026-04-09T15:25:01.679Z"
---

# pdd.ticket.goods.upload

## 门票商品新建及更新接口

更新时间：2021-10-15 14:10:20

¥免费API

必须用户授权

门票商品新建及更新

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
| carousel\_gallery | STRING\[\] | 非必填 | 商品轮播图，按次序上传，图片格式支持JPEG/JPG/PNG， 图片尺寸长宽比1：1且尺寸不低于480px，图片大小最高1MB。先通过pdd.goods.image.upload上传图片 |
| carousel\_video | OBJECT\[\] | 非必填 | 轮播视频。需要先上传到pdd.goods.filespace.image.upload |
| file\_id | LONG | 非必填 | 轮播视频id |
| video\_url | STRING | 非必填 | 轮播视频url |
| cat\_id | LONG | 非必填 | 类目id，国内门票（含港澳台）传9088，国外门票传20042。发布成功后不能修改。新增商品时必填。 |
| code\_mode | INTEGER | 非必填 | 电子票发码方式，0=手动电子票；1=实时电子票，自动发货。新增商品时必填。 |
| detail\_gallery | STRING\[\] | 非必填 | 商品详情图： a. 尺寸要求宽度处于480~1200px之间，高度0-1500px之间 b. 大小1M以内 c. 数量限制在20张之间 d. 图片格式仅支持JPG,PNG格式 。先通过pdd.goods.image.upload上传图片，新增商品时必填。 |
| goods\_commit\_id | LONG | 非必填 | 草稿id，编辑草稿时必传。 |
| goods\_desc | STRING | 非必填 | 商品描述，字数限制：20~500。新增商品时必填。 |
| goods\_id | LONG | 非必填 | 商品id，编辑商品时必传。 |
| goods\_name | STRING | 非必填 | 商品标题，新增商品时必填。 |
| goods\_properties | OBJECT\[\] | 非必填 | 商品属性，先调pdd.goods.cat.template.get，根据cat\_id获取，新增商品时必填。 |
| parent\_spec\_id | LONG | 非必填 | 父规格id，仅对于销售属性入参 |
| ref\_pid | LONG | 非必填 | 引用属性id |
| spec\_id | LONG | 非必填 | 规格id，仅对于销售属性入参，和sku中的spec对应 |
| value | STRING | 非必填 | 属性值 |
| value\_unit | STRING | 非必填 | 属性值单位 |
| vid | LONG | 非必填 | 属性值id |
| ignore\_edit\_warn | BOOLEAN | 非必填 | 是否获取商品发布警告信息，默认为忽略 |
| is\_submit | INTEGER | 非必填 | 是否提交本次编辑，0=不提交，表示仅保存草稿，不进行提交，不会进行校验；1=提交，表示提交本次编辑内容，会进行校验；不传时默认为提交 |
| market\_price | LONG | 非必填 | 商品参考价，单位为分，必须高于最高的sku单买价。新增商品时必填。 |
| out\_goods\_sn | STRING | 非必填 | 商品goods外部编码，同其他接口中的outer\_goods\_id 、out\_goods\_id、out\_goods\_sn、outer\_goods\_sn 都为商品维度的商家编码。 |
| reserve\_limit\_rule | STRING | 非必填 | 预定时间限制，格式：1\_20\_00，含义：需要提前1天，且在20:00分之前才可预定那天的门票。若不传则表示不限制预定时间。0\_24\_00表示在当前的24点前预定都可以，等效于不限制预定时间。 |
| sku\_list | OBJECT\[\] | 非必填 | sku列表。新增商品时必填。整个sku\_list会作为整体更新。 |
| child\_skus | OBJECT\[\] | 非必填 | 仅当sku\_type为日历库存时入参。若父sku多于10个，需要通过pdd.goods.child.sku.edit接口分批维护。 |
| date | STRING | 非必填 | 日期。格式：2020-06-01。每个sku最多支持180天。 |
| group\_price | LONG | 非必填 | 拼团价，单位为分。 |
| quantity\_delta | LONG | 非必填 | 库存增减。比如传-10表示将对应的sku库存减10。 |
| single\_price | LONG | 非必填 | 单买价，单位为分。 |
| group\_price | LONG | 非必填 | 拼团价，单位为分。仅当sku\_type为普通库存时入参 |
| is\_onsale | INTEGER | 非必填 | 上架状态。0=已下架，1=已上架。新建sku时不传时表示上架。 |
| out\_sku\_sn | STRING | 非必填 | sku外部编码，同其他接口中的outer\_id 、out\_id、out\_sku\_sn、outer\_sku\_sn、out\_sku\_id、outer\_sku\_id 都为商家编码（sku维度）。 |
| quantity\_delta | LONG | 非必填 | 库存增减。仅当sku\_type为普通库存时入参。比如传-10表示将对应的sku库存减10。 |
| rule\_id | STRING | 非必填 | 调pdd.scenic.sku.rule.get得到的规则id。在发布成功后不可修改。 |
| single\_price | LONG | 非必填 | 单买价，单位为分。仅当sku\_type为普通库存时入参。 |
| sku\_id | LONG | 非必填 | 如果传值，则在原sku基础上进行编辑，如果传空，则新增sku |
| spec\_id\_list | LONG\[\] | 非必填 | 商品规格列表，从pdd.goods.cat.template.get中获取销售属性规格id后，再在pdd.goods.spec.id.get获取spec\_id。spec\_id需要和goods\_properties中的对应。对于多种规格，需要传每个规格的spec\_id的值，如\[20,5\]。在发布后不可修改。 |
| thumb\_url | STRING | 非必填 | SKU预览图。图片格式支持JPEG/JPG/PNG， 图片尺寸长宽比1：1且尺寸不低于480px，图片大小最高1MB。先通过pdd.goods.image.upload上传图片 |
| sku\_type | INTEGER | 非必填 | 销售方式，0=普通库存，1=日历库存。对于普通库存入参sku维度的价格库存，对于日历库存需要在pdd.goods.child.sku.edit入参child\_sku维度的价格库存后再提交。编辑商品时不允许修改。 |
| sync\_goods\_operate | INTEGER | 非必填 | 提交后上下架状态，0=上架；1=保持原样。表示编辑商品并提交后商品的上下架状态，不传时默认为0，上架。 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| goods\_upload\_response | OBJECT |  |  |
| goods\_commit\_id | LONG |  | 草稿id |
| goods\_id | LONG |  | 商品id |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketGoodsUploadRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddTicketGoodsUploadResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketGoodsUploadRequest.CarouselVideoItem;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketGoodsUploadRequest.GoodsPropertiesItem;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketGoodsUploadRequest.SkuListItem;
import com.pdd.pop.sdk.http.api.pop.request.PddTicketGoodsUploadRequest.SkuListItemChildSkusItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddTicketGoodsUploadRequest request = new PddTicketGoodsUploadRequest();
        List<String> carouselGallery = new ArrayList<String>();
        carouselGallery.add("str");
        request.setCarouselGallery(carouselGallery);
        List<CarouselVideoItem> carouselVideo = new ArrayList<CarouselVideoItem>();

        CarouselVideoItem item = new CarouselVideoItem();
        item.setFileId(0L);
        item.setVideoUrl("str");
        carouselVideo.add(item);
        request.setCarouselVideo(carouselVideo);
        request.setCatId(9088L);
        request.setCodeMode(1);
        List<String> detailGallery = new ArrayList<String>();
        detailGallery.add("str");
        request.setDetailGallery(detailGallery);
        request.setGoodsCommitId(1L);
        request.setGoodsDesc("str");
        request.setGoodsId(1L);
        request.setGoodsName("str");
        List<GoodsPropertiesItem> goodsProperties = new ArrayList<GoodsPropertiesItem>();

        GoodsPropertiesItem item1 = new GoodsPropertiesItem();
        item1.setParentSpecId(0L);
        item1.setRefPid(0L);
        item1.setSpecId(0L);
        item1.setValue("str");
        item1.setValueUnit("str");
        item1.setVid(0L);
        goodsProperties.add(item1);
        request.setGoodsProperties(goodsProperties);
        request.setIgnoreEditWarn(true);
        request.setIsSubmit(1);
        request.setMarketPrice(1L);
        request.setOutGoodsSn("str");
        request.setReserveLimitRule("str");
        List<SkuListItem> skuList = new ArrayList<SkuListItem>();

        SkuListItem item2 = new SkuListItem();
        List<SkuListItemChildSkusItem> childSkus = new ArrayList<SkuListItemChildSkusItem>();

        SkuListItemChildSkusItem item3 = new SkuListItemChildSkusItem();
        item3.setDate("str");
        item3.setGroupPrice(0L);
        item3.setQuantityDelta(0L);
        item3.setSinglePrice(0L);
        childSkus.add(item3);
        item2.setChildSkus(childSkus);
        item2.setGroupPrice(0L);
        item2.setIsOnsale(0);
        item2.setOutSkuSn("str");
        item2.setQuantityDelta(0L);
        item2.setRuleId("str");
        item2.setSinglePrice(0L);
        item2.setSkuId(0L);
        List<Long> specIdList = new ArrayList<Long>();
        specIdList.add(0L);
        item2.setSpecIdList(specIdList);
        item2.setThumbUrl("str");
        skuList.add(item2);
        request.setSkuList(skuList);
        request.setSkuType(1);
        request.setSyncGoodsOperate(1);
        PddTicketGoodsUploadResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "goods_upload_response": {
    "goods_commit_id": 0,
    "goods_id": 0
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
| 旅游门票商品管理权限包 |  |

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

### API工具
