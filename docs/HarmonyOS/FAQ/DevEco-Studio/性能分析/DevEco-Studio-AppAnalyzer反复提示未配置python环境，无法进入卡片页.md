---
title: "DevEco Studio AppAnalyzer反复提示未配置python环境，无法进入卡片页"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-12"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "性能分析"
  - "DevEco Studio AppAnalyzer反复提示未配置python环境，无法进入卡片页"
captured_at: "2026-04-17T02:03:25.109Z"
---

# DevEco Studio AppAnalyzer反复提示未配置python环境，无法进入卡片页

**问题现象**

新用户使用6.0.1 beta及之前的版本, 可能有以下问题：

1.  反复提示配置python环境，无法进入卡片页（6.0）。
2.  场景化自动无法遍历（5.1）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/MMqm0VL5RZey0pqXLCTOXQ/zh-cn_image_0000002516304447.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=FF74999C56A289818E9312637CBB82AC1B73D72D8EC5E2E672E1A32BB9BBCD74)

**可能原因**

根因是hypium安装后, 由于未固定pynacl的版本号, pip安装了最新的pynacl及其适配的cffi, cffi更新后导致AppAnalyzer的依赖校验不通过。解决方案是提前安装pynacl并且固定pynacl==1.5.0。

**解决措施**

1.找到Python的安装目录。

MAC：

```powershell
# 6.0 版本
cat ~/Library/Application\ Support/Huawei/DevEcoStudio6.0/options/other.xml  | grep -i "location.python.path" 
# 5.1 版本
cat ~/Library/Application\ Support/Huawei/DevEcoStudio5.1/options/other.xml  | grep -i "location.python.path" 
```

WIN：

打开other.xml搜索location.python.path。

```xml
# 6.0 版本
C:\Users\<username>\AppData\Roaming\Huawei\DevEcoStudio6.0\options\other.xml
# 5.1 版本
C:\Users\<username>\AppData\Roaming\Huawei\DevEcoStudio5.1\options\other.xml
```

2.卸载pynacl 、cffi。

切换到python的安装目录，注意请使用当前目录中的python，执行依赖卸载命令，请参考：

```powershell
./python -m pip uninstall pynacl -y
./python -m pip uninstall cffi -y
```

3.安装pynacl 、cffi。

切换到python的安装目录，注意请使用当前目录中的python，执行依赖安装命令，请参考：

```powershell
./python -m pip install cffi==1.17.1
./python -m pip install pynacl==1.5.0
```

4.重新打开AppAnalyzer。
