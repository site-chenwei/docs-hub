---
title: "pdd.ddk.cms.prom.url.generate - 生成商城-频道推广链接"
source_url: "https://open.pinduoduo.com/application/document/api?id=pdd.ddk.cms.prom.url.generate"
menu_path:
  - "多多客API"
  - "pdd.ddk.cms.prom.url.generate"
captured_at: "2026-04-09T15:18:51.173Z"
---

# pdd.ddk.cms.prom.url.generate

## 生成商城-频道推广链接

更新时间：2024-09-14 11:38:52

¥免费API

不需用户授权

生成商城推广链接接口

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
| channel\_type | INTEGER | 非必填 | 0, "1.9包邮"；1, "今日爆款"； 2, "品牌清仓"； 4,"PC端专属商城(已下线，会生成默认商城链接)"；7，"跨境商城"; 不传值为默认商城 |
| country\_region\_code | INTEGER | 非必填 | 国家和地区代码，生成跨境商城时有效 |
| custom\_parameters | STRING | 非必填 | 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 用户唯一标识，可自行加密后传入，每个用户仅且对应一个标识，必填； sid 上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key。（如果使用GET请求，请使用URLEncode处理参数） |
| generate\_mobile | BOOLEAN | 非必填 | 是否生成手机跳转链接。true-是，false-否，默认false |
| generate\_schema\_url | BOOLEAN | 非必填 | 是否返回 schema URL |
| generate\_short\_url | BOOLEAN | 非必填 | 是否生成短链接，true-是，false-否 |
| generate\_we\_app | BOOLEAN | 非必填 | 是否生成拼多多福利券微信小程序推广信息 |
| keyword | STRING | 非必填 | 搜索关键词 |
| language\_code | STRING | 非必填 | 语言代码，生成跨境商城时有效 |
| multi\_group | BOOLEAN | 非必填 | 单人团多人团标志。true-多人团，false-单人团 默认false |
| p\_id\_list | STRING\[\] | 必填 | 推广位列表，例如：\["60005\_612"\] |

### 返回参数说明

| 参数接口 | 参数类型 | 例子 | 说明 |
| --- | --- | --- | --- |
| cms\_promotion\_url\_generate\_response | OBJECT |  | 商城推广链接返回对象 |
| total | INTEGER | 100 | total |
| url\_list | OBJECT\[\] |  | 链接列表 |
| mobile\_short\_url | STRING |  | 推广移动短链接，对应出参mobile\_url的短链接，与mobile\_url功能一致。 |
| mobile\_url | STRING |  | 推广移动链接，用户安装拼多多APP的情况下会唤起APP，否则唤起H5页面 |
| multi\_group\_mobile\_short\_url | STRING |  | 多人团推广移动短链接，对应出参multi\_group\_mobile\_url的短链接，与multi\_group\_mobile\_url功能一致。 |
| multi\_group\_mobile\_url | STRING |  | 多人团推广移动链接，用户安装拼多多APP的情况下会唤起APP，否则唤起H5页面 |
| multi\_group\_short\_url | STRING |  | 对应出参multi\_group\_url的短链接，与multi\_group\_url功能一致。 |
| multi\_group\_url | STRING |  | 多人团长链接，唤起H5页面 |
| multi\_url\_list | OBJECT |  | 双人团链接列表 |
| mobile\_short\_url | STRING |  | 双人团推广移动短链接，对应出参mobile\_url的短链接，与mobile\_url功能一致。 |
| mobile\_url | STRING |  | 双人团推广移动链接，用户安装拼多多APP的情况下会唤起APP，否则唤起H5页面 |
| schema\_url | STRING |  | schema链接，用户安装拼多多APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| short\_url | STRING |  | 双人团短链接，对应出参url的短链接，与url功能一致。 |
| tz\_schema\_url | STRING |  | 使用此推广链接，用户安装多多团长APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| url | STRING |  | 双人团长链接，唤起H5页面 |
| short\_url | STRING |  | h5短链接 |
| sign | STRING | CM1891891\_26364337\_0c06f43f39cc6829be275d7067c31db5 | CPSsign |
| single\_url\_list | OBJECT |  | 单人团链接列表 |
| mobile\_short\_url | STRING |  | 推广移动短链接，对应出参mobile\_url的短链接，与mobile\_url功能一致。 |
| mobile\_url | STRING |  | 推广移动链接，用户安装拼多多APP的情况下会唤起APP，否则唤起H5页面 |
| schema\_url | STRING |  | schema链接，用户安装拼多多APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| short\_url | STRING |  | 推广短链接，对应出参url的短链接，与url功能一致。 |
| tz\_schema\_url | STRING |  | 使用此推广链接，用户安装多多团长APP的情况下会唤起APP（需客户端支持schema跳转协议） |
| url | STRING |  | 推广长链接，唤起H5页面 |
| url | STRING |  | 推广长链接，唤起H5页面 |
| we\_app\_info | OBJECT |  | 拼多多福利券微信小程序信息 |
| app\_id | STRING |  | 小程序id |
| banner\_url | STRING |  | Banner图 |
| desc | STRING |  | 描述 |
| page\_path | STRING |  | 小程序path值 |
| source\_display\_name | STRING |  | 来源名 |
| title | STRING |  | 小程序标题 |
| user\_name | STRING |  | 用户名 |
| we\_app\_icon\_url | STRING |  | 小程序图片 |

### 请求示例

JAVA

CURL

```
package com.pdd.pop.sdk.http.demo;

import com.pdd.pop.sdk.common.util.JsonUtil;
import com.pdd.pop.sdk.http.api.pop.request.PddDdkCmsPromUrlGenerateRequest;
import com.pdd.pop.sdk.http.api.pop.response.PddDdkCmsPromUrlGenerateResponse;
import com.pdd.pop.sdk.http.PopClient;
import com.pdd.pop.sdk.http.PopHttpClient;

import java.util.*;

public class PopClientDemo {

    public static void main(String[] args) throws Exception {

        String clientId = "your clientId";
        String clientSecret = "your clientSecret";
        PopClient client = new PopHttpClient(clientId, clientSecret);

        PddDdkCmsPromUrlGenerateRequest request = new PddDdkCmsPromUrlGenerateRequest();
        request.setChannelType(0);
        request.setCountryRegionCode(1);
        request.setCustomParameters("str");
        request.setGenerateMobile(true);
        request.setGenerateSchemaUrl(false);
        request.setGenerateShortUrl(true);
        request.setGenerateWeApp(true);
        request.setKeyword("str");
        request.setLanguageCode("str");
        request.setMultiGroup(true);
        List<String> pIdList = new ArrayList<String>();
        pIdList.add("str");
        request.setPIdList(pIdList);
        PddDdkCmsPromUrlGenerateResponse response = client.syncInvoke(request);
        System.out.println(JsonUtil.transferToJson(response));
    }
}
```

### 响应示例

```
{
  "cms_promotion_url_generate_response": {
    "total": 100,
    "url_list": [
      {
        "mobile_short_url": "str",
        "mobile_url": "str",
        "multi_group_mobile_short_url": "str",
        "multi_group_mobile_url": "str",
        "multi_group_short_url": "str",
        "multi_group_url": "str",
        "multi_url_list": {
          "mobile_short_url": "str",
          "mobile_url": "str",
          "schema_url": "str",
          "short_url": "str",
          "tz_schema_url": "str",
          "url": "str"
        },
        "short_url": "str",
        "sign": "CM1891891_26364337_0c06f43f39cc6829be275d7067c31db5",
        "single_url_list": {
          "mobile_short_url": "str",
          "mobile_url": "str",
          "schema_url": "str",
          "short_url": "str",
          "tz_schema_url": "str",
          "url": "str"
        },
        "url": "str",
        "we_app_info": {
          "app_id": "str",
          "banner_url": "str",
          "desc": "str",
          "page_path": "str",
          "source_display_name": "str",
          "title": "str",
          "user_name": "str",
          "we_app_icon_url": "str"
        }
      }
    ]
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
| 多多客权限包 | 多多客联盟 |
| 多多客 |  |

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

接口总限流频次：16750次/10秒

### API工具
