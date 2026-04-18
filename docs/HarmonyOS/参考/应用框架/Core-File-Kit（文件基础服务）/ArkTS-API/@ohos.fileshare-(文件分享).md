---
title: "@ohos.fileshare (文件分享)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileshare"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "ArkTS API"
  - "@ohos.fileshare (文件分享)"
captured_at: "2026-04-17T01:48:14.019Z"
---

# @ohos.fileshare (文件分享)

该模块提供文件分享能力，提供系统应用将公共目录文件统一资源标识符（Uniform Resource Identifier，URI）以读写权限授权给其他应用的接口，授权后应用可通过[@ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)的相关接口进行相关open、read、write等操作，实现文件分享。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/XX4O-Ze4QHK0ua6T1H1iHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=3D694FEC2A38B04D4E63EE6CB3E0A7737793780A9E7B6F5FB913E916604BCCB0)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { fileShare } from '@kit.CoreFileKit';
```

#### OperationMode11+

枚举，授予或使能权限的URI访问模式。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| READ\_MODE | 0b1 | 读权限。 |
| WRITE\_MODE | 0b10 | 写权限。 |
| CREATE\_MODE20+ | 0b100 | 创建文件/文件夹权限。 |
| DELETE\_MODE20+ | 0b1000 | 删除文件/文件夹权限。 |
| RENAME\_MODE20+ | 0b10000 | 重命名文件/文件夹权限。 |

#### PolicyErrorCode11+

枚举，授予或使能权限策略失败的URI对应的错误码。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PERSISTENCE\_FORBIDDEN | 1 | URI禁止被持久化。 |
| INVALID\_MODE | 2 | 无效的模式。 |
| INVALID\_PATH | 3 | 无效的路径。 |
| PERMISSION\_NOT\_PERSISTED12+ | 4 | 权限没有被持久化。 |

#### PolicyErrorResult11+

授予或使能权限失败的URI策略结果。支持persistPermission、revokePermission、activatePermission、deactivatePermission接口抛出错误时使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/CjgAXg3eThaMBHXEEsfwLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=BCA714699D8D1584D0A676B961CFCB6DE1AB2DEC34F53A317516B73FA3890B4A)

从API version 23开始，PolicyErrorResult由type变更为interface类型。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | 否 | 否 | 授予或使能权限失败的URI。 |
| code | [PolicyErrorCode](#policyerrorcode11) | 否 | 否 | 授权策略失败的URI对应的错误码。 |
| message | string | 否 | 否 | 授权策略失败的URI对应的原因。 |

#### PolicyInfo11+

需要授予或使能权限URI的策略信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | 否 | 否 | 需要授予或使能权限的URI。 |
| operationMode | number | 否 | 否 | 授予或使能权限的URI访问模式，参考[OperationMode](#operationmode11)，如需授予多个权限，可以组合使用，例如使用READ\_MODE | WRITE\_MODE授予读写权限。 |

#### PathPolicyInfo15+

需要查询的文件或目录的信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| path | string | 否 | 否 | 需要查询的path。 |
| operationMode | OperationMode | 否 | 否 | 需要查询的path的访问模式，参考[OperationMode](#operationmode11)。 |

#### PolicyType15+

枚举，所查询策略信息对应的授权模式。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| TEMPORARY\_TYPE | 0 | 临时授权。 |
| PERSISTENT\_TYPE | 1 | 持久化授权。 |

#### fileShare.persistPermission11+

persistPermission(policies: Array<PolicyInfo>): Promise<void>

异步方法对所选择的多个文件或目录URI持久化授权，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/NqSYgZFiSgiZy_2Y2usfKg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=B19A935ACF630A0DB08C3ACEF994A71B6624FFB62423F534FFE861F025D48352)

从API version 22开始，支持媒体类URI的持久化。

可以组合授予多个权限。只能对已获取到的临时权限进行持久化授权，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

如果存在URI授权失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](#policyerrorresult11)\>形式提供错误信息。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function persistPermissionExample() {
  try {
    let DocumentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(DocumentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris[0],
      // 可以组合授予多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.persistPermission(policies).then(() => {
      console.info("persistPermission successfully");
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("persistPermission failed with error message: " + err.message + ", error code: " + err.code);
      if (err.code == 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error("error code : " + JSON.stringify(err.data[i].code));
          console.error("error uri : " + JSON.stringify(err.data[i].uri));
          console.error("error reason : " + JSON.stringify(err.data[i].message));
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('persistPermission failed with err: ' + JSON.stringify(err));
  }
}
```

#### fileShare.revokePermission11+

revokePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法对所选择的多个文件或目录uri取消持久化授权，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/MVjFgSFORdC0KHpH83xzgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=E008B8005EA580A125FFD3D71136832DD3A6AF79C25A8722BBD7C278EAA334D1)

从API version 22开始，支持媒体类URI的持久化。

可以组合取消多个权限。只能对已持久化的权限进行取消持久化，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

如果存在URI取消授权失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](#policyerrorresult11)\>形式提供错误信息。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function revokePermissionExample() {
  try {
    let DocumentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(DocumentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris[0],
      // 可以组合取消多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.revokePermission(policies).then(() => {
      console.info("revokePermission successfully");
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("revokePermission failed with error message: " + err.message + ", error code: " + err.code);
        if (err.code == 13900001 && err.data) {
          for (let i = 0; i < err.data.length; i++) {
            console.error("error code : " + JSON.stringify(err.data[i].code));
            console.error("error uri : " + JSON.stringify(err.data[i].uri));
            console.error("error reason : " + JSON.stringify(err.data[i].message));
          }
        }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('revokePermission failed with err: ' + JSON.stringify(err));
  }
}
```

#### fileShare.activatePermission11+

activatePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法使能多个已经永久授权过的文件或目录，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/WmiaUNwgRqCGAJh77FjQEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A94E2E7D2762C0B661AD773A8DE228D30E222C4315797D17DB0D4E4E7A388366)

从API version 22开始，支持媒体类URI的持久化。

可以组合使能多个权限。只能对已持久化的权限进行使能，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

如果存在URI使能权限失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](#policyerrorresult11)\>形式提供错误信息。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function activatePermissionExample() {
  try {
    let uri = "file://docs/storage/Users/username/tmp.txt";
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      // 可以组合使能多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.activatePermission(policies).then(() => {
      console.info("activatePermission successfully");
    }).catch(async (err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("activatePermission failed with error message: " + err.message + ", error code: " + err.code);
        if (err.code == 13900001 && err.data) {
          for (let i = 0; i < err.data.length; i++) {
            console.error("error code : " + JSON.stringify(err.data[i].code));
            console.error("error uri : " + JSON.stringify(err.data[i].uri));
            console.error("error reason : " + JSON.stringify(err.data[i].message));
            if(err.data[i].code == fileShare.PolicyErrorCode.PERMISSION_NOT_PERSISTED){
              await fileShare.persistPermission(policies);
            }
          }
        }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('activatePermission failed with err: ' + JSON.stringify(err));
  }
}
```

#### fileShare.deactivatePermission11+

deactivatePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法取消使能授权过的多个文件或目录，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/LRKpYT7jRiCMVeUq2xo8Qw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=A6694CAB01A91018684E8125F5A8891B0B36A4EAD984F567E0BF2EA98AD0F728)

从API version 22开始，支持媒体类URI的持久化。

可以组合取消使能多个权限。只能对已持久化的权限进行取消使能，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

如果存在URI取消使能权限失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](#policyerrorresult11)\>形式提供错误信息。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function deactivatePermissionExample() {
  try {
    let uri = "file://docs/storage/Users/username/tmp.txt";
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      // 可以组合取消使能多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.deactivatePermission(policies).then(() => {
      console.info("deactivatePermission successfully");
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("deactivatePermission failed with error message: " + err.message + ", error code: " + err.code);
        if (err.code == 13900001 && err.data) {
          for (let i = 0; i < err.data.length; i++) {
            console.error("error code : " + JSON.stringify(err.data[i].code));
            console.error("error uri : " + JSON.stringify(err.data[i].uri));
            console.error("error reason : " + JSON.stringify(err.data[i].message));
          }
        }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('deactivatePermission failed with err: ' + JSON.stringify(err));
  }
}
```

#### fileShare.checkPersistentPermission12+

checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>

异步方法校验所选择的多个文件或目录URI持久化授权，使用Promise异步回调。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<boolean>> | Promise对象。返回true表示有持久化授权；false表示不具有持久化授权。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function checkPersistentPermissionExample() {
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(documentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris[0],
      // 可以组合校验多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.checkPersistentPermission(policies).then(async (data) => {
      let result: Array<boolean> = data;
      for (let i = 0; i < result.length; i++) {
        console.info("checkPersistentPermission result: " + JSON.stringify(result[i]));
        if(!result[i]){
          let info: fileShare.PolicyInfo = {
            uri: policies[i].uri,
            operationMode: policies[i].operationMode,
          };
          let policy : Array<fileShare.PolicyInfo> = [info];
          await fileShare.persistPermission(policy);
        }
      }
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("checkPersistentPermission failed with error message: " + err.message + ", error code: " + err.code);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('checkPersistentPermission failed with err: ' + JSON.stringify(err));
  }
}
```
