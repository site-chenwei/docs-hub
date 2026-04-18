---
title: "ModuleInstall"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-moduleinstall"
menu_path:
  - "参考"
  - "应用服务"
  - "AppGallery Kit（应用市场服务）"
  - "C API"
  - "模块"
  - "ModuleInstall"
captured_at: "2026-04-17T01:48:56.729Z"
---

# ModuleInstall

#### 概述

描述AppGallery kit提供按需分发能力。

**起始版本：** 5.0.2(14)

#### 汇总

#### \[h2\]文件

| 名称 | 描述 |
| :-- | :-- |
| [module\_install.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-module_install) | 声明按需分发能力提供的API。 |

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef struct [ModuleInstall\_InstalledModule](#moduleinstall_installedmodule) [ModuleInstall\_InstalledModule](#moduleinstall_installedmodule) | 安装模块信息。 |
| typedef struct [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) | 安装模块结果。 |
| typedef struct [ModuleInstall\_StatusCallback](#moduleinstall_statuscallback) [ModuleInstall\_StatusCallback](#moduleinstall_statuscallback) | 模块安装状态回调。 |
| typedef void (\*[ModuleInstall\_OnStatusCallback](#moduleinstall_onstatuscallback))(char \*bundleName, char \*eventInfo) | 监听回调函数。 |

#### \[h2\]枚举

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_ErrCode](#moduleinstall_errcode) | 枚举错误码。 |
| [ModuleInstall\_InstallStatus](#moduleinstall_installstatus) | 枚举安装状态。 |
| [ModuleInstall\_RequestCode](#moduleinstall_requestcode) | 枚举请求码。 |
| [ModuleInstall\_TaskStatus](#moduleinstall_taskstatus) | 枚举任务状态。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [HMS\_ModuleInstall\_GetInstalledModule](#hms_moduleinstall_getinstalledmodule) | 查询模块是否安装。 |
| [HMS\_ModuleInstall\_GetInstalledModuleName](#hms_moduleinstall_getinstalledmodulename) | 获取模块名。 |
| [HMS\_ModuleInstall\_GetInstalledModuleType](#hms_moduleinstall_getinstalledmoduletype) | 获取模块类型。 |
| [HMS\_ModuleInstall\_GetModuleInstallStatus](#hms_moduleinstall_getmoduleinstallstatus) | 获取模块安装状态。 |
| [HMS\_ModuleInstall\_FetchModules](#hms_moduleinstall_fetchmodules) | 请求下载模块。 |
| [HMS\_ModuleInstall\_GetFetchModulesRequestCode](#hms_moduleinstall_getfetchmodulesrequestcode) | 获取模块下载请求码。 |
| [HMS\_ModuleInstall\_GetFetchModulesTaskStatus](#hms_moduleinstall_getfetchmodulestaskstatus) | 获取模块下载任务状态。 |
| [HMS\_ModuleInstall\_GetFetchModulesTaskId](#hms_moduleinstall_getfetchmodulestaskid) | 获取模块下载任务id。 |
| [HMS\_ModuleInstall\_GetFetchModulesDesc](#hms_moduleinstall_getfetchmodulesdesc) | 获取模块下载描述。 |
| [HMS\_ModuleInstall\_GetFetchModules](#hms_moduleinstall_getfetchmodules) | 获取模块下载模块名。 |
| [HMS\_ModuleInstall\_GetFetchModulesTotalSize](#hms_moduleinstall_getfetchmodulestotalsize) | 获取模块下载总大小。 |
| [HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](#hms_moduleinstall_getfetchmodulesdownloadedsize) | 获取模块下载已下载大小。 |
| [HMS\_ModuleInstall\_CancelTask](#hms_moduleinstall_canceltask) | 取消下载任务。 |
| [HMS\_ModuleInstall\_ShowCellularDataConfirmation](#hms_moduleinstall_showcellulardataconfirmation) | 展示流量弹窗。 |
| [HMS\_ModuleInstall\_CreateStatusCallback](#hms_moduleinstall_createstatuscallback) | 创建下载进度监听回调。 |
| [HMS\_ModuleInstall\_On](#hms_moduleinstall_on) | 下载进度监听。 |
| [HMS\_ModuleInstall\_ReleaseStatusCallback](#hms_moduleinstall_releasestatuscallback) | 释放下载进度监听回调。 |
| [HMS\_ModuleInstall\_Off](#hms_moduleinstall_off) | 取消下载进度监听。 |

#### 类型定义说明

#### \[h2\]ModuleInstall\_InstalledModule

```c
typedef struct ModuleInstall_InstalledModule ModuleInstall_InstalledModule
```

**描述**

安装模块信息。

**起始版本：** 5.0.2(14)

#### \[h2\]ModuleInstall\_FetchModulesResult

```c
typedef struct ModuleInstall_FetchModulesResult ModuleInstall_FetchModulesResult
```

**描述**

安装模块结果。

**起始版本：** 5.0.2(14)

#### \[h2\]ModuleInstall\_StatusCallback

```c
typedef struct ModuleInstall_StatusCallback ModuleInstall_StatusCallback
```

**描述**

模块安装状态回调。

**起始版本：** 5.0.2(14)

#### \[h2\]ModuleInstall\_OnStatusCallback

```c
typedef void (*ModuleInstall_OnStatusCallback)(char *bundleName, char *eventInfo)
```

**描述**

监听回调函数。

**起始版本：** 5.0.2(14)

#### 枚举类型说明

#### \[h2\]ModuleInstall\_ErrCode

```c
enum ModuleInstall_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| :-- | :-- |
| E\_NO\_ERROR = 0 | 成功。 |
| E\_PARAMS = 401 | 无效的参数。 |
| E\_QUERY\_MODULE = 1006500001 | 调用包管理模块接口异常。 |
| E\_REPEATED\_CALL = 1006500002 | 重复调用接口，输入相同。 |
| E\_CONNECT\_SA = 1006500004 | 服务异常。 |
| E\_OFF\_WITHOUT\_ON = 1006500006 | 未与[HMS\_ModuleInstall\_On](#hms_moduleinstall_on)接口共同使用。 |
| E\_CONNECT\_SERVICE\_EXTENSION = 1006500007 | 服务连接失败。 |
| E\_WRITE\_PARAM = 1006500008 | 参数写入异常。 |
| E\_REQUEST\_SERVER = 1006500009 | 请求服务异常。 |
| E\_RESPONSE\_INVALID = 1006500010 | 响应参数无法解析。 |
| E\_INNER\_ERROR = 1006500011 | 内部错误。 |

#### \[h2\]ModuleInstall\_InstallStatus

```c
enum ModuleInstall_InstallStatus
```

**描述**

枚举安装状态。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| :-- | :-- |
| INSTALLED = 0 | 已安装。 |
| NOT\_INSTALLED = 1 | 未安装。 |

#### \[h2\]ModuleInstall\_RequestCode

```c
enum ModuleInstall_RequestCode
```

**描述**

枚举按需下载模块请求码。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| :-- | :-- |
| MODULE\_ALREADY\_EXISTS = -8 | 模块已存在。 |
| MODULE\_UNAVAILABLE = -7 | 要下载的模块不存在或者模块不适配该设备。 |
| INVALID\_REQUEST = -6 | 该请求无效，请求中包含的信息不准确。 |
| NETWORK\_ERROR = -5 | 网络异常，请求失败。 |
| INVOKER\_VERIFICATION\_FAILED = -4 | 调用者信息异常。 |
| FOREGROUND\_REQUIRED = -3 | 仅允许应用在前台时请求按需加载。 |
| ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2 | 请求被拒绝，因为当前至少有一个请求正在下载。 |
| FAILURE = -1 | 失败。 |
| SUCCESS = 0 | 成功。 |
| DOWNLOAD\_WAIT\_WIFI = 1 | 
当前使用的是流量，开发者需要调用

[HMS\_ModuleInstall\_ShowCellularDataConfirmation](#hms_moduleinstall_showcellulardataconfirmation)接口，提醒用户确认是否使用流量下载。

 |

#### \[h2\]ModuleInstall\_TaskStatus

```c
enum ModuleInstall_TaskStatus
```

**描述**

枚举任务状态。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| :-- | :-- |
| CREATE\_TASK\_FAILED = -4 | 创建下载任务失败。 |
| HIGHER\_VERSION\_INSTALLED = -3 | 本地存在相同或者更高版本。 |
| TASK\_ALREADY\_EXISTS = -2 | 下载任务已存在。 |
| TASK\_UNFOUND = -1 | 下载任务不存在。 |
| TASK\_CREATED = 0 | 创建下载任务成功。 |
| DOWNLOADING = 1 | 下载中。 |
| DOWNLOAD\_PAUSED = 2 | 暂停中。 |
| DOWNLOAD\_WAITING = 3 | 等待下载中。 |
| DOWNLOAD\_SUCCESSFUL = 4 | 下载成功。 |
| DOWNLOAD\_FAILED = 5 | 下载失败。 |
| DOWNLOAD\_WAIT\_FOR\_WIFI = 6 | Wi-Fi预约。 |
| INSTALL\_WAITING = 20 | 等待安装。 |
| INSTALLING = 21 | 安装中。 |
| INSTALL\_SUCCESSFUL = 22 | 安装完成。 |
| INSTALL\_FAILED = 23 | 安装失败。 |

#### 函数说明

#### \[h2\]HMS\_ModuleInstall\_GetInstalledModule

```c
ModuleInstall_ErrCode HMS_ModuleInstall_GetInstalledModule(const char *moduleName, unsigned int length,
    ModuleInstall_InstalledModule **installedModule)
```

**描述**

查询模块是否安装。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| char \*moduleName | 模块名。 |
| int length | 模块名长度，最大长度512。 |
| [ModuleInstall\_InstalledModule](#moduleinstall_installedmodule) \*\*installedModule | 模块信息。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_QUERY\_MODULE表示调用包管理模块接口异常。

#### \[h2\]HMS\_ModuleInstall\_GetInstalledModuleName

```c
char *HMS_ModuleInstall_GetInstalledModuleName(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_InstalledModule](#moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

返回模块名。

#### \[h2\]HMS\_ModuleInstall\_GetInstalledModuleType

```c
int HMS_ModuleInstall_GetInstalledModuleType(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块类型。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_InstalledModule](#moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

返回模块类型, 取值参考：[bundleManager.ModuleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#moduletype)。当[ModuleInstall\_InstallStatus](#moduleinstall_installstatus)\=1时，默认返回0。

#### \[h2\]HMS\_ModuleInstall\_GetModuleInstallStatus

```c
ModuleInstall_InstallStatus HMS_ModuleInstall_GetModuleInstallStatus(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块安装状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_InstalledModule](#moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

模块安装状态，取值参考：[ModuleInstall\_InstallStatus](#moduleinstall_installstatus)。

#### \[h2\]HMS\_ModuleInstall\_FetchModules

```c
ModuleInstall_ErrCode HMS_ModuleInstall_FetchModules(const char *bundleName, unsigned int length, char **moduleNames, unsigned int moduleNamesLength, ModuleInstall_FetchModulesResult **fetchModulesResult)
```

**描述**

请求下载模块。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| char \*bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| char \*\*moduleNames | 模块名数组。 |
| int moduleNamesLength | 模块名数组长度，最大长度512。 |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*\*fetchModulesResult | 模块安装结果。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SA表示服务异常；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析；返回E\_INNER\_ERROR表示内部错误。

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesRequestCode

```c
ModuleInstall_RequestCode HMS_ModuleInstall_GetFetchModulesRequestCode(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载请求码。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

按需下载模块请求码，取值参考: [ModuleInstall\_RequestCode](#moduleinstall_requestcode)。

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesTaskStatus

```c
ModuleInstall_TaskStatus HMS_ModuleInstall_GetFetchModulesTaskStatus(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

模块下载任务状态，取值参考：[ModuleInstall\_TaskStatus](#moduleinstall_taskstatus)。

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesTaskId

```c
char *HMS_ModuleInstall_GetFetchModulesTaskId(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务id。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

任务id。

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesDesc

```c
char *HMS_ModuleInstall_GetFetchModulesDesc(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载描述。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载描述。

#### \[h2\]HMS\_ModuleInstall\_GetFetchModules

```c
char* HMS_ModuleInstall_GetFetchModules(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块名。

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesTotalSize

```c
int HMS_ModuleInstall_GetFetchModulesTotalSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载总大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块总大小。

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesDownloadedSize

```c
int HMS_ModuleInstall_GetFetchModulesDownloadedSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载已下载大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_FetchModulesResult](#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

已下载模块大小。

#### \[h2\]HMS\_ModuleInstall\_CancelTask

```c
ModuleInstall_ErrCode HMS_ModuleInstall_CancelTask(const char *taskId, unsigned int length, unsigned int cancelResult)
```

**描述**

取消下载任务。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| char \*taskId | 任务id。 |
| int length | 任务id长度，最大长度512。 |
| int cancelResult | 取消下载结果。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析；

#### \[h2\]HMS\_ModuleInstall\_ShowCellularDataConfirmation

```c
ModuleInstall_ErrCode HMS_ModuleInstall_ShowCellularDataConfirmation(const char *taskId, unsigned int length, unsigned int showResult)
```

**描述**

展示流量弹窗。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| char \*taskId | 任务id。 |
| int length | 任务id长度，最大长度512。 |
| int showResult | 展示流量弹窗结果。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析。

#### \[h2\]HMS\_ModuleInstall\_CreateStatusCallback

```c
ModuleInstall_StatusCallback *HMS_ModuleInstall_CreateStatusCallback(ModuleInstall_OnStatusCallback *onStatusCallback)
```

**描述**

创建下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_OnStatusCallback](#moduleinstall_onstatuscallback) \*onStatusCallback | 下载进度监听回调函数。 |

**返回：**

下载进度监听回调。

#### \[h2\]HMS\_ModuleInstall\_On

```c
ModuleInstall_ErrCode HMS_ModuleInstall_On(const char *bundleName, unsigned int length, unsigned int appIndex, unsigned int period, ModuleInstall_StatusCallback **callback)
```

**描述**

下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| char \*bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| int appIndex | 应用分身索引。 |
| int period | 监听周期。 |
| [ModuleInstall\_StatusCallback](#moduleinstall_statuscallback) \*\*callback | 下载进度监听回调。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_REPEATED\_CALL表示重复调用接口；返回E\_CONNECT\_SA表示服务异常。

#### \[h2\]HMS\_ModuleInstall\_ReleaseStatusCallback

```c
void HMS_ModuleInstall_ReleaseStatusCallback(ModuleInstall_StatusCallback *statusCallback)
```

**描述**

释放下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| [ModuleInstall\_StatusCallback](#moduleinstall_statuscallback) \*statusCallback | 下载进度监听回调。 |

#### \[h2\]HMS\_ModuleInstall\_Off

```c
ModuleInstall_ErrCode HMS_ModuleInstall_Off(const char *bundleName, unsigned int length, unsigned int appIndex)
```

**描述**

取消下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| char \*bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| int appIndex | 应用分身索引。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_OFF\_WITHOUT\_ON表示未与监听接口共同使用；返回E\_CONNECT\_SA表示服务异常。
