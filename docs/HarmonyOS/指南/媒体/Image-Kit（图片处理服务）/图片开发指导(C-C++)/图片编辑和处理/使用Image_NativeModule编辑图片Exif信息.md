---
title: "使用Image_NativeModule编辑图片Exif信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool-c"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(C/C++)"
  - "图片编辑和处理"
  - "使用Image_NativeModule编辑图片Exif信息"
captured_at: "2026-04-17T01:36:06.200Z"
---

# 使用Image\_NativeModule编辑图片Exif信息

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF、WEBP23+、DNG23+格式，且需要图片包含Exif信息。

在图库等应用中，需要查看或修改数码照片的Exif信息。当摄像机的手动镜头参数无法自动写入到Exif信息中，或者相机断电等原因会导致拍摄时间出错时，可手动修改错误的Exif数据。

系统目前仅支持对部分Exif信息的查看和修改，具体支持的范围请参见：[变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#变量)里的OHOS\_IMAGE\_PROPERTY\_XXX类型。需要注意的是，DNG格式图片仅支持读取Exif信息，不支持修改。

#### 开发步骤

#### \[h2\]添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so 以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```

#### \[h2\]Native接口调用

Exif信息的读取与编辑相关C API接口的详细介绍请参见[OH\_ImageSourceNative\_GetImageProperty()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_getimageproperty)和[OH\_ImageSourceNative\_ModifyImageProperty()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_modifyimageproperty)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\\src\\main\\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**读取和编辑图片Exif信息接口使用示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/RRxbYSJsSnyAduWioDtJGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=1A921346F23F4E4C25D5E8417B5EA4609AD5051AE31362F25AB57F84410BFD89)

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1.  导入相关头文件。
    
    #include <string>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include "napi/native\_api.h"
    
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
    
6.  在成功创建ImageSource对象后，读取、编辑Exif信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/6rRIUOMWQkStVC-LEl3Bow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=64453D3C05EA950736ACDD5AA911972EC8E5AB4F8F8C673B2AD4C9FFE754F559)
    
    创建ImageSource对象可参考[图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c)。
    
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
