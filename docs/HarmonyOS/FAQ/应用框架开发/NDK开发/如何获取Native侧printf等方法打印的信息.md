---
title: "如何获取Native侧printf等方法打印的信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-16"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何获取Native侧printf等方法打印的信息"
captured_at: "2026-04-17T02:03:01.764Z"
---

# 如何获取Native侧printf等方法打印的信息

**问题详情**

Native侧引用的三方库使用printf等方法打印到stdout、stderr的信息怎么获取？在三方库代码里有许多fprintf, std::cout printf 的标准日志打印log，在程序开发中无法查看这些日志。

**解决措施**

cout/printf是语言提供的打印函数，并不能填充到hilog日志中。可通过重定向的方法将日志打印到文件来获取打印信息。具体方法如下：

Native侧重定向方法主体。

#include "napi/native\_api.h" 
#include <hilog/log.h> 
#include <string> 
#include "iostream" 
#include "fstream" 
#define LOG\_TAG "Pure" 
 
static napi\_value Redirect(napi\_env env, napi\_callback\_info info) { 
    // Get the JS parameters of the function 
    size\_t argc = 1; 
    napi\_value argv\[1\] = {nullptr}; 
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr); 
    // Resolve parameter 1, the destination directory for saving the file
    size\_t targetDirectoryNameSize; 
    char targetDirectoryNameBuf\[512\]; 
    napi\_get\_value\_string\_utf8(env, argv\[0\], targetDirectoryNameBuf, sizeof(targetDirectoryNameBuf), 
                               &targetDirectoryNameSize); 
    std::string targetDirectoryName(targetDirectoryNameBuf, targetDirectoryNameSize); // target directory 
    OH\_LOG\_INFO(LOG\_APP, "C++Received target path on the side === %{public}s", targetDirectoryNameBuf); 
    std::string targetSandboxPath = targetDirectoryName + "/Log.log"; // Saved file path 
     
    // Use the freopen function to associate files with standard output 
    FILE \*stdoutFile = NULL; 
    FILE \*stderrFile = NULL; 
    stdoutFile = freopen(targetSandboxPath.c\_str(), "a", stdout); 
    stderrFile = freopen(targetSandboxPath.c\_str(), "a", stderr); 
    if (NULL == stdoutFile || NULL == stderrFile) { 
        OH\_LOG\_INFO(LOG\_APP, "Recreate！"); 
        // Opening the file output stream of the sandbox file will create a file
        std::ofstream outputFile(targetSandboxPath, std::ios::binary); 
        if (!outputFile) { 
            OH\_LOG\_ERROR(LOG\_APP, "Unable to create target file!"); 
            return nullptr; 
        } 
        stdoutFile = freopen(targetSandboxPath.c\_str(), "a", stdout); 
        stderrFile = freopen(targetSandboxPath.c\_str(), "a", stderr); 
        if (NULL == stdoutFile || NULL == stderrFile) { 
            OH\_LOG\_ERROR(LOG\_APP, "fail!"); 
            return nullptr; 
        } 
    } 
    OH\_LOG\_WARN(LOG\_APP, "redirect!"); 
    printf("\\n\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Redirect dividing line\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\n"); 
    return 0; 
}

在ArkTS侧调用并传入路径信息。

在EntryAbility的onCreate()方法中调用重定向。

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  let file : string = this.context.getApplicationContext().filesDir;
  testNapi.redirect(file);
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
}
