---
title: "在自绘编辑框中使用输入法开发指导 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-custom-edit-box-ndk"
menu_path:
  - "指南"
  - "应用框架"
  - "IME Kit（输入法开发服务）"
  - "在自绘编辑框中使用输入法开发指导 (C/C++)"
captured_at: "2026-04-17T01:35:45.456Z"
---

# 在自绘编辑框中使用输入法开发指导 (C/C++)

#### 场景介绍

IME Kit支持开发者在自绘编辑框中使用输入法，与输入法应用交互，包括显示、隐藏输入法，接收来自输入法应用的文本编辑操作通知等，本文档介绍开发者如何使用C/C++完成此功能开发。

#### 接口说明

详细接口说明请参考[InputMethod接口文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod)。

#### 添加动态链接库

CMakeLists.txt中添加以下lib。

```txt
libohinputmethod.so
```

#### 引用头文件

```c
#include <inputmethod/inputmethod_controller_capi.h>
```

#### 绑定输入法

开发者需要在输入框获焦时，通过调用接口[OH\_InputMethodController\_Attach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-controller-capi-h#oh_inputmethodcontroller_attach)绑定输入法，绑定成功后用户可以通过输入法输入文字。

1.  创建InputMethod\_TextEditorProxy实例，示例代码如下所示：
    
    // 创建InputMethod\_TextEditorProxy实例
    textEditorProxy = OH\_TextEditorProxy\_Create();
    
2.  创建InputMethod\_AttachOptions实例，设置绑定输入法时的选项。示例代码如下所示：
    
    // 创建InputMethod\_AttachOptions实例，选项showKeyboard用于指定此次绑定成功后是否显示键盘，此处以目标显示键盘为例
    bool showKeyboard = true;
    attachOptions = OH\_AttachOptions\_Create(showKeyboard);
    
3.  调用OH\_InputMethodController\_Attach发起绑定输入法服务，调用成功后，可以获取到用于和输入法交互的InputMethod\_InputMethodProxy。示例代码如下所示：
    
    // 发起绑定请求
    auto ret = OH\_InputMethodController\_Attach(textEditorProxy, attachOptions, &inputMethodProxy);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Attach failed, ret=%{public}d.", ret);
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        OH\_AttachOptions\_Destroy(attachOptions);
        return;
    }
    

#### 显示/隐藏面板功能

绑定成功后，可以使用获取到的[InputMethod\_InputMethodProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-inputmethodproxy)对象向输入法发送消息。示例代码如下所示：

```c
// 显示键盘
if (OH_InputMethodProxy_ShowKeyboard(inputMethodProxy) != InputMethod_ErrorCode::IME_ERR_OK) {
    OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "ShowKeyboard failed!");
}
// 隐藏键盘
if (OH_InputMethodProxy_HideKeyboard(inputMethodProxy) != InputMethod_ErrorCode::IME_ERR_OK) {
    OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "HideKeyboard failed!");
}
// 通知输入框配置信息变化
if (OH_InputMethodProxy_NotifyConfigurationChange(inputMethodProxy, InputMethod_EnterKeyType::IME_ENTER_KEY_GO, InputMethod_TextInputType::IME_TEXT_INPUT_TYPE_TEXT) != InputMethod_ErrorCode::IME_ERR_OK) {
    OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "NotifyConfigurationChange failed!");
}
```

#### 监听输入法应用的请求/通知

1.  需要先实现对输入法应用发送的请求或通知的响应处理函数，示例代码如下所示：
    
    ```c
    // 实现InputMethod_TextEditorProxy中的输入法应用事件响应函数
    void GetTextConfig(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_TextConfig *config)
    {
        // 处理输入法发送的获取输入框配置请求
    }
    void InsertText(InputMethod_TextEditorProxy *textEditorProxy, const char16_t *text, size_t length)
    {
        // 处理输入法发送的插入文本请求
    }
    void DeleteForward(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
    {
        // 处理输入法发送的删除文本请求
    }
    // ......
    ```
    
2.  将实现后的响应函数，设置到[InputMethod\_TextEditorProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-texteditorproxy)中，再通过绑定输入法时调用的[OH\_InputMethodController\_Attach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-controller-capi-h#oh_inputmethodcontroller_attach)将其设置到输入法框架中，完成监听注册。示例代码如下所示：
    
    OH\_TextEditorProxy\_SetGetTextConfigFunc(textEditorProxy, GetTextConfigFunc);
    OH\_TextEditorProxy\_SetInsertTextFunc(textEditorProxy, InsertTextFunc);
    OH\_TextEditorProxy\_SetDeleteForwardFunc(textEditorProxy, DeleteForwardFunc);
    OH\_TextEditorProxy\_SetDeleteBackwardFunc(textEditorProxy, DeleteBackwardFunc);
    OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(textEditorProxy, SendKeyboardStatusFunc);
    OH\_TextEditorProxy\_SetSendEnterKeyFunc(textEditorProxy, SendEnterKeyFunc);
    OH\_TextEditorProxy\_SetMoveCursorFunc(textEditorProxy, MoveCursorFunc);
    OH\_TextEditorProxy\_SetHandleSetSelectionFunc(textEditorProxy, HandleSetSelectionFunc);
    OH\_TextEditorProxy\_SetHandleExtendActionFunc(textEditorProxy, HandleExtendActionFunc);
    OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(textEditorProxy, GetLeftTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(textEditorProxy, GetRightTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(textEditorProxy, GetTextIndexAtCursorFunc);
    OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(textEditorProxy, ReceivePrivateCommandFunc);
    OH\_TextEditorProxy\_SetSetPreviewTextFunc(textEditorProxy, SetPreviewTextFunc);
    OH\_TextEditorProxy\_SetFinishTextPreviewFunc(textEditorProxy, FinishTextPreviewFunc);
    

#### 解绑输入法

当编辑框失焦，需要结束使用输入法，通过接口[OH\_InputMethodController\_Detach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-controller-capi-h#oh_inputmethodcontroller_detach)与输入法框架解绑。

// 发起解绑请求
OH\_InputMethodController\_Detach(inputMethodProxy);
OH\_TextEditorProxy\_Destroy(textEditorProxy);
OH\_AttachOptions\_Destroy(attachOptions);

#### 完整示例

示例代码展示了绑定输入法、隐藏输入法、解绑输入法的完整流程。

示例代码总入口为InputMethodNdkDemo函数。

说明：

需要在CMakeList.txt中添加libohinputmethod.so libhilog\_ndk.z.so依赖。

#include "napi/native\_api.h"
#include <codecvt>
#include <locale>
#include <thread>

#include "hilog/log.h"
#include "inputmethod/inputmethod\_controller\_capi.h"

 constexpr int32\_t TEXTSIZE = 1024;

static std::string g\_strText;
char g\_strTextChar\[TEXTSIZE\];
int32\_t g\_strTextCharLen = 0;
bool g\_flagShow = false;
std::mutex g\_textMutex;
InputMethod\_TextEditorProxy \*textEditorProxy = nullptr;
InputMethod\_AttachOptions \*attachOptions = nullptr;
InputMethod\_InputMethodProxy \*inputMethodProxy = nullptr;

void InputMethodDestroy();

void InitText()
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    if (g\_flagShow) {
        memset(g\_strTextChar, 0x00, sizeof(g\_strTextChar));
        g\_strTextCharLen = 0;
        g\_flagShow = false;
    }
}

void SetText(const char\* input)
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    g\_strTextCharLen = strlen(input);
    if (g\_strTextCharLen > TEXTSIZE) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Length greater than 1024 , ret=%{public}d", g\_strTextCharLen);
    }
    strncpy(g\_strTextChar, input, g\_strTextCharLen);
}

void GetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_TextConfig \*config)
{ // 处理获取输入框配置请求
    auto ret = OH\_TextConfig\_SetEnterKeyType(config, InputMethod\_EnterKeyType::IME\_ENTER\_KEY\_SEND);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "SetEnterKeyType failed, ret=%{public}d", ret);
        return;
    }

    ret = OH\_TextConfig\_SetInputType(config, InputMethod\_TextInputType::IME\_TEXT\_INPUT\_TYPE\_PHONE);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "SetInputType failed, ret=%{public}d", ret);
        return;
    }
}

void InsertTextFunc(InputMethod\_TextEditorProxy \*proxy, const char16\_t \*text, size\_t length)
{
    InitText();

    // 处理插入文本请求
    // 将char16\_t类型的字符串转换为u16string
    std::u16string u16Str(text, length + 1);

    // 转换为UTF-8编码的string
    std::wstring\_convert<std::codecvt\_utf8\_utf16<char16\_t>, char16\_t> converter;
    std::string utf8Str = converter.to\_bytes(u16Str);
    for (size\_t i = 0; i < utf8Str.size(); ++i) {
        unsigned char c = static\_cast<unsigned char>(utf8Str\[i\]);
        if (c != 0x00) {
            std::lock\_guard<std::mutex> lock(g\_textMutex);
            g\_strTextChar\[g\_strTextCharLen\] = c;
            g\_strTextCharLen += 1;
        }
    }
}

void DeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t length)
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    if (g\_strTextCharLen > 0) {
        strncpy(g\_strTextChar, g\_strTextChar + 1, g\_strTextCharLen - 1);
        g\_strTextCharLen = (g\_strTextCharLen > 0) ? g\_strTextCharLen - 1 : g\_strTextCharLen;
    }
}

void DeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t length)
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    g\_strTextCharLen = (g\_strTextCharLen > 0) ? g\_strTextCharLen - 1 : g\_strTextCharLen;
    g\_strTextChar\[g\_strTextCharLen\] = '\\0';
}

void SendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_KeyboardStatus status)
{
    if (status == InputMethod\_KeyboardStatus::IME\_KEYBOARD\_STATUS\_HIDE) {
        g\_flagShow = false;
        SetText("键盘已经被隐藏");
    } else if (status == InputMethod\_KeyboardStatus::IME\_KEYBOARD\_STATUS\_SHOW && g\_flagShow != true) {
        g\_flagShow = true;
        SetText("键盘已经被拉起");
    }
}

void SendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_EnterKeyType type)
{
    SetText("处理回车键请求事件");
    g\_flagShow = true;
}

void MoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_Direction direction)
{
    if (direction == InputMethod\_Direction::IME\_DIRECTION\_UP) {
        SetText("光标正在向 上 移动");
    } else if (direction == InputMethod\_Direction::IME\_DIRECTION\_DOWN) {
        SetText("光标正在向 下 移动");
    } else if (direction == InputMethod\_Direction::IME\_DIRECTION\_LEFT) {
        SetText("光标正在向 左 移动");
    } else if (direction == InputMethod\_Direction::IME\_DIRECTION\_RIGHT) {
        SetText("光标正在向 右  移动");
    } else {
        SetText("光标移动 出现错误");
    }
}

void HandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t start, int32\_t end)
{
    SetText("处理选中文本请求");
}

void HandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_ExtendAction action)
{
    SetText("处理扩展编辑请求");
}

void GetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t number, char16\_t text\[\], size\_t \*length)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "处理获取光标左侧文本请求  ...");
}

void GetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t number, char16\_t text\[\], size\_t \*length)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "处理获取光标右侧文本请求  ...");
}

int32\_t GetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "处理获取光标所在输入框文本索引请求  ...");
    return 0;
}
int32\_t ReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_PrivateCommand \*privateCommand\[\],
    size\_t size)
{
    SetText("处理扩展编辑请求");
    return 0;
}

int32\_t SetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, const char16\_t \*text, size\_t length, int32\_t start,
    int32\_t end)
{
    SetText("处理设置预上屏文本请求");
    return 0;
}

void FinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy)
{
    SetText("处理结束预上屏请求");
}

void ConstructTextEditorProxy(InputMethod\_TextEditorProxy \*textEditorProxy)
{
    OH\_TextEditorProxy\_SetGetTextConfigFunc(textEditorProxy, GetTextConfigFunc);
    OH\_TextEditorProxy\_SetInsertTextFunc(textEditorProxy, InsertTextFunc);
    OH\_TextEditorProxy\_SetDeleteForwardFunc(textEditorProxy, DeleteForwardFunc);
    OH\_TextEditorProxy\_SetDeleteBackwardFunc(textEditorProxy, DeleteBackwardFunc);
    OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(textEditorProxy, SendKeyboardStatusFunc);
    OH\_TextEditorProxy\_SetSendEnterKeyFunc(textEditorProxy, SendEnterKeyFunc);
    OH\_TextEditorProxy\_SetMoveCursorFunc(textEditorProxy, MoveCursorFunc);
    OH\_TextEditorProxy\_SetHandleSetSelectionFunc(textEditorProxy, HandleSetSelectionFunc);
    OH\_TextEditorProxy\_SetHandleExtendActionFunc(textEditorProxy, HandleExtendActionFunc);
    OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(textEditorProxy, GetLeftTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(textEditorProxy, GetRightTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(textEditorProxy, GetTextIndexAtCursorFunc);
    OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(textEditorProxy, ReceivePrivateCommandFunc);
    OH\_TextEditorProxy\_SetSetPreviewTextFunc(textEditorProxy, SetPreviewTextFunc);
    OH\_TextEditorProxy\_SetFinishTextPreviewFunc(textEditorProxy, FinishTextPreviewFunc);
}

void InputMethodNdkDemo()
{
    // 创建InputMethod\_TextEditorProxy实例
    textEditorProxy = OH\_TextEditorProxy\_Create();
    if (textEditorProxy == nullptr) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Create TextEditorProxy failed.");
        return;
    }

    // 将实现好的响应处理函数设置到InputMethod\_TextEditorProxy中
    ConstructTextEditorProxy(textEditorProxy);

    // 创建InputMethod\_AttachOptions实例，选项showKeyboard用于指定此次绑定成功后是否显示键盘，此处以目标显示键盘为例
    bool showKeyboard = true;
    attachOptions = OH\_AttachOptions\_Create(showKeyboard);
    if (attachOptions == nullptr) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Create AttachOptions failed.");
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        return;
    }

    // 发起绑定请求
    auto ret = OH\_InputMethodController\_Attach(textEditorProxy, attachOptions, &inputMethodProxy);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Attach failed, ret=%{public}d.", ret);
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        OH\_AttachOptions\_Destroy(attachOptions);
        return;
    }
}

static napi\_value InputMethodDestroy(napi\_env env, napi\_callback\_info info)
{
   // 隐藏键盘
    int ret = OH\_InputMethodProxy\_HideKeyboard(inputMethodProxy);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "HideKeyboard failed, ret=%{public}d.", ret);
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        OH\_AttachOptions\_Destroy(attachOptions);
        return nullptr;
    }

    // 发起解绑请求
    OH\_InputMethodController\_Detach(inputMethodProxy);
    OH\_TextEditorProxy\_Destroy(textEditorProxy);
    OH\_AttachOptions\_Destroy(attachOptions);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "Finished.");
    return nullptr;
}

static napi\_value AttachInputMethod(napi\_env env, napi\_callback\_info info)
{
    InputMethodNdkDemo();

    napi\_value result;
    napi\_create\_string\_utf8(env,  g\_strText.c\_str(),  g\_strText.length(),  &result);
    return result;
}

static napi\_value GetText(napi\_env env, napi\_callback\_info info)
{
    napi\_value result;
    napi\_create\_string\_utf8(env, g\_strTextChar, g\_strTextCharLen,  &result);
    return result;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        { "attachInputMethod", nullptr, AttachInputMethod, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "getText", nullptr, GetText, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "inputMethodDestroy", nullptr, InputMethodDestroy, nullptr, nullptr, nullptr, napi\_default, nullptr },
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}
