---
title: "分段式拍照(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-deferred-capture"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "分段式拍照(C/C++)"
captured_at: "2026-04-17T01:36:05.430Z"
---

# 分段式拍照(C/C++)

分段式拍照是相机的最重要功能之一，相机输出低质量图用作快速显示，提升用户感知拍照速度，同时使用高质量图保证最后的成图质量达到系统相机的水平，既满足了后处理算法的需求，又不阻塞前台的拍照速度，构筑相机性能竞争力，提升了用户的体验。

-   在第一阶段，系统快速上报轻量处理的图片，轻量处理的图片比全质量图低，出图速度快。应用通过回调会收到一个PhotoAsset对象，通过该对象可调用媒体库接口，读取图片或落盘图片。
-   在第二阶段，相机框架会根据应用的请求图片诉求或者在系统闲时，进行图像增强处理得到全质量图，将处理好的图片传回给媒体库，替换轻量处理的图片。

#### 开发步骤

详细的API说明请参考[OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。

1.  导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。
    
    #include <cstdint>
    #include <unistd.h>
    #include <string>
    #include <thread>
    #include <cstdio>
    #include <fcntl.h>
    #include <map>
    #include <string>
    #include <vector>
    #include <native\_buffer/native\_buffer.h>
    #include "iostream"
    #include "mutex"
    
    #include "hilog/log.h"
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "napi/native\_api.h"
    #include "ohcamera/camera\_manager.h"
    #include "common/log\_common.h"
    
    #include "multimedia/image\_framework/image/image\_native.h"
    #include "multimedia/image\_framework/image/image\_source\_native.h"
    #include "multimedia/image\_framework/image/image\_packer\_native.h"
    #include "multimedia/media\_library/media\_access\_helper\_capi.h"
    #include "multimedia/media\_library/media\_asset\_base\_capi.h"
    #include "multimedia/media\_library/media\_asset\_capi.h"
    #include "multimedia/media\_library/media\_asset\_change\_request\_capi.h"
    #include "multimedia/media\_library/media\_asset\_manager\_capi.h"
    #include "multimedia/media\_library/moving\_photo\_capi.h"
    #include "ohcamera/photo\_native.h"
    #include <window\_manager/oh\_display\_info.h>
    #include <window\_manager/oh\_display\_manager.h>
    
2.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC
        libace_napi.z.so
        libhilog_ndk.z.so
        libohcamera.so
        libimage_source.so
        libmedia_asset_manager.so
        libimage_packer.so
    )
    ```
    
3.  相机初始化及拍照触发参考[拍照(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)。
    
4.  注册分段式（PhotoAssetAvailable）拍照回调，对比单段式拍照，仅注册的拍照回调接口不同。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/BqOn0zRLQjmtGPYx6U-dJg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=57F7E1D96D035D7F5CBCA8E4D3CF6EA3250D2CD15016B1105EF7486F78B4C6C0)
    
    如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册，会导致流被重启，仅PhotoAssetAvailable生效。
    
    不建议开发者同时注册PhotoAssetAvailable和PhotoAvailable。
    
    注册PhotoAssetAvailableCallback回调，接收分段式拍照回图示例：
    
    **分段式拍照开发流程（PhotoAssetAvailableCallback）**：
    
    -   在会话commitConfig前注册分段式拍照回调。
    -   通过分段式拍照回调，获取媒体库资源mediaAsset。
    -   通过mediaAsset直接落盘图片或者通过mediaAsset配置策略模式请求图像资源，业务处理后通过buffer保存图片，或显示图片(参考[拍照(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)步骤5)。
    -   使用完后解注册分段式拍照回调函数。
    
    // 分段式拍照回调函数。
    void onPhotoAssetAvailable(Camera\_PhotoOutput \*photoOutput, OH\_MediaAsset \*mediaAsset)
    {
        if (mediaAsset == nullptr) {
            DRAWING\_LOGI("onPhotoAssetAvailable mediaAsset is nullptr !");
            return;
        }
        DRAWING\_LOGD("onPhotoAssetAvailable start!");
        NDKCamera::MediaAssetRelease();
        g\_mediaAsset = mediaAsset;
        NDKCamera::MediaAssetGetUri(mediaAsset);
        NDKCamera::MediaAssetGetDisplayName(mediaAsset);
        NDKCamera::MediaAssetGetSize(mediaAsset);
        NDKCamera::MediaAssetGetDateModifiedMs(mediaAsset);
        NDKCamera::MediaAssetGetWidth(mediaAsset);
        NDKCamera::MediaAssetGetHeight(mediaAsset);
        NDKCamera::MediaAssetGetOrientation(mediaAsset);
        NDKCamera::MediaAssetManagerCreate();
        NDKCamera::MediaAssetChangeRequest(mediaAsset);
        DRAWING\_LOGD("onPhotoAssetAvailable finish!");
        return;
    }
    
    // 注册分段式拍照回调。
    Camera\_ErrorCode NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback(void)
    {
        DRAWING\_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback start!");
        MediaAssetManagerCreate();
        ret\_ = OH\_PhotoOutput\_RegisterPhotoAssetAvailableCallback(photoOutput\_, onPhotoAssetAvailable);
        if (ret\_ != CAMERA\_OK) {
            DRAWING\_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback failed.");
        }
        DRAWING\_LOGD(
            "NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback return with ret code: %{public}d!",
            ret\_);
        return ret\_;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetChangeRequest(OH\_MediaAsset \*mediaAsset)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequest start!");
        MediaAssetChangeRequestCreate(mediaAsset);
        MediaAssetManagerRequestImage(mediaAsset);
        DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequest finish!");
        return MEDIA\_LIBRARY\_OK;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetChangeRequestCreate(OH\_MediaAsset \*mediaAsset)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequestCreate start!");
        g\_changeRequest = OH\_MediaAssetChangeRequest\_Create(mediaAsset);
        if (g\_changeRequest == nullptr) {
            DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequestCreate failed.");
        }
        return MEDIA\_LIBRARY\_OK;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetManagerCreate(void)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetManagerCreate start!");
        mediaAssetManager = OH\_MediaAssetManager\_Create();
        if (mediaAssetManager == nullptr) {
            DRAWING\_LOGD("NDKCamera::MediaAssetManagerCreate failed.");
        }
        return MEDIA\_LIBRARY\_OK;
    }
    
    void OnRequsetImageDataPreparedWithDetails(MediaLibrary\_ErrorCode result, MediaLibrary\_RequestId requestId,
        MediaLibrary\_MediaQuality mediaQuality, MediaLibrary\_MediaContentType type, OH\_ImageSourceNative \*imageSourceNative)
    {
        auto cb = (void (\*)(char \*))(g\_requestImageCallback);
        auto qCb = (void (\*)(char \*))(g\_requestImageQualityCallback);
        DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails start!");
        if (mediaQuality == MediaLibrary\_MediaQuality::MEDIA\_LIBRARY\_QUALITY\_FAST) {
            DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails into fast quality mode!");
            g\_mediaQualityCb = "fast";
            qCb(g\_mediaQualityCb);
        } else {
            DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails into high quality mode!");
            g\_mediaQualityCb = "high";
            qCb(g\_mediaQualityCb);
        }
        DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails GetUri uri\_ = %{public}s", URI);
        cb(const\_cast<char \*>(URI));
        NDKCamera::ChangeRequestAddResourceWithBuffer(imageSourceNative);
        return;
    }
    
    // 请求图片数据：deliveryMode/quality等通过requestOptions控制，完成后进回调OnRequsetImageDataPreparedWithDetails。
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetManagerRequestImage(OH\_MediaAsset \*mediaAsset)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetManagerRequestImage start! g\_deliveryMode = %{public}d",
            g\_deliveryMode);
        requestOptions.deliveryMode = g\_deliveryMode;
        result = OH\_MediaAssetManager\_RequestImage(mediaAssetManager, mediaAsset, requestOptions, &g\_requestId,
            OnRequsetImageDataPreparedWithDetails);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::MediaAssetManagerRequestImage failed.");
        }
        DRAWING\_LOGD("NDKCamera::MediaAssetManagerRequestImage return with ret code: %{public}d!", result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestAddResourceWithBuffer(OH\_ImageSourceNative \*imageSourceNative)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer start!");
        size\_t bufferSize = BUFFER\_SIZE;
        char buffer\[BUFFER\_SIZE\];
        int fd = open("/data/storage/el2/base/haps/test.jpg", O\_RDONLY);
        int fr = read(fd, buffer, bufferSize);
        if (fr == -1) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read failed.");
            return MEDIA\_LIBRARY\_OK;
        }
        if (fr == BUFFER\_SIZE) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read not complete.");
            return MEDIA\_LIBRARY\_OK;
        }
        result = OH\_MediaAssetChangeRequest\_AddResourceWithBuffer(g\_changeRequest,
            MediaLibrary\_ResourceType::MEDIA\_LIBRARY\_IMAGE\_RESOURCE, (uint8\_t \*)buffer, (uint32\_t)bufferSize);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed.");
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed %{public}d.", result);
            return MEDIA\_LIBRARY\_OK;
        }
        result = OH\_MediaAccessHelper\_ApplyChanges(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD(
                "NDKCamera::ChangeRequestAddResourceWithBuffer OH\_MediaAccessHelper\_ApplyChanges failed.");
            return MEDIA\_LIBRARY\_OK;
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer OH\_MediaAccessHelper\_ApplyChanges return "
                     "with ret code: %{public}d!",
            result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestSaveCameraPhoto(void)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto start!");
        result = OH\_MediaAssetChangeRequest\_SaveCameraPhoto(g\_changeRequest,
            MediaLibrary\_ImageFileType::MEDIA\_LIBRARY\_IMAGE\_JPEG);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD(
                "NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAssetChangeRequest\_SaveCameraPhoto failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAssetChangeRequest\_SaveCameraPhoto "
                     "return with ret code: %{public}d!",
            result);
        result = OH\_MediaAccessHelper\_ApplyChanges(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAccessHelper\_ApplyChanges failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAccessHelper\_ApplyChanges return with "
                     "ret code: %{public}d!",
            result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestDiscardCameraPhoto(void)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto start!");
        result = OH\_MediaAssetChangeRequest\_DiscardCameraPhoto(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto "
                         "OH\_MediaAssetChangeRequest\_DiscardCameraPhoto failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH\_MediaAssetChangeRequest\_DiscardCameraPhoto "
                     "return with ret code: %{public}d!",
            result);
        result = OH\_MediaAccessHelper\_ApplyChanges(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD(
                "NDKCamera::ChangeRequestDiscardCameraPhoto OH\_MediaAccessHelper\_ApplyChanges failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH\_MediaAccessHelper\_ApplyChanges return with "
                     "ret code: %{public}d!",
            result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestRelease(void)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestRelease start!");
        result = OH\_MediaAssetChangeRequest\_Release(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestRelease failed.");
        }
        g\_changeRequest = nullptr;
        DRAWING\_LOGD("NDKCamera::ChangeRequestRelease return with ret code: %{public}d!", result);
        return result;
    }
