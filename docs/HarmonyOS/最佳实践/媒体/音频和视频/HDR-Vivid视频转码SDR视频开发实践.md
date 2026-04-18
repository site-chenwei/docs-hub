---
title: "HDR Vivid视频转码SDR视频开发实践"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hdrtosdr"
menu_path:
  - "最佳实践"
  - "媒体"
  - "音频和视频"
  - "HDR Vivid视频转码SDR视频开发实践"
captured_at: "2026-04-17T01:54:15.353Z"
---

# HDR Vivid视频转码SDR视频开发实践

#### 概述

随着视频技术的发展，HDR（高动态范围）视频逐渐成为主流，其中HDR Vivid作为一种先进的HDR标准，能够提供更丰富的色彩和更广泛的亮度范围。然而，许多设备和平台仍然只支持SDR（标准动态范围）视频。因此，将HDR Vivid视频转码为SDR视频的需求日益增加，以确保内容在更多设备上能够正常播放。将HDR Vivid视频转码成SDR视频是一个涉及多个技术要点的复杂过程。通过合理的转码处理，可以确保视频内容在不同设备上都能呈现出更佳的效果，不仅优化了视频的播放体验，还能满足更广泛受众的需求，提高市场影响力。

目前系统只支持从HDR Vivid类型转码为SDR视频，其他诸如HDR HLG或HDR 10类型的视频，要通过系统色彩空间转换能力将其转换为HDR Vivid类型后，才可进而转码为SDR类型视频。

本文主要面向所有开发者。在开始之前，建议已了解视频解码的[Surface模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-decoding#surface模式)、[视频色彩空间转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-csc)。

本文提供如下开发场景，以帮助开发者解决HDR视频转码SDR视频的问题：

-   [基于AVTranscoder模块实现HDR Vivid视频到SDR视频转码](#section27410119279)
-   [基于AVCodec模块实现HDR Vivid视频到SDR视频转码](#section93022418321)
-   [基于VideoProcessing模块实现HDR Vivid视频到SDR视频转码](#section64161017191119)
-   [基于VideoProcessing模块转换HDR色彩空间](#section184641629165414)

#### 基于AVTranscoder模块实现HDR Vivid视频到SDR视频转码

#### \[h2\]实现原理

使用[AVTranscoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/media-kit-intro#avtranscoder)可以实现视频转码功能，从API 20开始支持视频转码的C/C++开发，转码功能可在手机、平板、PC/2in1设备上作为系统提供的基础能力使用。可以通过调用[canIUse()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-syscap#caniuse)接口来判断当前设备是否支持AVTranscoder，当canIUse("SystemCapability.Multimedia.Media.AVTranscoder")的返回值为true时，表示可以使用转码能力。转码步骤如下：初始化与准备阶段，调用[OH\_AVTranscoder\_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-h#oh_avtranscoder_create)创建\`OH\_AVTranscoder\` 对象；启动与运行阶段，调用OH\_AVTranscoder\_Start()启动转码任务，此时可调用[OH\_AVTranscoder\_Pause()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-h#oh_avtranscoder_pause)暂停任务。在暂停状态下，可调用[OH\_AVTranscoder\_Resume()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-h#oh_avtranscoder_resume)恢复任务；任务进行时，若想取消该任务，可调用[OH\_AVTranscoder\_Cancel()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-h#oh_avtranscoder_cancel)终止转码任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/_79ra9FSSFSp7LDNioMxqA/zh-cn_image_0000002541928605.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=FF45B6FF570A6F22D189653400AD326B51B9B274FB9FA8DCA454342733CC7315 "点击放大")

#### \[h2\]开发步骤

具体开发步骤，可参考[使用AVTranscoder实现视频转码(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ndk-avtranscoder-for-transcodering)。

关键点：调用[OH\_AVTranscoderConfig\_SetDstVideoType()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-h#oh_avtranscoderconfig_setdstvideotype)设置输出视频的编码格式为“video/avc”。

OH\_AVTranscoderConfig\_SetDstVideoType(config, "video/avc");            

1.  创建默认AVTranscoder配置，并设置输出视频的编码格式为“video/avc”。
    
    void AVTranscoder::CreateDefaultTransCoderConfig(int32\_t dstFd) {
        config = OH\_AVTranscoderConfig\_Create();
        OH\_AVTranscoderConfig\_SetDstFD(config, dstFd);                         
        OH\_AVTranscoderConfig\_SetDstFileType(config, AV\_OUTPUT\_FORMAT\_MPEG\_4); 
        OH\_AVTranscoderConfig\_SetDstVideoType(config, "video/avc");            
        OH\_AVTranscoderConfig\_SetDstAudioType(config, "audio/mp4a-latm");      
        OH\_AVTranscoderConfig\_SetDstAudioBitrate(config, 200000);              
        OH\_AVTranscoderConfig\_SetDstVideoBitrate(config, 3000000);             
    }
    
2.  进行AVTranscoder转码，并返回转码结果。
    
    int32\_t AVTranscoder::StartAVTranscoder(const SampleInfo &sampleInfo) {
        result = 0;
        sampleInfo\_ = sampleInfo;
        transcoder = OH\_AVTranscoder\_Create();
        CreateDefaultTransCoderConfig(sampleInfo.outputFd);
        OH\_AVTranscoder\_SetStateCallback(transcoder, AvTranscoderStateChangeCb, nullptr);
        OH\_AVTranscoder\_SetErrorCallback(transcoder, OnErrorCb, nullptr);
        OH\_AVErrCode result =
            OH\_AVTranscoderConfig\_SetSrcFD(config, sampleInfo.inputFd, 0, sampleInfo.inputFileSize); 
        if (result != AV\_ERR\_OK) {
            AVCODEC\_SAMPLE\_LOGI("Transcoder setSrcFD failed, ret %{public}d", result);
        }
        result = OH\_AVTranscoder\_Prepare(transcoder, config);
        if (result != AV\_ERR\_OK) {
            AVCODEC\_SAMPLE\_LOGI("Transcoder prepare failed, ret %{public}d", result);
        }
        result = OH\_AVTranscoder\_Start(transcoder);
        return result;
    }
    
3.  定义AVTranscoder状态改变函数，当状态为“AVTRANSCODER\_COMPLETED”时，释放AVTranscoder。
    
    void AVTranscoder::AvTranscoderStateChangeCb(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_State state, void \*userData) {
        if (transcoder == nullptr) {
            return;
        }
        switch (state) {
        case AVTRANSCODER\_COMPLETED: {
            AVTranscoder::GetInstance().result = 1;
            AVTranscoder::GetInstance().ReleaseAVTranscoder();
            break;
        }
        default:
            break;
        }
    }
    
4.  在[OH\_AVTranscoder\_SetStateCallback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-h#oh_avtranscoder_setstatecallback)中设置AvTranscoder状态改变监听。
    
    OH\_AVTranscoder\_SetStateCallback(transcoder, AvTranscoderStateChangeCb, nullptr);
    
5.  转码成功后，释放AVTranscoder。
    
    int32\_t AVTranscoder::ReleaseAVTranscoder() {
        int ret = 0;
        AVCODEC\_SAMPLE\_LOGI("OH\_AVTranscoder\_Release ret:%{public}d", ret);
        if (transcoder != nullptr) {
            ret = OH\_AVTranscoder\_Release(transcoder);
            AVCODEC\_SAMPLE\_LOGI("OH\_AVTranscoder\_Release ret:%{public}d", ret);
            transcoder = nullptr;
        }
        if (config != nullptr) {
            ret = OH\_AVTranscoderConfig\_Release(config);
            AVCODEC\_SAMPLE\_LOGI("OH\_AVTranscoderConfig\_Release ret:%{public}d", ret);
            config = nullptr;
        }
        return ret;
    }
    

#### 基于AVCodec模块实现HDR Vivid视频到SDR视频转码

#### \[h2\]实现原理

在视频分享或者编辑场景时，开发者有时需要将HDR Vivid视频转换为SDR视频，可以调用AVCodec原生能力实现该功能。

#### \[h2\]开发步骤

使用AVCodec原生转码能力，主要的开发步骤为（详细开发步骤可参考[视频解码支持HDRVivid2SDR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdrvivid2sdr)）：

1.  创建解码器实例，查询系统支持的解码器能力，根据查询结果基于name创建硬解码器。
    
    class VideoDecoder {
    // ...
    private:
        // ...
        OH\_AVCodec \*decoder\_ = nullptr;
    };
    
    int32\_t VideoDecoder::Create(SampleInfo &sampleInfo) {
        // ...
            OH\_AVCapability \*capability =
                OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC, false, HARDWARE);
            CHECK\_AND\_RETURN\_RET\_LOG(capability != nullptr, AVCODEC\_SAMPLE\_ERROR,
                                     "OH\_AVCodec\_GetCapabilityByCategory failed");
            const char \*name = OH\_AVCapability\_GetName(capability);
            decoder\_ = OH\_VideoDecoder\_CreateByName(name);
            // ...
        CHECK\_AND\_RETURN\_RET\_LOG(decoder\_ != nullptr, AVCODEC\_SAMPLE\_ERROR, "Create VideoDecoder failed");
        return AVCODEC\_SAMPLE\_OK;
    }
    
2.  调用[OH\_VideoDecoder\_RegisterCallback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_registercallback)设置回调函数。
    
    int32\_t VideoDecoder::SetCallback(CodecUserData \*codecUserData) {
        int32\_t ret =
            OH\_VideoDecoder\_RegisterCallback(decoder\_,
                                             {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
                                              SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},
                                             codecUserData);
        CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERROR, "Create SetCallback failed");
        return AVCODEC\_SAMPLE\_OK;
    }
    
3.  调用[OH\_VideoDecoder\_Configure()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_configure)配置解码器。必选配置项有：视频帧宽度、视频帧高度、视频像素格式、指定输出为SDR。
    
    int32\_t VideoDecoder::Configure(const SampleInfo &sampleInfo) {
        OH\_AVFormat \*format = OH\_AVFormat\_Create();
        CHECK\_AND\_RETURN\_RET\_LOG(format != nullptr, AVCODEC\_SAMPLE\_ERROR, "Create AVFormat failed");
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
        OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.frameRate);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, sampleInfo.pixelFormat);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ROTATION, sampleInfo.rotation);
        // ...
            // Key configuration: HDR to SDR conversion
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE, OH\_COLORSPACE\_BT709\_LIMIT);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENABLE\_LOW\_LATENCY, 1);
            // ...
        int ret = OH\_VideoDecoder\_Configure(decoder\_, format);
        OH\_AVFormat\_Destroy(format);
        format = nullptr;
        CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERROR, "VideoDecoder Configure failed");
        return AVCODEC\_SAMPLE\_OK;
    }
    
4.  目前仅Surface模式支持该能力，后续步骤具体可参考：视频解码的[Surface模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-decoding#surface模式)。

#### 基于VideoProcessing模块实现HDR Vivid视频到SDR视频转码

#### \[h2\]实现原理

开发者可以调用[VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)模块提供的C API接口，实现HDR2SDR的色彩空间转换。支持的转码范围如下：

<table><tbody><tr><th class="firstcol" id="mcps1.3.11.3.1.4.1.1" valign="top" width="19.521952195219523%"><p>输入ColorSpace</p></th><td class="cellrowborder" valign="top" width="40.714071407140715%"><p>OH_COLORSPACE_BT2020_PQ_LIMIT</p></td><td class="cellrowborder" valign="top" width="39.763976397639766%"><p>OH_COLORSPACE_BT2020_HLG_LIMIT</p></td></tr><tr><th class="firstcol" id="mcps1.3.11.3.1.4.2.1" valign="top" width="19.521952195219523%"><p>输入MetadataType</p></th><td class="cellrowborder" valign="top" width="40.714071407140715%"><p>OH_VIDEO_HDR_VIVID</p></td><td class="cellrowborder" valign="top" width="39.763976397639766%"><p>OH_VIDEO_HDR_VIVID</p></td></tr><tr><th class="firstcol" id="mcps1.3.11.3.1.4.3.1" valign="top" width="19.521952195219523%"><p>输入pixelFormat</p></th><td class="cellrowborder" valign="top" width="40.714071407140715%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td><td class="cellrowborder" valign="top" width="39.763976397639766%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td></tr><tr><th class="firstcol" id="mcps1.3.11.3.1.4.4.1" valign="top" width="19.521952195219523%"><p>输出ColorSpace</p></th><td class="cellrowborder" valign="top" width="40.714071407140715%"><p>OH_COLORSPACE_BT709_LIMIT</p></td><td class="cellrowborder" valign="top" width="39.763976397639766%"><p>OH_COLORSPACE_BT709_LIMIT</p></td></tr><tr><th class="firstcol" id="mcps1.3.11.3.1.4.5.1" valign="top" width="19.521952195219523%"><p>输出MetadataType</p></th><td class="cellrowborder" valign="top" width="40.714071407140715%"><p>OH_VIDEO_NONE</p></td><td class="cellrowborder" valign="top" width="39.763976397639766%"><p>OH_VIDEO_NONE</p></td></tr><tr><th class="firstcol" id="mcps1.3.11.3.1.4.6.1" valign="top" width="19.521952195219523%"><p>输出pixelFormat</p></th><td class="cellrowborder" valign="top" width="40.714071407140715%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_420_SP,</p><p>NATIVEBUFFER_PIXEL_FMT_YCRCB_420_SP,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_8888</p></td><td class="cellrowborder" valign="top" width="39.763976397639766%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_420_SP,</p><p>NATIVEBUFFER_PIXEL_FMT_YCRCB_420_SP,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_8888</p></td></tr></tbody></table>

#### \[h2\]开发步骤

HarmonyOS提供了Native侧的[VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)模块，可以将HDR Vivid视频转码成SDR视频，主要的开发步骤为（详细开发步骤可参考[视频色彩空间转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-csc)）：

1.  调用[OH\_VideoProcessing\_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_create)创建视频处理实例。
    
    void VideoProcessing::SetProcessingSurface(SampleInfo &sampleInfo) {
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Create(&processor, VIDEO\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION);
        ret = OH\_VideoProcessing\_GetSurface(processor, &sampleInfo.inWindow);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_GetSurface failed");
    }
    
    调用[OH\_VideoProcessing\_GetSurface()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_getsurface)在视频处理启动之前创建输入surface。
    
    int32\_t VideoEncoder::GetSurface(SampleInfo &sampleInfo) {
        int32\_t ret;
        if (sampleInfo.processType > 1) {
            ret = OH\_VideoEncoder\_GetSurface(encoder\_, &sampleInfo.outWindow);
        } else {
            ret = OH\_VideoEncoder\_GetSurface(encoder\_, &sampleInfo.window);
        }
        CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERROR, "Get surface failed, ret: %{public}d", ret);
        return AVCODEC\_SAMPLE\_OK;
    }
    
2.  调用[OH\_VideoProcessing\_SetSurface()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_setsurface)设置surface。
    
    int32\_t err = 0;
    err = OH\_NativeWindow\_SetMetadataValue(sampleInfo.outWindow, OH\_HDR\_METADATA\_TYPE, sizeof(uint8\_t),
                                           (uint8\_t \*)&sampleInfo.outputFormat.metadataType);
    CHECK\_AND\_RETURN\_LOG(err == 0, "SetMetadataValue BT2020\_PQ\_LIMIT failed");
    err = OH\_NativeWindow\_NativeWindowHandleOpt(sampleInfo.outWindow, SET\_FORMAT, sampleInfo.outputFormat.pixelFormat);
    CHECK\_AND\_RETURN\_LOG(err == 0, "NativeWindowHandleOpt BT2020\_PQ\_LIMIT failed");
    err = OH\_NativeWindow\_SetColorSpace(sampleInfo.outWindow,
                                        OH\_NativeBuffer\_ColorSpace(sampleInfo.outputFormat.colorSpace));
    CHECK\_AND\_RETURN\_LOG(err == 0, "SetColorSpace failed");
    
    ret = OH\_VideoProcessing\_SetSurface(processor, sampleInfo.outWindow);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "SetSurface failed");
    
3.  调用[OH\_VideoProcessing\_RegisterCallback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_registercallback)等函数创建并绑定回调函数。
    
    ret = OH\_VideoProcessingCallback\_Create(&callback);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_Create failed");
    ret = OH\_VideoProcessingCallback\_BindOnError(callback, OnError);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_BindOnError failed");
    ret = OH\_VideoProcessingCallback\_BindOnState(callback, OnState);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_BindOnState failed");
    ret = OH\_VideoProcessingCallback\_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_BindOnNewOutputBuffer failed");
    ret = OH\_VideoProcessing\_RegisterCallback(processor, callback, nullptr);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_RegisterCallback failed");
    
4.  调用[OH\_VideoProcessing\_Start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_start)启动色彩空间转换处理。
    
    void VideoProcessing::StartProcessing() {
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Start(processor);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_Start failed");
    }
    
5.  调用[OH\_VideoProcessing\_Stop()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_stop)停止色彩空间转换处理。
    
    void VideoProcessing::StopProcessing() {
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Stop(processor);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_Stop failed");
        DestroyProcessing();
    }
    
6.  调用[OH\_VideoProcessing\_Destroy()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_destroy)及[OH\_VideoProcessing\_DeinitializeEnvironment()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_deinitializeenvironment)释放处理实例和资源。
    
    void VideoProcessing::DestroyProcessing() {
        CHECK\_AND\_RETURN\_LOG(processor != nullptr, "processor is nullptr");
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_TAG, "start DestroyProcessing");
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Destroy(processor);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_Destroy failed");
        processor = nullptr;
        CHECK\_AND\_RETURN\_LOG(callback != nullptr, "callback is nullptr");
        ret = OH\_VideoProcessingCallback\_Destroy(callback);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_Destroy failed");
        callback = nullptr;
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_TAG, "Destroy And Callback\_Destroy succeed");
        OH\_VideoProcessing\_DeinitializeEnvironment();
    }
    

#### 基于VideoProcessing模块转换HDR色彩空间

#### \[h2\]实现原理

开发者可以调用[VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)模块提供的C API接口，实现HDR2HDR的色彩空间转换。支持的转码范围如下：

<table><tbody><tr><th class="firstcol" id="mcps1.3.14.3.1.6.1.1" valign="top" width="14.301430143014299%"><p>输入ColorSpace</p></th><td class="cellrowborder" valign="top" width="21.42214221422142%"><p>OH_COLORSPACE_BT2020_PQ_LIMIT</p></td><td class="cellrowborder" valign="top" width="21.562156215621563%"><p>OH_COLORSPACE_BT2020_PQ_LIMIT</p></td><td class="cellrowborder" valign="top" width="21.542154215421544%"><p>OH_COLORSPACE_BT2020_PQ_LIMIT</p></td><td class="cellrowborder" valign="top" width="21.172117211721172%"><p>OH_COLORSPACE_BT2020_PQ_HLG_LIMIT</p></td></tr><tr><th class="firstcol" id="mcps1.3.14.3.1.6.2.1" valign="top" width="14.301430143014299%"><p>输入MetadataType</p></th><td class="cellrowborder" valign="top" width="21.42214221422142%"><p>OH_VIDEO_HDR_VIVID</p></td><td class="cellrowborder" valign="top" width="21.562156215621563%"><p>OH_VIDEO_HDR_HLG</p></td><td class="cellrowborder" valign="top" width="21.542154215421544%"><p>OH_VIDEO_HDR_HLG</p></td><td class="cellrowborder" valign="top" width="21.172117211721172%"><p>OH_VIDEO_HDR_VIVID</p></td></tr><tr><th class="firstcol" id="mcps1.3.14.3.1.6.3.1" valign="top" width="14.301430143014299%"><p>输入pixelFormat</p></th><td class="cellrowborder" valign="top" width="21.42214221422142%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td><td class="cellrowborder" valign="top" width="21.562156215621563%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_</p><p>YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td><td class="cellrowborder" valign="top" width="21.542154215421544%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_</p><p>YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td><td class="cellrowborder" valign="top" width="21.172117211721172%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_</p><p>YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td></tr><tr><th class="firstcol" id="mcps1.3.14.3.1.6.4.1" valign="top" width="14.301430143014299%"><p>输出ColorSpace</p></th><td class="cellrowborder" valign="top" width="21.42214221422142%"><p>OH_COLORSPACE_BT2020_HLG_LIMIT</p></td><td class="cellrowborder" valign="top" width="21.562156215621563%"><p>OH_COLORSPACE_BT2020_HLG_LIMIT</p></td><td class="cellrowborder" valign="top" width="21.542154215421544%"><p>OH_COLORSPACE_BT2020_HLG_LIMIT</p></td><td class="cellrowborder" valign="top" width="21.172117211721172%"><p>OH_COLORSPACE_BT2020_PQ_HLG_LIMIT</p></td></tr><tr><th class="firstcol" id="mcps1.3.14.3.1.6.5.1" valign="top" width="14.301430143014299%"><p>输出MetadataType</p></th><td class="cellrowborder" valign="top" width="21.42214221422142%"><p>OH_VIDEO_HDR_VIVID</p></td><td class="cellrowborder" valign="top" width="21.562156215621563%"><p>OH_VIDEO_HDR_HDR10</p></td><td class="cellrowborder" valign="top" width="21.542154215421544%"><p>OH_VIDEO_HDR_VIVID</p></td><td class="cellrowborder" valign="top" width="21.172117211721172%"><p>OH_VIDEO_HDR_VIVID</p></td></tr><tr><th class="firstcol" id="mcps1.3.14.3.1.6.6.1" valign="top" width="14.301430143014299%"><p>输出pixelFormat</p></th><td class="cellrowborder" valign="top" width="21.42214221422142%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td><td class="cellrowborder" valign="top" width="21.562156215621563%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_</p><p>YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td><td class="cellrowborder" valign="top" width="21.542154215421544%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_</p><p>YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td><td class="cellrowborder" valign="top" width="21.172117211721172%"><p>NATIVEBUFFER_PIXEL_FMT_YCBCR_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_</p><p>YCRCB_P010,</p><p>NATIVEBUFFER_PIXEL_FMT_RGBA_1010102</p></td></tr></tbody></table>

#### \[h2\]开发步骤

具体开发步骤，可参考[视频色彩空间转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-csc)。

1.  初始化环境并查询是否支持视频颜色空间转换。
    
    bool VideoProcessing::IsColorSpaceConversionSupported(SampleInfo &sampleInfo) {
        OH\_VideoProcessing\_InitializeEnvironment();
        return OH\_VideoProcessing\_IsColorSpaceConversionSupported(&sampleInfo.inputFormat, &sampleInfo.outputFormat);
    }
    
2.  设置输入输出的值。
    
    sampleInfo.inputFormat.metadataType = OH\_VIDEO\_HDR\_VIVID;
    sampleInfo.inputFormat.colorSpace = OH\_COLORSPACE\_BT2020\_HLG\_LIMIT;
    sampleInfo.inputFormat.pixelFormat = NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010;
    sampleInfo.outputFormat.metadataType = OH\_VIDEO\_NONE;
    sampleInfo.outputFormat.colorSpace = OH\_COLORSPACE\_BT709\_LIMIT;
    sampleInfo.outputFormat.pixelFormat = NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP;
    
3.  创建色彩空间转换模块，并获取Surface。
    
    void VideoProcessing::SetProcessingSurface(SampleInfo &sampleInfo) {
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Create(&processor, VIDEO\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION);
        ret = OH\_VideoProcessing\_GetSurface(processor, &sampleInfo.inWindow);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_GetSurface failed");
    }
    
4.  配置异步回调函数。
    
    void OnError(OH\_VideoProcessing \*videoProcessor, VideoProcessing\_ErrorCode error, void \*userData) {
        (void)videoProcessor;
        (void)error;
        (void)userData;
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, LOG\_TAG, "OnError: %{public}d", error);
    }
    
    void OnState(OH\_VideoProcessing \*videoProcessor, VideoProcessing\_State state, void \*userData) {
        (void)videoProcessor;
        (void)state;
        (void)userData;
    }
    
    void OnNewOutputBuffer(OH\_VideoProcessing \*videoProcessor, uint32\_t index, void \*userData) {
    
        OH\_VideoProcessing\_RenderOutputBuffer(videoProcessor, index);
        (void)userData;
    }
    
    ret = OH\_VideoProcessingCallback\_Create(&callback);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_Create failed");
    ret = OH\_VideoProcessingCallback\_BindOnError(callback, OnError);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_BindOnError failed");
    ret = OH\_VideoProcessingCallback\_BindOnState(callback, OnState);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_BindOnState failed");
    ret = OH\_VideoProcessingCallback\_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_BindOnNewOutputBuffer failed");
    ret = OH\_VideoProcessing\_RegisterCallback(processor, callback, nullptr);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_RegisterCallback failed");
    
5.  设置Surface。
    
    int32\_t err = 0;
    err = OH\_NativeWindow\_SetMetadataValue(sampleInfo.outWindow, OH\_HDR\_METADATA\_TYPE, sizeof(uint8\_t),
                                           (uint8\_t \*)&sampleInfo.outputFormat.metadataType);
    CHECK\_AND\_RETURN\_LOG(err == 0, "SetMetadataValue BT2020\_PQ\_LIMIT failed");
    err = OH\_NativeWindow\_NativeWindowHandleOpt(sampleInfo.outWindow, SET\_FORMAT, sampleInfo.outputFormat.pixelFormat);
    CHECK\_AND\_RETURN\_LOG(err == 0, "NativeWindowHandleOpt BT2020\_PQ\_LIMIT failed");
    err = OH\_NativeWindow\_SetColorSpace(sampleInfo.outWindow,
                                        OH\_NativeBuffer\_ColorSpace(sampleInfo.outputFormat.colorSpace));
    CHECK\_AND\_RETURN\_LOG(err == 0, "SetColorSpace failed");
    
    ret = OH\_VideoProcessing\_SetSurface(processor, sampleInfo.outWindow);
    CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "SetSurface failed");
    
6.  调用[OH\_VideoProcessing\_Start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_start)启动色彩空间转换处理。
    
    void VideoProcessing::StartProcessing() {
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Start(processor);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_Start failed");
    }
    
7.  调用[OH\_VideoProcessing\_Stop()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_stop)停止色彩空间转换处理。
    
    void VideoProcessing::StopProcessing() {
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Stop(processor);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_Stop failed");
        DestroyProcessing();
    }
    
    调用[OH\_VideoProcessing\_Destroy()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_destroy)销毁视频处理实例。
    
    void VideoProcessing::DestroyProcessing() {
        CHECK\_AND\_RETURN\_LOG(processor != nullptr, "processor is nullptr");
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_TAG, "start DestroyProcessing");
        VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Destroy(processor);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessing\_Destroy failed");
        processor = nullptr;
        CHECK\_AND\_RETURN\_LOG(callback != nullptr, "callback is nullptr");
        ret = OH\_VideoProcessingCallback\_Destroy(callback);
        CHECK\_AND\_RETURN\_LOG(ret == VIDEO\_PROCESSING\_SUCCESS, "OH\_VideoProcessingCallback\_Destroy failed");
        callback = nullptr;
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_TAG, "Destroy And Callback\_Destroy succeed");
        OH\_VideoProcessing\_DeinitializeEnvironment();
    }
    

#### 示例代码

-   [实现HDR视频转码SDR视频功能](https://gitcode.com/harmonyos_samples/hdr2sdr/tree/master/)
