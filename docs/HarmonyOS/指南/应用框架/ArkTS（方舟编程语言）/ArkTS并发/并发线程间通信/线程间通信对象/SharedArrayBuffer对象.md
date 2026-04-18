---
title: "SharedArrayBuffer对象"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/shared-arraybuffer-object"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkTS（方舟编程语言）"
  - "ArkTS并发"
  - "并发线程间通信"
  - "线程间通信对象"
  - "SharedArrayBuffer对象"
captured_at: "2026-04-17T01:35:34.452Z"
---

# SharedArrayBuffer对象

SharedArrayBuffer内部包含一块Native内存，其JS对象壳被分配在虚拟机本地堆（LocalHeap）。支持跨并发实例间共享Native内存，但是对共享Native内存的访问及修改需要采用Atomics类，防止数据竞争。SharedArrayBuffer可用于多个并发实例间的状态或数据共享。通信过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/55by-a8MTreYmVIppGihHg/zh-cn_image_0000002538018448.png?HW-CC-KV=V1&HW-CC-Date=20260417T013535Z&HW-CC-Expire=86400&HW-CC-Sign=6789F7EFD944DF5837893AC7CDE67EAF69C4BA000196C825EA720ACC51A6D5E6)

#### 使用示例

使用TaskPool传递Int32Array对象，实现如下：

```ts
import { taskpool } from '@kit.ArkTS';

@Concurrent
function transferAtomics(arg1: Int32Array) {
  console.info("wait begin::");
  // 使用Atomics进行操作
  let res = Atomics.wait(arg1, 0, 0, 3000);
  return res;
}

// 定义可共享对象
let sab: SharedArrayBuffer = new SharedArrayBuffer(20);
let int32 = new Int32Array(sab);
let task: taskpool.Task = new taskpool.Task(transferAtomics, int32);
taskpool.execute(task).then((res) => {
  console.info("this res is: " + res);
});
setTimeout(() => {
  Atomics.notify(int32, 0, 1);
}, 1000);
```
