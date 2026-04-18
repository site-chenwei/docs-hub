---
title: "如何在系统深色模式下使用getColorSync(resource)返回深色颜色值"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-354"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何在系统深色模式下使用getColorSync(resource)返回深色颜色值"
captured_at: "2026-04-17T02:03:06.410Z"
---

# 如何在系统深色模式下使用getColorSync(resource)返回深色颜色值

目前有两种方案可供参考：

1.  传递资源ID。
    
    this.getUIContext().getHostContext()?.resourceManager.getColorSync($r('app.color.xxx').id);
    
2.  在配置了dark限定词目录的包的module.json5文件中添加配置。
    
    "metadata": \[
      {
        "name": "ContextResourceConfigLoadFromParentTemp",
        "value": "true"
      }
    \],
