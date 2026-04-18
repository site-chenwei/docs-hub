---
title: "DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-14"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "代码编辑"
  - "DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误"
captured_at: "2026-04-17T02:03:20.795Z"
---

# DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi\_init.cpp file and try again. ”错误

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/9Lk210CNSkCfKbcTW0GIhg/zh-cn_image_0000002229604349.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=7D7F20814D7C434FD3C2C95D8545E16D714F9D5A91AA56EFDA320B33E2BA7648)

**解决措施**

检查napi\_init.cpp文件的Init函数中是否初始化了napi\_property\_descriptor变量。没有初始化请添加napi\_property\_descriptor desc\[\] = {}; 然后重新生成NAPI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/L8FAv4DYR2CLrgIwklfv8g/zh-cn_image_0000002194318564.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=86EDE85019D536E5FECEECBE804C12A75CFF2A800DADDC3613D7F98B842DF5E5)
