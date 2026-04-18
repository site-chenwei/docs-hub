---
title: "如何在Native侧往用户目录写临时文件"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-11"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧往用户目录写临时文件"
captured_at: "2026-04-17T02:03:01.725Z"
---

# 如何在Native侧往用户目录写临时文件

**问题详情**

应用目录中，用户可以将临时文件写入以下目录。请查看native层写文件的代码示例：

cpp

#include <stdio.h>

void writeTempFile(const char\* path, const char\* content) {

FILE\* file = fopen(path, "w");

if (file != NULL) {

fprintf(file, "%s", content);

fclose(file);

}

}

可写入临时文件的目录包括：

cache：用于存放缓存文件。

files：用于存放应用数据文件。

**解决措施**

目前没有直接写文件的Native接口，但可以通过C++基础库结合沙箱路径实现写文件操作。

代码如下：

#include "WriteFile.h"
#include "napi/native\_api.h"
#include <fstream>
napi\_value WriteFile::WriteTemporaryFile(napi\_env env, napi\_callback\_info info) {
    std::ofstream file("data/storage/el2/base/temp/2.txt");
    if (file.is\_open()) {        // Determine if the file can be opened normally
        file << "Hello, World!"; // Write content to a file
        file.close();            // close file
    }
    return nullptr;
}

用户可访问的目录可参考以下链接：[应用沙箱目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)
