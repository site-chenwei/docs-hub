---
title: "@system.file (文件存储)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-file"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@system.file (文件存储)"
captured_at: "2026-04-17T01:48:14.145Z"
---

# @system.file (文件存储)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/N0Ct_jTrT9WlP6RVJsPahA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=DD47F100AEE37F68E9DDCB4668D9DC44A63E438A7D75AAB980E0E049856FD2FB)

-   模块维护策略：
    -   对于Lite Wearable设备类型，该模块长期维护，正常使用。
    -   对于支持该模块的其他设备类型，该模块从API Version 10开始不再维护，推荐使用新接口[@ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)。
-   本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import file from '@system.file';
```

#### file.move

move(Object): void

将指定文件移动到其他指定位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/jYbbm6YCRxqkDeV0CgSWuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=1589C898F471A8309332B7630F01196AC0ED2ECB50B0CFD938844DED3E7F3CB8)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.moveFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomovefile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| srcUri | string | 是 | 要移动的文件的uri。字符串最大长度为128，且不能包含“"\*+,:;<=>?\[\]|\\x7F”等特殊符号。 |
| dstUri | string | 是 | 文件要移动到的位置的uri。字符串最大长度为128，且不能包含“"\*+,:;<=>?\[\]|\\x7F”等特殊符号。 |
| success | Function | 否 | 接口调用成功的回调函数，返回文件要移动到的位置的uri。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  move() {
    file.move({
      srcUri: 'internal://app/myfiles1',
      dstUri: 'internal://app/myfiles2',
      success: function(uri) {
        console.info('call success callback success');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.copy

copy(Object): void

将指定文件拷贝并存储到指定位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/mfwrqFDOQUqE8ux4qyJZyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=50D6DAB4E8C31404F61100EA7F0F9AB5FEF8B73B8633EEEB675ADCE3DFEDD976)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.copyFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocopyfile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| srcUri | string | 是 | 要拷贝的文件的uri。 |
| dstUri | string | 是 | 
文件要拷贝到的位置的uri。

不支持用应用资源路径或tmp类型的uri。

 |
| success | Function | 否 | 接口调用成功的回调函数，返回文件要拷贝到的位置的uri。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  copy() {
    file.copy({
      srcUri: 'internal://app/file.txt',
      dstUri: 'internal://app/file_copy.txt',
      success: function(uri) {
        console.info('call success callback success');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.list

list(Object): void

获取指定路径下全部文件的列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/26cdwJ3wRDuuwmc-TlH93w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=C96D5C794499B6D71F7C8F949826BD18617C307EC3D6D2C4025D8711B6E9889D)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.listFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 目录uri。字符串最大长度为128，且不能包含“"\*+,:;<=>?\[\]|\\x7F”等特殊符号。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| :-- | :-- | :-- |
| fileList | Array<FileInfo> | 
获取的文件列表，其中每个文件的信息的格式为：

{

uri:'file1',

lastModifiedTime:1589965924479,

length:10240,

type: 'file'

}

 |

**表1** FileInfo

| 参数名 | 类型 | 说明 |
| :-- | :-- | :-- |
| uri | string | 文件的 uri。 |
| lastModifiedTime | number | 文件上一次保存时的时间戳，显示从1970/01/01 00:00:00 GMT到当前时间的毫秒数。 |
| length | number | 文件的大小，单位为Byte。 |
| type | string | 
文件的类型，可选值为：

\- dir：目录；

\- file：文件。

 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  list() {
    file.list({
      uri: 'internal://app/pic',
      success: function(data) {
        console.info(JSON.stringify(data.fileList));
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.get

get(Object): void

获取指定本地文件的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/CIjATZaFQfuTJLQUOdt15g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=8B9D283FF13EEF9478B7652812357FA415BB1EE557916F481F1404C1904D3007)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.stat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiostat)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 文件的uri。 |
| recursive | boolean | 否 | 是否进行递归获取子目录文件列表，true为进行该操作，缺省为false。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| :-- | :-- | :-- |
| uri | string | 文件的uri。 |
| length | number | 文件长度，单位为Byte。 |
| lastModifiedTime | number | 文件保存时的时间戳，从1970/01/01 00:00:00到当前时间的毫秒数。 |
| type | string | 
文件类型，可选值为：

\- dir：目录；

\- file：文件。

 |
| subFiles | Array | 文件列表。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  get() {
    file.get({
      uri: 'internal://app/file',
      success: function(data) {
        console.info(data.uri);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.delete

delete(Object): void

删除本地文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/BDqLtznLRvyfjNlJOcNV-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=EDF885A2D8183AC80F2F78865E66D45A54B28230D228B27054F0E8797520E049)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.unlink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiounlink)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 删除文件的uri，不能是应用资源路径。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 参数错误。 |
| 300 | I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  delete() {
    file.delete({
      uri: 'internal://app/my_file',
      success: function() {
        console.info('call delete success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.writeText

writeText(Object): void

写文本内容到指定文件。仅支持文本文档读写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/fsJwjQMOQCGtIzcn0Z_N9w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=F7CE132A98D28AD019D1F1A7598DA276D8BD82D1C03A73C10CF5407D5AD9FABA)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiowrite)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 本地文件uri，如果文件不存在会创建文件。 |
| text | string | 是 | 写入的字符串。 |
| encoding | string | 否 | 编码格式，默认为UTF-8。 |
| append | boolean | 否 | 是否追加模式，默认为false。true为追加，false为不追加。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 参数错误。 |
| 300 | I/O错误。 |

**示例：**

```ts
export default {
  writeText() {
    file.writeText({
      uri: 'internal://app/test.txt',
      text: 'Text that just for test.',
      success: function() {
        console.info('call writeText success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.writeArrayBuffer

writeArrayBuffer(Object): void

写Buffer内容到指定文件。仅支持文本文档读写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/a4kejjLdQ2GLY9V8G9hgnA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=0CFFF149CBE1B366915C69D323D98B7B8C1F3B24876B0B041EFEF846F21D4F33)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.write](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiowrite)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 本地文件uri，如果文件不存在会创建文件。 |
| buffer | Uint8Array | 是 | 写入的Buffer。 |
| position | number | 否 | 文件开始写入数据的位置的偏移量，单位为Byte，默认为0。 |
| append | boolean | 否 | 是否追加模式，默认为false。当设置为true时，position参数无效。true为追加，false为不追加。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |

**示例：**

```ts
export default {
  writeArrayBuffer() {
    file.writeArrayBuffer({
      uri: 'internal://app/test',
      buffer: new Uint8Array(8),// buffer为Uint8Array类型
      success: function() {
        console.info('call writeArrayBuffer success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.readText

readText(Object): void

从指定文件中读取文本内容。仅支持文本文档读写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/xSPQRWmsTlWfz4wCGBw8KQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=15C4940748E838B422B41F4E1C7B60941C6E723B6FDC82CE515E6DAECD22DFED)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.readText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioreadtext)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 本地文件uri。 |
| encoding | string | 否 | 编码格式，缺省为UTF-8。 |
| position | number | 否 | 读取的起始位置，单位为Byte，默认值为文件的起始位置。 |
| length | number | 否 | 读取的长度，单位为Byte，默认值为4096。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| :-- | :-- | :-- |
| text | string | 读取到的文本内容。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |
| 302 | 要读取的文件内容超过4KB。 |

**示例：**

```ts
export default {
  readText() {
    file.readText({
      uri: 'internal://app/text.txt',
      success: function(data) {
        console.info('call readText success: ' + data.text);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.readArrayBuffer

readArrayBuffer(Object): void

从指定文件中读取Buffer内容。仅支持文本文档读写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/XjsHEFkYQF-fFnXLlZePGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=577009DC0F77F37D9C6F128D203C29E27739B3493EE70B480234F9293F0AEB09)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.read](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioread)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 本地文件uri。 |
| position | number | 否 | 读取的起始位置，单位为Byte，缺省为文件的起始位置。 |
| length | number | 否 | 需要读取的长度，单位为Byte，缺省则读取到文件结尾。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| :-- | :-- | :-- |
| buffer | Uint8Array | 读取到的文件内容。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  readArrayBuffer() {
    file.readArrayBuffer({
      uri: 'internal://app/test',
      position: 10,
      length: 200,
      success: function(data) {
        console.info('call readArrayBuffer success: ' + data.buffer);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.access

access(Object): void

判断指定文件或目录是否存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/ZrqavCF7Qd2EghrGOwDxFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=0F4927DC3E9C6C1FD4C2023D3B5B41A8E14A24748936CAE30C6922D4D325FEEE)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.access](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioaccess)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 目录或文件uri。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O 错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  access() {
    file.access({
      uri: 'internal://app/test',
      success: function() {
        console.info('call access success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.mkdir

mkdir(Object): void

创建指定目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/pxn5vogDST-WmfGXEpT06w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=EF94DC0C2CABC49677D8106980A8D324C4548E4B62C9A5E33B1D48AFBD7481CC)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.mkdir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiomkdir)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 目录的uri路径。 |
| recursive | boolean | 否 | 是否递归创建该目录的上级目录，缺省为false。true为递归创建，false是不递归创建。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O 错误。 |

**示例：**

```ts
export default {
  mkdir() {
    file.mkdir({
      uri: 'internal://app/test_directory',
      success: function() {
        console.info('call mkdir success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### file.rmdir

rmdir(Object): void

删除指定目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ITVou-gZSxKwKCI7nxOi8w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014814Z&HW-CC-Expire=86400&HW-CC-Sign=7B6C83FD86852AD4C7C7E4F2A2F41AEF143E73F1DD837693CC53C98652F93A96)

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.rmdir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiormdir)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 目录的uri路径。 |
| recursive | boolean | 否 | 是否递归删除子文件和子目录，缺省为false。true为递归删除，false为不递归删除。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O 错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```ts
export default {
  rmdir() {
    file.rmdir({
      uri: 'internal://app/test_directory',
      success: function() {
        console.info('call rmdir success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```
