---
title: "基于AVRecorder录制格式化音频（C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-avrecorder"
menu_path:
  - "最佳实践"
  - "媒体"
  - "音频和视频"
  - "音频录制系列开发实践"
  - "基于AVRecorder录制格式化音频（C++）"
captured_at: "2026-04-17T01:54:15.160Z"
---

# 基于AVRecorder录制格式化音频（C++）

#### 概述

AVRecorder提供了Native API，可以快速实现音频录制，支持m4a、mp3等格式。本文适用于音频录制类应用的开发，针对市场上主流音频录制类应用的常见场景，介绍了在C/C++侧基于AVRecorder如何录制格式化音频，指导开发者实现基础录制。

基于AVRecorder录制格式化音频（C++）实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/fdQn-ZtCRsqu773o1ds5og/zh-cn_image_0000002524221070.gif?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=001E169DCF09A1981D574975F8D506D1C8D57CA0FE8727CDB0B45E05D34B72EA "点击放大")

本文的主要内容如下：

[基础录制](#section20569101215108)：介绍了在C/C++侧基于AVRecorder录制格式化音频，包括开始录制、暂停录制和结束录制。

#### 基础录制

#### \[h2\]实现原理

除了ArkTS语言版本外，HarmonyOS还提供了C/C++语言版本的AVRecorder录制器，用于在C/C++侧进行音频数据采集、音频编码以及音频文件封装等端到端一体化音频录制。C/C++侧AVRecorder的功能和开发流程与ArkTS侧基本一致。

**图1** 录制状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/6xgOFtmYROa7VIdKVrPZ2g/zh-cn_image_0000002555340939.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=844FCC6469F00411BAB92060DB4CEF5F6A0088EE8812FB67C193A0C163D80B2B "点击放大")

#### \[h2\]开发步骤

1.在CMake脚本中链接动态库libavrecorder.so、libnative\_media\_core.so等。

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libavrecorder.so libnative\_media\_core.so libhilog\_ndk.z.so)

2.在Native侧，配置AVRecorder。

-   创建OH\_AVRecorder\_Config对象，并设置音频录制的相关配置，包括音频采样率、音频格式、采样通道等。
-   根据实际需要，设置音频录制的回调函数，如错误回调函数OH\_AVRecorder\_SetErrorCallback()等。
-   调用OH\_AVRecorder\_Prepare()接口，让AVRecorder进入prepare状态。

// Set AVRecorder Config
void SetConfig(OH\_AVRecorder\_Config &config) {
    config.audioSourceType = AVRECORDER\_MIC;
    // Set media config
    config.profile.audioBitrate = 96000; // Set audio bitrate
    config.profile.audioChannels = 2; // Set audio channels
    config.profile.audioCodec = AVRECORDER\_AUDIO\_MP3; // Set audio codec
    config.profile.audioSampleRate = 48000; // Set audio sampleRate
    config.profile.fileFormat = AVRECORDER\_CFT\_MP3; // Set fileFormat
    config.fileGenerationMode = AVRECORDER\_APP\_CREATE; // Set FileGenerationMode
}

// Prepare AVRecorder
napi\_value AVRecorder::PrepareAVRecorder(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
    napi\_get\_value\_int32(env, args\[0\], &g\_outputFd);
    if (g\_outputFd <= 0) {
        napi\_value res;
        napi\_create\_int32(env, -1, &res);
        return res;
    }
    OH\_LOG\_INFO(LOG\_APP, "PrepareAVRecorder in!");
    g\_avRecorder = OH\_AVRecorder\_Create();
    OH\_LOG\_INFO(LOG\_APP, "AVRecorder Create ok! g\_avRecorder: %{public}p", g\_avRecorder);
    if (g\_avRecorder == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "AVRecorder Create failed!");
    }
    OH\_AVRecorder\_Config \*config = new OH\_AVRecorder\_Config();
    SetConfig(\*config);

    // Set url
    std::string fileUrl = "fd://" + std::to\_string(g\_outputFd);
    config->url = const\_cast<char \*>(fileUrl.c\_str());
    OH\_LOG\_INFO(LOG\_APP, "config.url is: %s", const\_cast<char \*>(fileUrl.c\_str()));

    // Set State Callback
    OH\_AVRecorder\_SetStateCallback(g\_avRecorder, OnStateChange, nullptr);
    // Set Error Callback
    OH\_AVRecorder\_SetErrorCallback(g\_avRecorder, OnError, nullptr);
    // Set recorder configuration
    OH\_AVRecorder\_SetWillMuteWhenInterrupted(g\_avRecorder, true);
    
    // Prepare
    int result = OH\_AVRecorder\_Prepare(g\_avRecorder, config);
    if (result != AV\_ERR\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, " AVRecorder Prepare failed %{public}d", result);
    }
    napi\_value res;
    napi\_create\_int32(env, result, &res);
    return res;
}

3.启动音频录制。

// Start AVRecorder
napi\_value AVRecorder::StartAVRecorder(napi\_env env, napi\_callback\_info info) {
    (void)info;
    OH\_LOG\_INFO(LOG\_APP, " g\_avRecorder start: %{public}p", g\_avRecorder);
    int result = OH\_AVRecorder\_Start(g\_avRecorder);
    if (result != AV\_ERR\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, " AVRecorder Start failed %{public}d", result);
    }
    napi\_value res;
    napi\_create\_int32(env, result, &res);
    return res;
}

4.暂停音频录制。

// Pause AVRecorder
napi\_value AVRecorder::PauseAVRecorder(napi\_env env, napi\_callback\_info info) {
    (void)info;
    int result = OH\_AVRecorder\_Pause(g\_avRecorder);
    if (result != AV\_ERR\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, " AVRecorder Pause failed %{public}d", result);
    }
    napi\_value res;
    napi\_create\_int32(env, result, &res);
    return res;
}

5.继续音频录制。

// Resume AVRecorder
napi\_value AVRecorder::ResumeAVRecorder(napi\_env env, napi\_callback\_info info) {
    (void)info;
    int result = OH\_AVRecorder\_Resume(g\_avRecorder);
    if (result != AV\_ERR\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, " AVRecorder Resume failed %{public}d", result);
    }
    napi\_value res;
    napi\_create\_int32(env, result, &res);
    return res;
}

6.停止音频录制。

// Stop AVRecorder
napi\_value AVRecorder::StopAVRecorder(napi\_env env, napi\_callback\_info info) {
    (void)info;
    int result = OH\_AVRecorder\_Stop(g\_avRecorder);
    if (result != AV\_ERR\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, " AVRecorder Stop failed %{public}d", result);
    }
    close(g\_outputFd);
    napi\_value res;
    napi\_create\_int32(env, result, &res);
    return res;
}

7.释放音频录制资源。

// Release AVRecorder
napi\_value AVRecorder::ReleaseAVRecorder(napi\_env env, napi\_callback\_info info) {
    (void)info;
    if (g\_avRecorder == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, " g\_avRecorder is nullptr!");
        napi\_value res;
        napi\_create\_int32(env, AV\_ERR\_INVALID\_VAL, &res);
        return res;
    }

    int result = OH\_AVRecorder\_Release(g\_avRecorder);
    g\_avRecorder = nullptr;

    if (result != AV\_ERR\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, " AVRecorder Release failed %{public}d", result);
    }
    napi\_value res;
    napi\_create\_int32(env, result, &res);
    return res;
}

#### 常见问题

#### \[h2\]设置静音打断模式

通过调用[OH\_AVRecorder\_SetWillMuteWhenInterrupted()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-h#oh_avrecorder_setwillmutewheninterrupted)接口设置是否开启静音打断模式。

#### \[h2\]设置回声消除

通过将[OH\_AVRecorder\_AudioSourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h#oh_avrecorder_audiosourcetype)值指定为AVRECORDER\_VOICE\_COMMUNICATION即可。

#### 示例代码

-   [基于AVRecorder录制音频（C++）](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-cpp)
