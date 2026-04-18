---
title: "Code Linter代码检查"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查"
captured_at: "2026-04-17T01:36:44.763Z"
---

# Code Linter代码检查

Code Linter支持对模块内文件或文件夹中的代码进行最佳实践/编程规范方面的检查。检查规则支持配置，配置方式请参考[配置代码检查规则](#section19310459444)。

开发者可根据扫描结果中告警提示手工修复代码缺陷，或者执行一键式自动修复，在代码开发阶段，确保代码质量。

#### 配置代码检查规则

新建工程时，工程根目录下默认创建code-linter.json5配置文件，可对代码检查的范围及对应生效的检查规则进行配置。若使用历史工程进行开发，可在工程中右键选择**Code Linter > Generate Config File**创建code-linter.json5配置文件。

其中files和ignore配置项共同确定了代码检查范围，ruleSet和rules配置项共同确定了生效的规则范围。具体配置项功能如下：

**files**：配置待检查的文件名单，如未指定目录，将检查当前被选中的文件或文件夹中所有的.ets文件。

**ignore**：配置无需检查的文件目录，其指定的目录或文件需使用相对路径格式，相对于code-linter.json5所在工程根目录，例如：build/\*\*/\*。

**ruleSet**：配置检查使用的规则集，规则集支持一次导入多条规则。规则详情请参见[Code Linter代码检查规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codelinter-rule)。目前支持的规则集包括：

-   通用规则@typescript-eslint
-   安全规则@security
-   性能规则@performance
-   预览规则@previewer
-   一次开发多端部署规则@cross-device-app-dev
-   ArkTS代码风格规则@hw-stylistic
-   正确性规则@correctness
-   兼容性规则@compatibility
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/DEwKgwScTBK0b4OiMp2bQA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=8D2156D3B302D2C64CA5EB3CFE0E5B0EB89A9A00A166D0988FD59860389F06CD)
    
    -   以上规则集均分为all和recommended两种规则集。all规则集是规则全集，包含所有规则；recommended规则集是推荐使用的规则集合。all规则集包含recommended规则集。
    -   不在工程根目录新建code-linter.json5文件的情况下，Code Linter默认会检查@performance/recommended和@typescript-eslint/recommended规则集包含的规则。
    

**rules**：可以基于ruleSet配置的规则集，新增额外规则项，或修改ruleSet中规则默认配置，例如：将规则集中某条规则告警级别由warn改为error。

**overrides**：针对工程根目录下部分特定目录或文件，可配置定制化检查的规则。

**extRuleSet**：配置需要检查的自定义规则，具体请参考：[自定义规则开发指南](https://gitcode.com/openharmony-sig/homecheck/blob/master/document/developer/ExtRule自定义规则开发指南.md)。该字段从DevEco Studio 5.1.0 Release版本开始支持。

{
  "files":   //用于表示配置适用的文件范围的 glob 模式数组。在没有指定的情况下，应用默认配置
  \[
    "\*\*/\*.js", //字符串类型
    "\*\*/\*.ts"
  \],
  "ignore":  //一个表示配置对象不应适用的文件的 glob 模式数组。如果没有指定，配置对象将适用于所有由 files 匹配的文件
  \[
    "build/\*\*/\*",    //字符串类型
    "node\_modules/\*\*/\*"
  \],
  "ruleSet":       //设置检查待应用的规则集
  \[
    "plugin:@typescript-eslint/recommended"    //快捷批量引入的规则集, 枚举类型：plugin:@typescript-eslint/all, plugin:@typescript-eslint/recommended, plugin:@cross-device-app-dev/all, plugin:@cross-device-app-dev/recommended等
  \],
  "rules":         //可以对ruleSet配置的规则集中特定的某些规则进行修改、去使能, 或者新增规则集以外的规则；ruleSet和rules共同确定了代码检查所应用的规则
  {
    "@typescript-eslint/no-explicit-any":  // ruleId后面跟数组时, 第一个元素为告警级别, 后面的对象元素为规则特定开关配置
    \[
      "error",              //告警级别: 枚举类型, 支持配置为suggestion, error, warn, off
      {
        "ignoreRestArgs": true   //规则特定的开关配置, 为可选项, 不同规则其下层的配置项不同
      }
    \],
    "@typescript-eslint/explicit-function-return-type": 2,   // ruleId后面跟单独一个数字时, 表示仅设置告警级别, 枚举值为: 3(suggestion), 2(error), 1(warn), 0(off)
    "@typescript-eslint/no-unsafe-return": "warn"            // ruleId后面跟单独一个字符串时, 表示仅设置告警级别, 枚举值为: suggestion, error, warn, off
  },
  "overrides":      //针对特定的目录或文件采用定制化的规则配置
  \[
    {
      "files":   //指定需要定制化配置规则的文件或目录
      \[
        "entry/\*\*/\*.ts"   //字符串类型
      \],
      "excluded":
      \[
        "entry/\*\*/\*.test.js" //指定需要排除的目录或文件, 被排除的目录或文件不会按照定制化的规则配置被检查; 字符串类型
      \],
      "rules":   //支持对overrides外公共配置的规则进行修改、去使能, 或者新增公共配置以外的规则; 该配置将覆盖公共配置
      {
        "@typescript-eslint/explicit-function-return-type":  // ruleId: 枚举类型
        \[
          "warn",     //告警级别: 枚举类型, 支持配置为error, warn, off; 覆盖公共配置, explicit-function-return-type告警级别为warn
          {
             "allowExpressions": true    //规则特定的开关配置, 为可选项, 不同规则其下层的配置项不同
          }
        \],
        "@typescript-eslint/no-unsafe-return": "off"   // 覆盖公共配置, 不检查no-unsafe-return规则
      },
      "extRules": {     //支持对overrides外自定义规则集配置的规则进行修改、去使能; 该配置将覆盖自定义规则配置
        "@extrulesproject/foreach-args-check": "off"   // 覆盖自定义规则配置, 不检查@extrulesproject/foreach-args-check规则
      }
    }
  \],
  "extRuleSet": \[     //自定义规则集的配置
    {
        "ruleSetName": "extrulesproject",     //自定义规则库的名称。格式为@group/packagename或者packagename，全局唯一。除@和/外，group和packagename只能包含小写字母、数字、下划线（\_）和中划线(-)。总长度小于等于128个字符。另外，group和packagename必须以字母开头，不能作为ArkTS的保留关键字
        "packagePath": "D:\\\\checker\\\\extrulesproject-1.0.0.tgz",     //自定义规则安装包路径，需使用绝对路径
        "extRules": {     //自定义规则名称以及告警等级，枚举值为: 3(suggestion), 2(error), 1(warn), 0(off)
          "@extrulesproject/foreach-args-check": 1
        }
    }
  \]
}

#### 通过DevEco Studio进行代码检查

#### \[h2\]操作方法

在已打开的代码编辑器窗口单击右键点击**Code Linter**，或在工程管理窗口中鼠标选中单个或多个工程文件/目录，右键选择**Code Linter** **> Full Linter**执行代码全量检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/he3Wrg_nRMm9BNKEPck6Cw/zh-cn_image_0000002530913722.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=67663B95AAAFECAEB9FCF94FBB94DC9A6B44745576AD75A1AADB170B356ADD00)

如只需对Git工程中增量文件（包含新增/修改/重命名）进行检查，可在commit界面右下角点击齿轮图标，选择**Incremental Linter**执行增量检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/_XA2Qx8xT0quBzEu7cqNyA/zh-cn_image_0000002530913730.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=83FB650445A699E5208AE92718D6F489D2166D0B7AF04101CBE8C779CCA1F6D2 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/82z-VwodRtmFSOf32H4giA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=02FF768250CF13F9996F0DF5BB945B909E950C3FD6F562BA35FEA30141EB8DC3)

-   若未配置代码检查规则文件，直接执行Code Linter，将按照默认的编程规范规则对.ets文件进行检查。
-   Code Linter不对如下文件及目录进行检查：
    -   src/ohosTest文件夹
    -   /src/test文件夹
    -   node\_modules文件夹
    -   oh\_modules文件夹
    -   build文件夹
    -   .preview文件夹
    -   hvigorfile.ts文件
    -   hvigorfile.js文件
    -   BuildProfile.ets文件

#### \[h2\]查看和处理代码检查结果

扫描完成后，在底部工具面板查看检查结果。勾选**Defects**中不同告警等级，可分别查看对应告警级别的信息。点击**Filter by scene**下拉菜单，可以筛选不同规则的检查结果。双击某条告警结果，可以跳转到对应代码缺陷位置；选中告警结果时，可以在右侧**Defect Description窗口**查看告警对应的规则详细说明，其中包含正向和反向示例，并根据其中的建议修改代码；搜索规则时，可设定是否全词匹配和大小写敏感。

单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/2nSH1s0vSCGyx_49qCRb3Q/zh-cn_image_0000002561833653.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=E675602567FFAAB5B8D6009A4AC299946BBDA42FEDD2E7BAB6A69EBFBC56296C)图标，查看可修复的代码规则，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/xZoeLObFTXCeYABK9rzx7A/zh-cn_image_0000002561833651.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=B7C1336EC1A8BB0AFD79333BF0F72FCDFA9504BCA47DB5F526415CBCDEBD6B80)代码修复图标，可以一键式批量修复告警，并刷新检查结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/qILsp5mMTcWRn14aRU3oBw/zh-cn_image_0000002530913734.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=FE2D021A4794D7B1CF90CFC5262ECCB7AA19308EFCDD23AD723E8E977CCB9AEE)

**屏蔽告警信息**：

-   在某些特殊场景下，若扫描结果中出现误报，点击单条告警结果后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jXn7xSizQp2_GNrxXAEsaA/zh-cn_image_0000002561833647.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=CCD734B71FCEF4B78204D584E17E4426F986DC862FA0E480F567C2D7A1685D3B)**Ignore**图标**，**可以忽略对告警所在行的code linter检查；或勾选文件名称或多条待屏蔽的告警，点击左侧工具面板**Ignore**图标批量执行操作；
-   在文件顶部添加注释/\* eslint-disable \*/可以屏蔽整个文件执行code linter检查，在eslint-disable 后加入一个或多个以逗号分隔的规则Id，可以屏蔽具体检查规则；
-   在需要忽略检查的代码块前后分别添加/\* eslint-disable \*/和/\* eslint-enable \*/添加注释信息，再执行**Code Linter，**将不再显示该代码块扫描结果；在待屏蔽的代码行前一行添加/\* eslint-disable-next-line \*/，也可屏蔽对该代码行的Code Linter检查。

如需恢复忽略的报错信息，可以直接删除该行上方的注释，重新执行**Code Linter**检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/pSvh3keEQOGuryBRoDkWuA/zh-cn_image_0000002561833661.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=2059052C7ED30B8F204A43B5DC2F80A6FE2C2F1D2A5A9A4605A8EFA88A886251)

**导出检查结果**：点击工具面板左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/9O3e6UCQQdyd1foEF3GN7g/zh-cn_image_0000002530753740.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=947B86884A96A036B468381B916FEC54D403FA1BBE91246C22533EE60A4D1E73)导出按钮，即可导出检查结果到excel文件，包含告警所在行，告警明细，告警级别等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/33c9QoUzQ5KkzFI7uIqY2g/zh-cn_image_0000002530913724.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=CB40E92606BFBD2B280894ADE37EC52138C015356835B2322E82B8FD98C7F0EE)

#### 通过命令行进行代码检查

从DevEco Studio 6.0.1 Beta1开始，支持通过命令行方式进行代码检查。在DevEco Studio安装包\\deveco-studio\\plugins\\codelinter\\run目录下打开cmd或者bash窗口，执行如下命令：

node ./index.js \[options\] \[dir\] 

options：可选配置，具体请参考[表codelinter命令行配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-codelinter#table25697717185)。

dir：待检查的工程根目录，可选，默认为当前上下文目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_sQqYjubQYWq6NzNowb2zg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=C09C2F04EDE4FDEA0DF090B44FB7F7D34299628DB737E1C9E51DE95F23D1AC0B)

使用命令行检查时，需要依赖于Node.js环境，本地安装的Node.js版本和DevEco Studio中tools目录下的Node.js版本需要保持一致。

#### 实践说明

以@typescript-eslint/no-restricted-syntax（使用某类语法时，codelinter告警）、@typescript-eslint/naming-convention（命名风格校验）和@hw-stylistic/file-naming-convention（检查代码文件的命名风格）三个规则为例，介绍Code Linter配置文件的使用方法。

#### \[h2\]示例1：调用类Foo下bar方法时，Code Linter告警

**在配置文件中定义规则**

在ArkTS工程中，pages/Index.ets文件下增加以下用例：

class Foo {
  static bar() {}
}

Foo.bar();

在工程根目录下新建code-linter.json5文件（文件名不可修改），新增以下配置：

{
  "rules": {
    "@typescript-eslint/no-restricted-syntax": \[
      // 告警级别: 枚举类型, 支持配置为error, warn, off
      "error",
      {
        // selector属性必选，配置要禁用的语法
        // 可通过特定DSL筛选待限制的语句，CallExpression表示方法调用表达式，后面的中括号里面是筛选条件（根据语法树Node节点来确定）
        // 其中callee.object.name根据指定的名称筛选调用方法的对象（class，namespace或module），以上示例中为"Foo"
        // callee.property.name则根据指定的名称筛选被调用的方法，以上示例中为"bar"
        "selector": "CallExpression\[callee.object.name='Foo'\]\[callee.property.name='bar'\]",
        // message属性可选，配置要展示的报错信息
        "message": "Foo.bar() is not allowed"
      }
    \]
  },
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/d699fEJkRAW-5iJ7kaGisA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=0EBBDDB5AD4DB90DD9B57C38A67280C10AD79E96392259955884FD5BE131EC16)

如需在code-linter.json5文件中配置其他字段，请参见[配置代码检查规则](#section19310459444)。

**执行代码检查**

对pages/Index.ets文件执行代码检查，检查结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/q8A3Xba9RsKkl_-6KDh7Uw/zh-cn_image_0000002561753677.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=D4A0481FBBDDC619E332BDD91520E5235C1B185496980A5E1A328EB8A01409F3)

#### \[h2\]示例2：对类名Foo的命名风格校验

**在配置文件中定义规则**

在ArkTS工程中，pages/Index.ets文件下增加以下用例：

class foo {    //此处构造一个命名风格错误的示例，foo为错误使用类名，正确类名应为Foo
  bar() {} 
}

在工程根目录下新建code-linter.json5文件，新增以下配置：

{
  "rules": {
    "@typescript-eslint/naming-convention": \[
      "error",
      {
        // selector属性必选，配置要检查的语法，这里配置的class表示检查自定义组件名
        "selector": "class",
        // format属性必选，配置期望的命名风格，支持枚举值，这里配置的PascalCase表示大驼峰风格
        "format": \["PascalCase"\],
        // custom属性可选，配置用户自定义的命名风格
        "custom": {
          // regex属性必选，配置具体的正则
          "regex": "^\[a-zA-Z\]+$",
          // match属性必选，配置为true表示正则未命中时报错；配置为false表示正则命中时报错
          "match": true
        }
      }
    \]
  },
}

**表1** 字段说明
| 
字段名称

 | 

参数说明

 | 

是否必选

 | 

类型

 | 

支持配置的参数

 |
| :-- | :-- | :-- | :-- | :-- |
| 

selector

 | 

配置要检查的语法

 | 

是

 | 

字符串、字符串数组

 | 

-   variable：变量
-   function：函数
-   parameter：参数
-   parameterProperty：参数属性
-   accessor：get/set方法
-   enumMember：枚举成员
-   classMethod：类方法
-   structMethod：自定义组件中的方法
-   objectLiteralMethod：对象方法
-   typeMethod：接口方法
-   classProperty：类属性
-   structProperty：自定义组件中的属性
-   objectLiteralProperty：对象属性
-   typeProperty：接口属性
-   class：类
-   struct：自定义组件
-   interface：接口
-   typeAlias：类型别名
-   enum：枚举
-   typeParameter：泛型参数
-   default：包含以上所有的类型
-   variableLike：包含variable，function，parameter
-   memberLike：包含classProperty，structProperty，objectLiteralProperty，typeProperty，parameterProperty ，enumMember，classMethod，objectLiteralMethod，typeMethod，accessor
-   typeLike：包含class，struct，interface，typeAlias，enum，typeParameter
-   method：包含classMethod，structMethod，objectLiteralMethod，typeMethod
-   property：包含classProperty，objectLiteralProperty，typeProperty

 |
| 

format

 | 

配置期望的命名风格

 | 

是

 | 

字符串数组

 | 

-   camelCase：小驼峰命名风格，比如getName，getID（支持连续大写字母），不支持下划线
-   strictCamelCase：严格小驼峰命名风格，除了不支持连续大写字母（getID），其他的和camelCase相同
-   PascalCase：大驼峰命名风格，比如Foo，CC，除了要求第一个字母大写，其他的和camelCase相同
-   StrictPascalCase：大驼峰命名风格，除了不支持连续大写字母（CC），其他的和PascalCase相同
-   snake\_case：小写字母+下划线+小写字母的命名风格，比如a\_a，不支持\_a，a\_a\_
-   UPPER\_CASE：大写字母+下划线+大写字母的命名风格，比如A\_A，不支持\_A，A\_A\_

 |
| 

custom

 | 

配置用户自定义的命名风格

 | 

否

 | 

对象

 | 

-   regex：属性必选，配置具体的正则
-   match：属性必选，配置为true表示正则未命中时报错，配置为false表示正则命中时报错

 |
| 

leadingUnderscore/trailingUnderscore

 | 

配置是否允许以下划线开头/以下划线结尾的命名风格

 | 

否

 | 

字符串

 | 

-   allow：允许以一个下划线开头/结尾的命名风格，比如\_name
-   allowDouble：允许以两个下划线开头/结尾的命名风格，比如\_\_name
-   allowSingleOrDouble：允许以一个或者两个下划线开头/结尾的命名风格（allow+allowDouble）
-   forbid：禁止以下划线开头/结尾的命名风格，比如\_name，\_\_name
-   require：必须是以下划线开头/结尾的命名风格，比如\_name，\_\_name
-   requireDouble：必须是以两个下划线开头/结尾的命名风格，比如\_\_name

 |
| 

prefix/suffix

 | 

配置固定前缀/后缀的命名风格。如果前缀/后缀未匹配则报错

 | 

否

 | 

字符串数组

 | 

用户自定义前缀/后缀

 |
| 

filter

 | 

过滤特定的命名风格，检查或者不检查正则命中的命名

 | 

否

 | 

对象

 | 

配置格式与custom相似

match：设置为true表示只检查正则命中的名字，设置为false表示不检查正则命中的名字

regex：设置过滤的正则

说明：

支持直接配置一个字符串，这个字符串配置的是regex，此时match相当于配置的是true。

 |
| 

modifiers

 | 

匹配修饰符，只有包含特定修饰符的命名才会检查

 | 

否

 | 

字符串数组

 | 

-   abstract：匹配abstract关键字
-   override：匹配override关键字
-   private：匹配private关键字
-   protected：匹配protected关键字
-   static：匹配static关键字
-   async：匹配async关键字
-   const：匹配const关键字
-   destructured：匹配解构语法
-   exported：匹配export关键字
-   global：匹配全局声明
-   #private：匹配私有符号#
-   public：匹配public级别的访问修饰符
-   requiresQuotes：匹配字符串类型的命名，并且 字符串中包含特殊字符
-   unused：匹配未使用的声明

 |
| 

types

 | 

匹配类型，只有特定类型的名字才会检查

 | 

否

 | 

字符串数组

 | 

-   array：数组类型
-   boolean：布尔类型
-   function：函数类型
-   number：数字类型
-   string：字符串类型

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/VpstsKaFSiq-hlp82E3KdQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=EAA00F61D144433B350746ACD13A25A18014B171C7CAF2AE575D45F899596DC3)

以上配置的参数有校验优先级：filter > types > modifiers > validate leading underscore > validate trailing underscore > validate prefix > validate suffix > validate custom > validate format。

**执行代码检查**

对pages/Index.ets文件执行代码检查，检查结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/XACweShHT2qwOv9p7UIRCA/zh-cn_image_0000002561833645.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=1FD4E6BFDADC0383A50229445AA4A974F5D5FB7B673DBAB1129F94B75AD16AAD)

#### \[h2\]示例3：检查代码文件的命名风格

**在配置文件中定义规则**

在ArkTS工程中，pages目录下新建test.ets文件；

在工程根目录下新建code-linter.json5文件，新增以下配置：

{
  "rules": {
    "@hw-stylistic/file-naming-convention": \[
      // 告警级别：枚举类型，支持配置为error，warn，off
      "error",
      {
        // selector属性可选，支持配置为code或者resources
        // code表示检查代码文件的命名风格
        // resources表示检查资源文件的命名风格
        "selector": "code"
      }
    \]
  },
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/1VuR5f_aT_m-vaWurkKHwA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=270AA272556135573B559921A2DCAA11CD125B01FA3B20E9D062667ADC2C8545)

如果selector属性不配置，默认检查代码文件和资源文件的命名风格。

**执行代码检查**

对pages/test.ets文件执行代码检查，检查结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/MLOhZKwBQnqxBbmxzN9BBg/zh-cn_image_0000002530913728.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=0344258E0DD7AE420A4219DAC3912E6625BA5C2BDC9632B0D8C0DA3AE4199207)
