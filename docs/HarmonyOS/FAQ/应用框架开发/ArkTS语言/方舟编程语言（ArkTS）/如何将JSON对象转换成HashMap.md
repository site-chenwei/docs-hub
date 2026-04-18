---
title: "如何将JSON对象转换成HashMap"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-89"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "如何将JSON对象转换成HashMap"
captured_at: "2026-04-17T02:03:00.380Z"
---

# 如何将JSON对象转换成HashMap

可以参考如下示例代码：

import { HashMap } from '@kit.ArkTS';

let str: string = '{\\"common\_params\\": {' +
  '\\"city\_id\\": 1,' +
  '\\"nav\_id\_list\\": \\"\\",' +
  '\\"show\_hook\_card\\": 2,' +
  '\\"use\_one\_stop\_structure\\": 1,' +
  '\\"version\_tag\\": \\"homepageonestop\\"' +
  '}' +
  '}';

let jsonObj: Object = JSON.parse(str);
let commObj = (jsonObj as Record<string, Object>);
let commRecord = (commObj\['common\_params'\] as Record<string, Object>);
let keyStr = Object.keys(commRecord);

for (let index: number = 0; index < keyStr.length; index++) {
  commRecord\[keyStr\[index\].toString()\].toString();
}

let hashMapData: HashMap<string, Object> = new HashMap();
hashMapData.set('common\_params', commRecord);

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('JSON to HashMap')
          .onClick(() => {
            // common\_params: {"city\_id":1,"nav\_id\_list":"","show\_hook\_card":2,"use\_one\_stop\_structure":1,"version\_tag":"homepageonestop"}
            console.log('common\_params:', JSON.stringify(hashMapData.get('common\_params')));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
