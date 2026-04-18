---
title: "styled_string.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "头文件"
  - "styled_string.h"
captured_at: "2026-04-17T01:48:07.685Z"
---

# styled\_string.h

#### 概述

在Native侧定义[组件类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodetype)为ARKUI\_NODE\_TEXT的组件的文本样式和文本布局管理器。

**引用文件：** <arkui/styled\_string.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**相关示例：** [StyledStringSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/StyledStringSample)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring) | ArkUI\_StyledString | 定义文本组件支持的格式化字符串数据对象。 |
| [ArkUI\_TextLayoutManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager) | ArkUI\_TextLayoutManager | 定义文本布局管理器对象。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString\* OH\_ArkUI\_StyledString\_Create(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_FontCollection\* collection)](#oh_arkui_styledstring_create) | 创建指向ArkUI\_StyledString对象的指针。 |
| [void OH\_ArkUI\_StyledString\_Destroy(ArkUI\_StyledString\* handle)](#oh_arkui_styledstring_destroy) | 释放被ArkUI\_StyledString对象占据的内存。 |
| [void OH\_ArkUI\_StyledString\_PushTextStyle(ArkUI\_StyledString\* handle, OH\_Drawing\_TextStyle\* style)](#oh_arkui_styledstring_pushtextstyle) | 将新的排版风格设置到当前格式化字符串样式栈顶。 |
| [void OH\_ArkUI\_StyledString\_AddText(ArkUI\_StyledString\* handle, const char\* content)](#oh_arkui_styledstring_addtext) | 基于当前格式化字符串样式设置对应的文本内容。 |
| [void OH\_ArkUI\_StyledString\_PopTextStyle(ArkUI\_StyledString\* handle)](#oh_arkui_styledstring_poptextstyle) | 将当前格式化字符串对象中栈顶样式出栈。 |
| [OH\_Drawing\_Typography\* OH\_ArkUI\_StyledString\_CreateTypography(ArkUI\_StyledString\* handle)](#oh_arkui_styledstring_createtypography) | 基于格式字符串对象创建指向[OH\_Drawing\_Typography](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typography)对象的指针，用于提前进行文本测算排版。 |
| [void OH\_ArkUI\_StyledString\_AddPlaceholder(ArkUI\_StyledString\* handle, OH\_Drawing\_PlaceholderSpan\* placeholder)](#oh_arkui_styledstring_addplaceholder) | 设置占位符。 |
| [ArkUI\_StyledString\_Descriptor\* OH\_ArkUI\_StyledString\_Descriptor\_Create(void)](#oh_arkui_styledstring_descriptor_create) | 创建属性字符串数据对象。 |
| [void OH\_ArkUI\_StyledString\_Descriptor\_Destroy(ArkUI\_StyledString\_Descriptor\* descriptor)](#oh_arkui_styledstring_descriptor_destroy) | 释放被[ArkUI\_StyledString\_Descriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-styledstring-descriptor)对象占据的内存。 |
| [int32\_t OH\_ArkUI\_UnmarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor)](#oh_arkui_unmarshallstyledstringdescriptor) | 将包含属性字符串信息的字节数组反序列化为属性字符串。 |
| [int32\_t OH\_ArkUI\_MarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor, size\_t\* resultSize)](#oh_arkui_marshallstyledstringdescriptor) | 将属性字符串信息序列化为字节数组。 |
| [const char\* OH\_ArkUI\_ConvertToHtml(ArkUI\_StyledString\_Descriptor\* descriptor)](#oh_arkui_converttohtml) | 将属性字符串信息转换成html。 |
| [void OH\_ArkUI\_TextLayoutManager\_Dispose(ArkUI\_TextLayoutManager\* layoutManager)](#oh_arkui_textlayoutmanager_dispose) | 释放被文本布局管理器对象占据的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineCount(ArkUI\_TextLayoutManager\* layoutManager, int32\_t\* outLineCount)](#oh_arkui_textlayoutmanager_getlinecount) | 获取文本行数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetRectsForRange(ArkUI\_TextLayoutManager\* layoutManager, int32\_t start, int32\_t end, OH\_Drawing\_RectWidthStyle widthStyle, OH\_Drawing\_RectHeightStyle heightStyle, OH\_Drawing\_TextBox\*\* outTextBoxes)](#oh_arkui_textlayoutmanager_getrectsforrange) | 获取给定的矩形区域宽度样式以及高度样式的规格下，文本中任意区间范围内的字符或占位符所占的绘制区域信息。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate(ArkUI\_TextLayoutManager\* layoutManager, double dx, double dy, OH\_Drawing\_PositionAndAffinity\*\* outPos)](#oh_arkui_textlayoutmanager_getglyphpositionatcoordinate) | 获取距离给定坐标最近的字形的位置信息。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineMetrics(ArkUI\_TextLayoutManager\* layoutManager, int32\_t lineNumber, OH\_Drawing\_LineMetrics\* outMetrics)](#oh_arkui_textlayoutmanager_getlinemetrics) | 获取指定行的行信息、文本样式信息、以及字体属性信息。 |

#### 函数说明

#### \[h2\]OH\_ArkUI\_StyledString\_Create()

```c
ArkUI_StyledString* OH_ArkUI_StyledString_Create(OH_Drawing_TypographyStyle* style, OH_Drawing_FontCollection* collection)
```

**描述：**

创建指向ArkUI\_StyledString对象的指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typographystyle)\* style | 指向OH\_Drawing\_TypographyStyle的指针，由[OH\_Drawing\_CreateTypographyStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* collection | 指向OH\_Drawing\_FontCollection的指针，由[OH\_Drawing\_CreateFontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-collection-h#oh_drawing_createfontcollection)获取。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)\* | 创建指向ArkUI\_StyledString对象的指针。如果对象返回空指针，表示创建失败，失败的原因是地址空间已满，或者是style，collection参数异常如空指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_Destroy()

```c
void OH_ArkUI_StyledString_Destroy(ArkUI_StyledString* handle)
```

**描述：**

释放被ArkUI\_StyledString对象占据的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)\* handle | 指向ArkUI\_StyledString对象的指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_PushTextStyle()

```c
void OH_ArkUI_StyledString_PushTextStyle(ArkUI_StyledString* handle, OH_Drawing_TextStyle* style)
```

**描述：**

将新的排版风格设置到当前格式化字符串样式栈顶。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)\* handle | 指向ArkUI\_StyledString对象的指针。 |
| [OH\_Drawing\_TextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textstyle)\* style | 指向OH\_Drawing\_TextStyle对象的指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_AddText()

```c
void OH_ArkUI_StyledString_AddText(ArkUI_StyledString* handle, const char* content)
```

**描述：**

基于当前格式化字符串样式设置对应的文本内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)\* handle | 指向ArkUI\_StyledString对象的指针。 |
| const char\* content | 指向文本内容的指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_PopTextStyle()

```c
void OH_ArkUI_StyledString_PopTextStyle(ArkUI_StyledString* handle)
```

**描述：**

将当前格式化字符串对象中栈顶样式出栈。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)\* handle | 指向ArkUI\_StyledString对象的指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_CreateTypography()

```c
OH_Drawing_Typography* OH_ArkUI_StyledString_CreateTypography(ArkUI_StyledString* handle)
```

**描述：**

基于格式字符串对象创建指向OH\_Drawing\_Typography对象的指针，用于提前进行文本测算排版。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)\* handle | 指向ArkUI\_StyledString对象的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_Typography](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typography)\* | 指向OH\_Drawing\_Typography对象的指针。如果对象返回空指针，表示创建失败，失败的原因可能是handle参数异常如空指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_AddPlaceholder()

```c
void OH_ArkUI_StyledString_AddPlaceholder(ArkUI_StyledString* handle, OH_Drawing_PlaceholderSpan* placeholder)
```

**描述：**

设置占位符。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)\* handle | 指向ArkUI\_StyledString对象的指针。 |
| [OH\_Drawing\_PlaceholderSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-placeholderspan)\* placeholder | 指向OH\_Drawing\_PlaceholderSpan对象的指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_Descriptor\_Create()

```c
ArkUI_StyledString_Descriptor* OH_ArkUI_StyledString_Descriptor_Create(void)
```

**描述：**

创建属性字符串数据对象。

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_StyledString\_Descriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-styledstring-descriptor)\* | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |

#### \[h2\]OH\_ArkUI\_StyledString\_Descriptor\_Destroy()

```c
void OH_ArkUI_StyledString_Descriptor_Destroy(ArkUI_StyledString_Descriptor* descriptor)
```

**描述：**

释放被ArkUI\_StyledString\_Descriptor对象占据的内存。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString\_Descriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-styledstring-descriptor)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |

#### \[h2\]OH\_ArkUI\_UnmarshallStyledStringDescriptor()

```c
int32_t OH_ArkUI_UnmarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor)
```

**描述：**

将包含属性字符串信息的字节数组反序列化为属性字符串。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint8\_t\* buffer | 待反序列化的字节数组。 |
| size\_t bufferSize | 字节数组长度。 |
| [ArkUI\_StyledString\_Descriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-styledstring-descriptor)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_MarshallStyledStringDescriptor()

```c
int32_t OH_ArkUI_MarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor, size_t* resultSize)
```

**描述：**

将属性字符串信息序列化为字节数组。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint8\_t\* buffer | 字节数组，用于存储属性字符串序列化后的数据。 |
| size\_t bufferSize | 字节数组长度。 |
| [ArkUI\_StyledString\_Descriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-styledstring-descriptor)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |
| size\_t\* resultSize | 属性字符串转换后的字节数组实际长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

[ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 无效的属性字符串。

 |

#### \[h2\]OH\_ArkUI\_ConvertToHtml()

```c
const char* OH_ArkUI_ConvertToHtml(ArkUI_StyledString_Descriptor* descriptor)
```

**描述：**

将属性字符串信息转化成html。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_StyledString\_Descriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-styledstring-descriptor)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| const char\* | html。该指针由内部管理，在[OH\_ArkUI\_StyledString\_Descriptor\_Destroy()](#oh_arkui_styledstring_descriptor_destroy)时释放。 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_Dispose()

```c
void OH_ArkUI_TextLayoutManager_Dispose(ArkUI_TextLayoutManager* layoutManager)
```

**描述**

释放被文本布局管理器对象占据的内存。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetLineCount()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetLineCount(ArkUI_TextLayoutManager* layoutManager, int32_t* outLineCount)
```

**描述**

获取文本行数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| int32\_t\* outLineCount | 文本行数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) | 
返回结果。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetRectsForRange()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetRectsForRange(ArkUI_TextLayoutManager* layoutManager, int32_t start, int32_t end, OH_Drawing_RectWidthStyle widthStyle, OH_Drawing_RectHeightStyle heightStyle, OH_Drawing_TextBox** outTextBoxes)
```

**描述**

获取给定的矩形区域宽度样式以及高度样式的规格下，文本中任意区间范围内的字符或占位符所占的绘制区域信息。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| int32\_t start | 起始位置索引，start取值需要大于等于0，否则会返回参数异常。 |
| int32\_t end | 结束位置索引，end取值需要大于等于start，否则会返回参数异常。 |
| [OH\_Drawing\_RectWidthStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_rectwidthstyle) widthStyle | 矩形区域宽度样式。 |
| [OH\_Drawing\_RectHeightStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_rectheightstyle) heightStyle | 矩形区域高度样式。 |
| [OH\_Drawing\_TextBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textbox)\*\* outTextBoxes | 指向OH\_Drawing\_TextBox对象的二级指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) | 
返回结果。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetGlyphPositionAtCoordinate(ArkUI_TextLayoutManager* layoutManager, double dx, double dy, OH_Drawing_PositionAndAffinity** outPos)
```

**描述**

获取距离给定坐标最近的字形的位置信息。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| double dx | 相对于控件的x坐标，单位为px。 |
| double dy | 相对于控件的y坐标，单位为px。 |
| [OH\_Drawing\_PositionAndAffinity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-positionandaffinity)\*\* outPos | 指向OH\_Drawing\_PositionAndAffinity对象的二级指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) | 
返回结果。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetLineMetrics()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetLineMetrics(ArkUI_TextLayoutManager* layoutManager, int32_t lineNumber, OH_Drawing_LineMetrics* outMetrics)
```

**描述**

获取指定行的行信息、文本样式信息、以及字体属性信息。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| int32\_t lineNumber | 指定行的行号索引，行号索引从0开始计数，lineNumber小于0或大于等于文本行数时会返回参数异常。 |
| [OH\_Drawing\_LineMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-linemetrics)\* outMetrics | 指向OH\_Drawing\_LineMetrics对象的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) | 
返回结果。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |
