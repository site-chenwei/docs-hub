---
title: "基于URL跳转方式"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-launch-third-party-payment-url"
menu_path:
  - "指南"
  - "应用服务"
  - "Payment Kit（鸿蒙支付服务）"
  - "通用收银台接入"
  - "拉起三方支付收银台"
  - "基于URL跳转方式"
captured_at: "2026-04-17T01:36:19.736Z"
---

# 基于URL跳转方式

1.  商户客户端根据Payment Kit接口返回的支付信息[PayResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-paymentservice#payresult)(混合支付场景）/[PickerResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-paymentservice#pickerresult)（纯外部支付场景），按照三方支付平台接入要求创建订单获取拉起三方支付收银台链接并构建**订单支付跳转信息**[orderStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-model#orderstr)请求[requestPayment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-paymentservice#paymentservicerequestpayment)接口跳转或拉起三方支付收银台。
    
    跳转三方支付收银台示例代码如下：
    
    ```typescript
    import { BusinessError } from '@kit.BasicServicesKit';
    import { paymentService } from '@kit.PaymentKit';
    import { common } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct Index {
      context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      requestPaymentPromise() {
        // used orderStr to jump third-party payment, use your own orderStr.
        const orderStr = '{"nextAction":"L","linkUrl":"https://www.***.pay.com/h5pay?prepay_id=***&sign=***","scheme":"","clientToken":"***"}';
        paymentService.requestPayment(this.context, orderStr, "AP")
          .then((payResult: paymentService.PayResult) => {
            // succeeded in paying
            console.info('succeeded in paying, pay result: ', payResult);
          })
          .catch((error: BusinessError) => {
            // failed to pay
            console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
          });
      }
    
      build() {
        Column() {
          Button('requestPaymentPromise')
            .type(ButtonType.Capsule)
            .width('50%')
            .margin(20)
            .onClick(() => {
              this.requestPaymentPromise();
            })
          }
        .width('100%')
        .height('100%')
      }
    }
    ```
    
2.  开发者按照三方支付平台要求完成订单支付后的下一步业务处理，如对返回的支付结果信息验签等。
