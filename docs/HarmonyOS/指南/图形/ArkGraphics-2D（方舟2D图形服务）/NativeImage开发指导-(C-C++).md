---
title: "NativeImage开发指导 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-image-guidelines"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "NativeImage开发指导 (C/C++)"
captured_at: "2026-04-17T01:36:09.078Z"
---

# NativeImage开发指导 (C/C++)

#### 场景介绍

NativeImage是提供**Surface与OpenGL外部纹理相互绑定**的模块，表示图形队列的消费者端。开发者可以通过NativeImage接口接收和使用Buffer，并将Buffer关联输出到绑定的OpenGL外部纹理。

NativeImage常见的开发场景如下：

-   通过NativeImage提供的Native API接口创建NativeImage实例作为消费者端，获取与该实例对应的NativeWindow作为生产者端。NativeWindow相关接口可用于填充Buffer内容并提交，NativeImage将Buffer内容更新到OpenGL外部纹理上。本模块需要配合NativeWindow、NativeBuffer、EGL、GLES3模块一起使用。

#### 接口说明

| 接口名 | 描述 |
| :-- | :-- |
| OH\_NativeImage\_Create (uint32\_t textureId, uint32\_t textureTarget) | 创建一个OH\_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联。本接口需要与OH\_NativeImage\_Destroy接口配合使用，否则会存在内存泄露。 |
| OH\_NativeImage\_AcquireNativeWindow (OH\_NativeImage \*image) | 获取与OH\_NativeImage相关联的OHNativeWindow指针，该OHNativeWindow在调用OH\_NativeImage\_Destroy时会将其释放，不需要调用OH\_NativeWindow\_DestroyNativeWindow释放，否则会出现访问已释放内存错误，可能会导致崩溃。 |
| OH\_NativeImage\_AttachContext (OH\_NativeImage \*image, uint32\_t textureId) | 将OH\_NativeImage实例附加到当前OpenGL ES上下文，且该OpenGL ES纹理会绑定到 GL\_TEXTURE\_EXTERNAL\_OES，并通过OH\_NativeImage进行更新。 |
| OH\_NativeImage\_DetachContext (OH\_NativeImage \*image) | 将OH\_NativeImage实例从当前OpenGL ES上下文分离。 |
| OH\_NativeImage\_UpdateSurfaceImage (OH\_NativeImage \*image) | 通过OH\_NativeImage获取最新帧更新相关联的OpenGL ES纹理。 |
| OH\_NativeImage\_GetTimestamp (OH\_NativeImage \*image) | 获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的相关时间戳。 |
| OH\_NativeImage\_GetTransformMatrixV2 (OH\_NativeImage \*image, float matrix\[16\]) | 获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的变化矩阵。 |
| OH\_NativeImage\_Destroy (OH\_NativeImage \*\*image) | 销毁通过OH\_NativeImage\_Create创建的OH\_NativeImage实例，销毁后该OH\_NativeImage指针会被赋值为空。 |

详细的接口说明请参考[native\_image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativeimage)。

#### 开发步骤

以下步骤描述了如何使用NativeImage提供的Native API接口，创建OH\_NativeImage实例作为消费者端，将数据内容更新到OpenGL外部纹理上。

**添加动态链接库**

CMakeLists.txt中添加以下库文件。

```txt
libEGL.so
libGLESv3.so
libnative_image.so
libnative_window.so
libnative_buffer.so
```

**头文件**

```
#include <iostream>
#include <string>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <GLES3/gl3.h>
#include <GLES2/gl2ext.h>
#include <sys/mman.h>
#include <native_image/native_image.h>
#include <native_window/external_window.h>
#include <native_buffer/native_buffer.h>
```

1.  **初始化EGL环境**。
    
    这里提供初始化EGL环境的代码示例。XComponent模块的详细使用方法，请参阅[XComponent开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。
    
    bool ImageRender::InitEGL(EGLNativeWindowType window, uint64\_t width, uint64\_t height)
    {
        window\_ = window;
        width\_ = width;
        height\_ = height;
    
        if (!InitializeEGLDisplay() || !ChooseEGLConfig() || !CreateEGLContext() || !CreateEGLSurface()) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to initialize EGL");
            return false;
        }
    
        if (!MakeCurrentContext()) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to make EGL context current");
            return false;
        }
    
        if (!CompileAndLinkShaders()) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to compile and link shaders");
            return false;
        }
    
        UpdateViewport();
    
        return true;
    }
    
    // ...
    bool ImageRender::InitializeEGLDisplay()
    {
        display\_ = eglGetDisplay(EGL\_DEFAULT\_DISPLAY);
        if (display\_ == EGL\_NO\_DISPLAY) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to get EGL display");
            return false;
        }
    
        if (!eglInitialize(display\_, nullptr, nullptr)) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to initialize EGL");
            return false;
        }
    
        return true;
    }
    
    bool ImageRender::ChooseEGLConfig()
    {
        const EGLint attribs\[\] = {
            EGL\_RENDERABLE\_TYPE, EGL\_OPENGL\_ES2\_BIT,
            EGL\_SURFACE\_TYPE, EGL\_WINDOW\_BIT,
            EGL\_RED\_SIZE, 8,
            EGL\_GREEN\_SIZE, 8,
            EGL\_BLUE\_SIZE, 8,
            EGL\_ALPHA\_SIZE, 8,
            EGL\_NONE
        };
    
        EGLint numConfigs;
        if (!eglChooseConfig(display\_, attribs, &config\_, 1, &numConfigs) || numConfigs == 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to choose EGL config");
            return false;
        }
        return true;
    }
    
    bool ImageRender::CreateEGLContext()
    {
        const EGLint contextAttribs\[\] = { EGL\_CONTEXT\_CLIENT\_VERSION, 2, EGL\_NONE };
        context\_ = eglCreateContext(display\_, config\_, EGL\_NO\_CONTEXT, contextAttribs);
        if (context\_ == EGL\_NO\_CONTEXT) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to create EGL context");
            return false;
        }
        return true;
    }
    
    bool ImageRender::CreateEGLSurface()
    {
        surface\_ = eglCreateWindowSurface(display\_, config\_, window\_, nullptr);
        if (surface\_ == EGL\_NO\_SURFACE) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to create EGL surface");
            return false;
        }
        return true;
    }
    
    bool ImageRender::MakeCurrentContext()
    {
        if (!eglMakeCurrent(display\_, surface\_, surface\_, context\_)) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to make EGL context current");
            return false;
        }
        return true;
    }
    
    void ImageRender::UpdateViewport()
    {
        glViewport(0, 0, static\_cast<GLsizei>(width\_), static\_cast<GLsizei>(height\_));
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "ImageRender",
                     "Viewport updated to %{public}llu x %{public}llu", width\_, height\_);
    }
    
    bool ImageRender::CompileAndLinkShaders()
    {
        GLuint vertexShader = CompileShader(GL\_VERTEX\_SHADER, g\_vertexShaderSource);
        if (vertexShader == 0) {
            return false;
        }
    
        GLuint fragmentShader = CompileShader(GL\_FRAGMENT\_SHADER, g\_fragmentShaderSource);
        if (fragmentShader == 0) {
            glDeleteShader(vertexShader);
            return false;
        }
    
        shaderProgram\_ = glCreateProgram();
        glAttachShader(shaderProgram\_, vertexShader);
        glAttachShader(shaderProgram\_, fragmentShader);
        glLinkProgram(shaderProgram\_);
    
        GLint linked;
        glGetProgramiv(shaderProgram\_, GL\_LINK\_STATUS, &linked);
        if (!linked) {
            PrintProgramLinkError(shaderProgram\_);
            glDeleteProgram(shaderProgram\_);
            glDeleteShader(vertexShader);
            glDeleteShader(fragmentShader);
            return false;
        }
    
        glUseProgram(shaderProgram\_);
    
        positionAttrib\_ = glGetAttribLocation(shaderProgram\_, "aPosition");
        texCoordAttrib\_ = glGetAttribLocation(shaderProgram\_, "aTexCoord");
        textureUniform\_ = glGetUniformLocation(shaderProgram\_, "uTexture");
    
        glDeleteShader(vertexShader);
        glDeleteShader(fragmentShader);
    
        return true;
    }
    
    void ImageRender::PrintProgramLinkError(GLuint program)
    {
        GLint infoLen = 0;
        glGetProgramiv(program, GL\_INFO\_LOG\_LENGTH, &infoLen);
        if (infoLen > 1) {
            std::unique\_ptr<char\[\]> infoLog = std::make\_unique<char\[\]>(infoLen);
            glGetProgramInfoLog(program, infoLen, nullptr, infoLog.get());
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                         "ImageRender", "Error linking program: %{public}s", infoLog.get());
        }
    }
    
2.  **创建OH\_NativeImage实例**。
    
    glGenTextures(1, &nativeImageTexId\_);
    // ...
    nativeImage\_ = OH\_NativeImage\_Create(nativeImageTexId\_, GL\_TEXTURE\_EXTERNAL\_OES);
    
3.  **获取对应的数据生产者端NativeWindow**。
    
    nativeWindow\_ = OH\_NativeImage\_AcquireNativeWindow(image);
    
4.  **设置NativeWindow的宽高**。
    
    int32\_t result = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow\_, SET\_BUFFER\_GEOMETRY,
        static\_cast<int32\_t>(width\_), static\_cast<int32\_t>(height\_));
    if (result != SUCCESS) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "OHNativeRender", "Failed to set buffer geometry.");
        return false;
    }
    
5.  **将生产的内容写入OHNativeWindowBuffer**。
    
    1.  从NativeWindow中获取OHNativeWindowBuffer。
        
        OHNativeWindowBuffer \*buffer = nullptr;
        int releaseFenceFd = INVALID\_FD;
        int32\_t result = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow\_, &buffer, &releaseFenceFd);
        if (result != SUCCESS || buffer == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                         "OHNativeRender", "Failed to request buffer, ret : %{public}d.", result);
            return;
        }
        // ...
        BufferHandle \*handle = OH\_NativeWindow\_GetBufferHandleFromNative(buffer);
        
    2.  将生产的内容写入OHNativeWindowBuffer。
        
        // 使用 mmap 获取虚拟地址
        void \*mappedAddr = mmap(nullptr, handle->size, PROT\_READ | PROT\_WRITE, MAP\_SHARED, handle->fd, 0);
        if (mappedAddr == MAP\_FAILED) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "OHNativeRender", "Failed to mmap buffer.");
            return;
        }
        
        // 获取像素指针
        uint32\_t \*pixel = static\_cast<uint32\_t \*>(mappedAddr);
        
        // 调用封装的函数来绘制渐变
        DrawGradient(pixel, handle->stride / BYTES\_PER\_PIXEL, height\_);
        
        // 解除内存映射
        result = munmap(mappedAddr, handle->size);
        if (result == FAILURE) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "OHNativeRender", "Failed to munmap buffer.");
        }
        // ...
        void OHNativeRender::DrawGradient(uint32\_t\* pixel, uint64\_t width, uint64\_t height)
        {
            static double time = 0.0;
            time += ANIMATION\_SPEED\_INCREMENT;
            double offset = (sin(time) + MAX\_INTENSITY) / INTENSITY\_MULTIPLIER;
        
            // 箭头参数
            const int arrowSize = std::min(width, height) / ARROW\_SIZE\_DIVISOR;
            const int arrowX = width / ARROW\_SIZE\_DIVISOR;
            const int arrowY = height / ARROW\_SIZE\_DIVISOR;
            const int stemWidth = arrowSize / STEM\_WIDTH\_DIVISOR;
            const int headWidth = arrowSize / HEAD\_WIDTH\_DIVISOR;
            const int headLength = arrowSize / HEAD\_LENGTH\_DIVISOR;
            const int stemStart = arrowX - arrowSize / ARROW\_SIZE\_DIVISOR;
            const int stemEnd = arrowX + arrowSize / ARROW\_SIZE\_DIVISOR - headLength;
        
            for (uint64\_t y = 0; y < height; y++) {
                for (uint64\_t x = 0; x < width; x++) {
                    double normalizedX = static\_cast<double>(x) / static\_cast<double>(width - 1);
                    bool isArrow = false;
        
                    if ((x >= stemStart && x <= stemEnd && y >= arrowY - stemWidth \* HEAD\_SLOPE\_MULTIPLIER &&
                        y <= arrowY + stemWidth \* HEAD\_SLOPE\_MULTIPLIER) || (x >= stemEnd && x <= stemEnd + headLength &&
                        fabs(static\_cast<int>(y - arrowY)) <= (headWidth \* HEAD\_SLOPE\_MULTIPLIER) \*
                        (1.0 - static\_cast<double>(x - stemEnd) / headLength))) {
                        isArrow = true;
                    }
        
                    uint8\_t red = static\_cast<uint8\_t>((1.0 - normalizedX) \* MAX\_COLOR\_VALUE);
                    uint8\_t blue = static\_cast<uint8\_t>(normalizedX \* MAX\_COLOR\_VALUE);
                    uint8\_t green = 0;
                    uint8\_t alpha = MAX\_COLOR\_VALUE;
                    if (isArrow) {
                        red = green = blue = MAX\_COLOR\_VALUE;
                    }
                    double intensity = fabs(normalizedX - offset);
                    intensity = MAX\_INTENSITY - std::min(INTENSITY\_MULTIPLIER \* intensity, INTENSITY\_LIMIT);
                    intensity = std::max(intensity, MIN\_INTENSITY);
        
                    red = static\_cast<uint8\_t>(red \* intensity);
                    green = static\_cast<uint8\_t>(green \* intensity);
                    blue = static\_cast<uint8\_t>(blue \* intensity);
        
                    \*pixel++ = (static\_cast<uint32\_t>(alpha) << ALPHA\_SHIFT) | (static\_cast<uint32\_t>(red) << RED\_SHIFT) |
                        (static\_cast<uint32\_t>(green) << GREEN\_SHIFT) | (static\_cast<uint32\_t>(blue) << BLUE\_SHIFT);
                }
            }
        }
        
    3.  将OHNativeWindowBuffer提交到NativeWindow。
        
        // 设置刷新区域
        Region region{nullptr, 0};
        // 提交给消费者
        result = OH\_NativeWindow\_NativeWindowFlushBuffer(nativeWindow\_, buffer, NO\_FENCE, region);
        if (result != SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                         "OHNativeRender", "Failed to flush buffer, result : %{public}d.", result);
        }
        
6.  **更新内容到OpenGL纹理**。
    
     int32\_t ret = OH\_NativeImage\_UpdateSurfaceImage(nativeImage\_);
     if (ret != 0) {
         OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderEngine",
                     "OH\_NativeImage\_UpdateSurfaceImage failed, ret: %{public}d, texId: %{public}u",
                     ret, nativeImageTexId\_);
         return;
     }
    
     UpdateTextureMatrix();
     if (imageRender\_) {
         imageRender\_->Render();
     } else {
         OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderEngine", "ImageRender is null");
     }
     // ...
    
    void RenderEngine::UpdateTextureMatrix()
    {
        float matrix\[16\];
        int32\_t ret = OH\_NativeImage\_GetTransformMatrixV2(nativeImage\_, matrix);
        if (ret != 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderEngine",
                         "OH\_NativeImage\_GetTransformMatrix failed, ret: %{public}d", ret);
            return;
        }
        imageRender\_->SetTransformMatrix(matrix);
    }
    
7.  **解绑OpenGL纹理，绑定到新的外部纹理上**。
    
    // 将OH\_NativeImage实例从当前OpenGL ES上下文分离
    OH\_NativeImage\_DetachContext(nativeImage\_);
    glGenTextures(1, &nativeImageTexId\_);
    glBindTexture(GL\_TEXTURE\_EXTERNAL\_OES, nativeImageTexId\_);
    // ...
    int ret = OH\_NativeImage\_AttachContext(nativeImage\_, nativeImageTexId\_);
    
8.  **OH\_NativeImage实例使用完需要销毁掉**。
    
    OH\_NativeImage\_Destroy(&nativeImage\_);
