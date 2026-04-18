---
title: "使用NAPI扩展TS接口时，常用属性和实现接口的基本用法"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-21"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "使用NAPI扩展TS接口时，常用属性和实现接口的基本用法"
captured_at: "2026-04-17T02:02:59.923Z"
---

# 使用NAPI扩展TS接口时，常用属性和实现接口的基本用法

1.  env是使用NAPI的模块化编程，注册模块后，通过回调函数调用。
    
    static napi\_value CallNapi(napi\_env env, napi\_callback\_info info) { 
        size\_t argc = 1; 
        napi\_value object = nullptr; 
        napi\_status status; 
        status = napi\_get\_cb\_info(env, info, &argc, &object, nullptr, nullptr); 
        return object; 
    } 
    NAPI\_MODULE\_INIT() { 
        napi\_property\_descriptor desc\[\] = { 
            { "callNapi", nullptr, CallNapi, nullptr, nullptr, nullptr, napi\_default, nullptr } 
        }; 
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc); 
        return exports; 
    }
    
2.  实现回调：
    
    #include "napi/native\_api.h" 
    #include <assert.h> 
    static napi\_value NativeCall(napi\_env env, napi\_callback\_info info) { 
        size\_t argc = 1; 
        napi\_value args\[1\] = { nullptr }; 
        napi\_status status; 
        status = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
        assert(status == napi\_ok); 
        napi\_valuetype valuetype; 
        napi\_typeof(env, args\[0\], &valuetype); 
        if (valuetype != napi\_valuetype::napi\_function) { 
            napi\_throw\_type\_error(env, nullptr, "napi\_function is expected"); 
        } 
        napi\_value cb = args\[0\]; 
        napi\_value undefined; 
        status = napi\_get\_undefined(env, &undefined); 
        assert(status == napi\_ok); 
        napi\_value argv\[2\] = { nullptr }; 
        status = napi\_create\_int32(env, 1, &argv\[0\]); 
        assert(status == napi\_ok); 
        status = napi\_create\_int32(env, 2, &argv\[1\]); 
        assert(status == napi\_ok); 
        napi\_value result; 
        status = napi\_call\_function(env, undefined, cb, 2, argv, &result); 
        assert(status == napi\_ok); 
        return nullptr; 
    } 
    EXTERN\_C\_START 
    static napi\_value Init(napi\_env env, napi\_value exports) { 
        napi\_property\_descriptor desc\[\] = { 
            { "nativeCall", nullptr, NativeCall, nullptr, nullptr, nullptr, napi\_default, nullptr } 
        }; 
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc); 
        return exports; 
    } 
    EXTERN\_C\_END 
    static napi\_module module = { 
        .nm\_version = 1, 
        .nm\_flags = 0, 
        .nm\_filename = nullptr, 
        .nm\_register\_func = Init, 
        .nm\_modname = "callback", 
        .nm\_priv = nullptr, 
        .reserved = { 0 }, 
    }; 
    extern "C" \_\_attribute\_\_((constructor)) void RegisterCallbackModule(void) { 
        napi\_module\_register(&module); 
    }
    
3.  Promise实现参考：
    
    #include "napi/native\_api.h" 
    // Empty value so that macros here are able to return NULL or void 
    #define NAPI\_RETVAL\_NOTHING  // Intentionally blank 
    #define GET\_AND\_THROW\_LAST\_ERROR(env)                                                                    
        do {                                                                                               
            const napi\_extended\_error\_info\* errorInfo = nullptr;                                             
            napi\_get\_last\_error\_info((env), &errorInfo);                                                     
            bool isPending = false;                                                                          
            napi\_is\_exception\_pending((env), &isPending);                                                    
            if (!isPending && errorInfo != nullptr) {                                                        
                const char\* errorMessage =                                                                   
                    errorInfo->error\_message != nullptr ? errorInfo->error\_message : "empty error message";  
                napi\_throw\_error((env), nullptr, errorMessage);                                              
            }                                                                                                
        } while (0) 
    #define NAPI\_ASSERT\_BASE(env, assertion, message, retVal)                                     
        do {                                                                                      
            if (!(assertion)) {                                                                   
                napi\_throw\_error((env), nullptr, "assertion ("#assertion") failed:" message);  
                return retVal;                                                                    
            }                                                                                     
        } while (0) 
    #define NAPI\_ASSERT(env, assertion, message) NAPI\_ASSERT\_BASE(env, assertion, message, nullptr) 
    #define NAPI\_ASSERT\_RETURN\_VOID(env, assertion, message)  
            NAPI\_ASSERT\_BASE(env, assertion, message, NAPI\_RETVAL\_NOTHING) 
    #define NAPI\_CALL\_BASE(env, theCall, retVal)  
        do {                                      
            if ((theCall) != napi\_ok) {           
                GET\_AND\_THROW\_LAST\_ERROR((env));  
                return retVal;                    
            }                                     
        } while (0) 
    #define NAPI\_CALL(env, theCall) NAPI\_CALL\_BASE(env, theCall, nullptr) 
    #define NAPI\_CALL\_RETURN\_VOID(env, theCall) NAPI\_CALL\_BASE(env, theCall, NAPI\_RETVAL\_NOTHING) 
    struct AsyncData { 
        napi\_deferred deferred; 
        napi\_async\_work work; 
        int32\_t arg; 
        double retVal; 
    }; 
    double DoSomething(int32\_t val) { 
        if (val != 0) { 
            return 1.0 / val;  
        } 
        return 0; 
    } 
    void ExecuteCallback(napi\_env env, void\* data) { 
        AsyncData\* asyncData = reinterpret\_cast<AsyncData\*>(data); 
        asyncData->retVal = DoSomething(asyncData->arg); 
    } 
    void CompleteCallback(napi\_env env, napi\_status status, void\* data) { 
        AsyncData\* asyncData = reinterpret\_cast<AsyncData\*>(data); 
        napi\_value retVal; 
        if (asyncData->retVal == 0) { 
            NAPI\_CALL\_RETURN\_VOID(env, napi\_create\_string\_utf8(env, "arg can't be zero", NAPI\_AUTO\_LENGTH, &retVal)); 
            NAPI\_CALL\_RETURN\_VOID(env, napi\_reject\_deferred(env, asyncData->deferred, retVal)); 
        } else { 
            NAPI\_CALL\_RETURN\_VOID(env, napi\_create\_double(env, asyncData->retVal, &retVal)); 
            NAPI\_CALL\_RETURN\_VOID(env, napi\_resolve\_deferred(env, asyncData->deferred, retVal)); 
        } 
        NAPI\_CALL\_RETURN\_VOID(env, napi\_delete\_async\_work(env, asyncData->work)); 
        asyncData->work = nullptr; 
        asyncData->deferred = nullptr; 
        delete asyncData; 
    } 
    static napi\_value NativeCall(napi\_env env, napi\_callback\_info info) { 
        size\_t argc = 1; 
        napi\_value args\[1\] = { nullptr }; 
        NAPI\_CALL(env, napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr)); 
        int32\_t arg; 
        NAPI\_CALL(env, napi\_get\_value\_int32(env, args\[0\], &arg)); 
        // Create promise 
        napi\_deferred deferred; 
        napi\_value promise; 
        NAPI\_CALL(env, napi\_create\_promise(env, &deferred, &promise)); 
        AsyncData\* data = new AsyncData; 
        data->deferred = deferred; 
        data->arg = arg; 
        napi\_async\_work work; 
        napi\_value workName; 
        napi\_create\_string\_utf8(env, "promise", NAPI\_AUTO\_LENGTH, &workName); 
        NAPI\_CALL(env, napi\_create\_async\_work(env, nullptr, workName,ExecuteCallback, CompleteCallback, data, &work)); 
        data->work = work; 
        NAPI\_CALL(env, napi\_queue\_async\_work(env, work)); 
        return promise; 
    } 
    EXTERN\_C\_START 
    static napi\_value Init(napi\_env env, napi\_value exports) { 
        napi\_property\_descriptor desc\[\] = { 
            { "nativeCall", nullptr, NativeCall, nullptr, nullptr, nullptr, napi\_default, nullptr } 
        }; 
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc); 
        return exports; 
    } 
    EXTERN\_C\_END 
    static napi\_module demoModule = { 
        .nm\_version = 1, 
        .nm\_flags = 0, 
        .nm\_filename = nullptr, 
        .nm\_register\_func = Init, 
        .nm\_modname = "promise", 
        .nm\_priv = nullptr, 
        .reserved = { 0 }, 
    }; 
    extern "C" \_\_attribute\_\_((constructor)) void RegisterPromiseModule(void) { 
        napi\_module\_register(&demoModule); 
    }
    
4.  使用libuv：直接导入[libuv](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/libuv)库。
