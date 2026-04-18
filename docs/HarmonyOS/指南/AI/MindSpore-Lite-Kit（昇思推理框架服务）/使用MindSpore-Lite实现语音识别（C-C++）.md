---
title: "使用MindSpore Lite实现语音识别（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-asr-based-native"
menu_path:
  - "指南"
  - "AI"
  - "MindSpore Lite Kit（昇思推理框架服务）"
  - "使用MindSpore Lite实现语音识别（C/C++）"
captured_at: "2026-04-17T01:36:39.808Z"
---

# 使用MindSpore Lite实现语音识别（C/C++）

#### 场景说明

开发者可以使用[MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)，在UI代码中集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现语音识别的应用。

语音识别可以将一段音频信息转换为文本，在智能语音助手、语音输入、语音搜索等领域有广泛的应用。

#### 环境配置

若需要使用模拟器运行该示例，请参考：[使用模拟器运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)

#### 基本概念

-   N-API：用于构建ArkTS本地化组件的一套接口。可利用N-API，将C/C++开发的库封装成ArkTS模块。

#### 开发流程

1.  选择语音识别模型。
2.  在端侧使用MindSpore Lite推理模型，实现对语音文件的语音识别。

#### 开发步骤

本文以对语音识别模型进行推理为例，提供使用MindSpore Lite实现语音识别应用的开发指导。

#### \[h2\]选择模型

本示例程序中使用的语音识别模型文件为tiny-encoder.ms、tiny-decoder-main.ms、tiny-decoder-loop.ms，放置在entry/src/main/resources/rawfile工程目录下。

#### \[h2\]编写播放音频代码

调用[@ohos.multimedia.media](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media)、[@ohos.multimedia.audio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio)，实现播放音频的功能。

// player.ets
import { media } from '@kit.MediaKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit';
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'MindSporeLite';

export default class AVPlayerDemo {
  private isSeek: boolean = false; // 用于区分模式是否支持seek操作。
  // 注册avplayer回调函数。
  setAVPlayerCallback(avPlayer: media.AVPlayer) {
    // seek操作结果回调函数。
    avPlayer.on('seekDone', (seekDoneTime: number) => {
      hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: AVPlayer seek succeeded, seek time is ${seekDoneTime}\`);
    });
    // error回调监听函数，当avPlayer在操作过程中出现错误时调用reset接口触发重置流程。
    avPlayer.on('error', (err: BusinessError) => {
      hilog.error(0xFF00, TAG, '%{public}s',
        \`MS\_LITE\_ERR: Invoke avPlayer failed, code is ${err.code}, message is ${err.message}\`);
      avPlayer.reset(); // 调用reset重置资源，触发idle状态。
    });
    // 状态机变化回调函数。
    avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
      switch (state) {
        case 'idle': // 成功调用reset接口后触发该状态机上报。
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state idle called.');
          avPlayer.release(); // 调用release接口销毁实例对象。
          break;
        case 'initialized': // avplayer 设置播放源后触发该状态上报。
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state initialized called.');
          avPlayer.audioRendererInfo = {
            usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // 音频流使用类型：音乐。根据业务场景配置。
            rendererFlags: 0 // 音频渲染器标志。
          };
          avPlayer.prepare();
          break;
        case 'prepared': // prepare调用成功后上报该状态机。
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state prepared called.');
          avPlayer.play(); // 调用播放接口开始播放。
          break;
        case 'playing': // play成功调用后触发该状态机上报。
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state playing called.');
          if (this.isSeek) {
            hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer start to seek.');
            avPlayer.seek(0); // 将播放位置移动到音频的开始。
          } else {
            // 当播放模式不支持seek操作时继续播放到结尾。
            hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer wait to play end.');
          }
          break;
        case 'paused': // pause成功调用后触发该状态机上报。
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state paused called.');
          setTimeout(() => {
            hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer paused wait to play again');
            avPlayer.play(); // 暂停3s后再次调用播放接口开始播放。
          }, 3000);
          break;
        case 'completed': // 播放结束后触发该状态机上报。
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state completed called.');
          avPlayer.stop(); // 调用播放结束接口。
          break;
        case 'stopped': // stop接口成功调用后触发该状态机上报。
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state stopped called.');
          avPlayer.reset(); // 调用reset接口初始化avplayer状态。
          break;
        case 'released':
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state released called.');
          break;
        default:
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state unknown called.');
          break;
      }
    });
  }

  // 使用资源管理接口获取音频文件并通过fdSrc属性进行播放。
  async avPlayerFdSrcDemo() {
    // 创建avPlayer实例对象。
    let avPlayer: media.AVPlayer = await media.createAVPlayer();
    // 创建状态机变化回调函数。
    this.setAVPlayerCallback(avPlayer);
    // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
    // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度。
    let context = new UIContext().getHostContext() as common.UIAbilityContext;
    let fileDescriptor = await context.resourceManager.getRawFd('zh.wav');
    let avFileDescriptor: media.AVFileDescriptor =
      { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };
    this.isSeek = true; // 支持seek操作。
    // 为fdSrc赋值触发initialized状态机上报。
    avPlayer.fdSrc = avFileDescriptor;
  }
}

#### \[h2\]编写识别音频代码

在 entry/src/main/cpp/mslite\_napi.cpp，调用[MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)，依次对3个模型进行推理，推理代码流程如下。

1.  引用对应的头文件。说明：需要用户下载三方库，其中librosa来源是[LibrosaCpp](https://github.com/ewan-xu/LibrosaCpp)，libsamplerate来源是[libsamplerate](https://github.com/libsndfile/libsamplerate)，下载后置于entry/src/main/cpp/third\_party目录下。AudioFile.h的来源是[AudioFile](https://github.com/adamstark/AudioFile/blob/1.1.2/AudioFile.h)，base64.h、base64.cpp的来源是[whisper.axera](https://github.com/ml-inory/whisper.axera/tree/main/cpp/src)下载后置于entry/src/main/cpp/src目录下。
    
    #include "AudioFile.h"
    #include "base64.h"
    #include "napi/native\_api.h"
    #include "utils.h"
    #include <algorithm>
    #include <cstdlib>
    #include <fstream>
    #include <hilog/log.h>
    #include <iostream>
    #include <librosa/librosa.h>
    #include <mindspore/context.h>
    #include <mindspore/model.h>
    #include <mindspore/status.h>
    #include <mindspore/tensor.h>
    #include <mindspore/types.h>
    #include <numeric> 
    #include <rawfile/raw\_file\_manager.h>
    #include <sstream>
    #include <vector>
    
2.  读取音频文件、模型文件等，转换为buffer数据。
    
    #define LOGI(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGD(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_DEBUG, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGW(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_WARN, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGE(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    
    using BinBuffer = std::pair<void \*, size\_t>;
    
    BinBuffer ReadBinFile(NativeResourceManager \*nativeResourceManager, const std::string &modelName)
    {
        auto rawFile = OH\_ResourceManager\_OpenRawFile(nativeResourceManager, modelName.c\_str());
        if (rawFile == nullptr) {
            LOGE("MS\_LITE\_ERR: Open model file failed");
            return BinBuffer(nullptr, 0);
        }
        long fileSize = OH\_ResourceManager\_GetRawFileSize(rawFile);
        if (fileSize <= 0) {
            LOGE("MS\_LITE\_ERR: FileSize not correct");
            return BinBuffer(nullptr, 0);
        }
        void \*buffer = malloc(fileSize);
        if (buffer == nullptr) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            return BinBuffer(nullptr, 0);
        }
        int ret = OH\_ResourceManager\_ReadRawFile(rawFile, buffer, fileSize);
        if (ret == 0) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return BinBuffer(nullptr, 0);
        }
        OH\_ResourceManager\_CloseRawFile(rawFile);
        return BinBuffer(buffer, fileSize);
    }
    
    BinBuffer ReadTokens(NativeResourceManager \*nativeResourceManager, const std::string &modelName)
    {
        auto rawFile = OH\_ResourceManager\_OpenRawFile(nativeResourceManager, modelName.c\_str());
        if (rawFile == nullptr) {
            LOGE("MS\_LITE\_ERR: Open model file failed");
            return BinBuffer(nullptr, 0);
        }
        long fileSize = OH\_ResourceManager\_GetRawFileSize(rawFile);
        if (fileSize <= 0) {
            LOGE("MS\_LITE\_ERR: FileSize not correct");
            return BinBuffer(nullptr, 0);
        }
        void \*buffer = malloc(fileSize);
        if (buffer == nullptr) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            return BinBuffer(nullptr, 0);
        }
        int ret = OH\_ResourceManager\_ReadRawFile(rawFile, buffer, fileSize);
        if (ret == 0) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return BinBuffer(nullptr, 0);
        }
        OH\_ResourceManager\_CloseRawFile(rawFile);
        BinBuffer res(buffer, fileSize);
        return res;
    }
    
3.  创建上下文，设置设备类型，并加载模型。
    
    void DestroyModelBuffer(void \*\*buffer)
    {
        if (buffer == nullptr) {
            return;
        }
        free(\*buffer);
        \*buffer = nullptr;
    }
    
    OH\_AI\_ModelHandle CreateMSLiteModel(BinBuffer &bin)
    {
        // 创建并配置上下文
        auto context = OH\_AI\_ContextCreate();
        if (context == nullptr) {
            DestroyModelBuffer(&bin.first);
            LOGE("MS\_LITE\_ERR: Create MSLite context failed.\\n");
            return nullptr;
        }
        auto cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
        OH\_AI\_DeviceInfoSetEnableFP16(cpu\_device\_info, false);
        OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);
    
        // 创建模型
        auto model = OH\_AI\_ModelCreate();
        if (model == nullptr) {
            DestroyModelBuffer(&bin.first);
            LOGE("MS\_LITE\_ERR: Allocate MSLite Model failed.\\n");
            return nullptr;
        }
    
        // 加载与编译模型，模型的类型为OH\_AI\_MODELTYPE\_MINDIR
        auto build\_ret = OH\_AI\_ModelBuild(model, bin.first, bin.second, OH\_AI\_MODELTYPE\_MINDIR, context);
        DestroyModelBuffer(&bin.first);
        if (build\_ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&model);
            LOGE("MS\_LITE\_ERR: Build MSLite model failed.\\n");
            return nullptr;
        }
        LOGI("MS\_LITE\_LOG: Build MSLite model success.\\n");
        return model;
    }
    
4.  设置模型输入数据，执行模型推理。
    
    constexpr int K\_NUM\_PRINT\_OF\_OUT\_DATA = 20;
    
    int FillInputTensor(OH\_AI\_TensorHandle input, const BinBuffer &bin)
    {
        if (OH\_AI\_TensorGetDataSize(input) != bin.second) {
            return OH\_AI\_STATUS\_LITE\_INPUT\_PARAM\_INVALID;
        }
        char \*data = (char \*)OH\_AI\_TensorGetMutableData(input);
        memcpy(data, (const char \*)bin.first, OH\_AI\_TensorGetDataSize(input));
        return OH\_AI\_STATUS\_SUCCESS;
    }
    
    // 执行模型推理
    int RunMSLiteModel(OH\_AI\_ModelHandle model, std::vector<BinBuffer> inputBins)
    {
        // 设置模型的输入数据
        auto inputs = OH\_AI\_ModelGetInputs(model);
        for(int i = 0; i < inputBins.size(); i++)
        {
            auto ret = FillInputTensor(inputs.handle\_list\[i\], inputBins\[i\]);
            if (ret != OH\_AI\_STATUS\_SUCCESS) {
                LOGE("MS\_LITE\_ERR: set input %{public}d error.\\n", i);
                return OH\_AI\_STATUS\_LITE\_ERROR;
            }
        }
    
        // 获取模型的输出张量
        auto outputs = OH\_AI\_ModelGetOutputs(model);
    
        // 模型推理
        auto predict\_ret = OH\_AI\_ModelPredict(model, inputs, &outputs, nullptr, nullptr);
        if (predict\_ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&model);
            LOGE("MS\_LITE\_ERR: MSLite Predict error.\\n");
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
        LOGD("MS\_LITE\_LOG: Run MSLite model Predict success.\\n");
    
        // 打印输出数据
        LOGD("MS\_LITE\_LOG: Get model outputs:\\n");
        for (size\_t i = 0; i < outputs.handle\_num; i++) {
            auto tensor = outputs.handle\_list\[i\];
            LOGD("MS\_LITE\_LOG: - Tensor %{public}d name is: %{public}s.\\n", static\_cast<int>(i),
                 OH\_AI\_TensorGetName(tensor));
            LOGD("MS\_LITE\_LOG: - Tensor %{public}d size is: %{public}d.\\n", static\_cast<int>(i),
                 (int)OH\_AI\_TensorGetDataSize(tensor));
            LOGD("MS\_LITE\_LOG: - Tensor data is:\\n");
            auto out\_data = reinterpret\_cast<const float \*>(OH\_AI\_TensorGetData(tensor));
            std::stringstream outStr;
            for (int i = 0; (i < OH\_AI\_TensorGetElementNum(tensor)) && (i <= K\_NUM\_PRINT\_OF\_OUT\_DATA); i++) {
                outStr << out\_data\[i\] << " ";
            }
            LOGD("MS\_LITE\_LOG: %{public}s", outStr.str().c\_str());
        }
        return OH\_AI\_STATUS\_SUCCESS;
    }
    
5.  调用以上方法，实现3个模型的推理流程。
    
    const float NEG\_INF = -std::numeric\_limits<float>::infinity();
    const int WHISPER\_SOT = 50258;
    const int WHISPER\_TRANSCRIBE = 50359;
    const int WHISPER\_TRANSLATE = 50358;
    const int WHISPER\_NO\_TIMESTAMPS = 50363;
    const int WHISPER\_EOT = 50257;
    const int WHISPER\_BLANK = 220;
    const int WHISPER\_NO\_SPEECH = 50362;
    const int WHISPER\_N\_TEXT\_CTX = 448;
    const int WHISPER\_N\_TEXT\_STATE = 384;
    constexpr int WHISPER\_SAMPLE\_RATE = 16000;
    
    BinBuffer GetMSOutput(OH\_AI\_TensorHandle output)
    {
        float \*outputData = reinterpret\_cast<float \*>(OH\_AI\_TensorGetMutableData(output));
        size\_t size = OH\_AI\_TensorGetDataSize(output);
        return {outputData, size};
    }
    
    void SuppressTokens(BinBuffer &logits, bool isInitial)
    {
        auto logits\_data = static\_cast<float \*>(logits.first);
        if (isInitial) {
            logits\_data\[WHISPER\_EOT\] = NEG\_INF;
            logits\_data\[WHISPER\_BLANK\] = NEG\_INF;
        }
    
        // 其他令牌的抑制
        logits\_data\[WHISPER\_NO\_TIMESTAMPS\] = NEG\_INF;
        logits\_data\[WHISPER\_SOT\] = NEG\_INF;
        logits\_data\[WHISPER\_NO\_SPEECH\] = NEG\_INF;
        logits\_data\[WHISPER\_TRANSLATE\] = NEG\_INF;
    }
    
    std::vector<int> LoopPredict(const OH\_AI\_ModelHandle model, const BinBuffer &n\_layer\_cross\_k,
                                 const BinBuffer &n\_layer\_cross\_v, const BinBuffer &logits\_init,
                                 BinBuffer &out\_n\_layer\_self\_k\_cache, BinBuffer &out\_n\_layer\_self\_v\_cache,
                                 const BinBuffer &data\_embedding, const int loop, const int offset\_init)
    {
        BinBuffer logits{nullptr, 51865 \* sizeof(float)};
        logits.first = malloc(logits.second);
        if (!logits.first) {
            LOGE("MS\_LITE\_ERR: Fail to malloc!\\n");
            return {};
        }
        void \*logits\_init\_src = static\_cast<char \*>(logits\_init.first) + 51865 \* 3 \* sizeof(float);
        memcpy(logits.first, logits\_init\_src, logits.second);
        SuppressTokens(logits, true);
    
        std::vector<int> output\_token;
        float \*logits\_data = static\_cast<float \*>(logits.first);
        int max\_token\_id = 0;
        float max\_token = logits\_data\[0\];
        for (int i = 0; i < logits.second / sizeof(float); i++) {
            if (logits\_data\[i\] > max\_token) {
                max\_token\_id = i;
                max\_token = logits\_data\[i\];
            }
        }
    
        int offset = offset\_init;
        BinBuffer slice{nullptr, 0};
        slice.second = WHISPER\_N\_TEXT\_STATE \* sizeof(float);
        slice.first = malloc(slice.second);
        if (!slice.first) {
            LOGE("MS\_LITE\_ERR: Fail to malloc!\\n");
            return {};
        }
    
        auto out\_n\_layer\_self\_k\_cache\_new = out\_n\_layer\_self\_k\_cache;
        auto out\_n\_layer\_self\_v\_cache\_new = out\_n\_layer\_self\_v\_cache;
    
        for (size\_t i = 0; i < loop; i++) {
            if (max\_token\_id == WHISPER\_EOT) {
                break;
            }
            output\_token.push\_back(max\_token\_id);
            std::vector<float> mask(WHISPER\_N\_TEXT\_CTX, 0.0f);
            for (size\_t i = 0; i < WHISPER\_N\_TEXT\_CTX - offset - 1; ++i) {
                mask\[i\] = NEG\_INF;
            }
            BinBuffer tokens{&max\_token\_id, sizeof(int)};
    
            void \*data\_embedding\_src =
                static\_cast<char \*>(data\_embedding.first) + offset \* WHISPER\_N\_TEXT\_STATE \* sizeof(float);
            memcpy(slice.first, data\_embedding\_src, slice.second);
            BinBuffer mask\_bin(mask.data(), mask.size() \* sizeof(float));
            int ret = RunMSLiteModel(model, {tokens, out\_n\_layer\_self\_k\_cache\_new, out\_n\_layer\_self\_v\_cache\_new,
                                             n\_layer\_cross\_k, n\_layer\_cross\_v, slice, mask\_bin});
    
            auto outputs = OH\_AI\_ModelGetOutputs(model);
            logits = GetMSOutput(outputs.handle\_list\[0\]);
            out\_n\_layer\_self\_k\_cache\_new = GetMSOutput(outputs.handle\_list\[1\]);
            out\_n\_layer\_self\_v\_cache\_new = GetMSOutput(outputs.handle\_list\[2\]);
            offset++;
            SuppressTokens(logits, false);
            logits\_data = static\_cast<float \*>(logits.first);
            max\_token = logits\_data\[0\];
    
            for (int j = 0; j < logits.second / sizeof(float); j++) {
                if (logits\_data\[j\] > max\_token) {
                    max\_token\_id = j;
                    max\_token = logits\_data\[j\];
                }
            }
            LOGI("MS\_LITE\_LOG: run decoder loop %{public}d ok!\\n token = %{public}d", i, max\_token\_id);
        }
        return output\_token;
    }
    
    std::vector<std::string> ProcessDataLines(const BinBuffer token\_txt)
    {
        void \*data\_ptr = token\_txt.first;
        size\_t data\_size = token\_txt.second;
        std::vector<std::string> tokens;
    
        const char \*char\_data = static\_cast<const char \*>(data\_ptr);
        std::stringstream ss(std::string(char\_data, char\_data + data\_size));
        std::string line;
        while (std::getline(ss, line)) {
            size\_t space\_pos = line.find(' ');
            tokens.push\_back(line.substr(0, space\_pos));
        }
        return tokens;
    }
    
    static napi\_value RunDemo(napi\_env env, napi\_callback\_info info)
    {
        // 执行样例推理
        napi\_value error\_ret;
        napi\_create\_int32(env, -1, &error\_ret);
        size\_t argc = 1;
        napi\_value argv\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
        auto resourcesManager = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
    
        // 数据预处理
        AudioFile<float> audioFile;
        std::string filePath = "zh.wav";
        auto audioBin = ReadBinFile(resourcesManager, filePath);
        if (audioBin.first == nullptr) {
            LOGE("MS\_LITE\_ERR: Fail to read  %{public}s!", filePath.c\_str());
            return error\_ret;
        }
        size\_t dataSize = audioBin.second;
        uint8\_t \*dataBuffer = (uint8\_t \*)audioBin.first;
        bool ok = audioFile.loadFromMemory(std::vector<uint8\_t>(dataBuffer, dataBuffer + dataSize));
        if (!ok) {
            LOGE("MS\_LITE\_ERR: Fail to read  %{public}s!", filePath.c\_str());
            return error\_ret;
        }
        std::vector<float> data(audioFile.samples\[0\]);
        ResampleAudio(data, audioFile.getSampleRate(), WHISPER\_SAMPLE\_RATE, 1, SRC\_SINC\_BEST\_QUALITY);
        std::vector<float> audio(data);
    
        int padding = 480000;
        int sr = 16000;
        int n\_fft = 480;
        int n\_hop = 160;
        int n\_mel = 80;
        int fmin = 0; // 最小频率，默认值为0.0 Hz
        int fmax =
            sr /
            2.0; // 最大频率，默认值为采样率（sr/2.0）的一半
        audio.insert(audio.end(), padding, 0.0f);
        std::vector<std::vector<float>> mels\_T =
            librosa::Feature::melspectrogram(audio, sr, n\_fft, n\_hop, "hann", true, "reflect", 2.f, n\_mel, fmin, fmax);
        std::cout << "mels: " << std::endl;
    
        std::vector<std::vector<float>> mels = TransposeMel(mels\_T);
        ProcessMelSpectrogram(mels);
    
        std::vector<float> inputMels(mels.size() \* mels\[0\].size(), 0);
        for (int i = 0; i < mels.size(); i++) {
            std::copy(mels\[i\].begin(), mels\[i\].end(), inputMels.begin() + i \* mels\[0\].size());
        }
    
        BinBuffer inputMelsBin(inputMels.data(), inputMels.size() \* sizeof(float));
    
        // tiny-encoder.ms模型推理
        auto encoderBin = ReadBinFile(resourcesManager, "tiny-encoder.ms");
        if (encoderBin.first == nullptr) {
            free(dataBuffer);
            dataBuffer = nullptr;
            return error\_ret;
        }
    
        auto encoder = CreateMSLiteModel(encoderBin);
    
        int ret = RunMSLiteModel(encoder, {inputMelsBin});
        if (ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&encoder);
            return error\_ret;
        }
        LOGI("MS\_LITE\_LOG: run encoder ok!\\n");
    
        auto outputs = OH\_AI\_ModelGetOutputs(encoder);
        auto n\_layer\_cross\_k = GetMSOutput(outputs.handle\_list\[0\]);
        auto n\_layer\_cross\_v = GetMSOutput(outputs.handle\_list\[1\]);
    
        // tiny-decoder-main.ms模型推理
        std::vector<int> SOT\_SEQUENCE = {WHISPER\_SOT,
                                         WHISPER\_SOT + 1 + 1,
                                         WHISPER\_TRANSCRIBE, WHISPER\_NO\_TIMESTAMPS};
        BinBuffer sotSequence(SOT\_SEQUENCE.data(), SOT\_SEQUENCE.size() \* sizeof(int));
    
        const std::string decoder\_main\_path = "tiny-decoder-main.ms";
        auto decoderMainBin = ReadBinFile(resourcesManager, decoder\_main\_path);
        if (decoderMainBin.first == nullptr) {
            OH\_AI\_ModelDestroy(&encoder);
            return error\_ret;
        }
        auto decoder\_main = CreateMSLiteModel(decoderMainBin);
        int ret2 = RunMSLiteModel(decoder\_main, {sotSequence, n\_layer\_cross\_k, n\_layer\_cross\_v});
    
        if (ret2 != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&decoder\_main);
            return error\_ret;
        }
        LOGI("MS\_LITE\_LOG: run decoder\_main ok!\\n");
    
        auto decoderMainOut = OH\_AI\_ModelGetOutputs(decoder\_main);
        auto logitsBin = GetMSOutput(decoderMainOut.handle\_list\[0\]);
        auto out\_n\_layer\_self\_k\_cache\_Bin = GetMSOutput(decoderMainOut.handle\_list\[1\]);
        auto out\_n\_layer\_self\_v\_cache\_Bin = GetMSOutput(decoderMainOut.handle\_list\[2\]);
    
        // tiny-decoder-loop.ms模型推理
        const std::string modelName3 = "tiny-decoder-loop.ms";
        auto modelBuffer3 = ReadBinFile(resourcesManager, modelName3);
        auto decoder\_loop = CreateMSLiteModel(modelBuffer3);
    
        const std::string dataName\_embedding = "tiny-positional\_embedding.bin"; // 获取输入数据
        auto data\_embedding = ReadBinFile(resourcesManager, dataName\_embedding);
        if (data\_embedding.first == nullptr) {
            OH\_AI\_ModelDestroy(&encoder);
            OH\_AI\_ModelDestroy(&decoder\_main);
            OH\_AI\_ModelDestroy(&decoder\_loop);
            return error\_ret;
        }
    
        int loop\_times = WHISPER\_N\_TEXT\_CTX - SOT\_SEQUENCE.size();
        int offset\_init = SOT\_SEQUENCE.size();
        auto output\_tokens =
            LoopPredict(decoder\_loop, n\_layer\_cross\_k, n\_layer\_cross\_v, logitsBin, out\_n\_layer\_self\_k\_cache\_Bin,
                        out\_n\_layer\_self\_v\_cache\_Bin, data\_embedding, loop\_times, offset\_init);
    
        std::vector<std::string> token\_tables = ProcessDataLines(ReadTokens(resourcesManager, "tiny-tokens.txt"));
        std::string result;
        for (const auto i : output\_tokens) {
            char str\[1024\];
            base64\_decode((const uint8 \*)token\_tables\[i\].c\_str(), (uint32)token\_tables\[i\].size(), str);
            result += str;
        }
        LOGI("MS\_LITE\_LOG: result is -> %{public}s", result.c\_str());
    
        OH\_AI\_ModelDestroy(&encoder);
        OH\_AI\_ModelDestroy(&decoder\_main);
        OH\_AI\_ModelDestroy(&decoder\_loop);
    
        napi\_value out\_data;
        napi\_create\_string\_utf8(env, result.c\_str(), result.length(), &out\_data);
        return out\_data;
    }
    
6.  编写CMake脚本，链接MindSpore Lite动态库。
    
    ```
    # the minimum version of CMake.
    cmake_minimum_required(VERSION 3.5.0)
    project(test)
    # AudioFile.h
    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
    set(NATIVERENDER_PATH ${CMAKE_CURRENT_SOURCE_DIR})
    
    if(DEFINED PACKAGE_FIND_FILE)
        include(${PACKAGE_FIND_FILE})
    endif()
    
    include_directories(${NATIVERENDER_PATH}
                        ${NATIVERENDER_PATH}/include)
    
    # libsamplerate
    set(LIBSAMPLERATE_DIR ${NATIVERENDER_PATH}/third_party/libsamplerate)
    include_directories(${LIBSAMPLERATE_DIR}/include)
    add_subdirectory(${LIBSAMPLERATE_DIR})
    
    include_directories(${NATIVERENDER_PATH}/third_party/opencc/include/opencc)
    # src
    aux_source_directory(src SRC_DIR)
    include_directories(${NATIVERENDER_PATH}/src)
    
    include_directories(${CMAKE_SOURCE_DIR}/third_party)
    
    file(GLOB SRC src/*.cc)
    
    add_library(entry SHARED mslite_napi.cpp ${SRC})
    target_link_libraries(entry PUBLIC samplerate)
    target_link_libraries(entry PUBLIC mindspore_lite_ndk)
    target_link_libraries(entry PUBLIC hilog_ndk.z)
    target_link_libraries(entry PUBLIC rawfile.z)
    target_link_libraries(entry PUBLIC ace_napi.z)
    ```
    

#### \[h2\]使用N-API将C++动态库封装成ArkTS模块

1.  在 entry/src/main/cpp/types/libentry/Index.d.ts，定义ArkTS接口runDemo() 。内容如下：
    
    export const runDemo: (a: Object) => string;
    
2.  在 oh-package.json5 文件，将API与so相关联，成为一个完整的ArkTS模块：
    
    ```json
    {
      "name": "libentry.so",
      "types": "./Index.d.ts",
      "version": "1.0.0",
      "description": "MindSpore Lite inference module."
    }
    ```
    

#### \[h2\]调用封装的ArkTS模块进行推理并输出结果

在 entry/src/main/ets/pages/Index.ets 中，调用封装的ArkTS模块，最后对推理结果进行处理。若提示@nutpi/chinese\_transverter不存在，请参考[中文简繁体转换器三方库](https://developer.huawei.com/consumer/cn/forum/topic/0202169478029484501?fid=0109140870620153026)安装@nutpi/chinese\_transverter组件。

// Index.ets
import msliteNapi from 'libentry.so'
import AVPlayerDemo from './player';
import { transverter, TransverterType, TransverterLanguage } from "@nutpi/chinese\_transverter"
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'MindSporeLite';

@Entry
@Component
struct Index {
  @State message: string = 'MSLite Whisper Demo';
  @State wavName: string = 'zh.wav';
  @State content: string = '';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold);
        Button() {
          Text('播放示例音频')
            .fontSize(20)
            .fontWeight(FontWeight.Medium)
        }
        .type(ButtonType.Capsule)
        .margin({
          top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
        .onClick(async () =>{
          // 通过实例调用类中的函数
          hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: begin to play wav.\`);
          let myClass = new AVPlayerDemo();
          myClass.avPlayerFdSrcDemo();
        })
        Button() {
          Text('识别示例音频')
            .fontSize(20)
            .fontWeight(FontWeight.Medium)
        }
        .type(ButtonType.Capsule)
        .margin({
          top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
        .onClick(() => {
          let resMgr = this.getUIContext()?.getHostContext()?.getApplicationContext().resourceManager;
          if (resMgr === undefined || resMgr === null) {
            hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: get resourceManager failed.\`);
            return
          }
          // 调用封装的runDemo函数
          hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: \*\*\* Start MSLite Demo \*\*\*\`);
          let output = msliteNapi.runDemo(resMgr);
          if (output === null || output.length === 0) {
            hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: runDemo failed.\`);
            return
          }
          hilog.info(0xFF00, TAG, '%{public}s',
            \`MS\_LITE\_LOG: output length = ${output.length}; value = ${output.slice(0, 20)}\`);
          this.content = output;
          hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: \*\*\* Finished MSLite Demo \*\*\*\`);
        })

        // 显示识别内容
        if (this.content) {
          Text('识别内容: \\n' + transverter({
            type: TransverterType.SIMPLIFIED,
            str: this.content,
            language: TransverterLanguage.ZH\_CN
          }) + '\\n').focusable(true).fontSize(20).height('20%')
        }
      }.width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]调测验证

1.  在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：
    
    ```shell
    Launching com.samples.mindsporelitecdemoasr
    $ hdc shell aa force-stop com.samples.mindsporelitecdemoasr
    $ hdc shell mkdir data/local/tmp/xxx
    $ hdc file send E:\xxx\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx"
    $ hdc shell bm install -p data/local/tmp/xxx
    $ hdc shell rm -rf data/local/tmp/xxx
    $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemoasr
    com.samples.mindsporelitecdemoasr successfully launched...
    ```
    
2.  在设备屏幕点击播放示例音频按钮，会播放本示例音频文件。点击识别示例音频按钮，设备屏幕显示本示例音频文件的中文内容。在日志打印结果中，过滤关键字”MS\_LITE\_LOG“，可得到如下结果：
    
    ```verilog
    05-16 14:53:44.200   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: begin to play wav.
    05-16 14:53:44.210   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     [a92ab1e0f831191, 0, 0] MS_LITE_LOG: AVPlayer state initialized called.
    05-16 14:53:44.228   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     [a92ab1e0f831191, 0, 0] MS_LITE_LOG: AVPlayer state prepared called.
    05-16 14:53:44.242   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state playing called.
    05-16 14:53:44.242   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer start to seek.
    05-16 14:53:44.372   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer seek succeeded, seek time is 0
    05-16 14:53:49.621   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state completed called.
    05-16 14:53:49.646   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state stopped called.
    05-16 14:53:49.647   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state idle called.
    05-16 14:53:49.649   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state released called.
    05-16 14:53:53.282   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: *** Start MSLite Demo ***
    05-16 14:53:53.926   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  I     MS_LITE_LOG: Build MSLite model success.
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: Run MSLite model Predict success.
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: Get model outputs:
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 0 name is: n_layer_cross_k.
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 0 size is: 9216000.
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor data is:
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: -1.14678 -2.30223 0.868679 0.284441 1.03233 -2.02062 0.688163 -0.732034 -1.10553 1.43459 0.083885 -0.116173 -0.772636 1.5466 -0.631993 -0.897929 -0.0501685 -1.62517 0.375988 -1.77772 -0.432178
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 1 name is: n_layer_cross_v.
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 1 size is: 9216000.
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor data is:
    05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: 0.0876085 -0.560317 -0.652518 -0.116969 -0.182608 -9.40531e-05 0.186293 0.123206 0.0127445 0.0708352 -0.489624 -0.226322 -0.0686949 -0.0341293 -0.0719619 0.103588 0.398025 -0.444261 0.396124 -0.347295 0.00541205
    05-16 14:53:54.430   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  I     MS_LITE_LOG: Build MSLite model success.
    05-16 14:53:54.462   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: Run MSLite model Predict success.
    ......
    05-16 14:53:55.272   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  I     MS_LITE_LOG: run decoder loop 16 ok!
                                                                                                    token = 50257
    05-16 14:53:55.334   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: *** Finished MSLite Demo ***
    ```
    

#### \[h2\]效果示意

在设备上，点击**播放示例音频**按钮，会播放本示例音频文件。点击**识别示例音频**按钮，设备屏幕显示本示例音频文件的中文内容。

| 初始页面 | 点击识别示例音频按钮后 |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/d3eMzWR7S6a_rqldqsA3kA/zh-cn_image_0000002538020294.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=0DF6D82E2665390C85FFA8676C260C1B5CD5C007EC10D47B9E62EBE655EAA1F5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/L2EDl-VASaSYF4B_JXs9JQ/zh-cn_image_0000002538180220.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=347441A53881E2D4F2891B85AEED4B9539BCDC4B194B033BA17ED2A7783BD139) |

#### 示例代码

-   [基于MindSporeLite接口实现语音识别（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MindSporeLiteKit/MindSporeLiteCDemoASR)
