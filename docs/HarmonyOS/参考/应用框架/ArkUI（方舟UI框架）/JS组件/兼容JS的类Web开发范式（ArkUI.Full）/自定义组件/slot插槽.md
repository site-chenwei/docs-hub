---
title: "slot插槽"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-slot"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "JS组件"
  - "兼容JS的类Web开发范式（ArkUI.Full）"
  - "自定义组件"
  - "slot插槽"
captured_at: "2026-04-17T01:48:06.063Z"
---

# slot插槽

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/fvvltR41TDW3pVM-i_y8Dw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=0D504D4BB2483C75E484971FFE08C94C271AE08E5C984B6E9281A88F5222BA5A)

从API version 7 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 默认插槽

自定义组件中通过slot标签来承载父组件中定义的内容，使用slot标签可以更加灵活的控制自定义组件的内容元素，使用方式如下：

```html
<!-- comp.hml -->
<div class="item">  
   <text class="text-style">下面使用父组件定义的内容</text> 
   <slot></slot> 
</div>
```

引用该自定义组件方式如下：

```html
<!-- xxx.hml --> 
 <element name='comp' src='../common/component/comp.hml'></element>  
 <div class="container">  
   <comp>
     <text class="text-style">父组件中定义的内容</text> 
   </comp>  
 </div>
```

#### 具名插槽

当自定义组件中需要使用多个插槽时，可通过对插槽命名的方式进行区分，当填充插槽内容时，通过声明插槽名称，将内容加到对应的插槽中。

```html
<!-- comp.hml -->
<div class="item">  
   <text class="text-style">下面使用父组件定义的内容</text> 
   <slot name="first"></slot>
   <slot name="second"></slot> 
</div>
```

引用该自定义组件方式如下：

```html
<!-- xxx.hml --> 
 <element name='comp' src='../common/component/comp.hml'></element>  
 <div class="container">  
   <comp>
     <text class="text-style" slot="second">插入第二个插槽中</text> 
     <text class="text-style" slot="first">插入第一个插槽中</text>
   </comp>  
 </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/cQaR_BY6QV-F2a1Xg_SVmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014805Z&HW-CC-Expire=86400&HW-CC-Sign=9EA4D1602B129A8042A95F37CC20B6EE28036F79CCAE7924B5A3F55D5C4B76EC)

name 和 slot 属性不支持绑定动态数据。
