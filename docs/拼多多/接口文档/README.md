# 接口文档

## 归类说明
- 本页收口全部 `*API` 目录，统一迁入当前目录，并按业务域做统一浏览入口。
- 接口文档共 288 篇，覆盖 27 个 API 域目录。
- 本轮已将根目录遗留的 19 篇未归类 API 文档归档到对应业务域目录。
- 场景说明类文章不放在本页，统一归到 `场景专题.md`。

## 业务域总览
| 业务域 | API 域目录 | 文档数 |
| --- | --- | --- |
| 商品与店铺 | 商品API、店铺API、门店API、自媒体API | 78 |
| 订单与售后 | 订单API、售后API、发票服务API、财务API、方舟数据传输API | 50 |
| 物流与仓配 | 物流API、仓储API、商家寄件API、电子面单API、电子面单代打API | 59 |
| 营销与流量 | 营销API、多多客API、多多客工具API、视频推荐API | 55 |
| 平台能力与生态 | 消息服务API、安全与会话API、服务市场API、短信服务API、短信供应商API | 18 |
| 垂直行业与专项 | 卡券API、虚拟类目API、旅游门票API、多多国际API | 28 |

## 完整索引

### 商品与店铺（78）

#### 商品API（57）
- [pdd.delete.draft.commit - 删除草稿接口](./商品API/pdd.delete.draft.commit-删除草稿接口.md)
- [pdd.delete.goods.commit - 删除商品接口](./商品API/pdd.delete.goods.commit-删除商品接口.md)
- [pdd.goods.add - 商品新增接口](./商品API/pdd.goods.add-商品新增接口.md)
- [pdd.goods.authorization.cats - 获取当前授权商家可发布的商品类目信息](./商品API/pdd.goods.authorization.cats-获取当前授权商家可发布的商品类目信息.md)
- [pdd.goods.cat.rule.get - 类目商品发布规则查询接口](./商品API/pdd.goods.cat.rule.get-类目商品发布规则查询接口.md)
- [pdd.goods.cat.template.get - 获取商品类目属性(已废弃)](<./商品API/pdd.goods.cat.template.get-获取商品类目属性(已废弃).md>)
- [pdd.goods.cats.get - 商品标准类目接口](./商品API/pdd.goods.cats.get-商品标准类目接口.md)
- [pdd.goods.child.sku.edit - 日历库存子SKU新增及编辑接口](./商品API/pdd.goods.child.sku.edit-日历库存子SKU新增及编辑接口.md)
- [pdd.goods.commit.detail.get - 获取商品提交的商品详情](./商品API/pdd.goods.commit.detail.get-获取商品提交的商品详情.md)
- [pdd.goods.commit.list.get - 草稿列表接口](./商品API/pdd.goods.commit.list.get-草稿列表接口.md)
- [pdd.goods.commit.status.get - 草稿状态查询接口](./商品API/pdd.goods.commit.status.get-草稿状态查询接口.md)
- [pdd.goods.country.get - 商品地区/国家接口](./商品API/pdd.goods.country.get-商品地区-国家接口.md)
- [pdd.goods.cps.mall.unit.change - 修改全店推广API](./商品API/pdd.goods.cps.mall.unit.change-修改全店推广API.md)
- [pdd.goods.cps.mall.unit.query - 查询全店推广API](./商品API/pdd.goods.cps.mall.unit.query-查询全店推广API.md)
- [pdd.goods.cps.unit.change - 修改商品推广API](./商品API/pdd.goods.cps.unit.change-修改商品推广API.md)
- [pdd.goods.cps.unit.create - 设置单品推广API](./商品API/pdd.goods.cps.unit.create-设置单品推广API.md)
- [pdd.goods.cps.unit.delete - 删除单品计划接口](./商品API/pdd.goods.cps.unit.delete-删除单品计划接口.md)
- [pdd.goods.cps.unit.query - 查询商品推广API](./商品API/pdd.goods.cps.unit.query-查询商品推广API.md)
- [pdd.cloud.goods.detail.get - 商品明细(方舟)](./商品API/pdd.cloud.goods.detail.get-商品明细(方舟).md)
- [pdd.goods.detail.get - 商品明细](./商品API/pdd.goods.detail.get-商品明细.md)
- [pdd.goods.edit.goods.commit - 新增或编辑草稿接口](./商品API/pdd.goods.edit.goods.commit-新增或编辑草稿接口.md)
- [pdd.goods.file.info.get - 文件详情查询](./商品API/pdd.goods.file.info.get-文件详情查询.md)
- [pdd.goods.filespace.image.upload - 图片上传到图片空间](./商品API/pdd.goods.filespace.image.upload-图片上传到图片空间.md)
- [pdd.goods.get.relation - 商品映射查询接口](./商品API/pdd.goods.get.relation-商品映射查询接口.md)
- [pdd.goods.image.upload - 商品图片上传接口](./商品API/pdd.goods.image.upload-商品图片上传接口.md)
- [pdd.goods.img.upload - 商品图片上传接口](./商品API/pdd.goods.img.upload-商品图片上传接口.md)
- [pdd.goods.information.get - 商品详情接口](./商品API/pdd.goods.information.get-商品详情接口.md)
- [pdd.goods.information.update - 商品编辑](./商品API/pdd.goods.information.update-商品编辑.md)
- [pdd.goods.latest.commit.status.get - 批量goodsId查询最新的审核状态](./商品API/pdd.goods.latest.commit.status.get-批量goodsId查询最新的审核状态.md)
- [pdd.cloud.goods.list.get - 商品列表接口（方舟）](./商品API/pdd.cloud.goods.list.get-商品列表接口（方舟）.md)
- [pdd.goods.list.get - 商品列表接口](./商品API/pdd.goods.list.get-商品列表接口.md)
- [pdd.goods.logistics.ser.template.detail - 商品送装服务模版详情](./商品API/pdd.goods.logistics.ser.template.detail-商品送装服务模版详情.md)
- [pdd.goods.logistics.ser.template.list - 商品送装服务模版列表](./商品API/pdd.goods.logistics.ser.template.list-商品送装服务模版列表.md)
- [pdd.goods.logistics.template.create - 创建商品物流模版](./商品API/pdd.goods.logistics.template.create-创建商品物流模版.md)
- [pdd.goods.logistics.template.get - 商品运费模版接口](./商品API/pdd.goods.logistics.template.get-商品运费模版接口.md)
- [pdd.goods.material.create - 商品素材创建接口](./商品API/pdd.goods.material.create-商品素材创建接口.md)
- [pdd.goods.material.delete - 商品素材删除接口](./商品API/pdd.goods.material.delete-商品素材删除接口.md)
- [pdd.goods.material.query - 商品素材列表查询](./商品API/pdd.goods.material.query-商品素材列表查询.md)
- [pdd.goods.opt.get - 查询商品标签列表](./商品API/pdd.goods.opt.get-查询商品标签列表.md)
- [pdd.goods.outer.cat.mapping.get - 类目预测接口](./商品API/pdd.goods.outer.cat.mapping.get-类目预测接口.md)
- [pdd.goods.price.check - 商品价格核实](./商品API/pdd.goods.price.check-商品价格核实.md)
- [pdd.goods.quantity.update - 商品库存更新接口](./商品API/pdd.goods.quantity.update-商品库存更新接口.md)
- [pdd.goods.sale.status.set - 商品上架状态设置](./商品API/pdd.goods.sale.status.set-商品上架状态设置.md)
- [pdd.goods.sizespec.class.get - 尺码表分类查询](./商品API/pdd.goods.sizespec.class.get-尺码表分类查询.md)
- [pdd.goods.sizespec.meta.get - 尺码组和尺码参数查询](./商品API/pdd.goods.sizespec.meta.get-尺码组和尺码参数查询.md)
- [pdd.goods.sizespec.templates.get - 自定义尺码表模版列表](./商品API/pdd.goods.sizespec.templates.get-自定义尺码表模版列表.md)
- [pdd.goods.sku.price.update - 修改商品sku价格](./商品API/pdd.goods.sku.price.update-修改商品sku价格.md)
- [pdd.goods.skus.get - 根据skuId查询sku详情](./商品API/pdd.goods.skus.get-根据skuId查询sku详情.md)
- [pdd.goods.spec.get - 商品属性类目接口](./商品API/pdd.goods.spec.get-商品属性类目接口.md)
- [pdd.goods.spec.id.get - 生成商家自定义的规格](./商品API/pdd.goods.spec.id.get-生成商家自定义的规格.md)
- [pdd.goods.spu.get - 标品详情接口](./商品API/pdd.goods.spu.get-标品详情接口.md)
- [pdd.goods.spu.search - 标品搜索接口](./商品API/pdd.goods.spu.search-标品搜索接口.md)
- [pdd.goods.submit.goods.commit - 编辑并提交草稿接口](./商品API/pdd.goods.submit.goods.commit-编辑并提交草稿接口.md)
- [pdd.goods.template.property.value.search - 模板属性值搜索接口](./商品API/pdd.goods.template.property.value.search-模板属性值搜索接口.md)
- [pdd.goods.video.upload - 商品视频上传接口](./商品API/pdd.goods.video.upload-商品视频上传接口.md)
- [pdd.gooods.sku.measurement.list - 商品sku计量单位枚举](./商品API/pdd.gooods.sku.measurement.list-商品sku计量单位枚举.md)
- [pdd.one.express.cost.template - 按id获取商品运费模版接口](./商品API/pdd.one.express.cost.template-按id获取商品运费模版接口.md)

#### 店铺API（7）
- [pdd.mall.cps.protocol.status.query - 查询店铺是否签署多多进宝协议接口](./店铺API/pdd.mall.cps.protocol.status.query-查询店铺是否签署多多进宝协议接口.md)
- [pdd.cloud.mall.info.get - 店铺信息接口(方舟)](./店铺API/pdd.cloud.mall.info.get-店铺信息接口(方舟).md)
- [pdd.mall.info.get - 店铺信息接口](./店铺API/pdd.mall.info.get-店铺信息接口.md)
- [pdd.mall.notification.type.show.check - 判断是否对商家展示某个通知](./店铺API/pdd.mall.notification.type.show.check-判断是否对商家展示某个通知.md)
- [pdd.trace.source.query.goods.info - 根据防伪码ID获取溯源商品信息](./店铺API/pdd.trace.source.query.goods.info-根据防伪码ID获取溯源商品信息.md)
- [pdd.trace.source.upload.code.info - 溯源服务商上传溯源码信息](./店铺API/pdd.trace.source.upload.code.info-溯源服务商上传溯源码信息.md)
- [pdd.trace.source.upload.plan.info - 溯源服务商上传正品溯源粘贴计划](./店铺API/pdd.trace.source.upload.plan.info-溯源服务商上传正品溯源粘贴计划.md)

#### 门店API（8）
- [pdd.mall.info.group.add.store.post - 门店组添加门店](./门店API/pdd.mall.info.group.add.store.post-门店组添加门店.md)
- [pdd.mall.info.group.list.store.get - 查询门店组下门店](./门店API/pdd.mall.info.group.list.store.get-查询门店组下门店.md)
- [pdd.mall.info.group.query.post - 查询店铺下门店组列表](./门店API/pdd.mall.info.group.query.post-查询店铺下门店组列表.md)
- [pdd.mall.info.group.remove.store.get - 门店组删除门店](./门店API/pdd.mall.info.group.remove.store.get-门店组删除门店.md)
- [pdd.mall.info.store.create.post.nopoi - 开放平台无PoiId创建门店](./门店API/pdd.mall.info.store.create.post.nopoi-开放平台无PoiId创建门店.md)
- [pdd.mall.info.store.get - 开放平台查询门店信息](./门店API/pdd.mall.info.store.get-开放平台查询门店信息.md)
- [pdd.mall.info.store.update.post.nopoi - 开放平台无PoiId编辑门店](./门店API/pdd.mall.info.store.update.post.nopoi-开放平台无PoiId编辑门店.md)
- [pdd.qrpay.payee.register - 交易二维码-参数注册接口](./门店API/pdd.qrpay.payee.register-交易二维码-参数注册接口.md)

#### 自媒体API（6）
- [pdd.live.img.mall.upload - 多多视频商家上传图片接口](./自媒体API/pdd.live.img.mall.upload-多多视频商家上传图片接口.md)
- [pdd.live.video.mall.create - 多多视频商家发布视频](./自媒体API/pdd.live.video.mall.create-多多视频商家发布视频.md)
- [pdd.live.video.mall.querymallvideoauditstatus - 查询商家视频的审核状态](./自媒体API/pdd.live.video.mall.querymallvideoauditstatus-查询商家视频的审核状态.md)
- [pdd.live.video.mall.upload.part - 多多视频商家上传视频分片上传接口](./自媒体API/pdd.live.video.mall.upload.part-多多视频商家上传视频分片上传接口.md)
- [pdd.live.video.mall.upload.part.complete - 多多视频商家上传视频分片完成接口](./自媒体API/pdd.live.video.mall.upload.part.complete-多多视频商家上传视频分片完成接口.md)
- [pdd.live.video.mall.upload.part.init - 多多视频商家上传视频分片初始化接口](./自媒体API/pdd.live.video.mall.upload.part.init-多多视频商家上传视频分片初始化接口.md)

### 订单与售后（50）

#### 订单API（26）
- [pdd.erp.order.sync - erp打单信息同步](./订单API/pdd.erp.order.sync-erp打单信息同步.md)
- [pdd.mille.query.buy.order.split.bill.amount - 查询采购单预计分账金额](./订单API/pdd.mille.query.buy.order.split.bill.amount-查询采购单预计分账金额.md)
- [pdd.order.account.attachment.upload - 政府补贴订单台账附件上传接口](./订单API/pdd.order.account.attachment.upload-政府补贴订单台账附件上传接口.md)
- [pdd.order.basic.list.get - 订单基础信息列表查询接口（根据成交时间）](./订单API/pdd.order.basic.list.get-订单基础信息列表查询接口（根据成交时间）.md)
- [pdd.order.information.get - 订单详情](./订单API/pdd.order.information.get-订单详情.md)
- [pdd.order.list.get - 订单列表查询接口（根据成交时间）](./订单API/pdd.order.list.get-订单列表查询接口（根据成交时间）.md)
- [pdd.order.merge.ship.order.group - 合并发货订单分组](./订单API/pdd.order.merge.ship.order.group-合并发货订单分组.md)
- [pdd.order.note.update - 编辑商家订单备注](./订单API/pdd.order.note.update-编辑商家订单备注.md)
- [pdd.order.number.list.increment.get - 订单增量接口](./订单API/pdd.order.number.list.increment.get-订单增量接口.md)
- [pdd.order.promise.info.get - 查询订单承诺信息](./订单API/pdd.order.promise.info.get-查询订单承诺信息.md)
- [pdd.order.promotion.get - 获取订单优惠明细数据](./订单API/pdd.order.promotion.get-获取订单优惠明细数据.md)
- [pdd.order.review.info - 订单审核信息查询接口](./订单API/pdd.order.review.info-订单审核信息查询接口.md)
- [pdd.order.search.order - 订单检索接口](./订单API/pdd.order.search.order-订单检索接口.md)
- [pdd.order.service.benefit.update - 服务权益单更新接口](./订单API/pdd.order.service.benefit.update-服务权益单更新接口.md)
- [pdd.order.specific.order.information.get - 特定类型订单查询接口](./订单API/pdd.order.specific.order.information.get-特定类型订单查询接口.md)
- [pdd.order.status.get - 订单状态](./订单API/pdd.order.status.get-订单状态.md)
- [pdd.order.submall.information.get - 以旧换新国补订单详情分店铺查询接口](./订单API/pdd.order.submall.information.get-以旧换新国补订单详情分店铺查询接口.md)
- [pdd.order.submall.list.get - 以旧换新国补订单列表分店铺查询接口（根据成交时间）](./订单API/pdd.order.submall.list.get-以旧换新国补订单列表分店铺查询接口（根据成交时间）.md)
- [pdd.order.tradein.info - 订单政府补贴信息查询接口](./订单API/pdd.order.tradein.info-订单政府补贴信息查询接口.md)
- [pdd.order.tradein.post.sn - 上传国补订单的sn码](./订单API/pdd.order.tradein.post.sn-上传国补订单的sn码.md)
- [pdd.order.update.address - 修改订单收件地址接口](./订单API/pdd.order.update.address-修改订单收件地址接口.md)
- [pdd.order.upload.delivery.feature - 订单发货内容信息上传](./订单API/pdd.order.upload.delivery.feature-订单发货内容信息上传.md)
- [pdd.order.upload.extra.logistics - 订单额外运单信息上传](./订单API/pdd.order.upload.extra.logistics-订单额外运单信息上传.md)
- [pdd.order.upload.relation.logistics - 订单关联运单信息上传](./订单API/pdd.order.upload.relation.logistics-订单关联运单信息上传.md)
- [pdd.order.virtual.information.get - 虚拟业务信息查询接口](./订单API/pdd.order.virtual.information.get-虚拟业务信息查询接口.md)
- [pdd.survey.query.special.survey - 根据订单号查询调查问卷和答案](./订单API/pdd.survey.query.special.survey-根据订单号查询调查问卷和答案.md)

#### 售后API（13）
- [pdd.nextone.logistics.warehouse.update - 退货入库](./售后API/pdd.nextone.logistics.warehouse.update-退货入库.md)
- [pdd.rdc.pddgenius.sendgoods.cancel - 取消发货](./售后API/pdd.rdc.pddgenius.sendgoods.cancel-取消发货.md)
- [pdd.cloud.refund.address.list.get - 获取商家退货地址库(方舟)](./售后API/pdd.cloud.refund.address.list.get-获取商家退货地址库(方舟).md)
- [pdd.refund.address.list.get - 获取商家退货地址库](./售后API/pdd.refund.address.list.get-获取商家退货地址库.md)
- [pdd.refund.agree - 同意退款](./售后API/pdd.refund.agree-同意退款.md)
- [pdd.refund.exchange.shipping - 商家换货发货](./售后API/pdd.refund.exchange.shipping-商家换货发货.md)
- [pdd.refund.images.get - 用户申请售后时提交的图片凭证](./售后API/pdd.refund.images.get-用户申请售后时提交的图片凭证.md)
- [pdd.cloud.refund.information.get - 售后单详情接口(方舟)](./售后API/pdd.cloud.refund.information.get-售后单详情接口(方舟).md)
- [pdd.refund.information.get - 售后单详情接口](./售后API/pdd.refund.information.get-售后单详情接口.md)
- [pdd.cloud.refund.list.increment.get - 售后列表接口（方舟）](./售后API/pdd.cloud.refund.list.increment.get-售后列表接口（方舟）.md)
- [pdd.refund.list.increment.get - 售后列表接口](./售后API/pdd.refund.list.increment.get-售后列表接口.md)
- [pdd.refund.returngoods.agree - 商家售后同意退货](./售后API/pdd.refund.returngoods.agree-商家售后同意退货.md)
- [pdd.refund.status.check - 售后校验接口](./售后API/pdd.refund.status.check-售后校验接口.md)

#### 发票服务API（4）
- [pdd.einvoice.info.query - 自动开票发票查询](./发票服务API/pdd.einvoice.info.query-自动开票发票查询.md)
- [pdd.invoice.application.query - 开票申请单查询](./发票服务API/pdd.invoice.application.query-开票申请单查询.md)
- [pdd.invoice.detail.invalid - 订单发票冲红](./发票服务API/pdd.invoice.detail.invalid-订单发票冲红.md)
- [pdd.invoice.detail.upload - 开票结果回传](./发票服务API/pdd.invoice.detail.upload-开票结果回传.md)

#### 财务API（1）
- [pdd.finance.balance.daily.bill.url.get - 商家货款日账单下载链接查询接口](./财务API/pdd.finance.balance.daily.bill.url.get-商家货款日账单下载链接查询接口.md)

#### 方舟数据传输API（6）
- [pdd.cloud.dts.order.information.get - 订单推送库详情查询接口](./方舟数据传输API/pdd.cloud.dts.order.information.get-订单推送库详情查询接口.md)
- [pdd.cloud.dts.order.list.increment.get - 订单推送库增量查询接口](./方舟数据传输API/pdd.cloud.dts.order.list.increment.get-订单推送库增量查询接口.md)
- [pdd.cloud.wms.order.send - 云内下发wms订单接口](./方舟数据传输API/pdd.cloud.wms.order.send-云内下发wms订单接口.md)
- [pdd.erp.order.list.get - 订单列表查询接口](./方舟数据传输API/pdd.erp.order.list.get-订单列表查询接口.md)
- [pdd.erp.oub.list.get - 出库单列表查询接口](./方舟数据传输API/pdd.erp.oub.list.get-出库单列表查询接口.md)
- [pdd.erp.refund.list.get - 售后列表查询接口](./方舟数据传输API/pdd.erp.refund.list.get-售后列表查询接口.md)

### 物流与仓配（59）

#### 物流API（9）
- [pdd.cross.cabinet.recycle.order - 快递柜包裹回收订单](./物流API/pdd.cross.cabinet.recycle.order-快递柜包裹回收订单.md)
- [pdd.delivery.receipt.image.upload - 发货底单图片上传](./物流API/pdd.delivery.receipt.image.upload-发货底单图片上传.md)
- [pdd.logistics.address.get - 获取拼多多标准地址库](./物流API/pdd.logistics.address.get-获取拼多多标准地址库.md)
- [pdd.logistics.available.company.recommend - 获取可发货快递接口](./物流API/pdd.logistics.available.company.recommend-获取可发货快递接口.md)
- [pdd.logistics.companies.get - 快递公司查看接口](./物流API/pdd.logistics.companies.get-快递公司查看接口.md)
- [pdd.logistics.isv.trace.notify.sub - ISV物流轨迹推送消息订阅接口](./物流API/pdd.logistics.isv.trace.notify.sub-ISV物流轨迹推送消息订阅接口.md)
- [pdd.cloud.logistics.online.send - 云内发货接口](./物流API/pdd.cloud.logistics.online.send-云内发货接口.md)
- [pdd.logistics.online.send - 订单发货通知接口](./物流API/pdd.logistics.online.send-订单发货通知接口.md)
- [pdd.logistics.ordertrace.get - 轨迹查询接口](./物流API/pdd.logistics.ordertrace.get-轨迹查询接口.md)

#### 仓储API（15）
- [pdd.express.add.depot - 增加仓库](./仓储API/pdd.express.add.depot-增加仓库.md)
- [pdd.express.change.depot.info - 修改仓库信息](./仓储API/pdd.express.change.depot.info-修改仓库信息.md)
- [pdd.express.depot.info.get - 仓库详细信息](./仓储API/pdd.express.depot.info.get-仓库详细信息.md)
- [pdd.express.depot.list.get - 仓库列表](./仓储API/pdd.express.depot.list.get-仓库列表.md)
- [pdd.express.search.depot - 根据仓库名称和仓库编码查询仓库](./仓储API/pdd.express.search.depot-根据仓库名称和仓库编码查询仓库.md)
- [pdd.stock.goods.id.to.sku.query - 根据商品id查询sku信息](./仓储API/pdd.stock.goods.id.to.sku.query-根据商品id查询sku信息.md)
- [pdd.stock.ware.create - 创建货品](./仓储API/pdd.stock.ware.create-创建货品.md)
- [pdd.stock.ware.delete - 删除货品](./仓储API/pdd.stock.ware.delete-删除货品.md)
- [pdd.stock.ware.detail.query - 查询货品详情](./仓储API/pdd.stock.ware.detail.query-查询货品详情.md)
- [pdd.stock.ware.info.list - 货品列表的查询接口](./仓储API/pdd.stock.ware.info.list-货品列表的查询接口.md)
- [pdd.stock.ware.list - 查询货品列表](./仓储API/pdd.stock.ware.list-查询货品列表.md)
- [pdd.stock.ware.move - 家电分仓库存-库存信息调整](./仓储API/pdd.stock.ware.move-家电分仓库存-库存信息调整.md)
- [pdd.stock.ware.sku.update - 货品关联sku](./仓储API/pdd.stock.ware.sku.update-货品关联sku.md)
- [pdd.stock.ware.update - 编辑货品](./仓储API/pdd.stock.ware.update-编辑货品.md)
- [pdd.stock.ware.warehouse.query - 货品仓库库存信息查询](./仓储API/pdd.stock.ware.warehouse.query-货品仓库库存信息查询.md)

#### 商家寄件API（13）
- [pdd.logistics.onlinedelivery.courier.query - 查询可选快递公司](./商家寄件API/pdd.logistics.onlinedelivery.courier.query-查询可选快递公司.md)
- [pdd.logistics.onlinedelivery.payment.status - 免密支付状态查询接口](./商家寄件API/pdd.logistics.onlinedelivery.payment.status-免密支付状态查询接口.md)
- [pdd.logistics.onlinedelivery.predict.price - 查询快递公司预估金额](./商家寄件API/pdd.logistics.onlinedelivery.predict.price-查询快递公司预估金额.md)
- [pdd.logistics.onlinedelivery.receipt.cancel - 取消寄件接口](./商家寄件API/pdd.logistics.onlinedelivery.receipt.cancel-取消寄件接口.md)
- [pdd.logistics.onlinedelivery.receipt.create - 商家寄件寄件单下单接口](./商家寄件API/pdd.logistics.onlinedelivery.receipt.create-商家寄件寄件单下单接口.md)
- [pdd.logistics.onlinedelivery.receipt.detail - 寄件单详情接口](./商家寄件API/pdd.logistics.onlinedelivery.receipt.detail-寄件单详情接口.md)
- [pdd.logistics.onlinedelivery.receipt.list - 查询已寄件寄件单列表](./商家寄件API/pdd.logistics.onlinedelivery.receipt.list-查询已寄件寄件单列表.md)
- [pdd.logistics.onlinedelivery.receipt.not.pay.list - 查询待支付寄件单列表](./商家寄件API/pdd.logistics.onlinedelivery.receipt.not.pay.list-查询待支付寄件单列表.md)
- [pdd.logistics.onlinedelivery.receipt.trigger.pay - 商家主动支付接口](./商家寄件API/pdd.logistics.onlinedelivery.receipt.trigger.pay-商家主动支付接口.md)
- [pdd.logistics.onlinedelivery.send.address.query - 获取商家发货地址信息](./商家寄件API/pdd.logistics.onlinedelivery.send.address.query-获取商家发货地址信息.md)
- [pdd.logistics.onlinedelivery.subsiby.appeal.result - 商家寄件补贴活动账单申诉结果推送](./商家寄件API/pdd.logistics.onlinedelivery.subsiby.appeal.result-商家寄件补贴活动账单申诉结果推送.md)
- [pdd.logistics.onlinedelivery.subsiby.shipbill.send - 商家寄件补贴活动快递公司账单下发接口](./商家寄件API/pdd.logistics.onlinedelivery.subsiby.shipbill.send-商家寄件补贴活动快递公司账单下发接口.md)
- [pdd.logistics.onlinedelivery.subsiby.weight.appeal - 商家寄件补贴活动重量申诉接口](./商家寄件API/pdd.logistics.onlinedelivery.subsiby.weight.appeal-商家寄件补贴活动重量申诉接口.md)

#### 电子面单API（15）
- [pdd.cloud.print - 云打印](./电子面单API/pdd.cloud.print-云打印.md)
- [pdd.cloud.print.task.query - 云打印任务查询](./电子面单API/pdd.cloud.print.task.query-云打印任务查询.md)
- [pdd.cloud.print.verify.code - 云打印验证码](./电子面单API/pdd.cloud.print.verify.code-云打印验证码.md)
- [pdd.cloud.printer.bind - 云打印机绑定](./电子面单API/pdd.cloud.printer.bind-云打印机绑定.md)
- [pdd.cloud.printer.setting - 云打印机设置](./电子面单API/pdd.cloud.printer.setting-云打印机设置.md)
- [pdd.cloud.printer.status.query - 云打印机状态查询](./电子面单API/pdd.cloud.printer.status.query-云打印机状态查询.md)
- [pdd.cloudprint.customares.get - 获取商家的自定义区模板信息](./电子面单API/pdd.cloudprint.customares.get-获取商家的自定义区模板信息.md)
- [pdd.cloudprint.stdtemplates.get - 获取所有标准电子面单模板](./电子面单API/pdd.cloudprint.stdtemplates.get-获取所有标准电子面单模板.md)
- [pdd.cloud.waybill.get - 云内电子面单获取接口](./电子面单API/pdd.cloud.waybill.get-云内电子面单获取接口.md)
- [pdd.cloud.waybill.update - 云内电子面单更新接口](./电子面单API/pdd.cloud.waybill.update-云内电子面单更新接口.md)
- [pdd.waybill.cancel - 商家取消获取的电子面单号](./电子面单API/pdd.waybill.cancel-商家取消获取的电子面单号.md)
- [pdd.waybill.get - 电子面单云打印接口](./电子面单API/pdd.waybill.get-电子面单云打印接口.md)
- [pdd.waybill.query.by.waybillcode - 通过面单号查询面单信息](./电子面单API/pdd.waybill.query.by.waybillcode-通过面单号查询面单信息.md)
- [pdd.waybill.search - 查询面单服务订购及面单使用情况](./电子面单API/pdd.waybill.search-查询面单服务订购及面单使用情况.md)
- [pdd.waybill.update - 电子面单云打印更新接口](./电子面单API/pdd.waybill.update-电子面单云打印更新接口.md)

#### 电子面单代打API（7）
- [pdd.fds.order.get - 订单详情](./电子面单代打API/pdd.fds.order.get-订单详情.md)
- [pdd.fds.order.list.get - 根据更新时间查询订单列表](./电子面单代打API/pdd.fds.order.list.get-根据更新时间查询订单列表.md)
- [pdd.fds.role.get - 查询店铺身份](./电子面单代打API/pdd.fds.role.get-查询店铺身份.md)
- [pdd.fds.waybill.cancel - 电子面单取消回传](./电子面单代打API/pdd.fds.waybill.cancel-电子面单取消回传.md)
- [pdd.fds.waybill.get - 电子面单取号](./电子面单代打API/pdd.fds.waybill.get-电子面单取号.md)
- [pdd.fds.waybill.return - 电子面单回传](./电子面单代打API/pdd.fds.waybill.return-电子面单回传.md)
- [pdd.fds.waybill.return.slave - 电子面单回传额外运单号](./电子面单代打API/pdd.fds.waybill.return.slave-电子面单回传额外运单号.md)

### 营销与流量（55）

#### 营销API（7）
- [pdd.promotion.goods.coupon.list.get - 商品优惠券批次列表查询](./营销API/pdd.promotion.goods.coupon.list.get-商品优惠券批次列表查询.md)
- [pdd.promotion.limited.activity.cancel - 限时限量购活动结束接口](./营销API/pdd.promotion.limited.activity.cancel-限时限量购活动结束接口.md)
- [pdd.promotion.limited.activity.create - 限时限量购活动创建接口](./营销API/pdd.promotion.limited.activity.create-限时限量购活动创建接口.md)
- [pdd.promotion.limited.discount.list.get - 限时限量购活动列表查询](./营销API/pdd.promotion.limited.discount.list.get-限时限量购活动列表查询.md)
- [pdd.promotion.limited.qualified.goods.get - 限时限量购可选商品查询接口](./营销API/pdd.promotion.limited.qualified.goods.get-限时限量购可选商品查询接口.md)
- [pdd.promotion.limited.qualified.sku.get - 限时限量购可选sku查询接口](./营销API/pdd.promotion.limited.qualified.sku.get-限时限量购可选sku查询接口.md)
- [pdd.promotion.merchant.coupon.list.get - 店铺优惠券批次列表接口](./营销API/pdd.promotion.merchant.coupon.list.get-店铺优惠券批次列表接口.md)

#### 多多客API（29）
- [pdd.ddk.cashgift.create - 创建多多礼金](./多多客API/pdd.ddk.cashgift.create-创建多多礼金.md)
- [pdd.ddk.cashgift.data.query - 查询多多礼金效果数据](./多多客API/pdd.ddk.cashgift.data.query-查询多多礼金效果数据.md)
- [pdd.ddk.cashgift.status.update - 多多礼金状态更新](./多多客API/pdd.ddk.cashgift.status.update-多多礼金状态更新.md)
- [pdd.ddk.cms.prom.url.generate - 生成商城-频道推广链接](./多多客API/pdd.ddk.cms.prom.url.generate-生成商城-频道推广链接.md)
- [pdd.ddk.goods.detail - 多多进宝商品详情查询](./多多客API/pdd.ddk.goods.detail-多多进宝商品详情查询.md)
- [pdd.ddk.goods.pid.generate - 创建多多进宝推广位](./多多客API/pdd.ddk.goods.pid.generate-创建多多进宝推广位.md)
- [pdd.ddk.goods.pid.query - 查询已经生成的推广位信息](./多多客API/pdd.ddk.goods.pid.query-查询已经生成的推广位信息.md)
- [pdd.ddk.goods.promotion.right.auth - 多多进宝信息流渠道备案授权素材上传接口](./多多客API/pdd.ddk.goods.promotion.right.auth-多多进宝信息流渠道备案授权素材上传接口.md)
- [pdd.ddk.goods.promotion.url.generate - 多多进宝推广链接生成](./多多客API/pdd.ddk.goods.promotion.url.generate-多多进宝推广链接生成.md)
- [pdd.ddk.goods.recommend.get - 多多进宝商品推荐API](./多多客API/pdd.ddk.goods.recommend.get-多多进宝商品推荐API.md)
- [pdd.ddk.goods.search - 多多进宝商品查询](./多多客API/pdd.ddk.goods.search-多多进宝商品查询.md)
- [pdd.ddk.goods.zs.unit.url.gen - 多多进宝转链接口](./多多客API/pdd.ddk.goods.zs.unit.url.gen-多多进宝转链接口.md)
- [pdd.ddk.member.authority.query - 查询是否绑定备案](./多多客API/pdd.ddk.member.authority.query-查询是否绑定备案.md)
- [pdd.ddk.order.detail.get - 查询订单详情](./多多客API/pdd.ddk.order.detail.get-查询订单详情.md)
- [pdd.ddk.order.list.increment.get - 最后更新时间段增量同步推广订单信息](./多多客API/pdd.ddk.order.list.increment.get-最后更新时间段增量同步推广订单信息.md)
- [pdd.ddk.order.list.range.get - 用时间段查询推广订单接口](./多多客API/pdd.ddk.order.list.range.get-用时间段查询推广订单接口.md)
- [pdd.ddk.pid.mediaid.bind - 批量绑定推广位的媒体id](./多多客API/pdd.ddk.pid.mediaid.bind-批量绑定推广位的媒体id.md)
- [pdd.ddk.promotion.goods.query - 多多进宝信息流投放商品报备进度查询](./多多客API/pdd.ddk.promotion.goods.query-多多进宝信息流投放商品报备进度查询.md)
- [pdd.ddk.report.img.upload - 多多客信息流投放备案图片上传接口](./多多客API/pdd.ddk.report.img.upload-多多客信息流投放备案图片上传接口.md)
- [pdd.ddk.report.video.upload - 多多客信息流投放备案视频上传接口](./多多客API/pdd.ddk.report.video.upload-多多客信息流投放备案视频上传接口.md)
- [pdd.ddk.report.video.upload.part - 多多客信息流投放备案视频上传分片上传接口](./多多客API/pdd.ddk.report.video.upload.part-多多客信息流投放备案视频上传分片上传接口.md)
- [pdd.ddk.report.video.upload.part.complete - 多多客信息流投放备案视频上传分片完成接口](./多多客API/pdd.ddk.report.video.upload.part.complete-多多客信息流投放备案视频上传分片完成接口.md)
- [pdd.ddk.report.video.upload.part.init - 多多客信息流投放备案视频上传分片初始化接口](./多多客API/pdd.ddk.report.video.upload.part.init-多多客信息流投放备案视频上传分片初始化接口.md)
- [pdd.ddk.resource.url.gen - 生成多多进宝频道推广](./多多客API/pdd.ddk.resource.url.gen-生成多多进宝频道推广.md)
- [pdd.ddk.rp.prom.url.generate - 生成营销工具推广链接](./多多客API/pdd.ddk.rp.prom.url.generate-生成营销工具推广链接.md)
- [pdd.ddk.statistics.data.query - 多多进宝数据统计查询接口](./多多客API/pdd.ddk.statistics.data.query-多多进宝数据统计查询接口.md)
- [pdd.ddk.tmc.activity.list - 千万神券活动数据列表](./多多客API/pdd.ddk.tmc.activity.list-千万神券活动数据列表.md)
- [pdd.ddk.url.short.parse - 多多进宝推广短链解析](./多多客API/pdd.ddk.url.short.parse-多多进宝推广短链解析.md)
- [pdd.ddk.weapp.qrcode.url.gen - 多多客生成单品推广小程序二维码url](./多多客API/pdd.ddk.weapp.qrcode.url.gen-多多客生成单品推广小程序二维码url.md)

#### 多多客工具API（18）
- [pdd.ddk.all.order.list.increment.get - 查询所有授权的多多客订单](./多多客工具API/pdd.ddk.all.order.list.increment.get-查询所有授权的多多客订单.md)
- [pdd.ddk.oauth.cashgift.create - 创建多多礼金](./多多客工具API/pdd.ddk.oauth.cashgift.create-创建多多礼金.md)
- [pdd.ddk.oauth.cashgift.status.update - 多多礼金状态更新](./多多客工具API/pdd.ddk.oauth.cashgift.status.update-多多礼金状态更新.md)
- [pdd.ddk.oauth.cms.prom.url.generate - 生成商城推广链接接口](./多多客工具API/pdd.ddk.oauth.cms.prom.url.generate-生成商城推广链接接口.md)
- [pdd.ddk.oauth.goods.detail - 多多进宝商品详情查询](./多多客工具API/pdd.ddk.oauth.goods.detail-多多进宝商品详情查询.md)
- [pdd.ddk.oauth.goods.pid.generate - 多多进宝推广位创建接口](./多多客工具API/pdd.ddk.oauth.goods.pid.generate-多多进宝推广位创建接口.md)
- [pdd.ddk.oauth.goods.pid.query - 多多客已生成推广位信息查询](./多多客工具API/pdd.ddk.oauth.goods.pid.query-多多客已生成推广位信息查询.md)
- [pdd.ddk.oauth.goods.prom.url.generate - 生成多多进宝推广链接](./多多客工具API/pdd.ddk.oauth.goods.prom.url.generate-生成多多进宝推广链接.md)
- [pdd.ddk.oauth.goods.recommend.get - 运营频道商品查询API](./多多客工具API/pdd.ddk.oauth.goods.recommend.get-运营频道商品查询API.md)
- [pdd.ddk.oauth.goods.search - 多多进宝商品查询](./多多客工具API/pdd.ddk.oauth.goods.search-多多进宝商品查询.md)
- [pdd.ddk.oauth.goods.zs.unit.url.gen - 多多进宝转链接口](./多多客工具API/pdd.ddk.oauth.goods.zs.unit.url.gen-多多进宝转链接口.md)
- [pdd.ddk.oauth.member.authority.query - 查询是否绑定备案](./多多客工具API/pdd.ddk.oauth.member.authority.query-查询是否绑定备案.md)
- [pdd.ddk.oauth.order.detail.get - 获取订单详情](./多多客工具API/pdd.ddk.oauth.order.detail.get-获取订单详情.md)
- [pdd.ddk.oauth.order.list.increment.get - 按照更新时间段增量同步推广订单信息](./多多客工具API/pdd.ddk.oauth.order.list.increment.get-按照更新时间段增量同步推广订单信息.md)
- [pdd.ddk.oauth.pid.mediaid.bind - 批量绑定推广位的媒体id](./多多客工具API/pdd.ddk.oauth.pid.mediaid.bind-批量绑定推广位的媒体id.md)
- [pdd.ddk.oauth.resource.url.gen - 拼多多主站频道推广接口](./多多客工具API/pdd.ddk.oauth.resource.url.gen-拼多多主站频道推广接口.md)
- [pdd.ddk.oauth.rp.prom.url.generate - 生成营销工具推广链接](./多多客工具API/pdd.ddk.oauth.rp.prom.url.generate-生成营销工具推广链接.md)
- [pdd.ddk.oauth.weapp.qrcode.url.gen - 多多客工具生成单品推广小程序二维码](./多多客工具API/pdd.ddk.oauth.weapp.qrcode.url.gen-多多客工具生成单品推广小程序二维码.md)

#### 视频推荐API（1）
- [pdd.vivodeskwindow.queryresources - vivo视界资源下发](./视频推荐API/pdd.vivodeskwindow.queryresources-vivo视界资源下发.md)

### 平台能力与生态（18）

#### 消息服务API（7）
- [pdd.ddy.pdp.user.add - 添加数据推送用户](./消息服务API/pdd.ddy.pdp.user.add-添加数据推送用户.md)
- [pdd.ddy.pdp.user.delete - 删除数据推送用户](./消息服务API/pdd.ddy.pdp.user.delete-删除数据推送用户.md)
- [pdd.ddy.pdp.users.get - 获取开通订单同步服务的用户](./消息服务API/pdd.ddy.pdp.users.get-获取开通订单同步服务的用户.md)
- [pdd.pmc.accrue.query - 消息队列积压数量查询](./消息服务API/pdd.pmc.accrue.query-消息队列积压数量查询.md)
- [pdd.pmc.user.cancel - 取消用户的消息服务](./消息服务API/pdd.pmc.user.cancel-取消用户的消息服务.md)
- [pdd.pmc.user.get - 获取用户已开通消息](./消息服务API/pdd.pmc.user.get-获取用户已开通消息.md)
- [pdd.pmc.user.permit - 为已授权的用户开通消息服务](./消息服务API/pdd.pmc.user.permit-为已授权的用户开通消息服务.md)

#### 安全与会话API（4）
- [pdd.cloud.isv.page.code - 开平ISV前端插件检测页面code获取接口](./安全与会话API/pdd.cloud.isv.page.code-开平ISV前端插件检测页面code获取接口.md)
- [pdd.cloud.security.event.tracking.batch.order - 多多云ISV用户订单事件批量上报](./安全与会话API/pdd.cloud.security.event.tracking.batch.order-多多云ISV用户订单事件批量上报.md)
- [pdd.cloud.security.event.tracking.login - 多多云ISV用户登录事件上报接口](./安全与会话API/pdd.cloud.security.event.tracking.login-多多云ISV用户登录事件上报接口.md)
- [pdd.cloud.websession.send - 会话同步接口](./安全与会话API/pdd.cloud.websession.send-会话同步接口.md)

#### 服务市场API（4）
- [pdd.servicemarket.contract.search - 服务市场订单履约查询](./服务市场API/pdd.servicemarket.contract.search-服务市场订单履约查询.md)
- [pdd.servicemarket.settlementbill.get - 月结算账单导出](./服务市场API/pdd.servicemarket.settlementbill.get-月结算账单导出.md)
- [pdd.servicemarket.tradelist.get - 交易明细单导出](./服务市场API/pdd.servicemarket.tradelist.get-交易明细单导出.md)
- [pdd.vas.order.search - 线上服务市场订单查询接口](./服务市场API/pdd.vas.order.search-线上服务市场订单查询接口.md)

#### 短信服务API（2）
- [pdd.open.msg.send.result.receive - 短信回执](./短信服务API/pdd.open.msg.send.result.receive-短信回执.md)
- [pdd.open.msg.service.send.express.msg - 根据运单号发短信](./短信服务API/pdd.open.msg.service.send.express.msg-根据运单号发短信.md)

#### 短信供应商API（1）
- [pdd.sms.detailbill.push - 短信明细回执](./短信供应商API/pdd.sms.detailbill.push-短信明细回执.md)

### 垂直行业与专项（28）

#### 卡券API（10）
- [pdd.reserved.medicine.logistics.upload - 预留药物流信息上传](./卡券API/pdd.reserved.medicine.logistics.upload-预留药物流信息上传.md)
- [pdd.voucher.appointment.info.send - 卡券预约提货接口](./卡券API/pdd.voucher.appointment.info.send-卡券预约提货接口.md)
- [pdd.voucher.ota.card.prepare.verification - 平台卡密核销验券](./卡券API/pdd.voucher.ota.card.prepare.verification-平台卡密核销验券.md)
- [pdd.voucher.ota.card.verification - 卡券（电子）核销接口（平台生成卡密）](./卡券API/pdd.voucher.ota.card.verification-卡券（电子）核销接口（平台生成卡密）.md)
- [pdd.voucher.physical.goods.send - 卡券发货（实物）接口](./卡券API/pdd.voucher.physical.goods.send-卡券发货（实物）接口.md)
- [pdd.voucher.realtime.verify.sync - 卡券API核销券码](./卡券API/pdd.voucher.realtime.verify.sync-卡券API核销券码.md)
- [pdd.voucher.virtual.card.batch.add - 批量添加卡券](./卡券API/pdd.voucher.virtual.card.batch.add-批量添加卡券.md)
- [pdd.voucher.virtual.card.verification - 卡券（电子）核销接口](./卡券API/pdd.voucher.virtual.card.verification-卡券（电子）核销接口.md)
- [pdd.voucher.voucher.complain - 卡券投诉接口](./卡券API/pdd.voucher.voucher.complain-卡券投诉接口.md)
- [pdd.voucher.voucher.info.send - 卡券信息发送接口](./卡券API/pdd.voucher.voucher.info.send-卡券信息发送接口.md)

#### 虚拟类目API（3）
- [pdd.virtual.game.server.query - 虚拟游戏类区服列表接口](./虚拟类目API/pdd.virtual.game.server.query-虚拟游戏类区服列表接口.md)
- [pdd.virtual.mobile.charge.notify - 虚拟类目发货通知接口](./虚拟类目API/pdd.virtual.mobile.charge.notify-虚拟类目发货通知接口.md)
- [pdd.warranty.orders.increment.get - 查询服务保障订单](./虚拟类目API/pdd.warranty.orders.increment.get-查询服务保障订单.md)

#### 旅游门票API（11）
- [pdd.service.aftersales.appoint.notify - 售后服务预约通知接口](./旅游门票API/pdd.service.aftersales.appoint.notify-售后服务预约通知接口.md)
- [pdd.ticket.areacode.get - 旅游门票区域编码查询](./旅游门票API/pdd.ticket.areacode.get-旅游门票区域编码查询.md)
- [pdd.ticket.goods.query - 门票商品查询接口](./旅游门票API/pdd.ticket.goods.query-门票商品查询接口.md)
- [pdd.ticket.goods.upload - 门票商品新建及更新接口](./旅游门票API/pdd.ticket.goods.upload-门票商品新建及更新接口.md)
- [pdd.ticket.order.create.notifycation - 旅游门票订单创建异步回调接口](./旅游门票API/pdd.ticket.order.create.notifycation-旅游门票订单创建异步回调接口.md)
- [pdd.ticket.order.refund.notifycation - 旅游门票订单售后结果回调](./旅游门票API/pdd.ticket.order.refund.notifycation-旅游门票订单售后结果回调.md)
- [pdd.ticket.scenic.get - 旅游门票拼多多景区编码查询](./旅游门票API/pdd.ticket.scenic.get-旅游门票拼多多景区编码查询.md)
- [pdd.ticket.sku.rule.add - 旅游门票商品履约规则新增](./旅游门票API/pdd.ticket.sku.rule.add-旅游门票商品履约规则新增.md)
- [pdd.ticket.sku.rule.edit - 旅游门票商品履约规则修改](./旅游门票API/pdd.ticket.sku.rule.edit-旅游门票商品履约规则修改.md)
- [pdd.ticket.sku.rule.get - 旅游门票商品履约生效规则查询](./旅游门票API/pdd.ticket.sku.rule.get-旅游门票商品履约生效规则查询.md)
- [pdd.ticket.verification.notifycation - 旅游门票订单核销通知接口](./旅游门票API/pdd.ticket.verification.notifycation-旅游门票订单核销通知接口.md)

#### 多多国际API（4）
- [pdd.customs.send.goods.record - 海淘服务商上传商品备案信息](./多多国际API/pdd.customs.send.goods.record-海淘服务商上传商品备案信息.md)
- [pdd.mall.info.bonded.warehouse.get - 保税仓信息查询接口](./多多国际API/pdd.mall.info.bonded.warehouse.get-保税仓信息查询接口.md)
- [pdd.oversea.clearance.get - 获取多多国际清关材料](./多多国际API/pdd.oversea.clearance.get-获取多多国际清关材料.md)
- [pdd.oversea.declaration.fail.notify - 同步海淘订单申报失败情况](./多多国际API/pdd.oversea.declaration.fail.notify-同步海淘订单申报失败情况.md)
