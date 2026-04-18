---
title: "如何在Native侧集成三方库Curl，并进行HTTP数据请求"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-31"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何在Native侧集成三方库Curl，并进行HTTP数据请求"
captured_at: "2026-04-17T02:03:01.965Z"
---

# 如何在Native侧集成三方库Curl，并进行HTTP数据请求

可以将Curl移植到HarmonyOS，并在Native侧开发时直接使用Curl的C++库实现。具体的移植方法请参考相关链接。

具体使用步骤如下：

1.  将移植后的Curl的so库放入Native工程的entry/libs/arm64-v8a/目录，将包含头文件的include目录放入entry/src/main/cpp目录。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/YsYRK9zxRj2SpimROcBojw/zh-cn_image_0000002194158760.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=9313AAC9949C591EA5F8CDC3F7574FEF8BA1694F447E1F9DDB6EF6BF9CA580AE "点击放大")
    
2.  在CMakeLists.txt文件中链接Curl对应的so库。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/XoVmXD28Thuo_lOcvfsrFQ/zh-cn_image_0000002194158764.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=990F7C1517E03D9A114BA868A3D3A29B0A4078B5969C3B4BC5D976603C24CADE "点击放大")
    
3.  在Native侧的.cpp文件中引入头文件curl.h，使用Curl的相关能力。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Y276lFsSSGqSLEQ4a7AJ3g/zh-cn_image_0000002229758629.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=930EB52733DBAF588DA023D51E7D1138A1784EC499549F680D938F2F5F855764 "点击放大")
    
    具体可参考以下代码：
    
    #include "curl/curl.h"
    
    // ...
    
    // Get request and post request data response functions
    size\_t ReqReply(void \*ptr, size\_t size, size\_t nmemb, void \*userdata) {
        string \*str = reinterpret\_cast<string \*>(userdata);
        (\*str).append((char \*)ptr, size \* nmemb);
        return size \* nmemb;
    }
    
    // http GET Request configuration
    CURLcode CurlGetReq(const std::string &url, std::string &response) {
        // Curl initialization
        CURL \*curl = curl\_easy\_init();
        // Curl return value
        CURLcode res;
        if (curl) {
            // Set the request header for Curl
            struct curl\_slist \*headers = NULL;
            headers = curl\_slist\_append(headers, "Content-Type:application/json");
            curl\_easy\_setopt(curl, CURLOPT\_HTTPHEADER, headers);
    
            // Set the URL address for the request
            curl\_easy\_setopt(curl, CURLOPT\_URL, url.c\_str());
    
            // Receive response header data, 0 represents not receiving, 1 represents receiving
            curl\_easy\_setopt(curl, CURLOPT\_HEADER, 1);
    
            // Set data receiving function
            curl\_easy\_setopt(curl, CURLOPT\_WRITEFUNCTION, ReqReply);
            curl\_easy\_setopt(curl, CURLOPT\_WRITEDATA, (void \*)&response);
    
            // Set to not use any signal/alarm handlers
            curl\_easy\_setopt(curl, CURLOPT\_NOSIGNAL, 1);
    
            // Set timeout period
            curl\_easy\_setopt(curl, CURLOPT\_CONNECTTIMEOUT, 10);
            curl\_easy\_setopt(curl, CURLOPT\_TIMEOUT, 10);
    
            // Open request
            res = curl\_easy\_perform(curl);
        }
        // Release curl
        curl\_easy\_cleanup(curl);
        return res;
    }
    
    
    static napi\_value NatReq(napi\_env env, napi\_callback\_info info) {
        string getUrlStr = "http://app.huawei.com";
        string getResponseStr;
        auto res = CurlGetReq(getUrlStr, getResponseStr);
        if (res == CURLE\_OK) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "pure", "response: \\n%{public}s", getResponseStr.c\_str());
        }
    
        // ...
    }
    

结果展示

终端使用curl指令获取的网站信息一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/NPghjXF6QyWRmyFpuIK1Mw/zh-cn_image_0000002229604137.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=AE7D4B5348EFE589E224BAEF8E84DD27677AD6DA7DBB34ADEE17BD85B245244E "点击放大")

**参考链接**

[使用命令行CMake构建NDK工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-cmake)

[使用lycium工具快速编译三方库](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lycium-adapts-to-harmonyos)
