---
title: "使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_ALLOC。"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-10"
menu_path:
  - "FAQ"
  - "图形开发"
  - "2D图形（ArkGraphics 2D）"
  - "使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_ALLOC。"
captured_at: "2026-04-17T02:03:19.851Z"
---

# 使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL\_BAD\_ALLOC。

编码器通过 OH\_VideoEncoder\_GetSurface(encoder\_, &NativeWindow) 获取 NativeWindow，使用该 NativeWindow 创建 Encoder 的 EGLSurface 来接收 OpenGL 的纹理数据。若未调用 OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_BUFFER\_GEOMETRY, height, width) 设置 buffer 大小，在调用 eglSwapBuffers API 时会报错。
