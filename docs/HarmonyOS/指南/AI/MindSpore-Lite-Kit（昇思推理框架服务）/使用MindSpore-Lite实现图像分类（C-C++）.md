---
title: "使用MindSpore Lite实现图像分类（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-guidelines-based-native"
menu_path:
  - "指南"
  - "AI"
  - "MindSpore Lite Kit（昇思推理框架服务）"
  - "使用MindSpore Lite实现图像分类（C/C++）"
captured_at: "2026-04-17T01:36:39.783Z"
---

# 使用MindSpore Lite实现图像分类（C/C++）

#### 场景说明

开发者可以使用[MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)，在UI代码中直接集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现图像分类的应用。

图像分类可实现对图像中物体的识别，在医学影像分析、自动驾驶、电子商务、人脸识别等领域有广泛的应用。

#### 基本概念

-   N-API：用于构建ArkTS本地化组件的一套接口。可利用N-API，将C/C++开发的库封装成ArkTS模块。

#### 开发流程

1.  选择图像分类模型。
2.  在端侧使用MindSpore Lite推理模型，实现对选择的图片进行分类。

#### 开发步骤

本文以对相册的一张图片进行推理为例，提供使用MindSpore Lite实现图像分类的开发指导。

#### \[h2\]选择模型

本示例程序中使用的图像分类模型文件为[mobilenetv2.ms](https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/1.5/mobilenetv2.ms)，放置在entry/src/main/resources/rawfile工程目录下。

如果开发者有其他图像分类的预训练模型，请参考[MindSpore Lite 模型转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-converter-guidelines)介绍，将原始模型转换成.ms格式。

#### \[h2\]编写推理代码

在 entry/src/main/cpp/mslite\_napi.cpp，调用[MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)实现端侧推理，推理代码流程如下。

1.  引用对应的头文件
    
    #include <iostream>
    #include <sstream>
    #include <cstdlib>
    #include <hilog/log.h>
    #include <rawfile/raw\_file\_manager.h>
    #include <mindspore/types.h>
    #include <mindspore/model.h>
    #include <mindspore/context.h>
    #include <mindspore/status.h>
    #include <mindspore/tensor.h>
    #include "napi/native\_api.h"
    
2.  读取模型文件
    
    #define LOGI(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGD(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_DEBUG, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGW(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_WARN, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGE(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    
    void \*ReadModelFile(NativeResourceManager \*nativeResourceManager, const std::string &modelName, size\_t \*modelSize)
    {
        auto rawFile = OH\_ResourceManager\_OpenRawFile(nativeResourceManager, modelName.c\_str());
        if (rawFile == nullptr) {
            LOGE("MS\_LITE\_ERR: Open model file failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return nullptr;
        }
        long fileSize = OH\_ResourceManager\_GetRawFileSize(rawFile);
        if (fileSize <= 0) {
            LOGE("MS\_LITE\_ERR: FileSize not correct");
        }
        void \*modelBuffer = malloc(fileSize);
        if (modelBuffer == nullptr) {
            LOGE("MS\_LITE\_ERR: malloc failed");
        }
        int ret = OH\_ResourceManager\_ReadRawFile(rawFile, modelBuffer, fileSize);
        if (ret == 0) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return nullptr;
        }
        OH\_ResourceManager\_CloseRawFile(rawFile);
        \*modelSize = fileSize;
        return modelBuffer;
    }
    
3.  创建上下文，设置线程数、设备类型等参数，并加载模型。本样例模型，不支持使用NNRt推理。
    
    void DestroyModelBuffer(void \*\*buffer)
    {
        if (buffer == nullptr) {
            return;
        }
        free(\*buffer);
        \*buffer = nullptr;
    }
    
    OH\_AI\_ContextHandle CreateMSLiteContext(void \*modelBuffer)
    {
        // Set executing context for model.
        auto context = OH\_AI\_ContextCreate();
        if (context == nullptr) {
            DestroyModelBuffer(&modelBuffer);
            LOGE("MS\_LITE\_ERR: Create MSLite context failed.\\n");
            return nullptr;
        }
        // 本样例模型，不支持配置OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_NNRT)
        auto cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
    
        OH\_AI\_DeviceInfoSetEnableFP16(cpu\_device\_info, true);
        OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);
        
        LOGI("MS\_LITE\_LOG: Build MSLite context success.\\n");
        return context;
    }
    
    OH\_AI\_ModelHandle CreateMSLiteModel(void \*modelBuffer, size\_t modelSize, OH\_AI\_ContextHandle context)
    {
        // Create model
        auto model = OH\_AI\_ModelCreate();
        if (model == nullptr) {
            DestroyModelBuffer(&modelBuffer);
            LOGE("MS\_LITE\_ERR: Allocate MSLite Model failed.\\n");
            return nullptr;
        }
    
        // Build model object
        // \`OH\_AI\_MODELTYPE\_MINDIR\` 适用于 \`.ms\` 模型文件格式
        auto build\_ret = OH\_AI\_ModelBuild(model, modelBuffer, modelSize, OH\_AI\_MODELTYPE\_MINDIR, context);
        DestroyModelBuffer(&modelBuffer);
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
    
    // 设置模型输入数据
    int FillInputTensor(OH\_AI\_TensorHandle input, std::vector<float> input\_data)
    {
        if (OH\_AI\_TensorGetDataType(input) == OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT32) {
            float \*data = (float \*)OH\_AI\_TensorGetMutableData(input);
            for (size\_t i = 0; i < OH\_AI\_TensorGetElementNum(input); i++) {
                data\[i\] = input\_data\[i\];
            }
            return OH\_AI\_STATUS\_SUCCESS;
        } else {
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
    }
    
    // 执行模型推理
    int RunMSLiteModel(OH\_AI\_ModelHandle model, std::vector<float> input\_data)
    {
        // Set input data for model.
        auto inputs = OH\_AI\_ModelGetInputs(model);
        auto ret = FillInputTensor(inputs.handle\_list\[0\], input\_data);
        if (ret != OH\_AI\_STATUS\_SUCCESS) {
            LOGE("MS\_LITE\_ERR: RunMSLiteModel set input error.\\n");
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
    
        // Get model output.
        auto outputs = OH\_AI\_ModelGetOutputs(model);
    
        // Predict model.
        auto predict\_ret = OH\_AI\_ModelPredict(model, inputs, &outputs, nullptr, nullptr);
        if (predict\_ret != OH\_AI\_STATUS\_SUCCESS) {
            LOGE("MS\_LITE\_ERR: MSLite Predict error.\\n");
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
        LOGI("MS\_LITE\_LOG: Run MSLite model Predict success.\\n");
    
        // Print output tensor data.
        LOGI("MS\_LITE\_LOG: Get model outputs:\\n");
        for (size\_t i = 0; i < outputs.handle\_num; i++) {
            auto tensor = outputs.handle\_list\[i\];
            LOGI("MS\_LITE\_LOG: - Tensor %{public}d name is: %{public}s.\\n", static\_cast<int>(i),
                 OH\_AI\_TensorGetName(tensor));
            LOGI("MS\_LITE\_LOG: - Tensor %{public}d size is: %{public}d.\\n", static\_cast<int>(i),
                 (int)OH\_AI\_TensorGetDataSize(tensor));
            LOGI("MS\_LITE\_LOG: - Tensor data is:\\n");
            auto out\_data = reinterpret\_cast<const float \*>(OH\_AI\_TensorGetData(tensor));
            std::stringstream outStr;
            for (int i = 0; (i < OH\_AI\_TensorGetElementNum(tensor)) && (i <= K\_NUM\_PRINT\_OF\_OUT\_DATA); i++) {
                outStr << out\_data\[i\] << " ";
            }
            LOGI("MS\_LITE\_LOG: %{public}s", outStr.str().c\_str());
        }
        return OH\_AI\_STATUS\_SUCCESS;
    }
    
5.  调用以上方法，实现完整的模型推理流程。
    
    static napi\_value RunDemo(napi\_env env, napi\_callback\_info info)
    {
        // run demo
        napi\_value error\_ret;
        napi\_create\_int32(env, -1, &error\_ret);
        // 传入数据处理
        size\_t argc = 2;
        napi\_value argv\[2\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
        bool isArray = false;
        napi\_is\_array(env, argv\[0\], &isArray);
        uint32\_t length = 0;
        // 获取数组的长度
        napi\_get\_array\_length(env, argv\[0\], &length);
        LOGI("MS\_LITE\_LOG: argv array length = %{public}d", length);
        std::vector<float> input\_data;
        double param = 0;
        for (int i = 0; i < length; i++) {
            napi\_value value;
            napi\_get\_element(env, argv\[0\], i, &value);
            napi\_get\_value\_double(env, value, &param);
            input\_data.push\_back(static\_cast<float>(param));
        }
        std::stringstream outstr;
        for (int i = 0; i < K\_NUM\_PRINT\_OF\_OUT\_DATA; i++) {
            outstr << input\_data\[i\] << " ";
        }
        LOGI("MS\_LITE\_LOG: input\_data = %{public}s", outstr.str().c\_str());
        // Read model file
        const std::string modelName = "mobilenetv2.ms";
        LOGI("MS\_LITE\_LOG: Run model: %{public}s", modelName.c\_str());
        size\_t modelSize;
        auto resourcesManager = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[1\]);
        auto modelBuffer = ReadModelFile(resourcesManager, modelName, &modelSize);
        if (modelBuffer == nullptr) {
            LOGE("MS\_LITE\_ERR: Read model failed");
            return error\_ret;
        }
        LOGI("MS\_LITE\_LOG: Read model file success");
        
        auto context = CreateMSLiteContext(modelBuffer);
        if (context == nullptr) {
            LOGE("MS\_LITE\_ERR: MSLiteFwk Build context failed.\\n");
            return error\_ret;
        }
        auto model = CreateMSLiteModel(modelBuffer, modelSize, context);
        if (model == nullptr) {
            OH\_AI\_ContextDestroy(&context);
            LOGE("MS\_LITE\_ERR: MSLiteFwk Build model failed.\\n");
            return error\_ret;
        }
        int ret = RunMSLiteModel(model, input\_data);
        if (ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&model);
            OH\_AI\_ContextDestroy(&context);
            LOGE("MS\_LITE\_ERR: RunMSLiteModel failed.\\n");
            return error\_ret;
        }
        napi\_value out\_data;
        napi\_create\_array(env, &out\_data);
        auto outputs = OH\_AI\_ModelGetOutputs(model);
        OH\_AI\_TensorHandle output\_0 = outputs.handle\_list\[0\];
        float \*output0Data = reinterpret\_cast<float \*>(OH\_AI\_TensorGetMutableData(output\_0));
        for (size\_t i = 0; i < OH\_AI\_TensorGetElementNum(output\_0); i++) {
            napi\_value element;
            napi\_create\_double(env, static\_cast<double>(output0Data\[i\]), &element);
            napi\_set\_element(env, out\_data, i, element);
        }
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        LOGI("MS\_LITE\_LOG: Exit runDemo()");
        return out\_data;
    }
    
6.  编写CMake脚本，链接MindSpore Lite动态库。
    
    ```cmake
    # the minimum version of CMake.
    cmake_minimum_required(VERSION 3.4.1)
    project(MindSporeLiteCDemo)
    
    set(NATIVERENDER_PATH ${CMAKE_CURRENT_SOURCE_DIR})
    
    if(DEFINED PACKAGE_FIND_FILE)
        include(${PACKAGE_FIND_FILE})
    endif()
    
    include_directories(${NATIVERENDER_PATH}
                        ${NATIVERENDER_PATH}/include)
    
    add_library(entry SHARED mslite_napi.cpp)
    target_link_libraries(entry PUBLIC mindspore_lite_ndk)
    target_link_libraries(entry PUBLIC hilog_ndk.z)
    target_link_libraries(entry PUBLIC rawfile.z)
    target_link_libraries(entry PUBLIC ace_napi.z)
    ```
    

#### \[h2\]使用N-API将C++动态库封装成ArkTS模块

1.  在 entry/src/main/cpp/types/libentry/Index.d.ts，定义ArkTS接口runDemo() 。内容如下：
    
    ```typescript
    export const runDemo: (a: number[], b:Object) => Array<number>;
    ```
    
2.  在 oh-package.json5 文件，将API与so相关联，成为一个完整的ArkTS模块：
    
    ```json
    {
      "name": "libentry.so",
      "types": "./Index.d.ts",
      "version": "1.0.0",
      "description": "MindSpore Lite inference module"
    }
    ```
    

#### \[h2\]实现图像输入和预处理，并执行推理

1.  此处以获取相册图片为例，调用[@ohos.file.picker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker) 实现相册图片文件的选择。
2.  根据模型的输入尺寸，调用[@ohos.multimedia.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image) （实现图片处理）、[@ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs) （实现基础文件操作） API对选择图片进行裁剪、获取图片buffer数据，并进行标准化处理。
3.  在 entry/src/main/ets/pages/Index.ets 中，调用封装的ArkTS模块，最后对推理结果进行处理。

// Index.ets
import msliteNapi from 'libentry.so';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'MindSporeLite';
const PERMISSIONS: Permissions\[\] = \['ohos.permission.READ\_IMAGEVIDEO'\];

@Entry
@Component
struct Index {
  @State message: string = 'MindSporeLite C Demo';
  @State modelName: string = 'mobilenetv2.ms';
  @State modelInputHeight: number = 224;
  @State modelInputWidth: number = 224;
  @State uris: Array<string> = \[\];
  @State max: number = 0;
  @State maxIndex: number = 0;
  @State maxArray: Array<number> = \[\];
  @State maxIndexArray: Array<number> = \[\];

  build() {
    Row() {
      Column() {
        Text(this.message)
        Button() {
          Text('photo')
            .fontSize(30)
            .fontWeight(FontWeight.Bold)
        }
        .onClick(() => {
          let resMgr = this.getUIContext()?.getHostContext()?.getApplicationContext().resourceManager;
          if (resMgr === null || resMgr === undefined){
            hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: get resMgr failed.\`);
            return
          }

          // 获取相册图片
          // 1.创建图片文件选择实例
          let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();

          // 2.设置选择媒体文件类型为IMAGE，设置选择媒体文件的最大数目
          photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
          photoSelectOptions.maxSelectNumber = 1;

          // 3.创建图库选择器实例，调用select()接口拉起图库界面进行文件选择。文件选择成功后，返回photoSelectResult结果集。
          let photoPicker = new photoAccessHelper.PhotoViewPicker();
          photoPicker.select(photoSelectOptions,
            async (err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
              if (err) {
                hilog.error(0xFF00, TAG, '%{public}s',
                  \`MS\_LITE\_ERR: PhotoViewPicker.select failed with err: ${JSON.stringify(err)}\`);
                return;
              }
              hilog.info(0xFF00, TAG, '%{public}s',
                \`MS\_LITE\_LOG: PhotoViewPicker.select successfully, uri: ${JSON.stringify(photoSelectResult)}\`);
              this.uris = photoSelectResult.photoUris;
              hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: uri: ${this.uris}\`);

              // 预处理图片数据
              try {
                // 1.使用fileIo.openSync接口，通过uri打开这个文件得到fd
                let file = fileIo.openSync(this.uris\[0\], fileIo.OpenMode.READ\_ONLY);
                hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: file fd: ${file.fd}\`);

                // 2.通过fd使用fileIo.readSync接口读取这个文件内的数据
                let inputBuffer = new ArrayBuffer(4096000);
                let readLen = fileIo.readSync(file.fd, inputBuffer);
                hilog.info(0xFF00, TAG, '%{public}s',
                  \`MS\_LITE\_LOG: readSync data to file succeed and inputBuffer size is: ${readLen}\`);

                // 3.通过PixelMap预处理
                let imageSource = image.createImageSource(file.fd);
                if (imageSource === undefined) {
                  hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: createImageSource failed.\`);
                  return
                }
                imageSource.createPixelMap({ editable: true }).then((pixelMap) => {
                  pixelMap.getImageInfo().then((info) => {
                    hilog.info(0xFF00, TAG, '%{public}s',
                      \`MS\_LITE\_LOG: info.width = ${info.size.width}\`);
                    hilog.info(0xFF00, TAG, '%{public}s',
                      \`MS\_LITE\_LOG: info.height = ${info.size.height}\`);

                    // 4.根据模型输入的尺寸，将图片裁剪为对应的size，获取图片buffer数据readBuffer
                    pixelMap.scale(256.0 / info.size.width, 256.0 / info.size.height).then(() => {
                      pixelMap.crop({
                        x: 16,
                        y: 16,
                        size: { height: this.modelInputHeight, width: this.modelInputWidth }
                      }).then(async () => {
                        let info = await pixelMap.getImageInfo();
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: crop info.width = ${info.size.width}\`);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: crop info.height = ${info.size.height}\`);
                        // 需要创建的像素buffer大小
                        let readBuffer = new ArrayBuffer(this.modelInputHeight \* this.modelInputWidth \* 4);
                        await pixelMap.readPixelsToBuffer(readBuffer);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: Succeeded in reading image pixel data, buffer: ${readBuffer.byteLength}\`);
                        // 处理readBuffer，转换成float32格式，并进行标准化处理
                        const imageArr =
                          new Uint8Array(readBuffer.slice(0, this.modelInputHeight \* this.modelInputWidth \* 4));
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: imageArr length: ${imageArr.length}\`);

                        let means = \[0.485, 0.456, 0.406\];
                        let stds = \[0.229, 0.224, 0.225\];
                        let float32View = new Float32Array(this.modelInputHeight \* this.modelInputWidth \* 3);
                        let index = 0;
                        for (let i = 0; i < imageArr.length; i++) {
                          if ((i + 1) % 4 === 0) {
                            float32View\[index\] = (imageArr\[i - 3\] / 255.0 - means\[0\]) / stds\[0\]; // B
                            float32View\[index+1\] = (imageArr\[i - 2\] / 255.0 - means\[1\]) / stds\[1\]; // G
                            float32View\[index+2\] = (imageArr\[i - 1\] / 255.0 - means\[2\]) / stds\[2\]; // R
                            index += 3;
                          }
                        }
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: float32View length: ${float32View.length}\`);
                        let printStr = 'float32View data:';
                        for (let i = 0; i < 20; i++) {
                          printStr += ' ' + float32View\[i\];
                        }
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: float32View data: ${printStr}\`);

                        // 调用c++的runDemo
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: \*\*\* Start MSLite Demo \*\*\*\`);

                        let output: Array<number> = msliteNapi.runDemo(Array.from(float32View), resMgr);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_WARN: output length = ${output.length}, value = ${output.slice(0, 20)}\`);

                        // 取分类占比的最大值top5
                        this.max = 0;
                        this.maxIndex = 0;
                        this.maxArray = \[\];
                        this.maxIndexArray = \[\];
                        let newArray = output.filter(value => value !== this.max);
                        for (let n = 0; n < 5; n++) {
                          this.max = output\[0\];
                          this.maxIndex = 0;
                          // 取最大值
                          for (let m = 0; m < newArray.length; m++) {
                            if (newArray\[m\] > this.max) {
                              this.max = newArray\[m\];
                              this.maxIndex = m;
                            }
                          }
                          this.maxArray.push(Math.round(this.max \* 10000));
                          this.maxIndexArray.push(this.maxIndex);
                          // filter数组过滤函数
                          newArray = newArray.filter(value => value !== this.max);
                        }
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: max: ${this.maxArray}\`);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: maxIndex: ${this.maxIndexArray}\`);

                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: \*\*\* Finished MSLite Demo \*\*\*\`);
                      }).catch((error: BusinessError) => {
                        hilog.error(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_ERR: getRawFileContent promise error is: ${error}\`);
                      })
                    })
                    // 5.关闭文件
                    fileIo.closeSync(file);
                  })
                })
              } catch (err) {
                hilog.error(0xFF00, TAG, '%{public}s',
                  \`MS\_LITE\_ERR: uri: open file fd failed. ${err}\`);
              }
            })
        })
      }.width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]调测验证

1.  在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：
    
    ```shell
    Launching com.samples.mindsporelitecdemo
    $ hdc shell aa force-stop com.samples.mindsporelitecdemo
    $ hdc shell mkdir data/local/tmp/xxx
    $ hdc file send C:\Users\xxx\MindSporeLiteCDemo\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx"
    $ hdc shell bm install -p data/local/tmp/xxx
    $ hdc shell rm -rf data/local/tmp/xxx
    $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemo
    ```
    
2.  在设备屏幕点击photo按钮，选择图片，点击确定。设备屏幕显示所选图片的分类结果，在日志打印结果中，过滤关键字”MS\_LITE“，可得到如下结果：
    
    ```verilog
    08-05 17:15:52.001   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: PhotoViewPicker.select successfully, photoSelectResult uri: {"photoUris":["file://media/Photo/13/IMG_1501955351_012/plant.jpg"]}
    ...
    08-05 17:15:52.627   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: crop info.width = 224
    08-05 17:15:52.627   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: crop info.height = 224
    08-05 17:15:52.628   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: Succeeded in reading image pixel data, buffer: 200704
    08-05 17:15:52.971   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: float32View data: float32View data: 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143
    08-05 17:15:52.971   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: *** Start MSLite Demo ***
    08-05 17:15:53.454   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: Build MSLite model success.
    08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: Run MSLite model Predict success.
    08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: Get model outputs:
    08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: - Tensor 0 name is: Default/head-MobileNetV2Head/Sigmoid-op466.
    08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: - Tensor data is:
    08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: 3.43385e-06 1.40285e-05 9.11969e-07 4.91007e-05 9.50266e-07 3.94537e-07 0.0434676 3.97196e-05 0.00054832 0.000246202 1.576e-05 3.6494e-06 1.23553e-05 0.196977 5.3028e-05 3.29346e-05 4.90475e-07 1.66109e-06 7.03273e-06 8.83677e-07 3.1365e-06
    08-05 17:15:53.781   4684-4684    A03d00/JSAPP                   pid-4684              W     MS_LITE_WARN: output length =  500 ;value =  0.0000034338463592575863,0.000014028532859811094,9.119685273617506e-7,0.000049100715841632336,9.502661555416125e-7,3.945370394831116e-7,0.04346757382154465,0.00003971960904891603,0.0005483203567564487,0.00024620210751891136,0.000015759984307806008,0.0000036493988773145247,0.00001235533181898063,0.1969769448041916,0.000053027983085485175,0.000032934600312728435,4.904751449430478e-7,0.0000016610861166554969,0.000007032729172351537,8.836767619868624e-7
    08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: max:9497,7756,1970,435,46
    08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: maxIndex:323,46,13,6,349
    08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: *** Finished MSLite Demo ***
    ```
    

#### \[h2\]效果示意

在设备上，点击photo按钮，选择相册中的一张图片，点击确定。在图片下方显示此图片占比前4的分类信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/2C74EYKaTsK_6uN1ncbtkw/zh-cn_image_0000002569020007.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=BE8BE7F528C11F11F2854AC6B2A59E9D1DAB156F7456E034137F62AFD004FC19) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/6jHLXvS5TEyhT8Ss5ocN_A/zh-cn_image_0000002568899997.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=3E4393DADE67E41EBEB9A6EE218ABB00495BBD7C0A1660FCCEA3C36EF618D470)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Ncn5NiJ-RT-JppBnSDgwvQ/zh-cn_image_0000002538020292.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=D1403E91C101A5F6C3870AE487A6BB44085C900E08602619C453EF38EA1195FE) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/SbQmELPgQL215q1svLjlfw/zh-cn_image_0000002568899999.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=95A12CB52FA6E4CA42B141290ABE866608F3E0B610B45FE7E120C59B81E87B1F)

#### 示例代码

-   [基于MindSporeLite接口实现图像分类（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MindSporeLiteKit/MindSporeLiteCDemo)
