---
title: "如何正确地在CMakeLists.txt文件中配置头文件搜索路径"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-43"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何正确地在CMakeLists.txt文件中配置头文件搜索路径"
captured_at: "2026-04-17T02:03:02.090Z"
---

# 如何正确地在CMakeLists.txt文件中配置头文件搜索路径

请按照以下示例进行配置：

**例1****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/rNCAn3_aRZqqaDDIie8cWQ/zh-cn_image_0000002199836868.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=1B10D9FCD8B88E344967ED867FBA5280FA5F5B82489626662275CA72E9FDA30A)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test.h'

**例2****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/PopBMFukTdeghJRw7hbq7Q/zh-cn_image_0000002234797125.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=89EC34FCDB1AC22353FB453A1552C2639714041E6A9EFF0A5DA062346B2CFC3A)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH})

cpp文件中引用头文件:

#include 'include/test/test.h'

**例3：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/98TLfumHRP2vCU3MFhdHSw/zh-cn_image_0000002234956969.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=5241651E225835665F01E42CB366BBA0D182B7A1A9DC32C1093009C85290DD62)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test/test.h'

**例4:**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/jz4dadQATRWxoqK-weCTtw/zh-cn_image_0000002199996680.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=7378AD9BB66D6CB0E9727C35A76D9F3A4A5A4B4A95300AD7F01D9E003A60027D)

CMakeLists.txt配置头文件搜索路径:

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include/test)

cpp文件中引用头文件:

#include 'test.h'
