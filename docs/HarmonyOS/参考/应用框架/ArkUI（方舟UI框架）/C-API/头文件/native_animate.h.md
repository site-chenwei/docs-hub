---
title: "native_animate.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "头文件"
  - "native_animate.h"
captured_at: "2026-04-17T01:48:07.522Z"
---

# native\_animate.h

#### 概述

提供ArkUI在Native侧的动画接口定义集合。native\_animate.h中的接口需要在主线程上调用。

**引用文件：** <arkui/native\_animate.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**相关示例：** [AnimationNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/AnimationNDK)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange) | ArkUI\_ExpectedFrameRateRange | 设置动画的期望帧率。 |
| [ArkUI\_AnimateCompleteCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-animatecompletecallback) | ArkUI\_AnimateCompleteCallback | 动画播放结束回调类型。 |
| [ArkUI\_NativeAnimateAPI\_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1) | ArkUI\_NativeAnimateAPI\_1 | ArkUI提供的Native侧动画接口集合。 |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption) | ArkUI\_AnimateOption | 设置动画效果相关参数。 |
| [ArkUI\_Curve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve) | ArkUI\_Curve | 提供曲线的插值对象定义。 |
| [ArkUI\_Curve\*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | ArkUI\_CurveHandle | 定义曲线的插值对象指针定义。 |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption) | ArkUI\_KeyframeAnimateOption | 定义关键帧动画参数对象。 |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption) | ArkUI\_AnimatorOption | 定义animator动画参数对象。 |
| [ArkUI\_Animator\*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h) | ArkUI\_AnimatorHandle | 定义animator动画对象指针。 |
| [ArkUI\_AnimatorEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatorevent) | ArkUI\_AnimatorEvent | 定义animator回调事件对象。 |
| [ArkUI\_AnimatorOnFrameEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoronframeevent) | ArkUI\_AnimatorOnFrameEvent | 定义animator接收到帧时回调对象。 |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect) | ArkUI\_TransitionEffect | 定义transition属性配置转场参数对象。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption\* OH\_ArkUI\_AnimateOption\_Create()](#oh_arkui_animateoption_create) | 创建动画效果参数。 |
| [void OH\_ArkUI\_AnimateOption\_Dispose(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_dispose) | 销毁动画效果参数指针。 |
| [uint32\_t OH\_ArkUI\_AnimateOption\_GetDuration(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getduration) | 获取动画持续时间，单位为ms（毫秒）。 |
| [float OH\_ArkUI\_AnimateOption\_GetTempo(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_gettempo) | 获取动画播放速度。 |
| [ArkUI\_AnimationCurve OH\_ArkUI\_AnimateOption\_GetCurve(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getcurve) | 获取动画曲线。 |
| [int32\_t OH\_ArkUI\_AnimateOption\_GetDelay(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getdelay) | 获取动画延迟播放时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimateOption\_GetIterations(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getiterations) | 获取动画播放次数。 |
| [ArkUI\_AnimationPlayMode OH\_ArkUI\_AnimateOption\_GetPlayMode(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getplaymode) | 获取动画播放模式。 |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimateOption\_GetExpectedFrameRateRange(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getexpectedframeraterange) | 获取动画的期望帧率。 |
| [void OH\_ArkUI\_AnimateOption\_SetDuration(ArkUI\_AnimateOption\* option, int32\_t value)](#oh_arkui_animateoption_setduration) | 设置动画持续时间，单位为ms（毫秒）。 |
| [void OH\_ArkUI\_AnimateOption\_SetTempo(ArkUI\_AnimateOption\* option, float value)](#oh_arkui_animateoption_settempo) | 设置动画播放速度。 |
| [void OH\_ArkUI\_AnimateOption\_SetCurve(ArkUI\_AnimateOption\* option, ArkUI\_AnimationCurve value)](#oh_arkui_animateoption_setcurve) | 设置动画曲线。 |
| [void OH\_ArkUI\_AnimateOption\_SetDelay(ArkUI\_AnimateOption\* option, int32\_t value)](#oh_arkui_animateoption_setdelay) | 设置动画延迟播放时间，单位为ms（毫秒）。 |
| [void OH\_ArkUI\_AnimateOption\_SetIterations(ArkUI\_AnimateOption\* option, int32\_t value)](#oh_arkui_animateoption_setiterations) | 设置动画播放次数。 |
| [void OH\_ArkUI\_AnimateOption\_SetPlayMode(ArkUI\_AnimateOption\* option, ArkUI\_AnimationPlayMode value)](#oh_arkui_animateoption_setplaymode) | 设置动画播放模式。 |
| [void OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange(ArkUI\_AnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* value)](#oh_arkui_animateoption_setexpectedframeraterange) | 设置动画的期望帧率。 |
| [void OH\_ArkUI\_AnimateOption\_SetICurve(ArkUI\_AnimateOption\* option, ArkUI\_CurveHandle value)](#oh_arkui_animateoption_seticurve) | 设置动画的动画曲线。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimateOption\_GetICurve(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_geticurve) | 获取动画的动画曲线。 |
| [ArkUI\_KeyframeAnimateOption\* OH\_ArkUI\_KeyframeAnimateOption\_Create(int32\_t size)](#oh_arkui_keyframeanimateoption_create) | 创建关键帧动画参数。 |
| [void OH\_ArkUI\_KeyframeAnimateOption\_Dispose(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_dispose) | 销毁关键帧动画参数。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDelay(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)](#oh_arkui_keyframeanimateoption_setdelay) | 设置关键帧动画的整体延时时间，单位为ms（毫秒），默认不延时播放。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetIterations(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)](#oh_arkui_keyframeanimateoption_setiterations) | 设置关键帧动画的动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*onFinish)()(void\* userData))](#oh_arkui_keyframeanimateoption_registeronfinishcallback) | 设置关键帧动画播放完成回调。当[关键帧动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)所有次数播放完成后调用。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* frameRate)](#oh_arkui_keyframeanimateoption_setexpectedframerate) | 设置关键帧动画期望帧率。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t value, int32\_t index)](#oh_arkui_keyframeanimateoption_setduration) | 设置关键帧动画某段关键帧动画的持续时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetCurve(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_CurveHandle value, int32\_t index)](#oh_arkui_keyframeanimateoption_setcurve) | 设置关键帧动画某段关键帧使用的动画曲线。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*event)(void\* userData), int32\_t index)](#oh_arkui_keyframeanimateoption_registeroneventcallback) | 设置关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDelay(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_getdelay) | 获取关键帧整体延时时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetIterations(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_getiterations) | 获取关键帧动画播放次数。 |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_getexpectedframerate) | 获取关键帧动画参数的期望帧率。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)](#oh_arkui_keyframeanimateoption_getduration) | 获取关键帧动画某段状态持续时间，单位为ms（毫秒）。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_KeyframeAnimateOption\_GetCurve(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)](#oh_arkui_keyframeanimateoption_getcurve) | 获取关键帧动画某段状态动画曲线。 |
| [ArkUI\_AnimatorOption\* OH\_ArkUI\_AnimatorOption\_Create(int32\_t keyframeSize)](#oh_arkui_animatoroption_create) | 创建animator动画对象参数。 |
| [void OH\_ArkUI\_AnimatorOption\_Dispose(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_dispose) | 销毁animator动画对象参数。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDuration(ArkUI\_AnimatorOption\* option, int32\_t value)](#oh_arkui_animatoroption_setduration) | 设置animator动画播放的时长，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDelay(ArkUI\_AnimatorOption\* option, int32\_t value)](#oh_arkui_animatoroption_setdelay) | 设置animator动画延时播放的时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetIterations(ArkUI\_AnimatorOption\* option, int32\_t value)](#oh_arkui_animatoroption_setiterations) | 设置animator动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetFill(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationFillMode value)](#oh_arkui_animatoroption_setfill) | 设置animator动画执行时组件在动画开始前和结束后的状态。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDirection(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationDirection value)](#oh_arkui_animatoroption_setdirection) | 设置animator动画播放方向。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value)](#oh_arkui_animatoroption_setcurve) | 设置animator动画插值曲线。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetBegin(ArkUI\_AnimatorOption\* option, float value)](#oh_arkui_animatoroption_setbegin) | 设置animator动画插值起点。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetEnd(ArkUI\_AnimatorOption\* option, float value)](#oh_arkui_animatoroption_setend) | 设置animator动画插值终点。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option, ArkUI\_ExpectedFrameRateRange\* value)](#oh_arkui_animatoroption_setexpectedframeraterange) | 设置animator动画期望的帧率范围。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframe(ArkUI\_AnimatorOption\* option, float time, float value, int32\_t index)](#oh_arkui_animatoroption_setkeyframe) | 设置animator动画关键帧参数。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value, int32\_t index)](#oh_arkui_animatoroption_setkeyframecurve) | 设置animator动画关键帧曲线类型。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetDuration(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getduration) | 获取animator动画播放的时长。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetDelay(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getdelay) | 获取animator动画延时播放时长。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetIterations(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getiterations) | 获取animator动画播放次数。 |
| [ArkUI\_AnimationFillMode OH\_ArkUI\_AnimatorOption\_GetFill(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getfill) | 获取animator动画执行时组件在动画开始前和结束后的状态。 |
| [ArkUI\_AnimationDirection OH\_ArkUI\_AnimatorOption\_GetDirection(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getdirection) | 获取animator动画播放方向。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetCurve(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getcurve) | 获取animator动画插值曲线。 |
| [float OH\_ArkUI\_AnimatorOption\_GetBegin(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getbegin) | 获取animator动画插值起点。 |
| [float OH\_ArkUI\_AnimatorOption\_GetEnd(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getend) | 获取animator动画插值终点。 |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getexpectedframeraterange) | 获取animator动画期望的帧率范围。 |
| [float OH\_ArkUI\_AnimatorOption\_GetKeyframeTime(ArkUI\_AnimatorOption\* option, int32\_t index)](#oh_arkui_animatoroption_getkeyframetime) | 获取animator动画关键帧时间，单位为ms（毫秒）。 |
| [float OH\_ArkUI\_AnimatorOption\_GetKeyframeValue(ArkUI\_AnimatorOption\* option, int32\_t index)](#oh_arkui_animatoroption_getkeyframevalue) | 获取animator动画关键帧数值。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve(ArkUI\_AnimatorOption\* option, int32\_t index)](#oh_arkui_animatoroption_getkeyframecurve) | 获取animator动画关键帧动画插值曲线。 |
| [void\* OH\_ArkUI\_AnimatorEvent\_GetUserData(ArkUI\_AnimatorEvent\* event)](#oh_arkui_animatorevent_getuserdata) | 获取动画事件对象中的用户自定义对象。 |
| [void\* OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData(ArkUI\_AnimatorOnFrameEvent\* event)](#oh_arkui_animatoronframeevent_getuserdata) | 获取动画的帧事件中的用户自定义对象。 |
| [float OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue(ArkUI\_AnimatorOnFrameEvent\* event)](#oh_arkui_animatoronframeevent_getvalue) | 获取动画帧回调事件对象中的插值结果。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorOnFrameEvent\* event))](#oh_arkui_animatoroption_registeronframecallback) | 设置animator动画接收到帧时回调。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](#oh_arkui_animatoroption_registeronfinishcallback) | 设置animator动画完成时回调。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](#oh_arkui_animatoroption_registeroncancelcallback) | 设置animator动画被取消时回调。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](#oh_arkui_animatoroption_registeronrepeatcallback) | 设置animator动画重复时回调。 |
| [int32\_t OH\_ArkUI\_Animator\_ResetAnimatorOption(ArkUI\_AnimatorHandle animatorHandle, ArkUI\_AnimatorOption\* option)](#oh_arkui_animator_resetanimatoroption) | 重置animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Play(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_play) | 启动animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Finish(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_finish) | 结束animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Pause(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_pause) | 暂停animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Cancel(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_cancel) | 取消animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Reverse(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_reverse) | 以相反的顺序播放animator动画。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCurveByType(ArkUI\_AnimationCurve curve)](#oh_arkui_curve_createcurvebytype) | 插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateStepsCurve(int32\_t count, bool end)](#oh_arkui_curve_createstepscurve) | 构造阶梯曲线对象。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)](#oh_arkui_curve_createcubicbeziercurve) | 构造三阶贝塞尔曲线对象。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)](#oh_arkui_curve_createspringcurve) | 构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受[animation](#oh_arkui_transitioneffect_setanimation)、[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#animateto)中的duration参数控制。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)](#oh_arkui_curve_createspringmotion) | 构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换掉前一个动画，并继承之前的速度。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)](#oh_arkui_curve_createresponsivespringmotion) | 构造弹性跟手动画曲线对象，是springMotion的一种特例，仅默认参数不同，可与springMotion混合使用。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)](#oh_arkui_curve_createinterpolatingspring) | 构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCustomCurve(void\* userData, float (\*interpolate)(float fraction, void\* userdata))](#oh_arkui_curve_createcustomcurve) | 构造自定义曲线对象。 |
| [void OH\_ArkUI\_Curve\_DisposeCurve(ArkUI\_CurveHandle curveHandle)](#oh_arkui_curve_disposecurve) | 销毁自定义曲线对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateOpacityTransitionEffect(float opacity)](#oh_arkui_createopacitytransitioneffect) | 创建组件转场时的透明度效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateTranslationTransitionEffect(ArkUI\_TranslationOptions\* translate)](#oh_arkui_createtranslationtransitioneffect) | 创建组件转场时的平移效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateScaleTransitionEffect(ArkUI\_ScaleOptions\* scale)](#oh_arkui_createscaletransitioneffect) | 创建组件转场时的缩放效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateRotationTransitionEffect(ArkUI\_RotationOptions\* rotate)](#oh_arkui_createrotationtransitioneffect) | 创建组件转场时的旋转效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateMovementTransitionEffect(ArkUI\_TransitionEdge edge)](#oh_arkui_createmovementtransitioneffect) | 创建组件平移效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateAsymmetricTransitionEffect(ArkUI\_TransitionEffect\* appear, ArkUI\_TransitionEffect\* disappear)](#oh_arkui_createasymmetrictransitioneffect) | 创建非对称的转场效果对象。 |
| [void OH\_ArkUI\_TransitionEffect\_Dispose(ArkUI\_TransitionEffect\* effect)](#oh_arkui_transitioneffect_dispose) | 销毁转场效果对象。 |
| [int32\_t OH\_ArkUI\_TransitionEffect\_Combine(ArkUI\_TransitionEffect\* firstEffect, ArkUI\_TransitionEffect\* secondEffect)](#oh_arkui_transitioneffect_combine) | 设置转场效果链式组合，以形成包含多种转场效果的TransitionEffect。 |
| [int32\_t OH\_ArkUI\_TransitionEffect\_SetAnimation(ArkUI\_TransitionEffect\* effect, ArkUI\_AnimateOption\* animation)](#oh_arkui_transitioneffect_setanimation) | 设置转场效果动画参数。 |

#### 函数说明

#### \[h2\]OH\_ArkUI\_AnimateOption\_Create()

```c
ArkUI_AnimateOption* OH_ArkUI_AnimateOption_Create()
```

**描述：**

创建动画效果参数。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* | 新的动画效果参数指针。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_Dispose()

```c
void OH_ArkUI_AnimateOption_Dispose(ArkUI_AnimateOption* option)
```

**描述：**

销毁动画效果参数指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetDuration()

```c
uint32_t OH_ArkUI_AnimateOption_GetDuration(ArkUI_AnimateOption* option)
```

**描述：**

获取动画持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，返回0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| uint32\_t | 动画持续时间，单位为ms（毫秒）。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetTempo()

```c
float OH_ArkUI_AnimateOption_GetTempo(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，返回0.0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| float | 动画播放速度。取值范围：\[0, +∞)。option异常时返回0.0。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetCurve()

```c
ArkUI_AnimationCurve OH_ArkUI_AnimateOption_GetCurve(ArkUI_AnimateOption* option)
```

**描述：**

获取动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，返回-1。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_AnimationCurve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve) | 动画曲线。option异常时返回-1。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetDelay()

```c
int32_t OH_ArkUI_AnimateOption_GetDelay(ArkUI_AnimateOption* option)
```

**描述：**

获取动画延迟播放时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，返回0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 动画延迟播放时间。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetIterations()

```c
int32_t OH_ArkUI_AnimateOption_GetIterations(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，返回0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 动画播放次数。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetPlayMode()

```c
ArkUI_AnimationPlayMode OH_ArkUI_AnimateOption_GetPlayMode(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，返回-1。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_AnimationPlayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationplaymode) | 动画播放模式。option异常时返回-1。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetExpectedFrameRateRange()

```c
ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimateOption_GetExpectedFrameRateRange(ArkUI_AnimateOption* option)
```

**描述：**

获取动画的期望帧率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，返回NULL。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange)\* | 动画的期望帧率，单位为帧/秒（fps）。option异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetDuration()

```c
void OH_ArkUI_AnimateOption_SetDuration(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |
| int32\_t value | 

动画持续时间，单位为ms（毫秒）。取值范围：\[0, +∞)。

value小于0时，按0处理。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetTempo()

```c
void OH_ArkUI_AnimateOption_SetTempo(ArkUI_AnimateOption* option, float value)
```

**描述：**

设置动画播放速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |
| float value | 

动画播放速度。取值范围：\[0, +∞)。

**说明：**

传入小于0的数值，会默认设置为1。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetCurve()

```c
void OH_ArkUI_AnimateOption_SetCurve(ArkUI_AnimateOption* option, ArkUI_AnimationCurve value)
```

**描述：**

设置动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |
| [ArkUI\_AnimationCurve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve) value | 

动画曲线。默认值：[ARKUI\_CURVE\_LINEAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve)，建议使用[ARKUI\_CURVE\_EASE\_IN\_OUT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve)获得更平滑的动画效果。

value值异常时，设置无效。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetDelay()

```c
void OH_ArkUI_AnimateOption_SetDelay(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画延迟播放时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |
| int32\_t value | 动画延迟播放时间，单位为ms（毫秒）。取值范围：(-∞, +∞)。默认值：0，表示不延迟。value大于0时表示延迟播放，小于0表示提前播放。value小于0时，如果value的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到value绝对值的时刻的状态；如果value的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetIterations()

```c
void OH_ArkUI_AnimateOption_SetIterations(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |
| int32\_t value | 

动画播放次数。取值范围：\[-1, +∞)，其中设置为0时不播放，-1表示无限次播放。默认值：1（播放一次）。

value小于-1时，操作无效。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetPlayMode()

```c
void OH_ArkUI_AnimateOption_SetPlayMode(ArkUI_AnimateOption* option, ArkUI_AnimationPlayMode value)
```

**描述：**

设置动画播放模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |
| [ArkUI\_AnimationPlayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationplaymode) value | 

动画播放模式。默认值：[ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationplaymode)。

value值异常时，操作无效。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange()

```c
void OH_ArkUI_AnimateOption_SetExpectedFrameRateRange(ArkUI_AnimateOption* option, ArkUI_ExpectedFrameRateRange* value)
```

**描述：**

设置动画的期望帧率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
动画效果参数。

option为NULL时，操作无效。

 |
| [ArkUI\_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange)\* value | 

动画的期望帧率，单位为帧/秒（fps）。

value为NULL时，操作无效。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetICurve()

```c
void OH_ArkUI_AnimateOption_SetICurve(ArkUI_AnimateOption* option, ArkUI_CurveHandle value)
```

**描述：**

设置动画的动画曲线。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/hv7OsJ9cTXSdIX7smTJ9xA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=24C42CED6EBEE7359206D7264BBB5D3B8B022E327E6FE83F7E21514A5455C499)

此方法优先于[OH\_ArkUI\_AnimateOption\_SetCurve](#oh_arkui_animateoption_setcurve)生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
animator动画参数。

option为NULL时，操作无效。

 |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) value | 

动画曲线参数。

value为NULL时，操作无效。

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetICurve()

```c
ArkUI_CurveHandle OH_ArkUI_AnimateOption_GetICurve(ArkUI_AnimateOption* option)
```

**描述：**

获取动画的动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* option | 
animator动画参数。

option为NULL时，返回NULL。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 动画的动画曲线。参数option异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_Create()

```c
ArkUI_KeyframeAnimateOption* OH_ArkUI_KeyframeAnimateOption_Create(int32_t size)
```

**描述：**

创建关键帧动画参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t size | 
关键帧动画状态数。

size小于0时返回NULL。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* | 关键帧动画参数对象。size小于0时返回NULL，option异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_Dispose()

```c
void OH_ArkUI_KeyframeAnimateOption_Dispose(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

销毁关键帧动画参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数对象。

option为NULL时，操作无效。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetDelay()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetDelay(ArkUI_KeyframeAnimateOption* option, int32_t value)
```

**描述：**

设置关键帧动画的整体延时时间，单位为ms（毫秒），默认不延时播放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| int32\_t value | 动画延迟播放时间，单位为ms（毫秒）。取值范围：(-∞, +∞)。默认值：0，表示不延迟。value大于0为延迟播放，value小于0表示提前播放。对于value小于0的情况：当value的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到value绝对值的时刻的状态；当value的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetIterations()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetIterations(ArkUI_KeyframeAnimateOption* option, int32_t value)
```

**描述：**

设置关键帧动画的动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| int32\_t value | 

动画播放次数。取值范围：\[-1, +∞)，其中设置为0时不播放，-1表示无限次播放。默认值：1，表示播放一次。

value小于-1时，操作无效，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnFinishCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*onFinish)(void* userData))
```

**描述：**

设置关键帧动画播放完成回调。当[关键帧动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)所有次数播放完成后调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| void\* userData | 

用户自定义对象指针。

不涉及异常值处理。

 |
| void (\*onFinish)(void\* userData) | 

回调方法。

userData：回调函数的入参，用户自定义对象指针。

onFinish为NULL时，操作无效。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option, ArkUI_ExpectedFrameRateRange* frameRate)
```

**描述：**

设置关键帧动画期望帧率。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| [ArkUI\_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange)\* frameRate | 

关键帧动画的期望帧率。

frameRate为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetDuration()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetDuration(ArkUI_KeyframeAnimateOption* option, int32_t value, int32_t index)
```

**描述：**

设置关键帧动画某段关键帧动画的持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| int32\_t value | 

关键帧动画的持续时间，单位为ms（毫秒），默认值1000ms。取值范围：\[0, +∞)。

value小于0时，按0处理。

 |
| int32\_t index | 

状态索引值。

index小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetCurve()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetCurve(ArkUI_KeyframeAnimateOption* option, ArkUI_CurveHandle value, int32_t index)
```

**描述：**

设置关键帧动画某段关键帧使用的动画曲线。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/SsqsgjGAQN6G0R572EPtWA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=83A44133C25D2F31995F946333CA9CF66AF06C0275E3EFD61BCA0DD6DF11A0AE)

由于[springMotion](#oh_arkui_curve_createspringmotion)、[responsiveSpringMotion](#oh_arkui_curve_createresponsivespringmotion)、[interpolatingSpring](#oh_arkui_curve_createinterpolatingspring)曲线时长不生效，故不支持这三种曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) value | 该关键帧使用的动画曲线。默认值：[ARKUI\_CURVE\_EASE\_IN\_OUT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve)。 |
| int32\_t index | 

状态索引值。取值范围：\[0, size-1\]，其中size为关键帧动画状态数。

index小于0或index超出范围时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnEventCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*event)(void* userData), int32_t index)
```

**描述：**

设置关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| void\* userData | 

用户定义对象指针。

不涉及异常值处理。

 |
| void (\*event)(void\* userData) | 

闭包函数。

event为NULL时，操作无效。

 |
| int32\_t index | 

状态索引值。取值范围：\[0, size-1\]，其中size为关键帧动画状态数。

index小于0或index超出范围时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetDelay()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_GetDelay(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧整体延时时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 整体延时时间，单位为ms（毫秒）。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetIterations()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_GetIterations(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 动画播放次数。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate()

```c
ArkUI_ExpectedFrameRateRange* OH_ArkUI_KeyframeAnimateOption_GetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧动画参数的期望帧率。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回NULL。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange)\* | 关键帧动画参数的期望帧率。option异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetDuration()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_GetDuration(ArkUI_KeyframeAnimateOption* option, int32_t index)
```

**描述：**

获取关键帧动画某段状态持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回0。

 |
| int32\_t index | 

状态索引值。

index小于0时，返回0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 持续时间，单位为ms（毫秒）。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetCurve()

```c
ArkUI_CurveHandle OH_ArkUI_KeyframeAnimateOption_GetCurve(ArkUI_KeyframeAnimateOption* option, int32_t index)
```

**描述：**

获取关键帧动画某段状态动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)\* option | 
关键帧动画参数。

option为NULL时，返回NULL。

 |
| int32\_t index | 

状态索引值。

index小于0时，返回NULL。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 动画曲线。参数异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_Create()

```c
ArkUI_AnimatorOption* OH_ArkUI_AnimatorOption_Create(int32_t keyframeSize)
```

**描述：**

创建animator动画对象参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/RvSWUKtsSqyWIXYgqW_mFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=7EE00B4FC93E3E220091D665266F342AD4061DC1EFD5A1BB743009E0B8EA2B72)

keyframeSize大于0时，动画插值起点默认是0，动画插值终点模式值是1。不支持设置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t keyframeSize | 
关键帧个数。

keyframeSize小于0时返回NULL。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* | animator动画对象参数指针。size小于0时返回NULL，option异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_Dispose()

```c
void OH_ArkUI_AnimatorOption_Dispose(ArkUI_AnimatorOption* option)
```

**描述：**

销毁animator动画对象参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，操作无效。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetDuration()

```c
int32_t OH_ArkUI_AnimatorOption_SetDuration(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画播放的时长，单位毫秒。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| int32\_t value | 

播放的时长，单位为ms（毫秒），默认值0ms。取值范围：\[0, +∞)。

value小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetDelay()

```c
int32_t OH_ArkUI_AnimatorOption_SetDelay(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画延时播放的时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| int32\_t value | 动画延迟播放时间，单位为ms（毫秒）。取值范围：(-∞, +∞)。默认值：0，表示不延迟。value大于0为延迟播放，value小于0表示提前播放。对于value小于0的情况：当value的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到value绝对值的时刻的状态；当value的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetIterations()

```c
int32_t OH_ArkUI_AnimatorOption_SetIterations(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/9IssCHijT8KFi7aDjm5cRA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=83EE9CF4C29E37BE56C807F60B51900FA1073D850C052B0D6EF115F14C84FE71)

设置为除-1外其他负数视为无效取值，无效取值动画默认播放1次。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| int32\_t value | 

取值范围：\[-1, +∞)，其中设置为0时不播放，-1表示无限次播放。默认值：1（播放一次）。

value小于-1时，操作无效。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetFill()

```c
int32_t OH_ArkUI_AnimatorOption_SetFill(ArkUI_AnimatorOption* option, ArkUI_AnimationFillMode value)
```

**描述：**

设置animator动画执行时组件在动画开始前和结束后的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| [ArkUI\_AnimationFillMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationfillmode) value | 

动画执行时组件在动画开始前和结束后的状态。默认值：[ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationfillmode)。

value小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetDirection()

```c
int32_t OH_ArkUI_AnimatorOption_SetDirection(ArkUI_AnimatorOption* option, ArkUI_AnimationDirection value)
```

**描述：**

设置animator动画播放方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| [ArkUI\_AnimationDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationdirection) value | 

动画播放方向。

value小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetCurve()

```c
int32_t OH_ArkUI_AnimatorOption_SetCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value)
```

**描述：**

设置animator动画插值曲线。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/u_FpAT8qT-WJLAEvunEzow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=E284FFDB8054A1223AACB62E275DA49409DBD60ACBD7AA79001B5D7099CE19DD)

不支持[springCurve](#oh_arkui_curve_createspringcurve)、[springMotion](#oh_arkui_curve_createspringmotion)、[responsiveSpringMotion](#oh_arkui_curve_createresponsivespringmotion)、[interpolatingSpring](#oh_arkui_curve_createinterpolatingspring)，[customCurve](#oh_arkui_curve_createcustomcurve)动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) value | 

动画插值曲线。默认值：[ARKUI\_CURVE\_LINEAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve)，建议使用[ARKUI\_CURVE\_EASE\_IN\_OUT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve)获得更平滑的动画效果。

value为NULL时，使用默认曲线[ARKUI\_CURVE\_LINEAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetBegin()

```c
int32_t OH_ArkUI_AnimatorOption_SetBegin(ArkUI_AnimatorOption* option, float value)
```

**描述：**

设置animator动画插值起点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/qgiDRQt5SbqhTlXAP-O7Eg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=C82DF34A86DE545B16A51BDDCDC49D945CEBD9E5A3D48CC6EC5763B717DBF000)

当Animator动画为[关键帧动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)时，此方法不生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| float value | 动画插值起点。取值范围：(-∞, +∞)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetEnd()

```c
int32_t OH_ArkUI_AnimatorOption_SetEnd(ArkUI_AnimatorOption* option, float value)
```

**描述：**

设置animator动画插值终点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/N5oJuzcZQyqePuYB2TyZgQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=9228E1963E2F190290C5C4322B7EAFA6540029AB0805A6D6A958BCC5B1200989)

当Animator动画为[关键帧动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption)时，此方法不生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| float value | 动画插值终点。取值范围：(-∞, +∞)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange()

```c
int32_t OH_ArkUI_AnimatorOption_SetExpectedFrameRateRange(ArkUI_AnimatorOption* option, ArkUI_ExpectedFrameRateRange* value)
```

**描述：**

设置animator动画期望的帧率范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| [ArkUI\_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange)\* value | 

期望的帧率范围对象。

value为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetKeyframe()

```c
int32_t OH_ArkUI_AnimatorOption_SetKeyframe(ArkUI_AnimatorOption* option, float time, float value, int32_t index)
```

**描述：**

设置animator动画关键帧参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| float time | 

关键帧时间。取值范围：\[0, 1\], 必须是递增。默认值：按索引均匀分布（如第1帧为0.0，第2帧为0.5，第3帧为1.0）。

time小于0或time大于1时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| float value | 关键帧数值。取值范围：(-∞, +∞)。 |
| int32\_t index | 

关键帧的索引值。

index小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve()

```c
int32_t OH_ArkUI_AnimatorOption_SetKeyframeCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value, int32_t index)
```

**描述：**

设置animator动画关键帧曲线类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/F1cHBz3iRouXUe5FPiDSeg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=AC20E292345406736450546F79ABF657351F50594ABE48F04CD6B232FBC35C1D)

不支持[springCurve](#oh_arkui_curve_createspringcurve)、[springMotion](#oh_arkui_curve_createspringmotion)、[responsiveSpringMotion](#oh_arkui_curve_createresponsivespringmotion)、[interpolatingSpring](#oh_arkui_curve_createinterpolatingspring)，[customCurve](#oh_arkui_curve_createcustomcurve)动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画对象参数。

option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) value | 动画插值曲线。默认值：NULL，表示线性插值。 |
| int32\_t index | 

关键帧的索引值。

index小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetDuration()

```c
int32_t OH_ArkUI_AnimatorOption_GetDuration(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放的时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | 
animator动画参数。

option为NULL时，返回0。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 动画播放的时长，单位毫秒。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetDelay()

```c
int32_t OH_ArkUI_AnimatorOption_GetDelay(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画延时播放时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 动画延时播放时长，单位毫秒。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetIterations()

```c
int32_t OH_ArkUI_AnimatorOption_GetIterations(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画动画参数。option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 动画播放次数。option异常时返回0。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetFill()

```c
ArkUI_AnimationFillMode OH_ArkUI_AnimatorOption_GetFill(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画执行时组件在动画开始前和结束后的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_AnimationFillMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationfillmode) | 动画执行时组件在动画开始前和结束后的状态。option异常时返回-1。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetDirection()

```c
ArkUI_AnimationDirection OH_ArkUI_AnimatorOption_GetDirection(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_AnimationDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationdirection) | 动画播放方向。option异常时返回-1。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetCurve()

```c
ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetCurve(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 动画插值曲线。option异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetBegin()

```c
float OH_ArkUI_AnimatorOption_GetBegin(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值起点。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| float | 动画插值起点。option异常时返回0.0。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetEnd()

```c
float OH_ArkUI_AnimatorOption_GetEnd(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值终点。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| float | 动画插值终点。option异常时返回0.0。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange()

```c
ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimatorOption_GetExpectedFrameRateRange(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画期望的帧率范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange)\* | 期望的帧率范围对象指针。函数参数异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetKeyframeTime()

```c
float OH_ArkUI_AnimatorOption_GetKeyframeTime(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画对象参数。 |
| int32\_t index | 关键帧的索引值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| float | 关键帧时间，单位为ms（毫秒）。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetKeyframeValue()

```c
float OH_ArkUI_AnimatorOption_GetKeyframeValue(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧数值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画对象参数。 |
| int32\_t index | 关键帧的索引值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| float | 关键帧数值。 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve()

```c
ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetKeyframeCurve(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧动画插值曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画对象参数。 |
| int32\_t index | 关键帧的索引值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 动画插值曲线。函数参数异常时返回NULL。 |

#### \[h2\]OH\_ArkUI\_AnimatorEvent\_GetUserData()

```c
void* OH_ArkUI_AnimatorEvent_GetUserData(ArkUI_AnimatorEvent* event)
```

**描述：**

获取动画事件对象中的用户自定义对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatorevent)\* event | 动画事件对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| void\* | 用户自定义对象。 |

#### \[h2\]OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData()

```c
void* OH_ArkUI_AnimatorOnFrameEvent_GetUserData(ArkUI_AnimatorOnFrameEvent* event)
```

**描述：**

获取动画的帧事件中的用户自定义对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOnFrameEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoronframeevent)\* event | 动画事件对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| void\* | 用户自定义对象。 |

#### \[h2\]OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue()

```c
float OH_ArkUI_AnimatorOnFrameEvent_GetValue(ArkUI_AnimatorOnFrameEvent* event)
```

**描述：**

获取动画帧回调事件对象中的插值结果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOnFrameEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoronframeevent)\* event | 动画事件对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| float | 
动画插值结果。

**说明：**

在动画过程中，插值结果根据动画参数在插值起点[OH\_ArkUI\_AnimatorOption\_SetBegin](#oh_arkui_animatoroption_setbegin)和插值终点[OH\_ArkUI\_AnimatorOption\_SetEnd](#oh_arkui_animatoroption_setend)间变化。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnFrameCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorOnFrameEvent* event))
```

**描述：**

设置animator动画接收到帧时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorOnFrameEvent\* event) | 
回调函数。

\- event：回调函数的入参，动画事件对象。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnFinishCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画完成时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 
回调函数。

\- event：回调函数的入参，动画事件对象。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnCancelCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画被取消时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 
回调函数。

\- event：回调函数的入参，动画事件对象。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnRepeatCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画重复时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 
回调函数。

\- event：回调函数的入参，动画事件对象。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_Animator\_ResetAnimatorOption()

```c
int32_t OH_ArkUI_Animator_ResetAnimatorOption(ArkUI_AnimatorHandle animatorHandle, ArkUI_AnimatorOption* option)
```

**描述：**

重置animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h) animatorHandle | animator动画对象。 |
| [ArkUI\_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_Animator\_Play()

```c
int32_t OH_ArkUI_Animator_Play(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

启动animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h) animatorHandle | animator动画对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_Animator\_Finish()

```c
int32_t OH_ArkUI_Animator_Finish(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

结束animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h) animatorHandle | animator动画对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_Animator\_Pause()

```c
int32_t OH_ArkUI_Animator_Pause(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

暂停animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h) animatorHandle | animator动画对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_Animator\_Cancel()

```c
int32_t OH_ArkUI_Animator_Cancel(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

取消animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h) animatorHandle | animator动画对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_Animator\_Reverse()

```c
int32_t OH_ArkUI_Animator_Reverse(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

以相反的顺序播放animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h) animatorHandle | animator动画对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateCurveByType()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCurveByType(ArkUI_AnimationCurve curve)
```

**描述：**

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_AnimationCurve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_animationcurve) curve | 曲线类型。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateStepsCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateStepsCurve(int32_t count, bool end)
```

**描述：**

构造阶梯曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t count | 
阶梯的数量，需要为正整数，取值范围：\[1, +∞)。

count值异常时，操作无效。

 |
| bool end | 在每个间隔的起点或是终点发生阶跃变化。true：在终点发生阶跃变化。false：在起点发生阶跃变化。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateCubicBezierCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)
```

**描述：**

构造三阶贝塞尔曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float x1 | 确定贝塞尔曲线第一点横坐标，取值范围：\[0, 1\]。设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| float y1 | 确定贝塞尔曲线第一点纵坐标。 |
| float x2 | 确定贝塞尔曲线第二点横坐标，取值范围：\[0, 1\]。设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| float y2 | 确定贝塞尔曲线第二点纵坐标。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateSpringCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)
```

**描述：**

构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受[animation](#oh_arkui_transitioneffect_setanimation)、[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#animateto)中的duration参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float velocity | 初始速度。是由外部因素对弹性动效产生的影响参数，其目的是保证对象从之前的运动状态平滑的过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。 |
| float mass | 
质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。取值范围：\[0, +∞)。

value小于等于0时，按1处理。

 |
| float stiffness | 

刚度。是物体抵抗施加的力而形变的程度。在弹性系统中，刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度就越快。取值范围：\[0, +∞)。

value小于等于0时，按1处理。

 |
| float damping | 

阻尼。用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。取值范围：\[0, +∞)。

value小于等于0时，按1处理。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateSpringMotion()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)
```

**描述：**

构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换掉前一个动画，并继承之前的速度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/OwQkey3VS7yk3KzgWq5EHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=CB758CA5FC249CBEE5EE54DA41FA0508601BC027AC60E9DE73F0CD9DDB33EDEA)

动画时间由曲线参数决定，不受[animation](#oh_arkui_transitioneffect_setanimation)、[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#animateto)中的duration参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float response | 
弹簧自然振动周期，决定弹簧复位的速度。取值范围：(0, +∞)。

参数小于等于0时，按0.55处理。

 |
| float dampingFraction | 

阻尼系数。大于0小于1的值为欠阻尼，运动过程中会超出目标值；等于1为临界阻尼；大于1为过阻尼，运动过程中逐渐趋于目标值。取值范围：(0, +∞)。

参数小于等于0时，按0.825处理。

 |
| float overlapDuration | 

弹性动画衔接时长。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。取值范围：\[0, +∞)。

参数小于0时，按0处理。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)
```

**描述：**

构造弹性跟手动画曲线对象，是springMotion的一种特例，仅默认参数不同，可与springMotion混合使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/uRoDbd19SgOO6q2WsGY0Fw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=19051AC97EBF172C0ADB3C3FDEE1373F30339CB11820111EBF31E0C86B9C2384)

动画时间由曲线参数决定，不受[animation](#oh_arkui_transitioneffect_setanimation)、[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#animateto)中的duration参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float response | 
弹簧自然振动周期，决定弹簧复位的速度。取值范围：(0, +∞)。

参数小于等于0时，按0.15处理。

 |
| float dampingFraction | 

阻尼系数。大于0小于1的值为欠阻尼，运动过程中会超出目标值；等于1为临界阻尼；大于1为过阻尼，运动过程中逐渐趋于目标值。取值范围：\[0, +∞)。

参数小于0时，按0.86处理。

 |
| float overlapDuration | 

弹性动画衔接时长。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。取值范围：\[0, +∞)。

参数小于0时，按0.25处理。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateInterpolatingSpring()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)
```

**描述：**

构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/oLdkb_upQD2giwLmYtOrhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=DAE549FAC3A7B840480BA7EB448DC58082CA4842C865D9770769EB0097BF5763)

动画时间由曲线参数决定，不受[animation](#oh_arkui_transitioneffect_setanimation)、[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#animateto)中的duration参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float velocity | 初始速度。外部因素对弹性动效产生的影响参数，目的是保证对象从之前的运动状态平滑地过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。 |
| float mass | 
质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。取值范围：\[0, +∞)。

value小于等于0时，按1处理。

 |
| float stiffness | 

刚度。表示物体抵抗施加的力而形变的程度。刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度越快。取值范围：\[0, +∞)。

value小于等于0时，按1处理。

 |
| float damping | 

阻尼。用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。取值范围：\[0, +∞)。

value小于等于0时，按1处理。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateCustomCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCustomCurve(void* userData, float (*interpolate)(float fraction, void* userdata))
```

**描述：**

构造自定义曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| void\* userData | 用户自定义数据。 |
| float (\*interpolate)(float fraction, void\* userdata) | 用户自定义的插值回调函数。fraction为动画开始时的插值输入x值。取值范围：\[0,1\]。返回值为曲线的y值。取值范围：\[0,1\]。fraction等于0时，返回值为0对应动画起点，返回不为0，动画在起点处有跳变效果。fraction等于1时，返回值为1对应动画终点，返回值不为1将导致动画的终值不是状态变量的值，出现大于或者小于状态变量值，再跳变到状态变量值的效果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) | 曲线的插值对象指针。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_Curve\_DisposeCurve()

```c
void OH_ArkUI_Curve_DisposeCurve(ArkUI_CurveHandle curveHandle)
```

**描述：**

销毁自定义曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_CurveHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h) curveHandle | 曲线的插值对象指针。 |

#### \[h2\]OH\_ArkUI\_CreateOpacityTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateOpacityTransitionEffect(float opacity)
```

**描述：**

创建组件转场时的透明度效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float opacity | 透明度，取值范围为\[0, 1\]。默认值为1。设置小于0的非法值按0处理，大于1的非法值按1处理，1表示不透明，0表示完全透明。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* | 组件转场时的透明度效果对象。 |

#### \[h2\]OH\_ArkUI\_CreateTranslationTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateTranslationTransitionEffect(ArkUI_TranslationOptions* translate)
```

**描述：**

创建组件转场时的平移效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TranslationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-translationoptions)\* translate | 组件转场时的平移参数对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* | 组件转场时的平移效果对象。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_CreateScaleTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateScaleTransitionEffect(ArkUI_ScaleOptions* scale)
```

**描述：**

创建组件转场时的缩放效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_ScaleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-scaleoptions)\* scale | 组件转场时的缩放参数对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* | 组件转场时的缩放效果对象。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_CreateRotationTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateRotationTransitionEffect(ArkUI_RotationOptions* rotate)
```

**描述：**

创建组件转场时的旋转效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_RotationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rotationoptions)\* rotate | 组件转场时的旋转参数对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* | 组件转场时的旋转效果对象。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_CreateMovementTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateMovementTransitionEffect(ArkUI_TransitionEdge edge)
```

**描述：**

创建组件平移效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TransitionEdge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_transitionedge) edge | 平移类型。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* | 组件转场时的平移效果对象。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_CreateAsymmetricTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateAsymmetricTransitionEffect(ArkUI_TransitionEffect* appear, ArkUI_TransitionEffect* disappear)
```

**描述：**

创建非对称的转场效果对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/APlIFs8_T76y7yiNT1osVg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=5F8DDB63CDE468783AA9E77F3BB9A37A88B0D4659E82FBE1888D3B416D7CC702)

如果不通过该函数构造[ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)，则表明该效果在组件出现和消失时均生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* appear | 出现的转场效果。 |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* disappear | 消失的转场效果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* | 非对称的转场效果对象。如果参数异常返回NULL。 |

#### \[h2\]OH\_ArkUI\_TransitionEffect\_Dispose()

```c
void OH_ArkUI_TransitionEffect_Dispose(ArkUI_TransitionEffect* effect)
```

**描述：**

销毁转场效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* effect | 转场效果对象。 |

#### \[h2\]OH\_ArkUI\_TransitionEffect\_Combine()

```c
int32_t OH_ArkUI_TransitionEffect_Combine(ArkUI_TransitionEffect* firstEffect, ArkUI_TransitionEffect* secondEffect)
```

**描述：**

设置转场效果链式组合，以形成包含多种转场效果的TransitionEffect。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* firstEffect | 转场效果。 |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* secondEffect | 需要链式转场效果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_TransitionEffect\_SetAnimation()

```c
int32_t OH_ArkUI_TransitionEffect_SetAnimation(ArkUI_TransitionEffect* effect, ArkUI_AnimateOption* animation)
```

**描述：**

设置转场效果动画参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/i8zhb0uGSGiyoD15g3fTNA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014807Z&HW-CC-Expire=86400&HW-CC-Sign=1544CBA4E8CFE4C4A45643C3289F556AD110FF55879B3FAE458961E9814539B7)

如果通过[OH\_ArkUI\_TransitionEffect\_Combine](#oh_arkui_transitioneffect_combine)进行转场效果的组合，前一转场效果的动画参数也可用于后一转场效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)\* effect | 转场效果。 |
| [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)\* animation | 属性显示动画效果相关参数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |
