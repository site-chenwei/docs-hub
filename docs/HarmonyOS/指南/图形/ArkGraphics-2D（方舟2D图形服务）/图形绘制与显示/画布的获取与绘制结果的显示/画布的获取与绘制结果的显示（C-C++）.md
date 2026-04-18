---
title: "画布的获取与绘制结果的显示（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "图形绘制与显示"
  - "画布的获取与绘制结果的显示"
  - "画布的获取与绘制结果的显示（C/C++）"
captured_at: "2026-04-17T01:36:08.524Z"
---

# 画布的获取与绘制结果的显示（C/C++）

#### 场景介绍

Canvas即画布，提供绘制基本图形的能力，用于在屏幕上绘制图形和处理图形。开发者可以通过Canvas实现自定义的绘图效果，增强应用的用户体验。

Canvas是图形绘制的核心，本章中提到的所有绘制操作（包括基本图形的绘制、文字的绘制、图片的绘制、图形变换等）都是基于Canvas的。

目前C/C++有两种获取Canvas的方式：获取可直接上屏显示的Canvas、获取离屏的Canvas，前者在调用绘制接口之后无需进行额外的操作即可完成绘制结果的上屏显示，而后者需要依靠已有的显示手段来显示绘制结果。

#### 接口说明

创建Canvas常用接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h)。

| 接口 | 描述 |
| :-- | :-- |
| OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreate (void) | 用于创建一个画布对象。 |
| void OH\_Drawing\_CanvasBind (OH\_Drawing\_Canvas\*, OH\_Drawing\_Bitmap\*) | 用于将一个位图对象绑定到画布中，使得画布绘制的内容输出到位图中。 |
| OH\_Drawing\_Canvas\* OH\_Drawing\_SurfaceGetCanvas (OH\_Drawing\_Surface \*) | 通过surface对象获取画布对象。 |

#### 获取可直接显示的Canvas画布

通过XComponent获取可直接显示的Canvas画布。

1.  添加链接库。
    
    在Native工程的src/main/cpp/CMakeLists.txt，添加如下链接库：
    
    ```
    // CMakeLists.txt
    target_link_libraries(entry PUBLIC libnative_drawing.so)
    ```
    
2.  导入依赖的相关头文件。
    
    #include <native\_drawing/drawing\_canvas.h>
    
    #include <native\_drawing/drawing\_surface.h>
    
3.  从XComponent对应的NativeWindow中获取BufferHandle对象。NativeWindow相关的API请参考[\_native\_window](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow)。
    
    // 通过 OH\_NativeWindow\_NativeWindowRequestBuffer 获取 OHNativeWindowBuffer 实例
    int ret = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow\_, &buffer\_, &fenceFd\_);
    SAMPLE\_LOGI("request buffer ret = %{public}d", ret);
    // 通过 OH\_NativeWindow\_GetBufferHandleFromNative 获取 buffer 的 handle
    bufferHandle\_ = OH\_NativeWindow\_GetBufferHandleFromNative(buffer\_);
    
4.  从BufferHandle中获取对应的内存地址。
    
    // 使用系统mmap接口拿到bufferHandle的内存虚拟地址
    mappedAddr\_ = static\_cast<uint32\_t \*>(
        mmap(bufferHandle\_->virAddr, bufferHandle\_->size, PROT\_READ | PROT\_WRITE, MAP\_SHARED, bufferHandle\_->fd, 0));
    if (mappedAddr\_ == MAP\_FAILED) {
        SAMPLE\_LOGE("mmap failed");
    }
    
5.  创建窗口画布。
    
    // 创建一个bitmap对象
    cScreenBitmap\_ = OH\_Drawing\_BitmapCreate();
    // 定义bitmap的像素格式
    OH\_Drawing\_BitmapFormat cFormat{COLOR\_FORMAT\_RGBA\_8888, ALPHA\_FORMAT\_OPAQUE};
    // 构造对应格式的bitmap
    OH\_Drawing\_BitmapBuild(cScreenBitmap\_, width, height\_, &cFormat);
    
    // 创建一个canvas对象
    cScreenCanvas\_ = OH\_Drawing\_CanvasCreate();
    // 将画布与bitmap绑定，画布画的内容会输出到绑定的bitmap内存中
    OH\_Drawing\_CanvasBind(cScreenCanvas\_, cScreenBitmap\_);
    
6.  利用上一步中得到的Canvas进行自定义的绘制操作，即本章下文中的内容。
    
7.  利用XComponent完成显示。
    
    // 设置刷新区域，如果Region中的Rect为nullptr,或者rectNumber为0，则认为OHNativeWindowBuffer全部有内容更改。
    Region region{nullptr, 0};
    // 通过OH\_NativeWindow\_NativeWindowFlushBuffer 提交给消费者使用，例如：显示在屏幕上。
    OH\_NativeWindow\_NativeWindowFlushBuffer(nativeWindow\_, buffer\_, fenceFd\_, region);
    

#### 离屏Canvas画布的获取与显示

目前有两种创建离屏Canvas的方式：创建CPU后端Canvas、创建GPU后端Canvas，这两种Canvas都需要依靠XComponent来完成绘制结果的上屏显示。由于历史原因，早期的Canvas都是CPU后端Canvas。目前已经支持GPU后端Canvas，GPU的并行计算能力更强，更适合图形绘制。但GPU后端Canvas对部分场景的支持还有欠缺，比如复杂的路径，对于简短文字的绘制性能也比不上CPU后端Canvas。

#### \[h2\]CPU后端Canvas的创建与显示

目前C/C++接口的绘制需要依赖于NativeWindow，CPU后端Canvas需要先离屏绘制，生成位图或像素图（从API Version 20开始支持），再借助XComponent上屏。

方式一：通过绑定位图（Bitmap）的方式创建Canvas。

1.  导入依赖的相关头文件。
    
    #include <native\_drawing/drawing\_bitmap.h>
    // ...
    #include <native\_drawing/drawing\_canvas.h>
    
2.  创建基于CPU的Canvas。需要通过OH\_Drawing\_BitmapCreate()接口创建一个位图对象（具体可参考[图片绘制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-c)），并通过OH\_Drawing\_CanvasBind()接口将位图绑定到Canvas中，从而使得Canvas绘制的内容可以输出到位图中。
    
    // 创建一个离屏位图对象
    cOffScreenBitmap\_ = OH\_Drawing\_BitmapCreate();
    // 设置位图属性
    OH\_Drawing\_BitmapFormat cFormat{COLOR\_FORMAT\_RGBA\_8888, ALPHA\_FORMAT\_PREMUL};
    // 设置位图长宽（按需设置）
    uint32\_t width = 800;
    uint32\_t height = 800;
    // 初始化位图
    OH\_Drawing\_BitmapBuild(cOffScreenBitmap\_, width, height, &cFormat);
    // 创建一个离屏Canvas对象
    cCPUCanvas\_ = OH\_Drawing\_CanvasCreate();
    // 将离屏Canvas与离屏bitmap绑定，离屏Canvas绘制的内容会输出到绑定的离屏bitmap内存中
    OH\_Drawing\_CanvasBind(cCPUCanvas\_, cOffScreenBitmap\_);
    
    如果需要将背景设置为白色，需要执行以下步骤：
    
    // 将背景设置为白色
    OH\_Drawing\_CanvasClear(cCPUCanvas\_, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MAX, 0xFF));
    
3.  将上一步中创建的位图绘制到[窗口画布](#获取可直接显示的canvas画布)上。
    
    // 将离屏bitmap中的内容绘制到屏幕画布，实现上屏操作
    OH\_Drawing\_CanvasDrawBitmap(cScreenCanvas\_, cOffScreenBitmap\_, 0, 0);
    

方式二：通过像素图（PixelMap）创建Canvas。从API Version 20开始，支持使用此种方式创建Canvas。

像素图是系统中用来表示图片的统一的数据结构，相比于drawing模块中提供的位图，像素图具备通用性，并且能够更好地发挥系统的能力。

1.  添加链接库。
    
    在Native工程的src/main/cpp/CMakeLists.txt，添加如下链接库：
    
    ```
    // CMakeLists.txt
    target_link_libraries(entry PUBLIC libhilog_ndk.z.so libpixelmap.so)
    ```
    
2.  导入依赖的相关头文件。
    
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
    #include <native\_drawing/drawing\_pixel\_map.h>
    
3.  需要通过OH\_Drawing\_PixelMapGetFromOhPixelMapNative()接口创建一个像素图对象（具体可参考[图片绘制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-c)），并通过OH\_Drawing\_CanvasCreateWithPixelMap()接口借助像素图对象创建Canvas。
    
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
    OH\_Drawing\_PixelMap \*pixelMap = OH\_Drawing\_PixelMapGetFromOhPixelMapNative(pixelMapNative);
    // PixelMap中像素的截取区域
    OH\_Drawing\_Rect \*src = OH\_Drawing\_RectCreate(0, 0, 600, 400);
    // 画布中显示的区域
    OH\_Drawing\_Rect \*dst = OH\_Drawing\_RectCreate(value200\_, value200\_, value800\_, value600\_);
    // 采样选项对象
    OH\_Drawing\_SamplingOptions\* samplingOptions = OH\_Drawing\_SamplingOptionsCreate(
        OH\_Drawing\_FilterMode::FILTER\_MODE\_LINEAR, OH\_Drawing\_MipmapMode::MIPMAP\_MODE\_LINEAR);
    // 绘制PixelMap
    OH\_Drawing\_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, samplingOptions);
    OH\_PixelmapNative\_Release(pixelMapNative);
    delete\[\] pixels;
    
    如果需要将背景设置为白色，需要执行以下步骤：
    
    ```
    OH_Drawing_CanvasClear(pixelmapCanvas, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0xFF, 0xFF));
    ```
    
4.  将上一步中创建的像素图绘制到[窗口画布](#获取可直接显示的canvas画布)上。
    
    // PixelMap中像素的截取区域
    OH\_Drawing\_Rect \*src = OH\_Drawing\_RectCreate(0, 0, 600, 400);
    // 画布中显示的区域
    OH\_Drawing\_Rect \*dst = OH\_Drawing\_RectCreate(value200\_, value200\_, value800\_, value600\_);
    // 采样选项对象
    OH\_Drawing\_SamplingOptions\* samplingOptions = OH\_Drawing\_SamplingOptionsCreate(
        OH\_Drawing\_FilterMode::FILTER\_MODE\_LINEAR, OH\_Drawing\_MipmapMode::MIPMAP\_MODE\_LINEAR);
    // 绘制PixelMap
    OH\_Drawing\_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, samplingOptions);
    

#### \[h2\]GPU后端Canvas的创建与显示

GPU后端Canvas指画布是基于GPU进行绘制的，GPU的并行计算能力优于CPU，适用于绘制图片或区域相对大的场景，但目前GPU后端的Canvas针对绘制复杂路径的能力还有欠缺。同CPU后端Canvas，目前C/C++接口的绘制需要依赖于XComponent，GPU后端Canvas需要先离屏绘制再借助XComponent上屏。

1.  当前创建GPU后端的Canvas依赖EGL的能力，需要在CMakeLists.txt中添加EGL的动态依赖库。
    
    ```
    // CMakeLists.txt
    libEGL.so
    ```
    
2.  导入依赖的头文件。
    
    #include <EGL/egl.h>
    #include <EGL/eglext.h>
    
    #include <native\_drawing/drawing\_gpu\_context.h>
    #include <native\_drawing/drawing\_surface.h>
    
3.  初始化EGL上下文。
    
    初始化上下文相关参数:
    
    EGLDisplay EGLDisplay\_ = EGL\_NO\_DISPLAY;
    EGLConfig EGLConfig\_ = nullptr;
    EGLContext EGLContext\_ = EGL\_NO\_CONTEXT;
    EGLSurface EGLSurface\_ = nullptr;
    
    初始化上下文相关配置：
    
    EGLConfig getConfig(int version, EGLDisplay eglDisplay)
    {
        int attribList\[\] = {EGL\_SURFACE\_TYPE,
                            EGL\_WINDOW\_BIT,
                            EGL\_RED\_SIZE,
                            8,
                            EGL\_GREEN\_SIZE,
                            8,
                            EGL\_BLUE\_SIZE,
                            8,
                            EGL\_ALPHA\_SIZE,
                            8,
                            EGL\_RENDERABLE\_TYPE,
                            EGL\_OPENGL\_ES2\_BIT,
                            EGL\_NONE};
        EGLConfig configs = NULL;
        int configsNum;
    
        if (!eglChooseConfig(eglDisplay, attribList, &configs, 1, &configsNum)) {
            SAMPLE\_LOGE("eglChooseConfig ERROR");
            return NULL;
        }
    
        return configs;
    }
    
    int32\_t SampleGraphics::InitializeEglContext()
    {
        EGLDisplay\_ = eglGetDisplay(EGL\_DEFAULT\_DISPLAY);
        if (EGLDisplay\_ == EGL\_NO\_DISPLAY) {
            SAMPLE\_LOGE("unable to get EGL display.");
            return -1;
        }
    
        EGLint eglMajVers;
        EGLint eglMinVers;
        if (!eglInitialize(EGLDisplay\_, &eglMajVers, &eglMinVers)) {
            EGLDisplay\_ = EGL\_NO\_DISPLAY;
            SAMPLE\_LOGE("unable to initialize display");
            return -1;
        }
    
        int version = 3;
        EGLConfig\_ = getConfig(version, EGLDisplay\_);
        if (EGLConfig\_ == nullptr) {
            SAMPLE\_LOGE("GLContextInit config ERROR");
            return -1;
        }
    
        /\* Create EGLContext from \*/
        int attribList\[\] = {EGL\_CONTEXT\_CLIENT\_VERSION, 2, EGL\_NONE}; // 2 size
    
        EGLContext\_ = eglCreateContext(EGLDisplay\_, EGLConfig\_, EGL\_NO\_CONTEXT, attribList);
    
        EGLint attribs\[\] = {EGL\_WIDTH, 1, EGL\_HEIGHT, 1, EGL\_NONE};
        EGLSurface\_ = eglCreatePbufferSurface(EGLDisplay\_, EGLConfig\_, attribs);
        if (!eglMakeCurrent(EGLDisplay\_, EGLSurface\_, EGLSurface\_, EGLContext\_)) {
            SAMPLE\_LOGE("eglMakeCurrent error = %{public}d", eglGetError());
            return -1;
        }
    
        SAMPLE\_LOGE("Init success.");
        return 0;
    }
    
4.  创建GPU后端Canvas。GPU后端Canvas需要借助Surface对象来获取，需先创建surface，surface的API请参考[drawing\_surface.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-surface-h)。通过OH\_Drawing\_GpuContextCreateFromGL接口创建绘图上下文，再将这个上下文作为参数创建surface，最后通过OH\_Drawing\_SurfaceGetCanvas接口从surface中获取到canvas。
    
    // 设置宽高（按需设定）
    int32\_t cWidth = 800;
    int32\_t cHeight = 800;
    // 设置图像，包括宽度、高度、颜色格式和透明度格式
    OH\_Drawing\_Image\_Info imageInfo = {cWidth, cHeight, COLOR\_FORMAT\_RGBA\_8888, ALPHA\_FORMAT\_PREMUL};
    // GPU上下文的选项
    OH\_Drawing\_GpuContextOptions options{true};
        
    // 创建一个使用OpenGL（GL）作为其GPU后端的绘图上下文
    OH\_Drawing\_GpuContext \*gpuContext = OH\_Drawing\_GpuContextCreateFromGL(options);
    // 创建surface对象
    OH\_Drawing\_Surface \*surface = OH\_Drawing\_SurfaceCreateFromGpuContext(gpuContext, true, imageInfo);
    // 创建一个canvas对象
    cGPUCanvas\_ = OH\_Drawing\_SurfaceGetCanvas(surface);
    
    如果需要将背景设置为白色，需要执行以下步骤：
    
    // 将背景设置为白色
    OH\_Drawing\_CanvasClear(cGPUCanvas\_, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MAX, 0xFF));
    
5.  将上一步中的绘制结果拷贝到[窗口画布](#获取可直接显示的canvas画布)上。
    
    void\* dstPixels = malloc(cWidth \* cHeight \* RGBA\_SIZE); // 4 for rgba
    OH\_Drawing\_CanvasReadPixels(cGPUCanvas\_, &imageInfo, dstPixels, RGBA\_SIZE \* cWidth, 0, 0);
    OH\_Drawing\_Bitmap\* cOffScreenBitmap\_ = OH\_Drawing\_BitmapCreateFromPixels(&imageInfo, dstPixels,
        RGBA\_SIZE \* cWidth);
    OH\_Drawing\_CanvasDrawBitmap(cScreenCanvas\_, cOffScreenBitmap\_, 0, 0);
    
6.  使用完之后需要将EGL上下文销毁。
    
    void SampleGraphics::DeInitializeEglContext()
    {
        EGLBoolean ret = eglDestroySurface(EGLDisplay\_, EGLSurface\_);
        if (!ret) {
            SAMPLE\_LOGE("eglDestroySurface failure.");
        }
    
        ret = eglDestroyContext(EGLDisplay\_, EGLContext\_);
        if (!ret) {
            SAMPLE\_LOGE("eglDestroyContext failure.");
        }
    
        ret = eglTerminate(EGLDisplay\_);
        if (!ret) {
            SAMPLE\_LOGE("eglTerminate failure.");
        }
    
        EGLSurface\_ = NULL;
        EGLContext\_ = NULL;
        EGLDisplay\_ = NULL;
    }
    

#### 示例代码

-   [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
