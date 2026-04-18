---
title: "使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_SURFACE （300d）。日志显示：QEGLPlatformContext: eglSwapBuffers failed: 300d。"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-9"
menu_path:
  - "FAQ"
  - "图形开发"
  - "2D图形（ArkGraphics 2D）"
  - "使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_SURFACE （300d）。日志显示：QEGLPlatformContext: eglSwapBuffers failed: 300d。"
captured_at: "2026-04-17T02:03:19.796Z"
---

# 使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL\_BAD\_SURFACE （300d）。日志显示：QEGLPlatformContext: eglSwapBuffers failed: 300d。

如果surface不是EGL绘图表面，系统会返回EGL\_BAD\_SURFACE错误。建议检查eglCreateWindowSurface、eglCreatePixmapSurface和eglCreatePbufferSurface的参数设置。
