---
title: "使用Image_NativeModule完成图片解码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(C/C++)"
  - "图片解码"
  - "使用Image_NativeModule完成图片解码"
captured_at: "2026-04-17T01:36:06.004Z"
---

# 使用Image\_NativeModule完成图片解码

创建ImageSource，获取位图的宽、高信息，以及释放ImageSource实例。

从API version 22开始支持对部分专业相机格式图片的预览图解码，具体格式包括：CR2、CR3、ARW、NEF、RAF、NRW、ORF、RW2、PEF、SRW。

#### 开发步骤

#### \[h2\]添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so、libpixelmap.so以及日志功能依赖的libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libpixelmap.so)
```

#### \[h2\]Native接口调用

具体接口说明请参考[Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\\src\\main\\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**解码接口使用示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/dBHS8V4ITKmcgAFUMtAeBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=8D74D8DCA5F6374D48A0BC1D9D1CFFEAD2545C44D9026DAE2C2EDD83C7B7CE81)

部分接口（如：[OH\_ImageSourceNative\_GetSupportedFormats](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_getsupportedformats)）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1.  导入相关头文件。
    
    #include <string>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include "napi/native\_api.h"
    #include <multimedia/image\_framework/image/image\_common.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
2.  日志宏定义可参考下述代码按实际需求自行修改。
    
    #undef LOG\_DOMAIN
    #undef LOG\_TAG
    #define LOG\_DOMAIN 0x3200
    #define LOG\_TAG "IMAGE\_SAMPLE"
    
3.  定义ImageSourceNative类。
    
    class ImageSourceNative {
    public:
        OH\_ImageSource\_Info \*imageInfo;
        OH\_ImageSourceNative \*source = nullptr;
        OH\_PixelmapNative \*resPixMap = nullptr;
        OH\_Pixelmap\_ImageInfo \*pixelmapImageInfo = nullptr;
        uint32\_t frameCnt = 0;
        ImageSourceNative() {}
        ~ImageSourceNative() {}
    };
    
4.  创建ImageSourceNative的一个实例。
    
    static ImageSourceNative \*g\_thisImageSource = new ImageSourceNative();
    
5.  创建GetJsResult函数处理napi返回值。
    
    // 处理napi返回值。
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
6.  常量定义。
    
    const int MAX\_STRING\_LENGTH = 1024;
    
7.  创建ImageSource实例。
    
    // 返回ErrorCode。
    napi\_value ReturnErrorCode(napi\_env env, Image\_ErrorCode errCode, std::string funcName)
    {
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "%{public}s failed, errCode: %{public}d.", funcName.c\_str(), errCode);
            return GetJsResult(env, errCode);
        }
        return GetJsResult(env, errCode);
    }
    
    // 获取解码能力范围。
    napi\_value GetSupportedFormats(napi\_env env, napi\_callback\_info info)
    {
        Image\_MimeType\* mimeType = nullptr;
        size\_t length = 10;
        Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetSupportedFormats(&mimeType, &length);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_GetSupportedFormats failed, "
                         "errCode: %{public}d.", errCode);
            return GetJsResult(env, errCode);
        }
        for (size\_t count = 0; count < length; count++) {
            OH\_LOG\_INFO(LOG\_APP, "Decode supportedFormats: %{public}s", mimeType\[count\].data);
        }
        return GetJsResult(env, errCode);
    }
    
    // 创建ImageSource实例。
    napi\_value CreateImageSource(napi\_env env, napi\_callback\_info info)
    {
        napi\_value argValue\[1\] = {nullptr};
        size\_t argCount = 1;
        if (napi\_get\_cb\_info(env, info, &argCount, argValue, nullptr, nullptr) != napi\_ok || argCount < 1 ||
            argValue\[0\] == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "CreateImageSource napi\_get\_cb\_info failed!");
            return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
        }
    
        char name\[MAX\_STRING\_LENGTH\];
        size\_t nameSize = MAX\_STRING\_LENGTH;
        napi\_get\_value\_string\_utf8(env, argValue\[0\], name, MAX\_STRING\_LENGTH, &nameSize);
    
        Image\_ErrorCode errCode = OH\_ImageSourceNative\_CreateFromUri(name, nameSize, &g\_thisImageSource->source);
        return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_CreateFromUri");
    }
    
8.  在创建ImageSource实例后，进行指定属性值的获取和修改、通过解码参数创建PixelMap对象、获取图像帧数等操作。
    
    -   创建PixelMap对象。
        
        // 通过图片解码参数创建PixelMap对象。
        napi\_value CreatePixelMap(napi\_env env, napi\_callback\_info info)
        {
            // ops参数支持传入nullptr, 当不需要设置解码参数时，不用创建。
            OH\_DecodingOptions \*ops = nullptr;
            OH\_DecodingOptions\_Create(&ops);
            // 设置为AUTO会根据图片资源格式和设备支持情况进行解码，如果图片资源为HDR资源且设备支持HDR解码则会解码为HDR的pixelmap。
            OH\_DecodingOptions\_SetDesiredDynamicRange(ops, IMAGE\_DYNAMIC\_RANGE\_AUTO);
            
            OH\_PixelmapNative\_Release(g\_thisImageSource->resPixMap);
            g\_thisImageSource->resPixMap = nullptr;
            
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_CreatePixelmap(g\_thisImageSource->source,
                                                                          ops, &g\_thisImageSource->resPixMap);
            OH\_DecodingOptions\_Release(ops);
            ops = nullptr;
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_CreatePixelmap failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
        
            // 判断pixelmap是否为HDR内容。
            OH\_PixelmapImageInfo\_Create(&g\_thisImageSource->pixelmapImageInfo);
            OH\_PixelmapNative\_GetImageInfo(g\_thisImageSource->resPixMap, g\_thisImageSource->pixelmapImageInfo);
            bool pixelmapIsHdr;
            OH\_PixelmapImageInfo\_GetDynamicRange(g\_thisImageSource->pixelmapImageInfo, &pixelmapIsHdr);
            if (pixelmapIsHdr) {
                OH\_LOG\_INFO(LOG\_APP, "The pixelMap's dynamicRange is HDR.");
            }
            OH\_PixelmapImageInfo\_Release(g\_thisImageSource->pixelmapImageInfo);
            g\_thisImageSource->pixelmapImageInfo = nullptr;
            return GetJsResult(env, errCode);
        }
        
    -   创建定义图片信息的结构体对象，并获取图片信息。
        
        // 创建定义图片信息的结构体对象，并获取图片信息。
        napi\_value GetImageInfo(napi\_env env, napi\_callback\_info info)
        {
            OH\_ImageSourceInfo\_Create(&g\_thisImageSource->imageInfo);
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetImageInfo(g\_thisImageSource->source,
                                                                        0, g\_thisImageSource->imageInfo);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceInfo\_Create failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
            
            uint32\_t width;
            uint32\_t height;
            OH\_ImageSourceInfo\_GetWidth(g\_thisImageSource->imageInfo, &width);
            OH\_ImageSourceInfo\_GetHeight(g\_thisImageSource->imageInfo, &height);
            OH\_LOG\_INFO(LOG\_APP, "OH\_ImageSourceNative\_GetImageInfo success,"
                       "width: %{public}d, height: %{public}d.", width, height);
            OH\_ImageSourceInfo\_Release(g\_thisImageSource->imageInfo);
            g\_thisImageSource->imageInfo = nullptr;
            return GetJsResult(env, width); // 返回获取到info信息的width。
        }
        
    -   读取、编辑Exif信息。
        
        // 获取指定property的value值。
        napi\_value GetImageProperty(napi\_env env, napi\_callback\_info info)
        {
            napi\_value argValue\[1\] = {nullptr};
            size\_t argCount = 1;
            if (napi\_get\_cb\_info(env, info, &argCount, argValue, nullptr, nullptr) != napi\_ok || argCount < 1 ||
                argValue\[0\] == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "GetImageProperty napi\_get\_cb\_info failed!");
                return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
            }
            // 修改指定属性键的值。
            char key\[MAX\_STRING\_LENGTH\];
            size\_t keySize = MAX\_STRING\_LENGTH;
            napi\_get\_value\_string\_utf8(env, argValue\[0\], (char \*)key, sizeof(key), &keySize);
            Image\_String getKey;
            getKey.data = key;
            getKey.size = keySize;
            Image\_String getValue;
            OH\_LOG\_INFO(LOG\_APP, "OH\_ImageSourceNative\_GetImageProperty key: %{public}s.", getKey.data);
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetImagePropertyWithNull(g\_thisImageSource->source,
                                                                                    &getKey, &getValue);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_GetImageProperty failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
            napi\_value resultNapi = nullptr;
            napi\_create\_string\_utf8(env, getValue.data, getValue.size, &resultNapi);
            free(getValue.data);
            getValue.data = nullptr;
            return resultNapi;
        }
        
        // 修改指定property的value值。
        napi\_value ModifyImageProperty(napi\_env env, napi\_callback\_info info)
        {
            napi\_value argValue\[2\] = {nullptr};
            size\_t argCount = 2;
            const size\_t minCount = 2;
            if (napi\_get\_cb\_info(env, info, &argCount, argValue, nullptr, nullptr) != napi\_ok || argCount < minCount ||
                argValue\[0\] == nullptr || argValue\[1\] == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "ModifyImageProperty napi\_get\_cb\_info failed!");
                return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
            }
        
            // 获取要修改的key值。
            char key\[MAX\_STRING\_LENGTH\];
            size\_t keySize = MAX\_STRING\_LENGTH;
            napi\_get\_value\_string\_utf8(env, argValue\[0\], (char \*)key, sizeof(key), &keySize);
            Image\_String setKey;
            setKey.data = key;
            setKey.size = keySize;
            OH\_LOG\_INFO(LOG\_APP, "ModifyImageProperty key: %{public}s.", setKey.data);
            
            // 获取要修改的value值。
            char value\[MAX\_STRING\_LENGTH\];
            size\_t valueSize;
            napi\_get\_value\_string\_utf8(env, argValue\[1\], (char \*)value, MAX\_STRING\_LENGTH, &valueSize);
            Image\_String setValue;
            setValue.data = value;
            setValue.size = valueSize;
            OH\_LOG\_INFO(LOG\_APP, "ModifyImageProperty value: %{public}s.", setValue.data);
        
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_ModifyImageProperty(g\_thisImageSource->source, &setKey, &setValue);
            return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_ModifyImageProperty");
        }
        
    -   获取图像帧数。
        
        // 获取图像帧数。
        napi\_value GetFrameCount(napi\_env env, napi\_callback\_info info)
        {
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetFrameCount(g\_thisImageSource->source,
                                                                         &g\_thisImageSource->frameCnt);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_GetFrameCount failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
            return GetJsResult(env, g\_thisImageSource->frameCnt); // 返回获取到的图像帧数。
        }
        
    -   通过图片解码参数创建Pixelmap列表。
        
        // 通过图片解码参数创建Pixelmap列表。
        napi\_value CreatePixelmapList(napi\_env env, napi\_callback\_info info)
        {
            OH\_DecodingOptions \*opts = nullptr;
            OH\_DecodingOptions\_Create(&opts);
            OH\_PixelmapNative\*\* resVecPixMap = new OH\_PixelmapNative\* \[g\_thisImageSource->frameCnt\];
            size\_t outSize = g\_thisImageSource->frameCnt;
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_CreatePixelmapList(g\_thisImageSource->source,
                                                                              opts, resVecPixMap, outSize);
            OH\_DecodingOptions\_Release(opts);
            opts = nullptr;
            delete\[\] resVecPixMap;
            return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_CreatePixelmapList");
        }
        
    -   获取图像延迟时间列表。
        
        // 获取图像延迟时间列表。
        napi\_value GetDelayTimeList(napi\_env env, napi\_callback\_info info)
        {
            int32\_t \*delayTimeList = new int32\_t\[g\_thisImageSource->frameCnt\];
            size\_t size = g\_thisImageSource->frameCnt;
            OH\_LOG\_INFO(LOG\_APP, "GetDelayTimeList size: %{public}zu.", size);
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetDelayTimeList(g\_thisImageSource->source, delayTimeList, size);
            delete\[\] delayTimeList;
            return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_GetDelayTimeList");
        }
        
9.  释放ImageSource。
    
    // 释放资源。
    napi\_value ReleaseImageSource(napi\_env env, napi\_callback\_info info)
    {
        Image\_ErrorCode errCode = OH\_ImageSourceNative\_Release(g\_thisImageSource->source);
        g\_thisImageSource->source = nullptr;
        OH\_PixelmapNative\_Release(g\_thisImageSource->resPixMap);
        g\_thisImageSource->resPixMap = nullptr;
        return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_Release");
    }
