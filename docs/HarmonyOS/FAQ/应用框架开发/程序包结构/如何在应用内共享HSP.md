---
title: "如何在应用内共享HSP"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-69"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序包结构"
  - "如何在应用内共享HSP"
captured_at: "2026-04-17T02:02:58.567Z"
---

# 如何在应用内共享HSP

如需在应用内共享HSP，请将HSP共享包上传至私仓。动态共享包HSP不能直接发布在私仓内，需要先转换为.tgz包。请按以下操作编译生成\*.tgz包。

1.  将编译模式设为release。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/sokgLlPdSeSrWGkeCcEwsg/zh-cn_image_0000002215625442.png?HW-CC-KV=V1&HW-CC-Date=20260417T020300Z&HW-CC-Expire=86400&HW-CC-Sign=3E796E117FC3AFF247F3F455A413B0EFB7BACB981441216F3F5BC65D28732713 "点击放大")
    
2.  选中HSP模块的根目录，点击Build > Make Module {libraryName}，启动构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/n1U8RfopQXORf2OyvQuY1w/zh-cn_image_0000002215465626.png?HW-CC-KV=V1&HW-CC-Date=20260417T020300Z&HW-CC-Expire=86400&HW-CC-Sign=DACE0879DF64BF6FD5D7BB67FD26578F915E6E5D0A86FF4AF5BA3E753CE2592C "点击放大")
    
3.  构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓（请参考[将三方库发布到 ohpm-repo](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-quickstart#zh-cn_topic_0000001792256157_将三方库发布到ohpm-repo)）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/xzkhpgo5Q6yl36MuNUNTMg/zh-cn_image_0000002250545457.png?HW-CC-KV=V1&HW-CC-Date=20260417T020300Z&HW-CC-Expire=86400&HW-CC-Sign=400FC7E96D57175DB92ECF56CFFFB82A56DC7BE76077CD015329B63DD800414F "点击放大")
    
4.  上传到仓库，然后使用 \`ohpm install\` 命令将依赖安装到工程的oh-package.json5文件的dependencies字段中，即可查看对外共享的 HSP 方法。

**参考链接**

[创建HSP模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp#section79378499185)
