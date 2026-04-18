---
title: "安全导入密钥(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-wrapped-key-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "本地密钥管理"
  - "密钥生成/导入"
  - "密钥导入"
  - "安全导入密钥(C/C++)"
captured_at: "2026-04-17T01:35:51.246Z"
---

# 安全导入密钥(C/C++)

以安全导入ECDH密钥对为例，涉及业务侧加密密钥的[密钥生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)、[协商](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-overview)等操作不在本示例中体现。

具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview#支持的算法)。

#### 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

#### 开发步骤

1.  设备A（导入设备）将待导入密钥转换成[HUKS密钥材料格式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-concepts#密钥材料格式)To\_Import\_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤）。
    
2.  设备B（被导入设备）生成一个安全导入用途的非对称密钥对Wrapping\_Key（公钥Wrapping\_Pk，私钥Wrapping\_Sk），导出Wrapping\_Key的公钥材料Wrapping\_Pk发送给设备A。
    
3.  设备A使用和设备B同样的算法，生成一个用于协商的非对称密钥对Caller\_Key（公钥Caller\_Pk，私钥Caller\_Sk），导出Caller\_Key的公钥材料Caller\_Pk并保存。
    
4.  设备A生成一个对称密钥Caller\_Kek，该密钥用于加密To\_Import\_Key生成To\_Import\_Key\_Enc。
    
5.  设备A基于Caller\_Key的私钥Caller\_Sk和设备B Wrapping\_Key的公钥Wrapping\_Pk，协商出Shared\_Key，使用Shared\_Key加密Caller\_Kek，生成Caller\_Kek\_Enc。
    
6.  设备A封装Caller\_Pk、Caller\_Kek\_Enc、To\_Import\_Key\_Enc等安全导入的密钥材料并发送给设备B，安全导入密钥材料格式见[安全导入密钥材料格式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview#安全导入密钥材料格式)。
    
7.  设备B导入封装的加密密钥材料。
    
8.  设备A、B删除用于安全导入的密钥。
    

#### 开发案例

构造安全导入密钥的参数集

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <algorithm>

#define MAX\_MALLOC\_SIZE 0x800000

OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet, const struct OH\_Huks\_Param \*params,
                            uint32\_t paramCount)
{
    OH\_Huks\_Result ret = OH\_Huks\_InitParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_AddParams(\*paramSet, params, paramCount);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        return ret;
    }
    ret = OH\_Huks\_BuildParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        return ret;
    }
    return ret;
}
struct HksImportWrappedKeyTestParams {
    // server key, for real.
    struct OH\_Huks\_Blob \*wrappingKeyAlias;
    struct OH\_Huks\_ParamSet \*genWrappingKeyParamSet;
    uint32\_t publicKeySize;
    struct OH\_Huks\_Blob \*callerKeyAlias;
    struct OH\_Huks\_ParamSet \*genCallerKeyParamSet;
    struct OH\_Huks\_Blob \*callerKekAlias;
    struct OH\_Huks\_Blob \*callerKek;
    struct OH\_Huks\_ParamSet \*importCallerKekParamSet;
    struct OH\_Huks\_Blob \*callerAgreeKeyAlias;
    struct OH\_Huks\_ParamSet \*agreeParamSet;
    struct OH\_Huks\_ParamSet \*importWrappedKeyParamSet;
    struct OH\_Huks\_Blob \*importedKeyAlias;
    struct OH\_Huks\_Blob \*importedPlainKey;
    uint32\_t keyMaterialLen;
};
static const uint32\_t IV\_SIZE = 16;
static uint8\_t IV\[IV\_SIZE\] = "bababababababab"; // 此处仅为测试数据，实际使用时该值每次应该不同。
static const uint32\_t WRAPPED\_KEY\_IV\_SIZE = 16;
static uint8\_t WRAPPED\_KEY\_IV\[IV\_SIZE\] = "bababababababab"; // 此处仅为测试数据，实际使用时该值每次应该不同。
static const uint32\_t AAD\_SIZE = 16;
static uint8\_t AAD\[AAD\_SIZE\] = "abababababababa"; // 此处仅为测试数据，实际使用时该值每次应该不同。
static const uint32\_t NONCE\_SIZE = 12;
static uint8\_t NONCE\[NONCE\_SIZE\] = "hahahahahah"; // 此处仅为测试数据，实际使用时该值每次应该不同。
static const uint32\_t AEAD\_TAG\_SIZE = 16;
static const uint32\_t X25519\_256\_SIZE = 256;
static struct OH\_Huks\_Blob g\_wrappingKeyAliasAes256 = {.size = (uint32\_t)strlen("test\_wrappingKey\_x25519\_aes256"),
                                                       .data = (uint8\_t \*)"test\_wrappingKey\_x25519\_aes256"};
static struct OH\_Huks\_Blob g\_callerKeyAliasAes256 = {.size = (uint32\_t)strlen("test\_caller\_key\_x25519\_aes256"),
                                                     .data = (uint8\_t \*)"test\_caller\_key\_x25519\_aes256"};
static struct OH\_Huks\_Blob g\_callerKekAliasAes256 = {.size = (uint32\_t)strlen("test\_caller\_kek\_x25519\_aes256"),
                                                     .data = (uint8\_t \*)"test\_caller\_kek\_x25519\_aes256"};
static struct OH\_Huks\_Blob g\_callerAes256Kek = {.size = (uint32\_t)strlen("This is kek to encrypt plain key"),
                                                .data = (uint8\_t \*)"This is kek to encrypt plain key"};
static struct OH\_Huks\_Blob g\_callerAgreeKeyAliasAes256 = {.size =
                                                              (uint32\_t)strlen("test\_caller\_agree\_key\_x25519\_aes256"),
                                                          .data = (uint8\_t \*)"test\_caller\_agree\_key\_x25519\_aes256"};
static struct OH\_Huks\_Blob g\_importedKeyAliasAes256 = {.size = (uint32\_t)strlen("test\_import\_key\_x25519\_aes256"),
                                                       .data = (uint8\_t \*)"test\_import\_key\_x25519\_aes256"};
static struct OH\_Huks\_Blob g\_importedAes256PlainKey = {.size = (uint32\_t)strlen("This is plain key to be imported"),
                                                       .data = (uint8\_t \*)"This is plain key to be imported"};

static struct OH\_Huks\_Param g\_importWrappedAes256Params\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT | OH\_HUKS\_KEY\_PURPOSE\_DECRYPT},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_GCM},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE},
    {.tag = OH\_HUKS\_TAG\_UNWRAP\_ALGORITHM\_SUITE, .uint32Param = OH\_HUKS\_UNWRAP\_SUITE\_X25519\_AES\_256\_GCM\_NOPADDING},
    {.tag = OH\_HUKS\_TAG\_ASSOCIATED\_DATA,
     .blob = {.size = AAD\_SIZE, .data = (uint8\_t \*)AAD}}, // 此处仅为测试数据，实际使用时该值应与调用者信息相关。
    {.tag = OH\_HUKS\_TAG\_NONCE,
     .blob = {.size = NONCE\_SIZE, .data = (uint8\_t \*)NONCE}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。
static const uint32\_t g\_x25519PubKeySize = 32;
static struct OH\_Huks\_Param g\_genWrappingKeyParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_UNWRAP},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_genCallerX25519Params\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_importParamsCallerKek\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_GCM},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE},
    {.tag = OH\_HUKS\_TAG\_IV,
     .blob = {.size = WRAPPED\_KEY\_IV\_SIZE,
              .data = (uint8\_t \*)WRAPPED\_KEY\_IV}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。
static struct OH\_Huks\_Param g\_callerAgreeParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_aesKekEncryptParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_GCM},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE},
    {.tag = OH\_HUKS\_TAG\_ASSOCIATED\_DATA,
     .blob = {.size = AAD\_SIZE, .data = (uint8\_t \*)AAD}}, // 此处仅为测试数据，实际使用时该值应与调用者信息相关。
    {.tag = OH\_HUKS\_TAG\_NONCE,
     .blob = {.size = NONCE\_SIZE, .data = (uint8\_t \*)NONCE}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。
static struct OH\_Huks\_Param g\_importAgreeKeyParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_GCM},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE},
    {.tag = OH\_HUKS\_TAG\_IV,
     .blob = {.size = IV\_SIZE, .data = (uint8\_t \*)IV}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。

安全导入密钥的核心函数实现

OH\_Huks\_Result HuksAgreeKey(const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*keyAlias,
                            const struct OH\_Huks\_Blob \*peerPublicKey, struct OH\_Huks\_Blob \*agreedKey)
{
    uint8\_t temp\[10\] = {0};
    struct OH\_Huks\_Blob inData = {sizeof(temp), temp};
    uint8\_t handleU\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleU};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, paramSet, &handle, nullptr);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint8\_t outDataU\[1024\] = {0};
    struct OH\_Huks\_Blob outDataUpdate = {1024, outDataU};
    ret = OH\_Huks\_UpdateSession(&handle, paramSet, peerPublicKey, &outDataUpdate);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, paramSet, &inData, agreedKey);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}

OH\_Huks\_Result MallocAndCheckBlobData(struct OH\_Huks\_Blob \*blob, const uint32\_t blobSize)
{
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    if (blobSize == 0 || blobSize > MAX\_MALLOC\_SIZE) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
    }
    blob->data = (uint8\_t \*)malloc(blobSize);
    if (blob->data == NULL) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
    }
    return ret;
}

static const uint32\_t TIMES = 4;
static const uint32\_t MAX\_UPDATE\_SIZE = 64;
static const uint32\_t MAX\_OUTDATA\_SIZE = MAX\_UPDATE\_SIZE \* TIMES;
#define HUKS\_FREE\_BLOB(blob)                                                                                           \\
    do {                                                                                                               \\
        if ((blob).data != nullptr) {                                                                                  \\
            free((blob).data);                                                                                         \\
            (blob).data = nullptr;                                                                                     \\
        }                                                                                                              \\
        (blob).size = 0;                                                                                               \\
    } while (0)
#define OH\_HUKS\_KEY\_BYTES(keySize) (((keySize) + 7) / 8)
static OH\_Huks\_Result HksEncryptLoopUpdate(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet,
                                           const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)
{
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    struct OH\_Huks\_Blob inDataSeg = \*inData;
    uint8\_t \*lastPtr = inData->data + inData->size - 1;
    struct OH\_Huks\_Blob outDataSeg = {MAX\_OUTDATA\_SIZE, NULL};
    uint8\_t \*cur = outData->data;
    outData->size = 0;
    inDataSeg.size = MAX\_UPDATE\_SIZE;
    bool isFinished = false;
    while (inDataSeg.data <= lastPtr) {
        if (inDataSeg.data + MAX\_UPDATE\_SIZE <= lastPtr) {
            outDataSeg.size = MAX\_OUTDATA\_SIZE;
        } else {
            isFinished = true;
            inDataSeg.size = lastPtr - inDataSeg.data + 1;
            break;
        }
        if (MallocAndCheckBlobData(&outDataSeg, outDataSeg.size).errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
            ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
            return ret;
        }
        ret = OH\_Huks\_UpdateSession(handle, paramSet, &inDataSeg, &outDataSeg);
        if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
            free(outDataSeg.data);
            return ret;
        }
        std::copy(outDataSeg.data, outDataSeg.data + outDataSeg.size, cur);
        cur += outDataSeg.size;
        outData->size += outDataSeg.size;
        free(outDataSeg.data);
        if ((isFinished == false) && (inDataSeg.data + MAX\_UPDATE\_SIZE > lastPtr)) {
            ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
            return ret;
        }
        inDataSeg.data += MAX\_UPDATE\_SIZE;
    }
    struct OH\_Huks\_Blob outDataFinish = {inDataSeg.size \* TIMES, NULL};
    if (MallocAndCheckBlobData(&outDataFinish, outDataFinish.size).errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
        return ret;
    }
    ret = OH\_Huks\_FinishSession(handle, paramSet, &inDataSeg, &outDataFinish);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        free(outDataFinish.data);
        return ret;
    }
    std::copy(outDataFinish.data, outDataFinish.data + outDataFinish.size, cur);
    outData->size += outDataFinish.size;
    free(outDataFinish.data);
    return ret;
}
OH\_Huks\_Result HuksEncrypt(const struct OH\_Huks\_Blob \*key, const struct OH\_Huks\_ParamSet \*paramSet,
                           const struct OH\_Huks\_Blob \*plainText, struct OH\_Huks\_Blob \*cipherText)
{
    uint8\_t handle\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleBlob = {sizeof(uint64\_t), handle};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(key, paramSet, &handleBlob, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = HksEncryptLoopUpdate(&handleBlob, paramSet, plainText, cipherText);
    return ret;
}
static OH\_Huks\_Result BuildWrappedKeyData(struct OH\_Huks\_Blob \*\*blobArray, uint32\_t size,
                                          struct OH\_Huks\_Blob \*outData)
{
    uint32\_t totalLength = size \* sizeof(uint32\_t);
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    /\* 计算大小 \*/
    for (uint32\_t i = 0; i < size; ++i) {
        totalLength += blobArray\[i\]->size;
    }
    struct OH\_Huks\_Blob outBlob = {0, nullptr};
    outBlob.size = totalLength;
    ret = MallocAndCheckBlobData(&outBlob, outBlob.size);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint32\_t offset = 0;
    /\* 拷贝数据 \*/
    for (uint32\_t i = 0; i < size; ++i) {
        if (totalLength - offset >= sizeof(blobArray\[i\]->size)) {
            std::copy(reinterpret\_cast<uint8\_t \*>(&blobArray\[i\]->size),
                      reinterpret\_cast<uint8\_t \*>(&blobArray\[i\]->size) + sizeof(blobArray\[i\]->size),
                      outBlob.data + offset);
        } else {
            ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
            return ret;
        }
        offset += sizeof(blobArray\[i\]->size);
        if (totalLength - offset >= blobArray\[i\]->size) {
            std::copy(blobArray\[i\]->data, blobArray\[i\]->data + blobArray\[i\]->size, outBlob.data + offset);
        } else {
            ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
            return ret;
        }
        offset += blobArray\[i\]->size;
    }
    outData->size = outBlob.size;
    outData->data = outBlob.data;
    return ret;
}

static OH\_Huks\_Result CheckParamsValid(const struct HksImportWrappedKeyTestParams \*params)
{
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    if (params == nullptr) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT;
        return ret;
    }
    if (params->wrappingKeyAlias == nullptr || params->genWrappingKeyParamSet == nullptr ||
        params->callerKeyAlias == nullptr || params->genCallerKeyParamSet == nullptr ||
        params->callerKekAlias == nullptr || params->callerKek == nullptr ||
        params->importCallerKekParamSet == nullptr || params->callerAgreeKeyAlias == nullptr ||
        params->agreeParamSet == nullptr || params->importWrappedKeyParamSet == nullptr ||
        params->importedKeyAlias == nullptr || params->importedPlainKey == nullptr) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT;
        return ret;
    }
    return ret;
}

static OH\_Huks\_Result GenerateAndExportHuksPublicKey(const struct HksImportWrappedKeyTestParams \*params,
                                                     struct OH\_Huks\_Blob \*huksPublicKey)
{
    OH\_Huks\_Result ret = OH\_Huks\_GenerateKeyItem(params->wrappingKeyAlias, params->genWrappingKeyParamSet, nullptr);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    huksPublicKey->size = params->publicKeySize;
    ret = MallocAndCheckBlobData(huksPublicKey, huksPublicKey->size);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(params->wrappingKeyAlias, nullptr, huksPublicKey);
    return ret;
}
static OH\_Huks\_Result GenerateAndExportCallerPublicKey(const struct HksImportWrappedKeyTestParams \*params,
                                                       struct OH\_Huks\_Blob \*callerSelfPublicKey)
{
    OH\_Huks\_Result ret = OH\_Huks\_GenerateKeyItem(params->callerKeyAlias, params->genCallerKeyParamSet, nullptr);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    callerSelfPublicKey->size = params->publicKeySize;
    ret = MallocAndCheckBlobData(callerSelfPublicKey, callerSelfPublicKey->size);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(params->callerKeyAlias, params->genWrappingKeyParamSet, callerSelfPublicKey);
    return ret;
}

static OH\_Huks\_Result ImportKekAndAgreeSharedSecret(const struct HksImportWrappedKeyTestParams \*params,
                                                    const struct OH\_Huks\_Blob \*huksPublicKey,
                                                    struct OH\_Huks\_Blob \*outSharedKey)
{
    OH\_Huks\_Result ret =
        OH\_Huks\_ImportKeyItem(params->callerKekAlias, params->importCallerKekParamSet, params->callerKek);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = MallocAndCheckBlobData(outSharedKey, outSharedKey->size);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = HuksAgreeKey(params->agreeParamSet, params->callerKeyAlias, huksPublicKey, outSharedKey);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    struct OH\_Huks\_ParamSet \*importAgreeKeyParams = nullptr;
    ret = InitParamSet(&importAgreeKeyParams, g\_importAgreeKeyParams,
                       sizeof(g\_importAgreeKeyParams) / sizeof(OH\_Huks\_Param));
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ImportKeyItem(params->callerAgreeKeyAlias, importAgreeKeyParams, outSharedKey);
    OH\_Huks\_FreeParamSet(&importAgreeKeyParams);
    return ret;
}
static OH\_Huks\_Result EncryptImportedPlainKeyAndKek(const struct HksImportWrappedKeyTestParams \*params,
                                                    struct OH\_Huks\_Blob \*plainCipherText,
                                                    struct OH\_Huks\_Blob \*kekCipherText)
{
    struct OH\_Huks\_ParamSet \*encryptParamSet = nullptr;
    OH\_Huks\_Result ret =
        InitParamSet(&encryptParamSet, g\_aesKekEncryptParams, sizeof(g\_aesKekEncryptParams) / sizeof(OH\_Huks\_Param));
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = HuksEncrypt(params->callerKekAlias, encryptParamSet, params->importedPlainKey, plainCipherText);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = HuksEncrypt(params->callerAgreeKeyAlias, encryptParamSet, params->callerKek, kekCipherText);
    OH\_Huks\_FreeParamSet(&encryptParamSet);
    return ret;
}
static OH\_Huks\_Result ImportWrappedKey(const struct HksImportWrappedKeyTestParams \*params,
                                       struct OH\_Huks\_Blob \*plainCipher, struct OH\_Huks\_Blob \*kekCipherText,
                                       struct OH\_Huks\_Blob \*peerPublicKey, struct OH\_Huks\_Blob \*wrappedKeyData)
{
    struct OH\_Huks\_Blob commonAad = {.size = AAD\_SIZE, .data = reinterpret\_cast<uint8\_t \*>(AAD)};
    struct OH\_Huks\_Blob commonNonce = {.size = NONCE\_SIZE, .data = reinterpret\_cast<uint8\_t \*>(NONCE)};
    struct OH\_Huks\_Blob keyMaterialLen = {.size = sizeof(uint32\_t), .data = (uint8\_t \*)&params->keyMaterialLen};
    /\* 从密文中拷贝AEAD的tag并缩小其大小 \*/
    const uint32\_t tagSize = AEAD\_TAG\_SIZE;
    uint8\_t kekTagBuf\[tagSize\] = {0};
    struct OH\_Huks\_Blob kekTag = {.size = tagSize, .data = kekTagBuf};
    std::copy(plainCipher->data + (plainCipher->size - tagSize),
              plainCipher->data + (plainCipher->size - tagSize) + tagSize, kekTag.data);
    plainCipher->size -= tagSize;
    /\* 从密钥加密密钥的密文中拷贝AEAD的tag并缩小其大小 \*/
    uint8\_t agreeKeyTagBuf\[tagSize\] = {0};
    struct OH\_Huks\_Blob agreeKeyTag = {.size = tagSize, .data = agreeKeyTagBuf};
    std::copy(kekCipherText->data + (kekCipherText->size - tagSize),
              kekCipherText->data + (kekCipherText->size - tagSize) + tagSize, agreeKeyTagBuf);
    kekCipherText->size -= tagSize;
    struct OH\_Huks\_Blob \*blobArray\[\] = {peerPublicKey, &commonAad,   &commonNonce, &agreeKeyTag,    kekCipherText,
                                        &commonAad,    &commonNonce, &kekTag,      &keyMaterialLen, plainCipher};
    OH\_Huks\_Result ret = BuildWrappedKeyData(blobArray, OH\_HUKS\_IMPORT\_WRAPPED\_KEY\_TOTAL\_BLOBS, wrappedKeyData);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    struct OH\_Huks\_Param \*purpose = nullptr;
    ret = OH\_Huks\_GetParam(params->importWrappedKeyParamSet, OH\_HUKS\_TAG\_PURPOSE, &purpose);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ImportWrappedKeyItem(params->importedKeyAlias, params->wrappingKeyAlias,
                                       params->importWrappedKeyParamSet, wrappedKeyData);
    return ret;
}

安全导入密钥的完整流程实现

OH\_Huks\_Result HksImportWrappedKeyTestCommonCase(const struct HksImportWrappedKeyTestParams \*params)
{
    OH\_Huks\_Result ret = CheckParamsValid(params);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return ret;
    }
    struct OH\_Huks\_Blob huksPublicKey = {0, nullptr};
    struct OH\_Huks\_Blob callerSelfPublicKey = {0, nullptr};
    struct OH\_Huks\_Blob outSharedKey = {.size = OH\_HUKS\_KEY\_BYTES(OH\_HUKS\_AES\_KEY\_SIZE\_256), .data = nullptr};
    struct OH\_Huks\_Blob wrappedKeyData = {0, nullptr};
    uint8\_t plainKeyCipherBuffer\[OH\_HUKS\_MAX\_KEY\_SIZE\] = {0};
    struct OH\_Huks\_Blob plainCipherText = {OH\_HUKS\_MAX\_KEY\_SIZE, plainKeyCipherBuffer};
    uint8\_t kekCipherTextBuffer\[OH\_HUKS\_MAX\_KEY\_SIZE\] = {0};
    struct OH\_Huks\_Blob kekCipherText = {OH\_HUKS\_MAX\_KEY\_SIZE, kekCipherTextBuffer};
    /\* 模拟安全导入密钥场景，设备A为远端设备（导入设备），设备B为本端设备（被导入设备） \*/
    do {
        /\*\*
         \* 1. 设备A将待导入密钥转换成HUKS密钥材料格式To\_Import\_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤），
         \*   本示例使用g\_importedAes256PlainKey（对称密钥）作为模拟
         \*/
        /\*\*
         \* 2. 设备B生成一个加密导入用途的、用于协商的非对称密钥对Wrapping\_Key（公钥Wrapping\_Pk，私钥Wrapping\_Sk），
         \* 导出Wrapping\_Key公钥Wrapping\_Pk存放在变量huksPublicKey中
         \*/
        ret = GenerateAndExportHuksPublicKey(params, &huksPublicKey);
        if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
            break;
        }
        /\*\*
         \* 3. 设备A使用和设备B同样的算法，生成一个用于协商的非对称密钥对Caller\_Key（公钥Caller\_Pk，私钥Caller\_Sk），
         \* 导出Caller\_Key公钥Caller\_Pk存放在变量callerSelfPublicKey中
         \*/
        ret = GenerateAndExportCallerPublicKey(params, &callerSelfPublicKey);
        if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
            break;
        }
        /\*\*
         \* 4. 设备A生成一个对称密钥Caller\_Kek，该密钥后续将用于加密To\_Import\_Key
         \* 设备A基于Caller\_Key的私钥Caller\_Sk和设备B Wrapping\_Key的公钥Wrapping\_Pk，协商出Shared\_Key
         \*/
        ret = ImportKekAndAgreeSharedSecret(params, &huksPublicKey, &outSharedKey);
        if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
            break;
        }
        /\*\*
         \* 5. 设备A使用Caller\_Kek加密To\_Import\_Key，生成To\_Import\_Key\_Enc
         \* 设备A使用Shared\_Key加密Caller\_Kek，生成Caller\_Kek\_Enc
         \*/
        ret = EncryptImportedPlainKeyAndKek(params, &plainCipherText, &kekCipherText);
        if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
            break;
        }
        /\*\*
         \* 6. 设备A封装Caller\_Pk、To\_Import\_Key\_Enc、Caller\_Kek\_Enc等安全导入的材料并发送给设备B。
         \* 本示例作为变量存放在callerSelfPublicKey，plainCipherText，kekCipherText
         \* 7. 设备B导入封装的加密密钥材料
         \*/
        ret = ImportWrappedKey(params, &plainCipherText, &kekCipherText, &callerSelfPublicKey, &wrappedKeyData);
    } while (0);
    /\* 8. 设备A、B删除用于安全导入的密钥 \*/
    HUKS\_FREE\_BLOB(huksPublicKey);
    HUKS\_FREE\_BLOB(callerSelfPublicKey);
    HUKS\_FREE\_BLOB(outSharedKey);
    HUKS\_FREE\_BLOB(wrappedKeyData);
    return ret;
}

void HksClearKeysForWrappedKeyTest(const struct HksImportWrappedKeyTestParams \*params)
{
    OH\_Huks\_Result ret = CheckParamsValid(params);
    if (ret.errorCode != (int32\_t)OH\_HUKS\_SUCCESS) {
        return;
    }
    (void)OH\_Huks\_DeleteKeyItem(params->wrappingKeyAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(params->callerKeyAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(params->callerKekAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(params->callerAgreeKeyAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(params->importedKeyAlias, nullptr);
}

static OH\_Huks\_Result InitCommonTestParamsAndDoImport(struct HksImportWrappedKeyTestParams \*importWrappedKeyTestParams,
                                                      const struct OH\_Huks\_Param \*importedKeyParamSetArray,
                                                      uint32\_t arraySize)
{
    struct OH\_Huks\_ParamSet \*genX25519KeyParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*genCallerKeyParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*callerImportParamsKek = nullptr;
    struct OH\_Huks\_ParamSet \*agreeParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*importPlainKeyParams = nullptr;
    OH\_Huks\_Result ret;
    do {
        ret = InitParamSet(&genX25519KeyParamSet, g\_genWrappingKeyParams,
                           sizeof(g\_genWrappingKeyParams) / sizeof(OH\_Huks\_Param));
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        importWrappedKeyTestParams->genWrappingKeyParamSet = genX25519KeyParamSet;
        importWrappedKeyTestParams->publicKeySize = g\_x25519PubKeySize;
        ret = InitParamSet(&genCallerKeyParamSet, g\_genCallerX25519Params,
                           sizeof(g\_genCallerX25519Params) / sizeof(OH\_Huks\_Param));
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        importWrappedKeyTestParams->genCallerKeyParamSet = genCallerKeyParamSet;
        ret = InitParamSet(&callerImportParamsKek, g\_importParamsCallerKek,
                           sizeof(g\_importParamsCallerKek) / sizeof(OH\_Huks\_Param));
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        importWrappedKeyTestParams->importCallerKekParamSet = callerImportParamsKek;
        ret = InitParamSet(&agreeParamSet, g\_callerAgreeParams, sizeof(g\_callerAgreeParams) / sizeof(OH\_Huks\_Param));
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        importWrappedKeyTestParams->agreeParamSet = agreeParamSet;
        ret = InitParamSet(&importPlainKeyParams, importedKeyParamSetArray, arraySize);
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        importWrappedKeyTestParams->importWrappedKeyParamSet = importPlainKeyParams;
        ret = HksImportWrappedKeyTestCommonCase(importWrappedKeyTestParams);
    } while (0);
    OH\_Huks\_FreeParamSet(&genX25519KeyParamSet);
    OH\_Huks\_FreeParamSet(&genCallerKeyParamSet);
    OH\_Huks\_FreeParamSet(&callerImportParamsKek);
    OH\_Huks\_FreeParamSet(&agreeParamSet);
    OH\_Huks\_FreeParamSet(&importPlainKeyParams);
    return ret;
}
static napi\_value NAPI\_Global\_importWrappedKey(napi\_env env, napi\_callback\_info info)
{
    struct HksImportWrappedKeyTestParams importWrappedKeyTestParams001 = {0};
    importWrappedKeyTestParams001.wrappingKeyAlias = &g\_wrappingKeyAliasAes256;
    importWrappedKeyTestParams001.keyMaterialLen = g\_importedAes256PlainKey.size;
    importWrappedKeyTestParams001.callerKeyAlias = &g\_callerKeyAliasAes256;
    importWrappedKeyTestParams001.callerKekAlias = &g\_callerKekAliasAes256;
    importWrappedKeyTestParams001.callerKek = &g\_callerAes256Kek;
    importWrappedKeyTestParams001.callerAgreeKeyAlias = &g\_callerAgreeKeyAliasAes256;
    importWrappedKeyTestParams001.importedKeyAlias = &g\_importedKeyAliasAes256;
    importWrappedKeyTestParams001.importedPlainKey = &g\_importedAes256PlainKey;
    OH\_Huks\_Result ohResult =
        InitCommonTestParamsAndDoImport(&importWrappedKeyTestParams001, g\_importWrappedAes256Params,
                                        sizeof(g\_importWrappedAes256Params) / sizeof(struct OH\_Huks\_Param));
    HksClearKeysForWrappedKeyTest(&importWrappedKeyTestParams001);
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

static napi\_value IsKeyExist(napi\_env env, napi\_callback\_info info)
{
    /\* 1.指定密钥别名 \*/
    struct OH\_Huks\_Blob keyAlias = {
        (uint32\_t)strlen("test\_key"),
        (uint8\_t \*)"test\_key"
    };

    /\* 2.调用OH\_Huks\_IsKeyItemExist判断密钥是否存在 \*/
    struct OH\_Huks\_Result ohResult = OH\_Huks\_IsKeyItemExist(&keyAlias, NULL);
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### 调测验证

调用[OH\_Huks\_IsKeyItemExist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_iskeyitemexist)验证密钥是否存在，如密钥存在即表示密钥导入成功。

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <string.h>
static napi_value IsKeyExist(napi_env env, napi_callback_info info)
{
    /* 1.指定密钥别名 */
    struct OH_Huks_Blob keyAlias = {
        (uint32_t)strlen("test_key"),
        (uint8_t *)"test_key"
    };
    
    /* 2.调用OH_Huks_IsKeyItemExist判断密钥是否存在 */
    struct OH_Huks_Result ohResult = OH_Huks_IsKeyItemExist(&keyAlias, NULL);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        // 失败。
    } else {
        // 成功。
    }
    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```
