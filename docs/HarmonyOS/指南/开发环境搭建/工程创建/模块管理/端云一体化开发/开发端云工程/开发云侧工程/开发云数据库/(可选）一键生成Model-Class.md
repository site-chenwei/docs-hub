---
title: "(可选）一键生成Model Class"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "端云一体化开发"
  - "开发端云工程"
  - "开发云侧工程"
  - "开发云数据库"
  - "(可选）一键生成Model Class"
captured_at: "2026-04-17T01:36:43.573Z"
---

# (可选）一键生成Model Class

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

#### 生成Server Model

1.  右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Vk6zRO_VSjO-8oSwV_xOAA/zh-cn_image_0000002214704509.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=EC897C5D9A59AE6D4AAD5AE9C5A4C49405FA91C2A77123F06E6C56C57F9A05D2)
    
2.  选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/t5gCZJ_LSu2NzzWd9liyRw/zh-cn_image_0000002214704513.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=C3B549A86B74CAF949F8A7D8D56ACC8D0F6B773431F2DEA024444C4255815C54)
    
3.  点击“OK”。
    
    指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/UDHO0KLpT02GCpjUFLA8Sg/zh-cn_image_0000002179498268.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=B6E96977C20E68E23C873D169449D5C174F8C9CF77D0B4E089EB30DBA4D7A359)
    
4.  在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。
    
    "dependencies": {
      "@hw-agconnect/cloud-server": "latest"
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/pXSQZw-ATWKfCAgHjSY1Dw/zh-cn_image_0000002308906729.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=CF2E49E5BDFA7F001B62651188457C60F027041D76E1A4B1D26F9AC7AB307FB8)
    
5.  在云对象文件idGenerator.ts中添加如下代码，实现云函数访问云数据库。
    
    import { cloud } from '@hw-agconnect/cloud-server'; 
    import { Post } from './Post'; // Post是Server Model 
    
    // Demo是Post对象类型使用的存储区名
    const collection = cloud.database({ zoneName: 'Demo' }).collection(Post);
    
    // IdGenerator云对象，实现了对Post对象类型的查询和更新
    export class IdGenerator {
      query() {
        return collection.query().get();
      }
    
      upsert(posts: Post\[\]) {
        return new Promise((resolve, reject) => {
          collection.upsert(posts.map(post => Post.parseFrom(post)))
            .then(result => resolve({ result }))
            .catch(err => reject(err))
        });
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/we2NYWmaQhmFF-E3gXo86g/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=F47A804936E430585FB08CB90B1D3FCEC7D6847CE13A88538A4EC0AC313548C2)
    
    如果定义的云数据库表字段中包含ByteArray或Date类型的字段，在插入或者更新云数据库时需要使用Server Model的parseFrom方法将入参转化成API识别的类型，例如上述示例中的Post.parseFrom方法。
    

#### 生成Client Model

1.  右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Client Model”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/HxR_Qz_8RhSxJIyJHkP1Fg/zh-cn_image_0000002214858901.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=ED5A1C48B6F2A8F8F24FFD82C900045A25C8240898E41F8FA53108320657EF80)
    
2.  选择生成的Client Model文件存放的端侧目录。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/7DtvsUrVSG-7RwOZoyAzhQ/zh-cn_image_0000002214858897.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=BD4DF5BE2C31F5EC6F977F0C01933EE6BC9B550B673CEE45A4A262AA71F48303)
    
3.  点击“OK”。
    
    指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/-ByLLKklSa22vWzKhAoLAQ/zh-cn_image_0000002179338564.png?HW-CC-KV=V1&HW-CC-Date=20260417T013644Z&HW-CC-Expire=86400&HW-CC-Sign=BC45F76F0AB0095FA890BC89D3E0AE353073F569BB9F744779537FD00163EAB8)
