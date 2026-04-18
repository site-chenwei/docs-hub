---
title: "text开发指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-text"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (兼容JS的类Web开发范式)"
  - "常见组件开发指导"
  - "基础组件"
  - "text开发指导"
captured_at: "2026-04-17T01:35:40.554Z"
---

# text开发指导

text是文本组件，用于呈现一段文本信息。具体用法请参考[text API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-text)。

#### 创建text组件

在pages/index目录下的hml文件中创建一个text组件。

```html
<!-- xxx.hml -->
<div class="container" style="text-align: center;justify-content: center; align-items: center;">
  <text>Hello World</text>
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/i14TIrbGSUCQFeEUIQy1lQ/zh-cn_image_0000002568898727.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=61162F36244ABCC9FB79A505B871FC93A3AB11143CFEB2D9D7DCE6F8A1361538)

#### 设置text组件样式和属性

-   添加文本样式
    
    设置color、font-size、allow-scale、word-spacing、text-align属性分别为文本添加颜色、大小、缩放、文本之间的间距和文本在水平方向的对齐方式。
    
    ```html
    <!-- xxx.hml -->
    <div class="container" style="background-color:#F1F3F5;flex-direction: column;justify-content: center; align-items: center;">   
      <text style="color: blueviolet; font-size: 40px; allow-scale:true"> 
        This is a passage
      </text>
      <text style="color: blueviolet; font-size: 40px; margin-top: 20px; allow-scale:true;word-spacing: 20px;text-align: center">
        This is a passage
      </text>
    </div> 
    ```
    
    ```css
    /* xxx.css */
    .container {
      display: flex;
      width: 100%;
      height: 100%;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background-color: #F1F3F5;
    }
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/0m6hW21fRe-0lWnbrZE1Bg/zh-cn_image_0000002538019022.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=B809CE54A15D066A9DADB159C2289E9F7DA079B534B2452304E60440925FF21D)
    
-   添加划线
    
    设置text-decoration和text-decoration-color属性为文本添加划线和划线颜色，text-decoration枚举值请参考 text自有样式。
    
    ```html
    <!-- xxx.hml -->
    <div class="container" style="background-color:#F1F3F5;">
      <text style="text-decoration:underline">
        This is a passage
      </text>
      <text style="text-decoration:line-through;text-decoration-color: red">
        This is a passage
       </text>
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
    }
    text{
      font-size: 50px;
    }
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/A2mxYYBlTFS9Tbmu-4su0g/zh-cn_image_0000002538178950.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=15C9C963E4965C9AD096E4543AFE90B44A94C630C47FF6840930C87503DF20E9)
    
-   隐藏文本内容
    
    当文本内容过多而显示不全时，添加text-overflow属性将隐藏内容以省略号的形式展现。
    
    ```html
    <!-- xxx.hml -->
    <div class="container">
      <text class="text">
        This is a passage
      </text>
    </div>
    ```
    
    ```css
    /* xxx.css */
    .container {
      width: 100%;
      height: 100%;
      flex-direction: column;
      align-items: center;
      background-color: #F1F3F5;
      justify-content: center;
    }
    .text{
      width: 200px;
      max-lines: 1;
      text-overflow:ellipsis;
    }
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/pF055TiMSFONkf_xylzgag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=B415D40E462140FC8DECBD7379279A47C71866C81FAD2188EF814911B5F949EF)
    
    -   text-overflow样式需要与max-lines样式配套使用，设置了最大行数的情况下生效。
    -   max-lines属性设置文本最多可以展示的行数。
    
    ​ ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/H5QFyX1DQ92t9a5B_2lOAg/zh-cn_image_0000002569018739.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=1C00618BBC95669934BB9766502413744D1A8819E8907E779DE4915894E5443E)
    
-   text组件支持[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-span)子组件
    
    ```html
    <!-- xxx.hml -->
    <div class="container" style="justify-content: center; align-items: center;flex-direction: column;background-color: #F1F3F5;  width: 100%;height: 100%;">
      <text style="font-size: 45px;">
        This is a passage
      </text>
      <text style="font-size: 45px;">
        <span style="color: aqua;">This </span><span style="color: #F1F3F5;">      1
        </span>   
        <span style="color: blue;"> is a </span>    <span style="color: #F1F3F5;">      1    </span>    
        <span style="color: red;">  passage </span>
      </text>
    </div>
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/cEjOKhMeR2mhikW-F71tRA/zh-cn_image_0000002568898729.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=CF9D527C47AB72AE3277D3319F5A1C54495B8789EFA45E5E2144E5C4E315DEF9)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/BN3BUSUrRmGGEkY-TCiK7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=877C5C8AE0D6DF0EBD2A7CF7BC6456ADBAD29B58EB9808CE8CEAD4DAAB18FC8A)
    
    -   当使用Span子组件组成文本段落时，如果Span属性样式异常（例如：font-weight设置为1000），将导致文本段落显示异常。
        
    -   在使用Span子组件时，注意text组件内不能存在文本内容，如果存在文本内容也只会显示子组件Span里的内容。
        
    

#### 场景示例

text组件通过数据绑定展示文本内容，Span组件通过设置show属性来实现文本内容的隐藏和显示。

```html
<!-- xxx.hml -->
<div class="container">
  <div style="align-items: center;justify-content: center;">
    <text class="title">
      {{ content }}
    </text>
    <switch checked="true" onchange="test"></switch>
  </div>
  <text class="span-container" style="color: #ff00ff;">
    <span show="{{isShow}}">  {{ content  }}  </span>
    <span style="color: white;">
        1
    </span>
    <span style="color: #f76160">Hide clip </span>
  </text>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  background-color: #F1F3F5;
}
.title {
  font-size: 26px;
  text-align:center;
  width: 200px;
  height: 200px;
}
```

```js
// xxx.js
export default {
  data: {
    isShow:true,
    content: 'Hello World'
  },
  onInit(){    },
  test(e) {
    this.isShow = e.checked
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/jwLGnitATKWpuLqR0lVQvA/zh-cn_image_0000002538019024.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=C84B090CC34D463A7D1BE08194F4CDBE8A71DF76EBCDD3E513CA23A00121209A)
