---
title: "动态调整预览帧率(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-setframerate-native"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "动态调整预览帧率(C/C++)"
captured_at: "2026-04-17T01:36:05.611Z"
---

# 动态调整预览帧率(C/C++)

动态调整帧率是直播、视频等场景下控制预览效果的重要能力之一。应用可通过此能力，显式地控制流输出帧率，以适应不同帧率下的业务目标。

某些场景下降低帧率可在相机设备启用时降低功耗。

#### 约束与限制

支持的帧率范围及帧率的设置依赖于硬件能力的实现，不同的硬件平台可能拥有不同的默认帧率。

#### 开发流程

相机使用预览功能前，均需要创建相机会话。完成会话配置后，应用提交和开启会话，才可以开始调用相机相关功能。

流程图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/nObuDIl-R6a76TJCD5psWQ/zh-cn_image_0000002568899235.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=06EBD65BD43D031EEBBCAD7909BA6969C571A605E9EDD2CB55DC9393142CCA13)

与普通的[预览](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview)流程相比，动态调整预览帧率的注意点如图上标识：

1.  调用[OH\_CameraManager\_CreateCaptureSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession)创建会话（Session）时，需要指定模式为NORMAL\_PHOTO或NORMAL\_VIDEO。
    
    仅当Session处于NORMAL\_PHOTO或NORMAL\_VIDEO模式时，支持调整预览流帧率。调整帧率的创建会话方式见[创建Session会话并指定模式](#创建session会话并指定模式)。
    
2.  [动态调整帧率](#动态调整帧率)的操作，可在启动预览前后任意时刻调用。
    
3.  [动态调整帧率](#动态调整帧率)在预览里属于可选操作，可以完成：
    
    -   查询当前支持调整的帧率范围
    -   设置当前帧率
    -   获取当前生效的帧率设置

如何配置会话（Session）、释放资源，请参考[会话管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management) > [预览](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview)。

#### 导入模块

1.  导入NDK接口，导入方法如下。
    
    ```
    // 导入NDK接口头文件
    #include "hilog/log.h"
    #include "ohcamera/camera.h"
    #include "ohcamera/camera_input.h"
    #include "ohcamera/capture_session.h"
    #include "ohcamera/photo_output.h"
    #include "ohcamera/preview_output.h"
    #include "ohcamera/video_output.h"
    #include "ohcamera/camera_manager.h"
    ```
    
2.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)
    ```
    

#### 创建Session会话并指定模式

相机使用预览等功能前，均需创建相机会话，调用[OH\_CameraManager\_CreateCaptureSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession)创建一个会话。

创建会话时调用[OH\_CaptureSession\_SetSessionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setsessionmode)指定[Camera\_SceneMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_scenemode)为NORMAL\_PHOTO或NORMAL\_VIDEO，创建出的Session处于拍照或录像模式。

以创建Session会话并指定为NORMAL\_PHOTO模式为例：

```
Camera_ErrorCode CreateCaptureSession(Camera_Manager *cameraManager, Camera_CaptureSession *captureSession) {
   Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
    if (captureSession == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
    }
    // 设置会话模式为拍照或录像模式，此处以拍照模式为例
    ret = OH_CaptureSession_SetSessionMode(captureSession, Camera_SceneMode::NORMAL_PHOTO);
    return ret;
}
```

#### 动态调整帧率

1.  调用[OH\_PreviewOutput\_GetSupportedFrameRates](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getsupportedframerates)，查询当前previewOutput支持的帧率范围。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/49lr8ZsjS0ezvMIXATKc0Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=86F56444DD784B1D625949D39BB151E3E5A882056D14FC8F8166A9A8E30B13FD)
    
    **调用时机**：
    
    需要在Session调用[OH\_CaptureSession\_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)完成配流之后调用。
    
    **OH\_PreviewOutput\_GetSupportedFrameRates调用限制：**
    
    -   在调用OH\_PreviewOutput\_GetSupportedFrameRates接口设置非固定帧率后，不支持再次调用该接口重新设置动态帧率。
    -   在调用OH\_PreviewOutput\_GetSupportedFrameRates接口设置固定帧率后，支持重新设置固定帧率，但必须保证新设置的帧率可以整除之前设置的帧率或者被之前设置的帧率整除。
    
    ```cpp
    Camera_ErrorCode PreviewOutputGetSupportedFrameRates(Camera_PreviewOutput* previewOutput,
        Camera_FrameRateRange** frameRateRange, uint32_t* size) {
        Camera_ErrorCode ret = OH_PreviewOutput_GetSupportedFrameRates(previewOutput, frameRateRange, size);
    
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetSupportedFrameRates failed.");
            return CAMERA_INVALID_ARGUMENT;
        }
        for (uint32_t i = 0; i < *size; i++) {
            OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates min %{public}d", (*frameRateRange)[i].min);
            OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates max %{public}d", (*frameRateRange)[i].max);
        }
        return ret;
    }
    ```
    
2.  根据实际开发需求，调用[OH\_PreviewOutput\_SetFrameRate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_setframerate)接口对帧率进行动态调整。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/mCRaSaF_RMONHO4Mux55dQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013605Z&HW-CC-Expire=86400&HW-CC-Sign=A9224A390F6CCD366AF960E88085B964EA69A6555E523E88A2028DAA099F48F7)
    
    -   需要在Session调用[OH\_CaptureSession\_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)完成配流之后调用。
        
    -   可在Session调用[OH\_PreviewOutput\_Start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_start)启动预览前后任意时刻调用。
        
    
    ```cpp
    Camera_ErrorCode PreviewOutputSetFrameRate(Camera_PreviewOutput* previewOutput,
        uint32_t minFps, uint32_t maxFps){
        Camera_ErrorCode ret = OH_PreviewOutput_SetFrameRate(previewOutput, minFps, maxFps);
        if (ret != CAMERA_OK) {
            return CAMERA_INVALID_ARGUMENT;
        }
        return ret;
    }
    ```
    
3.  （可选）通过[OH\_PreviewOutput\_GetActiveFrameRate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getactiveframerate)接口查询已设置过并生效的帧率。
    
    仅通过[OH\_PreviewOutput\_SetFrameRate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_setframerate)接口显式设置过帧率才可查询当前生效帧率信息。
    
    ```cpp
    Camera_ErrorCode PreviewOutputGetActiveFrameRate(Camera_PreviewOutput* previewOutput,
        Camera_FrameRateRange* frameRateRange){
        Camera_ErrorCode ret = OH_PreviewOutput_GetActiveFrameRate(previewOutput, frameRateRange);
        if (ret != CAMERA_OK) {
            return CAMERA_INVALID_ARGUMENT;
        }
        OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ min %{public}d", (*frameRateRange).min);
        OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ max %{public}d", (*frameRateRange).max);
        return ret;
    }
    ```
