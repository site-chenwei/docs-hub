---
title: "@performance/reasonable"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-audio-use-check"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "性能规则@performance"
  - "@performance/reasonable-audio-use-check"
captured_at: "2026-04-17T01:36:47.500Z"
---

# @performance/reasonable-audio-use-check

无长时任务的应用退到后台时，禁止使用麦克风或扬声器。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@performance/reasonable-audio-use-check": "suggestion",
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import { UIAbility } from '@kit.AbilityKit';
import { audio } from '@kit.AudioKit';
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL\_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // 编码格式。
};
const audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: {
    usage: audio.StreamUsage.STREAM\_USAGE\_UNKNOWN,
    rendererFlags: 1
  }
}
let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};
let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};
let audioRenderer: audio.AudioRenderer
let avPlayer: media.AVPlayer
let audioCapturer: audio.AudioCapturer;

export default class EntryAbility extends UIAbility {
  // Create an AudioRenderer based on the service requirements at the foreground
  onForeground(): void {
    audio.createAudioRenderer(audioRendererOptions, ((err, data) => {
      audioRenderer = data;
    }));
    avPlayer.play();
    audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
      audioCapturer = data;
    });
  }

  onBackground(): void {
    // Return to the background to stop or pause
    audioRenderer.stop((err: BusinessError) => {
    });
    avPlayer.stop();
    audioCapturer.stop((err: BusinessError) => {
    });
  }
}

#### 反例

import { UIAbility } from '@kit.AbilityKit';
import { audio } from '@kit.AudioKit';
import { media } from '@kit.MediaKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL\_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // 编码格式。
};
const audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: {
    usage: audio.StreamUsage.STREAM\_USAGE\_UNKNOWN,
    rendererFlags: 1
  }
}
let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};
let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};
let audioRenderer: audio.AudioRenderer
let avPlayer: media.AVPlayer
let audioCapturer: audio.AudioCapturer;

export default class EntryAbility extends UIAbility {
  // Create an AudioRenderer based on the service requirements at the foreground
  onForeground(): void {
    audio.createAudioRenderer(audioRendererOptions, ((err, data) => {
      audioRenderer = data;
    }));
    avPlayer.play();
    audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
      audioCapturer = data;
    });
  }

  onBackground(): void {
  }
}

#### 规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
