---
title: "（可选）同步云端代码至DevEco Studio工程"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "端云一体化开发"
  - "开发端云工程"
  - "（可选）同步云端代码至DevEco Studio工程"
captured_at: "2026-04-17T01:36:43.577Z"
---

# （可选）同步云端代码至DevEco Studio工程

DevEco Studio还支持您将AGC云端当前项目下的代码同步至本地工程，包括之前从本地部署到AGC云端的代码、以及在AGC云端编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](#section588213529814)、[仅同步云数据库](#section474014335350)、[一键同步云侧代码](#section1198316575339)。

#### 同步云函数/云对象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/4oGGQG71QxSJgXdfdvRFjw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=55DA16A508C8E1932B1FE3AFB80DDC06C74E923F4345C904DEE9BAA2D03C4BEB)

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

#### \[h2\]同步单个云函数/云对象

云函数/云对象部署到AGC云端后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1.  右击云对象目录，选择“Sync '_云对象名_'”。下文以云对象“id-generator”为例。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/w7quFNMHRIyfMAsc0N5YFw/zh-cn_image_0000002214704461.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=E8F7EB46539436FF0D4E070F622A25B53601DBE060E27E24E68063C6565013BE)
    
2.  在确认弹框中点击“Overwrite”，AGC云端的云对象“id-generator”将覆盖更新本地云对象“id-generator”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/RcVZPJs5SomPHFxSCZJN3g/zh-cn_image_0000002214704477.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=04851CAAA0C8B8F5A0F98A036FADD887CFB98C7596B102C01D3C8BBF50AF8FA4)
    
3.  等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/INFUrf_TQa-rtFFkShK51w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=8C6FA75D4EAE94422D36D86CAD39E7541F3A4DC3ABF65B42F3AEDAD875587F64)
    
    后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Jcm4weP5RU63oNY0c9_dow/zh-cn_image_0000002179498228.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=F3C5A82E7CB61405A11A88F2FF0DD941BBD30627050E6F15D907C4DB298A58E1)
    

#### \[h2\]批量同步云函数/云对象

批量同步云函数/云对象即将AGC云端当前项目下的所有云函数/云对象同步至本地工程。

1.  右击“cloudfunctions”目录，选择“Sync Cloud Functions”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/H0T-4jOMRiuuQwq_ZsaOcw/zh-cn_image_0000002179338512.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=C16F29CC1493579178B77F8AB6823FDABA53B14F0C5C00EB4FA1496BBDC70291)
    
2.  弹窗提示您本地工程下存在同名云函数/云对象。
    
    -   选择“Skip”，同步时将跳过本地同名云函数/云对象。
    -   选择“Overwrite”，AGC云端的云函数/云对象将覆盖更新本地同名云函数/云对象。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/iRO7zPDmTNGpKuSrwcUOMQ/zh-cn_image_0000002214704441.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=BEA3EABC44BF783E5A0D2501A57EC10C32337336D1E8A2F7071545A99901A263)
    
3.  如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。
    
    如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/WYKNpSClTo-OFnHpTiTn9Q/zh-cn_image_0000002214704485.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=A06A3656611FB9E1F4CA1D4A46F78EEBBCAA040F7A1B6BECA7050BED28A7CAAD)
    
4.  如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。
    
    如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-_备份时间_.backup”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/DGMDh_7KTGu4_lCXhsLQEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=3FB23A26C8888EFD8308CF7CCFF1B148F586ECFBACC85C9A1D98271546E95AB8)
    
    后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/_8rpgXY2ScOFMXSemaHFwA/zh-cn_image_0000002179338508.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=71397C378D422C5FE90B200AE8A7709180677AE9D8ADDF1592D77D02FFFF55E8)
    

#### 同步云数据库

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/cFkpVLShQyGFX9AaM4C4Mg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=8950E09026FCC67EB69146ACB821782E185D0F01F55CE979F169D9859FEC39AC)

目前仅支持同步对象类型。

#### \[h2\]同步单个对象类型

对象类型部署到AGC云端后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1.  右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/PNfDvXEuQuyQKRH-c5e5XQ/zh-cn_image_0000002179498216.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=36BE656798AF3A3591D213DCF02C238A98D0BB855B610B66AAA3F22B7C04A871)
    
2.  在确认弹框中点击“Overwrite”，AGC云端的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/a_XyeZV0SN-LzxY_QK1Mqg/zh-cn_image_0000002214704465.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=F93918D21600519944F881E061EAC6E85C0DB10F1934E1FBDAB35FF2DA6F6A7D)
    
3.  等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。
    
    -   如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
    -   如果云端和本地的同名对象类型内容完全一致，则不生成备份。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uJddIgqJT022IujkCXgpZQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=7327FBD6A262970082804E2F25E9F94E64DC4C3AB94E894586480DD78A7E333A)
    
    后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/YQhDjD77RR--ShrI9slxUg/zh-cn_image_0000002214704445.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=55B3507630ACFF10E76B0DDC21DC9A583E59328CE79D5E662792F50DACC75B77)
    

#### \[h2\]批量同步对象类型

您可以将AGC云端当前项目下所有的对象类型一键同步至本地。

1.  右击“objecttype”目录，选择“Sync Object Type”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/fHfpDDN3Q96D9GbPvEUgzQ/zh-cn_image_0000002179338532.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=549159650386E4A0511B4E2DD85CBA448F13CF13A055AD8B95A294AB7B449426)
    

2.  弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。
    
    -   选择“Skip”，同步时将跳过本地同名对象类型。
    -   选择“Overwrite”，AGC云端的对象类型将覆盖更新本地同名对象类型。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/GVJzUToQT8OB_G-28zw0bQ/zh-cn_image_0000002179498208.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=0E9A60D97B9111B45C70543EF8EB456E322FB729DAF3B3D6B0EC132D4D1FC3D9)
    
3.  如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。
    
    如下图，“objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/WklVwSoqT32untaX4WsG4Q/zh-cn_image_0000002179498196.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=A5BD6A494EF01D4E4C11F311506F132486262E99A796F1AFCCEE102BCC3CCB43)
    
4.  如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。
    
    -   如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
    -   如果云端和本地的同名对象类型内容完全一致，则不生成备份。
    
    如下图，“objecttype”目录下生成了“test\_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test\_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-_备份时间_.backup”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/JPw1aPduT1C7b9OkMtzd0Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=39F5D0CE8897D706109ECCD84FACB03E6D498F328E7B632E03F6B0D5881AA832)
    
    后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/La8XDxLsSuuBG1-opQL36w/zh-cn_image_0000002214704489.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=499345196455A7696E03BE39455A23D7FC2CD2302A5CE3E8962F4923030C9D0A)
    

#### 一键同步云侧代码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/M5docY5ERmiR2FflQRul3A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=FED6B4924C2F6B67390983E3CD77493CB8D59A287E6A56A3E7124347556BFB68)

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1.  右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/E4w6RbGUTve-25ATK2POQw/zh-cn_image_0000002214858849.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=A8454B6C23FAA10BF5BD1EAA5F578BFB4FD3893A46C908EE4A08574886113742)
    
2.  弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。
    
    -   选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
    -   选择“Overwrite”，AGC云端的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Z8L5LWoQQduGoNYHUclvIg/zh-cn_image_0000002214858861.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=71197347339B4326686000586ADFE313D21DC345D9936E90AB810795ED008D3A)
    
3.  如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。
    
    如下图：
    
    -   “objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
    -   “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/WsdxIbnHRn-uazp-5w0UeA/zh-cn_image_0000002179498236.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=DD39E45AE3C822672022192E1DA3B7B133D27C81D0EB7770FA6F8116422407A3)
    
4.  如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。
    
    -   如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
    -   如果云端和本地的同名对象类型内容完全一致，则不生成备份。
    -   无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。
    
    如下图：
    
    -   “objecttype”目录下生成了“test \_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test \_object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-_备份时间_.backup”。
    -   “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-_备份时间_.backup”。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/dZe96BLzSz6A8xxQ6aRz0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=3E57D9B2B3E676DBBEE79F759154B99DD54D688C7F4B9AF785FB0C7B0E69FFC4)
        
        后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/nU-ihn1iRcWKiW71u1wviQ/zh-cn_image_0000002179338516.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=853071FB0910D41458188C9AB8E3F709920A44284CEB86AB1E61BC9685007318)
