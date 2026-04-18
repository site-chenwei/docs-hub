---
title: "构建HAR"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har"
menu_path:
  - "指南"
  - "构建应用"
  - "配置构建流程"
  - "构建HAR"
captured_at: "2026-04-17T01:36:50.823Z"
---

# 构建HAR

构建模式：DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。

产物格式：构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。

从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，默认构建字节码HAR，用于提升发布产物的安全性。

#### 使用约束

HAR自身的构建不建议引用本地模块，可能导致其他模块依赖该HAR包时安装失败，如果安装失败，需要在工程级oh-package.json5中配置[overrides](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-oh-package-json5#zh-cn_topic_0000001792256137_overrides)。

#### 创建模块

1.  新建工程时选择API 10及以上的Stage模型，工程创建完成后，新建“Static Library”模块。模块创建方法可参考[在工程中添加Module](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-module)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/iSbFx48IQsO-zuGlt2lNJg/zh-cn_image_0000002561753161.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=3BC9183F664F5E0FC236A05E461D17FCD6D6937B30719D79BEBDFD93F84D1838)
    
2.  编写代码。
    
      library  // HAR根目录
      ├─libs  // 存放用户自定义引用的Native库，一般为.so文件
      └─src
      │   └─main
      │     ├─cpp
      │     │  ├─types  // 定义Native API对外暴露的接口  
      │     │  │  └─liblibrary  
      │     │  │      ├─index.d.ts
      │     │  │      └─oh-package.json5 
      │     │  ├─CMakeLists.txt  // CMake配置文件  
      │     │  └─napi\_init.cpp  // C++源码文件
      │     └─ets  // ArkTS源码目录
      │     │  └─components
      │     │     └─MainPage.ets
      │     ├─resources  // 资源目录，用于存放资源文件，如图片、多媒体、字符串等  
      │     └─module.json5  // 模块配置文件，包含当前HAR的配置信息  
      ├─build-profile.json5  // Hvigor编译构建所需的配置文件，包含编译选项
      ├─hvigorfile.ts  // Hvigor构建脚本文件，包含构建当前模块的插件、自定义任务等
      ├─Index.ets  // HAR的入口文件，一般作为出口定义HAR对外提供的函数、组件等   
      **└─oh-package.json5**  // HAR的描述文件，定义HAR的基本信息、依赖项等
    
3.  在oh-package.json5中“main”字段定义导出文件入口。若不设置“main”字段，默认以当前目录下Index.ets为入口文件，依据.ets>.ts>.js的顺序依次检索。以将ets/components/MainPage.ets文件设置为入口文件为例：
    
    {
      ...
      "main": "./src/main/ets/components/MainPage.ets",
      ...
    }
    

#### 字节码HAR

默认产物是包含字节码的HAR包，其中包含abc字节码、资源文件、配置文件、readme、changelog声明文件、license证书文件，提升发布到ohpm中心仓产物的安全性。

字节码HAR包中包含的是编译后的abc字节码，当字节码HAR被其他应用模块(HAP/HSP)依赖时，执行应用模块的编译构建，不需要再对依赖的HAR进行语法检查和编译等操作，相比源码HAR，可以有效提升应用模块的编译构建效率，提高安全性，降低代码泄漏的风险。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/9syWQKg9Sqq_MzmTSkQMSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=B5DCC36292C71C7C2302D16DFC2304D4449E2BB7498F843F652C1918A808711B)

由于构建字节码HAR需要生成二进制的格式，所以单独构建字节码HAR会比构建非字节码HAR耗时更多。

#### \[h2\]收益

-   字节码HAR可以降低代码泄漏的风险，增加反编译获取代码逻辑的难度。

-   采用ArkTS/TS语言开发的字节码HAR，被HAP/HSP集成时，可以减少语法检查、转换的耗时，提高构建性能。
-   字节码HAR可以减少编译时node的进程占用，有效降低内存占用。
-   通过其他代码生成工具生成的js语言HAR包，编译构建成字节码HAR后，被HAP/HSP集成时，可以减少编译阶段处理的文件和代码数量，降低内存，提高构建性能。

#### \[h2\]使用场景

从功能上来说所有的源码HAR包都可以按照任意顺序切换成字节码HAR。但是由于字节码HAR编译和集成的特点，按照推荐场景或顺序来逐步切换字节码HAR可能会获得比较好的性能、内存收益。以下场景中推荐切换使用字节码HAR：

-   适用于SDK厂商对外提供SDK，以及高安全的场景，字节码HAR可以降低源码泄漏的风险。
-   采用muti-repo的开发模式，在被主工程合并集成时，所有依赖的HAR均可以发布成字节码HAR，从而提高主HAP的构建效率。
-   采用mono-repo的开发模式，工程中含有单个代码文件较大，或通过代码生成工具生成的代码量较大的ArkTS/TS/JS 的二方、三方SDK(HAR包)时，可考虑将这些HAR包构建成字节码HAR。
-   对内存要求较高的场景，可以通过切换字节码HAR，降低内存的占用。
-   通过ArkTS/TS/JS编写的HAR，且在依赖链条中处于较为底层的叶子节点，含有较少的源码依赖时，切换为字节码HAR会有较好的收益。

#### \[h2\]约束条件

-   字节码HAR使用的依赖需要配置在本模块的oh-package.json5的dependencies或dynamicDependencies中，如果不配置，后续字节码HAR被集成时可能会出现运行时异常。如果出现异常，部分场景可通过在hvigor-config.json5中配置ohos.byteCodeHar.integratedOptimization后重新编译，具体请参考[编译行为差异说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-dependencies#section957371853712)。
-   字节码HAR的oh-package.json5中配置的依赖名和依赖包的包名（即包内oh-package.json5中的name）需要保持一致。
-   依赖字节码HAR包时，该工程的build-profile.json5中的[useNormalizedOHMUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app#section13181758123312)必须设置为true。
-   HAP/HSP/HAR依赖字节码HAR包时，HAP/HSP/HAR的oh-package.json5中配置的依赖名和字节码HAR包的oh-package.json5中的name需要保持一致。
-   HAP/HSP/HAR代码中import使用字节码HAR包时，\`import xxx from 'yyy'\`的依赖名yyy要和本模块oh-package.json5中配置的依赖名保持一致（包括大小写）。
-   依赖字节码HAR包时，字节码HAR的compatibleSdkVersion不能大于工程的compatibleSdkVersion。

#### \[h2\]操作步骤

1.  将工程级build-profile.json5的useNormalizedOHMUrl设置为true。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/Iqd-jzSzQ0qHW1QQRndixg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=04873CDBC8385A2474D8AC61F34938A128890BC4B34928C65970889FF7CC5685)
    
    从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，工程级build-profile.json5中useNormalizedOHMUrl字段默认为true，byteCodeHar缺省默认值为true，无需执行步骤1和2。
    
    {
      "app": {
        "products": \[
          {
             "buildOption": {
               "strictMode": {
                 "useNormalizedOHMUrl": true
               }
             }
          }
        \]
      }
    }
    
2.  在HAR模块的build-profile.json5中，将byteCodeHar设置为true。
    
    {
      "buildOption": {
        "arkOptions": {
          "byteCodeHar": true
        }
      }
    }
    
3.  点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Q4l6-bh9TcSZ0MIQuGsTlQ/zh-cn_image_0000002561833159.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=6D97952CF028A82D24EFEEB480AA4D318A6326E6D1B237EA5E4DCB828762DE01)，选择**Build Mode，**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/KMnwkmvqT0CjfWXGOh6O_Q/zh-cn_image_0000002530753236.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=0A018C7605F230ADE9EC4C460451183EDEFBB87C6A78E97AFED540E1B368532A)
    
4.  （可选）在编译模式为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[代码混淆](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-obfuscation)。
    
    {
      "apiType": "stageMode",
      "buildOption": {
      },
      "buildOptionSet": \[
        {
          "name": "release",
          "arkOptions": {
            // 混淆相关参数
            "obfuscation": {
              "ruleOptions": {
                // true表示进行混淆，false表示不进行混淆。5.0.3.600及以上版本默认为false
                "enable": true,
                // 混淆规则文件
                "files": \[
                  "./obfuscation-rules.txt"
                \]
              },
              // consumerFiles中指定的混淆配置文件会在构建依赖这个library的工程或library时被应用
              "consumerFiles": \[
                "./consumer-rules.txt"
              \]
            }
          },
        },
      \],
      "targets": \[
        {
          "name": "default"
        }
      \]
    }
    
5.  （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。
    
    "buildOption": {
      "packingOptions": {
        "asset": {
          "include": \["./src/router.json5","router.json5"\],    // 配置打包到HAR产物中的文件
          "exclude": \["./config/\*"\]     // 配置不打包到HAR产物中的文件
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Rg0z7Kj6ScueRDeWuID63A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=9DDD732133D35AF9D577FC6C5FFD36689ABDFB79C45A13CB60CDA0FBB23E755C)
    
    -   配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
    -   配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
    
6.  选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/1FoPulqGRcClm7dss1fTtw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=FCB3723DD8CCB42977D8B1259D24FCA30CFCF56976C9C4C0A7BE4717ECD6E3A8)
    
    若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/TxG3wLBfRcS_0NtSDSXopA/zh-cn_image_0000002561833149.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=79178AB72A7539D774F503850040A8F860D84394C664D8F08DE29E98B653587E)
    
    构建完成后，build目录下生成HAR包产物。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/oMz1FgxnQ4W7Nyb48HjbNw/zh-cn_image_0000002561753149.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=2233E0491C4BCCD0942D8A033E87D3CF906E70C0C862753D498B3F55AAF22B3B)
    
    HAR包产物解压后，结构如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/zbFv99JDTHygUbpC1MD88A/zh-cn_image_0000002561833135.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=07EC023402760E62AACE4A62E3FF48472D6AA81CEB151EA74E09020067F951CE)
    

#### 源码HAR

#### \[h2\]以debug模式构建

产物是包含源码的HAR包，其中包含源码、资源文件以及配置文件等，方便开发者进行本地调测，不包含build、node\_modules、oh\_modules、.cxx、.preview、.hvigor、.gitignore、.ohpmignore、.gitignore/.ohpmignore中配置的文件、cpp工程的CMakeLists.txt。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/s4a0oPE7TJmlhlfZo-04sg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=9E39ECDFBC6A6B42F4AFFFF6F5F321FFCDE9923D40A601F705FAD0550BE78499)

-   源码HAR包中包含源代码，请谨慎分发，避免造成源代码泄露。
-   如果是native工程，以debug模式构建的native产物中不包含调试信息和符号表，如需调试，请参考[三方源码调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-source-code-debugging)。
-   从5.0.3.403版本开始，不再建议使用相对路径跨模块引用代码文件，若历史工程存在此场景的跨模块引用，会出现warning告警，请尝试将该文件移至本模块内，再重新进行编译。
-   从5.0.3.403版本开始，以debug/release模式构建HAR的流程使用相同的语法校验规则，若历史工程出现ArkTS语法报错，请按照报错信息修改代码，以符合ArkTS语言规范。

1.  在HAR模块的build-profile.json5中，将byteCodeHar设置为false。
    
    {
      "buildOption": {
        "arkOptions": {
          "byteCodeHar": false
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/yrfn9DChT_Sy5xH5NuO8ng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=681C2C2AFB15872258BF7FA7DAA712A5D0D3E797383F7A2DFF8791F6698A1E9B)
    
    使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，模块级build-profile.json5的byteCodeHar字段的缺省默认值为false，无需执行本步骤。
    
2.  点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/xbyjxy1_QkWEDjmKDtmdww/zh-cn_image_0000002530753214.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=893E19582D78D50286B64083DAA5B30A0EE0176953F6F44E809A7E78B61567ED)，**Build Mode**选择**debug。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/I4Xzq9AyTdOAymYLqdPrkg/zh-cn_image_0000002561753157.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=9BED37783FB206B34B8785088543EC259694192BDA7276BE8D88BB587C977599)
    
3.  （可选）若部分工程源文件无需构建到HAR包中，可在模块目录下新建.ohpmignore文件，或者在模块目录下的.gitignore文件中，配置打包时要忽略的文件，.ohpmignore文件中支持正则表达式写法，.gitignore文件中支持glob语法。DevEco Studio构建时将过滤掉.ohpmignore或.gitignore文件中所包含的文件/文件夹。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/gbYQz-pUQuSRQVgLR5gCFg/zh-cn_image_0000002530753222.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=8C4BB44DB39EFB064C789D830E0E94563C5F79C8627EB9E2E7BE5239CF20299F)
    
4.  （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。配置include或exclude字段后，.gitignore和.ohpmignore文件将不再生效。
    
    "buildOption": {
      "packingOptions": {
        "asset": {
          "include": \["./src/router.json5","router.json5"\],    // 配置打包到HAR产物中的文件
          "exclude": \["./config/\*"\]     // 配置不打包到HAR产物中的文件
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/aXwT4zesT0uos_Qu4jY7ww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=3AB8E4CB4039A6CFF052EF1604BB13C12D69F0AAF9D2840211488E73DEE0632A)
    
    -   配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
    -   配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
    
5.  选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/jVnvcuCtSRGT7rJHDQhQ2w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=DDA152D21D0F34EF0007FE7084D7376D347160E06AA79A38E1052CE29A14C934)
    
    若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/3d91SrrYTj2oWa77oeZSfg/zh-cn_image_0000002561833137.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=DB6997B4276D01DD1AE655F08EFB9761878EAD3CD499EFD0BBD0EECA87B41646)
    
    构建完成后，build目录下生成HAR包产物。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/ATkjQW8OQ3yFEgicrNfgZg/zh-cn_image_0000002530753238.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=73525036D6131D1702B7605F895C74AD83061AE546B6347EE5C263BD551B7C34)
    
    HAR包产物解压后，结构如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/jxZ330R6SM6pdPATxvutLw/zh-cn_image_0000002561833145.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=21EB29C8C2C818FBA28BA52535C4F90968FF994B01025471E7FDA4895DC3E068)
    

#### \[h2\]以release模式构建

从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认不开启混淆，构建产物和debug模式相同，请参考[以debug模式构建](#section197792874110)。

为保护代码资产，建议开启混淆，开启后，构建产物是包含js中间码的HAR包，其中包含源码混淆后生成的js中间码文件、资源文件、配置文件、readme、changelog声明文件、license证书文件，用于发布到ohpm中心仓。

1.  在HAR模块的build-profile.json5中，将byteCodeHar设置为false。
    
    {
      "buildOption": {
        "arkOptions": {
          "byteCodeHar": false
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/_iF1lP9cQT2A9xZYfXl_Dg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=FADE01C197CDA865286835F86892EAB8D589E72B4B51ACFD5D21D3AF7A005142)
    
    使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，模块级build-profile.json5的byteCodeHar字段的缺省默认值为false，无需执行本步骤。
    
2.  点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/fc9SSVttQmON-rYhhjJqkA/zh-cn_image_0000002561753187.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=8610036AEC2D3C7169435A9982060D6AB63A65BE74FE8AC073EDC2063278E1AF)，**Build Mode**中选择**release。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/tQraej-tQQaRpqHqXhPquQ/zh-cn_image_0000002530913234.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=22BC7B9CF0E45E75DD7970CD6C11177DF3DA2BCCF288B8E5B07BC31B315020FB)
    
3.  在[编译模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-guide#section192461528194916)为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[代码混淆](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-obfuscation)。
    
    {
      "apiType": "stageMode",
      "buildOption": {
      },
      "buildOptionSet": \[
        {
          "name": "release",
          "arkOptions": {
            // 混淆相关参数
            "obfuscation": {
              "ruleOptions": {
                // true表示进行混淆，false表示不进行混淆。5.0.3.600及以上版本默认为false
                "enable": true,
                // 混淆规则文件
                "files": \[
                  "./obfuscation-rules.txt"
                \]
              },
              // consumerFiles中指定的混淆配置文件会在构建依赖这个library的工程或library时被应用
              "consumerFiles": \[
                "./consumer-rules.txt"
              \]
            }
          },
        },
      \],
      "targets": \[
        {
          "name": "default"
        }
      \]
    }
    
4.  （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。
    
    "buildOption": {
      "packingOptions": {
        "asset": {
          "include": \["./src/router.json5","router.json5"\],    // 配置打包到HAR产物中的文件
          "exclude": \["./config/\*"\]     // 配置不打包到HAR产物中的文件
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/UJrjepu2Rg2_IpZqZhsCsA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=01E8B93C1570E5B402EA008708716373A97F341CC1347EBAD6E441998810FE1C)
    
    -   配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
    -   配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
    
5.  选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/foyp_KDxTOyZpfJW6kOs1Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=2FA2F1E06F52C29943EB510190C9C6DBD1024819F2538B4544B936DCB826EBD5)
    
    若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ktn7fsezS2GUhfRIC7BFiw/zh-cn_image_0000002561833151.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=499BE4FE2A4893BDB295B4B4BB77731C7F8BB24E29A2929FDE38946D52523D05)
    
    构建完成后，build目录下生成HAR包产物。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/jw4FsNYnTXWv4_fktLRvXA/zh-cn_image_0000002530753226.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=FD6AA7AC2372C6B63A602C127E8988FDC0D40BB6D0A88B8CB38EF33DA72A96C7)
    
    HAR包产物解压后，结构如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/hmhR6DpnTXizzm68UUdK1g/zh-cn_image_0000002530753244.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=C94A3EF8EFBF370F484D57DB0C05EA5223F19184BF35EAD27EADF69B376A7B57)
    

#### 对HAR进行签名

DevEco Studio在构建HAR流程的基础上，支持对HAR进行签名。签名后的HAR包后续可用于接入生态市场，接入流程请参考[SDK类商品接入说明](https://developer.huawei.com/consumer/cn/doc/start/dev-mall-marketplace-sp-sdkservice-access-explain-0000001866499490)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/0Ogr5zRAShmPHNsy6jm8LQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=54FBAF69B2FD767736344AB37082192EA53A24D9DA76DF1512FEEE2FA9F8CAAA)

1\. 该能力只在Compatible SDK 5.0.0(12)及以上版本的SDK中支持。

2\. 该能力需开启Hvigor的Daemon能力，请确保当前工程开启了Daemon，打开**File > Settings**（macOS为**DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor**，勾选字段**Enable the Daemon for tasks**。

1.  在hvigor-config.json5中，开启构建签名HAR开关：
    
    {
      "properties": {
        "ohos.sign.har": true
      }
    }
    
2.  配置工程签名信息，配置流程请参考[配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app#section793484619307)。
3.  选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/VX9iqOFDRC-ueMPZT1zEbA/zh-cn_image_0000002530913240.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=C59D2B3B035E0D34F8A0F8510099023DA7EDCDAB72D84CECB7135ADADC0498F7)
    
    构建完成后，build目录下生成签名HAR包产物。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/VgpUO-XuT9qKDsha3O6YDw/zh-cn_image_0000002530913244.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=1519EC8FEC3DB9BC0FD719BA71205FBFD7FF4E93C6C8585209F3ED26F65A45EB)
