---
title: "基于AVScreenCapture录制音频"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-avscreencapture"
menu_path:
  - "最佳实践"
  - "媒体"
  - "音频和视频"
  - "音频录制系列开发实践"
  - "基于AVScreenCapture录制音频"
captured_at: "2026-04-17T01:54:15.156Z"
---

# 基于AVScreenCapture录制音频

#### 概述

AVScreenCapture具备采集设备内部音频和麦克风音频的能力，可以录制设备内播放的音频或者麦克风的音频。本文适用于音频录制类应用的开发，针对市场上主流音频录制类应用的常见场景，介绍了如何基于AVScreenCapture录制音频，指导开发者实现基础录制。

基于AVScreenCapture录制音频实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/a1I8CT1OTa-wE1Wb4EuOyQ/zh-cn_image_0000002524061076.gif?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=9B0ABDED8DDC6B3D5DF25394E530636FC1D7975C0A8744A1D4A712ABB8889CE1 "点击放大")

本文的主要内容如下：

[基础录制](#section20569101215108)：介绍在C/C++侧基于AVScreenCapture录制音频，包括开始录制、结束录制。

#### 基础录制

#### \[h2\]实现原理

开发者可以调用C/C++侧屏幕录制[AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/media-kit-intro#avscreencapture)模块的接口，完成屏幕录制，采集设备内部音频和麦克风等的音视频源数据。通过AVScreenCapture可以实现单独录制音频文件的功能，在录制音频文件时，支持录制m4a的音频格式，关键流程包括开始录制、停止录制、释放资源等。

#### \[h2\]开发步骤

1.在CMake脚本中链接动态库libnative\_avscreen\_capture.so、libnative\_media\_core.so等。

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libace\_ndk.z.so libjsvm.so libhilog\_ndk.z.so libnative\_avscreen\_capture.so libuv.so libnative\_media\_core.so)

2.配置音频录制相关参数。

-   设置视频录制相关参数OH\_VideoInfo，包括OH\_VideoCaptureInfo和OH\_VideoEncInfo。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/xbpRBOBLRLeFqtVdvPBEcQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=8116648F985F7138ACD84972E4C6FB77B6747BAFF3161C81C8AEEA9BE831A77D)

AVScreenCapture用于实现屏幕录制。当OH\_VideoCaptureInfo的videoFrameWidth和videoFrameHeight设置为0时，AVScreenCapture会忽略视频相关参数，不录制屏幕数据。

-   设置音频相关参数OH\_AudioInfo，包括音频采集信息OH\_AudioCaptureInfo、音频编码信息OH\_AudioEncInfo。

// Configuration parameters
void AVScreenCapture::SetConfig(OH\_AVScreenCaptureConfig &config) {
    OH\_RecorderInfo recorderInfo;
    recorderInfo.fileFormat = OH\_ContainerFormatType::CFT\_MPEG\_4A;
    // Config VideoCaptureInfo
    OH\_VideoCaptureInfo videoCapInfo = {
        .videoFrameWidth = 0, .videoFrameHeight = 0, .videoSource = OH\_VIDEO\_SOURCE\_SURFACE\_RGBA};
    // Config VideoEncInfo
    OH\_VideoEncInfo videoEncInfo = {
        .videoCodec = OH\_VideoCodecFormat::OH\_H264, .videoBitrate = 2000000, .videoFrameRate = 30};
    // Config VideoInfo
    OH\_VideoInfo videoInfo = {.videoCapInfo = videoCapInfo, .videoEncInfo = videoEncInfo};

    // Config Mic Capture Info
    OH\_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH\_MIC};
    // Config inner Capture Info
    OH\_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH\_ALL\_PLAYBACK};
    // Config Audio Encoder Info
    OH\_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH\_AudioCodecFormat::OH\_AAC\_LC};
    // Config Audio Info
    OH\_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};

    config.captureMode = OH\_CAPTURE\_HOME\_SCREEN; // screen capture mode
    config.dataType = OH\_CAPTURE\_FILE; // data type
    config.audioInfo = audioInfo; // audio info
    config.videoInfo = videoInfo; // video info
    config.recorderInfo = recorderInfo; // recorder info
}

3.启动音频录制。

-   在调用[OH\_AVScreenCapture\_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h#oh_avscreencapture_create)创建录制对象后，通过环境配置OH\_AVScreenCaptureConfig初始化该对象。
-   然后，调用OH\_AVScreenCapture\_StartScreenRecording()启动音频录制。

OH\_AVSCREEN\_CAPTURE\_ErrCode AVScreenCapture::StartScreenCaptureToFile(int32\_t outputFd) {
    if (avScreenCapture != nullptr) {
        StopScreenCaptureRecording(avScreenCapture);
        OH\_AVScreenCapture\_Release(avScreenCapture);
    }
    avScreenCapture = OH\_AVScreenCapture\_Create();
    if (avScreenCapture == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "AVScreenCapture create screen capture failed");
    }
    OH\_AVScreenCaptureConfig config\_;
    SetConfig(config\_);
    std::string fileUrl = "fd://" + std::to\_string(outputFd);
    config\_.recorderInfo.url = const\_cast<char \*>(fileUrl.c\_str());

    OH\_AVScreenCapture\_SetMicrophoneEnabled(avScreenCapture, true);
    OH\_AVScreenCapture\_SetErrorCallback(avScreenCapture, OnErrorSaveFile, nullptr);
    OH\_AVScreenCapture\_SetStateCallback(avScreenCapture, OnStateChangeSaveFile, nullptr);

    OH\_AVSCREEN\_CAPTURE\_ErrCode result = OH\_AVScreenCapture\_Init(avScreenCapture, config\_);

    if (result != AV\_SCREEN\_CAPTURE\_ERR\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture ScreenCapture OH\_AVScreenCapture\_Init failed %{public}d", result);
    }
    OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture ScreenCapture OH\_AVScreenCapture\_Init succ %{public}d", result);

    result = OH\_AVScreenCapture\_StartScreenRecording(avScreenCapture);
    if (result != AV\_SCREEN\_CAPTURE\_ERR\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture ScreenCapture Started failed %{public}d", result);
        OH\_AVScreenCapture\_Release(avScreenCapture);
    }
    OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture ScreenCapture Started succ %{public}d", result);
    isRunning = true;
    return result;
}

4.停止音频录制。

OH\_AVSCREEN\_CAPTURE\_ErrCode AVScreenCapture::StopScreenCaptureToFile() {
    OH\_AVSCREEN\_CAPTURE\_ErrCode result = AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT;

    if (isRunning && avScreenCapture != nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture ScreenCapture File Stop");
        result = OH\_AVScreenCapture\_StopScreenRecording(avScreenCapture);
        if (result != AV\_SCREEN\_CAPTURE\_ERR\_BASE) {
            OH\_LOG\_ERROR(LOG\_APP,
                         "AVScreenCapture StopScreenCapture OH\_AVScreenCapture\_StopScreenRecording Result: %{public}d",
                         result);
        } else {
            OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture StopScreenCapture OH\_AVScreenCapture\_StopScreenRecording");
        }
        result = OH\_AVScreenCapture\_Release(avScreenCapture);
        if (result != AV\_SCREEN\_CAPTURE\_ERR\_BASE) {
            OH\_LOG\_ERROR(LOG\_APP, "AVScreenCapture StopScreenCapture OH\_AVScreenCapture\_Release: %{public}d", result);
        } else {
            OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture OH\_AVScreenCapture\_Release success");
        }
        isRunning = false;
        avScreenCapture = nullptr;
    }
    return result;
}

5.释放音频录制资源。

void AVScreenCapture::ReleaseAVScreenCapture(struct OH\_AVScreenCapture \*capture) {
    StopScreenCaptureRecording(capture);
    if (capture != nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "AVScreenCapture ScreenCapture ReleaseSCInstanceWorker S");
        OH\_AVScreenCapture\_Release(capture);
        isRunning = false;
        avScreenCapture = nullptr;
    }
}

#### 示例代码

-   [基于AVScreenCapture录制音频（C++）](https://gitcode.com/HarmonyOS_Samples/avscreen-capture-record-system-audio-arkts)
