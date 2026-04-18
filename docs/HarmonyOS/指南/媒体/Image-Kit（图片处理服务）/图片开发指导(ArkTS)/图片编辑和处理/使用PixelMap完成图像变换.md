---
title: "使用PixelMap完成图像变换"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(ArkTS)"
  - "图片编辑和处理"
  - "使用PixelMap完成图像变换"
captured_at: "2026-04-17T01:36:05.847Z"
---

# 使用PixelMap完成图像变换

图片处理指对PixelMap进行相关的操作，如获取图片信息、裁剪、缩放、偏移、旋转、翻转、设置透明度、读写像素数据等。图片处理主要包括图像变换、[位图操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-pixelmap-operation)，本文介绍图像变换。

#### 开发步骤

图像变换相关API的详细介绍请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)。

1.  完成[图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding)，获取PixelMap对象。
    
2.  获取图片信息。
    
    ```ts
    import { BusinessError } from '@kit.BasicServicesKit';
    // 获取图片大小。
    pixelMap.getImageInfo().then( (info : image.ImageInfo) => {
      console.info('info.width = ' + info.size.width);
      console.info('info.height = ' + info.size.height);
    }).catch((err : BusinessError) => {
      console.error("Failed to obtain the image pixel map information.And the error is: " + err);
    });
    ```
    
3.  进行图像变换操作。
    
    原图：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/G45jHWGOQlmgS2g6uN5PAw/zh-cn_image_0000002568899237.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=27A1E1C8DCB77004531754B31CE4960F1BACE363294E58C6AD35660298E3A66F)
    
    -   裁剪
        
        ```ts
        // x：裁剪起始点横坐标0。
        // y：裁剪起始点纵坐标0。
        // height：裁剪高度400，方向为从上往下（裁剪后的图片高度为400）。
        // width：裁剪宽度400，方向为从左到右（裁剪后的图片宽度为400）。
        pixelMap.crop({x: 0, y: 0, size: { height: 400, width: 400 } });
        ```
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/mdOV2MLFRri9_ft4087flQ/zh-cn_image_0000002538019532.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=6FF41552DC9D8FF958EC291F320E81A6E9120CB7A85FF33FBB0007DD3276A442)
        
    -   缩放
        
        ```ts
        // 宽为原来的0.5。
        // 高为原来的0.5。
        pixelMap.scale(0.5, 0.5);
        ```
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/6vownfAzT0m_PL4Y3c42Dg/zh-cn_image_0000002538179462.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=EE5ADD061EFF2250C20AA4680D1E42F532B7FDC98BB285D8E85F0D61A28E196E)
        
    -   偏移
        
        ```ts
        // 向下偏移100。
        // 向右偏移100。
        pixelMap.translate(100, 100);
        ```
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/G0Slz15-QJGCGpsrfDSBVQ/zh-cn_image_0000002569019247.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=78CA065586691C114459D2DF7209FE0245B77E537148905558D09A251FF9DBF0)
        
    -   旋转
        
        ```ts
        // 顺时针旋转90°。
        pixelMap.rotate(90);
        ```
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/YsIcBWGwSN6saZmvQj25xA/zh-cn_image_0000002568899239.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=AF24FFB2464E1851E6B0930AAA4E17FCDB4F949D55179271F72F66E343A140A2)
        
    -   翻转
        
        ```ts
        // 垂直翻转。
        pixelMap.flip(false, true);
        ```
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/_CO_CRSqQpyz5Ha4GZ6E_A/zh-cn_image_0000002538019534.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=CEBA1AC8182E0D509DA411EE3B993FC92F3CBA11A29F6F5703D01AB12D73F926)
        
        ```ts
        // 水平翻转。
        pixelMap.flip(true, false);
        ```
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/aIG_Mqh9Q3OAsLjpKZwLWw/zh-cn_image_0000002538179464.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=49F548116401401969E67D6BF05530D6AEF77DAE255ADCC5A34EB52B8D997CF6)
        
    -   透明度
        
        ```ts
        // 透明度0.5。
        pixelMap.opacity(0.5);
        ```
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/3V9iWVBCTz-CdhhPenMVgg/zh-cn_image_0000002569019249.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=7D49BA3FA322F16EBB748F0C7DDD413FB73CA363478BB8C23FB9C491C1547B30)
        

#### 示例代码

-   [拼图](https://gitcode.com/HarmonyOS_Samples/game-puzzle)
