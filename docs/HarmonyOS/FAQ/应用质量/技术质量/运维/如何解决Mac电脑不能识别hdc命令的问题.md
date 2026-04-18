---
title: "如何解决Mac电脑不能识别hdc命令的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-42"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何解决Mac电脑不能识别hdc命令的问题"
captured_at: "2026-04-17T02:02:57.448Z"
---

# 如何解决Mac电脑不能识别hdc命令的问题

1.  环境变量因素的解决方法参考如下：
    1.  点击屏幕左上角的苹果图标，转到系统设置中的“用户与群组”。
    2.  按住Ctrl键，点击左侧窗格中的用户账户名称，然后选择“高级选项”。
    3.  点击"Login Shell"下拉框，然后选择"/bin/bash"以将Bash作为默认shell。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/678JQPIsQXqXortaQbTU_g/zh-cn_image_0000002194318532.png?HW-CC-KV=V1&HW-CC-Date=20260417T020259Z&HW-CC-Expire=86400&HW-CC-Sign=D9A30F2F3B239EB4A2F0A6FA123829BB1263CE1C8B8CE9D1102D519A5B248796 "点击放大")
        
2.  非环境变量因素的解决方法参见：
    
    1.  打开终端，输入 cd ~。
    2.  使用 sudo vim .bash\_profile 命令编辑文件。
    3.  在文档底部输入：
        
        export PATH=${PATH}:Sdk/default/base/toolchains
        
        按下Esc键退出，然后在下方输入:wq保存并退出。
        
    4.  运行 source .bash\_profile 命令以加载环境变量。
    5.  输入 hdc -v，显示版本信息即表示可用。
    
    **参考链接：**
    
    [常见问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#常见问题)
