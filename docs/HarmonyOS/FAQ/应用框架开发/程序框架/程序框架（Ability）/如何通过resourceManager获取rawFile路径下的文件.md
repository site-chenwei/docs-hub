---
title: "如何通过resourceManager获取rawFile路径下的文件"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-111"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "如何通过resourceManager获取rawFile路径下的文件"
captured_at: "2026-04-17T02:02:59.417Z"
---

# 如何通过resourceManager获取rawFile路径下的文件

**解决方案**

可以通过[@ohos.resourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)中的[getRawFileList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getrawfilelist10)方法获取RawFile路径下的所有文件。参考代码如下：

import { BusinessError } from '@kit.BasicServicesKit';

// Passing in '' indicates obtaining a list of files in the root directory of rawfile
try {
  let context = AppStorage.get('context') as UIContext;
  context.getHostContext()!.resourceManager.getRawFileList('', (error: BusinessError, value: Array<string>) => {
    if (error != null) {
      console.error(\`callback getRawFileList failed, error code: ${error.code}, message: ${error.message}.\`);
    } else {
      let rawFile = value;
    }
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`callback getRawFileList failed, error code: ${code}, message: ${message}.\`);
}
