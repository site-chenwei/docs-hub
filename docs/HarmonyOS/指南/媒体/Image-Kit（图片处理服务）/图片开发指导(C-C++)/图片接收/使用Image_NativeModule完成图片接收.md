---
title: "使用Image_NativeModule完成图片接收"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver-c"
menu_path:
  - "指南"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "图片开发指导(C/C++)"
  - "图片接收"
  - "使用Image_NativeModule完成图片接收"
captured_at: "2026-04-17T01:36:06.224Z"
---

# 使用Image\_NativeModule完成图片接收

图像接收类，用于获取组件的surfaceId、接收最新的图片、读取下一张图片以及释放ImageReceiver实例。结合camera API实现的相机预览示例代码可参考[预览流二次处理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview-imagereceiver)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/zqHKsKBZRJ22AF0vHf37Yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=5FF6CAF83732DF23C14E94A8DE675A78AEC65CDB999565EED9A49AD61162B939)

ImageReceiver只作为图片的接收方、消费者，在ImageReceiver设置的size、format等属性实际上并不会生效。图片属性需要在发送方、生产者进行设置，可参考[预览(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview)设置previewProfiles。

#### 开发步骤

#### \[h2\]添加依赖

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libohimage.so、libimage\_receiver.so、libnative\_image.so以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libohimage.so libimage_receiver.so libnative_image.so)
```

#### \[h2\]Native接口调用

具体接口说明请参考[Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。

下述代码主要演示了Receiver的初始化、相机预览流的创建以及获取图像的信息和Receiver的释放等相关功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/bFWUhYEkTVKGnJSOt6SHIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013606Z&HW-CC-Expire=86400&HW-CC-Sign=21827185865A970DB7A5A03F5A3212F9B840DC4870D9FE9DA1FA3472AF44A098)

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1.  导入相关头文件。
    
    #include <hilog/log.h>
    #include "napi/native\_api.h"
    #include <string>
    #include <multimedia/image\_framework/image/image\_native.h>
    #include <multimedia/image\_framework/image/image\_receiver\_native.h>
    
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "ohcamera/camera\_manager.h"
    
    #include <mutex>
    #include <shared\_mutex> // C++17以上使用
    #include <condition\_variable>
    
2.  常量定义。
    
    #undef LOG\_DOMAIN
    #define LOG\_DOMAIN 0x3200
    
    #undef LOG\_TAG
    #define LOG\_TAG "MY\_TAG"
    
    #define IMAGE\_WIDTH 320
    #define IMAGE\_HEIGHT 480
    #define IMAGE\_CAPACITY 2
    
3.  定义全局变量。
    
    static OH\_ImageReceiverNative\* g\_receiver = nullptr;
    
    static std::mutex g\_mutex;
    static std::shared\_mutex shared\_receiver\_mutex;
    static std::condition\_variable g\_condVar;
    static bool g\_imageReady = false;
    static OH\_ImageNative\* g\_imageInfoResult = nullptr;
    
4.  定义一些工具类函数，用来处理napi的返回值和参数类型的转换。
    
    // 处理napi返回值。
    napi\_value GetJsResultDemo(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
    // 将uint64\_t转换为一个以null结尾的char数组。
    std::unique\_ptr<char\[\]> ConvertUint64ToCharTemp(uint64\_t value)
    {
        std::string strValue = std::to\_string(value);
        auto charBuffer = std::make\_unique<char\[\]>(strValue.size() + 1);
        std::copy(strValue.begin(), strValue.end(), charBuffer.get());
        charBuffer\[strValue.size()\] = '\\0';
    
        return charBuffer;
    }
    
5.  初始化Receiver。
    
    -   创建并设置ReceiverOptions。
        
        static Image\_ErrorCode CreateAndConfigOptions(OH\_ImageReceiverOptions\*\* options)
        {
            Image\_ErrorCode errCode = OH\_ImageReceiverOptions\_Create(options);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Create image receiver options failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            Image\_Size imgSize = {IMAGE\_WIDTH, IMAGE\_HEIGHT};
            errCode = OH\_ImageReceiverOptions\_SetSize(\*options, imgSize);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Set image receiver options size failed, errCode: %{public}d.", errCode);
                OH\_ImageReceiverOptions\_Release(\*options);
                return errCode;
            }
            errCode = OH\_ImageReceiverOptions\_SetCapacity(\*options, IMAGE\_CAPACITY);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Set image receiver options capacity failed, errCode: %{public}d.", errCode);
                OH\_ImageReceiverOptions\_Release(\*options);
                return errCode;
            }
            return IMAGE\_SUCCESS;
        }
        
    -   获取ReceiverOptions。
        
        static Image\_ErrorCode ValidateOptions(OH\_ImageReceiverOptions\* options)
        {
            Image\_Size imgSizeRead;
            Image\_ErrorCode errCode = OH\_ImageReceiverOptions\_GetSize(options, &imgSizeRead);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options size failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            if (imgSizeRead.width != IMAGE\_WIDTH || imgSizeRead.height != IMAGE\_HEIGHT) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options size failed,"
                             "width: %{public}d, height: %{public}d.", imgSizeRead.width, imgSizeRead.height);
                return IMAGE\_BAD\_PARAMETER;
            }
            int32\_t capacity = 0;
            errCode = OH\_ImageReceiverOptions\_GetCapacity(options, &capacity);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options capacity failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            if (capacity != IMAGE\_CAPACITY) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options capacity failed, capacity: %{public}d.", capacity);
                return IMAGE\_BAD\_PARAMETER;
            }
            return IMAGE\_SUCCESS;
        }
        
    -   创建Receiver对象。
        
        static Image\_ErrorCode CreateReceiver(OH\_ImageReceiverOptions\* options, OH\_ImageReceiverNative\*\* receiver)
        {
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_Create(options, receiver);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Create image receiver failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            return IMAGE\_SUCCESS;
        }
        
    -   定义获取下一张图片的callback函数。
        
        static void OnCallback(OH\_ImageReceiverNative\* receiver)
        {
            OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest buffer available.");
        
            // 共享锁（读）
            std::shared\_lock<std::shared\_mutex> lock(shared\_receiver\_mutex);
            OH\_ImageNative\* image = nullptr;
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_ReadNextImage(receiver, &image);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "ImageReceiverNativeCTest get image receiver next image failed,"
                             "errCode: %{public}d.", errCode);
                OH\_ImageNative\_Release(image);
                return;
            } else {
                std::lock\_guard<std::mutex> lock(g\_mutex);
                g\_imageInfoResult = image;
                g\_imageReady = true;
            }
            g\_condVar.notify\_one();
        }
        
    -   注册callback。
        
        static Image\_ErrorCode RegisterCallbackAndQuery(OH\_ImageReceiverNative\* receiver)
        {
            uint64\_t surfaceID = 0;
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_On(receiver, OnCallback);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Image receiver on failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            errCode = OH\_ImageReceiverNative\_GetReceivingSurfaceId(receiver, &surfaceID);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver surfaceID failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            OH\_LOG\_INFO(LOG\_APP, "Get image receiver surfaceID: %{public}lu.", surfaceID);
            Image\_Size imgSizeRead;
            errCode = OH\_ImageReceiverNative\_GetSize(receiver, &imgSizeRead);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver size failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            OH\_LOG\_INFO(LOG\_APP, "Get image receiver size: width = %{public}d, height = %{public}d.",
                        imgSizeRead.width, imgSizeRead.height);
            int32\_t capacity = 0;
            errCode = OH\_ImageReceiverNative\_GetCapacity(receiver, &capacity);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver capacity failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            OH\_LOG\_INFO(LOG\_APP, "Get image receiver capacity: %{public}d.", capacity);
            return IMAGE\_SUCCESS;
        }
        
    -   初始化Receiver的整体流程。
        
        static napi\_value ImageReceiverNativeCTest(napi\_env env, napi\_callback\_info info)
        {
            if (g\_receiver != nullptr) {
                OH\_ImageReceiverNative\_Off(g\_receiver);
                OH\_ImageReceiverNative\_Release(g\_receiver);
                g\_receiver = nullptr;
            }
        
            OH\_ImageReceiverOptions\* options = nullptr;
            Image\_ErrorCode errCode = CreateAndConfigOptions(&options);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "CreateAndConfigOptions failed errCode=%{public}d", errCode);
                return GetJsResultDemo(env, errCode);
            }
            errCode = ValidateOptions(options);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "ValidateOptions failed errCode=%{public}d", errCode);
                OH\_ImageReceiverOptions\_Release(options);
                return GetJsResultDemo(env, errCode);
            }
            errCode = CreateReceiver(options, &g\_receiver);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "CreateReceiver failed errCode=%{public}d", errCode);
                OH\_ImageReceiverOptions\_Release(options);
                return GetJsResultDemo(env, errCode);
            }
            errCode = RegisterCallbackAndQuery(g\_receiver);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "RegisterCallbackAndQuery failed errCode=%{public}d", errCode);
                OH\_ImageReceiverOptions\_Release(options);
                OH\_ImageReceiverNative\_Release(g\_receiver);
                g\_receiver = nullptr;
                return GetJsResultDemo(env, errCode);
            }
            OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest create and config success.");
            OH\_ImageReceiverOptions\_Release(options);
            return GetJsResultDemo(env, IMAGE\_SUCCESS);
        }
        
6.  调用相机拍照流进行拍照，触发回调。
    
    -   创建一个CameraManager实例。
        
        Camera\_ErrorCode InitCameraManagerAndInput(Camera\_Manager\*& cameraManager,
                                                   Camera\_Device\*& cameras,
                                                   uint32\_t& size,
                                                   Camera\_Input\*& cameraInput)
        {
            cameraManager = nullptr;
            cameras = nullptr;
            size = 0;
            cameraInput = nullptr;
            Camera\_ErrorCode ret = OH\_Camera\_GetCameraManager(&cameraManager);
            if (cameraManager == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_GetCameraManager failed.");
                return ret;
            }
            ret = OH\_CameraManager\_GetSupportedCameras(cameraManager, &cameras, &size);
            if (cameras == nullptr || size < 1 || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameras failed.");
                return ret;
            }
        
            for (uint32\_t i = 0; i < size; ++i) {
                OH\_LOG\_INFO(LOG\_APP, "Camera\[%{public}u\]: id=%{public}s, position=%{public}d, type=%{public}d, "
                    "connectionType=%{public}d", i, cameras\[i\].cameraId, cameras\[i\].cameraPosition, cameras\[i\].cameraType,
                    cameras\[i\].connectionType);
            }
        
            ret = OH\_CameraManager\_CreateCameraInput(cameraManager, &cameras\[0\], &cameraInput);
            if (cameraInput == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCameraInput failed.ret:%{public}d", ret);
                return ret;
            }
            return CAMERA\_OK;
        }
        
    -   获取相机输出能力。
        
        Camera\_ErrorCode GetCameraOutputCapability(Camera\_Manager\* cameraManager,
                                                   Camera\_Device\* cameras,
                                                   uint32\_t cameraDeviceIndex,
                                                   Camera\_OutputCapability\*& capability)
        {
            capability = nullptr;
            Camera\_ErrorCode ret = OH\_CameraManager\_GetSupportedCameraOutputCapability(cameraManager,
                                                                                       &cameras\[cameraDeviceIndex\],
                                                                                       &capability);
            if (capability == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameraOutputCapability failed.");
            }
            return ret;
        }
        
    -   创建相机捕获会话，用于捕获相机拍摄的照片。
        
        Camera\_CaptureSession\* CreateAndStartSession(Camera\_Manager\* cameraManager, Camera\_Input\* cameraInput, int sessionMode)
        {
            Camera\_CaptureSession\* captureSession = nullptr;
            Camera\_ErrorCode ret = OH\_CameraManager\_CreateCaptureSession(cameraManager, &captureSession);
            if (captureSession == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCaptureSession failed.");
                return nullptr;
            }
            ret = OH\_CaptureSession\_SetSessionMode(captureSession, static\_cast<Camera\_SceneMode>(sessionMode));
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetSessionMode failed.");
                return nullptr;
            }
            ret = OH\_CaptureSession\_BeginConfig(captureSession);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_BeginConfig failed.");
                return nullptr;
            }
            ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
                return nullptr;
            }
            return captureSession;
        }
        
    -   开启捕获会话。
        
        static Camera\_ErrorCode StartCaptureSession(Camera\_Manager\* mgr, Camera\_Input\* input,
                                                    Camera\_PreviewOutput\* previewOutput,
                                                    Camera\_CaptureSession\*\* sessionOut)
        {
            \*sessionOut = CreateAndStartSession(mgr, input, NORMAL\_PHOTO);
            if (\*sessionOut == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "CreateAndStartSession failed.");
                return CAMERA\_INVALID\_ARGUMENT;
            }
        
            Camera\_ErrorCode ret = OH\_CaptureSession\_AddPreviewOutput(\*sessionOut, previewOutput);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
                return ret;
            }
        
            ret = OH\_CaptureSession\_CommitConfig(\*sessionOut);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
                return ret;
            }
        
            ret = OH\_CaptureSession\_Start(\*sessionOut);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
            }
            
            return ret;
        }
        
    -   创建相机拍照流。
        
        Camera\_ErrorCode StartTakePhoto(char\* str)
        {
            char\* photoSurfaceId = str;
            Camera\_Manager\* cameraManager = nullptr;
            Camera\_Device\* cameras = nullptr;
            uint32\_t size = 0;
            Camera\_Input\* cameraInput = nullptr;
            Camera\_ErrorCode ret = InitCameraManagerAndInput(cameraManager, cameras, size, cameraInput);
            if (ret != CAMERA\_OK) return ret;
        
            Camera\_OutputCapability\* cameraOutputCapability = nullptr;
            ret = GetCameraOutputCapability(cameraManager, cameras, 0, cameraOutputCapability);
            if (ret != CAMERA\_OK) return ret;
            
            const Camera\_Profile\* photoProfile = cameraOutputCapability->previewProfiles\[0\];
            Camera\_PreviewOutput\* previewOutput = nullptr;
            ret = OH\_CameraManager\_CreatePreviewOutput(cameraManager, photoProfile, photoSurfaceId, &previewOutput);
            if (photoProfile == nullptr || previewOutput == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreatePreviewOutput failed.");
                return ret;
            }
        
            ret = OH\_CameraInput\_Open(cameraInput);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_open failed.");
                return ret;
            }
        
            Camera\_CaptureSession\* captureSession = nullptr;
            ret = StartCaptureSession(cameraManager, cameraInput, previewOutput, &captureSession);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "StartCaptureSession failed.");
                return ret;
            }
            
            return CAMERA\_OK;
        }
        
    -   调用相机拍照的整体流程。
        
        static napi\_value TakePhoto(napi\_env env, napi\_callback\_info info)
        {
            if (g\_receiver == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "ImageReceiver not initialized.");
                return GetJsResultDemo(env, IMAGE\_BAD\_PARAMETER);
            }
            uint64\_t surfaceId = 0;
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_GetReceivingSurfaceId(g\_receiver, &surfaceId);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get surfaceId failed.");
                return GetJsResultDemo(env, errCode);
            }
        
            auto surfaceId\_c = ConvertUint64ToCharTemp(surfaceId);
            Camera\_ErrorCode photoRet = StartTakePhoto(surfaceId\_c.get());
            return GetJsResultDemo(env, photoRet);
        }
        
7.  获取Receiver接收到的图片信息。
    
    -   等待OnCallback回调通知。
        
        // 同步等待。
        static OH\_ImageNative\* NotifyJsImageInfoSync()
        {
            std::unique\_lock<std::mutex> lock(g\_mutex);
            g\_imageReady = false;
            g\_imageInfoResult = nullptr;
        
            // 等待OnCallback回调通知。
            bool ret = g\_condVar.wait\_for(lock, std::chrono::seconds(1), \[\] {
                OH\_LOG\_INFO(LOG\_APP, "NotifyJsImageInfoSync: wait\_for wakeup, g\_imageReady=%{public}d", g\_imageReady);
                return g\_imageReady;
            });
            if (!ret) {
                OH\_LOG\_ERROR(LOG\_APP, "NotifyJsImageInfoSync: wait\_for timeout.");
                return nullptr;
            }
            return g\_imageInfoResult;
        }
        
    -   获取图片大小。
        
        // 获取图片大小。
        static napi\_value GetImageSizeInfo(napi\_env env, OH\_ImageNative\* image)
        {
            OH\_LOG\_INFO(LOG\_APP, "GetImageSizeInfo: enter, image=%{public}p", image);
        
            Image\_Size imgSizeRead;
            Image\_ErrorCode errCode = OH\_ImageNative\_GetImageSize(image, &imgSizeRead);
            OH\_LOG\_INFO(LOG\_APP, "GetImageSizeInfo: GetImageSize errCode=%{public}d, width=%{public}d, height=%{public}d",
                        errCode, imgSizeRead.width, imgSizeRead.height);
        
            if (errCode == IMAGE\_SUCCESS) {
                napi\_value resultObj;
                napi\_create\_object(env, &resultObj);
        
                napi\_value width;
                napi\_value height;
                napi\_create\_int32(env, imgSizeRead.width, &width);
                napi\_create\_int32(env, imgSizeRead.height, &height);
        
                napi\_set\_named\_property(env, resultObj, "width", width);
                napi\_set\_named\_property(env, resultObj, "height", height);
        
                OH\_LOG\_INFO(LOG\_APP, "GetImageSizeInfo: exit");
                return resultObj;
            }
        
            OH\_LOG\_ERROR(LOG\_APP, "GetImageSizeInfo: Failed to get image size");
            return nullptr;
        }
        
    -   获取组件类型。
        
        // 获取组件类型。
        static size\_t GetComponentTypeSize(OH\_ImageNative\* image, size\_t& componentTypeSize)
        {
            OH\_LOG\_INFO(LOG\_APP, "GetComponentTypeSize: enter, image=%{public}p", image);
            // 获取组件类型的大小。
            Image\_ErrorCode errCode = OH\_ImageNative\_GetComponentTypes(image, nullptr, &componentTypeSize);
            OH\_LOG\_INFO(LOG\_APP, "GetComponentTypeSize: GetComponentTypes (query size) errCode=%{public}d,"
                        "componentTypeSize=%{public}zu", errCode, componentTypeSize);
            return componentTypeSize;
        }
        
    -   获取组件信息。
        
        // 获取组件信息。
        static napi\_value GetComponentInfo(napi\_env env, size\_t componentTypeSize, OH\_ImageNative\* image, napi\_value resultObj)
        {
            if (componentTypeSize > 0) {
                uint32\_t\* components = new uint32\_t\[componentTypeSize\];
                Image\_ErrorCode errCode = OH\_ImageNative\_GetComponentTypes(image, &components, &componentTypeSize);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetComponentTypes (get types) errCode=%{public}d,"
                            "firstComponent=%{public}u", errCode, componentTypeSize > 0 ? components\[0\] : 0);
                if (errCode != IMAGE\_SUCCESS) {
                    OH\_LOG\_ERROR(LOG\_APP, "GetImageInfoObject: GetComponentTypes (get types) failed");
                    delete \[\] components;
                    return resultObj;
                }
                
                OH\_NativeBuffer\* nativeBuffer = nullptr;
                errCode = OH\_ImageNative\_GetByteBuffer(image, components\[0\], &nativeBuffer);
                if (errCode == IMAGE\_SUCCESS) {
                    OH\_LOG\_INFO(LOG\_APP, "Get native buffer success.");
                }
            
                size\_t nativeBufferSize = 0;
                errCode = OH\_ImageNative\_GetBufferSize(image, components\[0\], &nativeBufferSize);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetBufferSize errCode=%{public}d, nativeBufferSize=%{public}zu",
                            errCode, nativeBufferSize);
                if (errCode == IMAGE\_SUCCESS) {
                    napi\_value bufSize;
                    napi\_create\_int32(env, static\_cast<int32\_t>(nativeBufferSize), &bufSize);
                    napi\_set\_named\_property(env, resultObj, "bufferSize", bufSize);
                }
            
                int32\_t rowStride = 0;
                errCode = OH\_ImageNative\_GetRowStride(image, components\[0\], &rowStride);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetRowStride errCode=%{public}d,"
                            "rowStride=%{public}d", errCode, rowStride);
                if (errCode == IMAGE\_SUCCESS) {
                    napi\_value jsRowStride;
                    napi\_create\_int32(env, rowStride, &jsRowStride);
                    napi\_set\_named\_property(env, resultObj, "rowStride", jsRowStride);
                }
            
                int32\_t pixelStride = 0;
                errCode = OH\_ImageNative\_GetPixelStride(image, components\[0\], &pixelStride);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetPixelStride errCode=%{public}d, pixelStride=%{public}d",
                            errCode, pixelStride);
                if (errCode == IMAGE\_SUCCESS) {
                    napi\_value jsPixelStride;
                    napi\_create\_int32(env, pixelStride, &jsPixelStride);
                    napi\_set\_named\_property(env, resultObj, "pixelStride", jsPixelStride);
                }
                delete \[\] components;
            }
            return resultObj;
        }
        
    -   获取图片属性并封装为napi对象。
        
        // 获取图像属性并封装为napi对象。
        static napi\_value GetImageInfoObject(napi\_env env, OH\_ImageNative\* image)
        {
            OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: enter, image=%{public}p", image);
            napi\_value resultObj;
            napi\_create\_object(env, &resultObj);
            resultObj = GetImageSizeInfo(env, image);
            
            size\_t componentTypeSize = 0;
            componentTypeSize = GetComponentTypeSize(image, componentTypeSize);
            if (componentTypeSize > 0) {
                resultObj = GetComponentInfo(env, componentTypeSize, image, resultObj);
            }
        
            int64\_t timestamp = 0;
            Image\_ErrorCode errCode = OH\_ImageNative\_GetTimestamp(image, &timestamp);
            OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetTimestamp errCode=%{public}d, timestamp=%{public}ld",
                        errCode, timestamp);
            if (errCode == IMAGE\_SUCCESS) {
                napi\_value jsTimestamp;
                napi\_create\_int64(env, timestamp, &jsTimestamp);
                napi\_set\_named\_property(env, resultObj, "timestamp", jsTimestamp);
            }
        
            OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: exit");
            return resultObj;
        }
        
    -   获取ReceiverImageInfo的整体流程。
        
        static napi\_value GetReceiverImageInfo(napi\_env env, napi\_callback\_info info)
        {
            OH\_ImageNative\* image = NotifyJsImageInfoSync();
            if (!image) {
                napi\_value undefined;
                napi\_get\_undefined(env, &undefined);
                return undefined;
            }
            napi\_value resultObj = GetImageInfoObject(env, image);
            OH\_ImageNative\_Release(image);
            return resultObj;
        }
        
8.  释放receiver。
    
    static napi\_value ReleaseImageReceiver(napi\_env env, napi\_callback\_info info)
    {
        if (g\_receiver == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "No image receiver to release.");
            return nullptr;
        }
    
        Image\_ErrorCode errCode = OH\_ImageReceiverNative\_Off(g\_receiver);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "ImageReceiverNativeCTest image receiver off failed, errCode: %{public}d.", errCode);
        }
    
        // 独占锁（写）
        std::unique\_lock<std::shared\_mutex> lock(shared\_receiver\_mutex);
        errCode = OH\_ImageReceiverNative\_Release(g\_receiver);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "Release image receiver failed, errCode: %{public}d.", errCode);
        }
        
        g\_receiver = nullptr;
        return GetJsResultDemo(env, errCode);
    }
