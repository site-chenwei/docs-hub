---
title: "search开发指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-search"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (兼容JS的类Web开发范式)"
  - "常见组件开发指导"
  - "基础组件"
  - "search开发指导"
captured_at: "2026-04-17T01:35:40.707Z"
---

# search开发指导

提供搜索框组件，用于提供用户搜索内容的输入区域，具体用法请参考[search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-search)。

#### 创建search组件

在pages/index目录下的hml文件中创建一个search组件。

```html
<!-- xxx.hml-->
<div class="container">
  <search></search>
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/AfNPpD1mTI6zJJxHkKb0KA/zh-cn_image_0000002568898757.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=33938DC69B21B10AC0952825E65A166270F43F286C81C81415D5B28613758AAB)

#### 设置属性

通过设置hint、icon和searchbutton属性设置搜索框的提示文字、图标和末尾搜索按钮的内容。

```html
<!-- xxx.hml-->
<div class="container">
  <search hint="Please enter the search content"  searchbutton="search" icon="/common/search1.png"></search>
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/XfgzeEiqR1CoVzlWxmdjAg/zh-cn_image_0000002538019052.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=4DABA6462B85FFDA95AA71DC92766BAE9D5C4B645524F8B0484CF4FA7525AD80)

#### 添加样式

通过color、placeholder-color和caret-color样式来设置搜索框的文本颜色、提示文本颜色和光标颜色。

```html
<!-- xxx.hml-->
<div class="container">
  <search hint="Please enter the search content"  searchbutton="search" ></search>
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
search{
  color: black;
  placeholder-color: black;
  caret-color: red;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/sQAl7m_hTFi-Sve4DrhSKg/zh-cn_image_0000002538178980.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=4F887385415D35A3FBF7FD367BD8B7DFA98EEB5A04CA91F294265A13EA2ECC7A)

#### 绑定事件

向search组件添加change、search、submit、share和translate事件，对输入信息进行操作。

```html
<!-- xxx.hml-->
<div class="container">
  <text style="margin-left: -7px;">
    <span>Enter text and then touch and hold what you've entered</span>
  </text>
  <search hint="Please enter the search content"  searchbutton="search" onsearch="search" onchange="change" ontranslate="translate" onshare="share"
  onsubmit="submit">
  </search>
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
text{
  width: 100%;
  font-size: 25px;
  text-align: center;
  margin-bottom: 100px;
}
```

```js
// index.js
import promptAction from '@ohos.promptAction';
export default {
  search(e){
    promptAction.showToast({
      message: e.value,
      duration: 3000,
    });
  },
  translate(e){
    promptAction.showToast({
      message:  e.value,
      duration: 3000,
    });
  },
  share(e){
    promptAction.showToast({
      message:  e.value,
      duration: 3000,
    });
  },
  change(e){
    promptAction.showToast({
      message:  e.value,
      duration: 3000,
    });
  },
  submit(e){
    promptAction.showToast({
      message: 'submit',
      duration: 3000,
    });
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/W7d5rnPbRO6xpxwl-UHBfA/zh-cn_image_0000002569018769.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=7BC3447A6EF10254BDE8C5FF3A07EC53FBBE9DD9D89E88F8ECD718FE5187BD65)

#### 场景示例

在本场景中通过下拉菜单选择search、Textarea和Input组件来实现搜索和输入效果。

```html
<!-- xxx.hml-->
<div style="flex-direction: column;align-items: center;justify-content: center; width: 100%;">
  <select class="slt1" id="slt1" onchange="setfield">
    <option value="search">search</option>
    <option value="textarea">Textarea</option>
    <option value="input">Input</option>
  </select>
  <div if="{{showsearch}}" style="flex-direction: column;align-items: center;margin-top: 50px;height: 400px;justify-content: space-around;">
    <search class="field" id="search1" hint="search1" onsubmit="submit" onchange="change" ></search>
    <search class="field" id="search2" icon="common/search1.png" hint="search2" show="{{showsec}}" onsubmit="submit" onchange="change" ></search>
  </div>
  <div if="{{showtextarea}}" style="flex-direction: column;align-items: center;margin-top: 50px;height: 400px;justify-content: space-around;">
    <textarea class="field" id="textarea1" extend="true" placeholder="textarea1" onchange="change" ></textarea>
    <textarea class="field" id="textarea2" extend="true" placeholder="textarea2" onchange="change" show="{{showsec}}"></textarea>
  </div>
  <div if="{{showinput}}" style="flex-direction: column;align-items: center;margin-top: 50px;height: 400px;justify-content: space-around;">
    <input type="text" class="field" id="input1" placeholder="input1" onchange="change" ></input>
    <input type="text" class="field" id="input2" placeholder="input2" onchange="change" show="{{showsec}}"></input>
  </div>
</div>
```

```css
/* xxx.css */
.field {
  width: 80%;
  color: mediumaquamarine;
  font-weight: 600;
  placeholder-color: orangered;
}
.slt1{
  font-size: 50px;
  position: absolute;
  left: 50px;
  top: 50px;
}
```

```js
// index.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
    showsearch: true,
    showtextarea: false,
    showinput: false,
    showsec: true,
  },
  setfield(e) {
    this.field = e.newValue
    if (e.newValue == 'search') {
      this.showsearch = true
      this.showtextarea = false
      this.showinput = false
    } else if (e.newValue == 'textarea') {
      this.showsearch = false
      this.showtextarea = true
      this.showinput = false
    } else {
      this.showsearch = false
      this.showtextarea = false
      this.showinput = true
    }
  },
  submit(e) {
    promptAction.showToast({
      message: '搜索！',
      duration: 2000
    })
  },
  change(e) {
    promptAction.showToast({
      message: '内容:' + e.text,
      duration: 2000
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/20F897h_Rwa59_SCstHrsA/zh-cn_image_0000002568898759.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=14DB12EBB00F9E5D071959448111E98E9B88496294F824E61774E64C7E29A07E)
