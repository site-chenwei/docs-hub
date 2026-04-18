---
title: "进度条 (Progress)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "添加组件"
  - "进度条 (Progress)"
captured_at: "2026-04-17T01:35:38.029Z"
---

# 进度条 (Progress)

Progress是进度条显示组件，显示内容通常为目标操作的当前进度。具体用法请参考[Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)。

#### 创建进度条

Progress通过调用接口来创建，接口调用方式如下：

```ts
Progress(options: {value: number, total?: number, type?: ProgressType})
```

其中，value用于设置初始进度值，total用于设置进度总长度，type用于设置Progress样式。

```ts
Progress({ value: 24, total: 100, type: ProgressType.Linear }) // 创建一个进度总长为100，初始进度值为24的线性进度条
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/CpHv8e7LQsKFqTZSoBgreQ/zh-cn_image_0000002538178742.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=0771E281327398C46905A199B656063027DF3FED161913614F976294C4BF2293)

#### 设置进度条样式

Progress有5种可选类型，通过ProgressType可以设置进度条样式。ProgressType类型包括：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

-   线性样式进度条（默认类型）
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/g1IsjI3OToCYT6yIV6KOiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=2C4A1EB227EB879036DC08CB0251768A8D4997B275D5E0F84959D96A7823241F)
    
    从API version 9开始，组件高度大于宽度时，自适应垂直显示；组件高度等于宽度时，保持水平显示。
    
    Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
    Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/MkFe8LSCSLKI-PMuQmyViA/zh-cn_image_0000002569018531.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=4801A5C112D02B5AC5723A9C6B8CBD5A4AD39FC539D0090B2A2E9C43FA4396FC)
    
-   环形无刻度样式进度条
    
    // 从左往右，1号环形进度条，默认前景色为蓝色渐变，默认strokeWidth进度条宽度为2.0vp
    Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
    // 从左往右，2号环形进度条
    Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
      .color(Color.Grey)    // 进度条前景色为灰色
      .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15.0vp
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/uFxOes8-StS-Ffh4WNAjSg/zh-cn_image_0000002568898521.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=FB0A063306665CEB6420DB5223ED6104EF9335527A83D540E47EFCFF39A075E1)
    
-   环形有刻度样式进度条
    
    Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
      .backgroundColor(Color.Black)
      .style({ scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条总刻度数为20，刻度宽度为5vp
    Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
      .backgroundColor(Color.Black)
      .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为5vp
    Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
      .backgroundColor(Color.Black)
      .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 3 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为3vp
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/a0wOLWrlSFutgJFYov81JA/zh-cn_image_0000002538018816.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=EEF1275BCAD8B74F065E6F085EAB2A5EF21222CE3FF96D267D558DFC76C0AEC2)
    
-   圆形样式进度条
    
    // 从左往右，1号圆形进度条，默认前景色为蓝色
    Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
    // 从左往右，2号圆形进度条，指定前景色为灰色
    Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/SHszdeAYTged6vmSi11uug/zh-cn_image_0000002538178744.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=9ED88EB63EA4AB8D9CBA2348F556FB3D45156C68EA67DFF97A3D8AD76C0D728E)
    
-   胶囊样式进度条
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/zJKDAxT5Shy4-RYVv6ggCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=EEC4BB2BE146B2080AF411AB4F9903C7CAD47D10385AD122FB1BBCBBA955044D)
    
    -   头尾两端圆弧处的进度展示效果与ProgressType.Eclipse样式一致。
        
    -   中段处的进度展示效果为矩形状长条，与ProgressType.Linear线性样式相似。
        
    -   组件高度大于宽度时，自适应垂直显示。
        
    
    Progress({ value: 10, total: 150, type: ProgressType.Capsule }).width(100).height(50)
    Progress({ value: 20, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Grey)
    Progress({ value: 50, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Blue).backgroundColor(Color.Black)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/wib7SNbqROmyGUFyH58BtA/zh-cn_image_0000002569018533.png?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=D888F24169C99DBFA2281C788F334B2811C5CBBE9DAF1BDB5EA3777D6B1A1610)
    

#### 场景示例

更新当前进度值，如应用安装进度条，可通过点击Button增加progressValue，value属性将progressValue设置给Progress组件，进度条组件即会触发刷新，更新当前进度。

@Entry
@Component
struct ProgressCase1 {
  @State progressValue: number = 0;    // 设置进度条初始值为0
  build() {
    Column() {
      Column() {
        Progress({value:0, total:100, type:ProgressType.Capsule}).width(200).height(50).value(this.progressValue)
        Row().width('100%').height(5)
        // 请将$r('app.string.progress\_add')替换为实际资源文件，在本示例中该资源文件的value值为"进度条+5"
        Button($r('app.string.progress\_add'))
          .onClick(()=>{
            this.progressValue += 5;
            if (this.progressValue > 100){
              this.progressValue = 0;
            }
          })
      }
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/_DtM4VkUSguasa5IumVAHA/zh-cn_image_0000002568898523.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013539Z&HW-CC-Expire=86400&HW-CC-Sign=6D766ED87DFE101566E4796C058210FBD3C9B7452AD5B13F3C6BEB6683A62D90)
