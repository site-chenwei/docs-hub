---
title: "基于Surface模式进行视频编码"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-surface-encoder"
menu_path:
  - "最佳实践"
  - "媒体"
  - "音频和视频"
  - "基于Surface模式进行视频编码"
captured_at: "2026-04-17T01:54:15.198Z"
---

# 基于Surface模式进行视频编码

#### 概述

视频编码是指通过压缩技术，将原始视频数据转换成压缩数据的过程。HarmonyOS提供了媒体文件的解析和封装、音视频的编解码。基于[Surface模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding#surface模式)进行视频编码指通过NativeWindow来传递编码的输入数据，使用AVCodec提供的视频编码能力实现视频编码的过程。开发者可以通过OHNativeWindow与其他模块进行对接，如相机模块、屏幕录制模块等。

#### 实现原理

#### \[h2\]Surface轮转原理

在Surface模式下，视频编码依赖NativeWindow传递编码数据。其中，NativeWindow是本地平台化窗口，表示图形队列的生产者端，包含了Surface对象。

Surface主要是用于管理、传递图形和媒体的共享内存，具体场景如图形的生产、消费、合成，媒体的播放、录制等。Surface通过共享内存的方式传递图形/媒体数据，避免了进程之间图形/媒体数据的拷贝，减少了进程之间数据传递的开销。

Surface分为生产者ProducerSurface和消费者ConsumerSurface。NativeWindow依赖生产者ProducerSurface，所以表示图形队列的生产者端。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/G1WJsF70TtKX5DdnrT8kzA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=A8D5F9B951885B6E31499B9AE4B81F9FA0C75E71CB59F77AAD4882B3E5518166)

相对于Buffer模式，Surface模式避免了进程之间的媒体数据拷贝，所以Surface模式的性能会更高。

Surface轮转流程如下所示，生产者先申请到一块Buffer，填充数据后将Buffer返回给BufferQueue。在触发回调函数后，通知消费者Buffer已经被生产者填充好数据。之后，消费者可以获取填充好数据的Buffer，直到不再需要该Buffer后，释放对应的Buffer。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/XHZP7B6RQHSV9w4q_Ix3aw/zh-cn_image_0000002493276208.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=B849D9178E77A74E8DD6F620545D8F1DDEC7C9AE491EFE74B82FE313414CAD75 "点击放大")

视频编码器提供了获取NativeWindow的接口，通过NativeWindow可以将相机产生的数据与视频编码器进行对接。视频编码器作为消费者，将Buffer数据进行消费编码，从而实现视频编码的操作。下面我们将通过相机录制和屏幕录制，介绍基于Surface模式进行视频编码。

#### 使用AVScreenCapture+AVCodec进行视频编码

#### \[h2\]场景描述

系统中提供了AVScreenCapture用于屏幕录制，AVScreenCapture可以支持屏幕录制并直接保存到视频文件中，还可以将录制的数据通过NativeWindow对接编码器进行数据编码。在基于Surface实现屏幕录制的方案中，开发者可以根据自己的需求保存对应的格式。

#### \[h2\]实现原理

Surface模式是通过NativeWindow包含的Surface传递录屏数据进行视频编码。在使用AVScreenCapture实现屏幕录制的场景中，开发者需要提前在编码器中获取NativeWindow对象，然后将获取的NativeWindow设置到AVScreenCapture中实现屏幕录制。具体开发步骤如下所示。

1.  初始化视频封装器，创建并配置视频封装器。
2.  初始化视频编码器，创建并配置视频编码器，并从编码器中获取NativeWindow对象。
3.  初始化AVScreenCapture，创建并配置AVScreenCapture。
4.  启动视频封装器。
5.  启动视频编码器。
6.  创建并启动编码输出子线程。
7.  将从编码器中获取的NativeWindow对象设置给AVScreenCapture，启动屏幕录制。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/u-2w3L_qSX-Oor28AsY8XA/zh-cn_image_0000002465431712.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=80FFDFD726007AC84A2B19024E16D3E43EFBF40EC22489522BDE63F0CB58CEB2 "点击放大")

#### \[h2\]开发步骤

1.  初始化视频封装器，创建并配置视频封装器。
    
    int32\_t Muxer::Create(int32\_t fd) {
        muxer\_ = OH\_AVMuxer\_Create(fd, AV\_OUTPUT\_FORMAT\_MPEG\_4);
        if (muxer\_ == nullptr) {
            return -1;
        }
        return 0;
    }
    
    int32\_t Muxer::Config(SampleInfo &sampleInfo) {
        OH\_AVFormat \*formatAudio = OH\_AVFormat\_CreateAudioFormat(sampleInfo.audioCodecMime.data(),
                                                                 sampleInfo.audioSampleRate, sampleInfo.audioChannelCount);
    
        OH\_AVFormat\_SetIntValue(formatAudio, OH\_MD\_KEY\_PROFILE, AAC\_PROFILE\_LC);
    
        int32\_t ret = OH\_AVMuxer\_AddTrack(muxer\_, &audioTrackId\_, formatAudio);
        OH\_AVFormat\_Destroy(formatAudio);
    
        OH\_AVFormat \*formatVideo =
            OH\_AVFormat\_CreateVideoFormat(sampleInfo.videoCodecMime.data(), sampleInfo.videoWidth, sampleInfo.videoHeight);
    
        OH\_AVFormat\_SetDoubleValue(formatVideo, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.frameRate);
        OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
        OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
        OH\_AVFormat\_SetStringValue(formatVideo, OH\_MD\_KEY\_CODEC\_MIME, sampleInfo.videoCodecMime.data());
    
        ret = OH\_AVMuxer\_AddTrack(muxer\_, &videoTrackId\_, formatVideo);
        if (ret != AV\_ERR\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "AddTrack failed");
        }
        OH\_AVFormat\_Destroy(formatVideo);
        formatVideo = nullptr;
        return ret;
    }
    
2.  初始化视频编码器，创建并配置视频编码器，并从编码器中获取NativeWindow对象。
    
    int32\_t VideoEncoder::Create(const std::string &videoCodecMime) {
        encoder\_ = OH\_VideoEncoder\_CreateByMime(videoCodecMime.c\_str());
        if (encoder\_ == nullptr) {
            return -1;
        }
        return 0;
    }
    
    int32\_t VideoEncoder::Config(SampleInfo &sampleInfo, CodecUserData \*codecUserData) {
        // Configure video encoder
        OH\_AVFormat \*format = OH\_AVFormat\_Create();
    
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
        OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.frameRate);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, sampleInfo.pixelFormat);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE, sampleInfo.bitrateMode);
        OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, sampleInfo.bitrate);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PROFILE, sampleInfo.hevcProfile);
    
        int ret = OH\_VideoEncoder\_Configure(encoder\_, format);
        if (ret != AV\_ERR\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Config failed, ret: %{public}d", ret);
        }
        OH\_AVFormat\_Destroy(format);
        format = nullptr;
    
        // GetSurface from video encoder
        OH\_VideoEncoder\_GetSurface(encoder\_, &sampleInfo.window);
    
        // SetCallback for video encoder
        OH\_VideoEncoder\_RegisterCallback(encoder\_,
                                         {VideoEncoder::OnCodecError, VideoEncoder::OnCodecFormatChange,
                                          VideoEncoder::OnNeedInputBuffer, VideoEncoder::OnNewOutputBuffer},
                                         codecUserData);
        // Prepare video encoder
        OH\_VideoEncoder\_Prepare(encoder\_);
    
        return 0;
    }
    
3.  初始化AVScreenCapture，创建并配置AVScreenCapture。
    
    void CAVScreenCaptureToStream::InitAVScreenCapture(int32\_t videoWidth,
                                                     int32\_t videoHeight) {
        if (g\_avCapture != nullptr) {
            StopScreenCaptureRecording(g\_avCapture);
        }
    
        g\_avCapture = OH\_AVScreenCapture\_Create();
        if (g\_avCapture == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "create screen capture failed");
        }
        OH\_LOG\_INFO(LOG\_APP, "ScreenCapture after create sc");
    
        // Set callback
        OH\_AVScreenCapture\_SetErrorCallback(g\_avCapture, OnErrorToStream, nullptr);
        OH\_AVScreenCapture\_SetStateCallback(g\_avCapture, OnSurfaceStateChangeToStream, nullptr);
    
        OH\_AVScreenCapture\_SetMicrophoneEnabled(g\_avCapture, true);
        OH\_AVScreenCapture\_SetCanvasRotation(g\_avCapture, true);
    
        // Initialize configuration information
        OH\_AVScreenCaptureConfig config;
        OH\_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH\_SOURCE\_DEFAULT};
        OH\_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH\_ALL\_PLAYBACK};
        OH\_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH\_AudioCodecFormat::OH\_AAC\_LC};
        OH\_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};
    
        OH\_VideoCaptureInfo videoCapInfo = {
            .videoFrameWidth = videoWidth, .videoFrameHeight = videoHeight, .videoSource = OH\_VIDEO\_SOURCE\_SURFACE\_RGBA};
    
        OH\_VideoEncInfo videoEncInfo = {
            .videoCodec = OH\_VideoCodecFormat::OH\_H264, .videoBitrate = 10000000, .videoFrameRate = 30};
    
        OH\_VideoInfo videoInfo = {.videoCapInfo = videoCapInfo, .videoEncInfo = videoEncInfo};
    
        config = {
            .captureMode = OH\_CAPTURE\_HOME\_SCREEN,
            .dataType = OH\_ORIGINAL\_STREAM,
            .audioInfo = audioInfo,
            .videoInfo = videoInfo,
        };
    
        int result = OH\_AVScreenCapture\_Init(g\_avCapture, config);
        if (result != AV\_SCREEN\_CAPTURE\_ERR\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "ScreenCapture OH\_AVScreenCapture\_Init failed %{public}d", result);
        }
        OH\_LOG\_INFO(LOG\_APP, "ScreenCapture OH\_AVScreenCapture\_Init %{public}d", result);
    }
    
4.  启动视频封装器。
    
    int32\_t Muxer::Start() {
        int ret = OH\_AVMuxer\_Start(muxer\_);
        return ret;
    }
    
5.  启动视频编码器。
    
    int32\_t VideoEncoder::Start() {
        int ret = OH\_VideoEncoder\_Start(encoder\_);
        return ret;
    }
    
6.  创建并启动编码输出子线程。
    
    void CAVScreenCaptureToStream::EncOutputThread() {
        while (true) {
            if (!isStarted\_) {
                OH\_LOG\_ERROR(LOG\_APP, "Work done, thread out");
                break;
            }
            std::unique\_lock<std::mutex> lock(videoEncContext\_->outputMutex);
            bool condRet = videoEncContext\_->outputCond.wait\_for(
                lock, 5s, \[this\]() { return !isStarted\_ || !videoEncContext\_->outputBufferInfoQueue.empty(); });
            if (!isStarted\_) {
                OH\_LOG\_ERROR(LOG\_APP, "Work done, thread out");
                break;
            }
            if (videoEncContext\_->outputBufferInfoQueue.empty()) {
                OH\_LOG\_ERROR(LOG\_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
                continue;
            }
    
            CodecBufferInfo bufferInfo = videoEncContext\_->outputBufferInfoQueue.front();
            videoEncContext\_->outputBufferInfoQueue.pop();
    
            if (bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                OH\_LOG\_ERROR(LOG\_APP, "Catch EOS, thread out");
                break;
            }
            lock.unlock();
            if ((bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME) ||
                (bufferInfo.attr.flags == AVCODEC\_BUFFER\_FLAGS\_NONE)) {
                videoEncContext\_->outputFrameCount++;
                // if first Frame, last frame info not init, Set pts directly to 0
                if (lastFrameTimestampPts\_ == 0) {
                    lastFrameTimestampPts\_ = bufferInfo.attr.pts;
                    bufferInfo.attr.pts = 0;
                } else {
                    // calc cur frame pts and last pts diff, get cur frame encode pts
                    lastFrameEncodePts\_ += (bufferInfo.attr.pts - lastFrameTimestampPts\_) / 1000;
                    // record last frame pts info
                    lastFrameTimestampPts\_ = bufferInfo.attr.pts;
                    // set cur frame encode pts.
                    bufferInfo.attr.pts = lastFrameEncodePts\_;
                }
            } else {
                bufferInfo.attr.pts = 0;
            }
    
            muxer\_->WriteSample(muxer\_->GetVideoTrackId(), reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer),
                                bufferInfo.attr);
            int32\_t ret = videoEncoder\_->FreeOutputBuffer(bufferInfo.bufferIndex);
    
            if (ret) {
                OH\_LOG\_ERROR(LOG\_APP, "Encoder output thread out");
                break;
            }
        }
        StartRelease();
        OH\_LOG\_INFO(LOG\_APP, "Exit, frame count: %{public}u", videoEncContext\_->outputFrameCount);
    }
    
7.  将从编码器中获取的NativeWindow对象设置给AVScreenCapture，启动屏幕录制。
    
    void CAVScreenCaptureToStream::StartScreenCapture(int32\_t outputFd, int32\_t videoWidth, int32\_t videoHeight) {
        InitMuxerAndEncoder(outputFd, videoWidth, videoHeight);
    
        InitAVScreenCapture(videoWidth, videoHeight);
        
        m\_IsRunning = true;
    
        StartMuxerAndEncoder();
    
        int result = OH\_AVScreenCapture\_StartScreenCaptureWithSurface(g\_avCapture, sampleInfo\_.window);
        OH\_LOG\_INFO(LOG\_APP, "OH\_VideoEncoder\_Start Started 2 %{public}d", result);
        if (result != AV\_SCREEN\_CAPTURE\_ERR\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "ScreenCapture Started failed %{public}d", result);
            OH\_AVScreenCapture\_Release(g\_avCapture);
        }
    }
    

#### 使用Camera+AVCodec进行视频编码

#### \[h2\]场景描述

在相机录制的场景中，可以Camera相机对接AVRecorder实现录制，还可以通过Surface将相机与视频编码器进行对接，从而实现视频录制。在基于Surface实现相机录制的场景中，开发者可以自行配置对应的格式，如录制HDR视频。

#### \[h2\]实现原理

在使用Camera实现相机录制中，需要通过NativeWindow传递相机数据。开发者需要提前从视频编码器中获取NativeWindow，并从NativeWindow中获取对应的surfaceId。最后，在相机配置时，通过surfaceId创建相机输出流。具体开发步骤如下所示。

1.  初始化视频封装器，创建并配置视频封装器。
2.  初始化视频编码器，创建并配置视频编码器，从编码器中获取NativeWindow对象。从NativeWindow对象获取对应的surfaceId。
3.  初始化相机配置，并通过createVideoOutput接口创建相机输出流。
4.  在开启相机时，启动视频封装器。
5.  启动视频编码器。
6.  创建并启动编码输出子线程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QJfWe3ZcSqCbkqLFEFFixw/zh-cn_image_0000002498550729.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=FC4F13E31682B79B6BB7DCAE1590201A770FCE426C22668AC327BA5556FF65DD "点击放大")

#### \[h2\]开发步骤

1.  初始化视频封装器，创建并配置视频封装器。（此代码与屏幕录制一致）
2.  初始化视频编码器，创建并配置视频编码器，从编码器中获取NativeWindow对象。
    
    int32\_t VideoEncoder::GetSurface(SampleInfo &sampleInfo) {
        int32\_t ret = OH\_VideoEncoder\_GetSurface(encoder\_, &sampleInfo.window);
        CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK && sampleInfo.window, AVCODEC\_SAMPLE\_ERR\_ERROR,
                                 "Get surface failed, ret: %{public}d", ret);
        return AVCODEC\_SAMPLE\_ERR\_OK;
    }
    
    从NativeWindow对象获取对应的surfaceId。
    
    void NativeInit(napi\_env env, void \*data) {
        AsyncCallbackInfo \*asyncCallbackInfo = static\_cast<AsyncCallbackInfo \*>(data);
        int32\_t ret = Recorder::GetInstance().Init(asyncCallbackInfo->sampleInfo);
        if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
            SetCallBackResult(asyncCallbackInfo, -1);
        }
    
        uint64\_t id = 0;
        ret = OH\_NativeWindow\_GetSurfaceId(asyncCallbackInfo->sampleInfo.window, &id);
        if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
            SetCallBackResult(asyncCallbackInfo, -1);
        }
        asyncCallbackInfo->surfaceId = std::to\_string(id);
        SurfaceIdCallBack(asyncCallbackInfo, asyncCallbackInfo->surfaceId);
    }
    
3.  初始化相机配置，并通过createVideoOutput接口创建相机输出流。
    
    // Add the encoder video stream to the session.
    try {
      videoSession.addOutput(encoderVideoOutput);
    } catch (error) {
      let err = error as BusinessError;
      Logger.error(TAG, \`Failed to add encoderVideoOutput. error: ${JSON.stringify(err)}\`);
    }
    
    点击相机录制时，启动相机输出流。
    
    // Start the video output stream
    encoderVideoOutput.start((err: BusinessError) => {
      if (err) {
        Logger.error(TAG, \`Failed to start the encoder video output. error: ${JSON.stringify(err)}\`);
        return;
      }
      Logger.info(TAG, 'Callback invoked to indicate the encoder video output start success.');
    });
    
4.  在开启相机时，启动视频封装器。
    
    int32\_t Muxer::Start() {
        CHECK\_AND\_RETURN\_RET\_LOG(muxer\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Muxer is null");
    
        int ret = OH\_AVMuxer\_Start(muxer\_);
        CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Start failed, ret: %{public}d", ret);
        return AVCODEC\_SAMPLE\_ERR\_OK;
    }
    
5.  启动视频编码器。
    
    // Start Encoder
    int32\_t VideoEncoder::Start() {
        CHECK\_AND\_RETURN\_RET\_LOG(encoder\_ != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "Encoder is null");
    
        int ret = OH\_VideoEncoder\_Start(encoder\_);
        CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Start failed, ret: %{public}d", ret);
        return AVCODEC\_SAMPLE\_ERR\_OK;
    }
    
6.  创建并启动编码输出子线程。
    
    void Recorder::EncOutputThread() {
        while (true) {
            CHECK\_AND\_BREAK\_LOG(isStarted\_, "Work done, thread out");
            std::unique\_lock<std::mutex> lock(encContext\_->outputMutex);
            bool condRet = encContext\_->outputCond.wait\_for(
                lock, 5s, \[this\]() { return !isStarted\_ || !encContext\_->outputBufferInfoQueue.empty(); });
            CHECK\_AND\_BREAK\_LOG(isStarted\_, "Work done, thread out");
            CHECK\_AND\_CONTINUE\_LOG(!encContext\_->outputBufferInfoQueue.empty(),
                                   "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
    
            CodecBufferInfo bufferInfo = encContext\_->outputBufferInfoQueue.front();
            encContext\_->outputBufferInfoQueue.pop();
            CHECK\_AND\_BREAK\_LOG(!(bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS), "Catch EOS, thread out");
            lock.unlock();
            if ((bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME) ||
                (bufferInfo.attr.flags == AVCODEC\_BUFFER\_FLAGS\_NONE)) {
                encContext\_->outputFrameCount++;
                bufferInfo.attr.pts = encContext\_->outputFrameCount \* MICROSECOND / sampleInfo\_.frameRate;
            } else {
                bufferInfo.attr.pts = 0;
            }
            AVCODEC\_SAMPLE\_LOGW("Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
                                encContext\_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
                                bufferInfo.attr.pts);
    
            muxer\_->WriteSample(muxer\_->GetVideoTrackId(), reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer),
                                bufferInfo.attr);
            int32\_t ret = videoEncoder\_->FreeOutputBuffer(bufferInfo.bufferIndex);
            CHECK\_AND\_BREAK\_LOG(ret == AVCODEC\_SAMPLE\_ERR\_OK, "Encoder output thread out");
        }
        AVCODEC\_SAMPLE\_LOGI("Exit, frame count: %{public}u", encContext\_->outputFrameCount);
        StartRelease();
    }
    

#### 示例代码

-   使用AVScreenCapture+AVCodec进行视频编码参考代码：[基于AVScreenCapture实现录屏功能](https://gitcode.com/harmonyos_samples/avscreen-capture-screen-record)
-   使用Camera+AVCodec进行视频编码参考代码：[基于AVCodec能力的视频编解码](https://gitcode.com/harmonyos_samples/AVCodecVideo)
