---
title: "微距能力设置(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-macro"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "微距能力设置(C/C++)"
captured_at: "2026-04-17T01:36:05.503Z"
---

# 微距能力设置(C/C++)

从API version 19开始，支持设置微距能力。微距能力是指通过光学设计与算法优化，实现近距离对焦并清晰捕捉微小物体细节的相机功能。

#### 开发步骤

详细的API说明请参考[OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。

1.  导入NDK接口。选择系统提供的NDK接口能力，导入NDK接口的方法如下。
    
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
    
3.  通过[OH\_CaptureSession\_IsMacroSupported()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_ismacrosupported)方法，检测当前设备是否支持微距能力。
    
    bool NDKCamera::IsMacroSupported(Camera\_CaptureSession\* captureSession)
    {
        // 判断设备是否支持微距能力。
        bool isMacroSupported = false;
        if (captureSession == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "IsMacroSupported: session is nullptr.");
            return isMacroSupported;
        }
        Camera\_ErrorCode ret = OH\_CaptureSession\_IsMacroSupported(captureSession, &isMacroSupported);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_IsMacroSupported failed.");
        }
        if (isMacroSupported) {
            OH\_LOG\_INFO(LOG\_APP, "support macro capability.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "No support macro capability.");
        }
        return isMacroSupported;
    }
    
4.  使用[OH\_CaptureSession\_EnableMacro()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_enablemacro)方法开启或关闭微距能力。
    
    void NDKCamera::EnableMacro(bool isMacro)
    {
        OH\_LOG\_INFO(LOG\_APP, "EnableMacro: isMacro is %{public}d", isMacro);
        if (IsMacroSupported(captureSession\_)) {
            Camera\_ErrorCode ret = OH\_CaptureSession\_EnableMacro(captureSession\_, isMacro);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_EnableMacro failed.");
            }
        }
    }
    

#### 状态监听

从API version 20开始，支持监听微距能力是否发生改变。

通过[OH\_CaptureSession\_RegisterMacroStatusChangeCallback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_registermacrostatuschangecallback)函数注册回调，返回监听结果。

void MacroStatusCallback(Camera\_CaptureSession \*captureSession, bool isMacroDetected)
{
    OH\_LOG\_INFO(LOG\_APP, "MacroStatusCallback isMacro: %{public}d", isMacroDetected);
}

// 注册回调函数。
Camera\_ErrorCode NDKCamera::RegisterMacroStatusCallback()
{
    Camera\_ErrorCode ret = OH\_CaptureSession\_RegisterMacroStatusChangeCallback(captureSession\_, MacroStatusCallback);
    if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_RegisterMacroStatusChangeCallback failed.");
    }
    return ret;
}

// 解注册
Camera\_ErrorCode NDKCamera::UnregisterMacroStatusCallback()
{
    Camera\_ErrorCode ret = OH\_CaptureSession\_UnregisterMacroStatusChangeCallback(captureSession\_, MacroStatusCallback);
    if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_UnregisterMacroStatusChangeCallback failed.");
    }
    return ret;
}
