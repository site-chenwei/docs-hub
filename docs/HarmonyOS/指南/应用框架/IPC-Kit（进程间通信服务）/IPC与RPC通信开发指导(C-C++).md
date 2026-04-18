---
title: "IPC与RPC通信开发指导(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ipc-capi-development-guideline"
menu_path:
  - "指南"
  - "应用框架"
  - "IPC Kit（进程间通信服务）"
  - "IPC与RPC通信开发指导(C/C++)"
captured_at: "2026-04-17T01:35:45.534Z"
---

# IPC与RPC通信开发指导(C/C++)

#### 场景介绍

IPC让运行在不同进程间的Proxy和Stub实现互相通信。IPC CAPI是IPC Kit提供的C语言接口。

IPC CAPI接口不直接提供获取通信代理对象的能力，该功能由[Ability Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilitykit-overview)提供。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/OKkFCGDOS12dOyeWLXt-Lg/zh-cn_image_0000002538019240.png?HW-CC-KV=V1&HW-CC-Date=20260417T013547Z&HW-CC-Expire=86400&HW-CC-Sign=5E5C3FFEA52322CD14A26F2FE3269E3E501EBF07461B952B4B12CC6E44C5A202)

进程间IPC通道的建立，请参考[Native子进程开发指导（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-development-guideline)。本文重点介绍IPC CAPI的使用。

#### 接口说明

**表1** IPC CAPI侧关键接口

| 接口名 | 描述 |
| :-- | :-- |
| 
typedef int (\*OH\_OnRemoteRequestCallback)

(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply,

void \*userData);

 | Stub端用于处理远端数据请求的回调函数。 |
| 

OHIPCRemoteStub\* OH\_IPCRemoteStub\_Create

(const char \*descriptor, OH\_OnRemoteRequestCallback requestCallback,

OH\_OnRemoteDestroyCallback destroyCallback, void \*userData);

 | 创建OHIPCRemoteStub对象。 |
| 

int OH\_IPCRemoteProxy\_SendRequest(const OHIPCRemoteProxy \*proxy,

uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply,

const OH\_IPC\_MessageOption \*option);

 | IPC消息发送函数。 |
| struct OHIPCRemoteProxy; | 用于向远端发送请求的OHIPCRemoteProxy对象，需要依赖元能力接口返回。 |
| 

OHIPCDeathRecipient\* OH\_IPCDeathRecipient\_Create

(OH\_OnDeathRecipientCallback deathRecipientCallback,

OH\_OnDeathRecipientDestroyCallback destroyCallback,

void \*userData);

 | 创建用于监听远端OHIPCRemoteStub对象死亡的通知对象（OHIPCDeathRecipient对象）。 |
| 

int OH\_IPCRemoteProxy\_AddDeathRecipient(OHIPCRemoteProxy \*proxy,

OHIPCDeathRecipient \*recipient);

 | 向OHIPCRemoteProxy对象注册死亡监听，用于接收远端OHIPCRemoteStub对象死亡时的回调通知。 |

详细的接口说明请参考[IPCKit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipckit)。

#### 开发步骤

先创建服务端Stub对象，通过元能力获取其客户端代理Proxy对象，然后用Proxy对象与服务端Stub对象进行IPC通信，同时再注册远端对象的死亡通知回调，用于Proxy侧感知服务端Stub对象所在进程的死亡状态。

**动态库文件**

CMakeLists.txt中添加以下lib。

```txt
# ipc capi
libipc_capi.so
# 元能力，ability capi
libchild_process.so
```

**头文件**

#include <IPCKit/ipc\_kit.h>
#include <AbilityKit/native\_child\_process.h>

**子进程实现**

#include <IPCKit/ipc\_kit.h>
// ...
#include <IPCKit/ipc\_cremote\_object.h>
#include <IPCKit/ipc\_cparcel.h>
#include <IPCKit/ipc\_error\_code.h>

class IpcCapiStubTest {
public:
    explicit IpcCapiStubTest();
    ~IpcCapiStubTest();
    OHIPCRemoteStub \*GetRemoteStub();
    static int OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData);

private:
    OHIPCRemoteStub \*stub\_{nullptr};
};

IpcCapiStubTest::IpcCapiStubTest()
{
    // 创建stub对象
    stub\_ = OH\_IPCRemoteStub\_Create("testIpc", &IpcCapiStubTest::OnRemoteRequest, nullptr, this);
}

IpcCapiStubTest::~IpcCapiStubTest()
{
    if (stub\_ != nullptr) {
        OH\_IPCRemoteStub\_Destroy(stub\_);
    }
}

OHIPCRemoteStub \*IpcCapiStubTest::GetRemoteStub() { return stub\_; }

int IpcCapiStubTest::OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData)
{
    return OH\_IPC\_SUCCESS;
}

IpcCapiStubTest g\_ipcStubObj;

extern "C" {
OHIPCRemoteStub \*NativeChildProcess\_OnConnect()
{
    // ipcRemoteStub指向子进程实现的ipc stub对象，用于接收来自主进程的IPC消息并响应
    // 子进程根据业务逻辑控制其生命周期
    return g\_ipcStubObj.GetRemoteStub();
}

void NativeChildProcessMainProc()
{
    // 相当于子进程的Main函数，实现子进程的业务逻辑
    // ...
    // 函数返回后子进程随即退出
}

} // extern "C"

**主进程实现**

#include <IPCKit/ipc\_kit.h>
#include <AbilityKit/native\_child\_process.h>
// ...
static void OnNativeChildProcessStarted(int errCode, OHIPCRemoteProxy \*remoteProxy)
{
    if (errCode != NCP\_NO\_ERROR) {
        // 子进程未能正常启动时的异常处理
        // ...
        return;
    }

    // 保存remoteProxy对象，后续基于IPC Kit提供的API同子进程间进行IPC通信
    // 耗时操作建议转移到独立线程去处理，避免长时间阻塞回调线程
    // IPC对象使用完毕后，需要调用OH\_IPCRemoteProxy\_Destroy方法释放
    // ...
}

void CreateNativeChildProcess()
{
    // 第一个参数"libchildprocesssample.so"为实现了子进程必要导出方法的动态库文件名称
    int32\_t ret = OH\_Ability\_CreateNativeChildProcess("libchildprocesssample.so", OnNativeChildProcessStarted);
    if (ret != NCP\_NO\_ERROR) {
        // 子进程未能正常启动时的异常处理
        // ...
    }
    g\_result = ret;
}

**Proxy侧实现**

#include "IpcProxy.h"
#include <IPCKit/ipc\_error\_code.h>
#include "Ipchelper.h"

IpcProxy::IpcProxy(OHIPCRemoteProxy \*ipcProxy)
    : ipcProxy\_(ipcProxy)
{
}

IpcProxy::~IpcProxy()
{
    if (ipcProxy\_ != nullptr) {
        OH\_IPCRemoteProxy\_Destroy(ipcProxy\_);
    }
}

bool IpcProxy::RequestExitChildProcess(int32\_t exitCode)
{
    if (ipcProxy\_ == nullptr) {
        return false;
    }
    
    StdUniPtrIpcParcel data(OH\_IPCParcel\_Create(), OH\_IPCParcel\_Destroy);
    StdUniPtrIpcParcel reply(OH\_IPCParcel\_Create(), OH\_IPCParcel\_Destroy);
    if (data == nullptr || reply == nullptr) {
        return false;
    }
    
    if (!WriteInterfaceToken(data.get()) ||
        OH\_IPCParcel\_WriteInt32(data.get(), exitCode) != OH\_IPC\_SUCCESS) {
        return false;
    }
    
    OH\_IPC\_MessageOption ipcOpt;
    ipcOpt.mode = OH\_IPC\_REQUEST\_MODE\_SYNC;
    ipcOpt.timeout = 0;
    ipcOpt.reserved = nullptr;
    int ret = OH\_IPCRemoteProxy\_SendRequest(ipcProxy\_, IPC\_ID\_REQUEST\_EXIT\_PROCESS, data.get(), reply.get(), &ipcOpt);
    if (ret != OH\_IPC\_SUCCESS) {
        return false;
    }
    
    return true;
}

int32\_t IpcProxy::Add(int32\_t a, int32\_t b)
{
    if (ipcProxy\_ == nullptr) {
        return INT32\_MIN;
    }
    
    int32\_t result = INT32\_MIN;
    StdUniPtrIpcParcel data(OH\_IPCParcel\_Create(), OH\_IPCParcel\_Destroy);
    StdUniPtrIpcParcel reply(OH\_IPCParcel\_Create(), OH\_IPCParcel\_Destroy);
    if (data == nullptr || reply == nullptr) {
        return result;
    }
    
    if (!WriteInterfaceToken(data.get()) ||
        OH\_IPCParcel\_WriteInt32(data.get(), a) != OH\_IPC\_SUCCESS ||
        OH\_IPCParcel\_WriteInt32(data.get(), b) != OH\_IPC\_SUCCESS) {
        return result;
    }
    
    OH\_IPC\_MessageOption ipcOpt;
    ipcOpt.mode = OH\_IPC\_REQUEST\_MODE\_SYNC;
    ipcOpt.timeout = 0;
    ipcOpt.reserved = nullptr;
    int ret = OH\_IPCRemoteProxy\_SendRequest(ipcProxy\_, IPC\_ID\_ADD, data.get(), reply.get(), &ipcOpt);
    if (ret != OH\_IPC\_SUCCESS) {
        return result;
    }
    
    OH\_IPCParcel\_ReadInt32(reply.get(), &result);
    return result;
}

int32\_t IpcProxy::StartNativeChildProcess()
{
    if (ipcProxy\_ == nullptr) {
        return INT32\_MIN;
    }
    
    int32\_t result = INT32\_MIN;
    StdUniPtrIpcParcel data(OH\_IPCParcel\_Create(), OH\_IPCParcel\_Destroy);
    StdUniPtrIpcParcel reply(OH\_IPCParcel\_Create(), OH\_IPCParcel\_Destroy);
    if (data == nullptr || reply == nullptr) {
        return result;
    }
    
    if (!WriteInterfaceToken(data.get())) {
        return result;
    }
    
    OH\_IPC\_MessageOption ipcOpt;
    ipcOpt.mode = OH\_IPC\_REQUEST\_MODE\_SYNC;
    ipcOpt.timeout = 0;
    ipcOpt.reserved = nullptr;
    int ret = OH\_IPCRemoteProxy\_SendRequest(
        ipcProxy\_, IPC\_ID\_START\_NATIVE\_CHILD\_PROCESS, data.get(), reply.get(), &ipcOpt);
    if (ret != OH\_IPC\_SUCCESS) {
        return result;
    }
    
    OH\_IPCParcel\_ReadInt32(reply.get(), &result);
    return result;
}

bool IpcProxy::WriteInterfaceToken(OHIPCParcel\* data)
{
    return OH\_IPCParcel\_WriteInterfaceToken(data, interfaceToken\_) == OH\_IPC\_SUCCESS;
}

**Stub侧实现**

#include "IpcStub.h"
#include <IPCKit/ipc\_error\_code.h>
#include <cstring>
#include <new>

IpcStub::IpcStub()
{
    ipcStub\_ = OH\_IPCRemoteStub\_Create("NativeChildIPCStubSample",
        IpcStub::OnRemoteRequest, IpcStub::OnRemoteObjectDestroy, this);
}

IpcStub::~IpcStub()
{
    OH\_IPCRemoteStub\_Destroy(ipcStub\_);
}

OHIPCRemoteStub\* IpcStub::GetIpcStub()
{
    return ipcStub\_;
}

void IpcStub::OnRemoteObjectDestroy(void \*userData)
{
}

int IpcStub::OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData)
{
    if (userData == nullptr) {
        return OH\_IPC\_CHECK\_PARAM\_ERROR;
    }
    
    if (!CheckInterfaceToken(data)) {
        return OH\_IPC\_CHECK\_PARAM\_ERROR;
    }
    
    int ret;
    IpcStub \*thiz = reinterpret\_cast<IpcStub\*>(userData);
    switch (code) {
        case IPC\_ID\_REQUEST\_EXIT\_PROCESS:
            ret = thiz->HandleRequestExitChildProcess(data, reply);
            break;
        
        case IPC\_ID\_ADD:
            ret = thiz->HandleAdd(data, reply);
            break;
        
        case IPC\_ID\_START\_NATIVE\_CHILD\_PROCESS:
            ret = thiz->HandleStartNativeChildProcess(data, reply);
            break;
        
        default:
            ret = OH\_IPC\_CODE\_OUT\_OF\_RANGE;
            break;
    }
    
    return ret;
}

void\* IpcStub::OnIpcMemAlloc(int32\_t len)
{
    // limit ipc memory alloc size to 128 bytes
    if (len > 128) {
        return nullptr;
    }

    return new (std::nothrow) char\[len\];
}

void IpcStub::ReleaseIpcMem(void\* ipcMem)
{
    delete\[\] reinterpret\_cast<char\*>(ipcMem);
}

bool IpcStub::CheckInterfaceToken(const OHIPCParcel\* data)
{
    char \*token;
    int32\_t tokenLen;
    int ret = OH\_IPCParcel\_ReadInterfaceToken(data, &token, &tokenLen, IpcStub::OnIpcMemAlloc);
    if (ret != OH\_IPC\_SUCCESS) {
        return false;
    }
    
    bool tokenCheckRes = strcmp(token, interfaceToken\_) == 0;
    ReleaseIpcMem(token);
    return tokenCheckRes;
}

int IpcStub::HandleRequestExitChildProcess(const OHIPCParcel \*data, OHIPCParcel \*reply)
{
    int exitCode = 0;
    if (OH\_IPCParcel\_ReadInt32(data, &exitCode) != OH\_IPC\_SUCCESS) {
        return OH\_IPC\_PARCEL\_READ\_ERROR;
    }
    int32\_t ret = RequestExitChildProcess(exitCode) ? 1 : 0;
    return OH\_IPCParcel\_WriteInt32(reply, ret);
}

int32\_t IpcStub::HandleAdd(const OHIPCParcel \*data, OHIPCParcel \*reply)
{
    int32\_t a = 0;
    int32\_t b = 0;
    if (OH\_IPCParcel\_ReadInt32(data, &a) != OH\_IPC\_SUCCESS ||
        OH\_IPCParcel\_ReadInt32(data, &b) != OH\_IPC\_SUCCESS) {
        return OH\_IPC\_PARCEL\_READ\_ERROR;
    }
    
    int32\_t result = Add(a, b);
    if (OH\_IPCParcel\_WriteInt32(reply, result) != OH\_IPC\_SUCCESS) {
        return OH\_IPC\_PARCEL\_WRITE\_ERROR;
    }
    
    return OH\_IPC\_SUCCESS;
}

int IpcStub::HandleStartNativeChildProcess(const OHIPCParcel \*data, OHIPCParcel \*reply)
{
    int32\_t ret = StartNativeChildProcess();
    return OH\_IPCParcel\_WriteInt32(reply, ret);
}
