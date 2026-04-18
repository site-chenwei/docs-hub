---
title: "三方库@ohos/axios中发起post请求，如何以queryParams形式传递参数"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-35"
menu_path:
  - "FAQ"
  - "系统开发"
  - "网络"
  - "网络（Network）"
  - "三方库@ohos/axios中发起post请求，如何以queryParams形式传递参数"
captured_at: "2026-04-17T02:03:17.234Z"
---

# 三方库@ohos/axios中发起post请求，如何以queryParams形式传递参数

-   方式一：使用axios.post接口时，Url.URLParams需要转换为字符串并拼接到URL后面。
    
    let params: url.URLParams = new url.URLParams()
    params.append('fod' ,'1')
    params.append('bard','2')
    axios.post('https://developer.mozilla.org/?' + params.toString()).then((res: AxiosResponse) => {
      let message = "request result: " + JSON.stringify(res.data);
    }).catch((err:AxiosError) => {
      let message = "request error: " + err.message;
    })
    
-   方式二：使用axios接口，请求参数写在config对象的params中。
    
    axios({ url: 'https://developer.mozilla.org/?', method: 'post', params: { fod: '1', bard: '2', } }).then((res: AxiosResponse) => {
      let message = "request result: " + JSON.stringify(res.data);
    }).catch((err:AxiosError) => {
      let message = "request error: " + err.message;
    })
    

**参考链接**

[URLParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-url#urlparams9)
