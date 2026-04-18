---
title: "GetAddr"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-memblock-getaddr"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "MemBlock"
  - "GetAddr"
captured_at: "2026-04-17T01:36:34.476Z"
---

# GetAddr

#### 函数功能

-   获取只读的device内存地址。
    
-   获取可读写的device内存地址。
    

#### 函数原型

-   获取只读的device内存地址场景：
    
    ```cpp
    const void *GetAddr() const
    ```
    
-   获取可读写的device内存地址场景：
    
    ```cpp
    void *GetAddr()
    ```
    

#### 参数说明

无

#### 返回值

-   获取只读的device内存地址场景：
    
    | 类型 | 描述 |
    | :-- | :-- |
    | void\* | 只读的device内存地址。 |
    
-   获取可读写的device内存地址场景：
    
    | 类型 | 描述 |
    | :-- | :-- |
    | void\* | 可读写的device内存地址。 |
    

#### 异常处理

无

#### 约束说明

无
