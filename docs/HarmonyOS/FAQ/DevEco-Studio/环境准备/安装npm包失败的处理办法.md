---
title: "安装npm包失败的处理办法"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-8"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "安装npm包失败的处理办法"
captured_at: "2026-04-17T02:03:20.182Z"
---

# 安装npm包失败的处理办法

**问题现象**

执行npm install命令安装npm包时，可能会提示安装失败。

**解决措施**

由于未设置npm仓库地址，可执行如下命令后重新安装。

```powershell
npm config set @ohos:registry=https://repo.harmonyos.com/npm/
```
