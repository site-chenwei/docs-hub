---
title: "SDK使用指南 - Java SDK使用说明"
source_url: "https://open.pinduoduo.com/application/document/browse?idStr=7E28519022C8E799"
menu_path:
  - "基础文档"
  - "开发文档"
  - "SDK使用指南"
captured_at: "2026-04-10T09:20:16.788Z"
---

# SDK使用指南

更新时间：2022-03-25 11:43:46

#### 

**SDK概述**

为了提高开发者的效率，拼多多开放平台SDK提供了用户授权、授权码刷新、接口访问、消息接收等功能

#### 

**环境依赖**

Plain Text

JAVA SDK 需要依赖Jave SE/EE 1.7及以上

目前官方仅支持JAVA版本SDK

#### 

**如何下载**

-   注册成为拼多多开放平台开发者身份，申请并创建完成所需的应用
    
-   进入控制台，选择应用，在开发者工具中进入SDK下载界面
    
-   点击「生成SDK」，生成成功后即可自动生成并下载，也可点击重新生成获取最新的SDK
    

![](https://t16img.yangkeduo.com/perse-open-api/2020-12-24/53d9b918-da71-4b73-b18f-d07f61e4ee94.png)

（下载SDK）

注意事项：

-   Java版本的sdk包含两个包，一个jar可以直接导入工程中使用，第二个是源码包
    
-   开发者只能通过SDK访问该应用拥有的权限包下所有接口，对无访问权限的接口仍无法调用成功 
    

## 

Java SDK使用说明

### 

环境依赖

-   Java SE/EE 1.7及以上（不支持Android平台）
    

### 

使用示例

获取access\_token

Java收起

PopAccessTokenClient client \= new PopAccessTokenClient(

                clientId,

                clientSecret);

AccessTokenResponse accessTokenResponse \= client.generate(code);

刷新access\_token

Java收起

PopAccessTokenClient client \= new PopAccessTokenClient(

                clientId,

                clientSecret);

AccessTokenResponse accessTokenResponse \= client.refresh(refreshToken);

API调用（以pdd.order.list.get为例）

Java收起

PopClient client \= new PopHttpClient(

                clientId,

                clientSecret);

PddOrderListGetRequest request \= new PddOrderListGetRequest();

request.setRefundStatus(refundStatus);

request.setOrderStatus(orderStatus);

request.setStartConfirmAt(startConfirmAt);

request.setEndConfirmAt(endConfirmAt);

request.setPage(page);

request.setPageSize(pageSize);

try {

    //同步调用

    PddOrderListGetResponse response \= client.syncInvoke(request,accessToken);

    //异步调用

    Future<PddOrderListGetResponse> futureResponse \= client.asyncInvoke(request,accessToken);

} catch (Exception e){

    System.out.println(e);

}

消息客户端

Java收起

WsClient ws \= new WsClient(

        clientId,

        clientSecret,

        new MessageHandler() {

            public void onMessage(Message message) throws InterruptedException {

                System.out.println("receive message: " + message);

            }

        });

ws.connect();

### 

服务地址

开放平台网关API服务地址

https://gw-api.pinduoduo.com/api/router

方舟网关API服务地址

https://ark-api.pinduoduo.com/ark/router

文件网关API服务地址

https://gw-upload.pinduoduo.com/api/upload

消息服务地址

wss://message-api.pinduoduo.com

SDK中已经默认设置了以上地址。

#### 

服务域名灾备

为了防止主域名失效，SDK 内部新增了备用服务地址。并支持主动切换与自动切换（全局生效，无需每个PopHttpClient都调用一次）。默认情况下 未开启自动切换，并使用主域名。

使用方式如下：

Java收起

// 开启主备域名自动切换

PopHttpClient.startAutoDomainSwitch();

// 关闭主备域名自动切换

PopHttpClient.stopAutoDomainSwitch();

// 手动启用备域名

// 若已开启自动切换，则此时自动切换会失效

PopHttpClient.enableBackupDomain();

// 取消手动启用备域名，并恢复到使用主域名

// 若开启过自动切换，则自动切换会恢复

PopHttpClient.disableBackupDomain();

### 

其他功能

用户可以通过修改默认的HttpClientConfig自定义Http客户端配置，默认配置如下：

Java收起

// 连接配置

private int connectionTimeoutMillis \= 5000;

private int socketTimeoutMillis \= 5000

private int connectionRequestTimeout \= 1000;

// 异步请求线程池配置

private int maxParallel \= 10;

private long threadKeepAliveTime \= 30;

// connectionManager配置

private int maxTotal \= 50;

private int defaultMaxPerRoute \= 20;

设置方法

Java收起

HttpClientConfig config \= HttpClientConfig.getDefault();

config.setConnectionTimeoutMillis(2000);

config.setSocketTimeoutMillis(2000);

config.setConnectionRequestTimeout(1000);

PopClient client \= new PopHttpClient(

                clientId,

                clientSecret,

                config);

注意事项

-   PopHttpClient是线程安全的，所以没有必要每次API请求都新建一个PopHttpClient
    
-   WsClient支持心跳重连，心跳发送间隔为10秒钟，心跳超时时间为3分钟
    
-   PopHttpClient的配置项connectionTimeoutMillis、socketTimeoutMillis、connectionRequestTimeout设置有最大值，超出最大值的设置将不生效，最大值设置为：
    
    -   connectionTimeoutMillis: 5000ms
        
    -   socketTimeoutMillis: 5000ms
        
    -   connectionRequestTimeout: 1000ms
        
    

本页目录：

Java SDK使用说明

环境依赖

使用示例

服务地址

其他功能
