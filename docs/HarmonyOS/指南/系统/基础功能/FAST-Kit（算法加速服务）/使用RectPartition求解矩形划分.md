---
title: "使用RectPartition求解矩形划分"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-rect-partition"
menu_path:
  - "指南"
  - "系统"
  - "基础功能"
  - "FAST Kit（算法加速服务）"
  - "使用RectPartition求解矩形划分"
captured_at: "2026-04-17T01:35:55.476Z"
---

# 使用RectPartition求解矩形划分

矩形划分求解器（Rectangular Partition Solver）用于解决矩形划分问题。其接收若干个彼此不相交的矩形作为输入（主要关注这些矩形共同定义的区域的并集），计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少（但不保证最优）。形如下方示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/8e9i15AhTtOd_qzix07iuA/zh-cn_image_0000002538179324.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=4D3A43974DAA85FA107D6C4CCF8763520AD4BCF07D7D24A7CD2F0A3C972AE3AE)

其相关定义如下：一个矩形![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/yhTT3LtsTpmY-2-8KuW31w/zh-cn_image_0000002569019111.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=EAD2D34488CCE32EF7BFD5F5E394E468E5A096BEED05D580F0EC377454F648DE)为二维网格内横纵坐标满足![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/JKxV5g6zQZeO4Cl68AAoDA/zh-cn_image_0000002568899101.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=E0EB7C0DF1A10B47DEB6F3654ED0D918039C8CBC7DBBF554D3F0B4E17FBAA28A)的所有单元矩形构成的集合（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。两个矩形相交，当且仅当它们共享至少一个公共的单元矩形。

在矩形划分问题（Rectangular Partition Problem）中，给定N个彼此不相交的矩形，要求输出M个矩形，使其满足如下几点：

-   输出的M个矩形彼此不相交。
    
-   输出的M个矩形的并集与输入的N个矩形的并集完全相同。
    
-   输出的矩形数量M尽可能少。
    

矩形划分求解器运行的时间复杂度为 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/q3Z1fQnwTrKMc1ZIbpGW_g/zh-cn_image_0000002538019396.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=7A649F9E6C38009467ED5449B3F95B0B89E5B203A0A271450377D2A70E385F05)，可以高效处理大规模输入数据。在网格数据处理和空间几何计算等优化场景中，可以使用矩形划分求解器提升区域处理效率，减少冗余空间。

#### 接口说明

具体API说明详见[接口文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)。

| 名称 | 描述 |
| :-- | :-- |
| FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_errorcode-1) [HMS\_FAST\_RectPartition\_CreateConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_createconfig) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*\*config) | 创建矩形划分求解器的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_destroyconfig) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*config) | 销毁矩形划分求解器的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_errorcode-1) [HMS\_FAST\_RectPartition\_SetAlgo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_setalgo) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*config, const char \*name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Ow_DWl9GQ-eLb9IWF_-2Ug/zh-cn_image_0000002538179326.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=8809687AD211EB17104F31FC2B976A6B3FE32233E38582C10DA55D99E58EC72C)。 |
| FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_errorcode-1) [HMS\_FAST\_RectPartition\_Solve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_solve) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*config, size\_t size, const [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) \*origin, [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) \*result, size\_t \*resultSize) | 
在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。

**说明**：

1\. 输入须保证矩形两两不相交（即任意两个矩形满足：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/9qugZCWvS0efnnDaoDg4ng/zh-cn_image_0000002569019113.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=E0B6D23B1A0FE91E3EF880BE84F4627694DE73831723917066CD33A53805F4E6) 或 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/gGW6_UhTTHmEEslmj0mJNw/zh-cn_image_0000002568899103.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=47289F6A279B2FD2666F683F14EB4E2DF33AAAF0D587E83CE729BB357472447B)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/85VyvyyrQDG7irylxt1xkw/zh-cn_image_0000002538019398.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=083D93E10E34618D0D981CC9F1251C77E836B0775ED85388DA06FBC38C4FBCF8)或 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/cqudZOfSQU6qAIygeVgnqg/zh-cn_image_0000002538179328.png?HW-CC-KV=V1&HW-CC-Date=20260417T013557Z&HW-CC-Expire=86400&HW-CC-Sign=0DAEDABB2A7368C859446E46D44467B4D94672277DA2522C4ED28CFD7B34517D)），否则函数返回FAST\_ERROR\_CODE\_ILLEGAL\_INPUT。

2\. 函数能保证输出矩形的数量小于等于输入矩形的数量。

 |

#### 开发步骤

1.  首先在CMake脚本中链接相关动态库。
    
    ```cmake
    target_link_libraries(entry PUBLIC libfast_ads.so)
    ```
    
2.  调用HMS\_FAST\_RectPartition\_CreateConfig生成矩形划分求解器配置实例（FAST\_RectPartitionConfig）。
    
3.  调用HMS\_FAST\_RectPartition\_SetAlgo设置求解算法为“SweepLineAlgo”（扫描线算法）。
    
4.  调用HMS\_FAST\_RectPartition\_Solve计算矩形划分方案。
    
5.  调用HMS\_FAST\_RectPartition\_DestroyConfig销毁矩形划分求解器配置实例。
    

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_solver_rect_partition.h"

// 定义一个函数来打印矩形
void print_rect(const FAST_Rect* rect) {
    printf("Rect: left=%d, top=%d, right=%d, bottom=%d\n",
           rect->left, rect->top, rect->right, rect->bottom);
}

FAST_ErrorCode rect_partition_demo() {
    // 定义输入矩形
    FAST_Rect origin[] = {
        {1, 4, 1, 6},
        {2, 1, 2, 6},
        {3, 1, 3, 3}
    };
    size_t size = sizeof(origin) / sizeof(FAST_Rect);

    // 定义输出矩形
    FAST_Rect* result = (FAST_Rect*)malloc(size * sizeof(FAST_Rect));
    size_t result_size = 0;

    FAST_RectPartitionConfig* config = nullptr;
    FAST_ErrorCode ret;

    do {
        // 创建配置
        ret = HMS_FAST_RectPartition_CreateConfig(&config);
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("Failed to create config: %d\n", ret);
            break;
        }

        // 设置算法
        ret = HMS_FAST_RectPartition_SetAlgo(config, "SweepLineAlgo");
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("Failed to set algorithm: %d\n", ret);
            break;
        }

        // 计算矩形划分方案
        ret = HMS_FAST_RectPartition_Solve(config, size, origin, result, &result_size);
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("Failed to solve: %d\n", ret);
            break;
        }

        // 打印结果
        printf("Resulting rectangles(result_size=%ld):\n", result_size);
        for (size_t i = 0; i < result_size; ++i) {
            print_rect(&result[i]);
        }
        /*
            Resulting rectangles(result_size=2):
            Rect: left=1, top=4, right=2, bottom=6
            Rect: left=2, top=1, right=3, bottom=3
        */

    } while (0);

    // 销毁配置
    HMS_FAST_RectPartition_DestroyConfig(config);

    // 释放数组
    free(result);

    return ret;
}
```
