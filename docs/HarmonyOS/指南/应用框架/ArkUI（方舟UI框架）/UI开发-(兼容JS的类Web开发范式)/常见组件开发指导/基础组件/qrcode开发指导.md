---
title: "qrcode开发指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-qrcode"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (兼容JS的类Web开发范式)"
  - "常见组件开发指导"
  - "基础组件"
  - "qrcode开发指导"
captured_at: "2026-04-17T01:35:40.710Z"
---

# qrcode开发指导

生成并显示二维码，具体用法请参考[qrcode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-qrcode)。

#### 创建qrcode组件

在pages/index目录下的hml文件中创建一个qrcode组件。

```html
<!-- xxx.hml-->
<div class="container">
  <qrcode value="Hello"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/WBJuW4b9TJa6S52MT0X7bQ/zh-cn_image_0000002568898755.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=EA3D5C9E8129D5915FCF3FB23F7C93FC0A2991C51A3476FBDC68D8C47DBCAD40)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/xO1ng02wRAavPHkfko5l6g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=2ECC5B0BAD26A51700DE608633F60FD9132C322C53FD5E1A2FD684ACEE0BA5FD)

qrcode组件在创建的时候value的值为必填项。

#### 设置组件类型

通过设置qrcode的type属性来选择二维码类型，如定义qrcode为矩形二维码、圆形二维码。

```html
<!-- xxx.hml-->
<div class="container">
  <select onchange="settype">
    <option for="{{bcol_list}}" value="{{$item}}">{{$item}}</option>
  </select>
  <qrcode value="Hello" type="{{qr_type}}"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
select{
  margin-top: 50px;
  margin-bottom: 50px;
}
```

```js
// index.js
export default {
  data: {
    qr_type: 'rect',
    bcol_list: ['rect','circle']
  },
  settype(e) {
    this.qr_type = e.newValue
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/-BcxSKZMQXOz5ylmYIroqw/zh-cn_image_0000002538019050.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=6D9B4BAA855CFDB216E49B5039E71FE6B73B3EAC552827B35E1D90EE6188BF7C)

#### 设置样式

通过color和background-color样式为二维码设置显示颜色和背景颜色。

```html
<!-- xxx.hml-->
<div class="container">
  <qrcode value="Hello" type="rect"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
qrcode{
  width: 300px;
  height: 300px;
 color: blue;  background-color: #ffffff;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/LsPCOx1oTBOJtTuaBC-V3w/zh-cn_image_0000002538178978.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=21BCC2CC8C4989017B3E0A9E3D7E697070B53EE03AB45E09EA9884699489A5AC)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/YZHPadDoS8CfbpcV0tQYKQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=2D0AF3712DE7A9BA2C6F64BE732DFBF6972AE0DE18DF76C1709B531887920692)

-   width和height不一致时，取二者较小值作为二维码的边长，且最终生成的二维码居中显示。
    
-   width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。
    

#### 场景示例

在本场景中将二维码与输入框绑定，通过改变输入框的内容改变二维码。

```html
<!-- xxx.hml-->
<div class="container">
  <input style="margin-bottom: 100px;" onchange="change"></input>
  <qrcode value="{{textVal}}"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
qrcode{
  width: 400px;
  height: 400px;
}
```

```js
// index.js
export default{
  data: {
    textVal: ''
  },
  change(e){
    this.textVal = e.value
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/4sWPLungQfiFcdVBRx98lA/zh-cn_image_0000002569018767.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=7832B9A89CB8ECF7283BF0A0C707D8C4DD69D7EFA4BDBBE440CE9684EB54046D)
