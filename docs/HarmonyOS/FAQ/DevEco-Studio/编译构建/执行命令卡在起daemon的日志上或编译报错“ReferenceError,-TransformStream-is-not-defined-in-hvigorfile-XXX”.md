---
title: "执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-183"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”"
captured_at: "2026-04-17T02:03:23.347Z"
---

# 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”

**问题现象**

流水线或命令行中执行命令后在起daemon的日志上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/IwfKjg6BQg-3ZNhRsXf7jg/zh-cn_image_0000002345811941.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=76D31E83956912F6A8DB67D57D6B09562E478DBE4A13B6DB8F3473584C873866)

或者是流水线或命令行中编译报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/l3EeJUdpQ-mBZXBS40Gm8A/zh-cn_image_0000002312015854.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=AB3C98E98C1E32CA7217E4F2EADAC39898545CE8D3C7E91549F9E2C99A6DB42D)

**问题原因**

编译不支持低于v18.0.0的Node.js版本。相关配置查看[配置Node.js环境变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app#section159168531288)。

**解决措施**

1.确认流水线或计算机配置的Node.js的版本。

Windows通过cmd或Powershell运行， Mac或Linux系统通过终端（Terminal）运行：

```powershell
node -v
```

查看输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WUL9tTpvQnubiff_zscyrg/zh-cn_image_0000002284561689.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=6772486F1FFAF4F9018C01AE9D7EAD6F050854E26227F300A098D4451EA9255B)

2.如果流水线或计算机配置的Node.js的版本低于v18.0.0，推荐使用DevEco Studio或Command Line Tools自带的Node.js包来配置系统变量。

Windows系统打开环境变量的配置，将DevEco或Command Line Tool自带的Node.js包的路径添加进系统变量的Path中。如果是通过NODE\_HOME配置的，可以直接修改NODE\_HOME配置的路径。若系统中已存在其他Node.js版本，需将工具自带的Node.js路径添加至Path变量的最前端，确保优先使用该版本；通过NODE\_HOME配置时，需检查Path中是否包含%NODE\_HOME%/bin（Windows）或$NODE\_HOME/bin（Mac/Linux）以确保生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/kaI9G56tS0qmLmWQAQ40Pg/zh-cn_image_0000002284693797.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=D207B4BA99B9DF6C80159630CDC2D42848CBE47BFD782086F98621C83528D106)

Mac或Linux系统参考[配置Node.js环境变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app#section159168531288)。

DevEco Studio的自带的Node.js的路径为DevEco Studio安装目录/DevEco Studio/tools/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/i-eWAeW_Ta6X1mjh7WJUJg/zh-cn_image_0000002284546061.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=47F4B8D5550FCC05D045E034D66F4EE10A63D8F326249545FD3FAF879D90703B)

Command Line Tools自带的Node.js的路径为Command Line Tools安装路径/command-line-tools/tool/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/rKo05M0dTgeXGlHuaha_mw/zh-cn_image_0000002284672673.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=E8AC98529FFAF296F6B4F06BB6A3CCAB2D6FAB336C8A19BF571732D5D46A1834 "点击放大")

3.将自定义的Node.js版本升级为与DevEco Studio或Command Line Tools自带的Node.js版本一致。通过上述路径运行node -v查看版本，然后在Node.js官方网站中下载对应版本。下载地址为：https://nodejs.org/dist/v18.20.1/。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/hRbvT5VYTPCF31QPU2za-Q/zh-cn_image_0000002277140989.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=A9B68EB95C528CFD92F3B1E7E5045B8714E74EB86ED2B2435D38B181AB6DCD35)
