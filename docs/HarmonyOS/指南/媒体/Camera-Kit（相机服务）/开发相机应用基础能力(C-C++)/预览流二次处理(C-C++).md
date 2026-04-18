---
title: "预览流二次处理(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview-imagereceiver"
menu_path:
  - "指南"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "开发相机应用基础能力(C/C++)"
  - "预览流二次处理(C/C++)"
captured_at: "2026-04-17T01:36:05.400Z"
---

# 预览流二次处理(C/C++)

通过ImageReceiver创建预览输出，获取预览流实时数据，以供后续进行图像二次处理，比如应用可以对其添加滤镜算法等。

#### 开发步骤

详细的API说明请参考[OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。

1.  导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。
    
    #include <cstdint>
    #include <cstdlib>
    #include "hilog/log.h"
    #include <memory>
    #include <new>
    #include <multimedia/image\_framework/image/image\_native.h>
    #include <multimedia/image\_framework/image/image\_receiver\_native.h>
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/camera\_device.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "ohcamera/camera\_manager.h"
    
    #include <multimedia/media\_library/media\_asset\_manager\_capi.h>
    #include <multimedia/media\_library/media\_asset\_change\_request\_capi.h>
    #include <multimedia/media\_library/media\_access\_helper\_capi.h>
    #include <multimedia/image\_framework/image/image\_packer\_native.h>
    
2.  在CMake脚本中链接相关动态库。
    
    ```txt
    target_link_libraries(entry PUBLIC
        libace_napi.z.so
        libhilog_ndk.z.so
        libohimage.so
        libimage_receiver.so
        libnative_image.so
        libohcamera.so
        libnative_buffer.so
    )
    ```
    
3.  初始化图片接收器[ImageReceiver](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver-c)实例，获取SurfaceId。
    
    通过image的OH\_ImageReceiverNative\_Create方法创建OH\_ImageReceiverNative实例，再通过实例的OH\_ImageReceiverNative\_GetReceivingSurfaceId方法获取SurfaceId。
    
    void InitImageReceiver(uint64\_t &receiverSurfaceID)
    {
        OH\_ImageReceiverOptions \*options = nullptr;
        // 注意捕获错误码处理异常及对象判空，当前示例仅展示调用流程。
        // 设置图片参数。
        Image\_ErrorCode errCode = OH\_ImageReceiverOptions\_Create(&options);
        if (errCode != IMAGE\_SUCCESS || options == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverOptions\_Create call failed");
            return;
        }
        Image\_Size imgSize;
        imgSize.width = PREVIEW\_WIDTH; // 创建预览流的宽。
        imgSize.height = PREVIEW\_HEIGHT; // 创建预览流的高。
        int32\_t capacity = 8; // BufferQueue里最大Image数量，推荐填写8。
        errCode = OH\_ImageReceiverOptions\_SetSize(options, imgSize);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverOptions\_SetSize call failed");
        }
        errCode = OH\_ImageReceiverOptions\_SetCapacity(options, capacity);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverOptions\_SetCapacity call failed");
        }
        // 创建OH\_ImageReceiverNative对象。
        OH\_ImageReceiverNative \*receiver = nullptr;
        errCode = OH\_ImageReceiverNative\_Create(options, &receiver);
        if (errCode != IMAGE\_SUCCESS || receiver == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverNative\_Create call failed");
            return;
        }
    
        errCode = OH\_ImageReceiverNative\_On(receiver, CallbackReadNextImage);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "%{public}s image receiver on failed, errCode: %{public}d.", \_\_func\_\_, errCode);
            OH\_ImageReceiverOptions\_Release(options);
            OH\_ImageReceiverNative\_Release(receiver);
            return;
        }
        // 获取OH\_ImageReceiverNative对象的SurfaceId。
        errCode = OH\_ImageReceiverNative\_GetReceivingSurfaceId(receiver, &receiverSurfaceID);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverNative\_GetReceivingSurfaceId call failed");
        } else {
            OH\_LOG\_INFO(LOG\_APP, "receiver surfaceID:%{public}lu", receiverSurfaceID);
        }
    }
    
4.  通过上一步获取到的SurfaceId创建预览流（在创建预览流之前需要将SurfaceId类型转成char \*），参考[预览(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview)步骤4。
    
5.  创建会话，使能会话，参考[会话管理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)。
    
6.  注册ImageReceiver图片接收器的回调，监听获取每帧上报图像内容。
    
    void copyBuffer(OH\_NativeBuffer \*srcBuffer, size\_t srcSize, OHNativeWindowBuffer \*dstBuffer)
    {
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s IN", \_\_func\_\_);
        void \*srcVir = nullptr;
        OH\_NativeBuffer\_Map(srcBuffer, &srcVir);
        BufferHandle \*bufferHandle = OH\_NativeWindow\_GetBufferHandleFromNative(dstBuffer);
        OH\_LOG\_INFO(LOG\_APP,
            "ImageReceiverNativeCTest %{public}s bufferHandle info fd= %{public}d , width= %{public}d, "
            "height=%{public}d, stride= %{public}d, size= %{public}d, format= %{public}d, usage= %{public}lu",
            \_\_func\_\_, bufferHandle->fd, bufferHandle->width, bufferHandle->height, bufferHandle->stride, bufferHandle->size,
            bufferHandle->format, bufferHandle->usage);
    
        void \*mappedAddr =
            mmap(bufferHandle->virAddr, bufferHandle->size, PROT\_READ | PROT\_WRITE, MAP\_SHARED, bufferHandle->fd, 0);
        std::memcpy(static\_cast<unsigned char \*>(mappedAddr), static\_cast<unsigned char \*>(srcVir), srcSize);
        munmap(mappedAddr, bufferHandle->size);
    
        OH\_NativeBuffer\_Unmap(srcBuffer);
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", \_\_func\_\_);
    }
    
    void ShowImage(OH\_ImageNative \*image)
    {
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s IN", \_\_func\_\_);
        uint64\_t xComponentSurfaceId = std::stoull(g\_xComponentSurfaceIdSlave);
        OH\_LOG\_ERROR(LOG\_APP, "ImageReceiverNativeCTest %{public}s XComponentId is : %{public}lu.", \_\_func\_\_,
            xComponentSurfaceId);
        OHNativeWindow \*nativeWindow = nullptr;
        int32\_t res = OH\_NativeWindow\_CreateNativeWindowFromSurfaceId(xComponentSurfaceId, &nativeWindow);
        if (res != 0) {
            OH\_LOG\_ERROR(LOG\_APP,
                "ShowImage CreateNativeWindowFromSurfaceId failed, errCode: %{public}d.", res);
            return;
        }
    
        // 关键：调整nativeWindow大小及format，需要与image的大小、format保持一致。
        res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_BUFFER\_GEOMETRY, g\_imageWidth, g\_imageHeight);
        res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_FORMAT, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP); // NV21
        // 设置旋转角度，后置默认旋转90，则需要将nativeWindow旋转270度，前置默认270，则需要将nativeWindow旋转90度。
        if (g\_isFront) {
            res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_TRANSFORM, NATIVEBUFFER\_FLIP\_V\_ROT90);
        } else {
            res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_TRANSFORM, NATIVEBUFFER\_ROTATE\_270);
        }
    
        OH\_NativeBuffer \*imageBuffer = nullptr;
        Image\_ErrorCode errCode = OH\_ImageNative\_GetByteBuffer(image, g\_jpegComponent, &imageBuffer);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "ShowImage GetByteBuffer failed, errCode: %{public}d.", errCode);
            return;
        }
        Image\_Size imgSize = {};
        OH\_ImageNative\_GetImageSize(image, &imgSize);
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s imgSize is : %{public}u, %{public}u.", \_\_func\_\_,
            imgSize.width, imgSize.height);
        size\_t bufSize = 0;
        OH\_ImageNative\_GetBufferSize(image, g\_jpegComponent, &bufSize);
    
        OHNativeWindowBuffer \*nativeWindowBuffer = nullptr;
        int fenceFd = -1;
        res = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow, &nativeWindowBuffer, &fenceFd);
        if (res != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "ShowImage RequestBuffer failed, errCode: %{public}d.", res);
            return;
        }
    
        // 将image数据拷贝到nativeWindowBuffer上。
        copyBuffer(imageBuffer, bufSize, nativeWindowBuffer);
    
        Region region1{};
        res = OH\_NativeWindow\_NativeWindowFlushBuffer(nativeWindow, nativeWindowBuffer, fenceFd, region1);
        if (res != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "ShowImage FlushBuffer failed, errCode: %{public}d.", res);
            return;
        }
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", \_\_func\_\_);
    }
    
    static void CallbackReadNextImage(OH\_ImageReceiverNative \*receiver)
    {
        OH\_LOG\_INFO(LOG\_APP, "CallbackReadNextImage %{public}s IN", \_\_func\_\_);
        // 读取OH\_ImageReceiverNative下一张图片对象。
        OH\_ImageNative \*image = nullptr;
        Image\_ErrorCode errCode = OH\_ImageReceiverNative\_ReadNextImage(receiver, &image);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP,
                "CallbackReadNextImage %{public}s get image receiver next image failed, errCode: %{public}d.", \_\_func\_\_,
                errCode);
            return;
        }
    
        ShowImage(image);
    
        // 释放OH\_ImageNative实例。
        errCode = OH\_ImageNative\_Release(image);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "CallbackReadNextImage %{public}s release image native failed, errCode: %{public}d.",
                \_\_func\_\_, errCode);
        }
        OH\_LOG\_INFO(LOG\_APP, "CallbackReadNextImage %{public}s SUCCESS", \_\_func\_\_);
    }
