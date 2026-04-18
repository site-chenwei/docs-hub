---
title: "预览(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "预览(C/C++)"
captured_at: "2026-04-17T01:36:05.382Z"
---

# 预览(C/C++)

预览是启动相机后看见的画面，通常在拍照和录像前执行。

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
        libohcamera.so
        libhilog_ndk.z.so
    )
    ```
    
3.  获取SurfaceId。
    
    XComponent组件为预览流提供的SurfaceId，而XComponent的能力由UI提供，相关介绍可参考[XComponent组件参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)。
    
4.  根据传入的SurfaceId，通过[OH\_CameraManager\_GetSupportedCameraOutputCapability()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)方法获取当前设备支持的预览能力。通过[OH\_CameraManager\_CreatePreviewOutput()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createpreviewoutput)方法创建预览输出流，其中，OH\_CameraManager\_CreatePreviewOutput()方法中的参数分别是cameraManager指针，previewProfiles数组中的第一项，步骤三中获取的surfaceId，以及返回的previewOutput指针。
    
    Camera\_ErrorCode NDKCamera::CreatePreviewOutput(void)
    {
        if (previewProfile\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get previewProfiles failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreatePreviewOutput(cameraManager\_, previewProfile\_, previewSurfaceId\_, &previewOutput\_);
        OH\_LOG\_ERROR(LOG\_APP, "create preview width: %{public}d, height: %{public}d, format: %{public}d",
            previewProfile\_->size.width, previewProfile\_->size.height, previewProfile\_->format);
        if (previewSurfaceId\_ == nullptr || previewOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreatePreviewOutput failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        return ret\_;
        PreviewOutputRegisterCallback();
    }
    
5.  使能。当session完成CommitConfig后通过调用[OH\_CaptureSession\_Start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_start)方法输出预览流，接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。
    
    Camera\_ErrorCode NDKCamera::SessionStart(void)
    {
        Camera\_ErrorCode ret = OH\_CaptureSession\_Start(captureSession\_);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Start success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed. %d ", ret);
        }
        return ret;
    }
    
6.  通过[OH\_CaptureSession\_Stop()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_stop)方法停止预览流，接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。
    
    Camera\_ErrorCode NDKCamera::SessionStop(void)
    {
        Camera\_ErrorCode ret = OH\_CaptureSession\_Stop(captureSession\_);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Stop success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Stop failed. %d ", ret);
        }
        return ret;
    }
    

#### 状态监听

在相机应用开发过程中，可以随时监听预览输出流状态，包括预览流启动、预览流结束、预览流输出错误。

-   通过注册固定的frameStart回调函数获取监听预览启动结果，previewOutput创建成功时即可监听，预览第一次曝光时触发，有该事件返回结果则认为预览流已启动。
    
    void PreviewOutputOnFrameStart(Camera\_PreviewOutput \*previewOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnFrameStart");
    }
    
-   通过注册固定的frameEnd回调函数获取监听预览结束结果，previewOutput创建成功时即可监听，预览完成最后一帧时触发，有该事件返回结果则认为预览流已结束。
    
    void PreviewOutputOnFrameEnd(Camera\_PreviewOutput \*previewOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutput frameCount = %{public}d", frameCount);
    }
    
-   通过注册固定的error回调函数获取监听预览输出错误结果，callback返回预览输出接口使用错误时对应的错误码，错误码类型参见[Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。
    
    void PreviewOutputOnError(Camera\_PreviewOutput \*previewOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutput errorCode = %{public}d", errorCode);
    }
    
    PreviewOutput\_Callbacks \*NDKCamera::GetPreviewOutputListener(void)
    {
        static PreviewOutput\_Callbacks previewOutputListener = {
            .onFrameStart = PreviewOutputOnFrameStart,
            .onFrameEnd = PreviewOutputOnFrameEnd,
            .onError = PreviewOutputOnError
        };
        return &previewOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::PreviewOutputRegisterCallback(void)
    {
        ret\_ = OH\_PreviewOutput\_RegisterCallback(previewOutput\_, GetPreviewOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PreviewOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
