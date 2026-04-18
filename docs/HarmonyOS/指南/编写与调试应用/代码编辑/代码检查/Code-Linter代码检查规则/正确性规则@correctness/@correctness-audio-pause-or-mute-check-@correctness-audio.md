---
title: "@correctness/audio"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-audio-pause-or-mute-check"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "正确性规则@correctness"
  - "@correctness/audio-pause-or-mute-check"
captured_at: "2026-04-17T01:36:48.317Z"
---

# @correctness/audio-pause-or-mute-check

建议应用在播放声音的场景下，监听音频发声设备变化。

改善[音视频播放](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-change#音频流输出设备变更原因)体验场景下，建议优先修改。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@correctness/audio-pause-or-mute-check": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
export class AudioPauseNoReport {
  demoCallBack() {
    let audioStreamInfo1: audio.AudioStreamInfo = {
      samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_44100,
      channels: audio.AudioChannel.CHANNEL\_1,
      sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE,
      encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW
    };
    let audioRendererInfo: audio.AudioRendererInfo = {
      usage: audio.StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION,
      rendererFlags: 0
    };
    let audioRendererOptions: audio.AudioRendererOptions = {
      streamInfo: audioStreamInfo1,
      rendererInfo: audioRendererInfo
    };
    media.createAVPlayer((error: BusinessError, player) => {
      if (player) {
        player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
          console.info('Succeeded');
        });
        player.on('audioOutputDeviceChangeWithInfo', ()=>{
          console.error(\`createAVPlayer audioOutputDeviceChangeWithInfo\`);
        });
        console.info('Succeeded in creating AVPlayer.');
      } else {
        console.error(\`Failed to create AVPlayer, error message:${error.message}\`);
      }
    });
    audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
      if (err) {
        console.error(\`AudioRenderer Created: Error: ${err}\`);
      } else {
        audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
          console.info('Succeeded');
        });
        audioRenderer.on('outputDeviceChangeWithInfo', ()=>{
          console.error(\`createAudioRenderer outputDeviceChangeWithInfo\`);
        })
        console.info('AudioRenderer Created: Success: SUCCESS');
      }
    });
  }
}

#### 反例

import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
let audioStreamInfo1: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_44100,
  channels: audio.AudioChannel.CHANNEL\_1,
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION,
  rendererFlags: 0
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo1,
  rendererInfo: audioRendererInfo
};
function demoCallBack() {
  // warning line
  media.createAVPlayer((error: BusinessError, player: media.AVPlayer) => {
    if (player != null) {
      player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
        console.info('Succeeded');
      });
      console.info('Succeeded in creating AVPlayer.');
    } else {
      console.error(\`Failed to create AVPlayer, error message:${error.message}\`);
    }
  });
  // warning line
  audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
    if (err) {
      console.error(\`AudioRenderer Created: Error: ${err}\`);
    } else {
      audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
        console.info('Succeeded');
      });
      console.info('AudioRenderer Created.');
    }
  });
}

#### 规则集

plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
