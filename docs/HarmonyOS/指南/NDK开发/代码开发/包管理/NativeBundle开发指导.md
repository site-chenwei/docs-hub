---
title: "NativeBundle开发指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-bundle-guidelines"
menu_path:
  - "指南"
  - "NDK开发"
  - "代码开发"
  - "包管理"
  - "NativeBundle开发指导"
captured_at: "2026-04-17T01:36:41.959Z"
---

# NativeBundle开发指导

#### 场景介绍

开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native Bundle接口获取应用自身相关信息。

#### 接口说明

常用接口如下表所示，具体API说明详见[Native\_Bundle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)。

| 接口名 | 描述 |
| :-- | :-- |
| [OH\_NativeBundle\_GetCurrentApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getcurrentapplicationinfo) | 获取应用自身相关信息。 |
| [OH\_NativeBundle\_GetAppId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getappid) | 获取自身应用的appId信息。 |
| [OH\_NativeBundle\_GetAppIdentifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getappidentifier) | 获取自身应用的appIdentifier信息。 |
| [OH\_NativeBundle\_GetMainElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getmainelementname) | 获取自身应用入口的信息。 |
| [OH\_NativeBundle\_GetCompatibleDeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getcompatibledevicetype) | 获取自身应用适用的设备类型。 |
| [OH\_NativeBundle\_IsDebugMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_isdebugmode) | 查询当前应用的调试模式。从API version 20开始支持。 |
| [OH\_NativeBundle\_GetModuleMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getmodulemetadata) | 获取当前应用的元数据信息。从API version 20开始支持。 |
| [OH\_NativeBundle\_GetAbilityResourceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getabilityresourceinfo) | 获取支持打开特定文件类型的组件资源信息列表。从API version 21开始支持。 |

#### 开发步骤

**1\. 创建工程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/piWitY-qT0S1xt1095EVbQ/zh-cn_image_0000002538020334.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=8DDA3228A903929CC8C2A3D6FB927EA29AA4E5B96A5C5B21CF0560D39FE0EE49)

**2\. 添加依赖**

创建完成后，DevEco Studio会在工程生成cpp目录，目录中包含types/libentry/index.d.ts、napi\_init.cpp、CMakeLists.txt等文件。

1.  打开src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加包管理的libbundle\_ndk.so。
    
    ```
    target_link_libraries(entry PUBLIC libace_napi.z.so libbundle_ndk.so)
    ```
    
2.  打开src/main/cpp/napi\_init.cpp文件，添加头文件。
    
    // napi依赖头文件
    #include "napi/native\_api.h"
    // native接口依赖头文件
    #include "bundle/ability\_resource\_info.h"
    #include "bundle/native\_interface\_bundle.h"
    // free()函数依赖的基础库
    #include <cstdlib>
    

**3\. 修改源文件**

1.  打开src/main/cpp/napi\_init.cpp文件，文件Init会对当前方法进行初始化映射，这里定义对外的接口。
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr },
            // 新增方法getCurrentApplicationInfo
            { "getCurrentApplicationInfo", nullptr, GetCurrentApplicationInfo, nullptr,
                nullptr, nullptr, napi\_default, nullptr},
            // 新增方法getAppId
            { "getAppId", nullptr, GetAppId, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // 新增方法getAppIdentifier
            { "getAppIdentifier", nullptr, GetAppIdentifier, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // 新增方法getMainElementName
            { "getMainElementName", nullptr, GetMainElementName, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // 新增方法getCompatibleDeviceType
            { "getCompatibleDeviceType", nullptr, GetCompatibleDeviceType, nullptr,
                nullptr, nullptr, napi\_default, nullptr},
            // 新增方法isDebugMode
            { "isDebugMode", nullptr, IsDebugMode, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // 新增方法getModuleMetadata
            { "getModuleMetadata", nullptr, GetModuleMetadata, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // 新增方法getAbilityResourceInfo
            { "getAbilityResourceInfo", nullptr, GetAbilityResourceInfo, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
2.  在src/main/cpp/napi\_init.cpp文件中获取Native的包信息对象，并转为js的包信息对象，即可在js侧获取应用的信息：
    
    static napi\_value GetCurrentApplicationInfo(napi\_env env, napi\_callback\_info info)
    {
        // 调用Native接口获取应用信息
        OH\_NativeBundle\_ApplicationInfo nativeApplicationInfo = OH\_NativeBundle\_GetCurrentApplicationInfo();
        napi\_value result = nullptr;
        napi\_create\_object(env, &result);
        // Native接口获取的应用包名转为js对象里的bundleName属性
        napi\_value bundleName;
        napi\_create\_string\_utf8(env, nativeApplicationInfo.bundleName, NAPI\_AUTO\_LENGTH, &bundleName);
        napi\_set\_named\_property(env, result, "bundleName", bundleName);
        // Native接口获取的指纹信息转为js对象里的fingerprint属性
        napi\_value fingerprint;
        napi\_create\_string\_utf8(env, nativeApplicationInfo.fingerprint, NAPI\_AUTO\_LENGTH, &fingerprint);
        napi\_set\_named\_property(env, result, "fingerprint", fingerprint);
        // 最后为了防止内存泄漏，手动释放
        free(nativeApplicationInfo.bundleName);
        free(nativeApplicationInfo.fingerprint);
        return result;
    }
    
    static napi\_value GetAppId(napi\_env env, napi\_callback\_info info)
    {
        // 调用Native接口获取应用appId
        char\* appId = OH\_NativeBundle\_GetAppId();
        // Native接口转成nAppId返回
        napi\_value nAppId;
        napi\_create\_string\_utf8(env, appId, NAPI\_AUTO\_LENGTH, &nAppId);
        // 最后为了防止内存泄漏，手动释放
        free(appId);
        return nAppId;
    }
    
    static napi\_value GetAppIdentifier(napi\_env env, napi\_callback\_info info)
    {
        // 调用Native接口获取应用appIdentifier
        char\* appIdentifier = OH\_NativeBundle\_GetAppIdentifier();
        // Native接口转成nAppIdentifier返回
        napi\_value nAppIdentifier;
        napi\_create\_string\_utf8(env, appIdentifier, NAPI\_AUTO\_LENGTH, &nAppIdentifier);
        // 最后为了防止内存泄漏，手动释放
        free(appIdentifier);
        return nAppIdentifier;
    }
    
    static napi\_value GetMainElementName(napi\_env env, napi\_callback\_info info)
    {
        // 调用Native接口获取应用入口的信息
        OH\_NativeBundle\_ElementName elementName = OH\_NativeBundle\_GetMainElementName();
        napi\_value result = nullptr;
        napi\_create\_object(env, &result);
        // Native接口获取的应用包名转为js对象里的bundleName属性
        napi\_value bundleName;
        napi\_create\_string\_utf8(env, elementName.bundleName, NAPI\_AUTO\_LENGTH, &bundleName);
        napi\_set\_named\_property(env, result, "bundleName", bundleName);
        // Native接口获取的模块名称转为js对象里的moduleName属性
        napi\_value moduleName;
        napi\_create\_string\_utf8(env, elementName.moduleName, NAPI\_AUTO\_LENGTH, &moduleName);
        napi\_set\_named\_property(env, result, "moduleName", moduleName);
        // Native接口获取的ability名称转为js对象里的abilityName属性
        napi\_value abilityName;
        napi\_create\_string\_utf8(env, elementName.abilityName, NAPI\_AUTO\_LENGTH, &abilityName);
        napi\_set\_named\_property(env, result, "abilityName", abilityName);
        // 最后为了防止内存泄漏，手动释放
        free(elementName.bundleName);
        free(elementName.moduleName);
        free(elementName.abilityName);
        return result;
    }
    
    static napi\_value GetCompatibleDeviceType(napi\_env env, napi\_callback\_info info)
    {
        // 调用Native接口获取应用deviceType
        char\* deviceType = OH\_NativeBundle\_GetCompatibleDeviceType();
        // Native接口转成nDeviceType返回
        napi\_value nDeviceType;
        napi\_create\_string\_utf8(env, deviceType, NAPI\_AUTO\_LENGTH, &nDeviceType);
        // 最后为了防止内存泄漏，手动释放
        free(deviceType);
        return nDeviceType;
    }
    
    static napi\_value IsDebugMode(napi\_env env, napi\_callback\_info info)
    {
        bool isDebug = false;
        // 调用Native接口获取应用DebugMode的信息，该接口从API version 20开始支持
        bool isSuccess = OH\_NativeBundle\_IsDebugMode(&isDebug);
        // 调用Native接口失败抛出异常
        if (isSuccess == false) {
            napi\_throw\_error(env, nullptr, "call failed");
            return nullptr;
        }
        // Native接口转成debug返回
        napi\_value debug;
        napi\_get\_boolean(env, isDebug, &debug);
        return debug;
    }
    
    static napi\_value GetModuleMetadata(napi\_env env, napi\_callback\_info info)
    {
        size\_t moduleCount = 0;
        // 调用Native接口获取应用元数据的信息，该接口从API version 20开始支持
        OH\_NativeBundle\_ModuleMetadata\* modules = OH\_NativeBundle\_GetModuleMetadata(&moduleCount);
        if (modules == nullptr || moduleCount == 0) {
            napi\_throw\_error(env, nullptr, "no metadata found");
            return nullptr;
        }
        napi\_value result;
        napi\_create\_array(env, &result);
        for (size\_t i = 0; i < moduleCount; i++) {
            napi\_value moduleObj;
            napi\_create\_object(env, &moduleObj);
            // Native接口获取的模块名转为js对象里的moduleName属性
            napi\_value moduleName;
            napi\_create\_string\_utf8(env, modules\[i\].moduleName, NAPI\_AUTO\_LENGTH, &moduleName);
            napi\_set\_named\_property(env, moduleObj, "moduleName", moduleName);
            napi\_value metadataArray;
            napi\_create\_array(env, &metadataArray);
            for (size\_t j = 0; j < modules\[i\].metadataArraySize; j++) {
                napi\_value metadataObj;
                napi\_create\_object(env, &metadataObj);
                napi\_value name;
                napi\_value value;
                napi\_value resource;
                napi\_create\_string\_utf8(env, modules\[i\].metadataArray\[j\].name, NAPI\_AUTO\_LENGTH, &name);
                napi\_create\_string\_utf8(env, modules\[i\].metadataArray\[j\].value, NAPI\_AUTO\_LENGTH, &value);
                napi\_create\_string\_utf8(env, modules\[i\].metadataArray\[j\].resource, NAPI\_AUTO\_LENGTH, &resource);
                // Native接口获取的元数据名称转为js对象里的name属性
                napi\_set\_named\_property(env, metadataObj, "name", name);
                // Native接口获取的元数据值名称转为js对象里的value属性
                napi\_set\_named\_property(env, metadataObj, "value", value);
                // Native接口获取的元数据资源转为js对象里的resource属性
                napi\_set\_named\_property(env, metadataObj, "resource", resource);
                napi\_set\_element(env, metadataArray, j, metadataObj);
            }
            napi\_set\_named\_property(env, moduleObj, "metadata", metadataArray);
            napi\_set\_element(env, result, i, moduleObj);
        }
        // 最后为了防止内存泄漏，手动释放
        for (size\_t i = 0; i < moduleCount; i++) {
            free(modules\[i\].moduleName);
            for (size\_t j = 0; j < modules\[i\].metadataArraySize; j++) {
                free(modules\[i\].metadataArray\[j\].name);
                free(modules\[i\].metadataArray\[j\].value);
                free(modules\[i\].metadataArray\[j\].resource);
            }
            free(modules\[i\].metadataArray);
        }
        free(modules);
        return result;
    }
    
    static void AddDefaultApp(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        bool isDefaultApp = true;
        // 该接口从API version 21开始支持
        OH\_NativeBundle\_CheckDefaultApp(temp, &isDefaultApp);
        napi\_value defaultAppValue;
        napi\_get\_boolean(env, isDefaultApp, &defaultAppValue);
        napi\_set\_named\_property(env, infoObj, "isDefaultApp", defaultAppValue);
    }
    
    static void AddAppIndex(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        int appIndex = -1;
        // 该接口从API version 21开始支持
        OH\_NativeBundle\_GetAppIndex(temp, &appIndex);
        napi\_value appIndexValue;
        napi\_create\_int32(env, appIndex, &appIndexValue);
        napi\_set\_named\_property(env, infoObj, "appIndex", appIndexValue);
    }
    
    static void AddLabel(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*label = nullptr;
        // 该接口从API version 21开始支持
        OH\_NativeBundle\_GetLabel(temp, &label);
        napi\_value labelValue;
        if (label) {
            napi\_create\_string\_utf8(env, label, NAPI\_AUTO\_LENGTH, &labelValue);
            free(label);
        } else {
            napi\_get\_null(env, &labelValue);
        }
        napi\_set\_named\_property(env, infoObj, "label", labelValue);
    }
    
    static void AddBundleName(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*bundleName = nullptr;
        // 该接口从API version 21开始支持
        OH\_NativeBundle\_GetBundleName(temp, &bundleName);
        napi\_value bundleNameValue;
        if (bundleName) {
            napi\_create\_string\_utf8(env, bundleName, NAPI\_AUTO\_LENGTH, &bundleNameValue);
            free(bundleName);
        } else {
            napi\_get\_null(env, &bundleNameValue);
        }
        napi\_set\_named\_property(env, infoObj, "bundleName", bundleNameValue);
    }
    
    static void AddModuleName(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*moduleName = nullptr;
        // 该接口从API version 21开始支持
        OH\_NativeBundle\_GetModuleName(temp, &moduleName);
        napi\_value moduleNameValue;
        if (moduleName) {
            napi\_create\_string\_utf8(env, moduleName, NAPI\_AUTO\_LENGTH, &moduleNameValue);
            free(moduleName);
        } else {
            napi\_get\_null(env, &moduleNameValue);
        }
        napi\_set\_named\_property(env, infoObj, "moduleName", moduleNameValue);
    }
    
    static void AddAbilityName(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*abilityName = nullptr;
        // 该接口从API version 21开始支持
        OH\_NativeBundle\_GetAbilityName(temp, &abilityName);
        napi\_value abilityNameValue;
        if (abilityName) {
            napi\_create\_string\_utf8(env, abilityName, NAPI\_AUTO\_LENGTH, &abilityNameValue);
            free(abilityName);
        } else {
            napi\_get\_null(env, &abilityNameValue);
        }
        napi\_set\_named\_property(env, infoObj, "abilityName", abilityNameValue);
    }
    
    static void GetDrawableDescriptor(
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        ArkUI\_DrawableDescriptor \*rawDrawable = nullptr;
        // 该接口从API version 21开始支持
        OH\_NativeBundle\_GetDrawableDescriptor(temp, &rawDrawable);
        if (rawDrawable) {
            // 使用ArkUI\_DrawableDescriptor对象绘制图标
        }
    }
    
    static void AssemblyAbilityResourceInfo(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        // 1. 添加Default App
        AddDefaultApp(env, infoObj, temp);
        // 2. 添加App Index
        AddAppIndex(env, infoObj, temp);
        // 3. 添加Label
        AddLabel(env, infoObj, temp);
        // 4. 添加Bundle Name
        AddBundleName(env, infoObj, temp);
        // 5. 添加Module Name
        AddModuleName(env, infoObj, temp);
        // 6. 添加Ability Name
        AddAbilityName(env, infoObj, temp);
        // 7. 获取ArkUI\_DrawableDescriptor对象
        GetDrawableDescriptor(temp);
    }
    
    static napi\_value GetAbilityResourceInfo(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\];
        napi\_status status;
        // 获取传入的参数
        status = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        if (status != napi\_ok || argc < 1) {
            napi\_throw\_error(env, nullptr, "Invalid arguments. Expected fileType string.");
            return nullptr;
        }
        // 检查参数类型是否为字符串
        napi\_valuetype valuetype;
        status = napi\_typeof(env, args\[0\], &valuetype);
        if (status != napi\_ok || valuetype != napi\_string) {
            napi\_throw\_error(env, nullptr, "Argument must be a string");
            return nullptr;
        }
        // 获取字符串参数
        char fileType\[256\] = {0}; // 假设文件类型不会超过255个字符
        size\_t strLen;
        status = napi\_get\_value\_string\_utf8(env, args\[0\], fileType, sizeof(fileType) - 1, &strLen);
        if (status != napi\_ok) {
            napi\_throw\_error(env, nullptr, "Failed to get fileType string");
            return nullptr;
        }
        size\_t infosCount = 0;
        OH\_NativeBundle\_AbilityResourceInfo \*infos = nullptr;
        // 调用Native接口获取组件资源信息，使用传入的fileType，该接口从API version 21开始支持
        BundleManager\_ErrorCode ret = OH\_NativeBundle\_GetAbilityResourceInfo(fileType, &infos, &infosCount);
        if (ret == BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED) {
            napi\_throw\_error(env, nullptr, "BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED");
            return nullptr;
        }
        if (infos == nullptr || infosCount == 0) {
            napi\_throw\_error(env, nullptr, "no metadata found");
            return nullptr;
        }
        napi\_value result;
        napi\_create\_array(env, &result);
        for (size\_t i = 0; i < infosCount; i++) {
            auto temp = (OH\_NativeBundle\_AbilityResourceInfo \*)((char \*)infos + OH\_NativeBundle\_GetSize() \* i);
            napi\_value infoObj;
            napi\_create\_object(env, &infoObj);
            AssemblyAbilityResourceInfo(env, infoObj, temp);
            napi\_set\_element(env, result, i, infoObj);
        }
        // 释放内存，该接口从API version 21开始支持
        OH\_AbilityResourceInfo\_Destroy(infos, infosCount);
        return result;
    }
    

**4\. 接口暴露**

1.  在src/main/cpp/types/libentry/Index.d.ts文件中，声明暴露接口。
    
    export const add: (a: number, b: number) => number;
    export const getCurrentApplicationInfo: () => object;   // 新增暴露方法 getCurrentApplicationInfo
    export const getAppId: () => string;                    // 新增暴露方法 getAppId
    export const getAppIdentifier: () => string;            // 新增暴露方法 getAppIdentifier
    export const getMainElementName: () => object;          // 新增暴露方法 getMainElementName
    export const getCompatibleDeviceType: () => string;     // 新增暴露方法 getCompatibleDeviceType
    export const isDebugMode: () => boolean;                // 新增暴露方法 isDebugMode
    export const getModuleMetadata: () => object;           // 新增暴露方法 getModuleMetadata
    export const getAbilityResourceInfo: (fileType: string) => object;      // 新增暴露方法 getAbilityResourceInfo
    

**5\. js侧调用**

1.  打开src/main/ets/pages/Index.ets，导入"libentry.so"，调用Native接口打印出获取的信息内容。示例如下：
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import testNapi from 'libentry.so';
    
    const DOMAIN = 0x0000;
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize($r('app.float.page\_text\_font\_size'))
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                this.message = 'Welcome';
                hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
                let appInfo = testNapi.getCurrentApplicationInfo();
                console.info("bundleNative getCurrentApplicationInfo success, data is " + JSON.stringify(appInfo));
                let appId = testNapi.getAppId();
                console.info("bundleNative getAppId success, appId is " + appId);
                let appIdentifier = testNapi.getAppIdentifier();
                console.info("bundleNative getAppIdentifier success, appIdentifier is " + appIdentifier);
                let mainElement = testNapi.getMainElementName();
                console.info("bundleNative getMainElementName success, data is " + JSON.stringify(mainElement));
                let deviceType = testNapi.getCompatibleDeviceType();
                console.info("bundleNative getCompatibleDeviceType success, deviceType is " + deviceType);
                let isDebugMode = testNapi.isDebugMode();
                console.info("bundleNative isDebugMode success, isDebugMode is " + isDebugMode);
                let moduleMetadata = testNapi.getModuleMetadata();
                console.info("bundleNative getModuleMetadata success, data is " + JSON.stringify(moduleMetadata));
                let fileType: string = '.png';
                let abilityResourceInfo = testNapi.getAbilityResourceInfo(fileType);
                console.info("bundleNative getAbilityResourceInfo success, data is " + JSON.stringify(abilityResourceInfo));
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

关于包管理NDK接口说明，可参考[Native\_Bundle模块介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)。
