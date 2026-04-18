---
title: "CppCrash类问题优化建议"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cpp-crash-opt"
menu_path:
  - "最佳实践"
  - "稳定性"
  - "稳定性优化"
  - "应用异常退出类问题优化建议"
  - "CppCrash类问题优化建议"
captured_at: "2026-04-17T01:54:19.911Z"
---

# CppCrash类问题优化建议

#### 优化建议1：使用map\\vector\\list\\set等STL库时，要避免数据竞争

错误示例：

void EraseMapItem1(int key)
{
    appRunningRecordMap\_.erase(key);
}

如果存在多个线程同时操作同一个map时，此处将map元素删除，另一个线程同时操作map会产生崩溃问题。

正确示例：

void EraseMapItem2(int key)
{
    // 加锁
    std::lock\_guard<std::mutex> lock(mutex\_);
    appRunningRecordMap\_.erase(key);
}

void FindMapItem(int key)
{
    // 加锁
    std::lock\_guard<std::mutex> lock(mutex\_);
    appRunningRecordMap\_.find(key);
}

#### 优化建议2：多线程访问全局变量/静态变量/类成员变量，如果涉及修改删除操作，对其所有操作都要加锁保护

错误示例：

std::list<std::shared\_ptr<Object>> g\_list;

void MainFunc()
{
    auto xxx = std::make\_shared<Object>();
    g\_list.push\_back(xxx);
}

// 线程1
void Thread1Func()
{
    for (auto &ptr : g\_list) {
        ptr->method();
    }
}

// 线程2
void Thread2Func()
{
    g\_list.clear(); // 此处清空list，可能会造成线程1使用g\_list时发生崩溃
}

正确示例：

// 线程1
void Thread1FuncEx()
{
    std::lock\_guard<std::mutex> lock(mutexEx\_);
    for (auto &ptr : g\_list) {
        ptr->method();
    }
}

// 线程2
void Thread2FuncEx()
{
    std::lock\_guard<std::mutex> lock(mutexEx\_);
    g\_list.clear();
}

#### 优化建议3：谨慎在异步场景lambda表达式中使用引用捕获，注意变量生命周期

错误示例：

void Checker::Detection(std::string& url)
{
    handler.PostAsyncTask(
        \[this, &url\]() {
            if (!Checker::DoCheck(url)) {
                // ...
            }
        }
    );
    // 这里url变量即将析构
}

bool Checker::DoCheck(const std::string& url)
{
    // ...
    return true;
}

正确示例：

void Checker::Detection2(std::string& url)
{
    handler.PostAsyncTask(
        \[this, url\]() {
            if (!Checker::DoCheck(url)) {
                // ...
            }
        }
    );
    // 这里url变量即将析构，但lambda已经有自己的拷贝
}

#### 优化建议4：智能指针和裸指针使用前，都要进行判空

错误示例：

std::shared\_ptr<Object> smartPointer = nullptr;
smartPointer->method();

正确示例：

std::shared\_ptr<Object> smartPointer = nullptr;
if (smartPointer != nullptr) {
    smartPointer->method();
}

#### 优化建议5：不要使用多个智能指针管理同一个裸指针

错误示例：

Object\* xxx = new Object();
std::shared\_ptr<Object> xxx1(xxx); // xxx1引用计数减为0时析构一次xxx
std::shared\_ptr<Object> xxx2(xxx); // xxx2引用计数减为0时析构一次xxx

正确示例：

std::shared\_ptr<Object> xxx = std::make\_shared<Object>();

#### 优化建议6：不要从智能指针中取出裸指针继续使用

错误示例：

auto smartPointer = std::make\_shared<Object>(); // smartPointer引用计数减为0时析构
auto pointer = smartPointer.get();
pointer->method(); // 当smartPinter析构后继续使用pointer可能发生crash

正确示例：

auto smartPointer = std::make\_shared<Object>();
smartPointer->method();

#### 优化建议7：禁止将裸指针构造为智能指针后，继续使用或主动释放裸指针

错误示例：

Object\* pointer = new Object();
std::shared\_ptr<Object> smartPointer(pointer); // smartPointer引用计数减为0时析构
pointer->method(); // 当smartPointer析构后继续使用pointer可能发生crash
delete pointer; // 主动释放裸指针发生crash

正确示例：

auto smartPointer = std::make\_shared<Object>();
smartPointer->method();

#### 优化建议8：禁止在信号处理流程中调用非异步安全函数和使用map\\vector\\list\\set等STL库

错误示例：

static void SignalHandler(int signo, siginfo\_t\* si, void\* context) // 信号处理函数
{
    char \*c = (char\*)malloc(10); // 禁止使用malloc，malloc是非异步安全函数
}

正确示例：

static void SignalHandlerEx(int signo, siginfo\_t\* si, void\* context) // 信号处理函数
{
    char c\[10\] = {0};
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/hnMEEYq_RT6irxpVO_JG7g/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=0F4E4C5C3403867000D27EEF75B3D7CE4724201B41221898686F7E0518B84C35)

信号处理函数直接或间接调用的对象或函数需确保异步安全。

**malloc是非异步安全函数，因此在信号处理函数中，**

1.  禁止在堆上申请内存
2.  禁止使用STL类对象，比如在堆动态分配内存的 string、vector、list、set、map...
3.  调用的外部函数，需确保该函数异步安全，典型非异步安全的getproctid、fgets、fopen...

**异步安全函数列表**

如果可以安全的调用该函数，并且在信号处理程序上文中可以安全的使用，则该函数是异步安全的或异步信号安全的。下表中所列的均为异步安全函数，来自POSIX标准。应用程序可以**在信号处理程序中调用这些异步安全函数**。

<table><tbody><tr><td class="cellrowborder" valign="top" width="25%"><p>_Exit()</p></td><td class="cellrowborder" valign="top" width="25%"><p>fexecve()</p></td><td class="cellrowborder" valign="top" width="25%"><p>posix_trace_event()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigprocmask()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>_exit()</p></td><td class="cellrowborder" valign="top" width="25%"><p>fork()</p></td><td class="cellrowborder" valign="top" width="25%"><p>pselect()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigqueue()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>abort()</p></td><td class="cellrowborder" valign="top" width="25%"><p>fstat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>pthread_kill()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigset()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>accept()</p></td><td class="cellrowborder" valign="top" width="25%"><p>fstatat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>pthread_self()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigsuspend()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>access()</p></td><td class="cellrowborder" valign="top" width="25%"><p>fsync()</p></td><td class="cellrowborder" valign="top" width="25%"><p>pthread_sigmask()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sleep()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>aio_error()</p></td><td class="cellrowborder" valign="top" width="25%"><p>ftruncate()</p></td><td class="cellrowborder" valign="top" width="25%"><p>raise()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sockatmark()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>aio_return()</p></td><td class="cellrowborder" valign="top" width="25%"><p>futimens()</p></td><td class="cellrowborder" valign="top" width="25%"><p>read()</p></td><td class="cellrowborder" valign="top" width="25%"><p>socket()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>aio_suspend()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getegid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>readlink()</p></td><td class="cellrowborder" valign="top" width="25%"><p>socketpair()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>alarm()</p></td><td class="cellrowborder" valign="top" width="25%"><p>geteuid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>readlinkat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>stat()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>bind()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getgid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>recv()</p></td><td class="cellrowborder" valign="top" width="25%"><p>symlink()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>cfgetispeed()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getgroups()</p></td><td class="cellrowborder" valign="top" width="25%"><p>recvfrom()</p></td><td class="cellrowborder" valign="top" width="25%"><p>symlinkat()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>cfgetospeed()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getpeername()</p></td><td class="cellrowborder" valign="top" width="25%"><p>recvmsg()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcdrain()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>cfsetispeed()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getpgrp()</p></td><td class="cellrowborder" valign="top" width="25%"><p>rename()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcflow()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>cfsetospeed()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getpid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>renameat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcflush()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>chdir()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getppid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>rmdir()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcgetattr()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>chmod()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getsockname()</p></td><td class="cellrowborder" valign="top" width="25%"><p>select()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcgetpgrp()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>chown()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getsockopt()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sem_post()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcsendbreak()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>clock_gettime()</p></td><td class="cellrowborder" valign="top" width="25%"><p>getuid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>send()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcsetattr()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>close()</p></td><td class="cellrowborder" valign="top" width="25%"><p>kill()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sendmsg()</p></td><td class="cellrowborder" valign="top" width="25%"><p>tcsetpgrp()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>connect()</p></td><td class="cellrowborder" valign="top" width="25%"><p>link()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sendto()</p></td><td class="cellrowborder" valign="top" width="25%"><p>time()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>creat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>linkat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>setgid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>timer_getoverrun()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>dup()</p></td><td class="cellrowborder" valign="top" width="25%"><p>listen()</p></td><td class="cellrowborder" valign="top" width="25%"><p>setpgid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>timer_gettime()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>dup2()</p></td><td class="cellrowborder" valign="top" width="25%"><p>lseek()</p></td><td class="cellrowborder" valign="top" width="25%"><p>setsid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>timer_settime()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>execl()</p></td><td class="cellrowborder" valign="top" width="25%"><p>lstat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>setsockopt()</p></td><td class="cellrowborder" valign="top" width="25%"><p>times()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>execle()</p></td><td class="cellrowborder" valign="top" width="25%"><p>mkdir()</p></td><td class="cellrowborder" valign="top" width="25%"><p>setuid()</p></td><td class="cellrowborder" valign="top" width="25%"><p>umask()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>execv()</p></td><td class="cellrowborder" valign="top" width="25%"><p>mkdirat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>shutdown()</p></td><td class="cellrowborder" valign="top" width="25%"><p>uname()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>execve()</p></td><td class="cellrowborder" valign="top" width="25%"><p>mkfifo()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigaction()</p></td><td class="cellrowborder" valign="top" width="25%"><p>unlink()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>faccessat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>mkfifoat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigaddset()</p></td><td class="cellrowborder" valign="top" width="25%"><p>unlinkat()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>fchdir()</p></td><td class="cellrowborder" valign="top" width="25%"><p>mknod()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigdelset()</p></td><td class="cellrowborder" valign="top" width="25%"><p>utime()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>fchmod()</p></td><td class="cellrowborder" valign="top" width="25%"><p>mknodat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigemptyset()</p></td><td class="cellrowborder" valign="top" width="25%"><p>utimensat()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>fchmodat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>open()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigfillset()</p></td><td class="cellrowborder" valign="top" width="25%"><p>utimes()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>fchown()</p></td><td class="cellrowborder" valign="top" width="25%"><p>openat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigismember()</p></td><td class="cellrowborder" valign="top" width="25%"><p>wait()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>fchownat()</p></td><td class="cellrowborder" valign="top" width="25%"><p>pause()</p></td><td class="cellrowborder" valign="top" width="25%"><p>signal()</p></td><td class="cellrowborder" valign="top" width="25%"><p>waitpid()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>fcntl()</p></td><td class="cellrowborder" valign="top" width="25%"><p>pipe()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigpause()</p></td><td class="cellrowborder" valign="top" width="25%"><p>write()</p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p>fdatasync()</p></td><td class="cellrowborder" valign="top" width="25%"><p>poll()</p></td><td class="cellrowborder" valign="top" width="25%"><p>sigpending()</p></td><td class="cellrowborder" valign="top" width="25%">&nbsp;&nbsp;</td></tr></tbody></table>

#### 优化建议9：不要传递this指针到其他模块或者线程

将this指针传递到其他模块或者线程是非常危险的行为，如果其他模块或者线程与this指针指向的对象的生命周期不一致时，很容易造成崩溃问题。

错误示例：

void Object1::Run()
{
    startThread\_ = std::shared\_ptr<std::thread>(new std::thread(\[this\] { // 将this指针传递给其他线程
        if (this == nullptr) {
            return;
        }
        this->GetInfo();
        // ...
    }));
    // ...
}

正确示例：

class Object2 : public std::enable\_shared\_from\_this<Object2> {
public:
    void Run();
    void GetInfo() {}
    // ...

private:
    std::shared\_ptr<std::thread> startThread\_;
    // ...
};

void Object2::Run()
{
    std::weak\_ptr<Object2> weakPtr = shared\_from\_this(); // 调用shared\_from\_this捕获this(c++17开始可使用waek\_form\_this)
    startThread\_ = std::shared\_ptr<std::thread>(new std::thread(\[weakPtr\] { // weakPtr传递给其他线程
        auto ptr = weakPtr.lock();
        if (ptr == nullptr) {
            return;
        }
        ptr->GetInfo();
        // ...
    }));
    // ...
}

void MainFuncEx()
{
    auto object = std::make\_shared<Object2>(); // 必须使用智能指针初始化Object对象
    object->Run();
}

#### 优化建议10：禁止接口返回局部变量的引用

错误示例：

std::string& GetString()
{
    std::string result = "this is string";
    return result; // 禁止返回局部变量result的引用
}

正确示例：

std::string GetStringEx()
{
    std::string result = "this is string";
    return result; // 返回局部变量的值
}
