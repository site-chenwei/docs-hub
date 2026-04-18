---
title: "组件启动规则（FA模型）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa"
menu_path:
  - "指南"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "FA模型开发指导"
  - "FA模型应用组件"
  - "组件启动规则（FA模型）"
captured_at: "2026-04-17T01:35:32.833Z"
---

# 组件启动规则（FA模型）

启动组件是指一切启动或连接应用组件的行为：

-   启动PageAbility、ServiceAbility，如使用startAbility()等相关接口。
    
-   连接ServiceAbility、DataAbility，如使用connectAbility()、acquireDataAbilityHelper()等相关接口。
    

为了保证用户具有更好的使用体验，对以下几种易影响用户体验与系统安全的行为做了限制：

-   后台应用任意弹框，如各种广告弹窗，影响用户使用。
    
-   后台应用相互唤醒，不合理的占用系统资源，导致系统功耗增加或系统卡顿。
    
-   前台应用任意跳转至其他应用，如随意跳转到其他应用的支付页面，存在安全风险。
    

鉴于此，系统制定了一套组件启动规则，主要包括：

-   **跨应用启动组件，需校验目标组件Visible**
    
    -   只针对跨应用场景。
    -   若目标组件visible字段配置为false，则需校验ohos.permission.START\_INVISIBLE\_ABILITY权限（该权限仅系统应用可申请）。
    -   组件visible配置参考[abilities对象的内部结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-structure#abilities对象的内部结构)的visible属性。
-   **位于后台的应用，启动组件需校验BACKGROUND权限**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/2buoYm0uS_q7TG67Z9C09g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013533Z&HW-CC-Expire=86400&HW-CC-Sign=EAF2811F1D306CBEFFD997CD5C097E3E052D77B569F75C6AB0C4EC165FB46715)
    
    基于API 8或更早版本SDK开发的应用在启动ServiceAbility组件或DataAbility组件时不受此限制的约束。
    
    -   应用前后台判断标准：若应用进程获焦或所属的UIAbility位于前台则判定为前台应用，否则为后台应用。
    -   需校验ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND权限（该权限仅系统应用可申请）。
-   **跨应用启动[FA模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#fa模型)的ServiceAbility组件或DataAbility组件，对端应用需配置关联启动**
    
    -   只针对跨应用场景。
    -   只针对目标组件为ServiceAbility与DataAbility生效。
    -   目标应用的AssociateWakeUp为**true**，其提供的ServiceAbility与DataAbility才允许被其他应用访问。
    -   只有系统预置应用才允许配置AssociateWakeUp字段，其余应用AssociateWakeUp默认为**false**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/B3oRGWI1QwGcaAV8i0vdTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013533Z&HW-CC-Expire=86400&HW-CC-Sign=19DE5359AB7BD94DA3E308DF678205E5FCD0F32E0B4E50FA9936E76158893B07)

1.  组件启动管控自v3.2 Release版本开始落地。
    
2.  与原本的启动规则不同，新的组件启动规则较为严格，开发者需熟知启动规则，避免业务功能异常。
    

启动组件的具体校验流程见下文。

#### 同设备组件启动规则

设备内启动组件，不同场景下的规则不同，可分为如下两种场景：

-   启动PageAbility。
    
-   启动ServiceAbility或DataAbility。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/08h4vttJTmGcTMLH3cbZcw/zh-cn_image_0000002538178356.png?HW-CC-KV=V1&HW-CC-Date=20260417T013533Z&HW-CC-Expire=86400&HW-CC-Sign=4E62233796153006488248DB404065C4FF154FEA89EDFBE039D92D649597BA3C)

#### 分布式跨设备组件启动规则

跨设备启动组件，不同场景下的规则不同，可分为如下两种场景：

-   启动PageAbility。
    
-   启动ServiceAbility。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/1jVm8pd8Sx6mMUUABR_S-w/zh-cn_image_0000002569018143.png?HW-CC-KV=V1&HW-CC-Date=20260417T013533Z&HW-CC-Expire=86400&HW-CC-Sign=2142AAA4918B05C9F5F0CF83F6AFC5864C4DD64D518F8B715D38D32C9A991124)
