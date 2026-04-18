---
title: "swiper开发指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-swiper"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (兼容JS的类Web开发范式)"
  - "常见组件开发指导"
  - "容器组件"
  - "swiper开发指导"
captured_at: "2026-04-17T01:35:40.519Z"
---

# swiper开发指导

swiper为滑动容器，提供切换显示子组件的能力。具体用法请参考[swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-swiper)。

#### 创建swiper组件

在pages/index目录下的hml文件中创建一个swiper组件。

```html
<!-- xxx.hml-->
<div class="container">
  <swiper>
    <div class="item" style="background-color: #bf45ea;">
      <text>item1</text>
    </div>
    <div class="item" style="background-color: #088684;">
      <text>item2</text>
    </div>
    <div class="item" style="background-color: #7786ee;">
      <text>item3</text>
    </div>
  </swiper>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
swiper{
  height: 30%;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 50px;
  color: white;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/PK1aqbiuRi2DVPwZij438g/zh-cn_image_0000002569018735.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=CF5BAF9EF747F161783D4C4334B25CE353EBC0282ECD7AE41A564B9D8C4A241E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/mL8kYNfCTe2Q9ZJg8DYIBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=79CB541B2E6FF2BD3454E203CFA90DD1B87330EDC0F0F8DCC2C0E9F90257E8F8)

swiper组件支持除<list>之外的子组件。

#### 添加属性

在swiper组件不开启循环播放（loop="false"）时添加自动播放属性（autoplay），设置自动播放时播放时间间隔（interval），页面会自动切换并停留在最后一个子组件页面。添加digital属性启用数字导航点，设置切换时为渐隐滑动效果（scrolleffect="fade"）。

```html
<!-- xxx.hml-->
<div class="container">
  <swiper index="1"  autoplay="true" interval="2000" indicator="true" digital="true" duration="500"
  scrolleffect="fade" loop="false">
    <div class="item" style="background-color: #bf45ea;">
      <text>item1</text>
    </div>
    <div class="item" style="background-color: #088684;">
      <text>item2</text>
    </div>
    <div class="item" style="background-color: #7786ee;">
      <text>item3</text>
    </div>
    <div class="item" style="background-color: #c88cee;">
      <text>item4</text>
    </div>
  </swiper>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
}
swiper{
  height: 30%;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 50px;
  color: white;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/PdIbz7gHQ86qmUd0tl8YuQ/zh-cn_image_0000002568898725.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=68F36F00397C2CD01EC38F5AE6C8EBCEC786826B82D88C68E17192DEA27CD8F7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/xlBPTxYvSu2SX_maN7-Drw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=D5FDA55127B8998F525AA042B9AA4BB0EB6E587D603A3AB295CC755A83B6FBEE)

-   设置indicator（是否启用导航点指示器）属性为true时digital（是否启用数字导航点）属性才会生效。
    
-   swiper子组件的个数大于等于2时设置的loop属性才会生效。
    
-   scrolleffect属性仅在loop属性值为false时生效。
    

#### 设置样式

设置swiper组件的宽高，导航点指示器的直径大小（indicator-size）、颜色（indicator-color）、相对位置（indicator-top）及选中时的颜色（indicator-selected-color）。

```html
<!-- xxx.hml-->
<div class="container">
    <swiper index="1" autoplay="true" interval="2000"  duration="500" >
        <div class="item" style="background-color: bisque;">
            <text>item1</text>
        </div>
        <div class="item" style="background-color: darkkhaki;">
            <text>item2</text>
        </div>
        <div class="item" style="background-color: cadetblue;">
            <text>item3</text>
        </div>
    </swiper>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
}
swiper{
  width:  500px;
  height: 500px;
  border-radius: 250px;
  indicator-color: white;
  indicator-selected-color: blue;
  indicator-size: 40px;
  indicator-top: 100px;
  overflow: hidden ;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  text-align: center;
  margin-top: 150px;
  font-size: 50px;
  color: white;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/2e09QysSSYq0qeRD7MIU5g/zh-cn_image_0000002538019020.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=132BA647036E5DAA033E9DBFE21714F98C74003E7DF3C1C557EBB67336E1F7F6)

#### 绑定事件

创建两个text组件添加点击事件，当点击后就调用showPrevious（显示上一个子组件）或showNext（显示下一个子组件）方法。添加select组件下拉选择时触发change事件后调用swipeTo方法跳转到指定轮播页面。swiper组件绑定change（当前显示的组件索引变化时触发）和finish（切换动画结束时触发）事件。

```html
<!-- xxx.hml-->
<div class="container">
  <swiper interval="2000" onchange="change" loop="false" onanimationfinish="finish" id="swiper">
    <div class="item" style="background-color: #bf45ea">
      <text>item1</text>
    </div>
    <div class="item" style="background-color: #088684;">
      <text>item2</text>
    </div>
    <div class="item" style="background-color: #7786ee;">
      <text>item3</text>
    </div>
    <div class="item" style="background-color: #c88cee;">
      <text>item4</text>
    </div>
  </swiper>
  <div class="content">
      <button class="pnbtn" onclick="previous">Previous</button>
      <select onchange="selectChange">
          <option value="0">swipeTo 1</option>
          <option value="1">swipeTo 2</option>
          <option value="2">swipeTo 3</option>
          <option value="3">swipeTo 4</option>
      </select>
    <button class="pnbtn" onclick="next">Next</button>
  </div>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
}
swiper{
  height: 30%;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 50px;
  color: white;
}
select{
  background-color: white;
  width: 250px;
  height: 80px;
}
.content{
  margin-top: 100px;
  justify-content: space-around;
}
.pnbtn{
  width: 200px;
  height: 80px;
  font-size: 30px;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default{
  change(e){
    promptAction.showToast({duration:2000,message:"current index:"+e.index});
  },
  finish(){
    promptAction.showToast({duration:2000,message:"切换动作结束"});
  },
  selectChange(e){
    this.$element('swiper').swipeTo({index: Number(e.newValue)});
  },
  previous(){
    this.$element('swiper').showPrevious();
  },
  next(){
    this.$element('swiper').showNext();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/SwclM0TgROWJMB7dsPckiQ/zh-cn_image_0000002538178948.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=BB4C79E9CB26E42B7C0EE419D00B4CC6837BF5B25E2918C2E16CECED22C5D1BF)

#### 场景示例

本场景中使用swiper创建一个轮播图，在轮播图底部制作一个缩略图，点击缩略图后调用swipeTo方法切换到对应的轮播图。

```html
<!-- xxx.hml-->
<div class="container">
  <swiper duration="500" indicator="false" id="swiper" onchange="change">
    <div class="item" for="item in list">
      <image src="{{item.src}}"></image>
    </div>
  </swiper>
  <div class="content">
    <div class="content_item {{index == $idx?'activated':''}}" for="item in list" onclick="imageTo({{$idx}})">
      <image src="{{item.src}}"></image>
    </div>
  </div>
</div>
```

```css
/* xxx.css */
.container{
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
swiper{
  width: 100%;
  height: 500px;
}
.item{
  width: 100%;
  height: 500px;
}
.content{
  margin-top: -120px;
  width: 70%;
  display: flex;
  justify-content: space-around;
  height: 100px;
}
.content_item{
  padding: 5px;
  transform: scale(0.5);
}
.activated{
  transform: scale(1);
  border: 1px solid #b20937ea;
}
```

```js
// xxx.js
export default {
  data:{
    index: 0,
    list:[
      {src: 'common/images/1.png'},
      {src: 'common/images/2.png'},
      {src: 'common/images/3.png'},
      {src: 'common/images/4.png'},]
    },
  imageTo(index){
    this.index = index;
    this.$element('swiper').swipeTo({index: index});
  },
  change(e){
    this.index = e.index;
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/qqfM972XQh27ZzJbDGjymw/zh-cn_image_0000002569018737.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013541Z&HW-CC-Expire=86400&HW-CC-Sign=7E78687406E0AA924FF308168E710AC5E5C39FC697164183A331F5769DC4E8F2)
