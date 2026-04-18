---
title: "元数据(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-metadata"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "元数据(C/C++)"
captured_at: "2026-04-17T01:36:05.489Z"
---

# 元数据(C/C++)

元数据（Metadata）是对相机返回的图像信息的描述和上下文。针对图像信息，提供更详细的数据，如照片或视频中，识别人像的取景框坐标等信息。

Metadata主要是通过一个TAG（Key），去找对应的Data（Value），用于传递参数和配置信息，减少内存拷贝操作。

#### 开发步骤

详细的API说明请参考[OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。

1.  导入NDK接口，导入方法如下。
    
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
        libohcamera.so
        libhilog_ndk.z.so
    )
    ```
    
3.  调用OH\_CameraManager\_GetSupportedCameraOutputCapability()方法，获取当前设备支持的元数据类型metaDataObjectType，并通过OH\_CameraManager\_CreateMetadataOutput()方法创建元数据输出流。
    
    Camera\_ErrorCode NDKCamera::CreateMetadataOutput(void)
    {
        metaDataObjectType\_ = cameraOutputCapability\_->supportedMetadataObjectTypes\[0\];
        if (metaDataObjectType\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get metaDataObjectType failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreateMetadataOutput(cameraManager\_, metaDataObjectType\_, &metadataOutput\_);
        if (metadataOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreateMetadataOutput failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        MetadataOutputRegisterCallback();
        return ret\_;
    }
    
4.  调用[OH\_CameraManager\_CreateCaptureSession()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession)方法创建一个会话。
    
    ret = OH\_CameraManager\_CreateCaptureSession(cameraManager\_, &captureSession\_);
    if (captureSession\_ == nullptr || ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Create captureSession failed.");
    }
    
5.  配置session，完成后通过调用[OH\_CaptureSession\_Start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_start)方法输出metadata数据。接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。
    
    // 开始配置会话。
    Camera\_ErrorCode ret = OH\_CaptureSession\_BeginConfig(captureSession\_);
    
    // 将相机输入流加入会话。
    ret = OH\_CaptureSession\_AddInput(captureSession\_, cameraInput\_);
    
    // 将相机预览流加入会话。
    ret = OH\_CaptureSession\_AddPreviewOutput(captureSession\_, previewOutput\_);
    
    if (isVideo\_) {
        // 将相机录像流加入会话。
        AddVideoOutput();
        if (isHdrVideo) {
            // HDR Vivid视频需要设置色彩空间为OH\_COLORSPACE\_BT2020\_HLG\_LIMIT。
            OH\_NativeBuffer\_ColorSpace colorSpace = OH\_NativeBuffer\_ColorSpace::OH\_COLORSPACE\_BT2020\_HLG\_LIMIT;
            SetColorSpace(colorSpace);
        }
    } else {
        // 将相机拍照流加入会话。
        AddPhotoOutput();
        ret = CreateMetadataOutput();
        ret = OH\_CaptureSession\_AddMetadataOutput(captureSession\_, metadataOutput\_);
        OH\_NativeBuffer\_ColorSpace colorSpace = OH\_NativeBuffer\_ColorSpace::OH\_COLORSPACE\_P3\_FULL;
        SetColorSpace(colorSpace);
    }
    
    // 提交会话配置信息。
    ret = OH\_CaptureSession\_CommitConfig(captureSession\_);
    // ...
    
    InitPreviewRotation();
    // 开始会话。
    OH\_LOG\_INFO(LOG\_APP, "session start");
    ret = OH\_CaptureSession\_Start(captureSession\_);
    
6.  调用stop()方法停止输出metadata数据，接口调用失败会返回相应错误码。
    
    ```
    Camera_ErrorCode StopMetadataOutput(Camera_MetadataOutput* metadataOutput)
    {
        Camera_ErrorCode ret = OH_MetadataOutput_Stop(metadataOutput);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_MetadataOutput_Stop failed.");
        }
        return ret;
    }
    ```
    

#### 状态监听

在相机应用开发过程中，可以随时监听metadata数据以及输出流的状态。

-   通过注册监听获取metadata对象，监听事件固定为metadataObjectsAvailable。检测到有效metadata数据时，callback返回相应的metadata数据信息，metadataOutput创建成功时可监听。
    
    void OnMetadataObjectAvailable(Camera\_MetadataOutput \*metadataOutput, Camera\_MetadataObject \*metadataObject,
        uint32\_t size)
    {
        OH\_LOG\_INFO(LOG\_APP, "size = %{public}d", size);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/jiNcHN8XQ7-7EABgrSglPA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=8DD56917FD6448E8A3EDCC5B2DF379EE646D967E39D46314282770516ED809B5)
    
    当前的元数据类型仅支持人脸检测（FACE\_DETECTION）功能。元数据信息对象为识别到的人脸区域的矩形信息（Rect），包含矩形区域的左上角x坐标、y坐标和矩形的宽高数据。
    
-   通过注册回调函数，获取监听metadata流的错误结果，callback返回metadata输出接口使用错误时返回的错误码，错误码类型参见[Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。
    
    void OnMetadataOutputError(Camera\_MetadataOutput \*metadataOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "OnMetadataOutput errorCode = %{public}d", errorCode);
    }
    
    MetadataOutput\_Callbacks \*NDKCamera::GetMetadataOutputListener(void)
    {
        static MetadataOutput\_Callbacks metadataOutputListener = {
            .onMetadataObjectAvailable = OnMetadataObjectAvailable,
            .onError = OnMetadataOutputError
        };
        return &metadataOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::MetadataOutputRegisterCallback(void)
    {
        ret\_ = OH\_MetadataOutput\_RegisterCallback(metadataOutput\_, GetMetadataOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_MetadataOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
