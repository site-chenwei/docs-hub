---
title: "ContentType使用场景说明"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-appendix"
menu_path:
  - "指南"
  - "应用服务"
  - "Scenario Fusion Kit（融合场景服务）"
  - "智能填充服务"
  - "ContentType使用场景说明"
captured_at: "2026-04-17T01:36:22.082Z"
---

# ContentType使用场景说明

华为账号昵称

| 名称 | 说明 |
| :-- | :-- |
| NICKNAME | 昵称，如“Vivian”。 |

用户姓名

| 名称 | 说明 |
| :-- | :-- |
| PERSON\_FULL\_NAME | 姓名，如“张三”。 |
| PERSON\_LAST\_NAME | 姓氏，如“张”。 |
| PERSON\_FIRST\_NAME | 名字，如“三”。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/1xtfa0JeRIqp_4Q5AvGCyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013623Z&HW-CC-Expire=86400&HW-CC-Sign=442A7A1F21580564B446C0D5E7F23B8B60BDE1363CDB9532E4C92061591DB115)

-   PERSON\_FULL\_NAME和（PERSON\_LAST\_NAME，PERSON\_FIRST\_NAME）不能同时在同一个表单中使用（在护照信息场景中可以同时使用）。
-   请在收集使用用户敏感个人信息的表单界面告知目的以及必要性。

联系方式

| 名称 | 说明 |
| :-- | :-- |
| PHONE\_NUMBER | 手机号，如“188\*\*\*\*\*\*88”。 |
| EMAIL\_ADDRESS | 邮箱地址，如“a\*\*\*\*t@huawei.com”。 |

身份信息

| 名称 | 说明 |
| :-- | :-- |
| ID\_CARD\_NUMBER | 身份证号，如“3201\*\*\*\*\*\*\*\*\*\*\*123”。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/G1ThBrImRA-pn3ZIevSKaw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013623Z&HW-CC-Expire=86400&HW-CC-Sign=CC25CC1FB0D6CC01CED757AD7CE24DC93807E75360C9D961C16AC642CDA64502)

-   ID\_CARD\_NUMBER目前只支持身份证号的推荐、填充，不支持其他类型的证件，可参考[动态修改ContentType值](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-amend)动态配置输入框的ContentType。
-   请在收集使用用户敏感个人信息的表单界面告知目的以及必要性。

护照信息

| 名称 | 说明 |
| :-- | :-- |
| COUNTRY\_ADDRESS | 国籍，如“中国”。 |
| PASSPORT\_NUMBER | 护照号，如“G\*\*\*\*\*\*\*1”。 |
| VALIDITY | 有效期至，如“2025-1-1”。 |
| ISSUE\_AT | 签发地，如“广东”。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/TpMJyARPTiumRrQgFlk3nw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013623Z&HW-CC-Expire=86400&HW-CC-Sign=BF2408E7EC99DD29CA8C80232E4794439824130981E5C65687898CAD99B0BDA2)

请在收集使用用户敏感个人信息的表单界面告知目的以及必要性。

车牌信息

| 名称 | 说明 |
| :-- | :-- |
| LICENSE\_PLATE | 车牌号，如“粤A\*\*\*\*\*1”。 |

地址信息

| 名称 | 说明 |
| :-- | :-- |
| FULL\_STREET\_ADDRESS | 带街道详细地址，如“雨花街道玉兰路98号”。 |
| FORMAT\_ADDRESS | 全量地址，如“中国江苏省南京市雨花台区雨花街道玉兰路98号”。 |
| DETAIL\_INFO\_WITHOUT\_STREET | 不带街道详细地址，如“玉兰路98号”。 |
| ADDRESS\_CITY\_AND\_STATE | 所在地区，如“中国广东省深圳市龙岗区”。 |

发票抬头信息

| 名称 | 说明 |
| :-- | :-- |
| ORGANIZATION | 名称，如“深圳市xx公司”。 |
| TAX\_ID | 税号，如“2020\*\*\*\*\*\*\*\*\*\*\*000”。 |
