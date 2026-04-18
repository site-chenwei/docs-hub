---
title: "DevEco Studio AppAnalyzer"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-10"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用测试"
  - "DevEco Studio AppAnalyzer-安装Python依赖错误"
captured_at: "2026-04-17T02:03:25.332Z"
---

# DevEco Studio AppAnalyzer-安装Python依赖错误

**问题现象**

安装Python依赖报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/GH3wR-x8TXOeGjRd7P8YlA/zh-cn_image_0000002265289721.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=B417AE55E98565454BEC0474BDC5420D58C992488E26C146F3665495DCBB3DCB)

**可能原因**一

pip配置问题。

**解决措施**

1.  修改pip配置。
    
    pip的配置文件位于用户根目录下的：~/.pip/pip.conf（Windows路径为：C:\\Users\\<UserName>\\pip\\pip.ini\*）。 开发者可以配置如下内容：
    
    ```text
    [global]
    index-url = https://mirrors.huaweicloud.com/repository/pypi/simple
    trusted-host = mirrors.huaweicloud.com
    timeout = 120 
    ```
    
    如需设置代理，可以参考以下配置，如果username、password包含特殊字符，需要进行转义。**proxyserver和port请按照实际代理服务器进行修改**。示例如下所示：
    
    ```text
    [global]
    index-url = https://mirrors.huaweicloud.com/repository/pypi/simple
    proxy = http://username:password@proxyserver:port/
    trusted-host = mirrors.huaweicloud.com
    timeout = 120  
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Sm8q2iTkRCek84S1Cjr6Rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=61D54970AAB44EA9C5AE11145010CE62F87CE7500672B870861DC62D224FC10C)
    
    如果password中存在特殊字符，如@、#、\*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：
    
    -   !：%21
    -   @：%40
    -   #：%23
    -   $：%24
    -   &：%26
    -   \*：%2A
    
2.  查看本地生效的pip配置。
    
    ```powershell
    pip config list
    ```
    

**可能原因二**

Win系统卸载Python时有残留。

**解决措施**

Win系统卸载Python时未删除Python安装目录，需要清理Python的安装目录。

**可能原因三**

无外网访问权限。

**解决措施**

冷启动、白块检测、UX检测需要网络下载依赖。请更换有外网访问权限的网络。

**可能原因四**

paddlepaddle==2.6.1已经日落，导致pip安装失败

**解决措施**

MAC

```powershell
 //进入python安装目录
cd python_dir_xxxx   
//python3.9安装命令
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp39-cp39-macosx_10_9_x86_64.whl
//python3.10安装命令
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp310-cp310-macosx_10_9_x86_64.whl
//python3.11安装命令
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp311-cp311-macosx_10_9_x86_64.whl
//python3.12安装命令
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp312-cp312-macosx_10_9_x86_64.whl
```

Win

```powershell
//进入python安装目录
cd python_dir_xxxx   
./python.exe -m pip install paddlepaddle==2.6.1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
```

**可能原因五**

Python兼容性问题。

**解决措施**

Python与某些指定版本的依赖不兼容，支持的版本为**Python 3.9 ~3.12**，推荐**Python 3.11.7。**如果Python最新的版本与一些依赖不兼容，建议卸载Python并安装推荐版本或者更新[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)。

<table><tbody><tr><td class="cellrowborder" valign="top" width="20%"><p>分类</p></td><td class="cellrowborder" valign="top" width="20%"><p>三方库</p></td><td class="cellrowborder" valign="top" width="20%"><p>DevEco Studio 5.0.x</p></td><td class="cellrowborder" valign="top" width="20%"><p>DevEco Studio 5.1.x</p></td><td class="cellrowborder" valign="top" width="20%"><p>DevEco Studio 6.0.x</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>Flask</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.3</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.3</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.3</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>numpy</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>onnxruntime</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.19.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.19.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.19.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>opencv-python</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>pillow</p></td><td class="cellrowborder" valign="top" width="20%"><p>10.4.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>10.4.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>10.4.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>pyclipper</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0.post6</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0.post6</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0.post6</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>shapely</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.0.6</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.0.6</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.0.6</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动&amp;&amp;白块检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>waitress</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>hypium</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>xdevice</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>xdevice-devicetest</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>xdevice-ohos</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>loguru</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.7.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.7.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>numpy</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>stable_baselines3</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.3.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.3.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>gym</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.26.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.26.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>gym-notices</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.0.8</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.0.8</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>gymnasium</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.29.1</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.29.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>Shimmy</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>opencv-python</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>cffi</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.17.1</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.17.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>pynacl</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.5.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.5.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>torch</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p><p></p></td><td class="cellrowborder" valign="top" width="20%"><p>python版本&lt;3.12：2.0.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>python版本&lt;3.12：2.0.0</p><p><span style="color: rgb(224,62,45);">python版本==3.12：2.2.0</span></p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>torchaudio</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p><p></p></td><td class="cellrowborder" valign="top" width="20%"><p>python版本&lt;3.12：2.0.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>python版本&lt;3.12：2.0.0</p><p><span style="color: rgb(224,62,45);">python版本==3.12：2.2.0</span></p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>torchvision</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p><p></p></td><td class="cellrowborder" valign="top" width="20%"><p>python版本&lt;3.12：0.15.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>python版本&lt;3.12：0.15.0</p><p><span style="color: rgb(224,62,45);">python版本==3.12：0.17.0</span></p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>冷启动-自动</p></td><td class="cellrowborder" valign="top" width="20%"><p>setuptools</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p><span style="color: rgb(224,62,45);">python 版本 </span><span style="color: rgb(224,62,45);">&lt;</span><span style="color: rgb(224,62,45);"> 3.12: python 自带</span></p><p><span style="color: rgb(224,62,45);">python版本==3.12：80.9.0</span></p></td><td class="cellrowborder" valign="top" width="20%"><p><span style="color: rgb(224,62,45);">python 版本 </span><span style="color: rgb(224,62,45);">&lt;</span><span style="color: rgb(224,62,45);"> 3.12: python 自带</span></p><p><span style="color: rgb(224,62,45);">python版本==3.12：80.9.0</span></p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>numpy</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>ImageHash</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.3.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>opencv-python</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>paddlepaddle</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>python版本&lt;3.12：2.6.2</p><p><span style="color: rgb(186,55,42);">python版本==3.12：3.0.0</span></p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>paddleocr</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.8.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>psutil</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.9.8</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>Werkzeug</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.1.3</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>scikit-learn</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.5.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>折叠机UX规则检测</p></td><td class="cellrowborder" valign="top" width="20%"><p>supervision</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.17.1</p></td></tr></tbody></table>
