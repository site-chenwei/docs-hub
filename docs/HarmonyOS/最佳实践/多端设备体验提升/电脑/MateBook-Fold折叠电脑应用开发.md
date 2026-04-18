---
title: "MateBook Fold折叠电脑应用开发"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-mate-book-fold"
menu_path:
  - "最佳实践"
  - "多端设备体验提升"
  - "电脑"
  - "MateBook Fold折叠电脑应用开发"
captured_at: "2026-04-17T01:54:16.963Z"
---

# MateBook Fold折叠电脑应用开发

#### 概述

HarmonyOS折叠电脑MateBook Fold，凭借其独特的折叠设计、全屏触控和[虚拟键盘](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-pc-0000002322600098#虚拟键盘)的交互方式，融合了一体机、笔记本和平板三种设备的使用体验，在形态创新与交互体验方面有所提升。除了具备传统电脑的功能特性外，这款折叠电脑还具备以下核心亮点：

1.  设备形态：支持五种使用形态：半折叠态（唤起全尺寸键盘）、半折叠态（关闭全尺寸键盘）、横向展开态、竖向展开态、外接显示器。
2.  交互设计：在半折叠态下，上下两块屏幕均可独立操作。用户可以通过点击桌面右下角的键盘图标或使用多指（八指及以上）轻触屏幕来唤起全尺寸键盘，从而实现传统电脑的操作体验。
3.  屏幕显示方向：在半折叠态下，屏幕仅支持一种显示方向，不支持旋转。而在展开态下，屏幕支持三种显示方向（[display.Orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#orientation10)）：横屏（1-LANDSCAPE）、反向横屏（3-LANDSCAPE\_INVERTED）和竖屏（0-PORTRAIT），并且始终支持旋转功能，无法关闭。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/seeLh4KGSCmeIcp89kRdeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015418Z&HW-CC-Expire=86400&HW-CC-Sign=648781D97108DC522CE0F4EF67A84BA93C554E104FD7760A1C530D0D8122FBD0)

当磁吸键盘贴附在下屏时，设备进入半折叠态（唤起全尺寸键盘），此时下屏无法使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/V5onPisXQp-oXMPSljdLqw/zh-cn_image_0000002419750993.png?HW-CC-KV=V1&HW-CC-Date=20260417T015418Z&HW-CC-Expire=86400&HW-CC-Sign=1A0AF2F8F8A5273A0A088DDCEFBF8AE232AC8CBD62E729669F0E6AFAEAAAE1AE "点击放大")

#### 硬件说明

#### \[h2\]屏幕规格信息

折叠电脑在不同折叠状态下具有不同的分辨率、屏幕宽度等属性：

-   在半折叠态（关闭全尺寸键盘）下，设备拥有上下两个屏幕，其中上屏的displayId为0，下屏的displayId为999。而在半折叠态（唤起全尺寸键盘）和展开态下，仅显示displayId为0的屏幕。
-   折叠电脑底部工具栏高度固定为118px，但在不同折叠电脑形态下，工具栏占用的宽度和位置不同，屏幕可用宽高（[availableWidth/availableHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#属性)）也会有所不同。
-   折叠电脑外接显示器时，会自动进入横向展开态布局，且屏幕方向为反向横屏，此时折叠电脑默认作为主显示器（displayId为0），外接屏幕作为副显示器（displayId与接入的端口有关）。可使用[getWindowProperties()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9)方法获取当前窗口的属性[WindowProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#windowproperties)，其中displayId为当前窗口所在屏幕的ID，从而可判断当前窗口所在的显示器。

**半折叠态屏幕规格信息**

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.5.1.8.1.1" valign="top"><p><a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#属性" target="_blank">屏幕旋转角度（rotation）</a></p></th><td align="center" class="cellrowborder" colspan="3" valign="top"><p>0(0度)</p></td><td align="center" class="cellrowborder" valign="top"><p>1(90度)</p></td><td align="center" class="cellrowborder" valign="top"><p>2(180度)</p></td><td align="center" class="cellrowborder" valign="top"><p>3(270度)</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.2.1" valign="top"><p>设备形态</p></th><td align="center" class="cellrowborder" valign="top"><p>半折叠态（唤起全尺寸键盘）</p></td><td align="center" class="cellrowborder" colspan="2" valign="top"><p>半折叠态（关闭全尺寸键盘）</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.3.1" valign="top"><p>半折叠态效果图</p></th><td align="center" class="cellrowborder" valign="top"><p><span><img height="336.1575" originheight="1166" originwidth="1384" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Gd1IL_RORZKIYqf4ZMT6uw/zh-cn_image_0000002386231824.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E1130105386000900FB68F085CDD7B0B5008D72AC173F4AD8897ABD38474A35" title="点击放大" width="399"></span></p></td><td align="center" class="cellrowborder" colspan="2" valign="top"><p><span><img height="349.27130000000005" originheight="1166" originwidth="1332" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/4R9QAC-bQ1Gh_y9-FCnhsA/zh-cn_image_0000002419631173.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8885EF86D35B16930414569C72EEED70199898EF7CA23D1A1BAD6DEBD30E97E4" title="点击放大" width="399"></span></p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.4.1" valign="top"><p><a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#orientation10" target="_blank">屏幕方向Orientation</a></p></th><td align="center" class="cellrowborder" colspan="3" valign="top"><p>竖屏PORTRAIT</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.5.1" valign="top" width="14.285714285714285%"><p>屏幕ID</p></th><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>displayId：0</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>displayId：0</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>displayId：999</p></td><td align="center" class="cellrowborder" valign="top" width="13.985804258722384%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.6.1" valign="top" width="14.285714285714285%"><p>分辨率（px）</p></th><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>2472*1608</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>2472*1608</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>2472*1606</p></td><td align="center" class="cellrowborder" valign="top" width="13.985804258722384%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.7.1" valign="top" width="14.285714285714285%"><p>分辨率（vp）向下取整</p></th><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>1373*893</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>1373*893</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>1373*892</p></td><td align="center" class="cellrowborder" valign="top" width="13.985804258722384%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.8.1" valign="top" width="14.285714285714285%"><p>屏幕可用宽高（px）</p></th><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>2472*1490（底部工具栏高度118px）</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>2472*1608</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>2472*1488（底部工具栏高度118px）</p></td><td align="center" class="cellrowborder" valign="top" width="13.985804258722384%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.9.1" valign="top" width="14.285714285714285%"><p>屏幕可用宽高（vp）向下取整</p></th><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>1373*827</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>1373*893</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>1373*826</p></td><td align="center" class="cellrowborder" valign="top" width="13.985804258722384%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.5.1.8.10.1" valign="top" width="14.285714285714285%"><p><a href="https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout#section1532120147301" target="_blank">横纵断点</a></p></th><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>横向断点lg，纵向断点sm</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>横向断点lg，纵向断点sm</p></td><td align="center" class="cellrowborder" valign="top" width="14.385684294711588%"><p>横向断点lg，纵向断点sm</p></td><td align="center" class="cellrowborder" valign="top" width="13.985804258722384%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="14.285714285714285%"><p>NA</p></td></tr></tbody></table>

**展开态屏幕规格信息**

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.7.1.7.1.1" valign="top"><p><a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#属性" target="_blank">屏幕旋转角度（rotation）</a></p></th><td align="center" class="cellrowborder" valign="top"><p>0(0度)</p></td><td align="center" class="cellrowborder" valign="top"><p>1(90度)</p></td><td align="center" class="cellrowborder" valign="top"><p>2(180度)</p></td><td align="center" class="cellrowborder" colspan="2" valign="top"><p>3(270度)</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.2.1" valign="top" width="14.618538146185381%"><p>设备形态</p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>竖向展开态</p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>横向展开态</p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p>横向展开态</p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p>外接显示器</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.3.1" valign="top" width="14.618538146185381%"><p>展开态效果图</p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p><span><img height="476.72520000000003" originheight="1444" originwidth="1128" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/RxJxaDs6QnyPnKykqJN3xA/zh-cn_image_0000002386071936.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBB580EDD6AAA669142A93CB060C087B8B4C038E25D14EFF33BED11F71D5384E" title="点击放大" width="372.40000000000003"></span></p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p><span><img height="327.5923" originheight="1150" originwidth="1494" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ELCbpadpT3CpMZZCVLlzew/zh-cn_image_0000002419751005.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C954FACDD4D6AFBCD31592B91A3868E3B570BA64CFCFCEFF21B5E91B4FB354CF" title="点击放大" width="425.6"></span></p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p><span><img height="327.5923" originheight="1150" originwidth="1494" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Wbjr1URkQF6wu-DQpcq1PQ/zh-cn_image_0000002386231864.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B5AC7C7FC46E2DDF69886BF31CC550826EC9A7C6D0C1A8867F941C456E81003" title="点击放大" width="425.6"></span></p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p><span><img height="255.9984" originheight="598" originwidth="1864" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/tyIer4UyQKuIpeURvEbXiw/zh-cn_image_0000002419631209.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4267BC743298E3713410B28E6EEF9733621C3C6BE1D4625696E2E054AD6C1EA" title="点击放大" width="798"></span></p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.4.1" valign="top"><p><a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#orientation10" target="_blank">屏幕方向Orientation</a></p></th><td align="center" class="cellrowborder" valign="top"><p>竖屏PORTRAIT</p></td><td align="center" class="cellrowborder" valign="top"><p>横屏LANDSCAPE</p></td><td align="center" class="cellrowborder" valign="top"><p>NA</p></td><td align="center" class="cellrowborder" colspan="2" valign="top"><p>反向横屏LANDSCAPE_INVERTED</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.5.1" valign="top" width="14.618538146185381%"><p>屏幕ID</p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>displayId：0</p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>displayId：0</p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p>displayId：0</p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p>主显示器：displayId为0</p><p>外接显示器：displayId与接入的端口有关</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.6.1" valign="top" width="14.618538146185381%"><p>分辨率（px）</p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>2472*3296</p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>3296*2472</p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p>3296*2472</p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p>3296*2472</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.7.1" valign="top" width="14.618538146185381%"><p>分辨率（vp）向下取整</p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>1373*1831</p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>1831*1373</p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p>1831*1373</p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p>1831*1373</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.8.1" valign="top" width="14.618538146185381%"><p>屏幕可用宽高（px）</p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>2472*3178（底部工具栏高度118px）</p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>3296*2354（底部工具栏高度118px）</p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p>3296*2354（底部工具栏高度118px）</p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p>3296*2354（底部工具栏高度118px）</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.9.1" valign="top" width="14.618538146185381%"><p>屏幕可用宽高（vp）向下取整</p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>1373*1765</p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>1831*1307</p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p>1831*1307</p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p>1831*1307</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.7.1.7.10.1" valign="top" width="14.618538146185381%"><p><a href="https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout#section1532120147301" target="_blank">横纵断点</a></p></th><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>横向断点lg，纵向断点lg</p></td><td align="center" class="cellrowborder" valign="top" width="17.998200179982003%"><p>横向断点xl，纵向断点sm</p></td><td align="center" class="cellrowborder" valign="top" width="8.819118088191182%"><p>NA</p></td><td align="center" class="cellrowborder" valign="top" width="12.31876812318768%"><p>横向断点xl，纵向断点sm</p></td><td align="center" class="cellrowborder" valign="top" width="28.247175282471748%"><p>横向断点xl，纵向断点sm</p></td></tr></tbody></table>

**常用接口**

-   获取屏幕对象相关接口
    
    [Display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)对象中包含屏幕宽高，屏幕可用区域宽高等重要信息，对应的Display区域如下图所示。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/CYgn_IvhQQKhtYGscT9ZnA/zh-cn_image_0000002386071972.png?HW-CC-KV=V1&HW-CC-Date=20260417T015418Z&HW-CC-Expire=86400&HW-CC-Sign=932B5B011FCF0014D910605F5107FE4E637CEF5B519DCF8DAA3BDEC7CA73AFE9 "点击放大")
    
    | 
    API
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    [display.getAllDisplays()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetalldisplays9)
    
     | 
    
    获取所有的Display对象。不同设备形态下对应的Display区域如上图所示。
    
     |
    | 
    
    [display.getDisplayByIdSync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdisplaybyidsync12)
    
     | 
    
    根据displayId获取对应的Display对象。具体的displayId可参考[屏幕规格信息](#section05491630111312)表格中屏幕ID行。
    
    除半折叠态（关闭全尺寸键盘）分为上下两屏，上屏displayId为0，下屏displayId为999，其余状态折叠电脑屏幕的displayId均为0。
    
     |
    | 
    
    [display.getDefaultDisplaySync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9)
    
     | 
    
    获取当前默认的Display对象。除半折叠态（关闭全尺寸键盘）获取的Display对象为displayId为0的上屏，其余设备形态下获取的Display区域如上图所示。
    
     |
    | 
    
    [display.getPrimaryDisplaySync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetprimarydisplaysync14)
    
     | 
    
    获取主屏信息。对于折叠电脑，当外接屏幕时，获取的是当前主屏幕的Display对象；当没有外接屏幕时，获取的是设备自带屏幕中displayId为0的Display对象。
    
     |
    | 
    
    [display.on('add'|'remove'|'change')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displayonaddremovechange)
    
     | 
    
    开启显示设备新增、移除、变化的监听。
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/2qHJjy7zT4O7b2-OywzPRA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015418Z&HW-CC-Expire=86400&HW-CC-Sign=F57068FCFF56142434EBDC40079B3E482D5F2C510F264A5F4F86850F2AD0F2C5)
    
    -   display.on('add'|'remove'|'change')触发场景如下：
        -   display.on('add')触发场景：半折叠态（唤起全尺寸键盘）->半折叠态（关闭全尺寸键盘）、外接显示器。
        -   display.on('change')触发场景：涉及Display变化时，包括折叠状态、屏幕方向，可用区域变化等。
        -   display.on('remove')触发场景：半折叠态（关闭全尺寸键盘）->半折叠态（唤起全尺寸键盘）、展开态、取消外接显示器。
    

#### \[h2\]其他硬件信息

折叠电脑相机预设了默认的[镜头安装角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#相机镜头安装角度)。使用时，需考虑镜头角度与设备的旋转角度，具体定义可参考[预览旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#预览旋转角度)。当屏幕方向一致时，前置镜头角度与需设置的预览流旋转角度如下，不同设备状态下的相机参数保持一致。

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.3.1.5.1.1" valign="top" width="16.8%"><p>屏幕旋转角度（rotation）</p></th><td align="center" class="cellrowborder" valign="top" width="28.849999999999998%"><p>0(0度)</p></td><td align="center" class="cellrowborder" valign="top" width="27.93%"><p>1(90度)</p></td><td align="center" class="cellrowborder" valign="top" width="26.419999999999998%"><p>3(270度)</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.3.1.5.2.1" valign="top" width="16.8%"><p>示意图</p></th><td align="center" class="cellrowborder" valign="top" width="28.849999999999998%"><p style="color: rgb(255,0,0);"><span><img height="520.5753000000001" originheight="1109" originwidth="850" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/jofj4j8fSOGKgmWY6DjgSQ/zh-cn_image_0000002419751053.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F123FF9857E879C30FDCC0003707CFB36D74B92D15BB51DE3C67861F84C4110" title="点击放大" width="399"></span></p><p style="color: rgb(255,0,0);"><span><img height="329.9331" originheight="855" originwidth="1034" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/u1aBeIB_TB60yX2Skzc2Qw/zh-cn_image_0000002386231868.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF90CE8BAE2A740F4215EB72AAC1516E47170081A5CEAFFCD9145271A51124A4" title="点击放大" width="399"></span></p></td><td align="center" class="cellrowborder" valign="top" width="27.93%"><p style="color: rgb(255,0,0);"><span><img height="305.8202" originheight="850" originwidth="1109" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/eKP1dDH_QpKQgRc6ZciMWQ/zh-cn_image_0000002419631221.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08AC9467696A62DD8BFA248EEF28D684911E345CBBBA5A7367481C84182D4215" title="点击放大" width="399"></span></p></td><td align="center" class="cellrowborder" valign="top" width="26.419999999999998%"><p style="color: rgb(255,0,0);"><span><img height="305.8202" originheight="850" originwidth="1109" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/m-jk4mEaQqCyUPNvTk3Bgg/zh-cn_image_0000002386071992.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EBE1CB23CAD162FE5FC4CF1D3DC408E08537BE943DE8A94ECBC6BC8826B4ED7" title="点击放大" width="399"></span></p></td></tr><tr><th class="firstcol" id="mcps1.3.4.3.1.5.3.1" valign="top" width="16.8%"><p>前置相机镜头角度</p></th><td align="center" class="cellrowborder" valign="top" width="28.849999999999998%"><p>270°</p></td><td align="center" class="cellrowborder" valign="top" width="27.93%"><p>270°</p></td><td align="center" class="cellrowborder" valign="top" width="26.419999999999998%"><p>270°</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.3.1.5.4.1" valign="top" width="16.8%"><p>预览旋转角度</p></th><td align="center" class="cellrowborder" valign="top" width="28.849999999999998%"><p>270°+0°=270°</p></td><td align="center" class="cellrowborder" valign="top" width="27.93%"><p>270°+90° = 0°</p></td><td align="center" class="cellrowborder" valign="top" width="26.419999999999998%"><p>270°+270° = 180°</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.3.1.5.5.1" valign="top"><p>后置相机镜头角度</p></th><td align="center" class="cellrowborder" colspan="3" valign="top"><p>无后置相机</p></td></tr></tbody></table>

#### \[h2\]设备特有能力

折叠电脑具备独特的折叠功能，在不同折叠状态下展现出不同的特性，具体如下：

1.  折叠时，折叠电脑进入睡眠状态，应用无法获取当前的折叠状态（[display.FoldStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#foldstatus10)）；半折叠时，折叠状态为FOLD\_STATUS\_HALF\_FOLDED；展开时，折叠状态为FOLD\_STATUS\_EXPANDED。
2.  通过接口[display.isFoldable()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displayisfoldable10)可判断设备是否支持折叠，若支持则返回true。然而，获取可折叠设备显示模式的接口[display.getFoldDisplayMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetfolddisplaymode10)不适用于电脑，其返回结果为FOLD\_DISPLAY\_MODE\_UNKNOWN。

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.4.1.7.1.1" valign="top"><p>设备形态</p></th><td align="center" class="cellrowborder" valign="top"><p>半折叠态（唤起全尺寸键盘）</p></td><td align="center" class="cellrowborder" colspan="2" valign="top"><p>半折叠态（关闭全尺寸键盘）</p></td><td align="center" class="cellrowborder" valign="top"><p>横向展开态</p></td><td align="center" class="cellrowborder" valign="top"><p>竖向展开态</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.4.1.7.2.1" valign="top"><p>效果图</p></th><td align="center" class="cellrowborder" valign="top"><p><span><img height="336.1575" originheight="1166" originwidth="1384" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/dDy4jJn9QLKbS3VnL0otNw/zh-cn_image_0000002419751057.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2080D0F1FAC6E1CA06B33DDAA5C282C7F94D592AA7A90BED6626ECFEB92DEADA" title="点击放大" width="399"></span></p></td><td align="center" class="cellrowborder" colspan="2" valign="top"><p><span><img height="349.27130000000005" originheight="1166" originwidth="1332" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/jaqQA29iRn-i50M75eHxEw/zh-cn_image_0000002386231876.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87470223A92BF106347D807812E5A24BAC219764D24BFDA836739152267788AC" title="点击放大" width="399"></span></p></td><td align="center" class="cellrowborder" valign="top"><p><span><img height="327.5923" originheight="1150" originwidth="1494" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/9eavLLPzRHiZ1zsMcvqLaw/zh-cn_image_0000002419631233.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83C7E1A3721BF58AC650298AD2EB85BB4F67E2CA80F9485ED64CDB5205F8600B" title="点击放大" width="425.6"></span></p></td><td align="center" class="cellrowborder" valign="top"><p><span><img height="476.72520000000003" originheight="1444" originwidth="1128" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/lbo4VesBRJ-Z3DbUYkjXAw/zh-cn_image_0000002386071996.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T015418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3823F65AF468C0BB51A0197F6D5A87A92E89BAB014DC42CA04E2B6C0CA274C18" title="点击放大" width="372.40000000000003"></span></p></td></tr><tr><th class="firstcol" id="mcps1.3.5.4.1.7.3.1" valign="top"><p>isFoldable</p></th><td align="center" class="cellrowborder" colspan="5" valign="top"><p>true</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.4.1.7.4.1" valign="top"><p>FoldStatus</p></th><td align="center" class="cellrowborder" colspan="3" valign="top"><p>FOLD_STATUS_HALF_FOLDED</p></td><td align="center" class="cellrowborder" colspan="2" valign="top"><p>FOLD_STATUS_EXPANDED</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.4.1.7.5.1" valign="top"><p>FoldDisplayMode</p></th><td align="center" class="cellrowborder" colspan="5" valign="top"><p>FOLD_DISPLAY_MODE_UNKNOWN</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.4.1.7.6.1" valign="top"><p><a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#foldcreaseregion10" target="_blank">FoldCreaseRegion</a></p></th><td align="center" class="cellrowborder" colspan="5" valign="top"><p>{"left":0,"top":1608,"width":2472,"height":82}</p></td></tr></tbody></table>

**常用接口**

-   获取设备折叠状态相关接口
    
    | 
    API
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    [display.getFoldStatus()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetfoldstatus10)
    
     | 
    
    主动获取可折叠设备的当前折叠状态。具体折叠状态可参考上表中的FoldStatus行。
    
     |
    | 
    
    [display.on('foldStatusChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displayonfoldstatuschange10)
    
     | 
    
    开启折叠设备折叠状态变化的监听。当前设备物理折叠状态FoldStatus变化时，触发回调函数，返回折叠设备当前折叠状态。
    
     |
    
-   获取可用区域相关接口
    
    | 
    API
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    [getAvailableArea()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#getavailablearea12)
    
     | 
    
    获取当前设备屏幕的可用区域，使用Promise异步回调，仅支持电脑设备。
    
     |
    | 
    
    [on('availableAreaChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#onavailableareachange12)
    
     | 
    
    开启当前设备屏幕的可用区域监听。当前设备屏幕有可用区域变化时，触发回调函数，返回可用区域，仅支持电脑设备。
    
     |
    | 
    
    [display.getDisplayByIdSync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdisplaybyidsync12)
    
     | 
    
    返回displayId对应的display对象。其中包含电脑设备上屏幕的可用区域宽度availableWidth和高度availableHeight。display对应的区域可参考[屏幕规格信息](#section05491630111312)中的常用接口部分。
    
     |
    
-   获取折痕区域相关接口
    
    | 
    API
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    [display.getCurrentFoldCreaseRegion()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetcurrentfoldcreaseregion10)
    
     | 
    
    在当前显示模式下获取折叠折痕区域。返回[FoldCreaseRegion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#foldcreaseregion10)对象，即设备在当前显示模式下的折叠折痕区域。具体返回数据可参考[设备特有能力](#section1792714518428)表中的FoldCreaseRegion行。
    
     |
    

#### 体验标准

应用体验建议分为功能与兼容性、稳定性、性能、功耗、安全和UX六个部分，详细信息如下所示。

| 
名称

 | 

简介

 |
| :-- | :-- |
| 

[应用基础功能和兼容性体验建议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/experience-suggestions-compatibility)

 | 

应用与OS兼容、应用与设备兼容、应用升级兼容、功能体验相关等。

 |
| 

[应用稳定性体验建议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/experience-suggestions-stability)

 | 

长时间运行故障率（崩溃、冻屏等）、长时间运行内存资源异常。

 |
| 

[应用性能体验建议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-experience-suggestions)

 | 

时延、帧率流畅体验和内存占用、CPU占用、线程数等资源占用约束。

 |
| 

[应用功耗体验建议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-power-experience-standards)

 | 

后台任务使用、后台硬件器件资源/软件系统资源占用管控，分布式资源占用等。

 |
| 

[应用安全隐私体验建议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/security-privacy-experience-standards)

 | 

基础安全、恶意软件、应用安全、隐私合规等。

 |
| 

[应用UX体验建议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/experience-suggestions-ux)

 | 

设计规范、设计约束的符合性，UX精致体验要求等。

 |

折叠电脑设备主要在UX上有着特殊的适配体验和建议，下文主要介绍折叠电脑的UX体验建议。

#### \[h2\]UX体验建议

**体验设计标准**

折叠电脑以“沉浸无界、灵动流畅、直觉自然”为核心设计理念，深度融合折叠屏的硬件特性与多模态交互需求，针对系统架构和桌面应用在多形态变换、应用适配、交互输入、系统动效表现等方面，为相关设计师和开发人员提供UX设计指南和规范，确保用户在任何场景下均能获得连贯高效的使用体验。UX设计指南可参考[电脑](https://developer.huawei.com/consumer/cn/doc/design-guides/2in1-0000001777531700)和[折叠电脑](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-pc-0000002322600098)。

**体验设计差异点**

折叠电脑具备折叠状态和展开状态等五种页面布局。在开发应用时，建议采用[响应式布局](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout)，以根据屏幕尺寸自动调整布局，实时响应窗口尺寸变化，确保内容以最优布局展示。响应式布局中最常用的特征是窗口宽度和窗口高宽比，可以将这些参数划分为不同的范围。应用需通过横纵断点来决定不同状态下的页面布局，关于断点的原理和使用示例，可参考[断点](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout#section1532120147301)。

折叠电脑涵盖了从xs到xl的所有横向断点，应用可根据需求设计不同断点对应的页面布局，以实现自适应和响应式布局。在适配折叠电脑页面布局时，为避免出现过多空白区域或内容过于拥挤，影响用户体验，开发者可[设置自由窗口宽度最小值](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-mode#section6754152523715)，从而避免xs断点的适配。

页面布局主要实现流程为：

1.  调用[on('windowSizeChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uiextension#onwindowsizechange)监听自由窗口尺寸的变化。
2.  通过[getWindowWidthBreakpoint()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getwindowwidthbreakpoint13)与[getWindowHeightBreakpoint()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getwindowheightbreakpoint13)获取当前窗口横向断点与纵向断点。
3.  通过状态变量将横纵断点绑定为组件的属性值，当横纵断点变化时组件自动变化，或通过横纵断点变化控制自定义组件的显隐，展示不同断点对应的页面布局。

**应用设计最佳实践**

根据上述UX体验标准和设计差异点，各垂域应用可根据功能和场景特点进行折叠电脑的UX设计；更多垂域设计信息和方案可参考[典型应用案例](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-pc-0000002322600098#section1124084104516)。

#### 工程管理

在折叠电脑设备上运行的应用，需要在module.json5配置文件的module字段中增加支持的deviceTypes工程配置，即需增设"2in1"。更多详情可参考[deviceTypes标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#devicetypes标签)。

#### 窗口适配

本章节主要介绍折叠电脑在窗口适配上需要适配的内容。

#### \[h2\]适配设备窗口模式

折叠电脑支持全屏、分屏、自由窗口三种窗口模式。

**全屏**

折叠电脑的窗口模式与传统电脑上一致，应用启动时默认应为自由窗口模式，用户可以通过[setWindowLayoutFullScreen()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowlayoutfullscreen9)接口，实现界面元素延伸至状态栏和导航区域，从而进入全屏模式，具体适配信息请参考[窗口沉浸式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-immersive)。

**分屏**

折叠电脑支持分屏窗口模式，一般用于两个应用长时间并行使用的场景，例如边看购物攻略边购物的场景；应用也可以主动实现应用内分屏。折叠电脑默认支持上下分屏和左右分屏，分屏窗口参数如下，具体适配信息请参考[分屏窗口模式适配](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-mode#section579413164399)。

| 
分屏方式

 | 

默认分屏比例

 | 

设备形态

 | 

旋转状态

 | 

分屏窗口尺寸(px)

 | 

分屏窗口尺寸(vp)向下取整

 | 

分屏窗口断点

 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 

左右分屏

 | 

1:1

 | 

半折叠态（唤起全尺寸键盘）

 | 

竖屏

 | 

1225\*1490

 | 

680 \* 827

 | 

横向断点md，纵向断点lg

 |
| 

半折叠态（关闭全尺寸键盘）

 | 

竖屏

 | 

1225\*1608

 | 

680 \* 893

 | 

横向断点md，纵向断点lg

 |
| 

横向展开态

 | 

横屏/反向横屏

 | 

1637\*2354

 | 

909 \* 1307

 | 

横向断点lg，纵向断点lg

 |
| 

上下分屏

 | 

1:1

 | 

竖向展开态

 | 

竖屏

 | 

2472\*1578

 | 

1373 \* 876

 | 

横向断点lg，纵向断点sm

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/nOz8NSTcRHqftBbzA8Yx7g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015418Z&HW-CC-Expire=86400&HW-CC-Sign=694924E57AE1BA47DB94EDC08A2FA4F4D114E245DB09F47577C2B191127973CC)

折叠电脑在半折叠状态下，只能在上屏使用左右分屏，下屏无法触发分屏模式。

**自由窗口**

折叠电脑的窗口模式与传统电脑上一致，应用启动时默认应为自由窗口模式，而非全屏模式，具体适配信息请参考[自由窗口模式适配](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-mode#section151195853214)。

-   跨屏幕移动
    
    折叠电脑在半折叠状态（关闭全尺寸键盘）下，如果应用位于下屏，开发者可以使用[moveWindowToGlobal()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#movewindowtoglobal15)接口将应用跨屏移动到上屏，从而实现从下屏到上屏的窗口移动。
    
    let mainWindow =
      (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync();
    let moveConfiguration: window.MoveConfiguration = {
      displayId: 0
    };
    await mainWindow.moveWindowToGlobal(0, 0, moveConfiguration);
    
-   窗口跨屏展示
    
    在半折叠状态（关闭全尺寸键盘）下，折叠电脑的全屏模式仅支持单屏最大化显示。如果应用内容过多，单屏显示无法完全呈现所有信息。此时，通过跨两个屏幕展示内容，可以更方便地查看所有信息。在这种情况下，可以长按最大化按键，在弹出的菜单中选择进入瀑布流模式，从而实现窗口的跨屏展示。
    

#### \[h2\]适配窗口显示方向

电脑上的窗口显示方向[Orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-e#orientation9)效果始终跟随屏幕显示方向[Orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#orientation10)的效果，屏幕显示方向由具体产品定义（MateBook Pro只支持横屏，MateBook Fold支持三个方向），具体信息可参考[硬件说明](#section7335104513501)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/l1vJC57nSIexyj28cuES9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015418Z&HW-CC-Expire=86400&HW-CC-Sign=B7C4C96FA0654FA05E246315A18EEBCE323F5D21B5E18ED5475BEBCADA0DED64)

由于[window.setPreferredOrientation()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9)设置窗口方向不生效，所以不建议调用[window.setPreferredOrientation()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9)设置电脑的窗口方向，也不建议调用[getPreferredOrientation()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getpreferredorientation12)获取窗口的显示方向。

#### \[h2\]适配窗口沉浸式

不同设备的定制沉浸式策略，推荐通过窗口模式进行区分，而非依赖设备类型判断。可通过动态识别当前窗口模式（如全屏、分屏、悬浮窗、自由窗口等），针对不同窗口形态实施定制化的沉浸式策略。适配窗口沉浸式请参考[窗口沉浸式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-immersive)。

#### 界面开发

折叠电脑的响应式布局符合电脑的标准，详情可参考[电脑布局设计](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pc-guide#section583511558587)。

#### 交互体验

折叠电脑的交互体验符合电脑的标准，详情可参考[电脑交互体验](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pc-guide#section1634505165912)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/WfxmUzgbRo-XlySgFjs3kg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015418Z&HW-CC-Expire=86400&HW-CC-Sign=817B37ED035D0B78772F285567B3E7A59987CD607CE6424E0A66E7E2C7385A42)

需要注意的是，折叠电脑与传统电脑的差异点在于，折叠电脑触屏点击应用内输入框会自动拉起[悬浮键盘](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-pc-0000002322600098#虚拟键盘)，鼠标点击应用内输入框不会自动拉起虚拟键盘。

#### 功能开发

#### \[h2\]适配相机的旋转角度

当折叠电脑处于不同的设备状态时，屏幕的状态也会有所不同。在这种情况下，相机应用预览输出的原始图像需要旋转不同的角度，以确保图像在正确的方向上显示。（预览旋转角度 = 镜头安装角度 + 屏幕显示补偿角度，屏幕显示补偿角度的值与屏幕旋转角度相同。若要自行获取镜头安装角度，可以参考：[getSupportedCameras()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedcameras)）

在预览时，预览旋转角度与屏幕显示旋转角度（[Display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#属性).rotation）相关。若要适配相机的旋转角度，则需要在session调用[commitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11)完成配流后，配置输出流：

1.  通过[display.getDefaultDisplaySync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9)接口获取[Display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#属性)对象并读取其rotation属性值，获得显示设备的屏幕旋转角度。
2.  并根据[相机镜头安装角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#相机镜头安装角度)+[屏幕显示旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#屏幕旋转角度)的值计算[预览旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#预览旋转角度)，可参考[相机硬件信息](#section1848513375424)查看对应预览旋转角度。
3.  再调用[setPreviewRotation()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput#getpreviewrotation12)接口，设置图像的预览旋转角度。

具体开发指导可参考[适配相机旋转角度-预览](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-angle-adaptation#预览)。

**应用对接预览流二次处理场景下的问题**

若三方应用接口对接的是预览流二次处理，导致系统无法将镜头安装角度补充到预览旋转角度中，导致不能使用系统现有的能力，因此向应用提供两种方案：

-   若应用不需要非镜像成像，建议应用在预览流二次处理后，直接套用系统现有的角度计算方法，应用补偿相机镜头安装角度进行适配。
-   若应用需要非镜像成像，建议应用在预览流二次处理后，自行开发一套角度计算公式，应用自行适配。（非镜像成像场景下，自行适配的性能大大优于补偿相机镜头安装角度的方法）

#### 常见问题

#### \[h2\]如何区分MateBook Fold和MateBook Pro

-   页面布局类问题：
    
    页面布局由窗口形态、宽度和高宽比属性决定，不应区分产品型号或设备类型。例如MateBook Fold的横向展开态布局应该和MateBook Pro布局保持一致，MateBook Fold的其他状态对应横向断点lg的页面布局，应与平板布局保持一致。所以，布局类问题只需判断断点，开发响应式布局即可。详情可参考[断点](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout#section1532120147301)的使用。
    
-   非页面布局或功能类问题：
    
    由于MateBook Fold和MateBook Pro的设备类型[deviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info#常量)均为2in1，因此，可以通过[isFoldable()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displayisfoldable10)判断是否为可折叠设备，MateBook Fold返回为true，MateBook Pro返回为false。
    

#### \[h2\]折叠状态变化导致的页面异常

**问题现象**

当折叠电脑的折叠状态发生变化时，可能会导致应用的页面布局出现异常。

**可能原因**

当折叠电脑的折叠状态发生变化时，窗口的大小及横纵断点也会同步发生变化，若应用感知到可用区域的变化，但未对不同断点下的页面布局做处理，可能会导致应用的页面布局不符合需求场景，或出现异常。

**解决措施**

使用获取可用区域的相关接口主动获取可用区域的尺寸或调用[on('windowSizeChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uiextension#onwindowsizechange)监听自由窗口尺寸的变更，根据获取到的可用区域尺寸判断所属[断点](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout#section1532120147301)，当断点改变时同步调整页面布局，实现页面的[响应式布局](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout)。具体方案可参考[UX体验建议](#section1756114301170)章节。

#### \[h2\]如何实现跨屏幕移动窗口

**问题现象**

折叠电脑在半折叠状态（关闭全尺寸键盘）下，上下两块屏幕均可独立操作，如果应用位于下屏，开发者想将应用跨屏移动到上屏，应该如何操作？

**解决措施**

可使用[moveWindowToGlobal()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#movewindowtoglobal15)接口实现跨屏幕移动窗口，将窗口从下屏移动至上屏。详情可参考[窗口模式](#section8155133712178)章节。

#### \[h2\]应用感知可用区域变化不及时

**问题现象**

应用未感知可用区域变化或者感知可用区域变化不及时，但调用moveTo()和resize()调整窗口大小或位置，导致窗口大小或位置异常。

**解决措施**

使用以下三种方法均可解决该问题：

-   使用[display.getDisplayByIdSync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdisplaybyidsync12)根据displayId主动获取对应可用区域的[display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)对象。
-   使用[getAvailableArea()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#getavailablearea12)主动获取当前设备屏幕的可用区域。
-   使用[on('availableAreaChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#onavailableareachange12)开启当前设备屏幕的可用区域监听。

#### \[h2\]相机预览画面旋转异常

**问题现象**

折叠电脑在屏幕旋转后，相机生成的预览画面出现异常。

**可能原因**

折叠电脑在屏幕旋转后，相机预览流未适配旋转后的预览角度，造成预览画面未更新。

**解决措施**

在session调用[commitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11)完成配流后调用，通过[display.getDefaultDisplaySync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9)获得显示设备的屏幕旋转角度displayRotation，并通过[setPreviewRotation()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput#getpreviewrotation12)，设置图像的预览旋转角度。具体可参考[功能开发](#section1110071416153)章节。
