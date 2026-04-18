---
title: "基于Buffer模式进行视频转码"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-buffer-mode-transcoding"
menu_path:
  - "最佳实践"
  - "媒体"
  - "音频和视频"
  - "基于Buffer模式进行视频转码"
captured_at: "2026-04-17T01:54:15.194Z"
---

# 基于Buffer模式进行视频转码

#### 概述

视频转码是指通过调整编码、比特率等参数将视频文件从一种格式转换为另一种格式的过程。Buffer模式是系统提供的一种视频编解码的方式，是媒体子系统的核心能力。在Buffer模式中，编码或解码完成的数据会以共享内存的方式输出，开发者可以获取共享内存的地址和数据信息，适用于视频转码、编辑等场景。

本文主要介绍了视频编解码的基本概念、Buffer模式下的视频编解码原理，并详细介绍了视频转码的实现方案和开发步骤。

#### 实现原理

#### \[h2\]基本概念

视频文件格式是视频保存的格式，常见的格式有MP4、AVI等。在视频文件（以MP4文件解码为例）解码时，首先需要将视频进行解封装，解封装会将一个封装好的音视频文件（如MP4、FLV等）中的音频和视频数据流分离出来。然后，从数据流中取出视频的媒体样本sample，通过视频解码器将媒体数据解码成YUV数据，流程如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/LLmumTkYTDSBjSuP6-Qh4g/zh-cn_image_0000002353142782.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=AC209875A9D976E617644BCF8D62E16AEC7990F0D993B440644671DBD114724C "点击放大")

在视频文件编码（以MP4文件编码为例）时，首先会通过视频编码器对YUV数据进行编码，将未压缩的视频数据YUV压缩成视频码流H.264，然后，将编码后的媒体数据按一定的格式封装存储到MP4文件里，流程如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/-fvkijrrTAOthUjO6E3ARA/zh-cn_image_0000002387023117.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=EFACA4F70B388EC768061C1ECEE8CBF27AD408FE847956FEEF9816D58B534E3F "点击放大")

关于视频文件编解码支持的格式，详情请参考[AVCodec支持的格式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avcodec-support-formats)。

#### \[h2\]YUV跨距对齐

YUV是编译true-color颜色空间（color space）的种类，Y'UV、YUV等专有名词都可以称为YUV。I420、NV12、NV21等是YUV具体的存储格式。I420和YV12属于YUV420P格式，NV12 和NV21属于YUV420SP格式。

由于硬件内存访问对齐要求，YUV图像数据在写入内存缓冲区时，其每行数据的存储长度会被硬件或底层驱动自动扩展至规定的对齐粒度（例如16/32/64字节），即YUV跨距对齐。在YUV跨距对齐时，会对每行有效像素数据进行边界填充（Padding），导致Stride值大于图像的有效像素宽度（以字节计算）。

以I420格式为例，其跨距对齐后的格式如下所示。其中，w\_stride是数据填充后的宽跨距，h\_stride是数据填充后的高跨距，height是实际的高度，width是实际的宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/faXAxqsqQMGdwvNcCZjHKQ/zh-cn_image_0000002353302590.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=9A769177BDFC078167172A55AE5E8BE149D6A0E4C5342234D95A920528D6C40B "点击放大")

#### \[h2\]视频编解码原理

视频编解码器的原理和实现机制是一样的，区别是处理的数据有所不同。在编码时，输入数据是原始数据（YUV），输出数据是视频数据（如H.264），解码的过程与编码相反。这里以视频解码的过程进行原理说明。

在视频解码的过程中，主要包含两个部分，分别为输入数据流转和输出数据流转。开发者需要通过输入数据流转将需要解码的数据填充给解码器，解码器再进行解码处理。在输出数据流转中，解码器会将解码完成的数据返回给开发者使用，在开发者使用完毕后，需要通知解码器释放视频数据，从而实现整体的Buffer循环，详细原理流程如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/FPLkBdnZS1GrY5HtleIhJQ/zh-cn_image_0000002386942825.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=AAF3BC53B57E8E287C8A81F5028F58C9E7BAF82D8FB4BD3BF4F5B2296001AEB5 "点击放大")

输入数据流转的步骤如下所示。

1.  解码器提供空的Buffer地址，该地址用于填充需要解码的视频数据。
2.  将解封装后的视频数据（如H.264）填充到解码器提供的Buffer地址中。
3.  通知解码器，当前Buffer地址已完成视频数据填充。
4.  当解码器收到通知后，会对数据进行解码操作。

输出数据流转的步骤如下所示。

1.  在完成输出数据流转后，解码器会提供已解码的数据。
2.  获取数据后，开发者可以根据实际业务使用视频数据，如送显到屏幕。
3.  使用完毕后，开发者需要将Buffer的使用权移交给解码器。
4.  解码器会循环再利用Buffer地址。Buffer内的视频数据不会被释放或者清零，而是在下一次循环中，将解码好的数据直接覆盖写入到已经空闲的Buffer地址里。

#### 视频转码

#### \[h2\]场景描述

不同的设备和平台支持视频格式各有不同，通过转码可以将视频转化成设备或平台适配的格式，从而确保视频能够正确地播放与观看，提高视频的兼容性和可播放性。例如，部分平台仅支持特定的视频格式。在相同的视频格式下，其分辨率、帧率、比特率等参数也各有不同，通过改变相应的参数，可以缩小视频文件的大小，从而节省视频的存储空间。

在ArkTS侧，系统提供了转码的相关接口AVTranscoder，可以实现简单的视频转码操作。而在复杂的场景下，如视频裁剪等场景，则需要调用系统的视频编解码的相关能力进行实现。在Buffer模式下的视频转码，可以对视频数据进行读写操作，能够满足更加灵活多变的场景需求。

#### \[h2\]开发步骤

在视频转码的场景中，视频文件会经历解封装、视频解码、视频编码和视频封装的步骤，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/CjFRZD3pSoSmbi66tBIz6w/zh-cn_image_0000002353142786.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=88AF1D8BB0B49443788ECA03B671FE448C4ACD0AD399C1DD9BA38D1D0B51350D "点击放大")

其主要包含三个大步骤。

**1\. 视频编解码环境初始化**：为后续视频编码、解码提前创建好对应的实例，并设置编解码所需要的参数。

**2\. 视频文件解码**：视频文件解码包含了视频解封装、视频解码的操作，最后生成解码后的视频数据。

**3\. 视频文件编码**：将解码后的数据进行拷贝处理，并通过编码器进行编码，最后封装到对应的视频文件中。

**视频编解码环境初始化**开发步骤如下所示。

1.1 创建与配置解封装器。

1.2 创建与配置解码器，并注册解码器的回调函数。其中，回调函数OnNeedInputBuffer()提供了解码空Buffer地址，回调函数OnNewOutputBuffer()提供了解码后的视频数据。

1.3 创建与配置封装器。

1.4 创建与配置编码器，并注册编码器的回调函数，回调函数需要配置的内容与解码器相同。

在视频文件解码中，主要包含两个步骤，输入缓存处理、输出缓存处理。在OnNeedInputBuffer()回调函数中，维护了一个空Buffer的缓存队列，在实现输入缓存处理时，需要解封装、填充视频数据。在OnNewOutputBuffer()回调函数中，维护了一个已解码视频数据的缓存队列，在实现输出缓存处理时，需要处理视频数据，其调用顺序如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/UkZ7kY98SA276mYNd8PKRw/zh-cn_image_0000002387023121.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=DA51DB75DD5CD56D499FBD411ADBF15A38027B38AB17201B87CE2830503DE5EC "点击放大")

**视频文件解码**开发步骤如下所示。

2.1 通过inputBufferInfoQueue获取视频缓存空地址。

2.2 通过Demuxer读取媒体数据，即视频码流数据及其格式。

2.3 在OH\_VideoDecoder\_PushInputBuffer()中设置对应的视频缓存数据。

2.4 在解码完成后，通过outputBufferInfoQueue获取视频缓存数据。

2.5 处理缓存数据，最后通过OH\_VideoDecoder\_FreeOutputBuffer()刷新缓存，将缓存资源返回给解码器。

**视频文件编码**开发步骤如下所示。在视频文件编码中，大致的处理流程与视频文件解码类似，而编码的输入缓存的数据来源于解码的输出缓存，所以，可以在解码的输出缓存处理子线程中同步处理编码的输入缓存数据。

3.1 通过inputBufferInfoQueue获取视频缓存地址。

3.2 将解码的输出缓存数据拷贝到编码的输入缓存中。

3.3 通过OH\_VideoEncoder\_PushInputBuffer()将已填充的输入缓存提交给编码器。

3.4 在编码完成后，通过outputBufferInfoQueue获取视频缓存数据。

3.5 通过Muxer将编码完成的视频数据写入到视频文件中

#### \[h2\]代码实现

1.  视频编解码环境初始化。
    -   初始化视频解码环境。
        
        int32\_t Transcoding::InitDecoder() {
            CHECK\_AND\_RETURN\_RET\_LOG(!isStarted\_, AVCODEC\_SAMPLE\_ERR\_ERROR, "Already started.");
            CHECK\_AND\_RETURN\_RET\_LOG(demuxer\_ == nullptr && videoDecoder\_ == nullptr,
                                     AVCODEC\_SAMPLE\_ERR\_ERROR, "Already started.");
        
            videoDecoder\_ = std::make\_unique<VideoDecoder>();
            demuxer\_ = std::make\_unique<Demuxer>();
        
            isReleased\_ = false;
            int32\_t ret = demuxer\_->Create(sampleInfo\_);
        
            if (ret == AVCODEC\_SAMPLE\_ERR\_OK) {
                ret = CreateVideoDecoder();
            } else {
                AVCODEC\_SAMPLE\_LOGE("Create audio decoder failed");
            }
            return ret;
        }
        
    -   创建解封装器。在创建解封装器时，需要根据需要解码的视频文件fd创建对应的OH\_AVSource对象，再根据该对象创建对应的解码器。
        
        int32\_t Demuxer::Create(SampleInfo &info) {
            source\_ = OH\_AVSource\_CreateWithFD(info.inputFd, info.inputFileOffset, info.inputFileSize);
            CHECK\_AND\_RETURN\_RET\_LOG(source\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR,
                                     "Create demuxer source failed, fd: %{public}d, offset: %{public}" PRId64
                                     ", file size: %{public}" PRId64,
                                     info.inputFd, info.inputFileOffset, info.inputFileSize);
            demuxer\_ = OH\_AVDemuxer\_CreateWithSource(source\_);
            CHECK\_AND\_RETURN\_RET\_LOG(demuxer\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Create demuxer failed");
        
            auto sourceFormat = std::shared\_ptr<OH\_AVFormat>(OH\_AVSource\_GetSourceFormat(source\_), OH\_AVFormat\_Destroy);
            CHECK\_AND\_RETURN\_RET\_LOG(sourceFormat != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Get source format failed");
        
            int32\_t ret = GetTrackInfo(sourceFormat, info);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Get video track info failed");
        
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   创建完解封装器后，可以通过解封装器获取视频对应的参数，如视频的宽高、帧率等信息。
        
        int32\_t Demuxer::GetTrackInfo(std::shared\_ptr<OH\_AVFormat> sourceFormat, SampleInfo &info) {
            int32\_t trackCount = 0;
            OH\_AVFormat\_GetIntValue(sourceFormat.get(), OH\_MD\_KEY\_TRACK\_COUNT, &trackCount);
            for (int32\_t index = 0; index < trackCount; index++) {
                int trackType = -1;
                auto trackFormat =
                    std::shared\_ptr<OH\_AVFormat>(OH\_AVSource\_GetTrackFormat(source\_, index), OH\_AVFormat\_Destroy);
                OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_TRACK\_TYPE, &trackType);
                if (trackType == MEDIA\_TYPE\_VID) {
                    OH\_AVDemuxer\_SelectTrackByID(demuxer\_, index);
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_WIDTH, &info.videoWidth);
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_HEIGHT, &info.videoHeight);
                    OH\_AVFormat\_GetDoubleValue(trackFormat.get(), OH\_MD\_KEY\_FRAME\_RATE, &info.frameRate);
                    OH\_AVFormat\_GetLongValue(trackFormat.get(), OH\_MD\_KEY\_BITRATE, &info.bitrate);
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_ROTATION, &info.rotation);
                    char \*videoCodecMime;
                    OH\_AVFormat\_GetStringValue(trackFormat.get(), OH\_MD\_KEY\_CODEC\_MIME,
                                               const\_cast<char const \*\*>(&videoCodecMime));
                    info.videoCodecMime = videoCodecMime;
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_PROFILE, &info.hevcProfile);
                    videoTrackId\_ = index;
        
                    AVCODEC\_SAMPLE\_LOGI("====== Demuxer Video config ======");
                    AVCODEC\_SAMPLE\_LOGI("Mime: %{public}s", videoCodecMime);
                    AVCODEC\_SAMPLE\_LOGI("%{public}d\*%{public}d, %{public}.1ffps, %{public}" PRId64 "kbps", info.videoWidth,
                                        info.videoHeight, info.frameRate, info.bitrate / 1024);
                    AVCODEC\_SAMPLE\_LOGI("====== Demuxer Video config ======");
                } else if (trackType == MEDIA\_TYPE\_AUD) {
                    OH\_AVDemuxer\_SelectTrackByID(demuxer\_, index);
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, &info.audioSampleForamt);
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, &info.audioChannelCount);
                    OH\_AVFormat\_GetLongValue(trackFormat.get(), OH\_MD\_KEY\_CHANNEL\_LAYOUT, &info.audioChannelLayout);
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, &info.audioSampleRate);
                    char \*audioCodecMime;
                    OH\_AVFormat\_GetStringValue(trackFormat.get(), OH\_MD\_KEY\_CODEC\_MIME,
                                               const\_cast<char const \*\*>(&audioCodecMime));
                    uint8\_t \*codecConfig = nullptr;
                    OH\_AVFormat\_GetBuffer(trackFormat.get(), OH\_MD\_KEY\_CODEC\_CONFIG, &codecConfig, &info.codecConfigLen);
                    if (info.codecConfigLen > 0 && info.codecConfigLen < sizeof(info.codecConfig)) {
                        memcpy(info.codecConfig, codecConfig, info.codecConfigLen);
                        AVCODEC\_SAMPLE\_LOGI(
                            "codecConfig:%{public}p, len:%{public}i, 0:0x%{public}02x 1:0x:%{public}02x, bufLen:%{public}u",
                            info.codecConfig, (int)info.codecConfigLen, info.codecConfig\[0\], info.codecConfig\[1\],
                            sizeof(info.codecConfig));
                    }
                    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_AAC\_IS\_ADTS, &info.aacAdts);
                    
                    info.audioCodecMime = audioCodecMime;
                    audioTrackId\_ = index;
        
                    AVCODEC\_SAMPLE\_LOGI("====== Demuxer Audio config ======");
                    AVCODEC\_SAMPLE\_LOGI(
                        "audioMime:%{public}s sampleForamt:%{public}d "
                        "sampleRate:%{public}d channelCount:%{public}d channelLayout:%{public}d adts:%{public}i",
                        info.audioCodecMime.c\_str(), info.audioSampleForamt, info.audioSampleRate, info.audioChannelCount,
                        info.audioChannelLayout, info.aacAdts);
                    AVCODEC\_SAMPLE\_LOGI("====== Demuxer Audio config ======");
                }
            }
        
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   创建视频解码器。
        
        int32\_t Transcoding::CreateVideoDecoder() {
            AVCODEC\_SAMPLE\_LOGW("video mime:%{public}s", sampleInfo\_.videoCodecMime.c\_str());
            int32\_t ret = videoDecoder\_->Create(sampleInfo\_.videoCodecMime);
            if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
                AVCODEC\_SAMPLE\_LOGW("Create video decoder failed, mime:%{public}s", sampleInfo\_.videoCodecMime.c\_str());
            } else {
                videoDecContext\_ = new CodecUserData;
                ret = videoDecoder\_->Config(sampleInfo\_, videoDecContext\_);
                CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, ret, "Video Decoder config failed");
            }
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   配置视频解码器，包括视频的宽、高、分辨率等基础信息和解码器的回调函数。
        
        // Setting the callback function
        int32\_t VideoDecoder::SetCallback(CodecUserData \*codecUserData) {
            int32\_t ret = AV\_ERR\_OK;
            ret = OH\_VideoDecoder\_RegisterCallback(decoder\_,
                                                   {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
                                                    SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},
                                                   codecUserData);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Set callback failed, ret: %{public}d", ret);
        
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
        int32\_t VideoDecoder::Configure(const SampleInfo &sampleInfo) {
            OH\_AVFormat \*format = OH\_AVFormat\_Create();
            CHECK\_AND\_RETURN\_RET\_LOG(format != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "AVFormat create failed");
        
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
            OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.frameRate);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, sampleInfo.pixelFormat);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ROTATION, sampleInfo.rotation);
        
            AVCODEC\_SAMPLE\_LOGI("====== VideoDecoder config ======");
            AVCODEC\_SAMPLE\_LOGI("%{public}d\*%{public}d, %{public}.1ffps", sampleInfo.videoWidth, sampleInfo.videoHeight,
                                sampleInfo.frameRate);
            AVCODEC\_SAMPLE\_LOGI("====== VideoDecoder config ======");
            int ret = OH\_VideoDecoder\_Configure(decoder\_, format);
            OH\_AVFormat\_Destroy(format);
            format = nullptr;
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Config failed, ret: %{public}d", ret);
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
        int32\_t VideoDecoder::Config(const SampleInfo &sampleInfo, CodecUserData \*codecUserData) {
            CHECK\_AND\_RETURN\_RET\_LOG(decoder\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Decoder is null");
            CHECK\_AND\_RETURN\_RET\_LOG(codecUserData != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Invalid param: codecUserData");
        
            // Configure video decoder
            int32\_t ret = Configure(sampleInfo);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Configure failed");
            
            // SetCallback for video decoder
            ret = SetCallback(codecUserData);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR,
                                     "Set callback failed, ret: %{public}d", ret);
        
            // Prepare video decoder
            ret = OH\_VideoDecoder\_Prepare(decoder\_);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Prepare failed, ret: %{public}d", ret);
        
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   初始化视频编码环境，包括创建配置视频编码器、视频封装器。
        
        int32\_t Transcoding::InitEncoder() {
            CHECK\_AND\_RETURN\_RET\_LOG(!isStarted\_, AVCODEC\_SAMPLE\_ERR\_ERROR, "Already started.");
            CHECK\_AND\_RETURN\_RET\_LOG(muxer\_ == nullptr && videoEncoder\_ == nullptr,
                                     AVCODEC\_SAMPLE\_ERR\_ERROR, "Already started.");
            
            videoEncoder\_ = std::make\_unique<VideoEncoder>();
            muxer\_ = std::make\_unique<Muxer>();
            
            int32\_t ret = muxer\_->Create(sampleInfo\_.outputFd);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, ret, "Create muxer with fd(%{public}d) failed",
                                     sampleInfo\_.outputFd);
            ret = muxer\_->Config(sampleInfo\_);
            
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, ret, "Create audio encoder failed");
        
            ret = CreateVideoEncoder();
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, ret, "Create video encoder failed");
            
            AVCODEC\_SAMPLE\_LOGI("Succeed");
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   创建视频编码器。
        
        // Create a video coder and initialize it
        int32\_t VideoEncoder::Create(const std::string &videoCodecMime) {
            encoder\_ = OH\_VideoEncoder\_CreateByMime(videoCodecMime.c\_str());
            CHECK\_AND\_RETURN\_RET\_LOG(encoder\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Create failed");
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   配置视频编码器。
        
        int32\_t VideoEncoder::Config(SampleInfo &sampleInfo, CodecUserData \*codecUserData) {
            CHECK\_AND\_RETURN\_RET\_LOG(encoder\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Encoder is null");
            CHECK\_AND\_RETURN\_RET\_LOG(codecUserData != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Invalid param: codecUserData");
        
            // Configure video encoder
            int32\_t ret = Configure(sampleInfo);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Configure failed");
        
            // SetCallback for video encoder
            ret = SetCallback(codecUserData);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR,
                                     "Set callback failed, ret: %{public}d", ret);
        
            // Prepare video encoder
            ret = OH\_VideoEncoder\_Prepare(encoder\_);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Prepare failed, ret: %{public}d", ret);
        
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
        // ...
        
        int32\_t VideoEncoder::Configure(const SampleInfo &sampleInfo) {
            OH\_AVFormat \*format = OH\_AVFormat\_Create();
            CHECK\_AND\_RETURN\_RET\_LOG(format != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "AVFormat create failed");
        
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
            OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.outputFrameRate);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, sampleInfo.pixelFormat);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE, sampleInfo.bitrateMode);
            OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, sampleInfo.outputBitrate);
            OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PROFILE, sampleInfo.hevcProfile);
            // Setting HDRVivid-related parameters
            if (sampleInfo.isHDRVivid) {
                OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_I\_FRAME\_INTERVAL, sampleInfo.iFrameInterval);
                OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_RANGE\_FLAG, sampleInfo.rangFlag);
                OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_COLOR\_PRIMARIES, sampleInfo.primary);
                OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS, sampleInfo.transfer);
                OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_MATRIX\_COEFFICIENTS, sampleInfo.matrix);
            }
            AVCODEC\_SAMPLE\_LOGI("====== VideoEncoder config ======");
            AVCODEC\_SAMPLE\_LOGI("%{public}d\*%{public}d, %{public}.1ffps", sampleInfo.videoWidth, sampleInfo.videoHeight,
                                sampleInfo.frameRate);
            // 1024: ratio of kbps to bps
            AVCODEC\_SAMPLE\_LOGI("BitRate Mode: %{public}d, BitRate: %{public}" PRId64 "kbps", sampleInfo.bitrateMode,
                                sampleInfo.bitrate / 1024);
            AVCODEC\_SAMPLE\_LOGI("====== VideoEncoder config ======");
            
            // Setting the Encoder
            int ret = OH\_VideoEncoder\_Configure(encoder\_, format);
            OH\_AVFormat\_Destroy(format);
            format = nullptr;
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Config failed, ret: %{public}d", ret);
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   配置视频封装器。在配置视频封装器时，需要设置视频封装的格式，包括视频宽高、帧率、编码格式等。
        
        int32\_t Muxer::Config(SampleInfo &sampleInfo) {
            CHECK\_AND\_RETURN\_RET\_LOG(muxer\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Muxer is null");
            OH\_AVFormat \*formatVideo =
                OH\_AVFormat\_CreateVideoFormat(sampleInfo.outputVideoCodecMime.data(), sampleInfo.videoWidth, sampleInfo.videoHeight);
            CHECK\_AND\_RETURN\_RET\_LOG(formatVideo != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Create video format failed");
        
            OH\_AVFormat\_SetDoubleValue(formatVideo, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.outputFrameRate);
            OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
            OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
            OH\_AVFormat\_SetStringValue(formatVideo, OH\_MD\_KEY\_CODEC\_MIME, sampleInfo.outputVideoCodecMime.data());
            if (sampleInfo.isHDRVivid) {
                OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID, 1);
                OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_RANGE\_FLAG, sampleInfo.rangFlag);
                OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_COLOR\_PRIMARIES, sampleInfo.primary);
                OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS, sampleInfo.transfer);
                OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_MATRIX\_COEFFICIENTS, sampleInfo.matrix);
            }
        
            int32\_t ret = OH\_AVMuxer\_AddTrack(muxer\_, &videoTrackId\_, formatVideo);
            OH\_AVFormat\_Destroy(formatVideo);
            formatVideo = nullptr;
            OH\_AVMuxer\_SetRotation(muxer\_, sampleInfo.rotation);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "AddTrack failed");
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
2.  视频文件解码。
    -   启动视频转码，包括视频解码输入缓存处理线程、输出缓存处理线程、编码输出缓存处理线程。
        
        int32\_t Transcoding::Start() {
            std::unique\_lock<std::mutex> lock(mutex\_);
            int32\_t ret;
            CHECK\_AND\_RETURN\_RET\_LOG(!isStarted\_, AVCODEC\_SAMPLE\_ERR\_ERROR, "Already started.");
            CHECK\_AND\_RETURN\_RET\_LOG(demuxer\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Already started.");
            if (videoDecContext\_) {
                ret = videoDecoder\_->Start();
                if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
                    AVCODEC\_SAMPLE\_LOGE("Video Decoder start failed");
                    lock.unlock();
                    StartRelease();
                    return AVCODEC\_SAMPLE\_ERR\_ERROR;
                }
                isStarted\_ = true;
                videoDecInputThread\_ = std::make\_unique<std::thread>(&Transcoding::VideoDecInputThread, this);
                videoDecOutputThread\_ = std::make\_unique<std::thread>(&Transcoding::VideoDecOutputThread, this);
        
                if (videoDecInputThread\_ == nullptr || videoDecOutputThread\_ == nullptr) {
                    AVCODEC\_SAMPLE\_LOGE("Create thread failed");
                    lock.unlock();
                    StartRelease();
                    return AVCODEC\_SAMPLE\_ERR\_ERROR;
                }
            }
        
            if (videoEncContext\_) {
                CHECK\_AND\_RETURN\_RET\_LOG(videoEncoder\_ != nullptr && muxer\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR,
                                         "Already started.");
                int32\_t ret = muxer\_->Start();
                CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, ret, "Muxer start failed");
                ret = videoEncoder\_->Start();
                CHECK\_AND\_RETURN\_RET\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, ret, "Encoder start failed");
                videoEncOutputThread\_ = std::make\_unique<std::thread>(&Transcoding::VideoEncOutputThread, this);
                if (videoEncOutputThread\_ == nullptr) {
                    AVCODEC\_SAMPLE\_LOGE("Create thread failed");
                    StartRelease();
                    return AVCODEC\_SAMPLE\_ERR\_ERROR;
                }
            }
            
            AVCODEC\_SAMPLE\_LOGI("Succeed");
            doneCond\_.notify\_all();
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   视频解码输入缓存处理。
        
        void Transcoding::VideoDecInputThread() {
            while (true) {
                CHECK\_AND\_BREAK\_LOG(isStarted\_, "Decoder input thread out");
                std::unique\_lock<std::mutex> lock(videoDecContext\_->inputMutex);
                bool condRet = videoDecContext\_->inputCond.wait\_for(
                    lock, 5s, \[this\]() { return !isStarted\_ || !videoDecContext\_->inputBufferInfoQueue.empty(); });
                CHECK\_AND\_BREAK\_LOG(isStarted\_, "Work done, thread out");
                CHECK\_AND\_CONTINUE\_LOG(!videoDecContext\_->inputBufferInfoQueue.empty(),
                                       "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
        
                CodecBufferInfo bufferInfo = videoDecContext\_->inputBufferInfoQueue.front();
                videoDecContext\_->inputBufferInfoQueue.pop();
                videoDecContext\_->inputFrameCount++;
                lock.unlock();
        
                demuxer\_->ReadSample(demuxer\_->GetVideoTrackId(), reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer),
                                     bufferInfo.attr);
        
                int32\_t ret = videoDecoder\_->PushInputBuffer(bufferInfo);
                CHECK\_AND\_BREAK\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, "Push data failed, thread out");
        
                CHECK\_AND\_BREAK\_LOG(!(bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS),
                                    "VideoDecInputThread Catch EOS, thread out");
            }
        }
        
    -   视频解码输出缓存处理。
        
        void Transcoding::VideoDecOutputThread() {
            sampleInfo\_.frameInterval = MICROSECOND / sampleInfo\_.frameRate;
            while (true) {
                CHECK\_AND\_BREAK\_LOG(isStarted\_, "Decoder output thread out");
                std::unique\_lock<std::mutex> lock(videoDecContext\_->outputMutex);
                bool condRet = videoDecContext\_->outputCond.wait\_for(lock, 5s, \[this\]() {
                    return !isStarted\_ ||
                           !(videoDecContext\_->outputBufferInfoQueue.empty() && videoEncContext\_->inputBufferInfoQueue.empty());
                });
                CHECK\_AND\_BREAK\_LOG(isStarted\_, "Decoder output thread out");
                CHECK\_AND\_CONTINUE\_LOG(!videoDecContext\_->outputBufferInfoQueue.empty(),
                                       "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
                CHECK\_AND\_CONTINUE\_LOG(!videoEncContext\_->inputBufferInfoQueue.empty(),
                                       "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
        
                CodecBufferInfo bufferInfo = videoDecContext\_->outputBufferInfoQueue.front();
                videoDecContext\_->outputBufferInfoQueue.pop();
                videoDecContext\_->outputFrameCount++;
                AVCODEC\_SAMPLE\_LOGW("Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
                                    videoDecContext\_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
                                    bufferInfo.attr.pts);
                lock.unlock();
        
                // get Buffer from inputBufferInfoQueue
                CodecBufferInfo encBufferInfo = videoEncContext\_->inputBufferInfoQueue.front();
                videoEncContext\_->inputBufferInfoQueue.pop();
                videoEncContext\_->inputFrameCount++;
                
                AVCODEC\_SAMPLE\_LOGW(
                    "Out bufferInfo flags: %{public}u, offset: %{public}d, pts: %{public}u, size: %{public}" PRId64,
                    bufferInfo.attr.flags, bufferInfo.attr.offset, bufferInfo.attr.pts, bufferInfo.attr.size);
        
        
                encBufferInfo.bufferAddr = OH\_AVBuffer\_GetAddr(reinterpret\_cast<OH\_AVBuffer \*>(encBufferInfo.buffer));
                bufferInfo.bufferAddr = OH\_AVBuffer\_GetAddr(reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer));
                CopyStrideYUV420SP(encBufferInfo, bufferInfo);
        
                AVCODEC\_SAMPLE\_LOGW(
                    "Out encBufferInfo flags: %{public}u, offset: %{public}d, pts: %{public}u, size: %{public}d" PRId64,
                    encBufferInfo.attr.flags, encBufferInfo.attr.offset, encBufferInfo.attr.pts, encBufferInfo.attr.size);
        
                OH\_AVBuffer\_SetBufferAttr(reinterpret\_cast<OH\_AVBuffer \*>(encBufferInfo.buffer), &encBufferInfo.attr);
        
                // Free Decoder's output buffer
                int32\_t ret = videoDecoder\_->FreeOutputBuffer(bufferInfo.bufferIndex, false);
                CHECK\_AND\_BREAK\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, "Decoder output thread out");
        
                // Push input buffer to Encoder
                videoEncoder\_->PushInputBuffer(encBufferInfo);
        
                if (bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                    AVCODEC\_SAMPLE\_LOGW("VideoDecOutputThread Catch EOS, thread out" PRId64);
                    break;
                }
            }
        }
        
3.  视频文件编码。
    -   在解码输出缓存子线程中，将解码输出缓存同步拷贝AVBuffer。同时，需要注意的是解码的数据中会进行YUV跨距对齐，需要专门处理对应的跨距，偏移填充的数据，才能正确的进行视频编码。
        
        void Transcoding::CopyStrideYUV420SP(CodecBufferInfo &encBufferInfo, CodecBufferInfo &bufferInfo) {
            int32\_t videoWidth = videoDecContext\_->width;
            int32\_t &stride = videoDecContext\_->widthStride;
            int32\_t size = 0;
            uint8\_t \*tempBufferAddr = encBufferInfo.bufferAddr;
        
            size += videoDecContext\_->height \* videoWidth \* 3 / 2;
            if (videoWidth == videoDecContext\_->widthStride && videoDecContext\_->heightStride == videoDecContext\_->height) {
                std::memcpy(tempBufferAddr, bufferInfo.bufferAddr, size);
            } else {
                // copy Y
                for (int32\_t row = 0; row < videoDecContext\_->height; row++) {
                    std::memcpy(tempBufferAddr, bufferInfo.bufferAddr, videoWidth);
                    tempBufferAddr += videoWidth;
                    bufferInfo.bufferAddr += stride;
                }
                bufferInfo.bufferAddr += (videoDecContext\_->heightStride - videoDecContext\_->height) \* stride;
        
                // copy U/V
                for (int32\_t row = 0; row < (videoDecContext\_->height / 2); row++) {
                    std::memcpy(tempBufferAddr, bufferInfo.bufferAddr, videoWidth);
                    tempBufferAddr += videoWidth;
                    bufferInfo.bufferAddr += stride;
                }
            }
            
            encBufferInfo.attr.size = size;
            encBufferInfo.attr.flags = bufferInfo.attr.flags;
            encBufferInfo.attr.offset = bufferInfo.attr.offset;
            encBufferInfo.attr.pts = bufferInfo.attr.pts;
        
            tempBufferAddr = nullptr;
            delete tempBufferAddr;
        }
        
    -   同时，拷贝的AVBuffer内存需要通过OH\_AVBuffer\_SetBufferAttr()设置对应的属性，其中，size属性为当前数据的大小，是实际AVBuffer的数据大小。最后，通过OH\_VideoEncoder\_PushInputBuffer()将填充的输入缓存数据提交给编码器。
        
        int32\_t VideoEncoder::PushInputBuffer(CodecBufferInfo &info) {
            CHECK\_AND\_RETURN\_RET\_LOG(encoder\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Decoder is null");
            int32\_t ret = OH\_VideoEncoder\_PushInputBuffer(encoder\_, info.bufferIndex);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Push input data failed");
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        
    -   在编码输出处理中，获取已编码的视频数据。
        
        void Transcoding::VideoEncOutputThread() {
            while (true) {
                std::unique\_lock<std::mutex> lock(videoEncContext\_->outputMutex);
                bool condRet = videoEncContext\_->outputCond.wait\_for(
                    lock, 5s, \[this\]() { return !isStarted\_ || !videoEncContext\_->outputBufferInfoQueue.empty(); });
                CHECK\_AND\_BREAK\_LOG(isStarted\_, "Work done, thread out");
                CHECK\_AND\_CONTINUE\_LOG(!videoEncContext\_->outputBufferInfoQueue.empty(),
                                       "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
        
                CodecBufferInfo bufferInfo = videoEncContext\_->outputBufferInfoQueue.front();
                videoEncContext\_->outputBufferInfoQueue.pop();
                CHECK\_AND\_BREAK\_LOG(!(bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS),
                                    "VideoEncOutputThread  Catch EOS, thread out");
                lock.unlock();
                if ((bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME) ||
                    (bufferInfo.attr.flags == AVCODEC\_BUFFER\_FLAGS\_NONE)) {
                    videoEncContext\_->outputFrameCount++;
                    bufferInfo.attr.pts = videoEncContext\_->outputFrameCount \* MICROSECOND / sampleInfo\_.frameRate;
                } else {
                    bufferInfo.attr.pts = 0;
                }
                AVCODEC\_SAMPLE\_LOGW("Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
                                    videoEncContext\_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
                                    bufferInfo.attr.pts);
        
                muxer\_->WriteSample(muxer\_->GetVideoTrackId(), reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer),
                                    bufferInfo.attr);
                int32\_t ret = videoEncoder\_->FreeOutputBuffer(bufferInfo.bufferIndex);
                CHECK\_AND\_BREAK\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, "Encoder output thread out");
            }
            AVCODEC\_SAMPLE\_LOGI("Exit, frame count: %{public}u", videoEncContext\_->outputFrameCount);
            StartRelease();
        }
        
    -   通过OH\_AVMuxer\_WriteSampleBuffer方法，将编码完成的数据写入到视频文件中，从而完成视频转码。
        
        int32\_t Muxer::WriteSample(int32\_t trackId, OH\_AVBuffer \*buffer, OH\_AVCodecBufferAttr &attr){
            std::lock\_guard<std::mutex> lock(writeMutex\_);
        
            CHECK\_AND\_RETURN\_RET\_LOG(muxer\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Muxer is null");
            CHECK\_AND\_RETURN\_RET\_LOG(buffer != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Get a empty buffer");
        
            int32\_t ret = OH\_AVBuffer\_SetBufferAttr(buffer, &attr);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "SetBufferAttr failed");
        
            ret = OH\_AVMuxer\_WriteSampleBuffer(muxer\_, trackId, buffer);
            CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Write sample failed");
            return AVCODEC\_SAMPLE\_ERR\_OK;
        }
        

#### 常见问题

#### \[h2\]通过Buffer模式进行编解码，视频出现花屏或者绿边

可能的原因是在视频编解码的过程中没有考虑YUV跨距的问题，需要注意宽高对齐，处理对应的跨距，关于跨距的原理，请参考[YUV跨距对齐](#section39419315541)。在视频编码时，跨距可以在编码的回调函数EncOnNeedInputBuffer()中进行获取，其中，OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH和OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT分别是视频图片的宽和高，OH\_MD\_KEY\_VIDEO\_STRIDE和OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT分别是字节填充后的宽和高。在视频解码时，跨距可以在解码的回调函数OnNewOutputBuffer()中进行获取，参考代码如下。

void SampleCallback::OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData) {
    if (userData == nullptr) {
        return;
    }
    CodecUserData \*codecUserData = static\_cast<CodecUserData \*>(userData);
    if(codecUserData->isDecFirstFrame) {
        OH\_AVFormat \*format = OH\_VideoDecoder\_GetOutputDescription(codec);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &codecUserData->width);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &codecUserData->height);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_STRIDE, &codecUserData->widthStride);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT, &codecUserData->heightStride);
        OH\_AVFormat\_Destroy(format);
        codecUserData->isDecFirstFrame = false;
    }
    std::unique\_lock<std::mutex> lock(codecUserData->outputMutex);
    codecUserData->outputBufferInfoQueue.emplace(index, buffer);
    codecUserData->outputCond.notify\_all();
}

void SampleCallback::EncOnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData) {
    if (userData == nullptr) {
        return;
    }
    CodecUserData \*codecUserData = static\_cast<CodecUserData \*>(userData);
    if (codecUserData->isEncFirstFrame) {
        OH\_AVFormat \*format = OH\_VideoDecoder\_GetOutputDescription(codec);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &codecUserData->width);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &codecUserData->height);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_STRIDE, &codecUserData->widthStride);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT, &codecUserData->heightStride);
        OH\_AVFormat\_Destroy(format);
        codecUserData->isEncFirstFrame = false;
    }
    std::unique\_lock<std::mutex> lock(codecUserData->inputMutex);
    codecUserData->inputBufferInfoQueue.emplace(index, buffer);
    codecUserData->inputCond.notify\_all();
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/fDSXM8GwT3CPd4KZXhnohA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=69C45B2103165E156A9A37AAD8DE312D603FA800EA3F1D1D0A700355650EA0AE)

在处理跨距时，需要注意size属性的计算与设置，如果size的大小和设置buffer的大小不一致，视频编解码时会出现buffer数据丢失。

#### \[h2\]在视频编解码中，Surface模式和Buffer模式的区别是什么

视频编解码包含两种方式，分别是Surface模式和Buffer模式。在Surface模式下，会通过window对象对接其他模块，如相机、屏幕录制等模块。相对于Surface模式，Buffer模式对于视频数据处理更加灵活，也更为复杂。关于Surface模式和Buffer模式的区别可以参考[Surface输入与Buffer输入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding#surface输入与buffer输入)、[Surface输出与Buffer输出](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-decoding#surface输出与buffer输出)。

#### 示例代码

-   [基于Buffer模式进行视频转码](https://gitcode.com/harmonyos_samples/avcodec-buffer-mode)
