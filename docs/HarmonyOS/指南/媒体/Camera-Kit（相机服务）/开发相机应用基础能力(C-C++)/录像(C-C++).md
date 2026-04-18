---
title: "录像(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-recording"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "录像(C/C++)"
captured_at: "2026-04-17T01:36:05.455Z"
---

# 录像(C/C++)

录像也是相机应用的最重要功能之一，录像是循环帧的捕获。对于录像的流畅度，开发者可以参考[拍照参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)中的步骤5，设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

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
    
    系统提供的[OH\_AVRecorder\_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-h#oh_avrecorder_create)接口可以创建一个录像AVRecorder实例，通过该实例的[OH\_AVRecorder\_GetInputSurface()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-h#oh_avrecorder_getinputsurface)方法获取SurfaceId。
    
4.  创建录像输出流。
    
    根据传入的SurfaceId，通过[OH\_CameraManager\_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)接口获取[Camera\_OutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-outputcapability)能力，可以通过[Camera\_OutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-outputcapability)中的videoProfiles，获取当前设备支持的录像输出流。然后，定义创建录像的参数，通过OH\_CameraManager\_CreateVideoOutput方法创建录像输出流。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/HTg4ZFCORVusnDD6BjbvfA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=99336DD00F44166C603AC39725C12693F7E6D7793EC601572201E6017AAF7732)
    
    -   预览流与录像输出流的分辨率的宽高比要保持一致。如示例代码中宽高比为640:480 = 4:3，则需要预览流中的分辨率的宽高比也为4:3，可选择的分辨率有：640:480、960:720、1440:1080等。
        
    -   在设置预览输出流的分辨率宽高前，需要先通过[OH\_AVRecorder\_Profile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-profile)查询视频帧支持可配置的宽高范围。
        
    
    Camera\_ErrorCode NDKCamera::CreateVideoOutput(char \*videoId)
    {
        if (videoProfile\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get videoProfiles failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreateVideoOutput(cameraManager\_, videoProfile\_, videoId, &videoOutput\_);
        OH\_LOG\_ERROR(LOG\_APP, " create video width: %{public}d, height: %{public}d, format: %{public}d",
            videoProfile\_->size.width, videoProfile\_->size.height, videoProfile\_->format);
        if (videoId == nullptr || videoOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreateVideoOutput failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        VideoOutputRegisterCallback();
        return ret\_;
    }
    
5.  开始录像。
    
    通过[OH\_VideoOutput\_Start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_start)方法启动录像输出流。
    
    Camera\_ErrorCode NDKCamera::VideoOutputStart(void)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutputStart begin.");
        Camera\_ErrorCode ret = OH\_VideoOutput\_Start(videoOutput\_);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_VideoOutput\_Start success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_Start failed. %d ", ret);
        }
        return ret;
    }
    
6.  停止录像。
    
    通过[OH\_VideoOutput\_Stop()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_stop)方法停止录像输出流。
    
    Camera\_ErrorCode NDKCamera::VideoOutputStop(void)
    {
        OH\_LOG\_ERROR(LOG\_APP, "enter VideoOutputStop.");
        ret\_ = OH\_VideoOutput\_Stop(videoOutput\_);
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "VideoOutputStop failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        return ret\_;
    }
    

#### 状态监听

在相机应用开发过程中，可以随时监听录像输出流状态，包括录像开始、录像结束、录像流输出的错误。

-   通过注册固定的frameStart回调函数获取监听录像开始结果，videoOutput创建成功时即可监听，录像第一次曝光时触发，当触发该事件回调时表示录像已开始。
    
    void VideoOutputOnFrameStart(Camera\_VideoOutput \*videoOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutputOnFrameStart");
    }
    
-   通过注册固定的frameEnd回调函数获取监听录像结束结果，videoOutput创建成功时即可监听，录像完成最后一帧时触发，有该事件返回结果则认为录像流已结束。
    
    void VideoOutputOnFrameEnd(Camera\_VideoOutput \*videoOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutput frameCount = %{public}d", frameCount);
    }
    
-   通过注册固定的error回调函数获取监听录像输出错误结果，callback返回录像输出接口使用错误时对应的错误码，错误码类型参见[Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。
    
    void VideoOutputOnError(Camera\_VideoOutput \*videoOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutput errorCode = %{public}d", errorCode);
    }
    
    VideoOutput\_Callbacks \*NDKCamera::GetVideoOutputListener(void)
    {
        static VideoOutput\_Callbacks videoOutputListener = {
            .onFrameStart = VideoOutputOnFrameStart,
            .onFrameEnd = VideoOutputOnFrameEnd,
            .onError = VideoOutputOnError
        };
        return &videoOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::VideoOutputRegisterCallback(void)
    {
        ret\_ = OH\_VideoOutput\_RegisterCallback(videoOutput\_, GetVideoOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
