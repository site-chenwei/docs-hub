---
title: "使用Image_NativeModule完成多图对象编码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-picture-c"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(C/C++)"
  - "图片编码"
  - "使用Image_NativeModule完成多图对象编码"
captured_at: "2026-04-17T01:36:06.081Z"
---

# 使用Image\_NativeModule完成多图对象编码

图像编码类，用于创建以及释放ImagePacker实例，并编码多图对象。

#### 开发步骤

#### \[h2\]添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_packer.so 以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

#### \[h2\]Native接口调用

具体接口说明请参考[Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。

在DevEco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\\src\\main\\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**编码接口使用示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/HytVaUDbSu2_UyfHgaKOmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=F83159759E7C19B8571D21FF1D9A8C2146BA88405FB43AFA14B412C3D21BDC28)

根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，编码参数中的编码格式image\_MimeType设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。

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
    
3.  定义用于图像处理的常量。
    
    #define AUTO 0
    #define SDR 1
    const int MAX\_SIZE = 1024;
    const int MAX\_FORMAT\_LENGTH = 20;
    
4.  定义ImagePictureNative类。
    
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
    
5.  创建ImagePictureNative的一个实例。
    
    static ImagePictureNative \*g\_thisPicture = new ImagePictureNative();
    
6.  创建GetJsResult函数处理napi返回值。
    
    // 处理napi返回值。
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
7.  创建ImagePacker实例，指定编码参数后，将Picture多图对象编码至文件或缓冲区。
    
    // 设置编码参数。
    void SetPackOptions(OH\_PackingOptions \*packerOptions,
                        Image\_MimeType format,
                        uint32\_t quality,
                        bool needsPackProperties,
                        int32\_t desiredDynamicRange)
    {
        OH\_PackingOptions\_SetMimeType(packerOptions, &format);
        OH\_PackingOptions\_SetQuality(packerOptions, quality);
        OH\_PackingOptions\_SetNeedsPackProperties(packerOptions, needsPackProperties);
        OH\_PackingOptions\_SetDesiredDynamicRange(packerOptions, desiredDynamicRange);
    }
    
    // PackToData。
    napi\_value PackToDataFromPicture(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed!");
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        
        size\_t outDataSize = 10000 \* 10000;
        uint8\_t \*outData = new uint8\_t\[outDataSize\];
    
        if (g\_thisPicture->packerOptions == nullptr) {
            g\_thisPicture->errorCode = OH\_PackingOptions\_Create(&g\_thisPicture->packerOptions);
        }
        if (g\_thisPicture->imagePacker == nullptr) {
            g\_thisPicture->errorCode = OH\_ImagePackerNative\_Create(&g\_thisPicture->imagePacker);
        }
        
        char strFormat\[MAX\_FORMAT\_LENGTH\];
        size\_t strFormatSize;
        napi\_get\_value\_string\_utf8(env, args\[0\], strFormat, MAX\_FORMAT\_LENGTH, &strFormatSize);
        OH\_LOG\_DEBUG(LOG\_APP, "PackToDataFromPicture format: %{public}s", strFormat);
    
        Image\_MimeType format;
        format.size = strFormatSize;
        format.data = const\_cast<char \*>(strFormat);
        uint32\_t quality = 95;
        bool needsPackProperties = true;
        int32\_t desiredDynamicRange = AUTO;
        SetPackOptions(g\_thisPicture->packerOptions, format, quality, needsPackProperties, desiredDynamicRange);
        // 确保picture对象已被创建。
        g\_thisPicture->errorCode = OH\_ImagePackerNative\_PackToDataFromPicture(
            g\_thisPicture->imagePacker, g\_thisPicture->packerOptions, g\_thisPicture->picture, outData, &outDataSize);
        
        // 释放imagePacker和packerOptions。
        OH\_PackingOptions\_Release(g\_thisPicture->packerOptions);
        g\_thisPicture->packerOptions = nullptr;
        OH\_ImagePackerNative\_Release(g\_thisPicture->imagePacker);
        g\_thisPicture->imagePacker = nullptr;
        
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImagePackerNative\_PackToDataFromPicture failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            delete\[\] outData;
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_ImagePackerNative\_PackToDataFromPicture success !");
        }
        delete\[\] outData;
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // PackToFile。
    napi\_value PackToFileFromPicture(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 2;
        napi\_value args\[2\] = {nullptr};
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed!");
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        uint32\_t fd = 0;
        napi\_get\_value\_uint32(env, args\[0\], &fd);
    
        if (g\_thisPicture->packerOptions == nullptr) {
            g\_thisPicture->errorCode = OH\_PackingOptions\_Create(&g\_thisPicture->packerOptions);
        }
        if (g\_thisPicture->imagePacker == nullptr) {
            g\_thisPicture->errorCode = OH\_ImagePackerNative\_Create(&g\_thisPicture->imagePacker);
        }
        
        char strFormat\[MAX\_FORMAT\_LENGTH\];
        size\_t strFormatSize;
        napi\_get\_value\_string\_utf8(env, args\[1\], strFormat, MAX\_FORMAT\_LENGTH, &strFormatSize);
        OH\_LOG\_INFO(LOG\_APP, "PackToFileFromPicture format: %{public}s", strFormat);
    
        Image\_MimeType format;
        format.size = strFormatSize;
        format.data = const\_cast<char \*>(strFormat);
        uint32\_t quality = 95;
        bool needsPackProperties = false;
        int32\_t desiredDynamicRange = SDR;
        SetPackOptions(g\_thisPicture->packerOptions, format, quality, needsPackProperties, desiredDynamicRange);
        // 确保picture对象已被创建。
        g\_thisPicture->errorCode = OH\_ImagePackerNative\_PackToFileFromPicture(
            g\_thisPicture->imagePacker, g\_thisPicture->packerOptions, g\_thisPicture->picture, fd);
        
        // 释放imagePacker和packerOptions。
        OH\_PackingOptions\_Release(g\_thisPicture->packerOptions);
        g\_thisPicture->packerOptions = nullptr;
        OH\_ImagePackerNative\_Release(g\_thisPicture->imagePacker);
        g\_thisPicture->imagePacker = nullptr;
        
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImagePackerNative\_PackToFileFromPicture failed,"
                         "errCode: %{public}d.", g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_ImagePackerNative\_PackToFileFromPicture success !");
        }
    
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
