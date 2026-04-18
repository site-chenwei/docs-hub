---
title: "应用文件访问(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fileio-guidelines"
menu_path:
  - "指南"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "应用文件"
  - "应用文件访问与管理"
  - "应用文件访问(C/C++)"
captured_at: "2026-04-17T01:35:43.075Z"
---

# 应用文件访问(C/C++)

#### 场景介绍

FileIO模块提供了部分文件基础操作能力，其他能力请参考[libc标准库](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/musl)/[c++标准库](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cpp)。

#### 约束限制

进行文件操作之前，必须保证传入正确有效的URI或path。

#### 接口说明

接口的详细说明，请参考[FileIO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-fileio-h)。

| 接口名称 | 描述 |
| :-- | :-- |
| FileManagement\_ErrCode OH\_FileIO\_GetFileLocation(char \*uri, int uriLength, FileIO\_FileLocation \*location) | 获取文件存储位置。 |
| enum FileIO\_FileLocation FileIO\_FileLocation | 文件存储位置枚举值。 |
| enum FileManagement\_ErrCode FileManagement\_ErrCode | 文件管理模块错误码。 |

#### 开发步骤

**在CMake脚本中链接动态库**

CMakeLists.txt中添加以下lib。

```txt
target_link_libraries(sample PUBLIC libohfileio.so)
```

**添加头文件**

```
#include <cstdio>
#include <cstring>
#include <filemanagement/fileio/oh_fileio.h>
```

调用OH\_FileIO\_GetFileLocation接口获取文件存储位置。示例代码如下所示：

```c
void GetFileLocationExample() {
    char *uri = "file://com.example.demo/data/storage/el2/base/files/test.txt";
    FileIO_FileLocation location;
    FileManagement_ErrCode ret = OH_FileIO_GetFileLocation(uri, strlen(uri), &location);
    if (ret == 0) {
        if (location == FileIO_FileLocation::LOCAL) {
            printf("This file is on local.");
        } else if (location == FileIO_FileLocation::CLOUD) {
            printf("This file is on cloud.");
        } else if (location == FileIO_FileLocation::LOCAL_AND_CLOUD) {
            printf("This file is both on local and cloud.");
        }
    } else {
        printf("GetFileLocation failed, error code is %d", ret);
    }
}
```
