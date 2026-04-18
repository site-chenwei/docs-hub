---
title: "API调用指南"
doc_key: "article.api_call"
source_kind: "article_id"
source_value: "8EC06C399636041E"
source_url: "https://open.pinduoduo.com/application/document/browse?idStr=8EC06C399636041E"
category:
  - "平台接入"
  - "开发文档"
app_types:
  - "商品优化分析"
  - "订单处理"
domain_tags:
  - "API调用"
  - "签名"
  - "请求规范"
priority: "P0"
depends_on:
captured_at: "2026-04-10T08:53:36.490Z"
---

# API调用指南

拼多多开放平台开放API基于http协议实现接口调用，已入驻开放平台开发者（ISV）可以按如下步骤实现请求，完成接口调用，以下调用指南针对开发者自行实现API调用，如您需要快速接入，可使用SDK快速实现，详情可参考[SDK调用指南](https://open.pinduoduo.com/application/document/browse?idStr=7E28519022C8E799)。

#### **调用流程**

拼多多开放平台API调用过程有以下步骤：

- 参数准备：了解您所要调用的API入参业务参数及系统参数
- 签名准备：系统参数sign（签名）的生成，需要使用所有参数参与签名过程
- 入参组装：组装入参请求结构体，完成请求前置所有动作
- 发起请求：发起API请求至指定接口地址
- 解析请求：对返回结构体进行解析，完成调用过程

![图片](https://testimg.yangkeduo.com/perse-open-api/2020-04-16/020d1eb7-50ef-4bec-9edd-c137617cf409.png)（拼多多开放平台API调用流程示意图）

#### 请求地址

所有开放平台开放API请求地址统一为：

| 环境 | http地址（已不允许调用） | https地址 |
| --- | --- | --- |
| 正式环境 | ~~http://gw-api.pinduoduo.com/api/router~~ | https://gw-api.pinduoduo.com/api/router |

#### **公共参数**

公共参数是指调用任何拼多多开放平台API均必须传入的参数，目前公共参数有以下：

| 参数名称 | 参数类型 | 是否必须 | 参数描述 |
| --- | --- | --- | --- |
| type | string | 是 | API接口名，形如：pdd.* |
| client_id | string | 是 | 已创建成功的应用标志client_id，可在应用详情和中查看 |
| timestamp | string | 是 | 时间戳，格式为UNIX时间（秒） |
| sign | string | 是 | API入参参数签名，签名值根据如下算法给出计算过程 |
| data_type | string | 否 | 请求返回的数据格式，可选参数为XML或JSON，默认为JSON |
| access_token | string | 否 | 用户授权令牌access_token，通过[pdd.pop.auth.token.create](https://open.pinduoduo.com/application/document/api?id=pdd.pop.auth.token.create)获取 |
| version | string | 否 | API版本，默认为V1，无要求不传此参数 |

#### **业务参数**

API调用除了必须包含公共参数外，如果API本身有业务级的参数也必须传入，各个API的业务级参数请考API文档详细描述说明。

#### **签名算法**

为了防止API调用过程中被恶意篡改，调用任何一个API都需要携带请求签名，开放平台服务端会根据请求参数，对签名进行验证，并对签名不合法的请求将会被拒绝。

目前支持的签名算法为：MD5(sign_method=md5)，签名过程如下：

- 本次请求中所有请求参数（包含公共参数与业务参数）进行首字母以ASCII方式升序排列（ASCII ASC），对于相同字母则使用下个字母做二次排序，字母序为从左到右，以此类推
- 排序后的结果按照参数名（key）参数值（value）的次序进行字符串拼接，拼接处不包含任何字符
- 拼接完成的字符串做进一步拼接成1个字符串（包含所有kv字符串的长串），并在该长串的头部及尾部分别拼接client_secret，完成签名字符串的组装
- 最后对签名字符串，使用MD5算法加密后，得到的MD5加密密文后转为大写，即为sign值

#### 调用示例

> 输入参数示例

```txt
array (
'access_token' => 'asd78172s8ds9a921j9qqwda12312w1w21211'
'client_id' =>1,
'data_type => 'XML',
'type'=> 'pdd.order.number.list.get',
'timestamp' => '1480411125',
'order_status' => '1',
'page' => '1',
'page_size' => '10'
)
```

> 按首字母升序排列（ASCII ASC）

```txt
array (
'access_token' => 'asd78172s8ds9a921j9qqwda12312w1w21211'
'client_id' =>1,
'data_type => 'XML',
'order_status' => '1',
'page' => '1',
'page_size ' => '10',
'timestamp' => '1480411125',
'type'=> 'pdd.order.number.list.get',
)
```

无缝拼接字符串，拼接完成后在头部以及尾部额外拼接上client_secret，假设client_secret为testSecret，则示例签名字符串如下：

```txt
testSecretaccess_tokenasd78172s8ds9a921j9qqwda12312w1w21211client_id1data_typeXMLorder_status1page1page_size10timestamp1480411125typepdd.order.number.list.gettestSecret
```

> 生成签名sign

```txt
UPPER_CASE(MD5(testSecretaccess_tokenasd78172s8ds9a921j9qqwda12312w1w21211client_id1data_typeXMLorder_status1page1page_size10timestamp1480411125typepdd.order.number.list.gettestSecret)) => E4DE3ED21002510DED352819E7AE6775
```

> 发起发起API请求（以JSON数据格式请求为例）

请求method：

```txt
POST
```

请求url：

```txt
https://gw-api.pinduoduo.com/api/router
```

请求header：

```txt
content-type: application/json
```

请求body：

```json
{
    "type": "pdd.order.number.list.get",
    "sign": "E4DE3ED21002510DED352819E7AE6775",
    "client_id": "1",
    "page": 1,
    "page_size": 10,
    "data_type": "XML",
    "timestamp": 1480411125,
    "order_status": 1,
    "access_token": "asd78172s8ds9a921j9qqwda12312w1w21211"
}
```

#### **注意事项**

- 所有的请求和响应数据编码皆为utf-8格式，url里的所有参数值请做urlencode编码。如果请求的content-type是 application/x-www-form-urlencoded，所有参数值也做urlencode编码；如果是multipart/form-data格式，每个表单字段的参数值无需编码，但每个表单字段的charset需要指定为utf-8
- 如果指定接口返回数据格式为JSON，请指明header头content-type: application/json
