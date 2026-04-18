---
title: "如何在App启动时让各种权限弹窗的申请自动弹出"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-92"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "如何在App启动时让各种权限弹窗的申请自动弹出"
captured_at: "2026-04-17T02:02:59.286Z"
---

# 如何在App启动时让各种权限弹窗的申请自动弹出

将requestPermissionsFromUser接口放到EntryAbility.ets文件的loadContent回调中，参考代码如下：

windowStage.loadContent('pages/Index', (err) => {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(this.context, \['ohos.permission.ACCESS\_BLUETOOTH'\])
    .then((data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    }).catch((err: BusinessError) => {
    console.error('data:' + JSON.stringify(err));
  });
});

在设置文件中声明目标权限：

"requestPermissions": \[
  {
    "name": "ohos.permission.ACCESS\_BLUETOOTH",
    "usedScene": {
      "abilities": \[
        "EntryAbility"
      \],
      "when": "inuse"
    },
    "reason": "$string:app\_name"
  }
\],

**参考链接**

[abilityAccessCtrl.createAtManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#abilityaccessctrlcreateatmanager)
