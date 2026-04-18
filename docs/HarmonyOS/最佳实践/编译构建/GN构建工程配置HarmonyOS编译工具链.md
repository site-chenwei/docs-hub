---
title: "GN构建工程配置HarmonyOS编译工具链"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-gn-adapts-to-harmonyos"
menu_path:
  - "最佳实践"
  - "编译构建"
  - "GN构建工程配置HarmonyOS编译工具链"
captured_at: "2026-04-17T01:54:20.122Z"
---

# GN构建工程配置HarmonyOS编译工具链

#### 概述

本文将介绍如何在GN工程中配置HarmonyOS工具链，然后通过HarmonyOS工具链编译出可以在HarmonyOS环境下使用的三方库。

HarmonyOS编译子系统是以GN和Ninja构建为基座，对构建和配置粒度进行部件化抽象、对内建模块进行功能增强、对业务模块进行功能扩展的系统，该系统提供以下基本功能：

-   以部件为最小粒度拼装产品和独立编译。
-   支持轻量、小型、标准三种系统的解决方案级版本构建，以及用于支撑应用开发者使用DevEco Studio开发的SDK开发套件的构建。
-   支持芯片解决方案厂商的灵活定制和独立编译。

**Ninja：**是一个专注于快速编译的小型构建系统。

**GN：**Generate Ninja的缩写，用于产生Ninja文件。

#### 编译环境配置

1.  Linux编译环境搭建（如果已有对应版本的Linux开发环境，可跳过Linux环境搭建过程）：详细指导见以下链接。
    
    [使用 WSL 在 Windows 上安装 Linux](https://learn.microsoft.com/zh-cn/windows/wsl/install)。
    
    [Ubuntu分发版本获取及安装说明](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual)。
    
    编译环境目前主要支持Ubuntu18.04和Ubuntu20.04。
    
2.  HarmonyOS SDK镜像下载：
    
    从HarmonyOS官网门户选择Linux版本的Command Line Tools下载即可。
    
    [下载链接](https://developer.huawei.com/consumer/cn/download/)。
    
3.  安装构建工具depot\_tools并添加到环境变量。
    
    任意位置创建工作目录depot\_tools，cd到自己创建的目录，拉取工具（需要网络环境）：
    
    ```screen
    mkdir depot_tools
    cd depot_tools
    git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
    ```
    
    将depot\_tools的路径加到环境变量中：
    
    编辑.bashrc文件将depot\_tools路径信息加到最后一行。
    
    ```screen
    vi ~/.bashrc                                    
    ```
    
    在.bashrc文件的最后添加下面一行代码。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/_NflEYOOT9KYADr0VN9xbA/zh-cn_image_0000002229335705.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=0E412AEB08C3BEFE0E8C9BAACD38A7D224DEBF94B2E42611B73E663E794E908C "点击放大")
    
    ```screen
    export PATH="$PATH:/xxx/depot_tools"
    ```
    
    此处需配置绝对路径信息，例如这里创建的本地路径是/mnt/d/my\_code/depot\_tools，故此处配置如上图。
    
    刷新环境变量使其生效：
    
    ```screen
    source ~/.bashrc 
    ```
    
4.  使用GN需要Python环境，安装Python环境。
    
    ```screen
    sudo apt update
    sudo apt install python
    ```
    
    直接输入指令sudo apt install python可能会安装失败，需要先输入sudo apt update更新一下可用包的最新列表。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/eXufo7pQSdCQt3wC9mVviQ/zh-cn_image_0000002193850372.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=0BAD8AFEBF52391ABF9EA8931D6F66D805BFAEDDB0266942226903C70B204401 "点击放大")
    
    判断python是否安装成功：
    
    输入python显示python版本即可。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/MSDbCqQBSqWIOi9CaXTBRw/zh-cn_image_0000002194009932.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=F87514DA0C8DE5AA8DB52D71E4712E08F8EE807D1AFF16FF7ADA7CF950DEF2BE)
    

#### GN构建工程适配流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/YuEZwcfITomblNkNWDez9Q/zh-cn_image_0000002229335737.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=860560A632929EF1102866A543C21E0A7D9020202E1DA3C0C0D809CD5D6B5FF8 "点击放大")

1.  新增HarmonyOS平台的宏定义。
2.  配置HarmonyOS平台的工具链核心信息，涵盖clang工具链路径，sysroot系统根目录以及clang版本等关键参数。
3.  在toolchain目录下，为各架构分别配置对应的ohos\_clang\_toolchain。
4.  扩充gcc\_toolchain模版功能，补充HarmonyOS启动引导程序所需的.o文件相关配置。
5.  设置HarmonyOS编译参数，重点配置基础编译选项、宏定义等核心内容。
6.  在BUILD.gn文件的各架构平台分支逻辑中，新增HarmonyOS平台对应的分支配置；对于暂未适配HarmonyOS的三方库，可暂时沿用Linux分支的编译配置。

#### webRTC适配案例

本文将通过webRTC的GN构建工程案例来对上一章节的流程进行实操讲解。WebRTC (Web Real-Time Communications) 是一项实时通讯技术，它允许网络应用或者站点，在不借助中间媒介的情况下，建立浏览器之间点对点（Peer-to-Peer）的连接，实现视频流和（或）音频流或者其他任意数据的传输。下面了解下如何通过GN构建工程将webRTC适配到HarmonyOS系统上。

三方库获取地址：[下载链接](https://gitee.com/openharmony/build)。

#### \[h2\]适配流程

1.  **添加HarmonyOS平台宏定义**
    
    这里主要在build/config/BUILDCONFIG.gn文件中适配HarmonyOS的default\_compiler\_configs和\_default\_toolchain。在GN工程里面，BUILDCONFIG.gn是第一位被解析的，里面定义的变量相当于全局变量，可以被后续所有的.gn文件使用。编译过程中可能会配置一些编译选项以及一些头文件搜索路径。default\_compiler\_configs指向的文件里面会包括一些默认的编译选项以及头文件搜索路径等等。\_default\_toolchain指向了一个工具链相关的函数。具体修改点如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/fg1K1aL0T4OT5k6uSDM1CA/zh-cn_image_0000002229335693.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=46730D00B229F28B897A0AC0C9F44168EA842D31327D3F4A271BFACD99FF3EFD "点击放大")
    
2.  **设置HarmonyOS平台clang工具链相关路径**
    
    不同平台的工具链会有一些差别，所以需要使用HarmonyOS的工具链。这里主要修改config/clang/clang.gni文件。.gni文件类似于GN的头文件，会被import到各个.gn文件中使用其定义的一些变量。该文件中的核心修改点在于配置指向HarmonyOS SDK的工具链路径。另外还需修改clang\_use\_chrome\_plugins的值为false，HarmonyOS中默认clang\_use\_chrome\_plugins值为false，不设置可能会报错find-bad-constructs文件找不到。
    
    此处ohos\_sdk\_native\_root的值需要对应修改为自己本地HarmonyOS SDK中的native的路径。具体修改点如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/JaGC5T9qQyCOEHL5-i5bZg/zh-cn_image_0000002193850288.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=32BB48693740373DAA1416683096475C251CCEA5F3F8AB2E8540C56457572FB8 "点击放大")
    
3.  **设置HarmonyOS平台sysroot路径**
    
    这里主要修改build/config/sysroot.gni文件，sysroot里面包含了许多头文件搜索路径，配置了sysroot之后，编译过程中会去该目录下搜索需要的头文件。SDK里面会提供大量的头文件，这些头文件都会放在sysroot目录下，所以需要引入HarmonyOS对应的sysroot。具体修改点如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/tegqrqe9SUCw_BfOOtvf4A/zh-cn_image_0000002194009944.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=9B00E57986B05369C2EFD25E4F70E6494C168A10ED50EEF16FA05ACBCC72A8C3 "点击放大")
    
4.  **修改HarmonyOS平台clang版本**
    
    这里主要修改build/toolchain/toolchain.gni文件，在该文件中配置HarmonyOS对应的clang版本号。具体修改点如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/YV2AXh9TSuOSi0jL4ILKGA/zh-cn_image_0000002193850284.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=02B98E099D848F438CAEC4DC2E2461C8425A71A138E628A9C2F2A293FFE03F0E "点击放大")
    
5.  **设置各个架构的ohos\_clang\_toolchain**
    
    这里主要是在build/toolchain路径下新建一个ohos/BUILD.gn文件，用于配置ohos\_clang\_toolchain，里面主要配置了HarmonyOS用于启动引导程序的.o文件。同时设置HarmonyOS不同架构(主要包括ohos\_clang\_arm、ohos\_clang\_arm64、ohos\_clang\_x86\_64)的ohos\_clang\_toolchain配置信息。具体添加内容如下：
    
    ```screen
    import("//build/config/sysroot.gni")
    import("//build/toolchain/gcc_toolchain.gni")
    
    declare_args() {
      # Whether unstripped binaries, i.e. compiled with debug symbols, should be
      # considered runtime_deps rather than stripped ones.
      ohos_unstripped_runtime_outputs = true
      ohos_extra_cflags = ""
      ohos_extra_cppflags = ""
      ohos_extra_cxxflags = ""
      ohos_extra_asmflags = ""
      ohos_extra_ldflags = ""
    }
    
    # The ohos clang toolchains share most of the same parameters, so we have this
    # wrapper around gcc_toolchain to avoid duplication of logic.
    #
    # Parameters:
    #  - toolchain_root
    #      Path to cpu-specific toolchain within the ndk.
    #  - sysroot
    #      Sysroot for this architecture.
    #  - lib_dir
    #      Subdirectory inside of sysroot where libs go.
    #  - binary_prefix
    #      Prefix of compiler executables.
    template("ohos_clang_toolchain") {
      gcc_toolchain(target_name) {
        assert(defined(invoker.toolchain_args),
               "toolchain_args must be defined for ohos_clang_toolchain()")
        toolchain_args = invoker.toolchain_args
        toolchain_args.current_os = "ohos"
    
        # Output linker map files for binary size analysis.
        enable_linker_map = true
    
        ohos_libc_dir =
            rebase_path(invoker.sysroot + "/" + invoker.lib_dir, root_build_dir)
        libs_section_prefix = "${ohos_libc_dir}/Scrt1.o"
        libs_section_prefix += " ${ohos_libc_dir}/crti.o"
        libs_section_postfix = "${ohos_libc_dir}/crtn.o"
    
        if (invoker.target_name == "ohos_clang_arm") {
          abi_target = "arm-linux-ohos"
        } else if (invoker.target_name == "ohos_clang_arm64") {
          abi_target = "aarch64-linux-ohos"
        } else if (invoker.target_name == "ohos_clang_x86_64") {
          abi_target = "x86_64-linux-ohos"
        }
    
        clang_rt_dir =
            rebase_path("${clang_lib_path}/${abi_target}/nanlegacy",
                        root_build_dir)
        print("ohos_libc_dir :", ohos_libc_dir)
        print("clang_rt_dir :", clang_rt_dir)
        solink_libs_section_prefix = "${ohos_libc_dir}/crti.o"
        solink_libs_section_prefix += " ${clang_rt_dir}/clang_rt.crtbegin.o"
        solink_libs_section_postfix = "${ohos_libc_dir}/crtn.o"
        solink_libs_section_postfix += " ${clang_rt_dir}/clang_rt.crtend.o"
    
        _prefix = rebase_path("${clang_base_path}/bin", root_build_dir)
        cc = "${_prefix}/clang"
        cxx = "${_prefix}/clang++"
        ar = "${_prefix}/llvm-ar"
        ld = cxx
        readelf = "${_prefix}/llvm-readobj"
        nm = "${_prefix}/llvm-nm"
        if (!is_debug) {
          strip = rebase_path("${clang_base_path}/bin/llvm-strip", root_build_dir)
          use_unstripped_as_runtime_outputs = ohos_unstripped_runtime_outputs
        }
        extra_cflags = ohos_extra_cflags
        extra_cppflags = ohos_extra_cppflags
        extra_cxxflags = ohos_extra_cxxflags
        extra_asmflags = ohos_extra_asmflags
        extra_ldflags = ohos_extra_ldflags
      }
    }
    
    ohos_clang_toolchain("ohos_clang_arm") {
      sysroot = "${sysroot}"
      lib_dir = "usr/lib/arm-linux-ohos"
      toolchain_args = {
        current_cpu = "arm"
      }
    }
    
    ohos_clang_toolchain("ohos_clang_arm64") {
      sysroot = "${sysroot}"
      lib_dir = "usr/lib/aarch64-linux-ohos"
      toolchain_args = {
        current_cpu = "arm64"
      }
    }
    
    ohos_clang_toolchain("ohos_clang_x86_64") {
      sysroot = "${sysroot}"
      lib_dir = "usr/lib/x86_64-linux-ohos"
      toolchain_args = {
        current_cpu = "x86_64"
      }
    }
    ```
    
6.  **扩充原本的gcc\_toolchain模版功能**
    
    主要修改/build/toolchain/gcc\_toolchain.gni文件。GN工程里面默认会配置gcc\_toolchain，里面会包括一些tool，例如tool("cc")、tool("cxx")、tool("tolink")等等，编译不同的内容时调用其对应的配置项。这里主要是需要修改tool("solink")、tool("solink\_module")中的rspfile\_content配置以及tool("link")中的link\_comand配置。需要在gcc\_toolchain.gni中template("gcc\_toolchain")下添加几个参数（libs\_section\_prefix、libs\_section\_postfix 、solink\_libs\_section\_prefix、solink\_libs\_section\_postfix ）的识别。这几个参数是指向了上一步骤中配置的用于启动引导程序的.o文件。这些参数会在需要修改的rspfile\_content、link\_comand参数中用到。具体修改如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/zzRcLpg3TXmkDzbRPtQang/zh-cn_image_0000002194009884.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=8D6E06BB49F8A79BBBD40A0CB6B064131C8F74F07EF1ECCA7DFC7901D9625D71 "点击放大")
    
    修改tool("solink")和tool("solink\_module")中的rspfile\_content为rspfile\_content = "-Wl,--whole-archive {{inputs}} {{solibs}} -Wl,--no-whole-archive $solink\_libs\_section\_prefix {{libs}} $solink\_libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。具体修改如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/n7jguenyRFOSsI46i5ja6Q/zh-cn_image_0000002193850312.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=9E94B4DB4DD455ED0843593859ECB7BAB0717A5FEC396EA7533713991A855329 "点击放大")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/zokpgEheQLC4dUlGoUuPYw/zh-cn_image_0000002194009912.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=3162CBE45CB570C564C7A64E41E176F33D1EE3DB841204A77BD988B16AD581E3 "点击放大")
    
    修改tool("link")中link\_command为link\_command = "$ld {{ldflags}}${extra\_ldflags} -o \\"$unstripped\_outfile\\" $libs\_section\_prefix $start\_group\_flag @\\"$rspfile\\" {{solibs}} {{libs}} $end\_group\_flag $libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/dmQHvWmnSVeUnQ3iUXM6AA/zh-cn_image_0000002229335741.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=EFFD46841AD200DAE176A3B7E5FB218FDC41AD9AEBCE70722224E4F7F3747B71 "点击放大")
    
7.  **设置HarmonyOS的一些编译参数，将其加入到BUILDCONFIG.gn中**
    
    这里需要在build/config路径下新建一个ohos/BUILD.gn文件，该文件主要是定义了一个config("compiler")，该config会被注册到所有的编译目标，该config里面主要设置了基础的编译选项、宏定义等。
    
    此处ohos\_clang\_base\_path 的值需要对应修改为自己本地HarmonyOS SDK中的llvm的路径。具体添加内容如下：
    
    ```screen
    import("//build/config/sysroot.gni")
    assert(is_ohos)
    
    ohos_clang_base_path = "/mnt/d/ohos/ohos-sdk/linux/native/llvm"
    ohos_clang_version = "15.0.4"
    
    if (is_ohos) {
      if (current_cpu == "arm") {
        abi_target = "arm-linux-ohos"
      } else if (current_cpu == "x86") {
        abi_target = ""
      } else if (current_cpu == "arm64") {
        abi_target = "aarch64-linux-ohos"
      } else if (current_cpu == "x86_64") {
        abi_target = "x86_64-linux-ohos"
      } else {
        assert(false, "Architecture not supported")
      }
    }
    
    config("compiler") {
      cflags = [
        "-ffunction-sections",
        "-fno-short-enums",
        "-fno-addrsig",
      ]
    
      cflags += [
        "-Wno-unknown-warning-option",
        "-Wno-int-conversion",
        "-Wno-unused-variable",
        "-Wno-misleading-indentation",
        "-Wno-missing-field-initializers",
        "-Wno-unused-parameter",
        "-Wno-c++11-narrowing",
        "-Wno-unneeded-internal-declaration",
        "-Wno-undefined-var-template",
        "-Wno-implicit-int-float-conversion",
      ]
      defines = [
        # The NDK has these things, but doesn't define the constants to say that it
        # does. Define them here instead.
        "HAVE_SYS_UIO_H",
      ]
    
      defines += [
        "OHOS",
        "__MUSL__",
        "_LIBCPP_HAS_MUSL_LIBC",
        "__BUILD_LINUX_WITH_CLANG",
        "__GNU_SOURCE",
        "_GNU_SOURCE",
      ]
    
      ldflags = [
        "-Wl,--no-undefined",
        "-Wl,--exclude-libs=libunwind_llvm.a",
        "-Wl,--exclude-libs=libc++_static.a",
    
        # Don't allow visible symbols from libraries that contain
        # assembly code with symbols that aren't hidden properly.
        # http://crbug.com/448386
        "-Wl,--exclude-libs=libvpx_assembly_arm.a",
      ]
    
      cflags += [ "--target=$abi_target" ]
      include_dirs = [
        "${sysroot}/usr/include/${abi_target}",
        "${ohos_clang_base_path}/lib/clang/${ohos_clang_version}/include",
      ]
    
      ldflags += [ "--target=$abi_target" ]
    
      # Assign any flags set for the C compiler to asmflags so that they are sent
      # to the assembler.
      asmflags = cflags
    }
    ```
    
8.  **build/config/compiler/BUILD.gn中增加对is\_ohos的判断**
    
    保证可以正确走HarmonyOS支持的编译分支。这里主要是为了防止clang版本号校验失败导致异常。具体修改如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/_cj6PEqyR_uL_dXQ-1zsXw/zh-cn_image_0000002194009888.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=7D52F000B727A66A1D09D749389046D70ABF52CFE842381C4B5D9E22105E96F9 "点击放大")
    
9.  **未适配HarmonyOS的三方库走linux编译配置**
    
    当前部分三方库还未适配HarmonyOS，涉及到时可以先走linux的编译配置，例如：需要获取config.h文件时。
    
    修改modules/video\_capture的BUILD.gn。具体修改如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/k2k6E_qtTJWw35BfgosIWA/zh-cn_image_0000002193850356.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=EC3832AE3029F252772074300496452551BC03FC80C07B149D0F24C42D12054D "点击放大")
    
    修改third\_party/zlib的BUILD.gn。具体修改如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/EpR0WhmVQhekluRIDBiNuQ/zh-cn_image_0000002194009896.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=756BD2A2FB652DA89CD609BA26B9EC71C17F7913F8E72ADB5E40BB745CD07218 "点击放大")
    
    修改third\_party/libevent中的BUILD.gn。HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。具体修改如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/ou78Y9wcQ3uesJ2czyaFRQ/zh-cn_image_0000002194009900.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=4D9ECC2F248C62CE664B704115B2F779CE6BAEB9D54E02920145300122F64148 "点击放大")
    
10.  **编译**
     
     先通过GN命令生成对应的ninja文件，然后使用ninja编译命令进行编译。
     
     ```screen
     gn gen ../out/xxx --args='is_clang=true target_os="ohos" target_cpu="arm64" xxx'  
     ninja -v -C ../out/xxx ${target_name} -j16 
     ```
     
     可以根据需要在编译指令中添加对应参数信息。
     
     查看具体编译命令：
     
     可以在gn gen命令中添加--ninja-args="-v -dkeeprsp"用于查看具体编译命令，这个命令将会在编译过程中打印详细的编译命令，并且保留编译过程中生成的rsp文件。
     
     查看一个目标被谁依赖：
     
     例如gn refs out/intermediate/arm64\_72 //pc:rtc\_pc\_base。这个命令将显示与目标//pc:rtc\_pc\_base相关的所有依赖项并列出所有引用了该目标的其他目标或文件。
     

#### \[h2\]常见问题总结

在对webRTC的GN工程进行HarmonyOS工具链适配过程中，遇到了一些常见问题场景。下面针对这些问题做一个具体分析。

1.  **Assertion failed. Unsupported ARM OS**
    
    **问题详情：**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/oqgrZ-uGRiKOCSqAeXDwzA/zh-cn_image_0000002193850336.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=6CB58FD33BA1965D6E47C3922B51FE5FBF95ADBCC02E349B809E9233883DFC06)
    
    **问题原因/解决措施：**
    
    三方库内部没有做对is\_ohos的判断，导致走到错误分支。当前很多业务模块还未适配HarmonyOS，暂时可以走linux分支以保证正常编译。
    
    **具体修改：**
    
    修改third\_party/zlib的BUILD.gn文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/843bJefiR3KKKsJk0QPuTw/zh-cn_image_0000002229335729.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=BA46B51B2E65A5FAD47D380F8C32590790347CB08F12C969FAABCD5EA85E202D "点击放大")
    
2.  **python找不到pkg-config文件：No such file or directory: 'pkg-config'**
    
    **问题详情：**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Oysp5hRUQT6JEi6iAL5j0w/zh-cn_image_0000002194009922.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=67BD9EAD63495E5548FD4DB3AFDE22DFA01E876981AB04BB36EE13CD9F6D4F30 "点击放大")
    
    **问题原因/解决措施：**
    
    缺少pkg-config插件，安装该插件。
    
    **具体指令：**
    
    ```screen
    sudo apt-get install pkg-config
    ```
    
3.  **Unknown command line argument '-split-threshold-for-reg-with-hint=0'**
    
    **问题详情：**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kngt61xzTSy1noYE4INdtw/zh-cn_image_0000002194009908.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=3E56263A24BDF94496A8C1BF25F7E034150F18814C747F64CEFE6774AF8BD1C0 "点击放大")
    
    **问题原因/解决措施：**
    
    编译过程中会提示部分配置不识别，需要将这些配置项删除。
    
    **具体修改：**
    
    在build/config/compiler/BUILD.gn中删除以下配置。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Ub4kqSitR1-wfyN0FBiU0g/zh-cn_image_0000002229335753.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=42F4566FB3177B6F88749D7C933602317E780F9B122833DCF3F1C0982060798B "点击放大")
    
4.  **WARN类型导致的ERROR**
    
    **问题详情：**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/L8JKOIEPRF6tmUihf5PsIQ/zh-cn_image_0000002229335717.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=0EF54CCF97DD058B2CB4938942E4F2636B5683FB4F2A0FACDBC115D50CD7882D "点击放大")
    
    **问题原因/解决措施：**
    
    编译器驱动程序有时（很少）会在调用之前发出警告。实际的链接器需要确保这些警告是否也被视为致命错误。为了避免编译中出现因警告而造成出错，可以添加编译参数treat\_warnings\_as\_errors = false，或者去除config(treat\_warnings\_as\_errors)中配置的“-Werror”，详情如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/KtGvTt2iRYKjtHiS9IqeeA/zh-cn_image_0000002193850296.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=E8DB20F41C263768FA94CF4F76BC0887E28775A672FC0C0539C4939438AE235E "点击放大")
    
    **具体修改：**
    
    -   添加编译指令配置项treat\_warnings\_as\_errors （建议使用）
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/WE4l7UtaRtuD3MO_6PX0GA/zh-cn_image_0000002193850360.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=CE26FB14CEAA48578E5F65FB1B1FBAFA71D3BA9B0D205487D0C4E442114A7CB3 "点击放大")
        
    -   修改源代码，在build/config/compiler/BUILD.gn中删除以下配置。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/tfk2SBhdSq-kvJgXC7FDMw/zh-cn_image_0000002193850368.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=BD16D04C4D56DA124A26233FDF4DBB6D70AAC4A68A2E4B809C039BCBDDC14EF6 "点击放大")
        
5.  **error: reinterpret\_cast from 'pthread\_t' (aka 'unsigned long') to 'rtc::PlatformThreadId' (aka 'int') is not allowed**
    
    **问题详情：**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Fle3tcseTu2a6qwacg8odw/zh-cn_image_0000002229450217.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=E08F79A27CD156A4064A6BC90A4543FB94EB99AD83237A937CB7E00B0261C793 "点击放大")
    
    **问题原因/解决措施：**
    
    rtc\_base/platform\_thread\_types.cc未识别到is\_ohos导致内部走错分支导致异常。目前HarmonyOS支持的接口是gettid()，rtc\_base/platform\_thread\_types.cc需要识别到is\_ohos然后调用gettid()。由于当前很多业务模块还未进行识别，暂时需要走linux分支，故需要保留linux的定义。
    
    **具体修改：**
    
    -   首先需要在根目录的BUILD.gn中配置识别HarmonyOS系统的变量is\_ohos：
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/rhYFHshYTUqxTeCwfQhzZQ/zh-cn_image_0000002229450213.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=4F136F3CD9E7809147CC0685E618BBBA29A306AF7857384E3B20840F0B2169ED "点击放大")
        
    -   修改rtc\_base/platform\_thread\_types.cc业务代码：
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/4gvlN9waR1ugDcTs-Ev1EQ/zh-cn_image_0000002193850300.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=66DDDFB96E3A046485551C8906CAF266BCDDB70393924CAD545ADC19868DFFA7 "点击放大")
        
6.  **fatal error: 'config.h' file not found**
    
    **fatal error: 'sys/queue.h' file not found**
    
    **问题详情：**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/SZ8Z7Q9oTJG-wpCwPynreQ/zh-cn_image_0000002229335681.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=75594B1802895D6ADFBB573E090B160501E18631055B33312806A7FF0CE2DCA5 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/5lHuIRqySo-b7LiH6Pw1Mg/zh-cn_image_0000002193850352.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=6DA29825F9A1D0929995102BF083ED4A46016A1C39C67DCC86019669942A6CEF "点击放大")
    
    **问题原因/解决措施：**
    
    找不到config.h头文件，libevent尚未适配HarmonyOS，需要添加is\_ohos的判断并走linux的文件路径寻找config.h。
    
    找不到'sys/queue.h'文件，HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。
    
    **具体修改：**
    
    修改third\_party/libevent中的BUILD.gn。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/6iBkprxjQaW4aoVIFbaJYw/zh-cn_image_0000002193850376.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=3EF35B60C3A5DE7119A42E676E2666AE5FE038EC3FC9ACE56B7FDCDE8FAF2D8A "点击放大")
