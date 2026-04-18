---
title: "基于Audio能力实现音频耳返"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-in-ear-monitor"
menu_path:
  - "最佳实践"
  - "媒体"
  - "音频和视频"
  - "基于Audio能力实现音频耳返"
captured_at: "2026-04-17T01:54:15.465Z"
---

# 基于Audio能力实现音频耳返

#### 概述

耳返是指通过耳机系统将音频实时传输到耳机中，让使用者能够听到自己的声音、伴奏或其它需要的信息。例如在K歌类应用中，将录制的人声和背景音乐实时送到耳机中，使用户通过反馈即时调整，获得更好的使用体验。

当前系统支持耳返的两种方案如下：

<table><tbody><tr><td class="cellrowborder" valign="top" width="7.520752075207521%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="27.522752275227525%"><p>实现方案</p></td><td class="cellrowborder" valign="top" width="31.503150315031505%"><p>优点</p></td><td class="cellrowborder" valign="top" width="33.45334533453346%"><p>缺点</p></td></tr><tr><td class="cellrowborder" valign="top" width="7.520752075207521%"><p>硬件耳返</p></td><td class="cellrowborder" valign="top" width="27.522752275227525%"><p>基于<a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback" target="_blank">AudioLoopback</a>实现音频耳返</p></td><td class="cellrowborder" valign="top" width="31.503150315031505%"><ol><li>物理耳返，延时低。</li><li>在API21，提供混响和均衡器等音效。</li></ol></td><td class="cellrowborder" valign="top" width="33.45334533453346%"><ol><li>当前仅支持有线耳机，不支持蓝牙耳机。</li><li>在耳返的场景下，仅支持录制麦克风。</li></ol></td></tr><tr><td class="cellrowborder" valign="top" width="7.520752075207521%"><p>软件耳返</p></td><td class="cellrowborder" valign="top" width="27.522752275227525%"><p>基于<a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio" target="_blank">OHAudio</a>实现音频耳返</p></td><td class="cellrowborder" valign="top" width="31.503150315031505%"><ol><li>可以支持有线耳机和蓝牙耳机。</li><li>可以支持耳返（使用者自己的声音或其它需要的信息等）和背景音乐同时录制写入到文件中。</li></ol></td><td class="cellrowborder" valign="top" width="33.45334533453346%"><ol><li>暂无硬件耳返的接口，软件耳返延时比硬件耳返高。</li><li>无音效相关的接口，音效等算法需要自行实现。</li></ol></td></tr></tbody></table>

本文将介绍以下两种实现音频耳返方案：

-   [基于AudioLoopback实现音频耳返](#section1720354614413)
-   [基于OHAudio实现音频耳返](#section144598624518)

#### 基于AudioLoopback实现音频耳返

#### \[h2\]场景描述

点击进入AudioLoopback页面，连接有线耳机，点击录制按钮开启耳返。开启耳返后开发者可通过麦克风在耳机中实时听到自己或周围的声音，同时进行耳返内音频的录制，并且可通过Slider滑块实现耳返音量调节功能。录制完成后进入播放页面，播放录制的音频资源。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/mz9i99eUTl-6Cw5WQcVpsA/zh-cn_image_0000002544829543.gif?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=641646A6B272093287B3AAD06F5B81B569B03C412C558F5B7624773765F88DB5 "点击放大")

#### \[h2\]实现原理

AudioLoopback是HarmonyOS提供的音频返听接口，用于实现低时延耳返功能，支持自动创建低时延渲染器与采集器，采集的音频可直接通过内部路由返回到渲染器，实时传输到耳机。

AudioLoopback的状态变化如下图所示，在创建AudioLoopback实例后，调用对应的方法可以进入指定的状态实现对应行为。同时需要注意的是，在确定的状态执行不合适的方法，可能导致AudioLoopback发生错误，建议开发者在调用状态转换的方法前进行状态检查，避免程序运行产生预期以外的结果，详细开发指导请参考：[实现音频低时延耳返](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-ear-monitor-loopback)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/179pRqqPRCSEe0Pz192oSg/zh-cn_image_0000002513149636.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=ABF24F429E8353E59EDBC0E06AD53A8BF92D8DCAA6B8DFF3191039828C70DB2D "点击放大")

#### \[h2\]开发步骤

使用AudioLoopback控制耳返的开启和关闭，结合[AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder)实现音频的录制，将录制的音频保存在应用沙箱目录，并通过[@ohos.file.fs (文件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)打开录制的音频文件，再通过[AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer)实现已录制音频的播放控制，详细流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/8IT_x_bIT4KkWLuz4x9WBA/zh-cn_image_0000002513309570.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=BEAE4CD0EC89B34EE4D9F1B2A6E557662D37ED0C4ED46DCC747B4D01F81CC318 "点击放大")

具体开发步骤如下：

1.  创建AudioLoopback。
    -   通过[isAudioLoopbackSupported()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#isaudioloopbacksupported20)查询当前系统是否支持音频返听模式。若支持，则调用[audio.createAudioLoopback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-f#audiocreateaudioloopback20)接口创建音频返听器。
        
        private audioLoopback: audio.AudioLoopback | undefined = undefined;
        // ...
        
        // Query capability, create AudioLoopback instance.
        public initAudioLoopback(): void {
          try {
            // Check whether the current system supports hardware in-ear monitor cancellation mode.
            let isSupported = audio.getAudioManager().getStreamManager().isAudioLoopbackSupported(this.mode);
            if (isSupported) {
              audio.createAudioLoopback(this.mode)
                .then((loopback) => {
                  this.audioLoopback = loopback;
                })
                .catch((err: BusinessError) => {
                  logger.error(\`Invoke createAudioLoopback failed, code is ${err.code}, message is ${err.message}.\`);
                });
            }
          } catch (error) {
            let err = error as BusinessError;
            logger.error(\`Failed to use isAudioLoopbackSupported, code=${err.code}, message=${err.message}}\`);
          }
        }
        
    -   通过AudioLoopback的[getStatus()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback#getstatus20)方获取音频返听状态，当返听状态为AVAILABLE\_IDLE时，表示返听可用，此时可调用[enable()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback#enable20)方法传入参数true，开启音频返听。
        
        // Set up a listening event and enable audio feedback.
        public async enable(): Promise<void> {
          // ...
        
          try {
            let status = await this.audioLoopback.getStatus();
            if (status === audio.AudioLoopbackStatus.AVAILABLE\_IDLE) {
              // Enable in-ear monitor.
              await this.audioLoopback.enable(true)
                .then((isSuccess: boolean) => {
                  if (isSuccess) {
                    this.setAudioReverbPreset(audio.AudioLoopbackReverbPreset.ORIGINAL);
                    this.setEqualizerPreset(audio.AudioLoopbackEqualizerPreset.FULL);
                  }
                })
                .catch((err: BusinessError) => {
                  logger.error(\`Audio loopback enable failed. code=${err.code}, message=${err.message}\`);
                })
            } else {
              this.statusChangeCallback(status);
            }
          } catch (err) {
            logger.error(\`code is ${err.code}, message is ${err.message}.\`);
          }
        }
        
    -   当返听状态为AVAILABLE\_RUNNING时，表示返听在运行中，调用[enable()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback#enable20)方法传入参数false，禁用音频返听。
        
        // Disable audio playback, close monitoring event.
        public async disable(): Promise<void> {
          // ...
          try {
            let status = await this.audioLoopback.getStatus();
            if (status === audio.AudioLoopbackStatus.AVAILABLE\_RUNNING) {
              // Disable in-ear monitor.
              await this.audioLoopback.enable(false)
                .then((isSuccess: boolean) => {
                  if (isSuccess) {
                    // Close monitoring.
                    this.audioLoopback?.off('statusChange', this.statusChangeCallback);
                  }
                })
                .catch((err: BusinessError) => {
                  logger.error(\`Audio loopback enable failed. code=${err.code}, message=${err.message}\`);
                })
            } else {
              this.statusChangeCallback(status);
            }
          } catch (err) {
            logger.error(\`Invoke disable failed, code is ${err.code}, message is ${err.message}.\`);
          }
        }
        
    -   调用[setVolume()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback#setvolume20)方法实现音频返听音量的调节。
        
        // Set audio playback volume.
        public async setVolume(volume: number): Promise<void> {
          // ...
          try {
            await this.audioLoopback.setVolume(volume);
            logger.info(\`Invoke setVolume ${volume} succeeded.\`);
          } catch (err) {
            logger.error(\`Invoke setVolume failed, code is ${err.code}, message is ${err.message}.\`);
          }
        }
        
2.  创建AVRecorder。
    -   调用[media.createAVRecorder()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreateavrecorder9)方法，用于创建AVRecorder实例。
        
        private avRecorder: media.AVRecorder | undefined = undefined;
        
        // Create an avRecorder instance.
        public async initAVRecorder() {
          try {
            this.avRecorder = await media.createAVRecorder();
          } catch (err) {
            let error: BusinessError = err as BusinessError;
            logger.error(\`Failed to create avRecorder, error code: ${error.code}, message: ${error.message}\`);
          }
        }
        
    -   调用[prepare()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#prepare9)方法设置音频录制的音频编码比特率、采集声道数、编码格式、采样率和容器格式等信息。
        
        // Configure audio recording parameters.
        public prepareAVRecorder(uiContext: Context) {
          // Audio recording configuration file.
          let avProfile: media.AVRecorderProfile = {
            audioBitrate: 112000, // Audio Bit Rate.
            audioChannels: 2, // Number of audio channels.
            audioCodec: media.CodecMimeType.AUDIO\_AAC, // Audio encoding format.
            audioSampleRate: 48000, // Audio sampling rate.
            fileFormat: media.ContainerFormatType.CFT\_MPEG\_4A // Container format.
          };
        
          const context: Context = uiContext;
          let filePath: string = context.filesDir + '/example.mp3';
          try {
            let audioFile: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
            let fileFd: number = audioFile?.fd as number;
            // Parameter settings for audio recording.
            let avConfig: media.AVRecorderConfig = {
              audioSourceType: media.AudioSourceType.AUDIO\_SOURCE\_TYPE\_MIC, // Audio input source, set as microphone here
              profile: avProfile,
              url: 'fd://' + fileFd
            };
            AppStorage.setOrCreate('fdSrc', fileFd);
            if(!this.avRecorder) {
              return;
            }
            if (this.avRecorder.state === 'idle' || this.avRecorder.state === 'stopped') {
              this.avRecorder.prepare(avConfig, (err: BusinessError) => {
                if (!err) {
                  this.startRecorder();
                }
              });
            }
          } catch (error) {
            let err = error as BusinessError;
            logger.error(\`Failed to open file, error code: ${err.code}, message: ${err.message}\`);
          }
        }
        
    -   调用[start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#start9)方法开始音频录制。
        
        // Start recording.
        public startRecorder() {
          // ...
          this.avRecorder.start((err: BusinessError) => {
            if (!err) {
              logger.info('Succeeded in start avRecorder');
            }
          });
        }
        
    -   调用[pause()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#pause9)方法暂停音频录制。
        
        // Pause recording.
        public pauseRecorder() {
          // ...
          this.avRecorder.pause((err: BusinessError) => {
            if (!err) {
              logger.info('Succeeded in pause avRecorder');
            }
          });
        }
        
    -   调用[resume()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#resume9)方法恢复音频录制。
        
        // Resume recording.
        public resumeRecorder() {
          // ...
          this.avRecorder.resume((err: BusinessError) => {
            if (!err) {
              logger.info('Succeeded in resume avRecorder');
            }
          });
        }
        
    -   调用[stop()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#stop9)方法停止音频录制。
        
        // Stop recording.
        public stopRecorder() {
          // ...
          this.avRecorder.stop((err: BusinessError) => {
            if (!err) {
              logger.info('Succeeded in stop avRecorder');
            }
          });
        }
        
    -   调用[release()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#release9)方法释放音频录制资源。
        
        // Release audio recording resources.
        public releaseRecorder() {
          // ...
          this.avRecorder.release((err: BusinessError) => {
            if (!err) {
              logger.info('Succeeded in release avRecorder');
            }
          });
        }
        
3.  创建AVPlayer。
    -   调用[media.createAVPlayer()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreateavplayer9-1)方法创建AVPlayer实例。
        
        private avPlayer: media.AVPlayer | undefined = undefined;
        
        // Initialize and create an AVPlayer instance.
        async initAVPlayer(fd: number, isPlay: boolean): Promise<void> {
          try {
            this.avPlayer = await media.createAVPlayer();
            await this.setAVPlayerCallback(isPlay);
            this.avPlayer.fdSrc = { fd: fd };
          } catch (error) {
            let err = error as BusinessError;
            logger.error(\`AVPlayer init fail. code=${err.code}, message=${err.message}\`);
          }
        }
        
    -   调用[play()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#play9-1)方法，用于播放录制的音频资源。
        
        // Play audio.
        play(): void {
          // ...
          this.avPlayer.play()
            .catch(() => {
              logger.error('AVPlayerController play error!');
            })
        }
        
    -   调用[pause()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#pause9-1)方法，暂停播放音频。
        
        // Pause playback.
        pause(): void {
          // ...
          this.avPlayer.pause()
            .catch(() => {
              logger.error('AVPlayerController pause error!');
            })
        }
        
    -   调用[release()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#release9-1)方法，释放播放资源。
        
        // Destruction of playback resources.
        release(): void {
          // ...
          this.avPlayer.release()
            .catch(() => {
              logger.error('AVPlayerController release error!');
            });
        }
        
4.  在页面内点击录制按钮后，请求用户授权麦克风权限，通过AudioLoopback开启耳返，同时通过AVRecorder进行耳返音频的录制。
    -   开启耳返并录制音频。
        
        [@ohos.abilityAccessCtrl (程序访问控制管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl)提供了应用程序的权限校验和管理能力，通过[requestPermissionsFromUser()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9)接口拉起弹框，向用户请求授权麦克风权限。
        
        // Pull up the pop-up box and request user authorization.
        atManager.requestPermissionsFromUser(this.getUIContext().getHostContext(), \['ohos.permission.MICROPHONE'\])
          .then((data) => {
            if (data.authResults\[0\] !== 0) {
              return;
            }
            this.capturesStart();
          })
          .catch((err: BusinessError) => {
            logger.error(\`requestPermissionsFromUser fail. err.code=${err.code}, err.message=${err.message}}\`);
          });
        
        调用自定义capturesStart()方法，通过AudioLoopback的enable()开启耳返，并通过prepareAVRecorder()进行耳返音频的录制。
        
        // Start collecting audio.
        capturesStart() {
          try {
            // Enable in-ear monitor.
            if (this.isArkTS) {
              this.audioLoopbackController.enable();
            } else {
              // ...
            }
            this.recorderController.prepareAVRecorder(this.getUIContext().getHostContext()!); // Start recording.
            this.recordSec = 0; // Initialize recording duration.
            this.showTime = '00:00:00'; // Initialize audio capture time.
            this.recordState = CommonConstants.PLAY\_STARTED; // Start recording status.
            clearInterval(this.interval); // Clear timer.
            this.interval = setInterval(async () => {
              // ...
              this.recordSec++;
              this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec); // Audio acquisition time conversion
            }, 1000)
          } catch (error) {
            let err = error as BusinessError;
            logger.error(\`AudioRecording:audioCapturer start err.code = ${err.code}, err.message=${err.message}\`);
          }
        }
        
    -   暂停录制。
        
        定义capturesPause()方法，在其中调用pauseRecorder()暂停音频录制，并调用disable()禁用音频返听。
        
        // Pause audio capture.
        capturesPause() {
          try {
            clearInterval(this.interval);
            this.recordState = CommonConstants.PLAY\_PAUSED;
            this.recorderController.pauseRecorder(); // Pause recording.
            // Disable in-ear monitor.
            if (this.isArkTS) {
              this.audioLoopbackController.disable();
            } else {
              // ...
            }
          } catch (error) {
            let err = error as BusinessError;
            logger.error(\`AudioRecording:audioCapturer stop. err.code=${err.code}, err.message=${err.message}}\`);
          }
        }
        
    -   继续录制。
        
        定义capturesContinue()方法，在其中调用enable()重启音频返听，并通过resumeRecorder()恢复录制。
        
        // Continue to collect.
        capturesContinue() {
          try {
            // ...
            this.recordState = CommonConstants.PLAY\_CONTINUED;
            // Enable in-ear monitor.
            if (this.isArkTS) {
              this.audioLoopbackController.enable();
            } else {
              // ...
            }
            this.recorderController.resumeRecorder(); // Resume recording
            this.interval = setInterval(async () => {
              // ...
              this.recordSec++;
              this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec);
            }, 1000);
          } catch (err) {
            logger.error(\`AudioRecording:audioCapturer start err = ${JSON.stringify(err)}\`);
          }
        }
        
    -   调节耳返音量。
        
        在Slider组件的onChange()事件中，调用audioLoopbackController的setVolume()方法，并传入value值，实现耳返音量的调节。
        
        Slider({
          min: 0,
          max: 1,
          step: 0.1,
          value: this.volumeValue,
        })
          .width('75%')
          .onChange((value: number) => {
            this.volumeValue = value;
            if (this.isArkTS) {
              this.audioLoopbackController.setVolume(value);
            } else {
              // ...
            }
          })
        
    -   停止录制。
        
        定义capturesStop()方法，在其中调用stopRecorder()方法停止录制，并通过disable()禁用音频返听。
        
        // Stop audio collection
        capturesStop() {
          clearInterval(this.interval);
          this.recorderController.stopRecorder(); // Stop recording.
          // Disable in-ear monitor.
          if (this.isArkTS) {
            this.audioLoopbackController.disable();
          } else {
            // ...
          }
        }
        
5.  播放音频。
    -   初始化AVPlayer实例，并传入音频资源句柄。
        
        private avPlayerController: AVPlayerController = new AVPlayerController();
        private fdSrc: number | undefined = 0;
        
        aboutToAppear(): void {
          this.fdSrc = AppStorage.get('fdSrc') as number;
          this.avPlayerController.initAVPlayer(this.fdSrc, false);
        }
        
    -   在点击事件中，调用avPlayerController的play()方法或pause()方法，实现音频资源的播放和暂停。
        
        Column() {
          // ...
        }
        // ...
        .onClick(() => {
          this.isPlay = !this.isPlay;
          if (this.fdSrc) {
            this.isPlay ? this.avPlayerController.play() : this.avPlayerController.pause();
          }
        })
        

#### 基于OHAudio实现音频耳返

#### \[h2\]场景描述

点击进入OHAudio页面，连接有线耳机或蓝牙耳机，点击录制按钮开启耳返。开启耳返后开发者同样可以通过麦克风在耳机中实时听到自己或周围的声音，并进行耳返音频的录制，以及可以通过Slider滑块实现耳返音量的调节。录制完成后进入播放页面，播放录制的音频资源。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/XcfbXFWATBy1r6ewUSO6Sg/zh-cn_image_0000002544789547.gif?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=38514339A9DEEC800506096296203F5A0CC23A9AAF61BE6F1D88B8B362C97B82 "点击放大")

#### \[h2\]实现原理

在C/C++侧实现耳返依赖OHAudio提供的低时延模式进行录制和播放。

1.  通过native\_audiocapturer采集麦克风数据，并将数据写入到音频录制与播放间的数据中转区，即音频的公共缓存中。
2.  读取音频的公共缓存，通过native\_audiorenderer播放音频，实现返听。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/0Q116WRpTqWBvJ-GZ-PrmA/zh-cn_image_0000002544829551.png?HW-CC-KV=V1&HW-CC-Date=20260417T015417Z&HW-CC-Expire=86400&HW-CC-Sign=7D95E15251E4CB727EB38A17231FA2A4166528D2B4BCF52B140BAF777E9729D5 "点击放大")

#### \[h2\]开发步骤

1.  录制音频数据。
    -   调用[OH\_AudioStreamBuilder\_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_create)，并指定[OH\_AudioStream\_Type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_type)音频流类型为AUDIOSTREAM\_TYPE\_CAPTURER，创建输入类型的音频流构造器实例，并设置输入音频流的采样率、声道数、低时延模式、采样格式、编码类型及工作场景等属性。
        
        static napi\_value AudioCapturerInit(napi\_env env, napi\_callback\_info info) {
            if (audioCapturer) {
                OH\_AudioCapturer\_Release(audioCapturer);
                OH\_AudioStreamBuilder\_Destroy(builder);
                audioCapturer = nullptr;
                builder = nullptr;
            }
            codecUserData = new CodecUserData();
        
            // Create builder.
            OH\_AudioStream\_Type type = AUDIOSTREAM\_TYPE\_CAPTURER;
            // Create an audio stream constructor of input type.
            OH\_AudioStreamBuilder\_Create(&builder, type);
            // Set the sampling rate of the audio stream.
            OH\_AudioStreamBuilder\_SetSamplingRate(builder, g\_samplingRate);
            // Set the number of channels for the audio stream.
            OH\_AudioStreamBuilder\_SetChannelCount(builder, g\_channelCount);
            // Set up low-latency audio streaming.
            OH\_AudioStreamBuilder\_SetLatencyMode(builder, AUDIOSTREAM\_LATENCY\_MODE\_FAST);
            // Set the sampling format of the audio stream.
            OH\_AudioStreamBuilder\_SetSampleFormat(builder, AUDIOSTREAM\_SAMPLE\_S16LE);
            // Set the encoding type of the audio stream.
            OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_RAW);
            // Set a working scenario for inputting audio streams.
            OH\_AudioStreamBuilder\_SetCapturerInfo(builder, AUDIOSTREAM\_SOURCE\_TYPE\_MIC);
            // ...
            
            // Create OH\_AudioCapturer.
            OH\_AudioStreamBuilder\_GenerateCapturer(builder, &audioCapturer);
            return nullptr;
        }
        
    -   调用[OH\_AudioCapturer\_Start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_start)启动音频采集器，获取音频数据。
        
        static napi\_value AudioCapturerStart(napi\_env env, napi\_callback\_info info) {
            // start
            OH\_AudioCapturer\_Start(audioCapturer);
            return nullptr;
        }
        
    -   调用[OH\_AudioCapturer\_Pause()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_pause)暂停音频流数据输入。
        
        static napi\_value AudioCapturerPause(napi\_env env, napi\_callback\_info info) {
            OH\_AudioCapturer\_Pause(audioCapturer);
            return nullptr;
        }
        
    -   调用[OH\_AudioCapturer\_Stop()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_stop)停止音频采集器，停止音频流数据输入。
        
        static napi\_value AudioCapturerStop(napi\_env env, napi\_callback\_info info) {
            OH\_AudioCapturer\_Stop(audioCapturer);
            return nullptr;
        }
        
    -   调用[OH\_AudioCapturer\_Release()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_release)释放输入音频流，并通过[OH\_AudioStreamBuilder\_Destroy()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_destroy)销毁输入类型的音频流构造器。
        
        static napi\_value AudioCapturerRelease(napi\_env env, napi\_callback\_info info) {
            if (audioCapturer) {
                OH\_AudioCapturer\_Release(audioCapturer);
                if (builder) {
                    OH\_AudioStreamBuilder\_Destroy(builder);
                }
                audioCapturer = nullptr;
                builder = nullptr;
            }
            // ...
            return nullptr;
        }
        
2.  播放音频数据。
    -   调用[OH\_AudioStreamBuilder\_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_create)，并指定[OH\_AudioStream\_Type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_type)音频流类型为AUDIOSTREAM\_TYPE\_RENDERER，创建输出类型的音频流构造器实例，并设置输出音频流的采样率、声道数、低时延模式、音频播放回调帧长、采样格式、编码类型及工作场景等。
        
        static napi\_value AudioRendererInit(napi\_env env, napi\_callback\_info info) {
            if (audioRenderer) {
                OH\_AudioRenderer\_Release(audioRenderer);
                OH\_AudioStreamBuilder\_Destroy(rendererBuilder);
        
                audioRenderer = nullptr;
                rendererBuilder = nullptr;
            }
        
            // Create an audio stream builder of output type.
            OH\_AudioStream\_Type type = AUDIOSTREAM\_TYPE\_RENDERER;
            OH\_AudioStreamBuilder\_Create(&rendererBuilder, type);
        
            // Set the sampling rate of the audio stream.
            OH\_AudioStreamBuilder\_SetSamplingRate(rendererBuilder, g\_samplingRate);
            // Set the number of channels for the audio stream.
            OH\_AudioStreamBuilder\_SetChannelCount(rendererBuilder, g\_channelCount);
            // Set up low-latency audio streaming.
            OH\_AudioStreamBuilder\_SetLatencyMode(rendererBuilder, AUDIOSTREAM\_LATENCY\_MODE\_FAST);
            OH\_AudioStreamBuilder\_SetFrameSizeInCallback(rendererBuilder, 2500);
            // Set the sampling format of the audio stream.
            OH\_AudioStreamBuilder\_SetSampleFormat(rendererBuilder, AUDIOSTREAM\_SAMPLE\_S16LE);
            // Set the working scenario for outputting audio streams.
            OH\_AudioStreamBuilder\_SetRendererInfo(rendererBuilder, AUDIOSTREAM\_USAGE\_MUSIC);
            OH\_AudioStreamBuilder\_SetRendererWriteDataCallback(rendererBuilder, AudioRendererOnWriteData, codecUserData);
        
            // Create an instance of output audio stream.
            OH\_AudioStreamBuilder\_GenerateRenderer(rendererBuilder, &audioRenderer);
            g\_readEnd = false;
            g\_rendererLowLatency = false;
            return nullptr;
        }
        
    -   调用[OH\_AudioRenderer\_Start()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_start)输出音频数据。
        
        static napi\_value AudioRendererStart(napi\_env env, napi\_callback\_info info) {
            g\_readEnd = false;
            // start
            OH\_AudioRenderer\_Start(audioRenderer);
            return nullptr;
        }
        
    -   调用[OH\_AudioRenderer\_Pause()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_pause)暂停输出音频数据。
        
        static napi\_value AudioRendererPause(napi\_env env, napi\_callback\_info info) {
            g\_readEnd = false;
            OH\_AudioRenderer\_Pause(audioRenderer);
            return nullptr;
        }
        
    -   调用[OH\_AudioRenderer\_SetVolume()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_setvolume)设置音频流音量值。
        
        static napi\_value AudioRendererSetVolume(napi\_env env, napi\_callback\_info info) {
            size\_t argc = 1;
            napi\_value args\[1\] = {nullptr};
            napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
            double volume = 1;
            napi\_get\_value\_double(env, args\[0\], &volume);
            OH\_AudioRenderer\_SetVolume(audioRenderer, volume);
            return nullptr;
        }
        
    -   调用[OH\_AudioRenderer\_Stop()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_stop)停止输出音频流。
        
        static napi\_value AudioRendererStop(napi\_env env, napi\_callback\_info info) {
            g\_readEnd = false;
            OH\_AudioRenderer\_Stop(audioRenderer);
            return nullptr;
        }
        
    -   调用[OH\_AudioRenderer\_Release()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_release)释放输出音频流资源，并通过OH\_AudioStreamBuilder\_Destroy()销毁输出类型的音频流构造器。
        
        static napi\_value AudioRendererRelease(napi\_env env, napi\_callback\_info info) {
            if (audioRenderer) {
                OH\_AudioRenderer\_Release(audioRenderer);
                OH\_AudioStreamBuilder\_Destroy(rendererBuilder);
                audioRenderer = nullptr;
                rendererBuilder = nullptr;
            }
            return nullptr;
        }
        
3.  在页面内点击录制按钮后，通过C/C++侧定义的方法实现耳返的开启或关闭，并通过AVRecorder进行耳返音频的录制。
    -   开启耳返并录制音频。
        
        调用audioCapturesStart()方法获取音频数据，并调用audioRendererStart()方法将音频数据通过耳机进行输出实现返听，以及通过prepareAVRecorder()方法进行耳返音频的录制。
        
        // Start collecting audio.
        capturesStart() {
          try {
            // Enable in-ear monitor.
            if (this.isArkTS) {
              // ...
            } else {
              nativeRecord.audioCapturesStart();
              nativeRecord.audioRendererStart();
            }
            this.recorderController.prepareAVRecorder(this.getUIContext().getHostContext()!); // Start recording.
            this.recordSec = 0; // Initialize recording duration.
            this.showTime = '00:00:00'; // Initialize audio capture time.
            this.recordState = CommonConstants.PLAY\_STARTED; // Start recording status.
            clearInterval(this.interval); // Clear timer.
            this.interval = setInterval(async () => {
              // ...
              this.recordSec++;
              this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec); // Audio acquisition time conversion
            }, 1000)
          } catch (error) {
            let err = error as BusinessError;
            logger.error(\`AudioRecording:audioCapturer start err.code = ${err.code}, err.message=${err.message}\`);
          }
        }
        
    -   暂停录制。
        
        调用pauseRecorder()方法暂停音频录制，并通过audioCapturesPause()方法及audioRendererPause()方法暂停音频数据的输入和输出，关闭音频返听。
        
        // Pause audio capture.
        capturesPause() {
          try {
            clearInterval(this.interval);
            this.recordState = CommonConstants.PLAY\_PAUSED;
            this.recorderController.pauseRecorder(); // Pause recording.
            // Disable in-ear monitor.
            if (this.isArkTS) {
              // ...
            } else {
              nativeRecord.audioCapturesPause();
              nativeRecord.audioRendererPause();
            }
          } catch (error) {
            let err = error as BusinessError;
            logger.error(\`AudioRecording:audioCapturer stop. err.code=${err.code}, err.message=${err.message}}\`);
          }
        }
        
    -   继续录制。
        
        调用audioCapturesStart()方法和audioRendererStart()方法获取并输出音频数据，开启返听，并通过resumeRecorder()恢复录制。
        
        // Continue to collect.
        capturesContinue() {
          try {
            // ...
            this.recordState = CommonConstants.PLAY\_CONTINUED;
            // Enable in-ear monitor.
            if (this.isArkTS) {
              // ...
            } else {
              nativeRecord.audioCapturesStart();
              nativeRecord.audioRendererStart();
            }
            this.recorderController.resumeRecorder(); // Resume recording
            this.interval = setInterval(async () => {
              // ...
              this.recordSec++;
              this.showTime = FormatTimeTools.getTimesBySecond(this.recordSec);
            }, 1000);
          } catch (err) {
            logger.error(\`AudioRecording:audioCapturer start err = ${JSON.stringify(err)}\`);
          }
        }
        
    -   调节返听音量。
        
        在Slider组件的onChange()事件中，调用audioRendererSetVolume()方法，并传入value值，设置返听音量。
        
        Slider({
          min: 0,
          max: 1,
          step: 0.1,
          value: this.volumeValue,
        })
          .width('75%')
          .onChange((value: number) => {
            this.volumeValue = value;
            if (this.isArkTS) {
              // ...
            } else {
              nativeRecord.audioRendererSetVolume(value);
            }
          })
        
    -   停止录制。
        
        调用stopRecorder()方法停止录制，并通过audioCapturesStop()方法和audioRendererStop()方法实现音频流数据的输入和输出，关闭耳返。
        
        // Stop audio collection
        capturesStop() {
          clearInterval(this.interval);
          this.recorderController.stopRecorder(); // Stop recording.
          // Disable in-ear monitor.
          if (this.isArkTS) {
            // ...
          } else {
            nativeRecord.audioCapturesStop();
            nativeRecord.audioRendererStop();
          }
        }
        
4.  音频播放，请参考基于AudioLoopback实现音频耳返场景中[播放音频](#li11370953124216)小节。

#### 示例代码

-   [实现音频耳返](https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor)
