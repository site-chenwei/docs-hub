---
title: "RemoteCommunication"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "模块"
  - "RemoteCommunication"
captured_at: "2026-04-17T01:48:27.056Z"
---

# RemoteCommunication

#### 概述

提供远程通信能力相关接口。

支持http会话功能。

**起始版本：** 5.0.0(12)

#### 汇总

#### \[h2\]文件

| 名称 | 描述 |
| :-- | :-- |
| [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h) | 声明用于访问远程通信的API。提供基本的函数，结构体和const定义。 |

#### \[h2\]结构体

| 名称 | 描述 |
| :-- | :-- |
| struct [Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer) | 文本存储结构。 |
| struct [Rcp\_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback) | [Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)中使用的简单表单数据字段值。 |
| struct [Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value) | 表单字段文件值。 |
| struct [Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value) | 简单表单数据字段值，参见[Rcp\_Form](#rcp_form)和[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。 |
| struct [Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value) | 多部分表单域值，在[Rcp\_MultipartForm](#rcp_multipartform)中使用。 |
| struct [Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content) | 请求的内容。 |
| struct [Rcp\_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value) | 请求或响应的标头映射的值类型。 |
| struct [Rcp\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry) | 请求或响应的标头的所有键值对。 |
| struct [Rcp\_Credential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___credential) | 凭据。某些服务器或代理服务器需要。 |
| struct [Rcp\_ServerAuthentication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication) | 服务器身份验证。 |
| struct [Rcp\_Urls](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls) | URL，用于确定主机是否正在使用代理。 |
| struct [Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions) | 代理配置中用于过滤不使用代理的URLs。 |
| struct [Rcp\_CertificateAuthority](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___certificate_authority) | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| struct [Rcp\_ClientCertificate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| struct [Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration) | 请求的安全配置。 |
| struct [Rcp\_WebProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy) | 自定义代理配置。 |
| struct [Rcp\_IpAndPort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_and_port) | 该接口用在[Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)中，表示一个DNS服务器的地址和端口。 |
| struct [Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers) | DNS服务器。[Rcp\_DnsConfiguration.dnsRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration#dnsrules)中的类型之一。 |
| struct [Rcp\_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address) | 指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)。 |
| struct [Rcp\_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item) | 描述单个静态DNS规则。 |
| struct [Rcp\_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule) | 静态DNS规则。 |
| struct [Rcp\_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule) | DNS规则配置。 |
| struct [Rcp\_OnDataReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_data_receive_callback) | 接收到数据时回调。[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中的配置。 |
| struct [Rcp\_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback) | 收发时回调配置，在[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置。 |
| struct [Rcp\_OnHeaderReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_header_receive_callback) | [Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的接收到的header的回调配置。 |
| struct [Rcp\_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback) | 在[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的数据结束或取消事件的回调配置。 |
| struct [Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler) | 监听不同HTTP事件的回调函数。 |
| struct [Rcp\_Timeout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___timeout) | 请求的超时配置。 |
| struct [Rcp\_DnsOverHttps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_over_https) | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| struct [Rcp\_TransferConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_configuration) | 传输配置。 |
| struct [Rcp\_InfoToCollect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___info_to_collect) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| struct [Rcp\_TracingConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration) | 请求追踪配置。 |
| struct [Rcp\_ProxyConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration) | 代理配置。 |
| struct [Rcp\_DnsConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration) | DNS解析配置。 |
| struct [Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration) | 请求配置。 |
| struct [Rcp\_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range) | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| struct [Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) | 网络请求。 |
| struct [Rcp\_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry) | 描述请求的所有Cookie键值对。 |
| struct [Rcp\_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info) | 描述存储在[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中的调试信息的结构。 |
| struct [Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry) | 响应Cookie属性条目。 |
| struct [Rcp\_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies) | 响应Cookie。 |
| struct [Rcp\_TimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___time_info) | 响应计时信息。 |
| struct [Rcp\_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object) | 响应回调结构体。 |
| struct [Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response) | 网络请求的响应。 |
| struct [Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor) | 异步拦截器。 |
| struct [Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor) | 同步拦截器。 |
| struct [Rcp\_InterceptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor_array) | 异步拦截器数组。 |
| struct [Rcp\_SyncInterceptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor_array) | 同步拦截器数组。 |
| struct [Rcp\_SessionListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_listener) | 关闭或取消会话事件的回调函数。 |
| struct [Rcp\_ConnectionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___connection_configuration) | 连接配置。 |
| struct [Rcp\_SessionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration) | 会话配置。 |
| struct [Rcp\_OnBinaryReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_binary_receive_callback) | 接收到响应的二进制数据时的回调。 |
| struct [Rcp\_OnStatusCodeReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_status_code_callback) | 接收到响应的状态码时的回调。 |

#### \[h2\]宏定义

| 名称 | 描述 |
| :-- | :-- |
| [RCP\_MAX\_REQUEST\_ID\_LEN](#rcp_max_request_id_len) 32 | 请求ID的最大长度。 |
| [RCP\_MAX\_CONTENT\_TYPE\_LEN](#rcp_max_content_type_len) 64 | 内容类型最大长度。 |
| [RCP\_MAX\_FILENAME\_LEN](#rcp_max_filename_len) 128 | 文件名最大长度。 |
| [RCP\_MAX\_PATH\_LEN](#rcp_max_path_len) 128 | 路径的最大长度。 |
| [RCP\_METHOD\_GET](#rcp_method_get) "GET" | HTTP get方法。 |
| [RCP\_METHOD\_HEAD](#rcp_method_head) "HEAD" | HTTP head方法。 |
| [RCP\_METHOD\_OPTIONS](#rcp_method_options) "OPTIONS" | HTTP options方法。 |
| [RCP\_METHOD\_TRACE](#rcp_method_trace) "TRACE" | HTTP trace方法。 |
| [RCP\_METHOD\_DELETE](#rcp_method_delete) "DELETE" | HTTP delete方法。 |
| [RCP\_METHOD\_POST](#rcp_method_post) "POST" | HTTP post方法。 |
| [RCP\_METHOD\_PUT](#rcp_method_put) "PUT" | HTTP put方法。 |
| [RCP\_METHOD\_PATCH](#rcp_method_patch) "PATCH" | HTTP patch方法。 |
| [RCP\_IP\_MAX\_LEN](#rcp_ip_max_len) 40 | IP地址的最大长度。 |
| [RCP\_HOST\_MAX\_LEN](#rcp_host_max_len) 256 | 主机名的最大长度。 |

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef enum [Rcp\_FormValueType](#rcp_formvaluetype) [Rcp\_FormValueType](#rcp_formvaluetype) | 表单值类型。 |
| typedef int(\* [Rcp\_GetDataCallback](#rcp_getdatacallback)) (char \*out, uint32\_t size) | 通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。 |
| typedef enum [Rcp\_ContentOrPathOrCallbackType](#rcp_contentorpathorcallbacktype) [Rcp\_ContentOrPathOrCallbackType](#rcp_contentorpathorcallbacktype) | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback)中使用的数据。 |
| typedef struct [Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer) [Rcp\_Buffer](#rcp_buffer) | 文本存储结构。 |
| typedef struct [Rcp\_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback) [Rcp\_ContentOrPathOrCallback](#rcp_contentorpathorcallback) | [Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)中使用的简单表单数据字段值。 |
| typedef enum [Rcp\_MultipartValueType](#rcp_multipartvaluetype) [Rcp\_MultipartValueType](#rcp_multipartvaluetype) | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)中使用的数据。 |
| typedef struct [Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value) [Rcp\_FormFieldFileValue](#rcp_formfieldfilevalue) | 表单字段文件值。 |
| typedef struct [Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value) [Rcp\_FormFieldValue](#rcp_formfieldvalue) | 简单表单数据字段值，参见[Rcp\_Form](#rcp_form)和[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。 |
| typedef struct [Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value) [Rcp\_MultipartFormFieldValue](#rcp_multipartformfieldvalue) | 多部分表单域值，在[Rcp\_MultipartForm](#rcp_multipartform)中使用。 |
| typedef enum [Rcp\_ContentType](#rcp_contenttype) [Rcp\_ContentType](#rcp_contenttype) | 内容类型。用于区分[Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中使用的数据。 |
| typedef struct [Rcp\_Form](#rcp_form) [Rcp\_Form](#rcp_form) | 简单表单。 |
| typedef struct [Rcp\_MultipartForm](#rcp_multipartform) [Rcp\_MultipartForm](#rcp_multipartform) | 多部分表单。 |
| typedef struct [Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content) [Rcp\_RequestContent](#rcp_requestcontent) | 请求的内容。 |
| typedef struct [Rcp\_Headers](#rcp_headers) [Rcp\_Headers](#rcp_headers) | 请求或响应的标头。 |
| typedef struct [Rcp\_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value) [Rcp\_HeaderValue](#rcp_headervalue) | 请求或响应的标头映射的值类型。 |
| typedef struct [Rcp\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry) [Rcp\_HeaderEntry](#rcp_headerentry) | 请求或响应的标头的所有键值对。 |
| typedef enum [Rcp\_AuthenticationType](#rcp_authenticationtype) [Rcp\_AuthenticationType](#rcp_authenticationtype) | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| typedef struct [Rcp\_Credential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___credential) [Rcp\_Credential](#rcp_credential) | 凭据。某些服务器或代理服务器需要。 |
| typedef struct [Rcp\_ServerAuthentication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication) [Rcp\_ServerAuthentication](#rcp_serverauthentication) | 服务器身份验证。 |
| typedef bool(\* [Rcp\_ExclusionFunction](#rcp_exclusionfunction)) (const char \*url) | 判断host是否使用代理的函数指针。 |
| typedef struct [Rcp\_Urls](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls) [Rcp\_Urls](#rcp_urls) | url，用于确定主机是否正在使用代理。 |
| typedef enum [Rcp\_ExclusionsValueType](#rcp_exclusionsvaluetype) [Rcp\_ExclusionsValueType](#rcp_exclusionsvaluetype) | 代理排除中使用的数据类型. 用于区分[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用的数据。 |
| typedef struct [Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions) [Rcp\_Exclusions](#rcp_exclusions) | 代理配置中用于过滤不使用代理的URLs。 |
| typedef enum [Rcp\_CertType](#rcp_certtype) [Rcp\_CertType](#rcp_certtype) | 客户端证书类型。 |
| typedef struct [Rcp\_CertificateAuthority](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___certificate_authority) [Rcp\_CertificateAuthority](#rcp_certificateauthority) | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| typedef struct [Rcp\_ClientCertificate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate) [Rcp\_ClientCertificate](#rcp_clientcertificate) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| typedef enum [Rcp\_RemoteValidationType](#rcp_remotevalidationtype) [Rcp\_RemoteValidationType](#rcp_remotevalidationtype) | 远程验证类型。 |
| typedef struct [Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration) [Rcp\_SecurityConfiguration](#rcp_securityconfiguration) | 请求的安全配置。 |
| typedef enum [Rcp\_ProxyTunnelMode](#rcp_proxytunnelmode) [Rcp\_ProxyTunnelMode](#rcp_proxytunnelmode) | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。 |
| typedef struct [Rcp\_WebProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy) [Rcp\_WebProxy](#rcp_webproxy) | 自定义代理配置。 |
| typedef struct [Rcp\_IpAndPort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_and_port) [Rcp\_IpAndPort](#rcp_ipandport) | 该接口用在[Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)中，表示一个DNS服务器的地址和端口。 |
| typedef struct [Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers) [Rcp\_DnsServers](#rcp_dnsservers) | DNS服务器。[Rcp\_DnsConfiguration.dnsRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration#dnsrules)中的类型之一。 |
| typedef struct [Rcp\_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address) [Rcp\_IpAddress](#rcp_ipaddress) | 指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)。 |
| typedef struct [Rcp\_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item) [Rcp\_StaticDnsRuleItem](#rcp_staticdnsruleitem) | 描述单个静态DNS规则。 |
| typedef struct [Rcp\_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule) [Rcp\_StaticDnsRule](#rcp_staticdnsrule) | 静态DNS规则。 |
| typedef [Rcp\_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address) \*(\* [Rcp\_DynamicDnsRuleFunction](#rcp_dynamicdnsrulefunction)) (const char \*host, uint16\_t port) | 一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。 |
| typedef enum [Rcp\_DnsRuleType](#rcp_dnsruletype) [Rcp\_DnsRuleType](#rcp_dnsruletype) | DNS规则类型。用于区分[Rcp\_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule)中使用的dns规则类型。 |
| typedef struct [Rcp\_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule) [Rcp\_DnsRule](#rcp_dnsrule) | DNS规则配置。 |
| typedef size\_t(\* [Rcp\_OnDataReceiveCallbackFunc](#rcp_ondatareceivecallbackfunc)) (void \*usrObject, const char \*data) | 接收到响应正文时调用的回调函数（字符数据）。 |
| typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](#rcp_onbinaryreceivecallbackfunc)) (void \*usrObject, [Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer) \*buffer) | 接收到响应正文时调用的回调函数（二进制数据）。 |
| typedef void (\* [Rcp\_OnStatusCodeReceiveCallbackFunc](#rcp_onstatuscodereceivecallbackfunc))(void \*usrObject, uint32\_t statusCode) | 接收到响应状态码时调用的回调函数。 |
| typedef void(\* [Rcp\_OnProgressCallbackFunc](#rcp_onprogresscallbackfunc)) (void \*usrObject, uint64\_t totalSize, uint64\_t transferredSize) | 请求/响应数据传输过程中调用的回调函数。 |
| typedef void(\* [Rcp\_OnHeaderReceiveCallbackFunc](#rcp_onheaderreceivecallbackfunc)) (void \*usrObject, [Rcp\_Headers](#rcp_headers) \*headers) | 收到所有请求时调用的回调。 |
| typedef void(\* [Rcp\_OnVoidCallbackFunc](#rcp_onvoidcallbackfunc)) (void \*usrObject) | 请求的DataEnd或Canceled事件回调的回调函数。 |
| typedef struct [Rcp\_OnDataReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_data_receive_callback) [Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback) | 接收到数据时回调。[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中的配置。 |
| typedef struct [Rcp\_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback) [Rcp\_OnProgressCallback](#rcp_onprogresscallback) | 收发时回调配置，在[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置。 |
| typedef struct [Rcp\_OnHeaderReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_header_receive_callback) [Rcp\_OnHeaderReceiveCallback](#rcp_onheaderreceivecallback) | [Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的接收到的header回调配置。 |
| typedef struct [Rcp\_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback) [Rcp\_OnVoidCallback](#rcp_onvoidcallback) | 在[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的数据结束或已取消事件的回调配置。 |
| typedef struct [Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler) [Rcp\_EventsHandler](#rcp_eventshandler) | 监听不同HTTP事件的回调函数。 |
| typedef struct [Rcp\_Timeout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___timeout) [Rcp\_Timeout](#rcp_timeout) | 请求的超时配置。 |
| typedef struct [Rcp\_DnsOverHttps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_over_https) [Rcp\_DnsOverHttps](#rcp_dnsoverhttps) | HTTPS上的DNS配置如果设置，则首选由DOH DNS服务器解析的地址。 |
| typedef enum [Rcp\_PathPreference](#rcp_pathpreference) [Rcp\_PathPreference](#rcp_pathpreference) | 请求路径首选项。 |
| typedef struct [Rcp\_TransferConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_configuration) [Rcp\_TransferConfiguration](#rcp_transferconfiguration) | 传输配置。 |
| typedef struct [Rcp\_InfoToCollect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___info_to_collect) [Rcp\_InfoToCollect](#rcp_infotocollect) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| typedef struct [Rcp\_TracingConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration) [Rcp\_TracingConfiguration](#rcp_tracingconfiguration) | 请求追踪配置。 |
| typedef enum [Rcp\_ProxyType](#rcp_proxytype) [Rcp\_ProxyType](#rcp_proxytype) | 代理类型。用于区分不同的代理配置。 |
| typedef struct [Rcp\_ProxyConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration) [Rcp\_ProxyConfiguration](#rcp_proxyconfiguration) | 代理配置。 |
| typedef struct [Rcp\_DnsConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration) [Rcp\_DnsConfiguration](#rcp_dnsconfiguration) | DNS解析配置。 |
| typedef struct [Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration) [Rcp\_Configuration](#rcp_configuration) | 请求配置。 |
| typedef struct [Rcp\_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range) [Rcp\_TransferRange](#rcp_transferrange) | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅返回HTTP响应的一部分。 |
| typedef struct [Rcp\_RequestCookies](#rcp_requestcookies) [Rcp\_RequestCookies](#rcp_requestcookies) | 请求Cookie。 |
| typedef struct [Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) [Rcp\_Request](#rcp_request) | 网络请求。 |
| typedef struct [Rcp\_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry) [Rcp\_RequestCookieEntry](#rcp_requestcookieentry) | 描述请求的所有Cookie键值对。 |
| typedef enum [Rcp\_StatusCode](#rcp_statuscode) [Rcp\_StatusCode](#rcp_statuscode) | 请求响应的状态码。 |
| typedef enum [Rcp\_DebugEvent](#rcp_debugevent) [Rcp\_DebugEvent](#rcp_debugevent) | 描述调试信息的事件类型。 |
| typedef struct [Rcp\_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info) [Rcp\_DebugInfo](#rcp_debuginfo) | 描述存储在[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中的调试信息的结构。 |
| typedef struct [Rcp\_CookieAttributes](#rcp_cookieattributes) [Rcp\_CookieAttributes](#rcp_cookieattributes) | 描述[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中Cookie属性的类型。 |
| typedef struct [Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry) [Rcp\_CookieAttributeEntry](#rcp_cookieattributeentry) | 响应Cookie属性条目。 |
| typedef struct [Rcp\_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies) [Rcp\_ResponseCookies](#rcp_responsecookies) | 响应Cookie。 |
| typedef struct [Rcp\_TimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___time_info) [Rcp\_TimeInfo](#rcp_timeinfo) | 响应计时信息。 |
| typedef struct [Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response) [Rcp\_Response](#rcp_response) | 网络请求的响应。 |
| typedef void(\* [Rcp\_ResponseCallback](#rcp_responsecallback)) (void \*usrCtx, [Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response) \*response, uint32\_t errCode) | 响应回调函数指针。 |
| typedef struct [Rcp\_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object) [Rcp\_ResponseCallbackObject](#rcp_responsecallbackobject) | 响应回调结构体。 |
| typedef struct [Rcp\_RequestHandler](#rcp_requesthandler) [Rcp\_RequestHandler](#rcp_requesthandler) | 与[Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)关联的异步处理器。 |
| typedef struct [Rcp\_SyncRequestHandler](#rcp_syncrequesthandler) [Rcp\_SyncRequestHandler](#rcp_syncrequesthandler) | 与[Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)关联的同步处理器。 |
| typedef struct [Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor) [Rcp\_Interceptor](#rcp_interceptor) | 异步拦截器。 |
| typedef struct [Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor) [Rcp\_SyncInterceptor](#rcp_syncinterceptor) | 同步拦截器。 |
| typedef struct [Rcp\_InterceptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor_array) [Rcp\_InterceptorArray](#rcp_interceptorarray) | 异步拦截器数组。 |
| typedef struct [Rcp\_SyncInterceptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor_array) [Rcp\_SyncInterceptorArray](#rcp_syncinterceptorarray) | 同步拦截器数组。 |
| typedef enum [Rcp\_SessionType](#rcp_sessiontype) [Rcp\_SessionType](#rcp_sessiontype) | 会话类型。 |
| typedef struct [Rcp\_Session](#rcp_session) [Rcp\_Session](#rcp_session) | 会话。 |
| typedef struct [Rcp\_SessionListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_listener) [Rcp\_SessionListener](#rcp_sessionlistener) | 关闭或取消会话事件的回调函数。 |
| typedef struct [Rcp\_ConnectionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___connection_configuration) [Rcp\_ConnectionConfiguration](#rcp_connectionconfiguration) | 连接配置。 |
| typedef struct [Rcp\_SessionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration) [Rcp\_SessionConfiguration](#rcp_sessionconfiguration) | 会话配置。 |
| typedef struct [Rcp\_OnBinaryReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_binary_receive_callback) [Rcp\_OnBinaryReceiveCallback](#rcp_onbinaryreceivecallback) | 接收到响应的二进制数据时的回调。 |
| typedef struct [Rcp\_OnStatusCodeReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_status_code_callback) [Rcp\_OnStatusCodeReceiveCallback](#rcp_onstatuscodereceivecallback) | 接收到响应的状态码时的回调。 |

#### \[h2\]枚举

| 名称 | 描述 |
| :-- | :-- |
| 
[Rcp\_FormValueType](#rcp_formvaluetype) {

RCP\_FORM\_VALUE\_TYPE\_INT32, RCP\_FORM\_VALUE\_TYPE\_INT64, RCP\_FORM\_VALUE\_TYPE\_BOOL, RCP\_FORM\_VALUE\_TYPE\_STRING,

RCP\_FORM\_VALUE\_TYPE\_DOUBLE

}

 | 表单值类型。 |
| [Rcp\_ContentOrPathOrCallbackType](#rcp_contentorpathorcallbacktype) { RCP\_FILE\_VALUE\_TYPE\_CONTENT, RCP\_FILE\_VALUE\_TYPE\_PATH, RCP\_FILE\_VALUE\_TYPE\_CALLBACK } | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback)中使用的数据。 |
| [Rcp\_MultipartValueType](#rcp_multipartvaluetype) { RCP\_TYPE\_FORM\_FIELD\_VALUE, RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE } | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)中使用的数据。 |
| [Rcp\_ContentType](#rcp_contenttype) { RCP\_CONTENT\_TYPE\_STRING, RCP\_CONTENT\_TYPE\_FORM, RCP\_CONTENT\_TYPE\_MULTIPARTFORM, RCP\_CONTENT\_TYPE\_GETCALLBACK } | 内容类型。用于区分[Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中使用的数据。 |
| [Rcp\_AuthenticationType](#rcp_authenticationtype) { RCP\_AUTHENTICATION\_AUTO, RCP\_AUTHENTICATION\_BASIC, RCP\_AUTHENTICATION\_NTLM, RCP\_AUTHENTICATION\_DIGEST } | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| [Rcp\_ExclusionsValueType](#rcp_exclusionsvaluetype) { RCP\_EXCLUSION\_USE\_URL\_ARRAY, RCP\_EXCLUSION\_USE\_CALLBACK } | 代理排除中使用的数据类型，用于区分[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用的数据。 |
| [Rcp\_CertType](#rcp_certtype) { RCP\_CERT\_PEM, RCP\_CERT\_DER, RCP\_CERT\_P12 } | 客户端证书类型。 |
| [Rcp\_RemoteValidationType](#rcp_remotevalidationtype) { RCP\_REMOTE\_VALIDATION\_SYSTEM, RCP\_REMOTE\_VALIDATION\_SKIP, RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY } | 远程验证类型。 |
| [Rcp\_ProxyTunnelMode](#rcp_proxytunnelmode) { RCP\_PROXY\_TUNNEL\_AUTO, RCP\_PROXY\_TUNNEL\_ALWAYS } | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。 |
| [Rcp\_DnsRuleType](#rcp_dnsruletype) { RCP\_DNS\_RULE\_DNS\_SERVERS, RCP\_DNS\_RULE\_STATIC, RCP\_DNS\_RULE\_DYNAMIC } | DNS规则类型。用于区分[Rcp\_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule)中使用的DNS规则类型。 |
| [Rcp\_PathPreference](#rcp_pathpreference) { RCP\_PATH\_PREFERENCE\_AUTO, RCP\_PATH\_PREFERENCE\_WIFI, RCP\_PATH\_PREFERENCE\_CELLULAR } | 请求路径首选项。 |
| [Rcp\_ProxyType](#rcp_proxytype) { RCP\_PROXY\_SYSTEM, RCP\_PROXY\_CUSTOM, RCP\_PROXY\_NO\_PROXY } | 代理类型。用于区分不同的代理配置。 |
| 

[Rcp\_StatusCode](#rcp_statuscode) {

RCP\_NONE = 0, RCP\_OK = 200, RCP\_CREATED, RCP\_ACCEPTED,

RCP\_NOT\_AUTHORITATIVE, RCP\_NO\_CONTENT, RCP\_RESET, RCP\_PARTIAL,

RCP\_MULTI\_CHOICE = 300, RCP\_MOVED\_PERMANENTLY, RCP\_MOVED\_TEMPORARILY, RCP\_SEE\_OTHER,

RCP\_NOT\_MODIFIED, RCP\_USE\_PROXY, RCP\_BAD\_REQUEST = 400, RCP\_UNAUTHORIZED,

RCP\_PAYMENT\_REQUIRED, RCP\_FORBIDDEN, RCP\_NOT\_FOUND, RCP\_BAD\_METHOD,

RCP\_NOT\_ACCEPTABLE, RCP\_PROXY\_AUTH, RCP\_CLIENT\_TIMEOUT, RCP\_CONFLICT,

RCP\_GONE, RCP\_LENGTH\_REQUIRED, RCP\_PRECON\_FAILED, RCP\_ENTITY\_TOO\_LARGE,

RCP\_REQ\_TOO\_LONG, RCP\_UNSUPPORTED\_TYPE, RCP\_INTERNAL\_ERROR = 500, RCP\_NOT\_IMPLEMENTED,

RCP\_BAD\_GATEWAY, RCP\_UNAVAILABLE, RCP\_GATEWAY\_TIMEOUT, RCP\_VERSION

}

 | 请求响应的状态码。 |
| 

[Rcp\_DebugEvent](#rcp_debugevent) {

RCP\_DEBUG\_EVENT\_TEXT, RCP\_DEBUG\_EVENT\_HEADER\_IN, RCP\_DEBUG\_EVENT\_HEADER\_OUT, RCP\_DEBUG\_EVENT\_DATA\_IN,

RCP\_DEBUG\_EVENT\_DATA\_OUT, RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN, RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT

}

 | 描述调试信息的事件类型。 |
| [Rcp\_SessionType](#rcp_sessiontype) { RCP\_SESSION\_TYPE\_HTTP = 0, RCP\_SESSION\_TYPE\_MAX = 100 } | 会话类型。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_Form](#rcp_form) \* [HMS\_Rcp\_CreateForm](#hms_rcp_createform) (void) | 创建一个简单表单。 |
| void [HMS\_Rcp\_DestroyForm](#hms_rcp_destroyform) ([Rcp\_Form](#rcp_form) \*form) | 销毁一个简单表单。 |
| uint32\_t [HMS\_Rcp\_SetFormValue](#hms_rcp_setformvalue) ([Rcp\_Form](#rcp_form) \*form, const char \*key, const [Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value) \*value) | 设置简单表单的键值对。 |
| [Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value) \* [HMS\_Rcp\_GetFormValue](#hms_rcp_getformvalue) ([Rcp\_Form](#rcp_form) \*form, const char \*key) | 通过键获取一个简单表单的对应值。 |
| [Rcp\_MultipartForm](#rcp_multipartform) \* [HMS\_Rcp\_CreateMultipartForm](#hms_rcp_createmultipartform) (void) | 创建一个多部分表单。 |
| void [HMS\_Rcp\_DestroyMultipartForm](#hms_rcp_destroymultipartform) ([Rcp\_MultipartForm](#rcp_multipartform) \*multipartForm) | 销毁一个多部分表单。 |
| uint32\_t [HMS\_Rcp\_SetMultipartFormValue](#hms_rcp_setmultipartformvalue) ([Rcp\_MultipartForm](#rcp_multipartform) \*multipartForm, const char \*key, const [Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value) \*value) | 设置多部分表单的键值对。 |
| [Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value) \* [HMS\_Rcp\_GetMultipartFormValue](#hms_rcp_getmultipartformvalue) ([Rcp\_MultipartForm](#rcp_multipartform) \*multipartForm, const char \*key) | 通过键获取多部分表单的值。 |
| [Rcp\_Headers](#rcp_headers) \* [HMS\_Rcp\_CreateHeaders](#hms_rcp_createheaders) (void) | 为请求或响应创建标头。 |
| void [HMS\_Rcp\_DestroyHeaders](#hms_rcp_destroyheaders) ([Rcp\_Headers](#rcp_headers) \*headers) | 销毁请求或响应的标头。 |
| uint32\_t [HMS\_Rcp\_SetHeaderValue](#hms_rcp_setheadervalue) ([Rcp\_Headers](#rcp_headers) \*headers, const char \*name, const char \*value) | 设置请求或响应头的键值对。 |
| [Rcp\_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value) \* [HMS\_Rcp\_GetHeaderValue](#hms_rcp_getheadervalue) ([Rcp\_Headers](#rcp_headers) \*headers, const char \*name) | 通过键获取请求或响应头的值。 |
| [Rcp\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry) \* [HMS\_Rcp\_GetHeaderEntries](#hms_rcp_getheaderentries) ([Rcp\_Headers](#rcp_headers) \*headers) | 获取请求或响应头的所有键值对。 |
| void [HMS\_Rcp\_DestroyHeaderEntries](#hms_rcp_destroyheaderentries) ([Rcp\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry) \*headerEntry) | 销毁[HMS\_Rcp\_GetHeaderEntries](#hms_rcp_getheaderentries)中获取的所有键值对。 |
| [Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \* [HMS\_Rcp\_CreateRequest](#hms_rcp_createrequest) (const char \*url) | 创建请求。 |
| void [HMS\_Rcp\_DestroyRequest](#hms_rcp_destroyrequest) ([Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \*request) | 销毁请求。 |
| [Rcp\_RequestCookies](#rcp_requestcookies) \* [HMS\_Rcp\_CreateRequestCookies](#hms_rcp_createrequestcookies) (void) | 创建空的请求Cookie。 |
| void [HMS\_Rcp\_DestroyRequestCookies](#hms_rcp_destroyrequestcookies) ([Rcp\_RequestCookies](#rcp_requestcookies) \*cookies) | 销毁请求Cookie。 |
| uint32\_t [HMS\_Rcp\_SetRequestCookieValue](#hms_rcp_setrequestcookievalue) ([Rcp\_RequestCookies](#rcp_requestcookies) \*cookies, const char \*name, const char \*value) | 设置请求Cookie。 |
| char \* [HMS\_Rcp\_GetRequestCookieValue](#hms_rcp_getrequestcookievalue) ([Rcp\_RequestCookies](#rcp_requestcookies) \*cookies, const char \*name) | 通过名称获取请求Cookie的值。 |
| [Rcp\_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry) \* [HMS\_Rcp\_GetRequestCookieEntries](#hms_rcp_getrequestcookieentries) ([Rcp\_RequestCookies](#rcp_requestcookies) \*cookies) | 获取请求Cookie中的所有键值对。 |
| void [HMS\_Rcp\_DestroyRequestCookieEntries](#hms_rcp_destroyrequestcookieentries) ([Rcp\_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry) \*cookieEntry) | 销毁从[HMS\_Rcp\_GetRequestCookieValue](#hms_rcp_getrequestcookievalue)获取的所有与请求Cookie相关的键值对。 |
| const char \* [HMS\_Rcp\_GetResponseCookieAttrValue](#hms_rcp_getresponsecookieattrvalue) ([Rcp\_CookieAttributes](#rcp_cookieattributes) \*cookieAttributes, const char \*name) | 通过名称获取Cookie属性的值。 |
| [Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry) \* [HMS\_Rcp\_GetResponseCookieAttrEntries](#hms_rcp_getresponsecookieattrentries) ([Rcp\_CookieAttributes](#rcp_cookieattributes) \*cookieAttributes) | 在[Rcp\_CookieAttributes](#rcp_cookieattributes)中获取所有响应Cookie属性。 |
| void [HMS\_Rcp\_DestroyResponseCookieAttrEntries](#hms_rcp_destroyresponsecookieattrentries) ([Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry) \*entries) | 销毁响应Cookie属性。 |
| uint32\_t [HMS\_Rcp\_CallNextRequestHandler](#hms_rcp_callnextrequesthandler) ([Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \*request, const [Rcp\_RequestHandler](#rcp_requesthandler) \*next, const [Rcp\_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object) \*responseCallback) | 在拦截器[Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)的函数中可以调用下一个拦截器或defaultHandler。 |
| [Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response) \* [HMS\_Rcp\_CallNextSyncRequestHandler](#hms_rcp_callnextsyncrequesthandler) ([Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \*request, const [Rcp\_SyncRequestHandler](#rcp_syncrequesthandler) \*next, uint32\_t \*errCode) | 在拦截器[Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)的函数中可以调用下一个拦截器或默认处理器。 |
| [Rcp\_Session](#rcp_session) \* [HMS\_Rcp\_CreateSession](#hms_rcp_createsession) (const [Rcp\_SessionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration) \*configuration, uint32\_t \*errCode) | 创建会话。 |
| const char \* [HMS\_Rcp\_GetSessionId](#hms_rcp_getsessionid) ([Rcp\_Session](#rcp_session) \*session) | 获取会话ID。 |
| const [Rcp\_SessionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration) \* [HMS\_Rcp\_GetSessionConfiguration](#hms_rcp_getsessionconfiguration) ([Rcp\_Session](#rcp_session) \*session) | 获取会话配置。 |
| [Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response) \* [HMS\_Rcp\_FetchSync](#hms_rcp_fetchsync) ([Rcp\_Session](#rcp_session) \*session, [Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \*request, uint32\_t \*errCode) | 发送同步请求并获取响应。 |
| uint32\_t [HMS\_Rcp\_Fetch](#hms_rcp_fetch) ([Rcp\_Session](#rcp_session) \*session, [Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \*request, const [Rcp\_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object) \*responseCallback) | 发送异步请求并获取响应。 |
| uint32\_t [HMS\_Rcp\_CancelRequest](#hms_rcp_cancelrequest) ([Rcp\_Session](#rcp_session) \*session, const [Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \*request) | 取消一个请求。 |
| uint32\_t [HMS\_Rcp\_CancelSession](#hms_rcp_cancelsession) ([Rcp\_Session](#rcp_session) \*session) | 取消会话。 |
| uint32\_t [HMS\_Rcp\_CloseSession](#hms_rcp_closesession) ([Rcp\_Session](#rcp_session) \*\*session) | 关闭会话。 |
| uint32\_t [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](#hms_rcp_setrequestonbinarydatarecvcallback) ([Rcp\_Request](#rcp_request) \*request, [Rcp\_OnBinaryReceiveCallback](#rcp_onbinaryreceivecallback) onBinaryReceiveCallback) | 为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback)功能一致。设置后将替换在[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback)。 |
| uint32\_t [HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](#hms_rcp_setrequestonstatuscodereceivecallback) ([Rcp\_Request](#rcp_request) \*request, [Rcp\_OnStatusCodeReceiveCallback](#rcp_onstatuscodereceivecallback) onStatusCodeReceiveCallback) | 为请求设置响应状态码接收回调函数。 |

#### 宏定义说明

#### \[h2\]RCP\_HOST\_MAX\_LEN

```cpp
#define RCP_HOST_MAX_LEN   256
```

**描述**

主机名的最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_IP\_MAX\_LEN

```cpp
#define RCP_IP_MAX_LEN   40
```

**描述**

IP地址的最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_MAX\_CONTENT\_TYPE\_LEN

```cpp
#define RCP_MAX_CONTENT_TYPE_LEN   64
```

**描述**

内容类型最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_MAX\_FILENAME\_LEN

```cpp
#define RCP_MAX_FILENAME_LEN   128
```

**描述**

文件名最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_MAX\_PATH\_LEN

```cpp
#define RCP_MAX_PATH_LEN   128
```

**描述**

路径的最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_MAX\_REQUEST\_ID\_LEN

```cpp
#define RCP_MAX_REQUEST_ID_LEN   32
```

**描述**

请求ID的最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_DELETE

```cpp
#define RCP_METHOD_DELETE   "DELETE"
```

**描述**

HTTP delete方法。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_GET

```cpp
#define RCP_METHOD_GET   "GET"
```

**描述**

HTTP get方法。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_HEAD

```cpp
#define RCP_METHOD_HEAD   "HEAD"
```

**描述**

HTTP head方法。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_OPTIONS

```cpp
#define RCP_METHOD_OPTIONS   "OPTIONS"
```

**描述**

HTTP options方法。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_PATCH

```cpp
#define RCP_METHOD_PATCH   "PATCH"
```

**描述**

HTTP patch方法。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_POST

```cpp
#define RCP_METHOD_POST   "POST"
```

**描述**

HTTP post方法。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_PUT

```cpp
#define RCP_METHOD_PUT   "PUT"
```

**描述**

HTTP put方法。

**起始版本：** 5.0.0(12)

#### \[h2\]RCP\_METHOD\_TRACE

```cpp
#define RCP_METHOD_TRACE   "TRACE"
```

**描述**

HTTP trace方法。

**起始版本：** 5.0.0(12)

#### 类型定义说明

#### \[h2\]Rcp\_AuthenticationType

```cpp
typedef enum Rcp_AuthenticationType Rcp_AuthenticationType
```

**描述**

枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Buffer

```cpp
typedef struct Rcp_Buffer Rcp_Buffer
```

**描述**

文本存储结构。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_CertificateAuthority

```cpp
typedef struct Rcp_CertificateAuthority Rcp_CertificateAuthority
```

**描述**

用于验证远程服务器标识的证书颁发机构（CA）。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_CertType

```cpp
typedef enum Rcp_CertType Rcp_CertType
```

**描述**

客户端证书类型。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ClientCertificate

```cpp
typedef struct Rcp_ClientCertificate Rcp_ClientCertificate
```

**描述**

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Configuration

```cpp
typedef struct Rcp_Configuration Rcp_Configuration
```

**描述**

请求配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ConnectionConfiguration

```cpp
typedef struct Rcp_ConnectionConfiguration Rcp_ConnectionConfiguration
```

**描述**

连接配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ContentOrPathOrCallback

```cpp
typedef struct Rcp_ContentOrPathOrCallback Rcp_ContentOrPathOrCallback
```

**描述**

[Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)中使用的简单表单数据字段值。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ContentOrPathOrCallbackType

```cpp
typedef enum Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallbackType
```

**描述**

回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback)中使用的数据。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ContentType

```cpp
typedef enum Rcp_ContentType Rcp_ContentType
```

**描述**

内容类型。用于区分[Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中使用的数据。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_CookieAttributeEntry

```cpp
typedef struct Rcp_CookieAttributeEntry Rcp_CookieAttributeEntry
```

**描述**

响应Cookie属性条目。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_CookieAttributes

```cpp
typedef struct Rcp_CookieAttributes Rcp_CookieAttributes
```

**描述**

描述[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中Cookie属性的类型。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Credential

```cpp
typedef struct Rcp_Credential Rcp_Credential
```

**描述**

凭据。按需设置，某些服务器或代理服务器需要用户名密码。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DebugEvent

```cpp
typedef enum Rcp_DebugEvent Rcp_DebugEvent
```

**描述**

描述调试信息的事件类型。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DebugInfo

```cpp
typedef struct Rcp_DebugInfo Rcp_DebugInfo
```

**描述**

描述存储在[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中的调试信息的结构。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DnsConfiguration

```cpp
typedef struct Rcp_DnsConfiguration Rcp_DnsConfiguration
```

**描述**

DNS解析配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DnsOverHttps

```cpp
typedef struct Rcp_DnsOverHttps Rcp_DnsOverHttps
```

**描述**

如果设置了HTTPS上的DNS配置，则首选由DOH DNS服务器解析的地址。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DnsRule

```cpp
typedef struct Rcp_DnsRule Rcp_DnsRule
```

**描述**

DNS规则配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DnsRuleType

```cpp
typedef enum Rcp_DnsRuleType Rcp_DnsRuleType
```

**描述**

DNS规则类型。用于区分[Rcp\_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule)中使用的DNS规则类型。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DnsServers

```cpp
typedef struct Rcp_DnsServers Rcp_DnsServers
```

**描述**

DNS服务器。[Rcp\_DnsConfiguration.dnsRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration#dnsrules)中的类型之一。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_DynamicDnsRuleFunction

```cpp
typedef Rcp_IpAddress*(* Rcp_DynamicDnsRuleFunction) (const char *host, uint16_t port)
```

**描述**

一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| host | 主机名称。 |
| port | 端口号。 |

**返回：**

Rcp\_IpAddress\* 指向[Rcp\_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address)的指针。基于主机名和端口的IP地址。

#### \[h2\]Rcp\_EventsHandler

```cpp
typedef struct Rcp_EventsHandler Rcp_EventsHandler
```

**描述**

监听不同HTTP事件的回调函数。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ExclusionFunction

```cpp
typedef bool(* Rcp_ExclusionFunction) (const char *url)
```

**描述**

判断host是否使用代理的函数指针。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| url | 请求的URL。 |

**返回：**

bool 返回是否使用代理。

#### \[h2\]Rcp\_Exclusions

```cpp
typedef struct Rcp_Exclusions Rcp_Exclusions
```

**描述**

代理配置中用于过滤不使用代理的URLs。

如果[Rcp\_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#url)匹配[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)规则，则[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)不会使用代理。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ExclusionsValueType

```cpp
typedef enum Rcp_ExclusionsValueType Rcp_ExclusionsValueType
```

**描述**

代理排除中使用的数据类型。用于区分[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用的数据。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Form

```cpp
typedef struct Rcp_FormRcp_Form
```

**描述**

简单表单。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_FormFieldFileValue

```cpp
typedef struct Rcp_FormFieldFileValue Rcp_FormFieldFileValue
```

**描述**

表单字段文件值。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_FormFieldValue

```cpp
typedef struct Rcp_FormFieldValue Rcp_FormFieldValue
```

**描述**

简单表单数据字段值，参见[Rcp\_Form](#rcp_form)和[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_FormValueType

```cpp
typedef enum Rcp_FormValueType Rcp_FormValueType
```

**描述**

表单值类型。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_GetDataCallback

```cpp
typedef int(* Rcp_GetDataCallback) (char *out, uint32_t size)
```

**描述**

通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。

该回调可能使用在[Rcp\_FormFieldFileValue.contentOrPathOrCb](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value#contentorpathorcb)和[Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| out | 输出的数据 |
| size | 数据大小 |

**返回：**

int 返回值为-1表示错误，返回值0表示停止传输。

#### \[h2\]Rcp\_HeaderEntry

```cpp
typedef struct Rcp_HeaderEntry Rcp_HeaderEntry
```

**描述**

请求或响应的标头的所有键值对。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Headers

```cpp
typedef struct Rcp_Headers Rcp_Headers
```

**描述**

请求或响应的标头。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_HeaderValue

```cpp
typedef struct Rcp_HeaderValue Rcp_HeaderValue
```

**描述**

请求或响应的标头映射的值类型。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_InfoToCollect

```cpp
typedef struct Rcp_InfoToCollect Rcp_InfoToCollect
```

**描述**

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Interceptor

```cpp
typedef struct Rcp_Interceptor Rcp_Interceptor
```

**描述**

异步拦截器。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_InterceptorArray

```cpp
typedef struct Rcp_InterceptorArray Rcp_InterceptorArray
```

**描述**

异步拦截器数组。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_IpAddress

```cpp
typedef struct Rcp_IpAddress Rcp_IpAddress
```

**描述**

指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_IpAndPort

```cpp
typedef struct Rcp_IpAndPort Rcp_IpAndPort
```

**描述**

该接口用在[Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)中，表示一个DNS服务器的地址和端口。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_MultipartForm

```cpp
typedef struct Rcp_MultipartForm Rcp_MultipartForm
```

**描述**

多部分表单。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_MultipartFormFieldValue

```cpp
typedef struct Rcp_MultipartFormFieldValue Rcp_MultipartFormFieldValue
```

**描述**

多部分表单域值，在[Rcp\_MultipartForm](#rcp_multipartform)中使用。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_MultipartValueType

```cpp
typedef enum Rcp_MultipartValueType Rcp_MultipartValueType
```

**描述**

多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)中使用的数据。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_OnDataReceiveCallback

```cpp
typedef struct Rcp_OnDataReceiveCallback Rcp_OnDataReceiveCallback
```

**描述**

接收到数据时回调。[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中的配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_OnDataReceiveCallbackFunc

```cpp
typedef size_t(* Rcp_OnDataReceiveCallbackFunc) (void *usrObject, const char *data)
```

**描述**

接收到响应正文时调用的回调函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| usrObject | 用户定义的对象。 |
| data | 响应体。 |

**返回：**

size\_t 响应体的长度。

#### \[h2\]Rcp\_OnBinaryReceiveCallback

```cpp
typedef struct Rcp_OnBinaryReceiveCallback Rcp_OnBinaryReceiveCallback
```

**描述**

响应的二进制数据接收回调函数。

**起始版本：** 5.0.1(13)

#### \[h2\]Rcp\_OnBinaryReceiveCallbackFunc

```cpp
typedef size_t(* Rcp_OnBinaryReceiveCallbackFunc) (void *usrObject, Rcp_Buffer *buffer)
```

**描述**

接收到响应正文时调用的二进制回调函数。其回调点与[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback)一致。设置后其回调函数会替换在[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback)，功能上能够涵盖[Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback)的字符数据接收获取功能。

**起始版本：** 5.0.1(13)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| usrObject | 用户定义的对象。 |
| buffer | 响应体的二进制数据。 |

**返回：**

size\_t 响应体二进制数据的长度。

#### \[h2\]Rcp\_OnStatusCodeReceiveCallback

```cpp
typedef struct Rcp_OnStatusCodeReceiveCallback Rcp_OnStatusCodeReceiveCallback
```

**描述**

用于接收响应状态码的回调函数。

**起始版本：** 6.0.1(21)

#### \[h2\]Rcp\_OnStatusCodeReceiveCallbackFunc

```cpp
typedef void (*Rcp_OnStatusCodeReceiveCallbackFunc) (void *usrObject, uint32_t statusCode)
```

**描述**

接收到响应状态码时调用的回调函数。

**起始版本：** 6.0.1(21)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| usrObject | 用户定义的对象。 |
| statusCode | 响应状态码。 |

#### \[h2\]Rcp\_OnHeaderReceiveCallback

```cpp
typedef struct Rcp_OnHeaderReceiveCallback Rcp_OnHeaderReceiveCallback
```

**描述**

[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的接收到的header的回调配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_OnHeaderReceiveCallbackFunc

```cpp
typedef void(* Rcp_OnHeaderReceiveCallbackFunc) (void *usrObject, Rcp_Headers *headers)
```

**描述**

收到所有请求时调用的回调。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| usrObject | 用户定义的对象。 |
| headers | 接收到的请求头，指向[Rcp\_Headers](#rcp_headers)的指针。 |

#### \[h2\]Rcp\_OnProgressCallback

```cpp
typedef struct Rcp_OnProgressCallback Rcp_OnProgressCallback
```

**描述**

收发时回调配置，在[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_OnProgressCallbackFunc

```cpp
typedef void(* Rcp_OnProgressCallbackFunc) (void *usrObject, uint64_t totalSize, uint64_t transferredSize)
```

**描述**

请求/响应数据传输过程中调用的回调函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| usrObject | 用户定义的对象。 |
| totalSize | 数据总大小。 |
| transferredSize | 已传输的数据大小。 |

#### \[h2\]Rcp\_OnVoidCallback

```cpp
typedef struct Rcp_OnVoidCallback Rcp_OnVoidCallback
```

**描述**

在[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的数据结束或已取消事件的回调配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_OnVoidCallbackFunc

```cpp
typedef void(* Rcp_OnVoidCallbackFunc) (void *usrObject)
```

**描述**

请求的DataEnd或Canceled事件回调的回调函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| usrObject | 用户定义的对象。 |

#### \[h2\]Rcp\_PathPreference

```cpp
typedef enum Rcp_PathPreference Rcp_PathPreference
```

**描述**

请求路径首选项。

调用者的建议，最终由系统决定使用哪个路径。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ProxyConfiguration

```cpp
typedef struct Rcp_ProxyConfiguration Rcp_ProxyConfiguration
```

**描述**

代理配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ProxyTunnelMode

```cpp
typedef enum Rcp_ProxyTunnelMode Rcp_ProxyTunnelMode
```

**描述**

用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。'auto'表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ProxyType

```cpp
typedef enum Rcp_ProxyType Rcp_ProxyType
```

**描述**

代理类型。用于区分不同的代理配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_RemoteValidationType

```cpp
typedef enum Rcp_RemoteValidationType Rcp_RemoteValidationType
```

**描述**

远程验证类型。

用于区分验证远程服务器身份的CA，在[Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)中描述。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Request

```cpp
typedef struct Rcp_Request Rcp_Request
```

**描述**

网络请求。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_RequestContent

```cpp
typedef struct Rcp_RequestContent Rcp_RequestContent
```

**描述**

请求的内容。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_RequestCookieEntry

```cpp
typedef struct Rcp_RequestCookieEntry Rcp_RequestCookieEntry
```

**描述**

描述请求的所有Cookie键值对。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_RequestCookies

```cpp
typedef struct Rcp_RequestCookies Rcp_RequestCookies
```

**描述**

请求Cookie。

允许你在一个对象中指定你需要的所有Cookies，例如：{'name1'：'value1'，'name2'：'value2'}。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_RequestHandler

```cpp
typedef struct Rcp_RequestHandler Rcp_RequestHandler
```

**描述**

与[Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)关联的异步处理器。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Response

```cpp
typedef struct Rcp_Response Rcp_Response
```

**描述**

网络请求的响应。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ResponseCallback

```cpp
typedef void(* Rcp_ResponseCallback) (void *usrCtx, Rcp_Response *response, uint32_t errCode)
```

**描述**

响应回调函数指针。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| usrCtx | 用户上下文。 |
| response | 请求所生成的响应。指向[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)的指针。 |
| errCode | 
\[out\] 表示常见的错误代码。

0：成功。

[1007900001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900001-不支持的协议)：不支持的协议。

[1007900003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900003-url格式错误)：URL使用了错误/非法的格式或缺少URL。

[1007900005](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900005-代理服务器域名解析失败)：无法解析代理名称。

[1007900006](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900006-域名解析失败)：无法解析主机名。

[1007900007](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900007-无法连接到服务器)：无法连接到服务器。

[1007900008](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900008-服务器返回非法数据)：异常的服务器回复。

[1007900009](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900009-拒绝对远程资源的访问)：对远程资源的访问被拒绝。

[1007900016](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900016-http2帧层错误)：HTTP2框架层中的错误。

[1007900018](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900018-服务器返回数据不完整)：已传输部分文件。

[1007900025](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900025-上传失败)：上载失败。

[1007900026](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900026-从文件应用程序中打开读取本地数据失败)：无法从文件/应用程序中打开/读取本地数据。

[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900027-内存不足)：内存不足。

[1007900028](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900028-操作超时)：已达到超时。

[1007900047](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900047-重定向次数达到最大值)：重定向数达到最大数量。

[1007900052](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900052-服务器没有返回内容)：服务器没有返回任何内容（没有标头，没有数据）。

[1007900055](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900055-发送网络数据失败)：向对等方发送数据失败。

[1007900056](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900056-接收网络数据失败)：从对等方接收数据时失败。

[1007900058](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900058-本地ssl证书错误)：本地SSL证书有问题。

[1007900059](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900059-无法使用指定的密码)：无法使用指定的SSL密钥。

[1007900060](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900060-远程服务器ssl证书或ssh秘钥不正确)：SSL对等证书或SSH远程密钥不正常。

[1007900061](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900061-无法识别或错误的http编码格式)：无法识别或错误的HTTP内容或传输编码。

[1007900063](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900063-超出最大文件大小)：超过了最大文件大小。

[1007900070](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900070-服务器磁盘空间不足)：磁盘已满或分配超出。

[1007900073](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900073-服务器返回文件已存在)：远程文件已存在。

[1007900077](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900077-ssl-ca证书不存在或没有访问权限)：SSL CA证书有问题 (路径？ 访问权限？)。

[1007900078](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900078-url请求的文件不存在)：找不到远程文件。

[1007900992](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900992-请求已被取消)：请求已取消。

[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900993-会话已关闭)：会话已关闭或无效。

[1007900094](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900094-身份校验失败)：身份验证函数返回了错误。

[1007900201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900201-禁止明文传输)：禁止明文传输。从6.1.0(23)起新增支持此错误码。

[1007900995](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900995-获取系统代理失败)：获取系统代理失败。

[1007900996](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900996-代理类型不支持)：代理类型不受支持。

[1007900997](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900997-无效的内容类型)：无效的内容类型。

[1007900998](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900998--所请求的方法不被支持)：方法不受支持。

[1007900999](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900999-内部错误)：内部错误。

Others：1007900000 + CURL\_ERROR\_CODE。 更多常见的错误码，请参见[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)。

 |

#### \[h2\]Rcp\_ResponseCallbackObject

```cpp
typedef struct Rcp_ResponseCallbackObject Rcp_ResponseCallbackObject
```

**描述**

响应回调结构体。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ResponseCookies

```cpp
typedef struct Rcp_ResponseCookies Rcp_ResponseCookies
```

**描述**

响应Cookie。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_SecurityConfiguration

```cpp
typedef struct Rcp_SecurityConfiguration Rcp_SecurityConfiguration
```

**描述**

请求的安全配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_ServerAuthentication

```cpp
typedef struct Rcp_ServerAuthentication Rcp_ServerAuthentication
```

**描述**

服务器身份验证。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Session

```cpp
typedef struct Rcp_Session Rcp_Session
```

**描述**

会话。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_SessionConfiguration

```cpp
typedef struct Rcp_SessionConfiguration Rcp_SessionConfiguration
```

**描述**

会话配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_SessionListener

```cpp
typedef struct Rcp_SessionListener Rcp_SessionListener
```

**描述**

关闭或取消会话事件的回调函数。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_SessionType

```cpp
typedef enum Rcp_SessionType Rcp_SessionType
```

**描述**

会话类型。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_StaticDnsRule

```cpp
typedef struct Rcp_StaticDnsRule Rcp_StaticDnsRule
```

**描述**

静态DNS规则。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_StaticDnsRuleItem

```cpp
typedef struct Rcp_StaticDnsRuleItem Rcp_StaticDnsRuleItem
```

**描述**

描述单个静态DNS规则。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_StatusCode

```cpp
typedef enum Rcp_StatusCode Rcp_StatusCode
```

**描述**

请求响应的状态码。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_SyncInterceptor

```cpp
typedef struct Rcp_SyncInterceptor Rcp_SyncInterceptor
```

**描述**

同步拦截器。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_SyncInterceptorArray

```cpp
typedef struct Rcp_SyncInterceptorArray Rcp_SyncInterceptorArray
```

**描述**

同步拦截器数组。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_SyncRequestHandler

```cpp
typedef struct Rcp_SyncRequestHandler Rcp_SyncRequestHandler
```

**描述**

与[Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)关联的同步处理器。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_TimeInfo

```cpp
typedef struct Rcp_TimeInfo Rcp_TimeInfo
```

**描述**

响应计时信息。

它将在[Rcp\_Response.timeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response#timeinfo)中被收集，[Rcp\_TracingConfiguration.collectTimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration#collecttimeinfo)决定是否收集它。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Timeout

```cpp
typedef struct Rcp_Timeout Rcp_Timeout
```

**描述**

请求的超时配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_TracingConfiguration

```cpp
typedef struct Rcp_TracingConfiguration Rcp_TracingConfiguration
```

**描述**

请求追踪配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_TransferConfiguration

```cpp
typedef struct Rcp_TransferConfiguration Rcp_TransferConfiguration
```

**描述**

传输配置。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_TransferRange

```cpp
typedef struct Rcp_TransferRange Rcp_TransferRange
```

**描述**

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_Urls

```cpp
typedef struct Rcp_Urls Rcp_Urls
```

**描述**

URLs，用于确定主机是否正在使用代理。

**起始版本：** 5.0.0(12)

#### \[h2\]Rcp\_WebProxy

```cpp
typedef struct Rcp_WebProxy Rcp_WebProxy
```

**描述**

自定义代理配置。

**起始版本：** 5.0.0(12)

#### 枚举类型说明

#### \[h2\]Rcp\_AuthenticationType

```cpp
enum Rcp_AuthenticationType
```

**描述**

枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_AUTHENTICATION\_AUTO | 自动 |
| RCP\_AUTHENTICATION\_BASIC | 基本类型 |
| RCP\_AUTHENTICATION\_NTLM | NTLM类型 |
| RCP\_AUTHENTICATION\_DIGEST | DIGEST类型 |

#### \[h2\]Rcp\_CertType

```cpp
enum Rcp_CertType
```

**描述**

客户端证书类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_CERT\_PEM | PEM证书类型。 |
| RCP\_CERT\_DER | DER证书类型。 |
| RCP\_CERT\_P12 | P12证书类型。 |

#### \[h2\]Rcp\_ContentOrPathOrCallbackType

```cpp
enum Rcp_ContentOrPathOrCallbackType
```

**描述**

回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_FILE\_VALUE\_TYPE\_CONTENT | 表示内容类型。 |
| RCP\_FILE\_VALUE\_TYPE\_PATH | 表示路径类型。 |
| RCP\_FILE\_VALUE\_TYPE\_CALLBACK | 表示回调类型。 |

#### \[h2\]Rcp\_ContentType

```cpp
enum Rcp_ContentType
```

**描述**

内容类型。用于区分[Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_CONTENT\_TYPE\_STRING | 文本。 |
| RCP\_CONTENT\_TYPE\_FORM | 表格。 |
| RCP\_CONTENT\_TYPE\_MULTIPARTFORM | 多部分表格。 |
| RCP\_CONTENT\_TYPE\_GETCALLBACK | 回调函数。 |

#### \[h2\]Rcp\_DebugEvent

```cpp
enum Rcp_DebugEvent
```

**描述**

描述调试信息的事件类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_DEBUG\_EVENT\_TEXT | 文本事件。 |
| RCP\_DEBUG\_EVENT\_HEADER\_IN | 传入标头事件。 |
| RCP\_DEBUG\_EVENT\_HEADER\_OUT | 传出标头事件。 |
| RCP\_DEBUG\_EVENT\_DATA\_IN | 接收数据事件。 |
| RCP\_DEBUG\_EVENT\_DATA\_OUT | 外发数据事件。 |
| RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN | 传入SSL/TLS事件。 |
| RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT | 传出SSL/TLS事件。 |

#### \[h2\]Rcp\_DnsRuleType

```cpp
enum Rcp_DnsRuleType
```

**描述**

DNS规则类型。用于区分[Rcp\_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule)中使用的DNS规则类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_DNS\_RULE\_DNS\_SERVERS | DNS服务器。 |
| RCP\_DNS\_RULE\_STATIC | 静态DNS规则。 |
| RCP\_DNS\_RULE\_DYNAMIC | 动态DNS规则。 |

#### \[h2\]Rcp\_ExclusionsValueType

```cpp
enum Rcp_ExclusionsValueType
```

**描述**

代理排除中使用的数据类型. 用于区分[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_EXCLUSION\_USE\_URL\_ARRAY | 表示在[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用urls。 |
| RCP\_EXCLUSION\_USE\_CALLBACK | 在[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用回调函数[Rcp\_ExclusionFunction](#rcp_exclusionfunction)。 |

#### \[h2\]Rcp\_FormValueType

```cpp
enum Rcp_FormValueType
```

**描述**

表单值类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_FORM\_VALUE\_TYPE\_INT32 | 表示INT32数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_INT64 | 表示INT64数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_BOOL | 表示bool数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_STRING | 表示string数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_DOUBLE | 表示double数据类型。 |

#### \[h2\]Rcp\_MultipartValueType

```cpp
enum Rcp_MultipartValueType
```

**描述**

多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_TYPE\_FORM\_FIELD\_VALUE | 表示使用[Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value)。 |
| RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE | 表示使用[Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)。 |

#### \[h2\]Rcp\_PathPreference

```cpp
enum Rcp_PathPreference
```

**描述**

请求路径首选项。

这只是调用者的建议，系统决定使用哪个路径。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_PATH\_PREFERENCE\_AUTO | 自动。 |
| RCP\_PATH\_PREFERENCE\_WIFI | 倾向WIFI网络。 |
| RCP\_PATH\_PREFERENCE\_CELLULAR | 倾向蜂窝网路。 |

#### \[h2\]Rcp\_ProxyTunnelMode

```cpp
enum Rcp_ProxyTunnelMode
```

**描述**

用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_PROXY\_TUNNEL\_AUTO | 自动。 |
| RCP\_PROXY\_TUNNEL\_ALWAYS | 总是创建。 |

#### \[h2\]Rcp\_ProxyType

```cpp
enum Rcp_ProxyType
```

**描述**

代理类型。用于区分不同的代理配置。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_PROXY\_SYSTEM | 系统代理。 |
| RCP\_PROXY\_CUSTOM | 使用自定义代理，选择后将解析[Rcp\_ProxyConfiguration.customProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration#customproxy)。 |
| RCP\_PROXY\_NO\_PROXY | 不使用代理。 |

#### \[h2\]Rcp\_RemoteValidationType

```cpp
enum Rcp_RemoteValidationType
```

**描述**

远程验证类型。

用于区分验证远程服务器身份的CA在[Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)中描述。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_REMOTE\_VALIDATION\_SYSTEM | 系统验证。 |
| RCP\_REMOTE\_VALIDATION\_SKIP | 跳过验证。 |
| RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY | CA验证。 |

#### \[h2\]Rcp\_SessionType

```cpp
enum Rcp_SessionType
```

**描述**

会话类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_SESSION\_TYPE\_HTTP | 使用HTTP会话。 |
| RCP\_SESSION\_TYPE\_MAX | Rcp\_SessionType的最大值。 |

#### \[h2\]Rcp\_StatusCode

```cpp
enum Rcp_StatusCode
```

**描述**

请求响应的状态码。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| RCP\_NONE = 0 | 默认值。 |
| RCP\_OK = 200 | 请求成功。 |
| RCP\_CREATED = 201 | 请求成功并创建了新资源。 |
| RCP\_ACCEPTED = 202 | 请求已接受，但尚未处理。 |
| RCP\_NOT\_AUTHORITATIVE = 203 | 返回信息不是原始的。 |
| RCP\_NO\_CONTENT = 204 | 请求成功，但无返回内容。 |
| RCP\_RESET= 205 | 请求已成功处理，但需要重置内容。 |
| RCP\_PARTIAL = 206 | 部分内容请求成功。 |
| RCP\_MULTI\_CHOICE = 300 | 对于该请求，服务器支持多种操作方式。 |
| RCP\_MOVED\_PERMANENTLY = 301 | 永久重定向。 |
| RCP\_MOVED\_TEMPORARILY = 302 | 临时重定向。 |
| RCP\_SEE\_OTHER = 303 | 查看其他位置。 |
| RCP\_NOT\_MODIFIED = 304 | 资源未修改。 |
| RCP\_USE\_PROXY = 305 | 使用代理。 |
| RCP\_BAD\_REQUEST = 400 | 请求语法错误。 |
| RCP\_UNAUTHORIZED = 401 | 未授权。 |
| RCP\_PAYMENT\_REQUIRED = 402 | 需要付费。 |
| RCP\_FORBIDDEN = 403 | 禁止访问。 |
| RCP\_NOT\_FOUND = 404 | 资源未找到。 |
| RCP\_BAD\_METHOD = 405 | 方法不允许。 |
| RCP\_NOT\_ACCEPTABLE = 406 | 不接受。 |
| RCP\_PROXY\_AUTH = 407 | 需要代理授权。 |
| RCP\_CLIENT\_TIMEOUT = 408 | 请求超时。 |
| RCP\_CONFLICT = 409 | 冲突。 |
| RCP\_GONE = 410 | 资源已永久删除。 |
| RCP\_LENGTH\_REQUIRED = 411 | 需要有效长度。 |
| RCP\_PRECON\_FAILED = 412 | 未满足前提条件。 |
| RCP\_ENTITY\_TOO\_LARGE = 413 | 请求实体过大。 |
| RCP\_REQ\_TOO\_LONG = 414 | 请求的 URI 过长。 |
| RCP\_UNSUPPORTED\_TYPE = 415 | 不支持的媒体类型。 |
| RCP\_INTERNAL\_ERROR = 500 | 服务器内部错误。 |
| RCP\_NOT\_IMPLEMENTED = 501 | 尚未实现。 |
| RCP\_BAD\_GATEWAY = 502 | 网关错误。 |
| RCP\_UNAVAILABLE = 503 | 服务不可用。 |
| RCP\_GATEWAY\_TIMEOUT = 504 | 网关超时。 |
| RCP\_VERSION = 505 | 不支持的HTTP版本。 |

#### 函数说明

#### \[h2\]HMS\_Rcp\_CallNextRequestHandler()

```cpp
uint32_t HMS_Rcp_CallNextRequestHandler (Rcp_Request * request, const Rcp_RequestHandler * next, const Rcp_ResponseCallbackObject * responseCallback )
```

**描述**

在拦截器[Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)的函数中可以调用下一个拦截器或defaultHandler。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| request | 指向[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。 |
| next | 指向下一个异步处理器的指针[Rcp\_RequestHandler](#rcp_requesthandler)。 |
| responseCallback | 响应回调。指向[Rcp\_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object)的指针。 |

**返回：**

uint32\_t。[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败) - 参数错误 或 表示下一个异步处理器的返回值。

#### \[h2\]HMS\_Rcp\_CallNextSyncRequestHandler()

```cpp
Rcp_Response* HMS_Rcp_CallNextSyncRequestHandler (Rcp_Request * request, const Rcp_SyncRequestHandler * next, uint32_t * errCode )
```

**描述**

在拦截器[Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)的函数中可以调用下一个拦截器或默认处理器。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| request | 指向[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。 |
| next | 指向下一个同步处理器的指针[Rcp\_SyncRequestHandler](#rcp_syncrequesthandler)。 |
| errCode | 输出项。[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)：参数错误 或 表示下一个同步处理器的返回值。 |

**返回：**

Rcp\_Response\* 返回响应。

#### \[h2\]HMS\_Rcp\_CancelRequest()

```cpp
uint32_t HMS_Rcp_CancelRequest (Rcp_Session * session, const Rcp_Request * request )
```

**描述**

取消一个请求。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| session | 需要取消请求的会话。指向[Rcp\_Session](#rcp_session)的指针。 |
| request | 需要取消的请求。指向要关闭的[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。 |

**返回：**

取消成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900993-会话已关闭)。

#### \[h2\]HMS\_Rcp\_CancelSession()

```cpp
uint32_t HMS_Rcp_CancelSession (Rcp_Session * session)
```

**描述**

取消会话。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| session | 需要取消的会话。指向要关闭的[Rcp\_Session](#rcp_session)的指针。 |

**返回：**

取消成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900993-会话已关闭)。

#### \[h2\]HMS\_Rcp\_CloseSession()

```cpp
uint32_t HMS_Rcp_CloseSession (Rcp_Session ** session)
```

**描述**

关闭会话。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| session | 需要关闭的会话。指向[Rcp\_Session](#rcp_session)指针的指针。 |

**返回：**

关闭成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900993-会话已关闭)。

#### \[h2\]HMS\_Rcp\_CreateForm()

```cpp
Rcp_Form* HMS_Rcp_CreateForm (void)
```

**描述**

创建一个简单表单。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_Form\* 指向[Rcp\_Form](#rcp_form)的指针。

#### \[h2\]HMS\_Rcp\_CreateHeaders()

```cpp
Rcp_Headers* HMS_Rcp_CreateHeaders (void)
```

**描述**

为请求或响应创建标头。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_Headers\* 创建的标头。指向[Rcp\_Headers](#rcp_headers)的指针。

#### \[h2\]HMS\_Rcp\_CreateMultipartForm()

```cpp
Rcp_MultipartForm* HMS_Rcp_CreateMultipartForm (void)
```

**描述**

创建一个多部分表单。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_MultipartForm\* 返回创建的多部分表单，指向[Rcp\_MultipartForm](#rcp_multipartform)的指针。

#### \[h2\]HMS\_Rcp\_CreateRequest()

```cpp
Rcp_Request* HMS_Rcp_CreateRequest (const char * url)
```

**描述**

创建请求。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| url | 请求URL。 |

**返回：**

Rcp\_Request\* 返回创建的请求。指向[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。

#### \[h2\]HMS\_Rcp\_CreateRequestCookies()

```cpp
Rcp_RequestCookies* HMS_Rcp_CreateRequestCookies (void)
```

**描述**

创建空的请求Cookie。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_RequestCookies\* 返回指向已创建的[Rcp\_RequestCookies](#rcp_requestcookies)的指针。

#### \[h2\]HMS\_Rcp\_CreateSession()

```cpp
Rcp_Session* HMS_Rcp_CreateSession (const Rcp_SessionConfiguration * configuration, uint32_t * errCode )
```

**描述**

创建会话。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| configuration | 会话配置。 |
| errCode | 
0：成功。

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)：参数错误。

[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)：权限不足。

[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900027-内存不足)：内存不足。

 |

**返回：**

Rcp\_Session\* 返回创建的会话。指向[Rcp\_Session](#rcp_session)的指针。

#### \[h2\]HMS\_Rcp\_DestroyForm()

```cpp
void HMS_Rcp_DestroyForm (Rcp_Form * form)
```

**描述**

销毁一个简单表单。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| form | 要销毁的表格。指向[Rcp\_Form](#rcp_form)的指针。 |

#### \[h2\]HMS\_Rcp\_DestroyHeaderEntries()

```cpp
void HMS_Rcp_DestroyHeaderEntries (Rcp_HeaderEntry * headerEntry)
```

**描述**

销毁[HMS\_Rcp\_GetHeaderEntries](#hms_rcp_getheaderentries)中获取的所有键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| headerEntry | 指向要销毁的[Rcp\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry)的指针。 |

#### \[h2\]HMS\_Rcp\_DestroyHeaders()

```cpp
void HMS_Rcp_DestroyHeaders (Rcp_Headers * headers)
```

**描述**

销毁请求或响应的标头。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| headers | 指向要销毁的[Rcp\_Headers](#rcp_headers)的指针。 |

#### \[h2\]HMS\_Rcp\_DestroyMultipartForm()

```cpp
void HMS_Rcp_DestroyMultipartForm (Rcp_MultipartForm * multipartForm)
```

**描述**

销毁一个多部分表单。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| multipartForm | 要销毁的多部分表单。指向[Rcp\_MultipartForm](#rcp_multipartform)的指针。 |

#### \[h2\]HMS\_Rcp\_DestroyRequest()

```cpp
void HMS_Rcp_DestroyRequest (Rcp_Request * request)
```

**描述**

销毁请求。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| request | 指向要销毁的[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。 |

#### \[h2\]HMS\_Rcp\_DestroyRequestCookieEntries()

```cpp
void HMS_Rcp_DestroyRequestCookieEntries (Rcp_RequestCookieEntry * cookieEntry)
```

**描述**

销毁从[HMS\_Rcp\_GetRequestCookieValue](#hms_rcp_getrequestcookievalue)获取的所有与请求Cookie相关的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cookieEntry | 指向要销毁的[Rcp\_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry)的指针。 |

#### \[h2\]HMS\_Rcp\_DestroyRequestCookies()

```cpp
void HMS_Rcp_DestroyRequestCookies (Rcp_RequestCookies * cookies)
```

**描述**

销毁请求Cookie。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cookies | 指向要销毁的[Rcp\_RequestCookies](#rcp_requestcookies)的指针。 |

#### \[h2\]HMS\_Rcp\_DestroyResponseCookieAttrEntries()

```cpp
void HMS_Rcp_DestroyResponseCookieAttrEntries (Rcp_CookieAttributeEntry * entries)
```

**描述**

销毁响应Cookie属性。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| entries | 指向要销毁的[Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry)的指针。 |

#### \[h2\]HMS\_Rcp\_Fetch()

```cpp
uint32_t HMS_Rcp_Fetch (Rcp_Session * session, Rcp_Request * request, const Rcp_ResponseCallbackObject * responseCallback )
```

**描述**

发送异步请求并获取响应。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| session | 发起请求使用的会话。指向[Rcp\_Session](#rcp_session)的指针。 |
| request | 发送的请求。指向[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。 |
| responseCallback | 指向用户定义的响应回调函数的指针。详情请参见[Rcp\_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object)。 |

**返回：**

执行成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900993-会话已关闭)。

**权限：**

ohos.permission.INTERNET（如需使用[PathPreference](#rcp_pathpreference-1)的RCP\_PATH\_PREFERENCE\_CELLULAR模式，则额外需要ohos.permission.GET\_NETWORK\_INFO）

#### \[h2\]HMS\_Rcp\_FetchSync()

```cpp
Rcp_Response* HMS_Rcp_FetchSync (Rcp_Session * session, Rcp_Request * request, uint32_t * errCode )
```

**描述**

发送同步请求并获取响应。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| session | 发起请求使用的会话。指向[Rcp\_Session](#rcp_session)的指针。 |
| request | 发送的请求。指向[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。 |
| errCode | 
\[out\] 输出常见的错误代码。

0：成功。

[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)：权限不足。

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)：参数错误。

[1007900001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900001-不支持的协议)：不支持的协议。

[1007900003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900003-url格式错误)：URL使用了错误/非法的格式或缺少URL。

[1007900005](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900005-代理服务器域名解析失败)：无法解析代理名称。

[1007900006](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900006-域名解析失败)：无法解析主机名。

[1007900007](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900007-无法连接到服务器)：无法连接到服务器。

[1007900008](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900008-服务器返回非法数据)：异常的服务器回复。

[1007900009](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900009-拒绝对远程资源的访问)：对远程资源的访问被拒绝。

[1007900016](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900016-http2帧层错误)：HTTP2框架层中的错误。

[1007900018](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900018-服务器返回数据不完整)：已传输部分文件。

[1007900025](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900025-上传失败)：上载失败。

[1007900026](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900026-从文件应用程序中打开读取本地数据失败)：无法从文件/应用程序中打开/读取本地数据。

[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900027-内存不足)：内存不足。

[1007900028](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900028-操作超时)：已达到超时。

[1007900047](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900047-重定向次数达到最大值)：重定向数达到最大数量。

[1007900052](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900052-服务器没有返回内容)：服务器没有返回任何内容（没有标头，没有数据）。

[1007900055](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900055-发送网络数据失败)：向对等方发送数据失败。

[1007900056](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900056-接收网络数据失败)：从对等方接收数据时失败。

[1007900058](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900058-本地ssl证书错误)：本地SSL证书有问题。

[1007900059](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900059-无法使用指定的密码)：无法使用指定的SSL密钥。

[1007900060](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900060-远程服务器ssl证书或ssh秘钥不正确)：SSL对等证书或SSH远程密钥不正常。

[1007900061](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900061-无法识别或错误的http编码格式)：无法识别或错误的HTTP内容或传输编码。

[1007900063](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900063-超出最大文件大小)：超过了最大文件大小。

[1007900070](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900070-服务器磁盘空间不足)：磁盘已满或分配超出。

[1007900073](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900073-服务器返回文件已存在)：远程文件已存在。

[1007900077](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900077-ssl-ca证书不存在或没有访问权限)：SSL CA证书有问题 (路径？ 访问权限?)。

[1007900078](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900078-url请求的文件不存在)：找不到远程文件。

[1007900992](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900992-请求已被取消)：请求已取消。

[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900993-会话已关闭)：会话已关闭或无效。

[1007900094](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900094-身份校验失败)：身份验证函数返回了错误。

[1007900201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900201-禁止明文传输)：禁止明文传输。从6.1.0(23)起新增支持此错误码。

[1007900995](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900995-获取系统代理失败)：获取系统代理失败。

[1007900996](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900996-代理类型不支持)：代理类型不受支持。

[1007900997](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900997-无效的内容类型)：无效的内容类型。

[1007900998](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900998--所请求的方法不被支持)：方法不受支持。

[1007900999](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900999-内部错误)：内部错误。

Others：1007900000 + CURL\_ERROR\_CODE。更多常见的错误码，请参见[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)。

 |

**返回：**

Rcp\_Response\* 返回的响应。指向[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)的指针。

**权限：**

ohos.permission.INTERNET（如需使用[PathPreference](#rcp_pathpreference-1)的RCP\_PATH\_PREFERENCE\_CELLULAR模式，则额外需要ohos.permission.GET\_NETWORK\_INFO）

#### \[h2\]HMS\_Rcp\_GetFormValue()

```cpp
Rcp_FormFieldValue* HMS_Rcp_GetFormValue (Rcp_Form * form, const char * key )
```

**描述**

通过键获取一个简单表单的对应值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| form | 指向[Rcp\_Form](#rcp_form)的指针。 |
| key | 键。 |

**返回：**

Rcp\_FormFieldValue\* 值。指向{@Rcp\_FormFieldValue}的指针。

#### \[h2\]HMS\_Rcp\_GetHeaderEntries()

```cpp
Rcp_HeaderEntry* HMS_Rcp_GetHeaderEntries (Rcp_Headers * headers)
```

**描述**

获取请求或响应头的所有键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| headers | 指向要获取所有键值对的[Rcp\_Headers](#rcp_headers)的指针。 |

**返回：**

Rcp\_HeaderEntry\* 指向所有获取到的键值对[Rcp\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry)。

#### \[h2\]HMS\_Rcp\_GetHeaderValue()

```cpp
Rcp_HeaderValue* HMS_Rcp_GetHeaderValue (Rcp_Headers * headers, const char * name )
```

**描述**

通过键获取请求或响应头的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| headers | 指向要获取值的[Rcp\_Headers](#rcp_headers)的指针。 |
| name | 键。 |

**返回：**

Rcp\_HeaderValue\* 指向获得的[Rcp\_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value)的指针。

#### \[h2\]HMS\_Rcp\_GetMultipartFormValue()

```cpp
Rcp_MultipartFormFieldValue* HMS_Rcp_GetMultipartFormValue (Rcp_MultipartForm * multipartForm, const char * key )
```

**描述**

通过键获取多部分表单的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| multipartForm | 需要获取值的多部分表单。指向[Rcp\_MultipartForm](#rcp_multipartform)的指针。 |
| key | 键。 |

**返回：**

Rcp\_MultipartFormFieldValue\* 多部分表单的值。指向[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)的指针。

#### \[h2\]HMS\_Rcp\_GetRequestCookieEntries()

```cpp
Rcp_RequestCookieEntry* HMS_Rcp_GetRequestCookieEntries (Rcp_RequestCookies * cookies)
```

**描述**

获取请求Cookie中的所有键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cookies | 需要获取所有键值对的请求Cookie。指向[Rcp\_RequestCookies](#rcp_requestcookies)的指针。 |

**返回：**

Rcp\_RequestCookieEntry\* 返回请求Cookie中的所有键值对。指向[Rcp\_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry)的指针。

#### \[h2\]HMS\_Rcp\_GetRequestCookieValue()

```cpp
char* HMS_Rcp_GetRequestCookieValue (Rcp_RequestCookies * cookies, const char * name )
```

**描述**

通过名称获取请求Cookie的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cookies | 需要获取值的请求Cookie。指向[Rcp\_RequestCookies](#rcp_requestcookies)的指针。 |
| name | 键。 |

**返回：**

char\* 返回请求Cookie的值。

#### \[h2\]HMS\_Rcp\_GetResponseCookieAttrEntries()

```cpp
Rcp_CookieAttributeEntry* HMS_Rcp_GetResponseCookieAttrEntries (Rcp_CookieAttributes * cookieAttributes)
```

**描述**

在[Rcp\_CookieAttributes](#rcp_cookieattributes)中获取所有响应Cookie属性。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cookieAttributes | 指向要获取所有Cookie属性的[Rcp\_CookieAttributes](#rcp_cookieattributes)的指针。 |

**返回：**

[Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry) \* 响应的Cookie属性列表。

#### \[h2\]HMS\_Rcp\_GetResponseCookieAttrValue()

```cpp
const char* HMS_Rcp_GetResponseCookieAttrValue (Rcp_CookieAttributes * cookieAttributes, const char * name )
```

**描述**

通过名称获取Cookie属性的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cookieAttributes | 指向要获取值的[Rcp\_CookieAttributes](#rcp_cookieattributes)的指针。 |
| name | 键。 |

**返回：**

char\* Cookie属性中的值。

#### \[h2\]HMS\_Rcp\_GetSessionConfiguration()

```cpp
const Rcp_SessionConfiguration* HMS_Rcp_GetSessionConfiguration (Rcp_Session * session)
```

**描述**

获取会话配置。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| session | 需要获取会话配置的会话。指向[Rcp\_Session](#rcp_session)的指针。 |

**返回：**

Rcp\_SessionConfiguration\* 返回的会话配置。指向[Rcp\_SessionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration)的指针。

#### \[h2\]HMS\_Rcp\_GetSessionId()

```cpp
const char* HMS_Rcp_GetSessionId (Rcp_Session * session)
```

**描述**

获取会话ID。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| session | 需要获取会话ID的会话。指向[Rcp\_Session](#rcp_session)的指针。 |

**返回：**

char\* 返回的会话ID。

#### \[h2\]HMS\_Rcp\_SetFormValue()

```cpp
uint32_t HMS_Rcp_SetFormValue (Rcp_Form * form, const char * key, const Rcp_FormFieldValue * value )
```

**描述**

设置简单表单的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| form | 需要设置键值对的表单。指向[Rcp\_Form](#rcp_form)的指针。 |
| key | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900027-内存不足)。

#### \[h2\]HMS\_Rcp\_SetHeaderValue()

```cpp
uint32_t HMS_Rcp_SetHeaderValue (Rcp_Headers * headers, const char * name, const char * value )
```

**描述**

设置请求或响应头的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| headers | 指向要设置的[Rcp\_Headers](#rcp_headers)的指针。 |
| name | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900027-内存不足)。

#### \[h2\]HMS\_Rcp\_SetMultipartFormValue()

```cpp
uint32_t HMS_Rcp_SetMultipartFormValue (Rcp_MultipartForm * multipartForm, const char * key, const Rcp_MultipartFormFieldValue * value )
```

**描述**

设置多部分表单的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| multipartForm | 需要设置的多部分表单。指向[Rcp\_MultipartForm](#rcp_multipartform)的指针。 |
| key | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900027-内存不足)。

#### \[h2\]HMS\_Rcp\_SetRequestCookieValue()

```cpp
uint32_t HMS_Rcp_SetRequestCookieValue (Rcp_RequestCookies * cookies, const char * name, const char * value )
```

**描述**

设置请求Cookie。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cookies | 需要设置的请求Cookie。指向[Rcp\_RequestCookies](#rcp_requestcookies)的指针。 |
| name | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-error-code#section1007900027-内存不足)。

#### \[h2\]HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback()

```cpp
uint32_t HMS_Rcp_SetRequestOnBinaryDataRecvCallback (Rcp_Request * request, Rcp_OnBinaryReceiveCallback onBinaryReceiveCallback);
```

**描述**

为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback)功能一致。设置后将替换在[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp\_OnDataReceiveCallback](#rcp_ondatareceivecallback)。

**起始版本：** 5.0.1(13)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| request | 需要设置二进制数据回调的请求。指向[Rcp\_Request](#rcp_request)的指针。 |
| onBinaryReceiveCallback | 需要设置的二进制数据接收回调函数。 |

**返回：**

设置成功返回0，参数错误时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)。

#### \[h2\]HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback()

```cpp
uint32_t HMS_Rcp_SetRequestOnStatusCodeReceiveCallback (Rcp_Request * request, Rcp_OnStatusCodeReceiveCallback onStatusCodeReceiveCallback);
```

**描述**

为请求设置响应状态码回调函数。在请求收到对端返回的响应码时触发。不可通过重新设置[Rcp\_OnStatusCodeReceiveCallbackFunc](#rcp_onstatuscodereceivecallbackfunc)为NULL实现取消监听。

**起始版本：** 6.0.1(21)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| request | 需要设置响应状态码回调的请求。指向[Rcp\_Request](#rcp_request)的指针。 |
| onStatusCodeReceiveCallback | 需要设置的响应状态码接收回调函数。 |

**返回：**

设置成功返回0，参数错误时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)。
