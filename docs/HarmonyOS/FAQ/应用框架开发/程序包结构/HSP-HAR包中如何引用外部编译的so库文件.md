---
title: "HSP/HAR包中如何引用外部编译的so库文件"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-6"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序包结构"
  - "HSP/HAR包中如何引用外部编译的so库文件"
captured_at: "2026-04-17T02:02:57.902Z"
---

# HSP/HAR包中如何引用外部编译的so库文件

1.  libxxx.so库文件放入HAR或HSP的libs/arm64-v8a目录。设备类型不同时，需添加对应子目录。新版的arm64为libs/arm64-v8a，老版的arm64为libs/armeabi-v7a，x86模拟器为libs/x86\_64。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/A1T8bmuXQtuq2VzKkiA6sQ/zh-cn_image_0000002194158696.png?HW-CC-KV=V1&HW-CC-Date=20260417T020259Z&HW-CC-Expire=86400&HW-CC-Sign=79F286270F0A3B002C059FB58332E42B28468E23A0CC33EE51787199BADE047F "点击放大")
    
2.  在src/main/cpp/CMakeLists.txt文件中链接so库文件。例如：target\_link\_libraries(entry PUBLIC libxxx)
