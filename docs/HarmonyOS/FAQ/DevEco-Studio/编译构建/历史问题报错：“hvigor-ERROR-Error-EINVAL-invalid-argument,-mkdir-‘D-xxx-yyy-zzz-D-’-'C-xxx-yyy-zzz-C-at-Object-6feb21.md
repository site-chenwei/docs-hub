---
title: "历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\\yyy\\zzz\\D:’/ 'C:xxx\\yyy\\zzz\\C:at Object.mkdirSync (node:fs:1391:3)”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-190"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\\yyy\\zzz\\D:’/ 'C:xxx\\yyy\\zzz\\C:at Object.mkdirSync (node:fs:1391:3)”"
captured_at: "2026-04-17T02:03:23.434Z"
---

# 历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\\yyy\\zzz\\D:’/ 'C:xxx\\yyy\\zzz\\C:at Object.mkdirSync (node:fs:1391:3)”

**问题现象**

构建报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\\yyy\\zzz\\D:’”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/F-m8Ouf_RU-4Z-RwWI-kFw/zh-cn_image_0000002433194024.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=62C6036BE3C31D1A21A6AABA1805C10740B7ACAF0E9D3717620355F3F41DF672)

**常见错误场景**

工程A通过引用外部模块的方式使用了工程B中的har模块，在工程B中执行ohpm后，在工程A中没有重新执行ohpm install直接编译（或者调试），导致编译报错。

**问题原因**

ohpm远程第三方包安装后，软连接指向的路径为非本工程路径（是由于被其他工程篡改），编译时会出现预期之外的错误。注：能以非本工程路径存在的依赖仅为本地模块，参考官网工程外模块的使用方式）

**解决措施**

1.**在问题工程中重新执行ohpm install**，或者sync。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/05T9XLWUQMSqceSc_2jBxQ/zh-cn_image_0000002433353864.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=FD9C1788D06EB4D04CDBF67D212F1F7861DC4B3857680525A548223A7E1D08A9 "点击放大")

2.使用build菜单先进行构建，再调试运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/4iIxnHuITcGMJ6lbxlkZBw/zh-cn_image_0000002466912421.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=A7A8800DE38AE5CC80EC7CC10C2F8131328E444CA4A880298486E1D90B5F641D "点击放大")
