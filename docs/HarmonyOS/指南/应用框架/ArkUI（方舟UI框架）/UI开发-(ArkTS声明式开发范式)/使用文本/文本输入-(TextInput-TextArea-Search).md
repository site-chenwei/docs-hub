---
title: "文本输入 (TextInput/TextArea/Search)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "使用文本"
  - "文本输入 (TextInput/TextArea/Search)"
captured_at: "2026-04-17T01:35:37.669Z"
---

# 文本输入 (TextInput/TextArea/Search)

TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)和[TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)组件的API文档。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)组件的API文档。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/VIBIXu_tRx26yxbzqB_bTg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=97091861938D3DB7D5EAF57F29452D0B842F0806724F75498DFBEAF47DDE0261)

仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件。

#### 创建输入框

TextInput是单行输入框，TextArea是多行输入框，Search是搜索框。通过以下接口创建这些组件。

```ts
TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

```ts
TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```ts
Search(options?:{placeholder?: ResourceStr, value?: ResourceStr, controller?: SearchController, icon?: string})
```

-   单行输入框。
    
    TextInput()
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ADE_bGjxT8CgaRRz9cG6oQ/zh-cn_image_0000002569018447.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DE634D21F0F708B08A6A0F6F2E973DC170585144B521F2052761D65C0BDE4C51)
    
-   多行输入框。
    
    TextArea()
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/xpFAmvHHRiqI9iRmjDxqjg/zh-cn_image_0000002568898437.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=4181033B7328709EA6C83DAB5DE67BE723162932EC0D4CA886BE7870022E816E)
    
-   多行输入框文字超出一行时会自动折行。
    
    /\* 请将$r('app.string.CreatTextInput\_textContent')替换为实际资源文件，在本示例中该资源文件的value值为
     \* "我是TextArea我是TextArea我是TextArea我是TextArea"
     \*/
    TextArea({ text: $r('app.string.CreatTextInput\_textContent') })
      .width(300)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/-swSamrXTqS0hBybEPXhZw/zh-cn_image_0000002538018732.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=AAE78FC2EB0F583BA8619100E1ACA992AD4F2F9B2A25C7F17F65BE999B7BEB0A)
    
-   搜索框。
    
    Search()
      // 请将$r('app.string.Creat\_TextInput\_Content')替换为实际资源文件，在本示例中该资源文件的value值为"搜索"
      .searchButton($r('app.string.Creat\_TextInput\_Content'))
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/kwyWNOqvS0iButU_xBk8AQ/zh-cn_image_0000002538178660.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F6D164251F15ABF285A7DB0FC2082707A15F8BDCCFD335AC6DCB4C3452BCE11A)
    

#### 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER\_NAME用户名输入模式、NEW\_PASSWORD新密码输入模式、NUMBER\_PASSWORD纯数字密码输入模式、NUMBER\_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#type)属性进行设置：

#### \[h2\]基本输入模式（默认类型）

TextInput()
  .type(InputType.Normal)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/7v2nkX7GT5GnhOObcaPl-Q/zh-cn_image_0000002569018449.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D5C7BF58268AEBF1137FA5F99C3DE1A538D945C9214C0EBA068CF123252E8F36)

#### \[h2\]密码模式

包括Password密码输入模式、NUMBER\_PASSWORD纯数字密码模式、NEW\_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

TextInput()
  .type(InputType.Password)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/x-QfCFueQI6Sk5Y7cbhYTQ/zh-cn_image_0000002568898439.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=AAA81E74D15F5D080927DEF163A709801088177CB9807E198A3B405A67281549)

#### \[h2\]邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

TextInput()
  .type(InputType.Email)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/YG_7JocQTW2VmWhVnA5_YA/zh-cn_image_0000002538018734.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=8CE8F99F9055669BC127FCBAC14CFD65E406A8704F8A76B3C17BADB82D0340A9)

#### \[h2\]纯数字输入模式

纯数字输入模式的输入框，只能输入数字\[0-9\]。

TextInput()
  .type(InputType.Number)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/lmFB62I5QIqDIbg5ShTZvA/zh-cn_image_0000002538178662.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=546414C3C0A5B36BC4C6DBDFD23F2F3688318681D6945B7011B9536908E462A9)

#### \[h2\]电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。

TextInput()
  .type(InputType.PhoneNumber)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/AiNuTHE7T0SRmJaajejlAw/zh-cn_image_0000002569018451.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=19173643174AFB2E9B12DF2DE8771C495DD175755D69310684EC88485844F89E)

#### \[h2\]带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字\[0-9\]和小数点，只能存在一个小数点。

TextInput()
  .type(InputType.NUMBER\_DECIMAL)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/IczmZ6HaRruWkgA294ZRiw/zh-cn_image_0000002568898441.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=91180D1C9D5C89548B93CCE44E5813EA74657CB785BE81CA458C32F5E6B40669)

#### \[h2\]带URL的输入模式

带URL的输入模式，无特殊限制。

TextInput()
  .type(InputType.URL)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KD5_0QzgTc-jDL_cxuJIBw/zh-cn_image_0000002538018736.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=7004EDCE08ED66A553EF47A51F6B54943E6A325EEF066D7900B26DFE4896ED38)

#### 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

#### \[h2\]默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

TextArea()
  .style(TextContentStyle.DEFAULT)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/yVId2fCPQbO99KbYeJbUug/zh-cn_image_0000002538178664.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D1BF4D8C366F55854541B826A9BCCE8C243C11F7E5029C96B68B6A496452DDE3)

#### \[h2\]内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

TextArea()
  .style(TextContentStyle.INLINE)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/P9v41EKnTgmE2lGlYIur2Q/zh-cn_image_0000002569018453.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=EF2CC054EA62E547C2A2CAC4D3D965BC5DB7637C821A5763FDB8F0E9391F8B7C)

#### 自定义样式

-   设置无输入时的提示文本。
    
    // 请将$r('app.string.i\_am\_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
    TextInput({ placeholder: $r('app.string.i\_am\_placeholder') })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/HeMHkpSoQCydNuPdHVtqtw/zh-cn_image_0000002568898443.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=CCA903ACC25B9478A42211E23508681EB6C2B64DE630C51CCC0F567F2E118E39)
    
-   设置输入框当前的文本内容。
    
    TextInput({
      // 请将$r('app.string.i\_am\_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
      placeholder: $r('app.string.i\_am\_placeholder'),
      // 请将$r('app.string.i\_am\_current\_text\_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
      text: $r('app.string.i\_am\_current\_text\_content')
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/DEgVz6LmTROz6cLFBgtsXw/zh-cn_image_0000002538018738.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F5B7D52F5ED91A5831A67C5FB7E7866A9BBA473564B2513EAB1EB5F2844DE78E)
    
-   添加backgroundColor改变输入框的背景颜色。
    
    TextInput({
      // 请将$r('app.string.i\_am\_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
      placeholder: $r('app.string.i\_am\_placeholder'),
      // 请将$r('app.string.i\_am\_current\_text\_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
      text: $r('app.string.i\_am\_current\_text\_content')
    })
      .backgroundColor(Color.Pink)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/gz9ajTSKQTuA7JG6flL-hw/zh-cn_image_0000002538178666.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3620E7F6E952034607550A0E4E65D035EB83C68BD0A4B89850517533484EC063)
    
    更丰富的样式可以结合[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)实现。
    

#### 添加事件

文本框主要用于获取用户输入的信息，并将信息处理成数据进行上传，绑定[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onchange)事件可以获取输入框内改变的文本内容，绑定[onSubmit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsubmit)事件可以获取回车提交的文本信息，绑定[onTextSelectionChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ontextselectionchange10)事件可以获取文本选中时手柄的位置信息或者编辑时光标的位置信息等等。用户也可以使用通用事件进行相应的交互操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/IuFXCKTfSrSon7RD0PB6OQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=373007CC8AE1A2F07604F555CF1B22EB398D0E71AAEB0800EE2404F7DEFC6847)

在密码模式下，设置[showPassword](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showpassword12)属性时，在[onSecurityStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsecuritystatechange12)回调中，建议增加状态同步，具体详见如下示例。

[onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)回调仅支持系统输入法的场景。

[onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)的回调时序晚于[onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)，早于[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)。

import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = '\[Sample\_Textcomponent\]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent\_';

@Entry
@Component
struct TextInputEventAdd {
  @State text: string = '';
  @State textStr1: string = '';
  @State textStr2: string = '';
  @State textStr3: string = '';
  @State textStr4: string = '';
  @State textStr5: string = '';
  @State textStr6: string = '';
  @State textStr7: string = '';
  @State textStr8: string = '';
  @State textStr9: string = '';
  @State passwordState: boolean = false;
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      Column() {
        Text(\`${this.textStr1}\\n${this.textStr2}\\n${this.textStr3}
          \\n${this.textStr4}\\n${this.textStr5}\\n${this.textStr6}
          \\n${this.textStr7}\\n${this.textStr8}\\n${this.textStr9}\`)
          .fontSize(20)
          .width('70%')
        TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
          .type(InputType.Password)
          .showPassword(this.passwordState)
          .onChange((value: string) => {
            // 文本内容发生变化时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onChange is triggering: ' + value);
            this.textStr1 = \`onChange is triggering: ${value}\`;
          })
          .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
            // 按下输入法回车键时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onSubmit is triggering: ' + enterKey + event.text);
            this.textStr2 = \`onSubmit is triggering: ${enterKey} ${event.text}\`;
          })
          .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
            // 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onTextSelectionChange is triggering: ' + selectionStart + selectionEnd);
            this.textStr3 = \`onTextSelectionChange is triggering: ${selectionStart} ${selectionEnd}\`;
          })
          .onSecurityStateChange((isShowPassword: boolean) => {
            // 密码显隐状态切换时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onSecurityStateChange is triggering: ' + isShowPassword);
            this.passwordState = isShowPassword;
            this.textStr4 = \`onSecurityStateChange is triggering: ${isShowPassword}\`;
          })
          .onWillInsert((info: InsertValue) => {
            // 在将要输入时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr5 = \`onWillInsert is triggering: ${info.insertValue} ${info.insertOffset}\`;
            return true;
          })
          .onDidInsert((info: InsertValue) => {
            // 在输入完成时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr6 = \`onDidInsert is triggering: ${info.insertValue} ${info.insertOffset}\`;
          })
          .onWillDelete((info: DeleteValue) => {
            // 在将要删除时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr7 = \`onWillDelete is triggering: ${info.deleteValue} ${info.deleteOffset}\`;
            return true;
          })
          .onDidDelete((info: DeleteValue) => {
            // 在删除完成时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr8 = \`onDidDelete is triggering: ${info.deleteValue} ${info.deleteOffset}\`;
          })
          .onFocus(() => {
            // 绑定通用事件，输入框获焦时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onFocus is triggering');
            this.textStr9 = \`onFocus is triggering\`;
          })
      }.width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/tpFYWA_rRMqjEBpLFnd_tw/zh-cn_image_0000002569018455.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=44CCF777F73864B556DFCE3570ADBED3F7BF15EF54C8E155E4377EFA1EEBCAA1)

#### 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、分享的菜单。

TextInput:

// 请将$r('app.string.show\_selected\_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
TextInput({ text: $r('app.string.show\_selected\_menu') })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/wjEJ2ZegRT6K_Hcf6amnOw/zh-cn_image_0000002568898445.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=29FCAA910873997EC024C372BB0FB7E10BB89A3B498BFF1500888DCD2B6919A7)

TextArea:

// 请将$r('app.string.show\_selected\_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
TextArea({ text: $r('app.string.show\_selected\_menu') })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/eSV_20UMTcWUTUvoyta5vA/zh-cn_image_0000002538018740.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=23300642DC7824E8141643CCEFDDAEDD420650D99C090989A5C389DF18E96615)

#### 禁用系统服务类菜单

从API version 20开始，支持使用[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)方法屏蔽文本选择菜单中的所有系统服务菜单项。

import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableSystemServiceMenuItem {
  aboutToAppear(): void {
    // 禁用所有系统服务菜单项
    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {
    // 页面消失时恢复系统服务菜单项
    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {
        // 请将$r('app.string.ProhibitSelectMenu\_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
        TextInput({ text: $r('app.string.ProhibitSelectMenu\_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems不包含被屏蔽的系统菜单项
              return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/DUNa7P_mReCKdZkkSNRR3Q/zh-cn_image_0000002538178668.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=81A5FB788A66AAF109D0827FD8A74030C1CE942165439791B8A825F30FC232AA)

从API version 20开始，支持使用[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)方法屏蔽文本选择菜单中指定的系统服务菜单项。

import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableMenuItem {
  aboutToAppear(): void {
    // 禁用搜索，翻译和AI帮写
    TextMenuController.disableMenuItems(\[TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE, TextMenuItemId.AI\_WRITER\])
  }

  aboutToDisappear(): void {
    // 页面消失时恢复系统服务菜单项
    TextMenuController.disableMenuItems(\[\])
  }

  build() {
    Row() {
      Column() {
        // 请将$r('app.string.ProhibitSelectMenu\_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
        TextInput({ text: $r('app.string.ProhibitSelectMenu\_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems不包含搜索和翻译
              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/CO00EdZDSTWydd_Eoqpg3Q/zh-cn_image_0000002569018457.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=A5E6094E11F546723E381CADCAC0102E3537B281CB7054EFD826D96C30C9E608)

#### 自动填充

输入框可以通过[contentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12)属性设置自动填充类型。

支持的类型请参考[ContentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12枚举说明)。

// 请将$r('app.string.Auto\_Fill\_PlaceHolder')替换为实际资源文件，在本示例中该资源文件的value值为"输入你的邮箱..."
TextInput({ placeholder: $r('app.string.Auto\_Fill\_PlaceHolder') })
  .width('95%')
  .height(40)
  .margin(20)
  .contentType(ContentType.EMAIL\_ADDRESS)

#### 设置属性

-   设置省略属性。
    
    输入框可以通过[ellipsisMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)属性设置省略位置。
    
    ellipsisMode属性需要配合[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。
    
    // 请将$r('app.string.Set\_Omission\_Property\_textContent')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示省略模式"
    TextInput({ text: $r('app.string.Set\_Omission\_Property\_textContent') })
      .textOverflow(TextOverflow.Ellipsis)
      .ellipsisMode(EllipsisMode.END)
      .style(TextInputStyle.Inline)
      .fontSize(30)
      .margin(30)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/5Cfu8f68RAGNYkkMvRVvfA/zh-cn_image_0000002568898447.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=EBB2144BEB4486CCFDECDD984B92A0124A34970F84116746D614A9FA711D99B5)
    
-   设置文本描边属性。
    
    从API version 20开始，输入框可以通过[strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokewidth20)和[strokeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokecolor20)属性设置文本的描边宽度及颜色。
    
    TextInput({ text: 'Text with stroke' })
      .width('100%')
      .height(60)
      .borderWidth(1)
      .fontSize(40)
      .strokeWidth(LengthMetrics.px(3.0))
      .strokeColor(Color.Red)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/gnM5gPvLQ2mDlHU-B60Yqw/zh-cn_image_0000002538018742.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=B6448B31F9B49CCFF441FFFA30D776E443039ADB164E882B4E0B91F73A06DCE1)
    

#### 设置文本行间距

从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

TextArea({
  text: 'The line spacing of this TextArea is set to 20\_px, and the spacing is effective only between the lines.'
})
  .fontSize(22)
  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/1RPo5QH3SGG4_TPR0zsoJw/zh-cn_image_0000002538178670.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=271248D5C790F62694853C8BA66017E28AC21C2B007DA3F9E986E27A61B74241)

#### 键盘避让

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)。

@Entry
@Component
struct KeyboardAvoid {
  placeHolderArr: string\[\] = \['1', '2', '3', '4', '5', '6', '7'\];

  build() {
    Scroll() {
      Column() {
        ForEach(this.placeHolderArr, (placeholder: string) => {
          TextInput({ placeholder: 'TextInput ' + placeholder })
            .margin(30)
            // ···
        })
      }
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/eIja6VhHQ-6NkrdynZwdFQ/zh-cn_image_0000002569018459.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=8BB0E5E3A4B41C96EF1D992EEC2BA1159DC81072A58E616C85EAFCC9FD35B28D)

#### 光标避让

[keyBoardAvoidMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e#keyboardavoidmode11)枚举中的OFFSET和RESIZE在键盘抬起后，不支持二次避让。如果想要支持光标位置在点击或者通过接口设置变化后发生二次避让，可以考虑使用OFFSET\_WITH\_CARET和RESIZE\_CARET替换原有的OFFSET和RESIZE模式。

对于滚动容器更推荐使用RESIZE\_WITH\_CARET，非滚动容器应该使用OFFSET\_WITH\_CARET。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { KeyboardAvoidMode } from '@kit.ArkUI';

// Used in UIAbility
onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err, data) => {
    let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
    windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET\_WITH\_CARET);
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  });
}

@Entry
@Component
struct CursorAvoid {
  @State caretPosition: number = 600;
  areaController: TextAreaController = new TextAreaController();
  text = 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot,' +
    ' or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy,' +
    ' totally forgetting that there is something happy in our own life.\\
    So the best way to destroy happiness is to look at something and focus on even the smallest flaw. ' +
    'It is the smallest flaw that would make us complain. And it is the complaint that leads to us becoming unhappy.\\
    If one chooses to be happy, he will be blessed; if he chooses to be unhappy, he will be cursed. ' +
    'Happiness is just what you think will make you happy.' +
    'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, ' +
    'or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life.\\
  ';

  build() {
    Scroll() {
      Column() {
        Row() {
          Button('CaretPosition++: ' + this.caretPosition).onClick(() => {
            this.caretPosition += 1;
          }).fontSize(10)
          Button('CaretPosition--: ' + this.caretPosition).onClick(() => {
            this.caretPosition -= 1;
          }).fontSize(10)
          Button('SetCaretPosition: ').onClick(() => {
            this.areaController.caretPosition(this.caretPosition);
          }).fontSize(10)
        }

        TextArea({ text: this.text, controller: this.areaController })
          .width('100%')
          .fontSize('20fp')
      }
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/UaV035EuTf-r0L7CpylyBw/zh-cn_image_0000002568898449.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C258FA7E5BC6B5D85E91BB5663FA5E4CA1B83BDD4834FD23A79E752C5A10F8D6)

#### 常见问题

#### \[h2\]如何设置TextArea的文本最少展示行数并自适应高度

**问题现象**

设置TextArea的初始高度来控制最少文本展示行数，当输入文本超过初始高度时，TextArea的高度自适应。

**解决措施**

设置[minLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minlines20)（从API version 20开始），或者设置height为"auto"，并使用[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)自行计算高度。

import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct TextExample {
  private textAreaPadding = 12;
  private setMaxLines = 3;
  private resourceManager = this.getUIContext().getHostContext()?.resourceManager;
  // 请在resources\\base\\element\\string.json文件中配置name为'NormalQuestion\_change'，value为非空字符串的资源
  private changeText = this.resourceManager?.getStringByNameSync('NormalQuestion\_change') as string;
  @State fullText: string = this.changeText;
  @State originText: string = this.changeText;
  @State uiContext: UIContext = this.getUIContext();
  @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.originText,
    fontSize: 18
  });

  build() {
    Column() {
      TextArea({ text: 'minLines: ' + this.fullText })
        .fontSize(18)
        .width(300)
        .minLines(3)

      Blank(50)

      TextArea({ text: 'constraintSize: ' + this.fullText })
        .fontSize(18)
        .padding({ top: this.textAreaPadding, bottom: this.textAreaPadding })
        .width(300)
        .height('auto')
        .constraintSize({
          // 结合padding计算，设置至少显示this.setMaxLines行文本
          // 若涉及适老化字号缩放，需要监听并调整高度
          minHeight: this.textAreaPadding \* 2 +
            this.setMaxLines \* this.getUIContext().px2vp(Number(this.textSize.height))
        })

      Blank(50)
      // 请将$r('app.string.NormalQuestion\_AddInput')替换为实际资源文件，在本示例中该资源文件的value值为"增加输入"
      Button($r('app.string.NormalQuestion\_AddInput'))
        .onClick(() => {
          this.fullText += this.changeText;
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .padding({ top: 30 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/sxf5m70UQfS-ksWZoVNdjw/zh-cn_image_0000002538018744.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=A9967FD6363E6E37BC3D8FCF7FA503FE6D8593FFA02DED27629738D88D0196F5)
