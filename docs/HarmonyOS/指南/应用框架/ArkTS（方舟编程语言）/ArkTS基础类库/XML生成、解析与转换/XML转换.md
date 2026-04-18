---
title: "XML转换"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-conversion"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkTS（方舟编程语言）"
  - "ArkTS基础类库"
  - "XML生成、解析与转换"
  - "XML转换"
captured_at: "2026-04-17T01:35:34.130Z"
---

# XML转换

将XML文本转换为JavaScript对象，便于处理和操作数据，适用于JavaScript应用程序。

语言基础类库提供ConvertXML类，将XML文本转换为JavaScript对象，输入为待转换的XML字符串及转换选项，输出为转换后的JavaScript对象。具体转换选项可见[API参考@ohos.convertxml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-convertxml)。

#### 注意事项

XML解析及转换需要确保传入的XML数据符合XML标准格式。

#### 开发步骤

以XML转换为JavaScript对象为例，说明如何获取标签值。

1.  引入所需的模块。
    
    ```typescript
    import { convertxml } from '@kit.ArkTS';
    ```
    
2.  输入待转换的XML，设置转换选项。支持的转换选项及含义，请参见[ConvertOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-convertxml#convertoptions)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/CU4iM2R6Q1CRCdZ47hLUZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013534Z&HW-CC-Expire=86400&HW-CC-Sign=B69A480DD45BD839EC1252FBB9B21FEA9563A22935943C199FCC5396C0E29CDB)
    
    请确保传入的XML文本符合标准格式，若包含“&”字符，请使用实体引用“&amp;”替换。
    
    ```typescript
    let xml: string =
      '<?xml version="1.0" encoding="utf-8"?>' +
        '<note importance="high" logged="true">' +
        '    <title>Happy</title>' +
        '    <todo>Work</todo>' +
        '    <todo>Play</todo>' +
        '</note>';
    let options: convertxml.ConvertOptions = {
      // trim: false 转换后是否删除文本前后的空格，否
      // declarationKey: "_declaration" 转换后文件声明使用_declaration来标识
      // instructionKey: "_instruction" 转换后指令使用_instruction标识
      // attributesKey: "_attributes" 转换后属性使用_attributes标识
      // textKey: "_text" 转换后标签值使用_text标识
      // cdataKey: "_cdata" 转换后未解析数据使用_cdata标识
      // docTypeKey: "_doctype" 转换后文档类型使用_doctype标识
      // commentKey: "_comment" 转换后注释使用_comment标识
      // parentKey: "_parent" 转换后父类使用_parent标识
      // typeKey: "_type" 转换后元素类型使用_type标识
      // nameKey: "_name" 转换后标签名称使用_name标识
      // elementsKey: "_elements" 转换后元素使用_elements标识
      trim: false,
      declarationKey: '_declaration',
      instructionKey: '_instruction',
      attributesKey: '_attributes',
      textKey: '_text',
      cdataKey: '_cdata',
      doctypeKey: '_doctype',
      commentKey: '_comment',
      parentKey: '_parent',
      typeKey: '_type',
      nameKey: '_name',
      elementsKey: '_elements'
    }
    ```
    
3.  调用fastConvertToJSObject函数并打印结果。
    
    ```typescript
    let conv: convertxml.ConvertXML = new convertxml.ConvertXML();
    let result: object = conv.fastConvertToJSObject(xml, options);
    let strRes: string = JSON.stringify(result); // 将js对象转换为json字符串，用于显式输出
    console.info(strRes);
    ```
    
    输出结果如下所示：
    
    ```json
    strRes:
    {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note",
     "_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_parent":"note",
     "_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_parent":"note","_elements":
     [{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_parent":"note","_elements":[{"_type":"text",
     "_text":"Play"}]}]}]}
    ```
