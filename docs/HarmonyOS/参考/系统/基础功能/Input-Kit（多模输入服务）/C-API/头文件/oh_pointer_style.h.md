---
title: "oh_pointer_style.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pointer-style-h"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "C API"
  - "头文件"
  - "oh_pointer_style.h"
captured_at: "2026-04-17T01:48:30.814Z"
---

# oh\_pointer\_style.h

#### 概述

鼠标光标的样式。

**引用文件：** <multimodalinput/oh\_pointer\_style.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 22

**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)

#### 汇总

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [Input\_PointerStyle](#input_pointerstyle) | Input\_PointerStyle | 鼠标光标样式。 |

#### 枚举类型说明

#### \[h2\]Input\_PointerStyle

```c
enum Input_PointerStyle
```

**描述**

鼠标光标样式。

**起始版本：** 22

| 枚举项 | 描述 | 图示 |
| :-- | :-- | :-- |
| DEFAULT = 0 | 默认 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/A9VLZRT7SpCWlfzlzvx9kA/zh-cn_image_0000002538181424.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=42414A090003B3E8BFF944AB1050BCB63E89C30C8D8C06DA865266397267FCF1) |
| EAST = 1 | 向东箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/dnQ_74b-RzKx-VOgow_hEw/zh-cn_image_0000002569021211.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=B1B446B40DD467530FE4B0BCFDED7798F27D6407CE983C8BF1C3E169FDBF5203) |
| WEST = 2 | 向西箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Y-pLTWSlRYK39wUImtK8mQ/zh-cn_image_0000002568901201.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=BB7072A991F73AE78066F6892A4B05A1A41D3DB774C051BCF0209445ACFC7BE4) |
| SOUTH = 3 | 向南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/1Fj8vHuKRYW9pOoO5fP4Ew/zh-cn_image_0000002538021500.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=2C4D7F3F367A3C1BF4E9BB74DDDA41AB541C36311395540C3054CD2F901F97EB) |
| NORTH = 4 | 向北箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/RpSwD_fSQV-MsvJNRmtKKg/zh-cn_image_0000002538181426.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=03E51BA1BD445E7A6A5CB1EC5531BFF66F2A0AE7566ADE5685F9087A20BB2E53) |
| WEST\_EAST = 5 | 向西东箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/b77sC6G-TkuBRlYLmxDEpQ/zh-cn_image_0000002569021213.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=6C337BDF93E1C2B924E23DB761CBE549F2DC0FA88682416A1417C140FB30774B) |
| NORTH\_SOUTH = 6 | 向北南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/74WcjmSSQsWIFWzWTxd4tQ/zh-cn_image_0000002568901203.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=AECDEA3548FC918FD2399E5793184B302DE170590F6EA8751B24EB5170764234) |
| NORTH\_EAST = 7 | 向东北箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/k_DTI34DRbKD8uud9Nbomg/zh-cn_image_0000002538021502.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=5E6FE40373715279A0BEE0FCF49683784042A2F83B08C5B93759A4B16A192718) |
| NORTH\_WEST = 8 | 向西北箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/rLXkbmAgQ7KzPXbRAOvtQg/zh-cn_image_0000002538181428.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=C63F225169A3ED811B8351C26D1E27B943A33D8855670DE41BBF7E227A801705) |
| SOUTH\_EAST = 9 | 向东南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ZZs3tIl-Q-mu8UIK2fM41Q/zh-cn_image_0000002569021215.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=A369D9B9101463AF19327CACA5B306BA6B20AB485C23BE61682815A7A88A2EF0) |
| SOUTH\_WEST = 10 | 向西南箭头 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/KqDlBUjHSh-rqFXk4N-gpw/zh-cn_image_0000002568901205.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=6ACFDDB0ACF1B696CAE06F0FC54247A25F4BDA039AC8D159961486D29965E552) |
| NORTH\_EAST\_SOUTH\_WEST = 11 | 东北西南调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/0vOCD0wsQdy2Ng7uMYyaCA/zh-cn_image_0000002538021504.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=E60464FF90E4CD1A326CFD94F851B6ADFFFE6C23852C8618B9ADEB87CAD12EFF) |
| NORTH\_WEST\_SOUTH\_EAST = 12 | 西北东南调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/f21ChAjeSumq8_SCFyQhGg/zh-cn_image_0000002538181430.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=6409A689D6B08496F620C679C8B8261BC14882805B624BC1B8FBDAF624B0DFC6) |
| CROSS = 13 | 准确选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/rWcZj-nqTrCrxnHaNVNufA/zh-cn_image_0000002569021217.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=8D07519D5C81AC23A385F89E67833E74B29D28AB8FF2BA2A61FDE5D26095D47E) |
| CURSOR\_COPY = 14 | 拷贝 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/cHOE2TdSQt-k4Bnt6oFEZw/zh-cn_image_0000002568901207.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=AC1E39DE40F0ADC1C3000F72AB828A3EE0102C3515A152B9EAA8AE317F802366) |
| CURSOR\_FORBID = 15 | 不可用 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/BcozqO-HR1edgQtRMGmuUg/zh-cn_image_0000002538021506.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F7FAAF2EAF9DD0E8565837B40B829D8C1B0AAE3C56D1E41440D80358D753ECCB) |
| COLOR\_SUCKER = 16 | 取色器 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/xdvQ-P9pSbem_0FHeGCYiw/zh-cn_image_0000002538181432.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=D11EC12810D9EC42CE9C5AC25EFE16B212FC6E6B79C644C6812294D092A8249A) |
| HAND\_GRABBING = 17 | 并拢的手 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Ad5Z4byRRwaYN58kgiZ3RQ/zh-cn_image_0000002569021219.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=466DFB6B1D1AC8F7FE85BD85720938C4CB3C3615DE38367BEA122B4BF05D2ED4) |
| HAND\_OPEN = 18 | 张开的手 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Z_AQZPEHSECI3HP6yVp-FQ/zh-cn_image_0000002568901209.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F0B9CA9682DDD0EDBAAC850244EF6B62F0E73B8A30D324F58B3C70A051F01DB8) |
| HAND\_POINTING = 19 | 手形指针 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/TEM540hDQmeBkbKGW2RUUA/zh-cn_image_0000002538021508.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=82C6C19B556CBBB0568585779A82F2EA4DBDCDED644FB4AE97D8E43829A230AD) |
| HELP = 20 | 帮助选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/WfiGnUbkSmSNi1AEjPOlfw/zh-cn_image_0000002538181434.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F646E2F15F19728BE6F995B7E60B5E9015A044FFE3C112991E0031016D3CAD83) |
| MOVE = 21 | 移动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/aq4NRryiQ8qMSXK74Eiwew/zh-cn_image_0000002569021221.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=1D78BB6BB543F75196F17C391CC8787A79AB57DBD9411A873A03E5D22628B4CF) |
| RESIZE\_LEFT\_RIGHT = 22 | 内部左右调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/ekEhH86JR-Cr0e8cj6K0FQ/zh-cn_image_0000002568901211.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=543D216A1338B7487C922E9F98C3249A89E4B600520C496629627A416DAB2681) |
| RESIZE\_UP\_DOWN = 23 | 内部上下调整 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Q4gUpW5ETPSSUOF7A4_KOg/zh-cn_image_0000002538021510.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=CE439E07AF87749FB796B73D5CD4CC8CB588A950F0BC203CD0E084E29142B90F) |
| SCREENSHOT\_CHOOSE = 24 | 截图十字准星 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/gAnA0SbKSzOy1GIudERZmA/zh-cn_image_0000002538181436.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F08211FE3FDE181F44A50D3DD9845E45A1E886987EB7AB557F3C0DB8A83C30B1) |
| SCREENSHOT\_CURSOR = 25 | 截图 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/V1TjnLObS3GcQxSoZVbNcA/zh-cn_image_0000002569021223.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=42209963E309261E5A50E8705727669C5910010022DB36AF185788DC1BCD2C6A) |
| TEXT\_CURSOR = 26 | 文本选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/nWQHAEHKQLiZ1XO1VJkDhA/zh-cn_image_0000002568901213.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=7F8ECF3E1D7312D085E5445E90E46ABA7CDC40609976627ED2184CAF2D6E1CE3) |
| ZOOM\_IN = 27 | 放大 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/P8aBa9TcS4Wqi0ojmZ2wbg/zh-cn_image_0000002538021512.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=06CE7CF197088000854B6777DA5304D9ECE4C01B4CB323D11222258F989D191D) |
| ZOOM\_OUT = 28 | 缩小 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/aosPLe5PRaejj0tfeG42aQ/zh-cn_image_0000002538181438.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=981A4AD1DDDE032390893853A73F36EB9A9E2CB40E335BA2B0A75076E0C7DE4E) |
| MIDDLE\_BTN\_EAST = 29 | 向东滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/hUfMD_BZS-6CtEGHrpOQ9g/zh-cn_image_0000002569021225.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F9A75178E4483B6D2E03ADF38388B1D62859B45B7458303ABE0C6FDFED20205D) |
| MIDDLE\_BTN\_WEST = 30 | 向西滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/NyZA-nJdRgaEkqeLCpt8aw/zh-cn_image_0000002568901215.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=7B3854819ECDBA5F26D7BC3BBDE08CC403C3FCF4D0FE2B790D240B576468CB3C) |
| MIDDLE\_BTN\_SOUTH = 31 | 向南滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/My-g-ZYiQFGUqiZh5qMhPA/zh-cn_image_0000002538021514.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=27AEB8C3124F528E17291881E6FCF23FE7C136D5B6320C68BE700A9D5E9B74C2) |
| MIDDLE\_BTN\_NORTH = 32 | 向北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/IU1KwGKpS8SNwRCB0WMisA/zh-cn_image_0000002538181440.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=9D2B21B0220273119A90D760F60021032AF464F1432C023E04C0CC7536378896) |
| MIDDLE\_BTN\_NORTH\_SOUTH = 33 | 向南北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/pNk1gkjkQRyyDTKoExFoyw/zh-cn_image_0000002569021227.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=5929EFED68A12F347E17F9D7995BB7E1494EEC42A1175211FFCE47FFBC1E4FD1) |
| MIDDLE\_BTN\_NORTH\_EAST = 34 | 向东北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/t6QaXgqnQ--VxFQpLWYpUA/zh-cn_image_0000002568901217.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=62DF9AB9FB4970891DFEBF344F4E7021FC45FAAA1714303217AADA587E0BC9C0) |
| MIDDLE\_BTN\_NORTH\_WEST = 35 | 向西北滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ceKfn9l2RVWDKtSReOU0Ig/zh-cn_image_0000002538021516.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F2250B583E5CA4E0F76DAEBE16ACCEF62BD7D4D27F6FE32AFE3F18E2FC393524) |
| MIDDLE\_BTN\_SOUTH\_EAST = 36 | 向东南滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6CvyArTsQdmruO15f7Lx9A/zh-cn_image_0000002538181442.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=F7D547D8EB8FF1B144C2F5DCD4EFB52C4C441E7A620F275554B0BEC9AA73075D) |
| MIDDLE\_BTN\_SOUTH\_WEST = 37 | 向西南滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/VGGqbhcQSfmehsY5kdjgMA/zh-cn_image_0000002569021229.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=B72FE98A24EEEB0829B176D559DF8D3587D6A69F4B843F2F5C4ECAD5933B06CC) |
| MIDDLE\_BTN\_NORTH\_SOUTH\_WEST\_EAST = 38 | 四向锥形移动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ySgkBK2pT8WsizTq83FdgQ/zh-cn_image_0000002568901219.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=E3E3FF9FB3AA4A52061FC0771C5058E74CD26BCDC94938FD141FFFA7E2DC742D) |
| HORIZONTAL\_TEXT\_CURSOR = 39 | 垂直文本选择 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/36UKZQgDTqmxKm9fBKZYVg/zh-cn_image_0000002538021518.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=118FF6867155C0488FE80C4BEE2BCD6CF25DEA7E54BAF82BE68DF2DEFFFA7A51) |
| CURSOR\_CROSS = 40 | 十字光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/yJWWPssxSUO_VHREnh0VYg/zh-cn_image_0000002538181444.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=ADD7393D37EE83E272AF4D43A842E67CC11EB825FF0532581DAEA4DC912B8DBE) |
| CURSOR\_CIRCLE = 41 | 圆形光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/8YsuUS_fQo-2SyQjvF5QGg/zh-cn_image_0000002569021231.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=97C3B9D44689ABF4408A5698930B10B82E11FDD5DDB1C388A3BB09F4CAB0E9AC) |
| LOADING = 42 | 正在载入动画光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/NxjGvBeSQJGaR2zkw3gddg/zh-cn_image_0000002568901221.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=948739F348F7B0D6371818FE21A92E543CBE92CD9546CF589731F7144D34B124) |
| RUNNING = 43 | 后台运行中动画光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/fENZujfwQ8G-NSF49uVKqw/zh-cn_image_0000002538021520.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=4158411914440459AF8B87DA0E376FD2EDBDE795A32FCAFE71960F1C800882F5) |
| MIDDLE\_BTN\_EAST\_WEST = 44 | 向东西滚动 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/uYyPmmkORSeVqAZpThYuxQ/zh-cn_image_0000002538181446.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=FB9197AD2A38D19E78AAAF49D99661E6D7214CAE4B1267745E7F4B50E6B8CCD8) |
| RUNNING\_LEFT = 45 | 后台运行中动画光标(拓展1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/gLU_qxwVRASJR0S1vvGykg/zh-cn_image_0000002569021233.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=41DE96C955C8282EDA8F45E99F4175CBFD76FF0884AFC15CB1703461792E060F) |
| RUNNING\_RIGHT = 46 | 后台运行中动画光标(拓展2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/x55JTYm-QByvN8lmfwuldA/zh-cn_image_0000002568901223.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=A6C9166910BAFE6E69EB0AF018672126E4712E6D5B019CBEA548503BA9C5837D) |
| AECH\_DEVELOPER\_DEFINED\_ICON = 47 | 圆形自定义光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/OsFQXL77QVi7xdCAvfb9tw/zh-cn_image_0000002538021522.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=C593A8ABA841AEFE9C35E217856363FA984C217F923902CCA1CDD93940059328) |
| SCREENRECORDER\_CURSOR = 48 | 录屏光标 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/NAGpdSRKRNGGD-RWvqHWyg/zh-cn_image_0000002538181448.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=CE846D061DB3E3387187491713FAD99A3A717854ED1A9E21660C131288D1B6FD) |
| LASER\_CURSOR = 49 | 
悬浮光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/kGKKmGEfS0mWELgznEiUpw/zh-cn_image_0000002569021235.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=42937D5D1ED132167F7B96E9BBE86C49E94FB29F86C0FAA7FFAA61D3DDCA5870) |
| LASER\_CURSOR\_DOT = 50 | 

点击光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/xKz6QXamT5qgh7QWlgrQoQ/zh-cn_image_0000002568901225.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=E27775C881F07BEAC68DA676C27E1CCCA4698C5F4DBA8C0D18320FBFC6E397A8) |
| LASER\_CURSOR\_DOT\_RED = 51 | 

激光笔光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。

空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/MtkLmnvVS3eMtXDiBGhFKA/zh-cn_image_0000002538021524.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=BEDF259111F0C46CB8F7CB6BEBFE2AF8409A23ACB8B507132DBE8A6BA61E7FAB) |
| DEVELOPER\_DEFINED\_ICON = -100 | 自定义光标，开发者可使用[OH\_Input\_SetCustomCursor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_setcustomcursor)设置自定义光标，不支持使用[OH\_Input\_SetPointerStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_setpointerstyle)直接设置。 | 自定义光标样式，通过接口设置。 |
