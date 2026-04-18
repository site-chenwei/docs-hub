---
title: "图片绘制（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "图元绘制"
  - "图片绘制（C/C++）"
captured_at: "2026-04-17T01:36:08.725Z"
---

# 图片绘制（C/C++）

位图是一种用于在内存中存储和表示图像的数据结构，它是一个未经过压缩的像素集合，而JPEG或PNG等图片是压缩格式的，两者并不相同。如果需要将JPEG或PNG绘制到屏幕上，需要先解码成位图格式，具体可参考[图片处理服务（Image Kit）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-overview)图片解码相关章节。

目前Drawing（C/C++）中位图绘制需要依赖PixelMap，它可以用于读取或写入图像数据以及获取图像信息。详细的API介绍请参考[drawing\_pixel\_map.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pixel-map-h)。

有多个API接口可以创建PixelMap，下文以使用OH\_Drawing\_PixelMapGetFromOhPixelMapNative()为例。

1.  添加链接库。
    
    在Native工程的src/main/cpp/CMakeLists.txt，添加如下链接库：
    
    ```
    target_link_libraries(entry PUBLIC libnative_drawing.so)
    target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
    target_link_libraries(entry PUBLIC libpixelmap.so)
    ```
    
2.  导入依赖的相关头文件。
    
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
3.  创建OH\_PixelmapNative像素图对象。
    
    PixelMap需要从图像框架定义的像素图对象（OH\_PixelmapNative）中获取，所以需要先通过OH\_PixelmapNative\_CreatePixelmap()创建OH\_PixelmapNative。该函数接受4个参数，第一个参数为图像像素数据的缓冲区，用于初始化PixelMap的像素。第二个参数是缓冲区长度。第三个参数是位图格式（包括长、宽、颜色类型、透明度类型等）。第四个参数即OH\_PixelmapNative对象，作为出参使用。
    
    // 图片宽高分别为 600 \* 400
    uint32\_t width = 600;
    uint32\_t height = 400;
    // 字节长度，RGBA\_8888每个像素占4字节
    size\_t bufferSize = width \* height \* 4;
    uint8\_t \*pixels = new uint8\_t\[bufferSize\];
    for (uint32\_t i = 0; i < width \* height; ++i) {
        // 遍历并编辑每个像素，从而形成红绿蓝相间的条纹
        uint32\_t n = i / 20 % 3;
        pixels\[i \* RGBA\_SIZE\] = RGBA\_MIN; // 红色通道
        pixels\[i \* RGBA\_SIZE + 1\] = RGBA\_MIN; // +1表示绿色通道
        pixels\[i \* RGBA\_SIZE + 2\] = RGBA\_MIN; // +2表示蓝色通道
        pixels\[i \* RGBA\_SIZE + 3\] = 0xFF; // +3表示不透明度通道
        if (n == 0) {
            pixels\[i \* RGBA\_SIZE\] = 0xFF; // 红色通道赋值，颜色显红色
        } else if (n == 1) {
            pixels\[i \* RGBA\_SIZE + 1\] = 0xFF; // +1表示绿色通道赋值，其余通道为0，颜色显绿色
        } else {
            pixels\[i \* RGBA\_SIZE + 2\] = 0xFF; // +2表示蓝色通道赋值，其余通道为0，颜色显蓝色
        }
    }
    // 设置位图格式（长、宽、颜色类型、透明度类型）
    OH\_Pixelmap\_InitializationOptions \*createOps = nullptr;
    OH\_PixelmapInitializationOptions\_Create(&createOps);
    OH\_PixelmapInitializationOptions\_SetWidth(createOps, width);
    OH\_PixelmapInitializationOptions\_SetHeight(createOps, height);
    OH\_PixelmapInitializationOptions\_SetPixelFormat(createOps, PIXEL\_FORMAT\_RGBA\_8888);
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOps, PIXELMAP\_ALPHA\_TYPE\_UNKNOWN);
    // 创建OH\_PixelmapNative对象
    OH\_PixelmapNative \*pixelMapNative = nullptr;
    OH\_PixelmapNative\_CreatePixelmap(pixels, bufferSize, createOps, &pixelMapNative);
    
4.  创建PixelMap。
    
    通过OH\_Drawing\_PixelMapGetFromOhPixelMapNative()函数从OH\_PixelmapNative中获取PixelMap。
    
    OH\_Drawing\_PixelMap \*pixelMap = OH\_Drawing\_PixelMapGetFromOhPixelMapNative(pixelMapNative);
    
5.  绘制PixelMap。
    
    需要通过OH\_Drawing\_CanvasDrawPixelMapRect()绘制位图PixelMap。函数接受5个参数，分别为画布Canvas、PixelMap对象、PixelMap中像素的截取区域、画布中显示的区域以及采样选项对象。
    
    其中采样选项对象（OH\_Drawing\_SamplingOptions）表示了从原始像素数据（即Bitmap）中采样以生成新的像素值的具体方式，具体可见[drawing\_sampling\_options.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-sampling-options-h)。
    
    // PixelMap中像素的截取区域
    OH\_Drawing\_Rect \*src = OH\_Drawing\_RectCreate(0, 0, 600, 400);
    // 画布中显示的区域
    OH\_Drawing\_Rect \*dst = OH\_Drawing\_RectCreate(value200\_, value200\_, value800\_, value600\_);
    // 采样选项对象
    OH\_Drawing\_SamplingOptions\* samplingOptions = OH\_Drawing\_SamplingOptionsCreate(
        OH\_Drawing\_FilterMode::FILTER\_MODE\_LINEAR, OH\_Drawing\_MipmapMode::MIPMAP\_MODE\_LINEAR);
    // 绘制PixelMap
    OH\_Drawing\_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, samplingOptions);
    
6.  绘制完成后释放相关对象。
    
    OH\_PixelmapNative\_Release(pixelMapNative);
    delete\[\] pixels;
    
    绘制效果如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/WUn11D-2RNaQ6Yprn5j1-g/zh-cn_image_0000002569019327.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=A143C9DD4EC5B8E8CD85828A230C6221892AF8D52143FBBDDBBF07EA460958BA)
    

#### 示例代码

-   [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
