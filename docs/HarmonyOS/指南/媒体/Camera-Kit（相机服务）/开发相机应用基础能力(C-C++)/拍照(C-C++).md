---
title: "拍照(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "拍照(C/C++)"
captured_at: "2026-04-17T01:36:05.405Z"
---

# 拍照(C/C++)

#### 概述

拍照是相机的重要功能之一，拍照模块基于相机复杂的逻辑，为了保证用户拍出的照片质量，在中间步骤可以设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

目前相机开发有两种相机拍照方案，分别是相机[分段式拍照](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-deferred-capture)和相机单段式拍照（**本文将以单段式拍照为基础进行说明**）。

-   分段式拍照是指相机拍照既可以输出低质量图用作缩略图，提升用户感知拍照速度，也可以使用高质量图保证最后的成图质量达到系统相机的水平。满足了图像处理算法的需求的同时，又不会阻塞前台的拍照速度，构筑相机性能竞争力，提升用户体验。
-   单段式拍照是指在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，所以Shot2See（用户点击拍照控件到在缩略图显示区域显示缩略图的过程）完成时延较长。此外，单段式拍照支持通过[高性能拍照](#高性能拍照)功能调整[画质优先策略](#画质优先策略)，以加快出图速度或提升图片质量。

#### 开发步骤

详细的API说明请参考[OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。

1.  导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。
    
    #include <cstdint>
    #include <native\_buffer/buffer\_common.h>
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
    #include <window\_manager/oh\_display\_info.h>
    #include <window\_manager/oh\_display\_manager.h>
    
    namespace OHOS\_CAMERA\_SAMPLE {
    class NDKCamera {
      public:
        struct CameraBuildingConfig {
            char \*str;
            uint32\_t focusMode;
            uint32\_t cameraDeviceIndex;
            bool isVideo;
            bool isHdr;
            char \*videoId;
        };
        ~NDKCamera();
        explicit NDKCamera(CameraBuildingConfig config);
        // ...
    };
    } // namespace OHOS\_CAMERA\_SAMPLE
    
2.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC
        libace_napi.z.so
        libhilog_ndk.z.so
        libnative_buffer.so
        libohcamera.so
        libohimage.so
        libohfileuri.so
    )
    ```
    
3.  创建并打开相机设备，参考 [设备输入(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-device-input)步骤3-5。
    
4.  选择设备支持的输出流能力，创建拍照输出流。
    
    通过[OH\_CameraManager\_CreatePhotoOutputWithoutSurface()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createphotooutputwithoutsurface)方法创建拍照输出流。
    
    Camera\_ErrorCode NDKCamera::CreatePhotoOutputWithoutSurfaceId()
    {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePhotoOutputWithoutSurfaceId enter.");
        profile\_ = cameraOutputCapability\_->photoProfiles\[0\];
        Camera\_Profile\* profile = cameraOutputCapability\_->photoProfiles\[0\];
        profile->size.width = NUM\_1920;
        profile->size.height = NUM\_1080;
        profile\_ = profile;
        if (profile\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get photoProfiles failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreatePhotoOutputWithoutSurface(cameraManager\_, profile\_, &photoOutput\_);
        if (photoOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreatePhotoOutputWithoutSurfaceId failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
    // ...
        return ret\_;
    }
    
5.  注册单段式(PhotoAvailable)拍照回调，若应用希望快速得到回图，推荐使用[分段式拍照回调(PhotoAssetAvailable)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-deferred-capture)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/UH7CEuHNQ_uuOYOluI43WA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=0D52D4AC0078F95B9767461712AFD7F396496D991F3C326F8BA7C9ABF680C16F)
    
    如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册，会导致流被重启，仅PhotoAssetAvailable生效。
    
    不建议开发者同时注册PhotoAssetAvailable和PhotoAvailable。
    
    **单段式拍照开发流程（PhotoAvailable）**：
    
    -   在会话commitConfig前注册单段式拍照回调。
        
    -   在单段式拍照回调函数中获取图片信息，解析出buffer数据，做自定义业务处理。
        
    -   将处理完的buffer通过回调传给ArkTS侧，做图片显示或通过安全控件写文件保存图片。
        
    -   使用完后解注册单段式拍照回调函数。
        
        // 保存NAPI侧注册的buffer处理回调函数。
        Camera\_ErrorCode NDKCamera::RegisterBufferCb(void \*cb)
        {
            OH\_LOG\_INFO(LOG\_APP, " RegisterBufferCb start");
            if (cb == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, " RegisterBufferCb invalid error");
                return CAMERA\_INVALID\_ARGUMENT;
            }
            g\_bufferCb = cb;
            return CAMERA\_OK;
        }
        
        static bool ProcessImageNative(OH\_ImageNative\* imageNative, uint32\_t\*\* components,
                                       OH\_NativeBuffer\*\* nativeBuffer, size\_t\* nativeBufferSize)
        {
            if (imageNative == nullptr || components == nullptr || nativeBuffer == nullptr || nativeBufferSize == nullptr) {
                return false;
            }
        
            Image\_Size size;
            Image\_ErrorCode imageErr = OH\_ImageNative\_GetImageSize(imageNative, &size);
            if (imageErr != IMAGE\_SUCCESS) {
                return false;
            }
        
            size\_t componentTypeSize = 0;
            imageErr = OH\_ImageNative\_GetComponentTypes(imageNative, nullptr, &componentTypeSize);
            if (imageErr != IMAGE\_SUCCESS || componentTypeSize == 0) {
                OH\_LOG\_ERROR(LOG\_APP, "GetComponentTypes failed: %{public}d, size: %{public}zu",
                    imageErr, componentTypeSize);
                return false;
            }
        
            if (componentTypeSize > (SIZE\_MAX / sizeof(uint32\_t))) {
                OH\_LOG\_ERROR(LOG\_APP, "componentTypeSize too large: %{public}zu", componentTypeSize);
                return false;
            }
        
            uint32\_t\* compArray = new (std::nothrow) uint32\_t\[componentTypeSize\];
            if (!compArray) {
                return false;
            }
        
            size\_t tempSize = componentTypeSize;
            imageErr = OH\_ImageNative\_GetComponentTypes(imageNative, &compArray, &tempSize);
            if (imageErr != IMAGE\_SUCCESS) {
                delete\[\] compArray;
                return false;
            }
            \*components = compArray;
        
            imageErr = OH\_ImageNative\_GetByteBuffer(imageNative, compArray\[0\], nativeBuffer);
            if (imageErr != IMAGE\_SUCCESS) {
                delete\[\] compArray;
                return false;
            }
        
            imageErr = OH\_ImageNative\_GetBufferSize(imageNative, compArray\[0\], nativeBufferSize);
            if (imageErr != IMAGE\_SUCCESS) {
                delete\[\] compArray;
                return false;
            }
        
            int32\_t rowStride = 0;
            int32\_t pixelStride = 0;
            OH\_ImageNative\_GetRowStride(imageNative, compArray\[0\], &rowStride);
            OH\_ImageNative\_GetPixelStride(imageNative, compArray\[0\], &pixelStride);
            OH\_LOG\_INFO(LOG\_APP, "Buffer size: %{public}zu, strides: %{public}d/%{public}d",
                \*nativeBufferSize, rowStride, pixelStride);
        
            return true;
        }
        
        
        static void CleanupResources(OH\_ImageNative\* imageNative, uint32\_t\* components,
                                     OH\_NativeBuffer\* nativeBuffer, void\* virAddr)
        {
            if (components) {
                delete\[\] components;
            }
        
            if (imageNative) {
                int32\_t ret = OH\_ImageNative\_Release(imageNative);
                if (ret != 0) {
                    OH\_LOG\_ERROR(LOG\_APP, "Release image failed: %{public}d", ret);
                }
            }
        
            if (nativeBuffer && virAddr) {
                int32\_t ret = OH\_NativeBuffer\_Unmap(nativeBuffer);
                if (ret != 0) {
                    OH\_LOG\_ERROR(LOG\_APP, "Unmap buffer failed: %{public}d", ret);
                }
            }
        }
        
        void OnPhotoAvailable(Camera\_PhotoOutput \*photoOutput, OH\_PhotoNative \*photo)
        {
            OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable start!");
        
            OH\_ImageNative \*imageNative = nullptr;
            Camera\_ErrorCode errCode = OH\_PhotoNative\_GetMainImage(photo, &imageNative);
            if (errCode != CAMERA\_OK || !imageNative) {
                OH\_LOG\_ERROR(LOG\_APP, "GetMainImage failed: %{public}d", errCode);
                return;
            }
        
            uint32\_t\* components = nullptr;
            OH\_NativeBuffer\* nativeBuffer = nullptr;
            size\_t nativeBufferSize = 0;
        
            if (!ProcessImageNative(imageNative, &components, &nativeBuffer, &nativeBufferSize)) {
                CleanupResources(imageNative, components, nullptr, nullptr);
                return;
            }
        
            void\* virAddr = nullptr;
            int32\_t ret = OH\_NativeBuffer\_Map(nativeBuffer, &virAddr);
            if (ret != 0 || !virAddr) {
                OH\_LOG\_ERROR(LOG\_APP, "Map buffer failed: %{public}d", ret);
                CleanupResources(imageNative, components, nativeBuffer, nullptr);
                return;
            }
        
            auto cb = (void (\*)(void \*, size\_t))(g\_bufferCb);
            if (cb && virAddr && nativeBufferSize > 0) {
                cb(virAddr, nativeBufferSize);
                OH\_LOG\_INFO(LOG\_APP, "Buffer callback called");
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "Invalid callback parameters");
            }
        
            CleanupResources(imageNative, components, nativeBuffer, virAddr);
        
            OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable end");
        }
        
        Camera\_ErrorCode NDKCamera::PhotoOutputRegisterPhotoAvailableCallback(void)
        {
            OH\_LOG\_INFO(LOG\_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback start!");
            Camera\_ErrorCode ret = OH\_PhotoOutput\_RegisterPhotoAvailableCallback(photoOutput\_, OnPhotoAvailable);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_INFO(LOG\_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback failed.");
            }
            OH\_LOG\_INFO(LOG\_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback return with ret code: %{public}d!",
                ret\_);
            return ret;
        }
        
        // 解注册单段式拍照回调。
        Camera\_ErrorCode NDKCamera::PhotoOutputUnRegisterPhotoAvailableCallback()
        {
            OH\_LOG\_INFO(LOG\_APP, "PhotoOutputUnRegisterPhotoAvailableCallback start!");
            Camera\_ErrorCode ret = OH\_PhotoOutput\_UnregisterPhotoAvailableCallback(photoOutput\_, OnPhotoAvailable);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "PhotoOutputUnRegisterPhotoAvailableCallback failed.");
            }
            OH\_LOG\_INFO(LOG\_APP, "PhotoOutputUnRegisterPhotoAvailableCallback return with ret code: %{public}d!", ret);
            return ret;
        }
        
        NAPI层buffer回调处理参考示例代码：
        
        // NAPI层buffer回调方法。
        static void BufferCb(void\* buffer, size\_t size)
        {
            OH\_LOG\_INFO(LOG\_APP, "BufferCb size:%{public}zu", size);
            g\_size = size;
            napi\_value asyncResource = nullptr;
            napi\_value asyncResourceName = nullptr;
            napi\_async\_work work;
        
            if (size == 0 || size > SIZE\_MAX) {
                OH\_LOG\_ERROR(LOG\_APP, "BufferCb size is invalid");
                return;
            }
            void\* copyBuffer = malloc(size);
            if (copyBuffer == nullptr) {
                return;
            }
            OH\_LOG\_INFO(LOG\_APP, "BufferCb copyBuffer:%{public}p", copyBuffer);
            // 使用std::memcpy复制buffer的内容到copyBuffer。
            std::memcpy(copyBuffer, buffer, size);
            napi\_create\_string\_utf8(env\_, "BufferCb", NAPI\_AUTO\_LENGTH, &asyncResourceName);
            napi\_status status = napi\_create\_async\_work(
                env\_, asyncResource, asyncResourceName, \[\](napi\_env env, void\* copyBuffer) {},
                \[\](napi\_env env, napi\_status status, void\* copyBuffer) {
                    napi\_value retVal;
                    napi\_value callback = nullptr;
                    void\* data = nullptr;
                    napi\_value arrayBuffer = nullptr;
                    size\_t bufferSize = g\_size;
                    napi\_create\_arraybuffer(env, bufferSize, &data, &arrayBuffer);
                    std::memcpy(data, copyBuffer, bufferSize);
                    OH\_LOG\_INFO(LOG\_APP, "BufferCb g\_size: %{public}zu", g\_size);
                    napi\_get\_reference\_value(env, bufferCbRef\_, &callback);
                    if (callback) {
                        OH\_LOG\_INFO(LOG\_APP, "BufferCb callback is full");
                    } else {
                        OH\_LOG\_ERROR(LOG\_APP, "BufferCb callback is null");
                    }
                    // 调用ArkTS的buffer处理回调函数，将图片arrayBuffer传给页面做显示或保存。
                    napi\_call\_function(env, nullptr, callback, 1, &arrayBuffer, &retVal);
                },
                copyBuffer, &work);
            // 错误检查：创建异步工作失败时释放内存。
            if (status != napi\_ok) {
                OH\_LOG\_ERROR(LOG\_APP, "Failed to create async work");
                free(copyBuffer); // 释放分配的内存。
                return;
            }
            napi\_queue\_async\_work\_with\_qos(env\_, work, napi\_qos\_user\_initiated);
        }
        
6.  创建拍照类型会话，参考[会话管理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)，开启会话，准备拍照。
    
7.  配置拍照参数（可选）。
    
    配置相机的参数可以调整拍照的一些功能，包括闪光灯、变焦、焦距等。
    
    Camera\_ErrorCode NDKCamera::HasFlashFn(uint32\_t mode)
    {
        Camera\_FlashMode flashMode = static\_cast<Camera\_FlashMode>(mode);
        // 检查闪光灯。
        bool hasFlash = false;
        Camera\_ErrorCode ret = OH\_CaptureSession\_HasFlash(captureSession\_, &hasFlash);
        if (captureSession\_ == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_HasFlash failed.");
        }
        if (hasFlash) {
            OH\_LOG\_INFO(LOG\_APP, "hasFlash success-----");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "hasFlash fail-----");
        }
    
        // 查询闪光灯模式是否支持。
        bool isSupported = false;
        ret = OH\_CaptureSession\_IsFlashModeSupported(captureSession\_, flashMode, &isSupported);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_IsFlashModeSupported failed.");
        }
        if (isSupported) {
            OH\_LOG\_INFO(LOG\_APP, "isFlashModeSupported success-----");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "isFlashModeSupported fail-----");
        }
    
        // 设置闪光灯模式。
        ret = OH\_CaptureSession\_SetFlashMode(captureSession\_, flashMode);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_SetFlashMode success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetFlashMode failed. %{public}d ", ret);
        }
    
        // 获取当前设备的闪光灯模式。
        ret = OH\_CaptureSession\_GetFlashMode(captureSession\_, &flashMode);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetFlashMode success. flashMode：%{public}d ", flashMode);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetFlashMode failed. %d ", ret);
        }
        return ret;
    }
    
    // 对焦模式。
    Camera\_ErrorCode NDKCamera::IsFocusModeSupported(uint32\_t mode)
    {
        Camera\_FocusMode focusMode = static\_cast<Camera\_FocusMode>(mode);
        ret\_ = OH\_CaptureSession\_IsFocusModeSupported(captureSession\_, focusMode, &isFocusModeSupported\_);
        if (&isFocusModeSupported\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "IsFocusModeSupported failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        return ret\_;
    }
    
    Camera\_ErrorCode NDKCamera::IsFocusMode(uint32\_t mode)
    {
        OH\_LOG\_INFO(LOG\_APP, "IsFocusMode start.");
        Camera\_FocusMode focusMode = static\_cast<Camera\_FocusMode>(mode);
        ret\_ = OH\_CaptureSession\_IsFocusModeSupported(captureSession\_, focusMode, &isFocusModeSupported\_);
        if (&isFocusModeSupported\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "IsFocusModeSupported failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CaptureSession\_SetFocusMode(captureSession\_, focusMode);
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "SetFocusMode failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CaptureSession\_GetFocusMode(captureSession\_, &focusMode);
        if (&focusMode == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "GetFocusMode failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        OH\_LOG\_INFO(LOG\_APP, "IsFocusMode end.");
        return ret\_;
    }
    
    Camera\_ErrorCode NDKCamera::setZoomRatioFn(uint32\_t zoomRatio)
    {
        float zoom = float(zoomRatio);
        // 获取支持的缩放范围。
        float minZoom;
        float maxZoom;
        Camera\_ErrorCode ret = OH\_CaptureSession\_GetZoomRatioRange(captureSession\_, &minZoom, &maxZoom);
        if (captureSession\_ == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetZoomRatioRange failed.");
        } else {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
                minZoom, maxZoom);
        }
    
        // 设置缩放比例。
        ret = OH\_CaptureSession\_SetZoomRatio(captureSession\_, zoom);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_SetZoomRatio success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetZoomRatio failed. %{public}d ", ret);
        }
    
        // 获取当前设备的缩放比例。
        ret = OH\_CaptureSession\_GetZoomRatio(captureSession\_, &zoom);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio success. zoom：%{public}f ", zoom);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio failed. %{public}d ", ret);
        }
        return ret;
    }
    
8.  触发拍照。
    
    通过[OH\_PhotoOutput\_Capture\_WithCaptureSetting()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_capture_withcapturesetting)方法，执行拍照任务。
    
    Camera\_ErrorCode NDKCamera::TakePicture(int32\_t degree)
    {
        Camera\_ErrorCode ret = CAMERA\_OK;
        Camera\_ImageRotation imageRotation;
        bool isMirSupported;
        OH\_PhotoOutput\_IsMirrorSupported(photoOutput\_, &isMirSupported);
        OH\_PhotoOutput\_GetPhotoRotation(photoOutput\_, degree, &imageRotation);
    
        Camera\_PhotoCaptureSetting curPhotoSetting = {
            quality : QUALITY\_LEVEL\_HIGH,
            rotation : imageRotation,
            mirror : isMirSupported
        };
        ret = OH\_PhotoOutput\_Capture\_WithCaptureSetting(photoOutput\_, curPhotoSetting);
        OH\_LOG\_INFO(LOG\_APP, "TakePicture get quality %{public}d, rotation %{public}d, mirror %{public}d",
            curPhotoSetting.quality, curPhotoSetting.rotation, curPhotoSetting.mirror);
        OH\_LOG\_INFO(LOG\_APP, "TakePicture ret = %{public}d.", ret);
        return ret;
    }
    

#### 高性能拍照

从API version 21开始支持高性能拍照功能，即在进行单段式拍照时设置明确的[画质优先策略](#画质优先策略)。

单段式拍照的体验主要由出图速度和最终图片质量衡量。因此，为满足开发者在不同场景下的差异化需求，对这两项指标的侧重也不同。例如，街头抓拍要求快速捕捉瞬间，而风景或人像拍摄则更追求极致的画质。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/joFIsId7S92aUm2-_ccnZw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=DFF39FA4380B9C9FB206D69BC1C3542FCA7CD827452DF34479751B3BCBD4B2F2)

仅单段式拍照支持设置画质优先策略。若在分段式拍照中设置画质优先策略，该设置将无效。

#### \[h2\]画质优先策略

在使用单段式拍照时，支持设置速度优先和画质优先两种画质优先策略类型，并且分别对应着不同的[Camera\_PhotoQualityPrioritization](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_photoqualityprioritization)枚举类型。

-   [CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_SPEED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_photoqualityprioritization)对应着速度优先，表示降低画质来提升拍照的速度。如果开发者在进行单段式拍照时没有设置明确的画质优先策略，**单段式拍照就默认为速度优先状态**。
-   [CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_HIGH\_QUALITY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_photoqualityprioritization)对应着画质优先，表示通过较长的耗时来得到画质更高的图片。

#### \[h2\]如何正确设置画质优先策略

为了正确的在单段式拍照中设置画质优先策略，高性能拍照功能提供了如下两个接口：

-   [OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_isphotoqualityprioritizationsupported)：查询当前设备是否支持指定的画质优先策略。返回true表示支持，返回false表示不支持。在进行设置画质优先策略之前，必须先查询将要设置的画质优先策略在当前设备上是否可用。
-   [OH\_PhotoOutput\_SetPhotoQualityPrioritization](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_setphotoqualityprioritization)：画质优先策略设置接口，通过该接口设置对应的画质优先策略，实现高性能拍照。

#### \[h2\]开发步骤

高性能拍照相关接口需要在[会话管理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)流程的使能步骤中进行调用。

具体调用时机如下：

-   在[会话管理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)流程中的使能步骤中的[OH\_CaptureSession\_CommitConfig()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)结束之后进行调用。
    
    ```
    Camera_ErrorCode StartSession(Camera_CaptureSession* captureSession, Camera_Input* cameraInput,
      Camera_PreviewOutput* previewOutput, Camera_PhotoOutput* photoOutput)
    {
      // 向会话中添加相机输入流。
      Camera_ErrorCode ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
        return ret;
      }
    
      // 向会话中添加预览输出流。
      ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
        return ret;
      }
    
      // 向会话中添加拍照输出流。
      ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
        return ret;
      }
    
      // 提交会话配置。
      ret = OH_CaptureSession_CommitConfig(captureSession);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
        return ret;
      }
    
      // 启动会话。
      ret = OH_CaptureSession_Start(captureSession);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
      }
    
      SetHighQualityPhotoQualityPrioritization(photoOutput);
      return ret;
    }
    
    void SetHighQualityPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput)
    {
      Camera_PhotoQualityPrioritization quality = Camera_PhotoQualityPrioritization::CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY;
      bool isSupported = false;
      Camera_ErrorCode ret = OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
      if (isSupported) {
        ret = OH_PhotoOutput_SetPhotoQualityPrioritization(photoOutput, quality);
        if (ret != 0) {
          OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_SetPhotoQualityPrioritization failed.");
        }
      } else {
        OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_IsPhotoQualityPrioritizationSupported not supported.");
      }
    }
    ```
    
-   在[会话管理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)流程中的使能步骤中的[OH\_CaptureSession\_CommitConfig()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)之前调用。
    
    ```
    Camera_ErrorCode StartSession(Camera_CaptureSession* captureSession, Camera_Input* cameraInput,
      Camera_PreviewOutput* previewOutput, Camera_PhotoOutput* photoOutput)
    {
      // 向会话中添加相机输入流。
      Camera_ErrorCode ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
        return ret;
      }
    
      // 向会话中添加预览输出流。
      ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
        return ret;
      }
    
      // 向会话中添加拍照输出流。
      ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
        return ret;
      }
    
      SetHighQualityPhotoQualityPrioritization(photoOutput);
      
      // 提交会话配置。
      ret = OH_CaptureSession_CommitConfig(captureSession);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
        return ret;
      }
    
      // 启动会话。
      ret = OH_CaptureSession_Start(captureSession);
      if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
      }
    
      return ret;
    }
    
    void SetHighQualityPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput)
    {
      Camera_PhotoQualityPrioritization quality = Camera_PhotoQualityPrioritization::CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY;
      bool isSupported = false;
      Camera_ErrorCode ret = OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
      if (isSupported) {
        ret = OH_PhotoOutput_SetPhotoQualityPrioritization(photoOutput, quality);
        if (ret != 0) {
          OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_SetPhotoQualityPrioritization failed.");
        }
      } else {
        OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_IsPhotoQualityPrioritizationSupported not supported.");
      }
    }
    ```
    

#### 状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍照输出流的错误。

-   通过注册固定的onFrameStart回调函数获取监听拍照开始结果，photoOutput创建成功时即可监听，拍照第一次曝光时触发。
    
    // PhotoOutput Callback
    void PhotoOutputOnFrameStart(Camera\_PhotoOutput \*photoOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutputOnFrameStart");
    }
    
    void PhotoOutputOnFrameShutter(Camera\_PhotoOutput \*photoOutput, Camera\_FrameShutterInfo \*info)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutputOnFrameShutter");
    }
    
-   通过注册固定的onFrameEnd回调函数获取监听拍照结束结果，photoOutput创建成功时即可监听。
    
    void PhotoOutputOnFrameEnd(Camera\_PhotoOutput \*photoOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutput frameCount = %{public}d", frameCount);
    }
    
-   通过注册固定的onError回调函数获取监听拍照输出流的错误结果。callback返回拍照输出接口使用错误时的对应错误码，错误码类型参见[Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。
    
    void PhotoOutputOnError(Camera\_PhotoOutput \*photoOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutput errorCode = %{public}d", errorCode);
    }
    
    PhotoOutput\_Callbacks \*NDKCamera::GetPhotoOutputListener(void)
    {
        static PhotoOutput\_Callbacks photoOutputListener = {
            .onFrameStart = PhotoOutputOnFrameStart,
            .onFrameShutter = PhotoOutputOnFrameShutter,
            .onFrameEnd = PhotoOutputOnFrameEnd,
            .onError = PhotoOutputOnError
        };
        return &photoOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::PhotoOutputRegisterCallback(void)
    {
        ret\_ = OH\_PhotoOutput\_RegisterCallback(photoOutput\_, GetPhotoOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
