---
title: "案例：ArkTS内存泄漏分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkts-memory-leak-analysis"
menu_path:
  - "指南"
  - "优化应用性能"
  - "内存泄露：Snapshot分析"
  - "案例：ArkTS内存泄漏分析"
captured_at: "2026-04-17T01:36:51.843Z"
---

# 案例：ArkTS内存泄漏分析

本案例介绍如何判断应用存在ArkTS泄漏，以及如何通过快照对比找出ArkTS内存泄漏的原因。

#### 初步识别内存问题

1.  使用[实时监控功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/realtime-monitor)对应用的内存资源进行监控。正常操作应用，观察运行过程中的应用内存变化情况。
    
    监控Memory用到变化。当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/NDTqGFJ5QOW8gVuskLhbXQ/zh-cn_image_0000002561833153.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D0E83C24EB4894C9ABF0A08B495A93F2D822556F9B78EBDFD8417FA59A5DBAB3 "点击放大")
    
2.  当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3.  以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/BHZ4_NVxTxi7eUb12WYVxQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=151027274EE41CC63775EE24B2D81A5121BE8D86D254D685BC3544F9631A073D)
    
    其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/sToV7e1kTiiPpuYVLuVrpw/zh-cn_image_0000002530913220.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=B6B7A672285596CBDA45ADA7331FE082A96236F272E5FB46CE7A07C29F53B0C0)
    
4.  点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/_jV99ATFRfCcnt8WS9QbZA/zh-cn_image_0000002561833127.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9A59D8BE56E08F701625FAD1584788E7ABAD1FFB7AD20C0AFDD104E18D58569B "点击放大")即开始录制。
5.  录制过程中，不断操作应用在问题场景的功能，将问题放大，便于快速定界问题点。
6.  点击下图中方块按钮或者左侧停止按钮结束录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/OWcXnzJoT563gKAAD1Xj6A/zh-cn_image_0000002561753143.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=5016C9F7BAB9117A5195B021B23E010A1F7CBC01CA2477C2989BD84EDC8626F3 "点击放大")
    
7.  录制完成后，展开Memory泳道，其中ArkTS Heap表示方舟虚拟机内存，这部分内存受到方舟虚拟机的管控。当ArkTS Heap有明显的上涨，说明在方舟虚拟机内的堆内存上可能存在内存泄漏，可以使用Snapshot模板进行下一步分析。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/MR_DQL-8QY2xTuTxEcukNw/zh-cn_image_0000002561753137.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=1BEAD8992018271D4BF8DD8D96C90623427109D7EF52EED52728758D1C26DD8F "点击放大")
    

#### 使用Snapshot模板分析ArkTS内存问题

分析内存泄漏问题步骤如下：

1.  使用Snapshot模板录制数据；
2.  在问题场景前拍摄快照；
3.  触发问题场景后，再次拍摄快照；
4.  对比两次快照的数据，可快速找到泄漏对象并做进一步分析；
5.  当有多个对象在比较视图都存在时，可以重复多次触发问题场景后拍摄快照，分别和问题场景前拍摄的快照进行对比，观察是否有对象出现明显的线性变化趋势，进一步缩小泄漏对象的范围。

#### \[h2\]录制模板数据

1.  连接设备后启动应用，点击应用选择框选择需要录制的应用，选择**Snapshot**模板，点击Create Session或双击Snapshot图标即可创建一个Snapshot的录制模板。
2.  创建模板后，点击三角按钮即开始录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/GPoomzTTSgqfOky7jGcMyA/zh-cn_image_0000002561833155.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=5050634E0A79D8FB25CFCB48813F4E05BDB12B40E0DC02AD1C05E76F10AD4265 "点击放大")
    
3.  待右侧泳道全部显示recording后则表明正在录制中。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/6ygS8XuASxOxPj_nVzsNWQ/zh-cn_image_0000002530913210.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D4F31B226349F88B62B8CE011E8EC3ACD712D5CDBBD6251DEA3518F346E62294 "点击放大")
    
4.  拍摄第一次堆快照作为基准（点击图中①处拍摄按钮，待②处显示出紫色条块表示快照拍摄完成）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/bZ9BSVuCQwyPSZhmR4XMBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=60EB59CB7C138BAFCB745FB51851600571070E0DB69C99C30CDAE4AD2A9EC633)
    
    方舟虚拟机提供了在获取快照前自动GC（Garbage Collection，对堆内存进行垃圾回收）的能力，因此拍摄快照之前不用主动触发GC。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/0mxp4MAWQiuA-Yg_mpMS6w/zh-cn_image_0000002561833121.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=068DE0BB932A4E2D7BD650C7C02B564D33FC4E6DA77DA9CF6C74522F6B5FEFEA "点击放大")
    
5.  多次触发内存泄漏操作。可以操作5，7，11等这种特殊的次数。比如操作了5次对比两个快照发现有很多创建了5次没释放的场景，则可能存在内存泄漏，再操作7次，如果创建了7次那就可以确认发生了泄漏。
6.  拍摄第二次堆快照。
7.  点击下图中方块按钮或者左侧停止按钮结束录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/r0eOS_N2TbKu1a1XfqpcZw/zh-cn_image_0000002530753210.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9E2CBC91A5292012B41E88ACA44FF3FB74D9D024908C3A7EF3D791F8921A577A "点击放大")
    

#### \[h2\]分析ArkTS Heap

1.  在每次拍摄堆快照之前，虚拟机都会触发GC，所以理论上堆快照内存在的对象都是当前虚拟机已经无法GC掉的对象。我们可以将两个堆快照进行比较，来查看哪些对象是在触发问题场景时新增了且不能释放的。切换到窗口下方详情区域的“Comparison”页签，将两次快照进行对比。图中数据的含义是以Snapshot2作为基准，Snapshot2对比Snapshot1的数据变化量。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/_6vUe3OMSJCnZAp8C55sww/zh-cn_image_0000002530753208.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A7160C97018FC242F51D17ECA940A5E67CB271025DD97D4FABA843BBDA799D48 "点击放大")
    
2.  优先寻找与触发内存泄漏操作次数强相关、与业务代码强相关的Constructor，首先来分析这些对象是否正常。主要是按照Distance逐渐减小的方式找引用链，可以从references里面一层层去寻找，排查引用链上的可疑对象（一般指与业务代码关联的对象）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/PI5gVHa4RmuKLi4BuaIKAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=AC2C09D86602BB2BF1EF11B67B12FD6D20A1E221DAE7D76A2665E6A40D58DC6A)
    
    选择一个实例结点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮，系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的结点），并在右侧区域展示。
    

#### 分析Snapshot数据

#### \[h2\]常见对象介绍

**JSArray**

目前所有JSArray展开后为数组里的各个元素：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/sJoK8LomSFaIK5IM87qdjw/zh-cn_image_0000002530753220.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=64786EA80E4F289F1F45E54DAD8577301CA687CB1EF027B303A2B64234EE7EBC)

其中\_\_proto\_\_：原型对象，所有数组的\_\_proto\_\_应该是一致的；length：内置属性访问器，可以访问数组长度。

**TaggedDict**

位于(array)标签中，一般为虚拟机内部创建的字典，ArkTS代码层面不可见。

**TaggedArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**COWArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**JSObject**

JSObject展开后为内部的各个属性如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Zh6eSQqRTnKxhmzrmjponA/zh-cn_image_0000002530913202.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=E762A6335086427C9539C054282F94C3F233EA3DE9C8D18A29BB7F8265B9E017)

以下通过具体代码来介绍下实例化对象、声明对象、构造函数间的关系：

// HelloWorldPage.ets
class People {
  old: number
  name: string
  constructor(old: number, name: string) {
    this.old \= old;
    this.name \= name;
  }
  printOld() {
    console.log("old = ", this.old);
  }
  printName() {
    console.log("name = ", this.name);
  }
}

@Entry
@Component
struct HelloWorldPage {
  @State message: string \= 'Hello World';
  private people: People \= new People(20, "Tom");

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

采集到的snapshot数据如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/U_LYftPYRtmCk3PGHGqQWA/zh-cn_image_0000002530753228.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D71387D9AE41F380BC6F402DEB7C26F7B86F0E0889B63285C6F7DE3856EA0BE5)

202169对象对应的是People，其主要声明了对象的属性和方法。

实例化对象的\_\_proto\_\_属性指向声明时的对象，声明对象里则会有constructor构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。

**JSFunction**

目前所有JSFunction都在(closure)标签中，展开即可看到所有JSFunction：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/amf_x4HBSvaTn9C0nx24Pg/zh-cn_image_0000002561833131.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=B958BF8E17981BEEF5BF7F6A8EA0AC84A52A5B3B0CC76C21BFE3CFA82BB0C787 "点击放大")

每个函数展开后为函数内的各个属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/iGj1Q_xHTYSZUMh93aVX2Q/zh-cn_image_0000002530753234.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=B7809A006A8BC903414261E38A6DBE43B535BE8E3308AF7BE8CD59812A6DFC00)

其中HomeObject表示父类对象，即该方法属于哪个对象；\_proto\_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。

如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/mnRRgE-gRguw57zOzUw_Cg/zh-cn_image_0000002530753230.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=4D1FA7CF9496DAE8263E60E66C8BEAA4A05B2ABD694A9C78E5CB45BF098FB895)

**ArkInternalConstantPool**

虚拟机创建的常量池，ArkTS代码层面不可见，涉及到的字符串常量会在(array)标签中展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/lrnBpIFGQxazBCvwDiKYkA/zh-cn_image_0000002530913204.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9974773FE03F207011D8A1C2F3DBF6EBFF837F064D70195E0AFF046827CF4089 "点击放大")

**LexicalEnv**

闭包变量上下文；闭包是一个链状结构，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/tpqb0RgFQR-P-ddnGbYP4A/zh-cn_image_0000002561833139.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=BB699F1C07E1DC9F32D83B97EBAD419353CC5094A936A0FAD9A010EBCD8D3080)

733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。

**InternalAccessor**

内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。

**LocalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于(handle)标签中，用于管理JS对象生命周期的引用句柄（napi\_value）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/qLZToh3jRAST2cvxfgPdrw/zh-cn_image_0000002531842516.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A4FCCCB3AD6F89B381903BF7D9AA3C5D741F08DB8BAFFEAAB7B6846AFCFA193A)

**GlobalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于(handle)标签中，允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref）。

#### \[h2\]常见属性介绍

| 
属性

 | 

含义

 |
| :-- | :-- |
| 

\_\_proto\_\_

 | 

原型对象

 |
| 

(object elements)

 | 

对象元素

 |
| 

(object properties)

 | 

对象属性

 |
| 

hclass

 | 

隐藏类

 |
| 

ArkInternalHash

 | 

ArkTS运行时内部的哈希值

 |
| 

ProtoOrHClass

 | 

原型或隐藏类指针

 |
| 

RawProfileTypeInfo

 | 

运行时类型剖析信息

 |
| 

HomeObject

 | 

父类对象

 |
| 

FunctionKind

 | 

函数类型标识

 |
| 

FunctionExtraInfo

 | 

函数附加信息

 |
| 

prototype

 | 

构造函数或类对象关联的原型对象

 |
| 

Inlineproperty

 | 

内联属性

 |

#### \[h2\]分析方法

**查看对象名称**

对于声明对象，可以通过constructor属性来确定对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/WGp_ZT0iQMS6KkEQsc-Mdw/zh-cn_image_0000002530913208.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D17A3450097851598FDEC599B5F88D72F9FC4BD9A49BF174E1CB4EC3BBD1B8A9)

对于实例化对象，一般没有constructor，则需要展开\_\_proto\_\_属性后查找constructor；

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/wLn0wyikQIWHxEE-ZCfzXg/zh-cn_image_0000002530913216.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=CA453E384CCF993255E93942EF4BDD0AA38E07F43405444AD04C31392BBB32C6)

若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。

如果对象间有继承关系，则可以继续展开\_\_proto\_\_：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/-_TBw5ZuTVeawwtrfu1SNA/zh-cn_image_0000002561833143.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=195C76C6BC4595EC1D6AB96D585AC411F0B944FBCFE93B0FF5348FBEA41CCB89)

如上图则表明Man对象继承自People对象。
