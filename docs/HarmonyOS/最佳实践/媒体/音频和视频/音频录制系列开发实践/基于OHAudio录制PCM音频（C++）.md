---
title: "基于OHAudio录制PCM音频（C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-ohaudio"
menu_path:
  - "最佳实践"
  - "媒体"
  - "音频和视频"
  - "音频录制系列开发实践"
  - "基于OHAudio录制PCM音频（C++）"
captured_at: "2026-04-17T01:54:15.135Z"
---

# 基于OHAudio录制PCM音频（C++）

#### 概述

在C/C++侧，OHAudio提供音频模块相关能力，包含音频采集OH\_AudioCapturer、音频管理和音频播放等能力。OH\_AudioCapturer仅支持录制PCM格式，可以在C/C++侧实现音频母带录制。本文适用于音频录制类应用的开发，针对市场上主流音频录制类应用的常见场景，介绍了基于OHAudio如何录制PCM音频，指导开发者实现基础录制。

基于OHAudio录制PCM音频（C++）实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/hOsaoT2WRmSf2URF14wuMg/zh-cn_image_0000002524221068.gif?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=111C70275C3207168762ABAC13C24395D0E84755334F7BCB7B92341C534FB766 "点击放大")

本文的主要内容如下：

[基础录制](#section20569101215108)：介绍了基于OHAudio录制PCM音频，包括开始录制、暂停录制、结束录制。

#### 基础录制

#### \[h2\]实现原理

在C/C++侧，OHAudio提供音频模块相关能力，包含音频采集OH\_AudioCapturer、音频管理和音频播放等能力。当前，OH\_AudioCapturer仅支持PCM格式，同时支持设置低时延通路、静音打断和回声消除，适用于依赖Native层实现音频录制的场景。整个开发流程可以概括为：音频流构造器实例创建、音频采集参数配置、采集回调注册（各类事件监听）、采集器实例创建、采集的开始与停止以及资源的释放等。其中，事件监听主要包括音频输入流回调等。在创建完实例后，开发者可以调用相关方法使得音频录制流进入对应的状态。

**图1** OHAudio音频录制状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/L26UHEzkSlm7aBwQIOFbVA/zh-cn_image_0000002555340937.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=73056E5D99ED30DDC8143C54428105EDDB0568DFE0976F963B6310479FDABF49 "点击放大")

#### \[h2\]开发步骤

1.依赖导入。

-   在CMake脚本中链接动态库libohaudio.so、libnative\_media\_codecbase.so等。

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libohaudio.so libhilog\_ndk.z.so libnative\_media\_codecbase.so)

2.创建音频采集器。

-   创建OH\_AudioStreamBuilder，用于采集器的相关配置。
-   通过OH\_AudioStreamBuilder设置环境配置，包括采样率、采样通道数、回调函数等。其中，回调函数OH\_AudioCapturer\_OnReadData是向PCM文件中写入采集到的音频数据。
-   通过OH\_AudioStreamBuilder\_GenerateCapturer创建音频采集器。

static int32\_t AudioRendererOnWriteData(OH\_AudioRenderer \*renderer, void \*userData, void \*buffer, int32\_t bufferLen) {
    if (g\_file == nullptr) {
        return 0;
    }
    size\_t readCount = fread(buffer, bufferLen, 1, g\_file);
    if (!readCount) {
        // End of the file
        if (feof(g\_file)) {
            // Seek start point
            fseek(g\_file, 0, SEEK\_SET);
        }
    }
    return 0;
}

static napi\_value AudioCapturerLowLatencyInit(napi\_env env, napi\_callback\_info info) {
    if (audioCapturer != nullptr) {
        OH\_AudioCapturer\_Release(audioCapturer);
        OH\_AudioStreamBuilder\_Destroy(builder);
        
        audioCapturer = nullptr;
        builder = nullptr;
    }
    if (g\_file) {
        fclose(g\_file);
        g\_file = nullptr;
    }
    g\_file = fopen(g\_filePath.c\_str(), "wb");
    // 1. create builder
    OH\_AudioStream\_Type type = AUDIOSTREAM\_TYPE\_CAPTURER;
    OH\_AudioStreamBuilder\_Create(&builder, type);
    // 2. set params and callbacks
    OH\_AudioStreamBuilder\_SetSamplingRate(builder, g\_samplingRate); // Set SamplingRate 
    OH\_AudioStreamBuilder\_SetChannelCount(builder, g\_channelCount); // Set ChannelCount
    OH\_AudioStreamBuilder\_SetLatencyMode(builder, AUDIOSTREAM\_LATENCY\_MODE\_FAST); // Set LatencyMode
    OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_RAW); // Set EncodingType

    OH\_AudioCapturer\_Callbacks callbacks;
    callbacks.OH\_AudioCapturer\_OnReadData = AudioCapturerOnReadData; // Set ReadData Callback
    callbacks.OH\_AudioCapturer\_OnError = nullptr;
    callbacks.OH\_AudioCapturer\_OnInterruptEvent = nullptr;
    callbacks.OH\_AudioCapturer\_OnStreamEvent = nullptr;
    OH\_AudioStreamBuilder\_SetCapturerCallback(builder, callbacks, nullptr); // Set Capturer Callback

    // 3. create OH\_AudioCapturer
    OH\_AudioStreamBuilder\_GenerateCapturer(builder, &audioCapturer); // Generate Capturer
    return nullptr;
}

3.开始音频录制。

static napi\_value AudioCapturerStart(napi\_env env, napi\_callback\_info info) {
    // start
    OH\_AudioCapturer\_Start(audioCapturer);
    return nullptr;
}

4.暂停音频录制。

static napi\_value AudioCapturerPause(napi\_env env, napi\_callback\_info info) {
    OH\_AudioCapturer\_Pause(audioCapturer);
    return nullptr;
}

5.停止音频录制。

static napi\_value AudioCapturerStop(napi\_env env, napi\_callback\_info info) {
    OH\_AudioCapturer\_Stop(audioCapturer);
    return nullptr;
}

6.释放音频录制资源。

static napi\_value AudioCapturerRelease(napi\_env env, napi\_callback\_info info) {
    if (audioCapturer) {
        OH\_AudioCapturer\_Release(audioCapturer);
        OH\_AudioStreamBuilder\_Destroy(builder);
        audioCapturer = nullptr;
        builder = nullptr;
    }
    if (g\_file) {
        fclose(g\_file);
        g\_file = nullptr;
    }
    return nullptr;
}

#### 常见问题

#### \[h2\]设置静音打断模式

开发者在创建AudioCapturer实例时，调用[OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setcapturerwillmutewheninterrupted)接口设置是否开启静音打断模式。

#### \[h2\]设置回声消除

通过将[OH\_AudioStream\_SourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sourcetype)值指定为AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_COMMUNICATION、AUDIOSTREAM\_SOURCE\_TYPE\_LIVE即可。

#### \[h2\]设置音频录制低时延

通过调用[OH\_AudioStreamBuilder\_SetLatencyMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setlatencymode)设置低时延模式。

#### 示例代码

-   [基于AudioCapturer录制音频(C++)](https://gitcode.com/HarmonyOS_Samples/audio-native)
