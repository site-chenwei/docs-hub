---
title: "EGL绘制是否支持多线程？如何在多线程的场景下同时操作一块buffer进行图形绘制"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-6"
menu_path:
  - "FAQ"
  - "图形开发"
  - "2D图形（ArkGraphics 2D）"
  - "EGL绘制是否支持多线程？如何在多线程的场景下同时操作一块buffer进行图形绘制"
captured_at: "2026-04-17T02:03:19.786Z"
---

# EGL绘制是否支持多线程？如何在多线程的场景下同时操作一块buffer进行图形绘制

-   支持多线程，可以通过每个线程各自产生一块纹理，再将这些纹理合成到一块buffer。
-   可以使用sharedContext，另外绘制操作可通过调用OpenGL实现。
-   创建ShareContext的代码如下：
    
    void CreateShareEglContext() 
    {
      if (renderContext == nullptr) { // RenderContext is the main thread context 
        RS\_LOGE("renderContext\_ is nullptr");
        return;
      }
      eglShareContext = renderContext->CreateShareContext(); // Create share context 
      if (eglShareContext == EGL\_NO\_CONTEXT) {
        RS\_LOGE("eglShareContext is EGL\_NO\_CONTEXT");
        return;
      }
      if (!eglMakeCurrent(renderContext->GetEGLDisplay(), EGL\_NO\_SURFACE, EGL\_NO\_SURFACE, eglShareContext)) {
        RS\_LOGE("eglMakeCurrent failed");
        return;
      }
    }
