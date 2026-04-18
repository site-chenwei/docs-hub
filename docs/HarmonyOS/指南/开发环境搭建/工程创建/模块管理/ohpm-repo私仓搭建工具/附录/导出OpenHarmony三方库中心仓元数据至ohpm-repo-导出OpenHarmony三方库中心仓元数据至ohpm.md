---
title: "导出OpenHarmony三方库中心仓元数据至ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-metadata"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "附录"
  - "导出OpenHarmony三方库中心仓元数据至ohpm-repo"
captured_at: "2026-04-17T01:36:43.060Z"
---

# 导出OpenHarmony三方库中心仓元数据至ohpm-repo

支持通过export\_pkginfo和batch\_download命令，将OpenHarmony三方库中心仓中所有包批量导出，并能够通过batch\_publish命令将导出的库批量上传至部署的ohpm-repo实例中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Uzp49YJAT0y2KvgwQMwA1Q/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=5EA63579C0C2E1FBD9A698315B376007502C739A64FBCEF4CD8585147AAE208B)

开始执行下面的命令之前，请确保已经执行过ohpm-repo install和ohpm-repo start命令。

#### 获取所有已上架的包列表

使用[export\_pkginfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-pkginfo) 命令，导出OpenHarmony三方库中心仓已上架的包列表。

ohpm-repo export\_pkginfo --public-registry <OpenHarmony三方库中心仓registry地址> --http-proxy <可选配置代理地址>

执行结果

PS C:\\Users\\xxxxx\\Desktop> ohpm-repo export\_pkginfo  --public-registry https://ohpm.openharmony.cn/ohpm/
...
\[xxxx-xx-xxTxx:51:46.664\] \[INFO\] DEFAULT - Export 912 packages names success: save to "C:\\Users\\xxxxx\\Desktop\\pkgInfo\_1712069506662.json".

// pkgInfo\_1712069506662.json中记录着公仓的包列表
{
  "packageNameArray": \[
    "@ohos/lottie-turbo@1.0.0",
    "@ohos/lottie-turbo@1.0.0-rc.0",
    "@ohos/lottie-turbo@1.0.0-rc.1",
    ...
  \]
}

#### 批量下载三方包

执行[batch\_download](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-batch-download)命令将上一步生成的pkgInfo\_xxx.json文件中记录的包全部下载。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/2qbF8K4rQiCNZoQODGlxCg/notice_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=A609AE07B0189F6E23AA8A9363B2058DA863A0F873C6614664F0AC04443C6610)

若只需要下载中心仓的部分包，可以手动修改pkgInfo\_xxx.json文件，此时该命令只会批量下载pkgInfo\_xxx.json文件中指定的包。

ohpm-repo batch\_download <pkgInfo\_xxx.json文件地址> --public-registry <OpenHarmony三方库中心仓registry地址> --http-proxy <配置代理地址> --not-use-proxy <配置不使用代理>

执行结果

PS C:\\Users\\xxxxx\\Desktop> ohpm-repo batch\_download C:\\Users\\xxxxx\\Desktop\\pkgInfo\_1712069506662.json --public-registry https://ohpm.openharmony.cn/ohpm/
...
\[2024-04-02T23:16:59.217\] \[INFO\] default - A total of 912 package(s) successfully obtain download url.
\[2024-04-02T23:16:59.217\] \[INFO\] default - A total of 912 package(s) are successfully downloaded.
\[2024-04-02T23:16:59.217\] \[INFO\] default - A total of 912 package(s) are converted successfully.
\[2024-04-02T23:16:59.217\] \[INFO\] default - Packing the .zip file. . .
\[2024-04-02T23:16:59.475\] \[INFO\] default - save the .zip file to : "C:\\Users\\xxxxx\\Desktop\\batch\_download\_1712071006796.zip".

#### 批量上传

执行batch\_publish命令将上一步生成的batch\_download\_xxx.zip压缩包中全部包批量上传到ohpm-repo。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/ifLB_V99QSa3XrusmFCVbA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=D7521224EF8D2527ABB2F8F124E94E299523FAAE9CADCCD4AEA95827DB859B09)

1.  batch\_download\_xxx.zip文件中存在pkgInfo.json文件，其中记录了每个包的 文件名、包名、组织、上传者、Tag标签，用于在批量上传时准确指定ohpm-repo的数据库中某用户为某包的真实上传用户，同时将包的Tag标签一起上传。
2.  假设某个中心仓包的组织为A，如需为其指定ohpm-repo的数据库中某用户为其真实上传用户，但ohpm-repo实例中不存在A组织时，执行batch\_download命令后该包的真实上传用户将设定为空，并且提醒用户手动创建A组织。执行批量上传时，也会提醒A组织在ohpm-repo实例中不存在，需要先手动创建A组织。如果需要自动添加组织，使用batch\_publish命令的可选参数--force，将会选取一个管理员用户作为A组织负责人，自动创建A组织后进行该包的上传。
3.  从ohpm-repo 5.3.0版本开始，ohpm-repo支持配置多个仓库。通过batch\_download下载下来的包如果执行batch\_publish命令，默认上传到ohpm-repo仓库名为ohpm的仓库中，如果不存在仓库名为ohpm仓库，将报错，可通过batch\_publish的选项 --target-repo重新指定需要上传的仓库名。

ohpm-repo batch\_publish <batch\_download\_xxx.zip文件地址> --force

执行结果

PS C:\\Users\\xxxxx\\Desktop> ohpm-repo batch\_publish C:\\Users\\xxxxx\\Desktop\\batch\_download\_1712071006796.zip --force
...
\[xxxx-xx-xxTxx:50:29.100\] \[INFO\] default - all 912 package(s) are successfully published
\[xxxx-xx-xxTxx:50:29.101\] \[WARN\] default - You are using "filedb" to store data. If you have already started a repository service, please run \`ohpm-repo restart\` to restart the service.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/sfJNOriPQX-JhcYOoEjSfQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=98E38E0A03690160951F63C1E5299C89BAB1B9F011501C8F82E058A69596F06B)

如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo实例缓存中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。
