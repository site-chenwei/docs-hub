---
title: "编辑图片Exif信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(ArkTS)"
  - "图片编辑和处理"
  - "编辑图片Exif信息"
captured_at: "2026-04-17T01:36:05.944Z"
---

# 编辑图片Exif信息

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF、WEBP23+、DNG23+格式，且需要图片包含Exif信息。

在图库等应用中，需要查看或修改数码照片的Exif信息。当摄像机的手动镜头参数无法自动写入到Exif信息中，或者相机断电等原因会导致拍摄时间出错时，可手动修改错误的Exif数据。

系统目前仅支持对部分Exif信息的查看和修改，具体支持的范围请参见：[Exif信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#propertykey7)。需要注意的是，DNG格式图片仅支持读取Exif信息，不支持修改。

#### 开发步骤

Exif信息的读取与编辑相关的API详细介绍请参考[getImageProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource#getimageproperty11)等接口。

获取图片，创建ImageSource。读取、编辑Exif信息。示例代码如下：

1.  导入相关模块包。
    
    // 导入相关模块包。
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  获取指定key的Exif信息接口示例。
    
    // 获取指定key的Exif信息接口示例
    async getExif(imageSourceApi: image.ImageSource | undefined, key: image.PropertyKey): Promise<string> {
      let info: string = '';
      if (imageSourceApi) {
        console.info('getExif: The imageSourceApi is not undefined.');
        // 根据传入的key获取其Exif信息
        let options: image.ImagePropertyOptions = { index: 0, defaultValue: 'This key has no value!' };
        try {
          let data = await imageSourceApi.getImageProperty(key, options);
          info = \`Succeeded in getting the ${key}'s value: ${data}.\`;
          console.info(info);
          return info; // 获取key值成功时返回获取到的key值
        } catch (error) {
          info =
            \`Failed to get the value of the ${key} with error: ${error}.\`;
          console.error(info);
          return info; // 获取key值失败时返回错误信息
        }
      } else {
        info = 'getExif: The imageSourceApi is undefined.';
        console.info(info);
        return info; // 如果 imageSourceApi 是 undefined，则直接返回信息
      }
    }
    
3.  修改指定key的Exif信息的接口示例。
    
    // 修改指定key的Exif信息的接口示例
    async modifyExif(imageSourceApi: image.ImageSource | undefined, key: image.PropertyKey, value: string)
      : Promise<string> {
      let info: string = '';
      if (imageSourceApi) {
        // 编辑EXIF信息
        try {
          await imageSourceApi.modifyImageProperty(key, value);
          try {
            let modifyValue = await imageSourceApi.getImageProperty(key)
            info = \`The ${key}'s value is modified to ${modifyValue}.\`
            console.info(info);
            return info; // 获取key值成功时返回修改成功信息
          } catch (error) {
            console.error(\`Failed to get the the ${key}'s value with ${error}\`);
            console.error(info);
            return info; // 获取key值失败时返回错误信息
          }
        } catch (error) {
          info = \`Failed to modify the ${key}'s value with ${error}\`;
          console.error(info);
          return info; // 修改key值失败时返回错误信息
        }
      } else {
        info = 'modifyExif: The imageSourceApi is undefined.';
        console.info(info);
        return info; // 如果 imageSourceApi 是 undefined，直接返回信息
      }
    }
