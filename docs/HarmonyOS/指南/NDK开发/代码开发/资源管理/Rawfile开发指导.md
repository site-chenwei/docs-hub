---
title: "Rawfile开发指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rawfile-guidelines"
menu_path:
  - "指南"
  - "NDK开发"
  - "代码开发"
  - "资源管理"
  - "Rawfile开发指导"
captured_at: "2026-04-17T01:36:41.862Z"
---

# Rawfile开发指导

#### 场景介绍

开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native Rawfile接口操作Rawfile目录和文件。功能包括文件列表遍历、文件打开、搜索、读取和关闭Rawfile。

64后缀相关接口属于新增接口，新接口支持打开更大的rawfile文件(超过2G建议使用)，具体请参考：[Rawfile接口介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile)。64相关的开发步骤和非64一致，将非64接口替换为64接口即可，例如：OH\_ResourceManager\_OpenRawFile替换为OH\_ResourceManager\_OpenRawFile64。

#### 接口说明

| 接口名 | 描述 |
| :-- | :-- |
| NativeResourceManager \*OH\_ResourceManager\_InitNativeResourceManager(napi\_env env, napi\_value jsResMgr) | 初始化native resource manager。 |
| RawDir \*OH\_ResourceManager\_OpenRawDir(const NativeResourceManager \*mgr, const char \*dirName) | 打开指定rawfile目录。 |
| int OH\_ResourceManager\_GetRawFileCount(RawDir \*rawDir) | 获取指定rawfile目录下的rawfile文件数量。 |
| const char \*OH\_ResourceManager\_GetRawFileName(RawDir \*rawDir, int index) | 获取rawfile名字。 |
| RawFile \*OH\_ResourceManager\_OpenRawFile(const NativeResourceManager \*mgr, const char \*fileName) | 打开指定rawfile文件。 |
| long OH\_ResourceManager\_GetRawFileSize(RawFile \*rawFile) | 获取rawfile文件大小。 |
| int OH\_ResourceManager\_ReadRawFile(const RawFile \*rawFile, void \*buf, size\_t length) | 读取rawfile文件内容。 |
| void OH\_ResourceManager\_CloseRawFile(RawFile \*rawFile) | 释放rawfile文件相关资源。 |
| void OH\_ResourceManager\_CloseRawDir(RawDir \*rawDir) | 释放rawfile目录相关资源。 |
| bool OH\_ResourceManager\_GetRawFileDescriptor(const RawFile \*rawFile, RawFileDescriptor &descriptor) | 获取rawfile的fd。 |
| void OH\_ResourceManager\_ReleaseNativeResourceManager(NativeResourceManager \*resMgr) | 释放native resource manager相关资源。 |
| bool OH\_ResourceManager\_IsRawDir(const NativeResourceManager \*mgr, const char \*path) | 判断路径是否是rawfile下的目录。 |

详细的接口说明请参考[rawfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile)。

#### 开发步骤

以ArkTS侧获取rawfile文件列表、获取rawfile文件内容、获取rawfile描述符（fd, offset, length）、判断是否是rawfile下的目录四种调用方式为例。

**1\. 创建工程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/bTVZizGaRPCknO11a0XYyg/zh-cn_image_0000002538020334.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=59836A7825C7CEA57E171462132DE529BD374EDFAF1DDBA9097BBABF4D22B97D)

**2\. 添加依赖**

创建完成后，DevEco Studio会在工程中生成cpp目录，目录下有libentry/index.d.ts、hello.cpp、CMakeLists.txt等文件。

1.  打开src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加rawfile依赖librawfile.z.so以及日志依赖libhilog\_ndk.z.so。
    
    ```
    target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so librawfile.z.so)
    ```
    
2.  打开src/main/cpp/types/libentry/index.d.ts文件，在此文件中声明ArkTS侧接口getFileList、getRawFileContent、getRawFileDescriptor、isRawDir。
    
    import { resourceManager } from '@kit.LocalizationKit';
    export const getFileList: (resMgr: resourceManager.ResourceManager, path: string) => Array<String>;
    export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
    export const getRawFileDescriptor: (resMgr: resourceManager.ResourceManager, path: string) => resourceManager.RawFileDescriptor;
    export const isRawDir: (resMgr: resourceManager.ResourceManager, path: string) => boolean;
    

**3\. 修改源文件**

1.  打开src/main/cpp/hello.cpp文件，在Init方法中添加ArkTS接口与C++接口的映射。ArkTS侧接口getFileList、getRawFileContent、getRawFileDescriptor、isRawDir，映射C++接口分别为GetFileList、GetRawFileContent、GetRawFileDescriptor、IsRawDir。
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "getFileList", nullptr, GetFileList, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "getRawFileContent", nullptr, GetRawFileContent, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "getRawFileDescriptor", nullptr, GetRawFileDescriptor, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "isRawDir", nullptr, IsRawDir, nullptr, nullptr, nullptr, napi\_default, nullptr }
        };
    
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
2.  在src/main/cpp/目录下创建hello.h文件，在hello.h文件中增加对应的四个方法，如下所示：
    
    #ifndef RAWFILE\_HELLO\_H
    #define RAWFILE\_HELLO\_H
    
    #include <js\_native\_api.h>
    #include <js\_native\_api\_types.h>
    #include <string>
    #include <vector>
    #include <cstdlib>
    #include "napi/native\_api.h"
    
    napi\_value GetFileList(napi\_env env, napi\_callback\_info info);
    napi\_value GetRawFileContent(napi\_env env, napi\_callback\_info info);
    napi\_value GetRawFileDescriptor(napi\_env env, napi\_callback\_info info);
    napi\_value IsRawDir(napi\_env env, napi\_callback\_info info);
    
    #endif // RAWFILE\_HELLO\_H
    
3.  在hello.cpp文件中实现上述四个方法。通过env和info获取Js的资源管理对象，并转换为Native的资源管理对象，即可调用Native资源管理对象的接口，示例代码如下：
    
    导入头文件
    
    #include "hello.h"
    #include "rawfile/raw\_file\_manager.h"
    #include "rawfile/raw\_file.h"
    #include "rawfile/raw\_dir.h"
    #include "hilog/log.h"
    
    声明hilog日志打印的DOMAIN和TAG常量
    
    const int GLOBAL\_RESMGR = 0xFF00;
    const char \*TAG = "\[Sample\_rawfile\]";
    
    示例：
    
    // 示例一：获取rawfile文件列表 GetFileList
    napi\_value GetFileList(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "NDKTest GetFileList Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // 获取参数信息
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\]即为函数第一个参数Js资源对象，OH\_ResourceManager\_InitNativeResourceManager转为Native对象
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
    
        // 获取函数argv\[1\]，此为rawfile相对路径
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string dirName(strBuf, strSize);
    
        // 获取对应的rawDir指针对象
        RawDir\* rawDir = OH\_ResourceManager\_OpenRawDir(mNativeResMgr, dirName.c\_str());
    
        // 获取rawDir下文件及文件夹数量
        int count = OH\_ResourceManager\_GetRawFileCount(rawDir);
    
        // 遍历获取文件名称，并保存
        std::vector<std::string> tempArray;
        for (int i = 0; i < count; i++) {
            std::string filename = OH\_ResourceManager\_GetRawFileName(rawDir, i);
            tempArray.emplace\_back(filename);
        }
    
        // 转为js数组
        napi\_value fileList;
        napi\_create\_array(env, &fileList);
        for (size\_t i = 0; i < tempArray.size(); i++) {
            napi\_value jsString;
            napi\_create\_string\_utf8(env, tempArray\[i\].c\_str(), NAPI\_AUTO\_LENGTH, &jsString);
            napi\_set\_element(env, fileList, i, jsString);
        }
    
        // 关闭打开的指针对象
        OH\_ResourceManager\_CloseRawDir(rawDir);
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        return fileList;
    }
    
    // 示例二：获取rawfile文件内容 GetRawFileContent
    napi\_value CreateJsArrayValue(napi\_env env, std::unique\_ptr<uint8\_t\[\]> &data, long length)
    {
        // 创建js外部ArrayBuffer
        napi\_value buffer;
        napi\_status status = napi\_create\_external\_arraybuffer(env, data.get(), length,
            \[\](napi\_env env, void \*data, void \*hint) {
                delete\[\] static\_cast<char\*>(data);
            }, nullptr, &buffer);
        // 检测ArrayBuffer是否创建成功
        if (status != napi\_ok) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "Failed to create external array buffer");
            return nullptr;
        }
        // 创建js TypedArray  将ArrayBuffer绑定到TypedArray
        napi\_value result = nullptr;
        status = napi\_create\_typedarray(env, napi\_uint8\_array, length, buffer, 0, &result);
        if (status != napi\_ok) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "Failed to create media typed array");
            return nullptr;
        }
        data.release();
        return result;
    }
    
    napi\_value GetRawFileContent(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "GetFileContent Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // 获取参数信息
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\]即为函数第一个参数Js资源对象，OH\_ResourceManager\_InitNativeResourceManager转为Native对象
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string filename(strBuf, strSize);
    
        // 获取rawfile指针对象
        RawFile \*rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, filename.c\_str());
        if (rawFile != nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "OH\_ResourceManager\_OpenRawFile success");
        }
        // 获取rawfile大小并申请内存
        long len = OH\_ResourceManager\_GetRawFileSize(rawFile);
        std::unique\_ptr<uint8\_t\[\]> data = std::make\_unique<uint8\_t\[\]>(len);
    
        // 一次性读取rawfile全部内容
        int res = OH\_ResourceManager\_ReadRawFile(rawFile, data.get(), len);
    
        // 关闭打开的指针对象
        OH\_ResourceManager\_CloseRawFile(rawFile);
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        // 转为js对象
        return CreateJsArrayValue(env, data, len);
    }
    
    // 示例三：获取rawfile文件描述符 GetRawFileDescriptor
    // 定义一个函数，将RawFileDescriptor转为js对象
    napi\_value createJsFileDescriptor(napi\_env env, RawFileDescriptor& descriptor)
    {
        // 创建js对象
        napi\_value result;
        napi\_status status = napi\_create\_object(env, &result);
        if (status != napi\_ok) {
            return result;
        }
    
        // 将文件描述符fd存入到result对象中
        napi\_value fd;
        status = napi\_create\_int32(env, descriptor.fd, &fd);
        if (status != napi\_ok) {
            return result;
        }
        status = napi\_set\_named\_property(env, result, "fd", fd);
        if (status != napi\_ok) {
            return result;
        }
    
        // 将文件偏移量offset存入到result对象中
        napi\_value offset;
        status = napi\_create\_int64(env, descriptor.start, &offset);
        if (status != napi\_ok) {
            return result;
        }
        status = napi\_set\_named\_property(env, result, "offset", offset);
        if (status != napi\_ok) {
            return result;
        }
    
        // 将文件长度length存入到result对象中
        napi\_value length;
        status = napi\_create\_int64(env, descriptor.length, &length);
        if (status != napi\_ok) {
            return result;
        }
        status = napi\_set\_named\_property(env, result, "length", length);
        if (status != napi\_ok) {
            return result;
        }
        return result;
    }
    
    napi\_value GetRawFileDescriptor(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "NDKTest GetRawFileDescriptor Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // 获取参数信息
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\]即为函数第一个参数Js资源对象，OH\_ResourceManager\_InitNativeResourceManager转为Native对象
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string filename(strBuf, strSize);
        // 获取rawfile指针对象
        RawFile \*rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, filename.c\_str());
        if (rawFile != nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "OH\_ResourceManager\_OpenRawFile success");
        }
        // 获取rawfile的描述符RawFileDescriptor {fd, offset, length}
        RawFileDescriptor descriptor;
        OH\_ResourceManager\_GetRawFileDescriptor(rawFile, descriptor);
        // 关闭打开的指针对象
        OH\_ResourceManager\_CloseRawFile(rawFile);
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        // 转为js对象
        return createJsFileDescriptor(env, descriptor);
    }
    
    // 示例四：判断路径是否是rawfile下的目录 IsRawDir
    napi\_value CreateJsBool(napi\_env env, bool &bValue)
    {
        napi\_value jsValue = nullptr;
        if (napi\_get\_boolean(env, bValue, &jsValue) != napi\_ok) {
            return nullptr;
        }
        return jsValue;
    }
    
    napi\_value IsRawDir(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "NDKTest IsRawDir Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // 获取参数信息
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\]即为函数第一个参数Js资源对象，OH\_ResourceManager\_InitNativeResourceManager转为Native对象
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
    
        napi\_valuetype fileNameType;
        napi\_typeof(env, argv\[1\], &fileNameType);
        if (fileNameType == napi\_undefined || fileNameType == napi\_null) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "NDKTest file name is null");
            bool temp = false;
            return CreateJsBool(env, temp);
        }
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string filename(strBuf, strSize);
        // 判断是否是rawfile下的目录
        bool result = OH\_ResourceManager\_IsRawDir(mNativeResMgr, filename.c\_str());
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        return CreateJsBool(env, result);
    }
    

**4\. ArkTS侧调用**

1.  打开src\\main\\ets\\pages\\index.ets, 导入"libentry.so"。
    
2.  资源获取包括获取本应用包资源、应用内跨包资源、跨应用包资源。
    
    通过context.resourceManager获取本应用包resourceManager对象。
    
    通过context.createModuleContext().resourceManager获取应用内跨包resourceManager对象。
    
    Context的更多使用信息请参考[应用上下文Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage)。
    
3.  调用src/main/cpp/types/libentry/index.d.ts中声明的接口，如getFileList，传入js的资源管理对象以及rawfile文件夹的相对路径。
    
    获取本应用包资源resourceManager对象的示例如下：
    
    import { util } from '@kit.ArkTS';
    import { resourceManager } from '@kit.LocalizationKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import testNapi from 'libentry.so'; // 导入so
    
    const DOMAIN = 0x0000;
    const TAG = '\[Sample\_rawfile\]';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
      private resMgr = this.getUIContext().getHostContext()?.resourceManager; // 获取本应用包的资源对象
      @State rawfileListMsg: string = 'FileList = ';
      @State retMsg: string = 'isRawDir = ';
      @State rawfileContentMsg: string = 'RawFileContent = ';
      @State rawfileDescriptorMsg: string = 'RawFileDescriptor.length = ';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .id('hello\_world')
              .fontSize(30)
              .fontWeight(FontWeight.Bold)
              .onClick(async () => {
                // 传入资源管理对象，以及访问的rawfile文件夹名称
                let rawFileList: Array<String> = testNapi.getFileList(this.resMgr, '');
                this.rawfileListMsg = 'FileList = ' + rawFileList;
                hilog.info(DOMAIN, TAG, this.rawfileListMsg);
    
                // 'sub\_rawfile'仅作示例，请替换为实际使用的资源
                let ret: boolean = testNapi.isRawDir(this.resMgr, 'sub\_rawfile');
                this.retMsg = 'isRawDir = ' + ret;
                hilog.info(DOMAIN, TAG, this.retMsg);
    
                // 传入资源管理对象，以及访问的rawfile文件夹名称
                // 'rawfile1.txt'仅作示例，请替换为实际使用的资源
                let rawfileArray: Uint8Array = testNapi.getRawFileContent(this.resMgr, 'rawfile1.txt');
                // 将Uint8Array转为字符串
                let textDecoder: util.TextDecoder = new util.TextDecoder();
                let rawfileContent: string = textDecoder.decodeToString(rawfileArray);
                this.rawfileContentMsg = 'RawFileContent = ' + rawfileContent;
                hilog.info(DOMAIN, TAG, this.rawfileContentMsg);
    
                // 传入资源管理对象，以及访问的rawfile文件名称
                // 'rawfile1.txt'仅作示例，请替换为实际使用的资源
                let rawfileDescriptor: resourceManager.RawFileDescriptor =
                  testNapi.getRawFileDescriptor(this.resMgr, 'rawfile1.txt');
                this.rawfileDescriptorMsg = 'RawFileDescriptor.length = ' + rawfileDescriptor.length;
                hilog.info(DOMAIN, TAG, this.rawfileDescriptorMsg);
              })
            Text(this.rawfileListMsg).id('get\_file\_list').fontSize(30);
            Text(this.retMsg).id('is\_raw\_dir').fontSize(30);
            Text(this.rawfileContentMsg).id('get\_raw\_file\_content').fontSize(30);
            Text(this.rawfileDescriptorMsg).id('get\_raw\_file\_descriptor').fontSize(30);
          }
          .width('100%')
        }
        .height('100%')
      }
    }
