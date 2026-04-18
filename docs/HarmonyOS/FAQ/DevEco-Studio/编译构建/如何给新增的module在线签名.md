---
title: "如何给新增的module在线签名"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-52"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何给新增的module在线签名"
captured_at: "2026-04-17T02:03:21.710Z"
---

# 如何给新增的module在线签名

操作步骤：

1.  连接真机设备，确保[DevEco Studio与真机设备已连接](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device)，真机连接成功后如下图所示：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/xNqiI1YER2eSZWnzdRNQDg/zh-cn_image_0000002229604037.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=70933B0119A663F36504466EA7BE8FE19DCCC82A30AEA05821D4C30C4A56F53D)
    
2.  进入 File > Project Structure... > Project > Signing Configs 界面，勾选“Automatically generate signature”。如果是 HarmonyOS 工程，还需勾选“Support HarmonyOS”。若未登录，请先单击 Sign In 进行登录，然后完成签名。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/H0R5Ydj9QeGU87evD4huFA/zh-cn_image_0000002229758513.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=395B0758B44766614A999C9B0E11C7B4B3BF1E279324237B6FFA5D3D4CB98A43 "点击放大")
    
    签名完成后，如下图所示：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/k8tYaMksRyyzS5SNoMkXdA/zh-cn_image_0000002194318264.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=88B39C72EA86ACE2737265FA1FDE5EC074B8B0B9EA5FB258012B3C380DB394FC "点击放大")
