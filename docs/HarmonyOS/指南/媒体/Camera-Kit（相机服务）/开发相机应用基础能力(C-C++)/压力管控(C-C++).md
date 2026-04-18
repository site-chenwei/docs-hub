---
title: "压力管控(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-system-pressure"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "压力管控(C/C++)"
captured_at: "2026-04-17T01:36:05.495Z"
---

# 压力管控(C/C++)

从API version 20开始，相机框架提供对系统压力等级的监听。

在长时间使用相机的场景（如直播业务）中，相机应用可以通过监听系统压力等级变化，动态调整画质（如帧率、分辨率等），平衡功耗、发热和系统负载，保证功能长时间可用。

#### 状态监听

可以通过注册[OH\_CaptureSession\_OnSystemPressureLevelChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_onsystempressurelevelchange)的回调函数获取系统压力的监听结果。

当系统压力发生变化时，callback返回Camera\_SystemPressureLevel参数。

参数的具体内容可参考相机管理器回调接口实例[Camera\_SystemPressureLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_systempressurelevel)。

void SystemPressureLevelChangeCallback(Camera\_CaptureSession \*captureSession,
    Camera\_SystemPressureLevel systemPressureLevel)
{
    OH\_LOG\_INFO(LOG\_APP, "SystemPressureLevelChangeCallback level: %{public}d", systemPressureLevel);
}

Camera\_ErrorCode NDKCamera::RegisterSystemPressureCallback()
{
    Camera\_ErrorCode ret = OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback(
        captureSession\_, SystemPressureLevelChangeCallback);
    if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP,
            "OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback failed.");
    }
    return ret;
}
