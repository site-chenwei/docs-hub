---
title: "pdd.goods.spu.get - 标品详情接口"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.goods.spu.get"
menu_path:
  - "商品API"
  - "pdd.goods.spu.get"
captured_at: "2026-04-09T15:17:35.774Z"
---

# pdd.goods.spu.get

## 标品详情接口

更新时间：2020-09-27 22:12:42

¥免费API

必须用户授权

根据标品类目和关键属性获取标品详情信息，可以先通过pdd.goods.spu.search接口获取标品的类目及关键属性。

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
| cat\_id | STRING | 必填 | 标品所在的类目ID |
| key\_prop | OBJECT\[\] | 必填 | 关键属性 |
| ref\_pid | LONG | 非必填 | 引用属性ID |
| value\_unit | STRING | 非必填 | 属性值单位 |
| value | STRING | 非必填 | 关键属性值，和vid必须入参其一。 |
| vid | LONG | 非必填 | 关键属性值ID，和value必须入参其一。 |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| spu\_get\_response | OBJECT |  | 标品详情查询结果 |
| bind\_prop | OBJECT\[\] |  | 绑定属性，商品属性中对应的引用属性的属性值需要和绑定属性值相同。 |
| pname | STRING |  | 属性名 |
| ref\_pid | LONG |  | 引用属性ID |
| value\_unit | STRING |  | 属性值单位 |
| value | STRING |  | 属性值 |
| vid | LONG |  | 属性值ID |
| carousel\_gallery | STRING\[\] |  | 商品轮播图 |
| cat\_id | LONG |  | 标品所在的类目ID。若非叶子类目，表示该标品可用于该类目下的任何叶子类目。 |
| detail\_gallery | STRING\[\] |  | 商品详情图 |
| goods\_name | STRING |  | 商品标题 |
| key\_prop | OBJECT\[\] |  | 关键属性 |
| pname | STRING |  | 属性名 |
| ref\_pid | LONG |  | 引用属性id |
| value\_unit | STRING |  | 属性值单位 |
| value | STRING |  | 属性值 |
| vid | LONG |  | 属性值ID |
| pre\_title | STRING |  | 商品前缀标题，若有返回值，则表示发布该标品对应的商品时，商品标题的开头需要包含这部分字符串。 |
| sale\_prop | OBJECT\[\] |  | 销售属性，商品属性中对应的引用属性的属性值需要是销售属性值的子集。 |
| group\_id | INTEGER |  | 组ID |
| parent\_spec\_id | LONG |  | 父规格ID |
| pname | STRING |  | 属性名 |
| ref\_pid | LONG |  | 引用属性ID |
| spec\_id | LONG |  | 规格ID |
| value\_unit | STRING |  | 属性值单位 |
| value | STRING |  | 属性值 |
| vid | LONG |  | 属性值ID |
| spu\_name | STRING |  | 标品标题 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsSpuGetRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddGoodsSpuGetResponse;
import com.pdd.pop.sdk.http.api.pop.request.PddGoodsSpuGetRequest.KeyPropItem;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        String accessToken = "your accessToken";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddGoodsSpuGetRequest request = new PddGoodsSpuGetRequest();
        request.setCatId("str");
        List<KeyPropItem> keyProp = new ArrayList<KeyPropItem>();

        KeyPropItem item = new KeyPropItem();
        item.setRefPid(0L);
        item.setValueUnit("str");
        item.setValue("str");
        item.setVid(0L);
        keyProp.add(item);
        request.setKeyProp(keyProp);
        PddGoodsSpuGetResponse response = client.syncInvoke(request, accessToken);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "spu_get_response": {
    "bind_prop": [
      {
        "pname": "str",
        "ref_pid": 0,
        "value": "str",
        "value_unit": "str",
        "vid": 0
      }
    ],
    "carousel_gallery": [
      "str"
    ],
    "cat_id": 0,
    "detail_gallery": [
      "str"
    ],
    "goods_name": "str",
    "key_prop": [
      {
        "pname": "str",
        "ref_pid": 0,
        "value": "str",
        "value_unit": "str",
        "vid": 0
      }
    ],
    "pre_title": "str",
    "sale_prop": [
      {
        "group_id": 0,
        "parent_spec_id": 0,
        "pname": "str",
        "ref_pid": 0,
        "spec_id": 0,
        "value": "str",
        "value_unit": "str",
        "vid": 0
      }
    ],
    "spu_name": "str"
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

接口总限流频次：500次/1秒

### API工具
