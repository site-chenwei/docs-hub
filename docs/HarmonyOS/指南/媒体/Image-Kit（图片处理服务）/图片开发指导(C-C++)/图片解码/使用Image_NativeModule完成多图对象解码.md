---
title: "使用Image_NativeModule完成多图对象解码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-picture-c"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(C/C++)"
  - "图片解码"
  - "使用Image_NativeModule完成多图对象解码"
captured_at: "2026-04-17T01:36:06.009Z"
---

# 使用Image\_NativeModule完成多图对象解码

创建ImageSource实例，解码获取Picture，然后释放ImageSource实例。

#### 开发步骤

#### \[h2\]添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so 以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```

#### \[h2\]Native接口调用

具体接口说明请参考[Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\\src\\main\\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**解码接口使用示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/xqOIsoO7QR-aC1L5HVaCkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=A1FAC5F49D051A95FEC55AA1FC94171ED8CCF2CC6376360BFB826056E02572AD)

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1.  导入相关头文件。
    
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_native.h>
    #include <multimedia/image\_framework/image/image\_packer\_native.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include <multimedia/image\_framework/image/picture\_native.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
2.  日志宏定义可参考下述代码按实际需求自行修改。
    
    #undef LOG\_DOMAIN
    #undef LOG\_TAG
    #define LOG\_DOMAIN 0x3200
    #define LOG\_TAG "IMAGE\_SAMPLE"
    
3.  定义ImagePictureNative类。
    
    class ImagePictureNative {
    public:
        Image\_ErrorCode errorCode = IMAGE\_SUCCESS;
        OH\_DecodingOptionsForPicture \*options = nullptr;
        OH\_ImagePackerNative \*imagePacker = nullptr;
        OH\_PackingOptions \*packerOptions = nullptr;
        OH\_PictureNative \*picture = nullptr;
        OH\_ImageSourceNative \*source = nullptr;
        ImagePictureNative() {}
        ~ImagePictureNative() {}
    };
    
4.  创建一个ImagePictureNative实例。
    
    static ImagePictureNative \*g\_thisPicture = new ImagePictureNative();
    
5.  定义ImageAuxiliaryPictureNative类。
    
    class ImageAuxiliaryPictureNative {
    public:
        Image\_ErrorCode errorCode = IMAGE\_SUCCESS;
        Image\_AuxiliaryPictureType type = AUXILIARY\_PICTURE\_TYPE\_GAINMAP;
        OH\_AuxiliaryPictureNative \*auxiliaryPicture = nullptr;
        size\_t buffSize = 640 \* 480 \* 4; // 辅助图size：\`长 \* 宽 \* 每个像素占用的字节数\`。
        ImageAuxiliaryPictureNative() {}
        ~ImageAuxiliaryPictureNative() {}
    };
    
6.  创建一个ImageAuxiliaryPictureNative实例。
    
    static ImageAuxiliaryPictureNative \*g\_thisAuxiliaryPicture  = new ImageAuxiliaryPictureNative();
    
7.  创建GetJsResult函数处理napi返回值。
    
    // 处理napi返回值。
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
8.  创建解码参数，配置解码参数，调用解码接口进行解码并获取辅助图。
    
    // 释放ImageSource。
    napi\_value ReleasePictureSource(napi\_env env, napi\_callback\_info info)
    {
        if (g\_thisPicture->source != nullptr) {
            g\_thisPicture->errorCode = OH\_ImageSourceNative\_Release(g\_thisPicture->source);
            g\_thisPicture->source = nullptr;
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        
        if (g\_thisPicture->picture != nullptr) {
            g\_thisPicture->errorCode = OH\_PictureNative\_Release(g\_thisPicture->picture);
            g\_thisPicture->picture = nullptr;
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        
        OH\_LOG\_DEBUG(LOG\_APP, "ReleasePictureSource source is null !");
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // 创造解码参数。
    napi\_value CreateDecodingOptions(napi\_env env, napi\_callback\_info info)
    {
        g\_thisPicture->errorCode = OH\_DecodingOptionsForPicture\_Create(&g\_thisPicture->options);
    
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_DecodingOptionsForPicture\_Create failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_DecodingOptionsForPicture\_Create success !");
        }
    
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // 配置解码参数 从应用层传入。
    napi\_value SetDesiredAuxiliaryPictures(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok || argc < 1 || args\[0\] == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed !");
            return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
        }
    
        uint32\_t length = 0;
        napi\_get\_array\_length(env, args\[0\], &length);
        if (length <= 0) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_array\_length failed !");
            return GetJsResult(env, IMAGE\_UNKNOWN\_ERROR);
        }
        Image\_AuxiliaryPictureType typeList\[length\];
        for (int index = 0; index < length; index++) {
            napi\_value element;
            uint32\_t ulType = 0;
            napi\_get\_element(env, args\[0\], index, &element);
            napi\_get\_value\_uint32(env, element, &ulType);
            typeList\[index\] = static\_cast<Image\_AuxiliaryPictureType>(ulType);
            OH\_LOG\_DEBUG(LOG\_APP, "ulType is :%{public}d", ulType);
        }
        
        // 调用OH\_DecodingOptionsForPicture\_Create接口创建DecodingOptions。
        CreateDecodingOptions(env, info);
        g\_thisPicture->errorCode =
            OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures(g\_thisPicture->options, typeList, length);
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures failed,errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures success !");
        }
    
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // 解码。
    napi\_value CreatePictureByImageSource(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok || argc < 1 || args\[0\] == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "CreatePicture\_ napi\_get\_cb\_info failed !");
            return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
        }
        
        char filePath\[MAX\_SIZE\];
        size\_t pathSize;
        napi\_get\_value\_string\_utf8(env, args\[0\], filePath, MAX\_SIZE, &pathSize);
    
        g\_thisPicture->errorCode = OH\_ImageSourceNative\_CreateFromUri(filePath, pathSize, &g\_thisPicture->source);
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_CreateFromUri failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_ImageSourceNative\_CreateFromUri success !");
        }
        
        // 先创建解码参数，再进行解码，此处创建解码参数的接口在SetDesiredAuxiliaryPictures实现。
        g\_thisPicture->errorCode =
            OH\_ImageSourceNative\_CreatePicture(g\_thisPicture->source, g\_thisPicture->options, &g\_thisPicture->picture);
        
        // 释放options。
        OH\_DecodingOptionsForPicture\_Release(g\_thisPicture->options);
        g\_thisPicture->options = nullptr;
        
        g\_thisAuxiliaryPicture ->errorCode = OH\_PictureNative\_GetAuxiliaryPicture(g\_thisPicture->picture,
            g\_thisAuxiliaryPicture ->type, &g\_thisAuxiliaryPicture ->auxiliaryPicture);
        if (g\_thisAuxiliaryPicture ->errorCode == IMAGE\_SUCCESS) {
            uint8\_t\* buff = new uint8\_t\[g\_thisAuxiliaryPicture ->buffSize\];
            OH\_AuxiliaryPictureNative\_ReadPixels(g\_thisAuxiliaryPicture ->auxiliaryPicture, buff,
                &g\_thisAuxiliaryPicture ->buffSize);
            OH\_AuxiliaryPictureNative\_Release(g\_thisAuxiliaryPicture ->auxiliaryPicture);
            g\_thisAuxiliaryPicture ->auxiliaryPicture = nullptr;
            delete \[\]buff;
        }
        
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "ImageSourceNative\_CreatePicture failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "ImageSourceNative\_CreatePicture success !");
        }
        
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
