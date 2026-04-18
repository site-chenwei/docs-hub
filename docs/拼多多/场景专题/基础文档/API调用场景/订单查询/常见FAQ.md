---
title: "常见FAQ"
source_url: "https://open.pinduoduo.com/application/document/browse?idStr=3155CCB725082A31"
menu_path:
  - "基础文档"
  - "API调用场景"
  - "订单查询"
  - "常见FAQ"
captured_at: "2026-04-10T09:21:19.580Z"
---

# 常见FAQ

更新时间：2025-03-17 22:28:20

**Q：漏单现象如何解决？**

A：平台优先推荐使用**订单同步系统**获取订单，该系统具备自动补偿机制防止漏单，同时能避免受接口限流影响，保障服务稳定。具体对接方案详见[《订单同步服务》](https://open.pinduoduo.com/application/document/browse?idStr=098A2CBA3F76DFAD)。

如仍选择通过增量查询接口获取订单，返回结果是根据订单的更新时间倒序返回的，建议从后往前翻页，以免出现翻页过程中订单变更而导致漏单。

具体操作方式为：

1.  首次调用入参use\_has\_next=false，获取订单总数后根据自身指定的page\_size计算得出总页数
    
2.  第二次调用开始入参use\_has\_next=true，page入参值从大到小，即从后往前翻页。
    

订单更新结束时间（end\_updated\_at）不得小于拼多多系统时间前3min（可通过[pdd.time.get](https://open.pinduoduo.com/application/document/api?id=pdd.time.get)接口校准）。每次增量查询的起始时间也建议适当前移几分钟，以免出现极个别情况下，系统数据延迟更新到数据库导致的漏单。

**Q：消息没有收到，如何确认是不是消息服务漏掉了？**

A：消息未收到可能为应用未获取店铺授权、未调用接口为店铺开通消息、消息推送后SDK已经ACK但是用户程序问题导致未获取（此情况需自查程序）

排查消息可以登录开放平台-控制台-应用详情页查看，

-   排查工具：店铺-消息订阅关系、消息推送状态
    
-   数据监控：消息长链链接状态
    
-   或通过如下方式排查确认：
    

1.  首先确认店铺授权access\_token是否有效；
    
2.  调用[pdd.pmc.user.get](https://open.pinduoduo.com/application/document/api?id=pdd.pmc.user.get)确认当前用户以及开通的消息；
    
3.  查看链接状态可用WsClient.isOnline()测试心跳是否正常连接。
    

若以上排查不出结果可以通过KNOCK咨询服务-开放平台小助手反馈确认：clientid、消息名称、订单号

**Q: pdd.order.information.get、pdd.order.list.get、pdd.order.number.list.increment.get 订单接口中收件人信息为什么都加密了？如何解密？**

A:为了提高数据安全，对从平台获取的订单敏感数据进行加密，请大家根据文档进行改造。

-   加密字段：包括但不限于 收件人的姓名、电话、收货地址等
    
-   涉及加密接口：[pdd.order.information.get](https://open.pinduoduo.com/application/document/api?id=pdd.order.information.get)、[pdd.order.list.get](https://open.pinduoduo.com/application/document/api?id=pdd.order.list.get)、[pdd.order.number.list.increment.get](https://open.pinduoduo.com/application/document/api?id=pdd.order.number.list.increment.get)
    
-   解密方式：接口直接将加密字段，以密文形式返回，服务商/商家需要在多多云内通过解密接口，获取明文信息。（注：每日解密次数有上限，上限以店铺纬度限制）
    

在多多云内可通过调用[pdd.open.decrypt.batch](https://open.pinduoduo.com/application/document/api?id=pdd.open.decrypt.batch)批量数据解密接口获取明文信息（附：[《多多云对接指南》](https://open.pinduoduo.com/paas/guide)）

-   涉及业务范围：
    

订单列表打码改造、订单敏感数据展示改造、订单收件人查询、电子面单的获取改造、订单合单业务改造、WMS仓储下发业务改造、修改收件人信息改造、ERP登录会话信息改造、前端解密接入风控

详细改造方案可参考-[【文档中心/基础文档/安全保障】](https://open.pinduoduo.com/application/document/browse?idStr=7B7498F731A92F3E)：

-   [《订单类接入方案》](https://open.pinduoduo.com/application/document/browse?idStr=242268D94F9434F4)
    
-   [《企业ERP接入方案》](https://open.pinduoduo.com/application/document/browse?idStr=E2F933436A7C7C5F)
    
-   [《商家自研接入方案》](https://open.pinduoduo.com/application/document/browse?idStr=57AB0E5D4B3EE6FD)
    

如有疑问请通过KNOCK咨询服务-开放平台小助手沟通确认。

**Q：订单接口获取到订单数据，但是收件人信息为空，什么原因？**

A：收件人信息在已发货、已退款、审核中等情况隐藏，详见公告及文档说明：

[《开放平台收件人地址信息改造通知》](https://open.pinduoduo.com/application/document/announcement?id=71)

[《关于拼多多订单接口调整通知》](https://open.pinduoduo.com/application/document/announcement?id=87)

[《审核订单说明》](https://open.pinduoduo.com/application/document/browse?idStr=697D8F2EC5A48FEA)

注：收件人信息请在订单待发货状态获取后密文保存

**Q：订单接口的支付方式字段pay\_type、支付单号字段pay\_no、支付申报订单号 inner\_transaction\_id返回为空，是什么原因？**

A：非多多国际商家支付方式、支付单号、支付申报订单号等字段隐藏，详情参见开放平台2020-04-01公告[《关于拼多多订单接口调整通知》](https://open.pinduoduo.com/application/document/announcement?id=78)

多多国际店铺可使用[pdd.oversea.clearance.get](https://open.pinduoduo.com/application/document/api?id=pdd.oversea.clearance.get)接口获取多多国际清关材料

**Q: 订单接口中step\_discount\_amount 膨胀金额 单位：元 是什么？**

A：定金单会有膨胀金额，例如设置定金10元可当50元使用，50-10=40，膨胀金额即为40。

**Q: 订单商品金额减去折扣金额后依然与支付金额不一致？**

A：商家可能为促使成交在店铺后台操作过改价处理，请查看接口文档中金额字段的描述，目前改价金额可从order\_change\_amount字段获取。

**Q: 消息推送和多多云订单同步服务哪个优先级高，会不会出现有已有消息推送，但是云内订单同步未收到的情况？**

A：可能出现这个情况，消息推送和云内订单同步服务是两个获取订单的路径，两个推送无先后关系；入云对接订单同步服务后可不使用网关消息推送，或只做备用。

**Q：订单查询接口，根据订单编号无法查询到相关订单信息，提示"订单不属于当前店铺或订单不存在"。**

A: 可能存在的原因如下：

1.  可能调用接口入参的access\_token并不属于该订单所在店铺，请自行排查或重新授权获取access\_token以确保是该店铺的，再调用接口。
    
2.  如果是消息推送获取的订单号，请延后10min调用接口；接口比消息推送略有延迟
    
3.  接口可查以往订单至多90天以内
    
4.  订单号录错
