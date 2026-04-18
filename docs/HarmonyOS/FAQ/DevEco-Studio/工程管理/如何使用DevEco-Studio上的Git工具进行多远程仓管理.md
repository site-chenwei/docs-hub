---
title: "如何使用DevEco Studio上的Git工具进行多远程仓管理"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-19"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "工程管理"
  - "如何使用DevEco Studio上的Git工具进行多远程仓管理"
captured_at: "2026-04-17T02:03:20.514Z"
---

# 如何使用DevEco Studio上的Git工具进行多远程仓管理

添加新的远程仓库：

1.  右击Remote以调出菜单。
2.  点击Manage Remotes，打开Git Remotes窗口。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/LPr5AoAUSrWauJqzHEpKXg/zh-cn_image_0000002194318352.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=6D7F22D1366D332AB4B1F5C67772521071132F2C14EBCF3525F872B24DFF1515)
    
3.  点击添加按钮。
4.  输入远程仓名称和URL，远程仓名称可自由命名。
5.  点击Define Remote窗口的OK按钮，在新弹出的窗口中输入域账号和密码。
6.  点击Git Remotes窗口的确定按钮。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/sddybng9QxGUoBjI0FC42g/zh-cn_image_0000002229604125.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=06DE6F44873A1D3761195D2F24950A190D21ED65F77DA9BA7A4467B25EF07167 "点击放大")
    
7.  点击拉取远程记录，新添加的远程仓库将在Remote子菜单中显示。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/W1RgSQI7TjOAB68kCleigQ/zh-cn_image_0000002229758613.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=97D69422B29FC0E46B2AB72C712A621EEE15C17A681EEFFE91E79B706C0B95A0)
    

Push提交：

Push提交和Push提交到远程仓库的过程相似。如需切换远程仓库，可单击下图中标记1的分支名；标记3表示以PR方式提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Ry_LCOwDTTyEzFULCNRz6g/zh-cn_image_0000002194158744.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=9DBB33B764197C432B3AE2F37DFFFC930F46F6BBC39A422E3B9F66C28ECB38DF "点击放大")

切换默认关联的远程仓库：

可以使用以下命令进行切换。

```screen
git branch hmos_dev_20230907 --set-upstream-to=codehub_origin/hmos_dev_20230907
```
