---
title: "执行python.exe"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-3"
menu_path:
  - "FAQ"
  - "DevEco Testing"
  - "专项测试"
  - "场景化性能测试"
  - "执行python.exe -m pip install --upgrade pip命令更新pip库时报错ValueError: Unable to find resource t64.exe in package pip._vendor.distlib"
captured_at: "2026-04-17T02:03:26.135Z"
---

# 执行python.exe -m pip install --upgrade pip命令更新pip库时报错ValueError: Unable to find resource t64.exe in package pip.\_vendor.distlib

输入python -m pip uninstall pip setuptools卸载setuptools，输入pip install --upgrade setuptools重新安装 setuptools，然后重新执行python -m pip install --upgrade pip更新pip库。
