---
title: "按钮 (Button)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-button"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "表单选择"
  - "按钮 (Button)"
captured_at: "2026-04-17T01:35:37.824Z"
---

# 按钮 (Button)

Button是按钮组件，通常用于响应用户的点击操作，其类型包括胶囊按钮、圆形按钮、普通按钮、圆角矩形按钮。Button作为容器使用时可以通过添加子组件实现包含文字、图片等元素的按钮。具体用法请参考[Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button)。

#### 创建按钮

Button通过调用接口来创建，接口调用有以下两种形式：

-   通过label和[ButtonOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttonoptions对象说明)创建不包含子组件的按钮。以ButtonOptions中的type和stateEffect为例。
    
    ```ts
    Button(label?: ResourceStr, options?: { type?: ButtonType, stateEffect?: boolean })
    ```
    
    其中，label用来设置按钮文字，type用于设置Button类型，stateEffect属性设置Button是否开启点击效果。
    
    Button('Ok', { type: ButtonType.Normal, stateEffect: true })
      .borderRadius(8)
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/1YnUaMDCShiVDF9rW8D-Ug/zh-cn_image_0000002568898503.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=795B1CE01F6D89B70C61AC457BA214CD9038119760ABFD08665929FB8704F057)
    
-   通过[ButtonOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttonoptions对象说明)创建包含子组件的按钮。以ButtonOptions中的type和stateEffect为例。
    
    ```ts
    Button(options?: {type?: ButtonType, stateEffect?: boolean})
    ```
    
    只支持包含一个子组件，子组件可以是基础组件或者容器组件。
    
    Button({ type: ButtonType.Normal, stateEffect: true }) {
      Row() {
        // 请将$r('app.media.loading')替换为实际资源文件
        Image($r('app.media.loading')).width(20).height(40).margin({ left: 12 })
        Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
      }.alignItems(VerticalAlign.Center)
    }.borderRadius(8).backgroundColor(0x317aff).width(90).height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/czV0bry_RgmTXIqGtMhaMQ/zh-cn_image_0000002538018798.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=24AC24343498456575E1AF948DA33E7E24D46854045BF50A48ABD60F3A51F0AD)
    

#### 设置按钮类型

Button有四种可选类型，分别为胶囊类型（Capsule）、圆形按钮（Circle）、普通按钮（Normal）和圆角矩形按钮（ROUNDED\_RECTANGLE），通过type进行设置。

-   胶囊按钮（默认类型）。
    
    此类型按钮的圆角自动设置为高度的一半，不支持通过borderRadius属性重新设置圆角。
    
    Button('Disable', { type: ButtonType.Capsule, stateEffect: false })
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/MMGqKvTcQ-yLZ8hHvSNDbA/zh-cn_image_0000002538178726.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D84BD6C2B4C9AFF378136A4B34F4B4CD664D600BC642AB0685E900CC71F3FC7F)
    
-   圆形按钮。
    
    此类型按钮为圆形，不支持通过borderRadius属性重新设置圆角。
    
    Button('Circle', { type: ButtonType.Circle, stateEffect: false })
      .backgroundColor(0x317aff)
      .width(90)
      .height(90)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/umlF0X6YTsG_pmKhPqBT0Q/zh-cn_image_0000002569018515.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=CA744DC4A12F209ECD8E64A3976DBF61C59711FDD7842AF2499F1E445E7CA975)
    
-   普通按钮。
    
    此类型的按钮默认圆角为0，支持通过borderRadius属性重新设置圆角。
    
    Button('Ok', { type: ButtonType.Normal, stateEffect: true })
      .borderRadius(8)
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/QMeny6IZQiSvbN-LrvWnPQ/zh-cn_image_0000002568898505.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=956D3EC43C712D0DEE299D02D75863D80583E3DA9A170F33718AB2C253235CDE)
    
-   圆角矩形按钮。
    
    当[controlSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#controlsize11)为NORMAL时，默认圆角大小为20vp，[controlSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#controlsize11)为SMALL时，圆角大小为14vp，支持通过borderRadius属性重新设置圆角。
    
    Button('Disable', { type: ButtonType.ROUNDED\_RECTANGLE, stateEffect: true })
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/N1E_kHVgQ2q2xkv3eRsoqw/zh-cn_image_0000002538178726.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=60A0751FDA288FD68FD39CDE38194DAA06361E5BA1AEC399AD4BCB950536B1EB)
    

#### 自定义样式

-   设置边框弧度。
    
    使用通用属性来自定义按钮样式。例如通过borderRadius属性设置按钮的边框弧度。
    
    Button('circle border', { type: ButtonType.Normal })
      .borderRadius(20)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/2e-QI9d5SV-rmW4Dd2f78w/zh-cn_image_0000002538018800.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3AFE217860F8CA57671A1E42B5BF5AD7C63327EBD4D7D81C51CD3EA8E8764CEF)
    
-   设置文本样式。
    
    通过添加文本样式设置按钮文本的展示样式。
    
    Button('font style', { type: ButtonType.Normal })
      .fontSize(20)
      .fontColor(Color.Pink)
      .fontWeight(800)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/vUOEI7p0QcaiV3fYHALs7A/zh-cn_image_0000002538178728.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3FB9A64F8AB15A1A44C9DE874EDB8238BC97CD845D9DD3DDFEF222FFECCE25BA)
    
-   设置背景颜色。
    
    添加backgroundColor属性设置按钮的背景颜色。
    
    Button('background color').backgroundColor(0xF55A42)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/3Glcba8SRJepTkGD289fBA/zh-cn_image_0000002569018517.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DD38B866C74B309C16DAF342D471178EE84F8E18893E3B15CDCF299BE5B72559)
    
-   创建功能型按钮。
    
    创建删除操作的按钮。
    
    Button({ type: ButtonType.Circle, stateEffect: true }) {
      // 请将$r('app.media.ic\_public\_delete\_filled3')替换为实际资源文件
      Image($r('app.media.ic\_public\_delete\_filled')).width(30).height(30)
    }.width(55).height(55).margin({ 'left': 20 }).backgroundColor(0xF55A42)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/796uPcP3RZqlkv1Sl6BG0g/zh-cn_image_0000002568898507.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=9558BBD5FD4C2B5A2C4F0492BAF75CFFDC49135BFBF88BDBCA29F90AAA1E77BE)
    

#### 添加事件

Button组件通常用于触发某些操作，可以绑定onClick事件来响应点击操作后的自定义行为。

Button('Ok', { type: ButtonType.Normal, stateEffect: true })
  .onClick(()=>{
    hilog.info(DOMAIN, 'testTag', 'Button onClick');
  }).margin(10)

#### 场景示例

-   用于启动操作。
    
    可以用按钮启动任何用户界面元素，按钮会根据用户的操作触发相应的事件。例如，在List容器里通过点击按钮进行页面跳转。
    
    const DOMAIN = 0x0000;
    // xxx.ets
    @Entry
    @Component
    export struct ButtonCaseTouch {
      pathStack: NavPathStack = new NavPathStack();
    
      @Builder
      PageMap(name: string) {
        if (name === 'first\_page') {
          pageOneTmp()
        } else if (name === 'second\_page') {
          pageTwoTmp()
        } else if (name === 'third\_page') {
          pageThreeTmp()
        }
      }
    
      build() {
        NavDestination() {
          Navigation(this.pathStack) {
            List({ space: 4 }) {
              ListItem() {
                Button('First').onClick(() => {
                  this.pathStack.pushPath({ name: 'first\_page' });
                })
                  .width('100%')
              }
    
              ListItem() {
                Button('Second').onClick(() => {
                  this.pathStack.pushPath({ name: 'second\_page' });
                })
                  .width('100%')
              }
    
              ListItem() {
                Button('Third').onClick(() => {
                  this.pathStack.pushPath({ name: 'third\_page' });
                })
                  .width('100%')
              }
            }
            .listDirection(Axis.Vertical)
            .backgroundColor(0xDCDCDC).padding(20)
          }
          .mode(NavigationMode.Stack)
          .navDestination(this.PageMap)
        }
      }
    }
    
    // pageOne
    @Component
    export struct pageOneTmp {
      pathStack: NavPathStack = new NavPathStack();
    
      build() {
        NavDestination() {
          Column() {
            Text('first\_page')
          }.width('100%').height('100%')
        }.title('pageOne')
        .onBackPressed(() => {
          const popDestinationInfo = this.pathStack.pop(); // 弹出路由栈栈顶元素
          // 请将$r('app.string.return\_value')替换为实际资源文件，在本示例中该资源文件的value值为"返回值"
          hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return\_value') + JSON.stringify(popDestinationInfo));
          return true;
        })
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        })
      }
    }
    
    // pageTwo
    @Component
    export struct pageTwoTmp {
      pathStack: NavPathStack = new NavPathStack();
    
      build() {
        NavDestination() {
          Column() {
            Text('second\_page')
          }.width('100%').height('100%')
        }.title('pageTwo')
        .onBackPressed(() => {
          const popDestinationInfo = this.pathStack.pop(); // 弹出路由栈栈顶元素
          // 请将$r('app.string.return\_value')替换为实际资源文件，在本示例中该资源文件的value值为"返回值"
          hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return\_value') + JSON.stringify(popDestinationInfo));
          return true;
        })
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        })
      }
    }
    
    // pageThree
    @Component
    export struct pageThreeTmp {
      pathStack: NavPathStack = new NavPathStack();
    
      build() {
        NavDestination() {
          Column() {
            Text('third\_page')
          }.width('100%').height('100%')
        }.title('pageThree')
        .onBackPressed(() => {
          const popDestinationInfo = this.pathStack.pop(); // 弹出路由栈栈顶元素
          /// 请将$r('app.string.return\_value')替换为实际资源文件，在本示例中该资源文件的value值为"返回值"
          hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return\_value') + JSON.stringify(popDestinationInfo));
          return true;
        })
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        })
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/5wxLZlotR5aEj2tZ3RBfHQ/zh-cn_image_0000002538018802.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=4D17FF9FBD345FE32E46E3F4A68CB16CBA5D723D64C3E89C231F1A3EC449168D)
    
-   用于提交表单。
    
    在用户登录/注册页面，使用按钮进行登录或注册操作。
    
    // xxx.ets
    const DOMAIN = 0x0000;
    @Entry
    @Component
    export struct ButtonCaseLogin {
      build() {
        NavDestination() {
          Column() {
            TextInput({ placeholder: 'input your username' }).margin({ top: 20 })
            TextInput({ placeholder: 'input your password' }).type(InputType.Password).margin({ top: 20 })
            Button('Register').width(300).margin({ top: 20 })
              .onClick(() => {
                // 需要执行的操作
              })
            // ···
          }.padding(20)
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/XoHoECupT8eg7pY62YldEw/zh-cn_image_0000002538178730.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=2171832CB94731B6787B05482833471BA8CA154B3A79310DC473226F0E4E2A6F)
    
-   悬浮按钮。
    
    在可以滑动的界面，滑动时按钮始终保持悬浮状态。
    
    // xxx.ets
    @Entry
    @Component
    export struct HoverButtonExample {
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
      build() {
        NavDestination() {
          Stack() {
            List({ space: 20, initialIndex: 0 }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('' + item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(0xFFFFFF)
                }
              }, (item: number) => item.toString())
            }.width('90%')
    
            Button() {
              // 请将$r('app.media.ic\_public\_add')替换为实际资源文件
              Image($r('app.media.ic\_public\_add'))
               .width(50)
               .height(50)
            }
            .width(60)
            .height(60)
            .position({ x: '80%', y: 600 })
            .shadow({ radius: 10 })
            .onClick(() => {
              // 需要执行的操作
            })
          }
          .width('100%')
          .height('100%')
          .backgroundColor(0xDCDCDC)
          .padding({ top: 5 })
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/FyaQaLAvSXqw26iOSf-14Q/zh-cn_image_0000002569018519.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=0847B2BB4EBBE911F24AE760B442155832621D00F61931A3C2ABBEDA28F1E05A)
