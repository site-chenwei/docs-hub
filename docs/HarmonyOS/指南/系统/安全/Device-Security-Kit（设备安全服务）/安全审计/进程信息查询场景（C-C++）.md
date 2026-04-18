---
title: "进程信息查询场景（C/C++）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-queryproc-c"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Device Security Kit（设备安全服务）"
  - "安全审计"
  - "进程信息查询场景（C/C++）"
captured_at: "2026-04-17T01:35:50.325Z"
---

# 进程信息查询场景（C/C++）

#### 场景介绍

从6.0.0(20) 开始，新增提供应用进程信息查询接口，可以获取设备上已启动的应用进程信息。进程信息包括进程ID、指令命令行、父进程PID、用户ID、用户组ID、进程启动时间、进程所有者ID类型、进程所有者ID等相关信息。

#### 约束和限制

1.  当前能力仅支持2in1设备。
    
2.  支持单次输入要查询的进程数最大限制为16个。
    

#### 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/JfDLOagOT5uqAu8MuqLtjA/zh-cn_image_0000002569019049.png?HW-CC-KV=V1&HW-CC-Date=20260417T013552Z&HW-CC-Expire=86400&HW-CC-Sign=0F3F745F3DCCA4135AC67A44DBF9E3B6233BA9AEEC33A6B6DFB5864BF95C28D6)

**流程说明：**

1.  用户在hap应用上调用查询接口获取应用进程信息。
    
2.  Device Security Kit接口同步返回应用进程信息给hap应用，hap应用根据返回的应用进程信息进行业务处理。
    

#### 接口说明

接口如下表，更多接口及使用方法请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_queryallprocesses)。

| 接口名 | 描述 |
| :-- | :-- |
| int32\_t HMS\_SecurityAudit\_QueryAllProcesses(char\*\* result) | 获取所有的应用进程信息。 |
| int32\_t HMS\_SecurityAudit\_QueryProcesses(uint64\_t\* pids, uint64\_t count, char\*\* result) | 获取输入的pid的应用进程信息。 |

#### 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/I1-bEQmqS_aeu7iu0zNcqQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013552Z&HW-CC-Expire=86400&HW-CC-Sign=25EB1D61152273867F19CE422431930A406B30AE6647C91CA68459524897F357)

-   在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT。
    
-   只允许清单内的企业类应用申请该权限，申请方式请参考：[申请使用企业类应用可用权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-enterprise-apps)。
    

1.  在CMakeLists.txt中导入安全审计共享库，并链接该库。
    
    ```cmake
    find_library(dsm-lib libsecurityaudit_ndk.z.so)
    target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
    ```
    
2.  导入安全审计的头文件。
    
    ```cpp
    #include <DeviceSecurityKit/security_audit.h>
    #include <cstdio>
    ```
    
3.  开发者根据实际场景，获取单个或所有应用进程信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/GMEkTE8ZRDu6PbgcqiTHHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013552Z&HW-CC-Expire=86400&HW-CC-Sign=7BC70F6AF27B02E63D451DCB32C0BD721F15315FACB150545B43D2CBF154CF32)
    
    应用在根据应用进程信息进行业务处理后，需要释放查询接口出入参的内存。
    
    -   调用HMS\_SecurityAudit\_QueryProcesses接口，获取单个应用进程信息。
        
        ```cpp
        char *result = nullptr;
        uint64_t pids[] = {3266};
        int32_t ret = HMS_SecurityAudit_QueryProcesses(pids, sizeof(pids)/sizeof(pids[0]), &result);
        if (ret == 0 && result != nullptr) {
            printf("HMS_SecurityAudit_QueryProcesses result: %s\n", result);
        } else {
            printf("HMS_SecurityAudit_QueryProcesses failed with error: %d\n", ret);
        }
        if (result != nullptr) {
            delete[] result;
            result = nullptr;
        }
        ```
        
    -   调用HMS\_SecurityAudit\_QueryAllProcesses接口，获取所有的应用进程信息。
        
        ```cpp
        char *result = nullptr;
        int32_t ret = HMS_SecurityAudit_QueryAllProcesses(&result);
        if (ret == 0 && result != nullptr) {
            printf("HMS_SecurityAudit_QueryAllProcesses result: %s\n", result);
        } else {
            printf("HMS_SecurityAudit_QueryAllProcesses failed with error: %d\n", ret);
        }
        if (result != nullptr) {
            delete[] result;
            result = nullptr;
        }
        ```
