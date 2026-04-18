---
title: "svg动画"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-svg"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (兼容JS的类Web开发范式)"
  - "动效开发指导"
  - "CSS动画"
  - "svg动画"
captured_at: "2026-04-17T01:35:40.997Z"
---

# svg动画

为svg组件添加动画效果。

#### 属性样式动画

在svg的子组件[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)中，通过attributeName设置需要进行动效的属性，from设置开始值，to设置结束值。

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="300" y="300" fill="blue">
      Hello
      <animate attributeName="font-size" from="30" to="60" dur="3s" repeatCount="indefinite">
      </animate>
      <animate attributeName="fill" from="red" to="blue" dur="3s" repeatCount="indefinite">
      </animate>
      <animate attributeName="opacity" from="1" to="0.3" dur="3s" repeatCount="indefinite">
      </animate>
    </text>
    <text x="300" y="600" fill="blue">
      World
      <animate attributeName="font-size" from="30" to="60" values="30;80" dur="3s" repeatCount="indefinite">
      </animate>
      <animate attributeName="fill" from="red" to="blue"  dur="3s" repeatCount="indefinite">
      </animate>
      <animate attributeName="opacity" from="0.3" to="1" dur="3s" repeatCount="indefinite">
      </animate>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/oyrB_rYVQs6Df-q533WW_w/zh-cn_image_0000002568898775.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=098B8CF7803FA30FC5FD7D877D963A8A51F702F2AE0E2FFD176A59F472EFF8C9)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Ejxv1vmDTmG_35nC89ccmw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=2C0DB67DB007121856DA2709DD18A788341A4DEA0000DE1003D52E50840BEC34)

在设置动画变化值时，如果已经设置了values属性，则from和to都失效。

#### 路径动画

在svg的子组件[animateMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion)中，通过path设置动画变化的路径。

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="800" height="900">
    <path d="M300,200 h-150 a150 150 0 1 0 150 -150 z" fill="white" stroke="blue" stroke-width="5" >
    </path>
    <path fill="red" d="M-5,-5 L10,0 L-5,5 L0,0 Z"  >
      <animateMotion dur="2000" repeatCount="indefinite" rotate="auto-reverse"path="M300,200 h-150 a150 150 0 1 0 150 -150 z">
      </animateMotion>
    </path>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/PVGwg5QAT02vZrXWhAEdXg/zh-cn_image_0000002538019070.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=DFA920578108739460CC564C0F7BBC2AC012D3488C9570DDD6DCCDF44EF8D5F8)

#### animateTransform动画

在svg的子组件[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)中，通过attributeName绑定transform属性，type设置动画类型，from设置开始值，to设置结束值。

```html
<!-- xxx.hml -->
<div class="container" style="">
  <svg>
    <line x1="90" y1="300" x2="90" y2="730" stroke-width="10" stroke="black" stroke-linecap="round">
      <animateTransform attributeName="transform" attributeType="XML" type="translate"  dur="3s" values="0;30;10;30;20;30;25;30" keyTimes="0;0.3;0.5;0.7;0.8;0.9;1.0;1.1"
      fill="freeze">
      </animateTransform>
    </line>
    <circle cx="500" cy="500" r="50" stroke-width="15" fill="red" stroke="#e70d0d">
      <animateTransform attributeName="transform" attributeType="XML" type="rotate"  dur="3s" values="0;30;10;30;20;30;25;30" keyTimes="0;0.3;0.5;0.7;0.8;0.9;1.0;1.1" fill="freeze">
      </animateTransform>
      <animateTransform attributeName="transform" attributeType="XML" type="scale"  dur="6s" values="1;1;1.3" keyTimes="0;0.5;1" fill="freeze"></animateTransform>
      <animateTransform attributeName="transform" attributeType="XML" type="translate"  dur="9s" values="0;0;300 7" keyTimes="0;0.6;0.9" fill="freeze"></animateTransform>
    </circle>
    <rect width="500" height="200" x="90" y="840">
      <animateTransform attributeName="transform" attributeType="XML" type="skewY"  dur="6s" values="0;0;30" keyTimes="0;0.5;1" fill="freeze"></animateTransform>
    </rect>
    <line x1="650" y1="300" x2="650" y2="600" stroke-width="20" stroke="blue" stroke-linecap="round">
      <animateTransform attributeName="transform" attributeType="XML" type="translate"  dur="9s" values="0;0;0 800" keyTimes="0;0.6;1" fill="freeze"></animateTransform>
    </line>
  </svg>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: #F1F3F5;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/lERqn7-MTXGzM6jwUst63Q/zh-cn_image_0000002538178998.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=21D79E81E449E595AB4283ECA1F432859BE4D32944EAD8D2131110AA6645FC54)
