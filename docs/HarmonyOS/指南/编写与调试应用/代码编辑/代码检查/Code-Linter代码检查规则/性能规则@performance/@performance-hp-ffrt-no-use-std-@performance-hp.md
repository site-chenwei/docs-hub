---
title: "@performance/hp"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-ffrt-no-use-std"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "性能规则@performance"
  - "@performance/hp-ffrt-no-use-std"
captured_at: "2026-04-17T01:36:47.277Z"
---

# @performance/hp-ffrt-no-use-std

禁止在FFRT worker中使用std::xxx等同步接口。该规则仅对C/C++文件进行检查。

并行化场景下，建议优先修改。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@performance/hp-ffrt-no-use-std": "suggestion",
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

#include <iostream>
#include <algorithm>
#include <mutex>
#include <condition\_variable>
#include <unistd.h>
// ffrt头文件
#include "ffrt/ffrt.h"
using namespace std;
int N = 100;
int M = 100;

_// ffrt::submit中使用了std::mutex_
    void PositiveCase1(int temp) {
    ffrt::mutex lock;
    int acc = 0;
    for (int i = 0; i < N; ++i) {
        ffrt::submit(
            \[&\]() {
                for (int j = 0; j < M; ++j) {
                    lock.lock();
                    acc++;
                    lock.unlock();
                }
            },
            {}, {});
    }
}
_// ffrt::submit中使用了std::condition\_variable_
    void PositiveCase2(int temp) {
    ffrt::condition\_variable cond;
    int a = 0;
    ffrt::mutex lock\_;
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<ffrt::mutex> lck(lock\_);
            cond.wait(lck, \[&\] { return a == 1; });
        },
        {}, {});
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<ffrt::mutex> lck(lock\_);
            a = 1;
            cond.notify\_one();
        },
        {}, {});
    ffrt::wait();
}
_// ffrt::submit中使用了std::usleep_
    void PositiveCase3(int temp) {
    ffrt::submit(
        \[&\]() {
        ffrt\_usleep(100);
        printf("test");
        ffrt\_yield();      
    }, {}, {});
}
_// ffrt::submit中使用了pthread\_rwlock\_wrlock或pthread\_rwlock\_rdlock_
    void PositiveCase4(int temp) {
    int a = 0;
    ffrt\_rwlock\_t mtx;
    ffrt::submit(
        \[&\]() {
        int ret = ffrt\_rwlock\_wrlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
        a++;
        ret = ffrt\_rwlock\_unlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
    }, {}, {});
    ffrt::submit(
        \[&\]() {
        int ret = ffrt\_rwlock\_rdlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
        printf("sum is %d\\n", a);
        ret = ffrt\_rwlock\_unlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
    }, {}, {});
}

#### 反例

#include <iostream>
#include <algorithm>
#include <mutex>
#include <condition\_variable>
#include <unistd.h>
// ffrt头文件 
#include "ffrt/ffrt.h" 
using namespace std;
int N = 100;
int M = 100;
_// ffrt::submit中使用了std::mutex_
    void NegativeCase1(int temp) {
    std::mutex lock;
    int acc = 0;
    for (int i = 0; i < N; ++i) {
        ffrt::submit(
            \[&\]() {
                for (int j = 0; j < M; ++j) {
                    lock.lock();
                    acc++;
                    lock.unlock();
                }
            },
            {}, {});
    }
}
_// ffrt::submit中使用了std::condition\_variable_
    void NegativeCase2(int temp) {
    std::condition\_variable cond;
    int a = 0;
    std::mutex lock\_;
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<std::mutex> lck(lock\_);
            cond.wait(lck, \[&\] { return a == 1; });
        },
        {}, {});
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<std::mutex> lck(lock\_);
            a = 1;
            cond.notify\_one();
        },
        {}, {});
    ffrt::wait();
}
_// ffrt::submit中使用了std::usleep_
    void NegativeCase3(int temp) {
    ffrt::submit(
        \[&\]() {
        usleep(100);
        printf("test");
        ffrt\_yield();
    }, {}, {});
}
_// ffrt::submit中使用了pthread\_rwlock\_wrlock或pthread\_rwlock\_rdlock_
    void NegativeCase4(int temp) {
    int a = 0;
    pthread\_rwlock\_t mtx;
    ffrt::submit(
        \[&\]() {
        int ret = pthread\_rwlock\_wrlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
        a++;
        ret = pthread\_rwlock\_unlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
    }, {}, {});
    ffrt::submit(
        \[&\]() {
        int ret = pthread\_rwlock\_rdlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
        printf("sum is %d\\n", a);
        ret = pthread\_rwlock\_unlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
    }, {}, {});
}

#### 规则集

plugin:@performance/recommended
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
