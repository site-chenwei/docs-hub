---
title: "使用Image_NativeModule完成图片编码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-c"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(C/C++)"
  - "图片编码"
  - "使用Image_NativeModule完成图片编码"
captured_at: "2026-04-17T01:36:06.099Z"
---

# 使用Image\_NativeModule完成图片编码

图像编码类，用于创建以及释放ImagePacker实例。

#### 开发步骤

#### \[h2\]添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_packer.so 以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

#### \[h2\]Native接口调用

具体接口说明请参考[Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\\src\\main\\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**编码接口使用示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/BdQSuR7DR7SkTbpn5tcZzw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=9AEFF14FF407EC5CDC9729469D65650B75D3B88F71E8A062B30192F2419AA26F)

-   根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，编码参数中的编码格式image\_MimeType设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。
    
-   部分接口（如：[OH\_ImagePackerNative\_GetSupportedFormats](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_getsupportedformats)）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。
    

1.  导入相关头文件。
    
    #include <string>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include "napi/native\_api.h"
    #include <multimedia/image\_framework/image/image\_common.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    #include <set>
    #include <multimedia/image\_framework/image/image\_packer\_native.h>
    
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
    
5.  定义一个全局变量用来记录编码所支持的格式。
    
    static std::set<std::string> g\_encodeSupportedFormats;
    
6.  创建GetJsResult函数处理napi返回值。
    
    // 处理napi返回值。
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
7.  创建ImagePacker实例后，指定编码参数，将ImageSource或PixelMap编码至文件或者缓冲区。
    
    // 获取编码能力范围。
    Image\_ErrorCode GetEncodeSupportedFormats()
    {
        Image\_MimeType\* mimeType = nullptr;
        size\_t length = 0;
        Image\_ErrorCode errCode = OH\_ImagePackerNative\_GetSupportedFormats(&mimeType, &length);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImagePackerNative\_GetSupportedFormats failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        for (size\_t count = 0; count < length; count++) {
            if (mimeType\[count\].data != nullptr) {
                g\_encodeSupportedFormats.insert(std::string(mimeType\[count\].data));
                OH\_LOG\_INFO(LOG\_APP, "Encode supportedFormats: %{public}s", mimeType\[count\].data);
            }
        }
        return IMAGE\_SUCCESS;
    }
    
    Image\_MimeType GetMimeTypeIfEncodable(const char \*format)
    {
        auto it = g\_encodeSupportedFormats.find(format);
        if (it == g\_encodeSupportedFormats.end()) {
            return {const\_cast<char \*>(""), 0};
        }
        return {const\_cast<char \*>(format), strlen(format)};
    }
    
    Image\_ErrorCode packToFileFromImageSourceTest(int fd, OH\_ImageSourceNative\* imageSource)
    {
        // 创建ImagePacker实例。
        OH\_ImagePackerNative \*testPacker = nullptr;
        Image\_ErrorCode errCode = OH\_ImagePackerNative\_Create(&testPacker);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_ImagePackerNative\_Create failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        // 获取编码能力范围。
        errCode = GetEncodeSupportedFormats();
        if (errCode != IMAGE\_SUCCESS) {
            OH\_ImagePackerNative\_Release(testPacker);
            return errCode;
        }
        
        // 指定编码参数，将ImageSource直接编码进文件。
        OH\_PackingOptions \*option = nullptr;
        OH\_PackingOptions\_Create(&option);
        Image\_MimeType image\_MimeType = GetMimeTypeIfEncodable(MIME\_TYPE\_JPEG);
        if (image\_MimeType.data == nullptr || image\_MimeType.size == 0) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest GetMimeTypeIfEncodable failed,"
                         "format can't support encode.");
            return IMAGE\_BAD\_PARAMETER;
        }
        OH\_PackingOptions\_SetMimeType(option, &image\_MimeType);
        // 当设备支持HDR编码，资源本身为HDR图且图片资源的格式为jpeg时，编码产物才能为HDR内容。
        OH\_PackingOptions\_SetDesiredDynamicRange(option, IMAGE\_PACKER\_DYNAMIC\_RANGE\_AUTO);
        // 设置编码质量，quality默认为0，建议quality的值不低于80
        uint32\_t quality = 90;
        OH\_PackingOptions\_SetQuality(option, quality);
        errCode = OH\_ImagePackerNative\_PackToFileFromImageSource(testPacker, option, imageSource, fd);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_ImagePackerNative\_PackToFileFromImageSource failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
    
        // 释放ImagePacker实例。
        errCode = OH\_ImagePackerNative\_Release(testPacker);
        testPacker = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_ImagePackerNative\_Release failed,"
                         "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        // 释放PackingOptions实例。
        errCode = OH\_PackingOptions\_Release(option);
        option = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_PackingOptions\_Release failed,"
                         "errCode: %{public}d.", errCode);
            return errCode;
        }
        return IMAGE\_SUCCESS;
    }
    
    Image\_ErrorCode packToFileFromPixelmapTest(int fd, OH\_PixelmapNative \*pixelmap)
    {
        // 创建ImagePacker实例。
        OH\_ImagePackerNative \*testPacker = nullptr;
        Image\_ErrorCode errCode = OH\_ImagePackerNative\_Create(&testPacker);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest CreatePacker OH\_ImagePackerNative\_Create failed,"
                         "errCode: %{public}d.", errCode);
            return errCode;
        }
    
        // 指定编码参数，将PixelMap直接编码进文件。
        OH\_PackingOptions \*option = nullptr;
        OH\_PackingOptions\_Create(&option);
        char type\[\] = "image/jpeg";
        Image\_MimeType image\_MimeType = {type, strlen(type)};
        OH\_PackingOptions\_SetMimeType(option, &image\_MimeType);
        // 设置编码质量，quality默认为0，建议quality的值不低于80
        uint32\_t quality = 90;
        OH\_PackingOptions\_SetQuality(option, quality);
        errCode = OH\_ImagePackerNative\_PackToFileFromPixelmap(testPacker, option, pixelmap, fd);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest OH\_ImagePackerNative\_PackToFileFromPixelmap failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
    
        // 释放ImagePacker实例。
        errCode = OH\_ImagePackerNative\_Release(testPacker);
        testPacker = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest ReleasePacker OH\_ImagePackerNative\_Release failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        // 释放PackingOptions实例。
        errCode = OH\_PackingOptions\_Release(option);
        option = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest OH\_PackingOptions\_Release failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        return IMAGE\_SUCCESS;
    }
    
    napi\_value PackToFileFromImageSourceTestJs(napi\_env env, napi\_callback\_info info)
    {
        napi\_value argv\[1\] = {0};
        size\_t argc = 1;
        if (napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr) != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "PackToFileFromImageSourceTestJs napi\_get\_cb\_info failed.");
            return nullptr;
        }
        
        int fd;
        napi\_get\_value\_int32(env, argv\[0\], &fd);
        
        Image\_ErrorCode errCode = packToFileFromImageSourceTest(fd, g\_thisImageSource->source);
        if (errCode == IMAGE\_SUCCESS) {
            OH\_LOG\_INFO(LOG\_APP, "ImagePackerNativeCTest PackToFileFromImageSourceTestJs successfully.");
        }
        return GetJsResult(env, errCode);
    }
    
    napi\_value PackToFileFromPixelmapTestJs(napi\_env env, napi\_callback\_info info)
    {
        napi\_value argv\[1\] = {0};
        size\_t argc = 1;
        if (napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr) != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "PackToFileFromImageSourceTestJs napi\_get\_cb\_info failed.");
            return nullptr;
        }
        
        int fd;
        napi\_get\_value\_int32(env, argv\[0\], &fd);
        
        Image\_ErrorCode errCode = packToFileFromPixelmapTest(fd, g\_thisImageSource->resPixMap);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest failed,"
                         "errCode: %{public}d.", errCode);
            return GetJsResult(env, errCode);
        } else {
            OH\_LOG\_INFO(LOG\_APP, "PackToFileFromPixelmapTestJs successfully.");
        }
        return GetJsResult(env, errCode);
    }
