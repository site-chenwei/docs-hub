---
title: "GPU/CPU内存访问同步操作开发指南 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fence-guidelines"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "GPU/CPU内存访问同步操作开发指南 (C/C++)"
captured_at: "2026-04-17T01:36:09.108Z"
---

# GPU/CPU内存访问同步操作开发指南 (C/C++)

#### 场景介绍

NativeFence是管理fenceFd同步状态的模块。开发者可通过其接口实现以下功能：设置阻塞时间、永久阻塞、关闭fenceFd以及检查其有效性。

#### 接口说明

| 接口名 | 描述 |
| :-- | :-- |
| OH\_NativeFence\_IsValid (int fenceFd) | 检查fenceFd是否有效。 |
| OH\_NativeFence\_Wait (int fenceFd, uint32\_t timeout) | 阻塞传入的fenceFd，超时参数指定了允许等待的最长时间。 |
| OH\_NativeFence\_WaitForever (int fenceFd) | 永久阻塞传入的fenceFd。 |
| OH\_NativeFence\_Close (int fenceFd) | 关闭fenceFd。 |

详细的接口说明请参考[NativeFence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativefence)。

#### 开发步骤

以下步骤描述了如何使用NativeFence提供的Native API接口。

**添加动态链接库**

CMakeLists.txt中添加以下库文件。

```txt
libnative_fence.so
```

**头文件**

```
#include <native_fence/native_fence.h>
#include <cstring>
#include <iostream>
#include <linux/sync_file.h>
#include <signal.h>
#include <sys/signalfd.h>
#include <unistd.h>
```

1.  **使用signalfd()接口创建fenceFd**。
    
    sigset\_t mask;
    sigemptyset(&mask);
    sigaddset(&mask, SIGINT); // Monitor SIGINT signal (Ctrl C)
    sigaddset(&mask, SIGURG); // Generated when urgent data or out of band data arrives at the socket
    sigprocmask(SIG\_BLOCK, &mask, NULL);
    int sfd = signalfd(-1, &mask, 0);
    
2.  **判断传入的fenceFd是否合法**。
    
    bool isValid = OH\_NativeFence\_IsValid(INVALID\_FD);
    if (!isValid) {
        DRAWING\_LOGW("fenceFd is invalid");
    }
    
3.  **调用OH\_NativeFence\_Wait阻塞接口，等待fence完成后进行下一步操作**。
    
    constexpr uint32\_t TIMEOUT\_MS = 5000;
    // ...
    bool result = OH\_NativeFence\_Wait(INVALID\_FD, TIMEOUT\_MS);
    
4.  **调用OH\_NativeFence\_WaitForever阻塞接口，等待fence完成后进行下一步操作**。
    
    bool result2 = false;
    auto startTime = std::chrono::steady\_clock::now();
    result2 = OH\_NativeFence\_WaitForever(sfd);
    auto endTime = std::chrono::steady\_clock::now();
    auto duration = std::chrono::duration\_cast<std::chrono::milliseconds>(endTime - startTime).count();
    if (result2) {
        DRAWING\_LOGI("SyncFenceWaitForever has an event occurring result2 %{public}d, cost\_time: %{public}d",
            result2, duration);
    } else {
        DRAWING\_LOGI("SyncFenceWaitForever timeout with no event occurrence"
            "result2 %{public}d, cost\_time: %{public}d", result2, duration);
    }
    
5.  **GPU或CPU发送同步信号(signal)，通知fenceFd解除阻塞**。
    
6.  **关闭fenceFd**。
    
    OH\_NativeFence\_Close(sfd);
