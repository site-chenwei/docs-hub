---
title: "如何正确使用OH_JSVM_GetValueStringUtf8获取字符串"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-5"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "JSVM"
  - "如何正确使用OH_JSVM_GetValueStringUtf8获取字符串"
captured_at: "2026-04-17T02:03:02.741Z"
---

# 如何正确使用OH\_JSVM\_GetValueStringUtf8获取字符串

**问题现象**

1.  OH\_JSVM\_GetValueStringUtf8 中传入的缓冲区大小不确定。
2.  使用 OH\_JSVM\_GetValueStringUtf8 获取超长字符串时可能会导致崩溃。

**解决措施**

函数 OH\_JSVM\_GetValueStringUtf8 的第三个参数用于指定字符串写入的内存地址。如果传入空指针，接口会通过最后一个参数 result 返回字符串的长度（不包含终止符）。

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringUtf8(JSVM\_Env env,
                                                   JSVM\_Value value,
                                                   char\* buf,
                                                   size\_t bufsize,
                                                   size\_t\* result);

获取字符串可分为以下三步：

1.  调用接口获取字符串长度；
2.  申请buffer内存空间；
3.  调用接口获取字符串。
    
    std::string GetValueString(JSVM\_Env env, JSVM\_Value value) {
        constexpr size\_t PREALLOC\_SIZE = 256;
        char preallocMemory\[PREALLOC\_SIZE\];
    
    
        char \*buff = preallocMemory;
        
        // Obtain length
        size\_t totalLen = 0;
        OH\_JSVM\_GetValueStringUtf8(env, value, nullptr, 0, &totalLen);
        size\_t needed = totalLen + 1;
    
    
        if (needed > PREALLOC\_SIZE) {
            // Allocate space, size must include termination character
            buff = new char\[needed\];
        }
        // get string
        OH\_JSVM\_GetValueStringUtf8(env, value, buff, needed, nullptr);
    
    
        std::string ret(buff, totalLen);
    
    
        if (needed > PREALLOC\_SIZE) {
            delete\[\] buff;
        }
        return ret;
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/t_zEvt3PTeS2lQCwjQzfgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=809CB72ACE01E5B5F7AB2A83E4A9F73428572BCA1876F0D8EB487150373C3254)

1.  分配的 buffer 大小必须大于字符串长度，因为字符串长度不包含最后的终止字符。如果 buffer 的大小等于字符串长度，字符串的最后一个字符将被终止字符覆盖。
2.  不建议直接在栈上使用 \`char buff\[totalLen + 1\]\` 分配空间，因为当字符串长度过大时，可能会导致栈溢出，从而引发应用崩溃。
