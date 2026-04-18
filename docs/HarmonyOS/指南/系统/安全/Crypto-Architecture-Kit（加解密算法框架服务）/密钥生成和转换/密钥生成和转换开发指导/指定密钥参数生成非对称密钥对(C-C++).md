---
title: "指定密钥参数生成非对称密钥对(C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec-ndk"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "Crypto Architecture Kit（加解密算法框架服务）"
  - "密钥生成和转换"
  - "密钥生成和转换开发指导"
  - "指定密钥参数生成非对称密钥对(C/C++)"
captured_at: "2026-04-17T01:35:47.783Z"
---

# 指定密钥参数生成非对称密钥对(C/C++)

以RSA、ECC、SM2为例，根据指定的密钥参数，生成非对称密钥对（KeyPair），并获取密钥参数属性。

该对象可用于后续的加解密等操作。获取的密钥参数属性可用于存储或传输。

#### 指定密钥参数生成RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#rsa)。

1.  调用[OH\_CryptoAsymKeySpec\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_create)，指定算法名为"RSA"， 密钥参数类型为CRYPTO\_ASYM\_KEY\_KEY\_PAIR\_SPEC，创建参数对象（keySpec）。
    
2.  指定uint8\_t类型的RSA密钥对数据（pk、sk、n），分别封装成[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)。
    
3.  调用[OH\_CryptoAsymKeySpec\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_setparam)，指定参数类型分别为CRYPTO\_RSA\_E\_DATABLOB（pk）、CRYPTO\_RSA\_D\_DATABLOB（sk）、CRYPTO\_RSA\_N\_DATABLOB（n）, 依次传入封装后的[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)，设置参数对象（keySpec）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/zpWSurU6T_qNY5hlFcipYg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=A39F1D9D8BBC5C047921E3785E4E0DA3023B1A4F1340DB3B1FBCD491A06DB40F)
    
    pk、sk、n均要以大端模式输入，且必须为正数。
    
4.  调用[OH\_CryptoAsymKeyGeneratorWithSpec\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygeneratorwithspec_create)，将参数对象（keySpec）传入，创建非对称密钥生成器（generatorSpec）。
    
5.  调用[OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygeneratorwithspec_genkeypair)，生成RSA密钥对（keyPair）。
    
6.  分别传入密钥对中的私钥和公钥，调用[OH\_CryptoPrivKey\_GetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoprivkey_getparam)和[OH\_CryptoPubKey\_GetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptopubkey_getparam)，获取RSA算法中私钥和公钥的各种密钥参数。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <string>
#define SPLIT\_SIZE 2

static OH\_Crypto\_ErrCode GetRsaKeyParams(OH\_CryptoKeyPair \*keyCtx, Crypto\_DataBlob \*pubKeyData, Crypto\_DataBlob \*dataN)
{
    OH\_CryptoPubKey \*pubKey = OH\_CryptoKeyPair\_GetPubKey(keyCtx);
    if (pubKey == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }
    OH\_Crypto\_ErrCode ret = OH\_CryptoPubKey\_GetParam(pubKey, CRYPTO\_RSA\_E\_DATABLOB, pubKeyData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    return OH\_CryptoPubKey\_GetParam(pubKey, CRYPTO\_RSA\_N\_DATABLOB, dataN);
}

static void FreeRsaKeyParams(Crypto\_DataBlob \*pubKeyData, Crypto\_DataBlob \*dataN)
{
    OH\_Crypto\_FreeDataBlob(pubKeyData);
    OH\_Crypto\_FreeDataBlob(dataN);
}

size\_t RsaConvertHex(uint8\_t\* dest, size\_t count, const char\* src)
{
    size\_t i;
    int value;

    for (i = 0; i < count && sscanf(src + i \* SPLIT\_SIZE, "%2x", &value) == 1; i++) {
        dest\[i\] = value;
    }
    return i;
}

struct RsaParams {
    Crypto\_DataBlob nData;
    Crypto\_DataBlob eData;
    uint8\_t n\[1024\];
    uint8\_t e\[20\];
};

static void PrepareRsaParams(RsaParams \*params)
{
    std::string nStr = "9260d0750ae117eee55c3f3deaba74917521a262ee76007cdf8a56755ad73a1598a1408410a01434c3f"
    "5bc54a88b57fa19fc4328daea0750a4c44e88cff3b2382621b80f670464433e4336e6d003e8cd65bff211da144b88291c2259a"
    "00a72b711c116ef7686e8fee34e4d933c868187bdc26f7be071493c86f7a5941c3510806ad67b0f94d88f5cf5c02a092821d86"
    "26e8932b65c5bd8c92049c210932b7afa7ac59c0e886ae5c1edb00d8ce2c57633db26bd6639bff73cee82be9275c402b4cf2a4"
    "388da8cf8c64eefe1c5a0f5ab8057c39fa5c0589c3e253f0960332300f94bea44877b588e1edbde97cf2360727a09b775262d"
    "7ee552b3319b9266f05a25";
    std::string eStr = "010001";
    
    size\_t nLen = RsaConvertHex(params->n, nStr.size() / SPLIT\_SIZE, nStr.c\_str());
    size\_t eLen = RsaConvertHex(params->e, eStr.size() / SPLIT\_SIZE, eStr.c\_str());
    
    params->nData = {.data = params->n, .len = nLen};
    params->eData = {.data = params->e, .len = eLen};
}

static OH\_Crypto\_ErrCode CreateRsaKeySpec(RsaParams \*params, OH\_CryptoAsymKeySpec \*\*keySpec)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeySpec\_Create("RSA", CRYPTO\_ASYM\_KEY\_PUBLIC\_KEY\_SPEC, keySpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    
    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_RSA\_E\_DATABLOB, &params->eData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }
    
    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_RSA\_N\_DATABLOB, &params->nData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }
    
    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode GenerateRsaKeyPair(OH\_CryptoAsymKeySpec \*keySpec,
    OH\_CryptoAsymKeyGeneratorWithSpec \*\*generatorSpec, OH\_CryptoKeyPair \*\*keyPair)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGeneratorWithSpec\_Create(keySpec, generatorSpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    
    ret = OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair(\*generatorSpec, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(\*generatorSpec);
        return ret;
    }
    
    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode ValidateRsaKeyPair(OH\_CryptoKeyPair \*keyPair)
{
    Crypto\_DataBlob dataE = {.data = nullptr, .len = 0};
    Crypto\_DataBlob dataN = {.data = nullptr, .len = 0};
    OH\_Crypto\_ErrCode ret = GetRsaKeyParams(keyPair, &dataE, &dataN);
    if (ret != CRYPTO\_SUCCESS) {
        FreeRsaKeyParams(&dataE, &dataN);
        return ret;
    }
    FreeRsaKeyParams(&dataE, &dataN);
    return CRYPTO\_SUCCESS;
}

OH\_Crypto\_ErrCode doTestRsaGenKeyPairBySpec()
{
    RsaParams params = {};
    PrepareRsaParams(&params);
    
    OH\_CryptoAsymKeySpec \*keySpec = nullptr;
    OH\_Crypto\_ErrCode ret = CreateRsaKeySpec(&params, &keySpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    
    OH\_CryptoAsymKeyGeneratorWithSpec \*generatorSpec = nullptr;
    OH\_CryptoKeyPair \*keyPair = nullptr;
    ret = GenerateRsaKeyPair(keySpec, &generatorSpec, &keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(keySpec);
        return ret;
    }
    
    ret = ValidateRsaKeyPair(keyPair);
    
    OH\_CryptoKeyPair\_Destroy(keyPair);
    OH\_CryptoAsymKeySpec\_Destroy(keySpec);
    OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(generatorSpec);
    return ret;
}

#### 指定密钥参数生成ECC密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：ECC](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#ecc)。

1.  调用[OH\_CryptoAsymKeySpec\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_create)，指定算法名为"ECC"， 密钥参数类型为CRYPTO\_ASYM\_KEY\_COMMON\_PARAMS\_SPEC，创建参数对象（keySpec）。
    
2.  指定uint8\_t类型的ECC公私钥包含的公共参数（p、a、b、gx、gy、n、h），分别封装成[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)。
    
3.  调用[OH\_CryptoAsymKeySpec\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_setparam)，指定参数类型分别为CRYPTO\_ECC\_FP\_P\_DATABLOB（p）、CRYPTO\_ECC\_A\_DATABLOB（a）、CRYPTO\_ECC\_B\_DATABLOB（b）、CRYPTO\_ECC\_G\_X\_DATABLOB（gx）、CRYPTO\_ECC\_G\_Y\_DATABLOB（gy）、CRYPTO\_ECC\_N\_DATABLOB（n）、CRYPTO\_ECC\_H\_INT（h）, 依次传入封装后的[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)，设置到参数对象（keySpec）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/DO6ZkYFXT6-3IjCsshobVg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=9A820F6F2E9B79F44B3F16FE8596C132B1930200E6FD81348DD37582777C815C)
    
    p、a、b、gx、gy、n、h均要以大端模式输入，且必须为正数。
    
4.  调用[OH\_CryptoAsymKeyGeneratorWithSpec\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygeneratorwithspec_create)，将参数对象（keySpec）传入，创建非对称密钥生成器（generatorSpec）。
    
5.  调用[OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygeneratorwithspec_genkeypair)，生成ECC密钥对（keyPair）。
    
6.  分别传入密钥对中的私钥和公钥，调用[OH\_CryptoPrivKey\_GetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoprivkey_getparam)和[OH\_CryptoPubKey\_GetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptopubkey_getparam)，获取ECC算法中私钥和公钥的各种密钥参数。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <string>

#define SPLIT\_SIZE 2

static OH\_Crypto\_ErrCode GetEccKeyParams(OH\_CryptoKeyPair \*keyCtx, Crypto\_DataBlob \*pubKeyXData,
    Crypto\_DataBlob \*pubKeyYData, Crypto\_DataBlob \*privKeyData)
{
    OH\_CryptoPubKey \*pubKey = OH\_CryptoKeyPair\_GetPubKey(keyCtx);
    if (pubKey == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }
    OH\_Crypto\_ErrCode ret = OH\_CryptoPubKey\_GetParam(pubKey, CRYPTO\_ECC\_PK\_X\_DATABLOB, pubKeyXData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPubKey\_GetParam(pubKey, CRYPTO\_ECC\_PK\_Y\_DATABLOB, pubKeyYData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    OH\_CryptoPrivKey \*privKey = OH\_CryptoKeyPair\_GetPrivKey(keyCtx);
    if (privKey == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_SK\_DATABLOB, privKeyData);
    return ret;
}

static void FreeEccKeyParams(Crypto\_DataBlob \*pubKeyXData, Crypto\_DataBlob \*pubKeyYData, Crypto\_DataBlob \*privKeyData)
{
    OH\_Crypto\_FreeDataBlob(pubKeyXData);
    OH\_Crypto\_FreeDataBlob(pubKeyYData);
    OH\_Crypto\_FreeDataBlob(privKeyData);
}

struct EccCommonParams {
    Crypto\_DataBlob pData;
    Crypto\_DataBlob aData;
    Crypto\_DataBlob bData;
    Crypto\_DataBlob gxData;
    Crypto\_DataBlob gyData;
    Crypto\_DataBlob nData;
    Crypto\_DataBlob hData;
};

static OH\_Crypto\_ErrCode GetEccCommonParams(OH\_CryptoKeyPair \*keyCtx, EccCommonParams \*params)
{
    OH\_CryptoPrivKey \*privKey = OH\_CryptoKeyPair\_GetPrivKey(keyCtx);
    if (privKey == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }
    OH\_Crypto\_ErrCode ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_FP\_P\_DATABLOB, &params->pData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_A\_DATABLOB, &params->aData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_B\_DATABLOB, &params->bData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_G\_X\_DATABLOB, &params->gxData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_G\_Y\_DATABLOB, &params->gyData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_N\_DATABLOB, &params->nData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_H\_INT, &params->hData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    return ret;
}

static void FreeEccCommonParams(EccCommonParams \*params)
{
    OH\_Crypto\_FreeDataBlob(&params->pData);
    OH\_Crypto\_FreeDataBlob(&params->aData);
    OH\_Crypto\_FreeDataBlob(&params->bData);
    OH\_Crypto\_FreeDataBlob(&params->gxData);
    OH\_Crypto\_FreeDataBlob(&params->gyData);
    OH\_Crypto\_FreeDataBlob(&params->nData);
    OH\_Crypto\_FreeDataBlob(&params->hData);
}

size\_t ConvertHex(uint8\_t\* dest, size\_t count, const char\* src)
{
    size\_t i;
    int value;

    for (i = 0; i < count && sscanf(src + i \* SPLIT\_SIZE, "%2x", &value) == 1; i++) {
        dest\[i\] = value;
    }
    return i;
}

struct EccParams {
    Crypto\_DataBlob pData;
    Crypto\_DataBlob aData;
    Crypto\_DataBlob bData;
    Crypto\_DataBlob gxData;
    Crypto\_DataBlob gyData;
    Crypto\_DataBlob nData;
    Crypto\_DataBlob hData;
    uint8\_t p\[256\];
    uint8\_t gx\[256\];
    uint8\_t gy\[256\];
    uint8\_t a\[256\];
    uint8\_t b\[256\];
    uint8\_t n\[256\];
    uint8\_t h\[4\];
};

static void PrepareEccParams(EccParams \*params)
{
    std::string pStr = "ffffffffffffffffffffffffffffffff000000000000000000000001";
    std::string gxStr = "b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21";
    std::string gyStr = "bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34";
    std::string aStr = "fffffffffffffffffffffffffffffffefffffffffffffffffffffffe";
    std::string bStr = "b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4";
    std::string nStr = "ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d";
    uint8\_t h\[\] = {0x00, 0x00, 0x00, 0x01}; // 大端序

    size\_t pLen = ConvertHex(params->p, pStr.size() / SPLIT\_SIZE, pStr.c\_str());
    size\_t gxLen = ConvertHex(params->gx, gxStr.size() / SPLIT\_SIZE, gxStr.c\_str());
    size\_t gyLen = ConvertHex(params->gy, gyStr.size() / SPLIT\_SIZE, gyStr.c\_str());
    size\_t aLen = ConvertHex(params->a, aStr.size() / SPLIT\_SIZE, aStr.c\_str());
    size\_t bLen = ConvertHex(params->b, bStr.size() / SPLIT\_SIZE, bStr.c\_str());
    size\_t nLen = ConvertHex(params->n, nStr.size() / SPLIT\_SIZE, nStr.c\_str());

    params->pData = {.data = params->p, .len = pLen};
    params->aData = {.data = params->a, .len = aLen};
    params->bData = {.data = params->b, .len = bLen};
    params->gxData = {.data = params->gx, .len = gxLen};
    params->gyData = {.data = params->gy, .len = gyLen};
    params->nData = {.data = params->n, .len = nLen};
    params->hData = {.data = h, .len = sizeof(h)};
}

static OH\_Crypto\_ErrCode CreateEccKeySpec(EccParams \*params, OH\_CryptoAsymKeySpec \*\*keySpec)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeySpec\_Create("ECC", CRYPTO\_ASYM\_KEY\_COMMON\_PARAMS\_SPEC, keySpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_FP\_P\_DATABLOB, &params->pData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }

    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_A\_DATABLOB, &params->aData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }

    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_B\_DATABLOB, &params->bData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }

    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_G\_X\_DATABLOB, &params->gxData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }

    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_G\_Y\_DATABLOB, &params->gyData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }

    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_N\_DATABLOB, &params->nData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }

    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_H\_INT, &params->hData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode GenerateEccKeyPair(OH\_CryptoAsymKeySpec \*keySpec,
    OH\_CryptoAsymKeyGeneratorWithSpec \*\*generatorSpec, OH\_CryptoKeyPair \*\*keyPair)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGeneratorWithSpec\_Create(keySpec, generatorSpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    ret = OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair(\*generatorSpec, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(\*generatorSpec);
        return ret;
    }

    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode ValidateEccKeyPair(OH\_CryptoKeyPair \*keyPair)
{
    Crypto\_DataBlob dataPkX = {.data = nullptr, .len = 0};
    Crypto\_DataBlob dataPkY = {.data = nullptr, .len = 0};
    Crypto\_DataBlob dataSk = {.data = nullptr, .len = 0};
    OH\_Crypto\_ErrCode ret = GetEccKeyParams(keyPair, &dataPkX, &dataPkY, &dataSk);
    if (ret != CRYPTO\_SUCCESS) {
        FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);
        return ret;
    }
    FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);

    EccCommonParams commonParams = {};
    ret = GetEccCommonParams(keyPair, &commonParams);
    if (ret != CRYPTO\_SUCCESS) {
        FreeEccCommonParams(&commonParams);
        return ret;
    }
    FreeEccCommonParams(&commonParams);

    return CRYPTO\_SUCCESS;
}

OH\_Crypto\_ErrCode doTestEccGenKeyPairBySpec()
{
    EccParams params = {};
    PrepareEccParams(&params);

    OH\_CryptoAsymKeySpec \*keySpec = nullptr;
    OH\_Crypto\_ErrCode ret = CreateEccKeySpec(&params, &keySpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    OH\_CryptoAsymKeyGeneratorWithSpec \*generatorSpec = nullptr;
    OH\_CryptoKeyPair \*keyPair = nullptr;
    ret = GenerateEccKeyPair(keySpec, &generatorSpec, &keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(keySpec);
        return ret;
    }

    ret = ValidateEccKeyPair(keyPair);

    OH\_CryptoKeyPair\_Destroy(keyPair);
    OH\_CryptoAsymKeySpec\_Destroy(keySpec);
    OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(generatorSpec);
    return ret;
}

#### 根据椭圆曲线名生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#sm2)。

1.  调用[OH\_CryptoAsymKeySpec\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_create)，指定算法名为"SM2"， 密钥参数类型为CRYPTO\_ASYM\_KEY\_KEY\_PAIR\_SPEC，创建密钥参数对象（keySpec）。
    
2.  调用[OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_geneccommonparamsspec)，指定曲线为"NID\_sm2"， 生成SM2公共参数对象（sm2CommonSpec）。
    
3.  调用[OH\_CryptoAsymKeySpec\_SetCommonParamsSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_setcommonparamsspec)，将生成SM2公共参数对象（sm2CommonSpec）设置到密钥参数对象（keySpec）。
    
4.  指定uint8\_t类型的SM2密钥对数据（pkx、pky、sk），分别封装成[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)。
    
5.  调用[OH\_CryptoAsymKeySpec\_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeyspec_setparam)，指定参数类型分别为CRYPTO\_ECC\_PK\_X\_DATABLOB（pkx）、CRYPTO\_ECC\_PK\_Y\_DATABLOB（pky）、CRYPTO\_ECC\_SK\_DATABLOB（sk）, 依次传入封装后的[Crypto\_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)，设置到参数对象（keySpec）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Sd7_63_hQQecbHWBI8ZYWg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013549Z&HW-CC-Expire=86400&HW-CC-Sign=7A2B2B5353C8C5470A9C0F00591779C0FC70A93A86D5AA07607479BC7232C8D8)
    
    pkx、pky、sk均要以大端模式输入，且必须为正数。
    
6.  调用[OH\_CryptoAsymKeyGeneratorWithSpec\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygeneratorwithspec_create)，将参数对象（keySpec）传入，创建非对称密钥生成器（generatorSpec）。
    
7.  调用[OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygeneratorwithspec_genkeypair)，生成SM2密钥对（keyPair）。
    
8.  分别传入密钥对中的私钥和公钥，调用[OH\_CryptoPrivKey\_GetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoprivkey_getparam)和[OH\_CryptoPubKey\_GetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptopubkey_getparam)，获取SM2算法中私钥和公钥的各种密钥参数。
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <string>
#define SPLIT\_SIZE 2

static OH\_Crypto\_ErrCode GetEccKeyParams(OH\_CryptoKeyPair \*keyCtx, Crypto\_DataBlob \*pubKeyXData,
    Crypto\_DataBlob \*pubKeyYData, Crypto\_DataBlob \*privKeyData)
{
    OH\_CryptoPubKey \*pubKey = OH\_CryptoKeyPair\_GetPubKey(keyCtx);
    if (pubKey == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }
    OH\_Crypto\_ErrCode ret = OH\_CryptoPubKey\_GetParam(pubKey, CRYPTO\_ECC\_PK\_X\_DATABLOB, pubKeyXData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    ret = OH\_CryptoPubKey\_GetParam(pubKey, CRYPTO\_ECC\_PK\_Y\_DATABLOB, pubKeyYData);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    OH\_CryptoPrivKey \*privKey = OH\_CryptoKeyPair\_GetPrivKey(keyCtx);
    if (privKey == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }
    ret = OH\_CryptoPrivKey\_GetParam(privKey, CRYPTO\_ECC\_SK\_DATABLOB, privKeyData);
    return ret;
}

static void FreeEccKeyParams(Crypto\_DataBlob \*pubKeyXData, Crypto\_DataBlob \*pubKeyYData, Crypto\_DataBlob \*privKeyData)
{
    OH\_Crypto\_FreeDataBlob(pubKeyXData);
    OH\_Crypto\_FreeDataBlob(pubKeyYData);
    OH\_Crypto\_FreeDataBlob(privKeyData);
}

size\_t Sm2ConvertHex(uint8\_t\* dest, size\_t count, const char\* src)
{
    size\_t i;
    int value;

    for (i = 0; i < count && sscanf(src + i \* SPLIT\_SIZE, "%2x", &value) == 1; i++) {
        dest\[i\] = value;
    }
    return i;
}

struct Sm2Params {
    Crypto\_DataBlob pkXData;
    Crypto\_DataBlob pkYData;
    Crypto\_DataBlob skData;
    uint8\_t pkX\[256\];
    uint8\_t pkY\[256\];
    uint8\_t sk\[256\];
};

static void PrepareSm2Params(Sm2Params \*params)
{
    std::string pkXStr = "67F3B850BDC0BA5D3A29D8A0883C4B17612AB84F87F18E28F77D824A115C02C4";
    std::string pkYStr = "D48966CE754BBBEDD6501A1385E1B205C186E926ADED44287145E8897D4B2071";
    std::string skStr = "6330B599ECD23ABDC74B9A5B7B5E00E553005F72743101C5FAB83AEB579B7074";
    
    size\_t pkXLen = Sm2ConvertHex(params->pkX, pkXStr.size() / SPLIT\_SIZE, pkXStr.c\_str());
    size\_t pkYLen = Sm2ConvertHex(params->pkY, pkYStr.size() / SPLIT\_SIZE, pkYStr.c\_str());
    size\_t skLen = Sm2ConvertHex(params->sk, skStr.size() / SPLIT\_SIZE, skStr.c\_str());
    
    params->pkXData = {.data = params->pkX, .len = pkXLen};
    params->pkYData = {.data = params->pkY, .len = pkYLen};
    params->skData = {.data = params->sk, .len = skLen};
}

static OH\_Crypto\_ErrCode CreateSm2KeySpec(Sm2Params \*params, OH\_CryptoAsymKeySpec \*\*keySpec,
    OH\_CryptoAsymKeySpec \*\*sm2CommonSpec)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeySpec\_Create("SM2", CRYPTO\_ASYM\_KEY\_KEY\_PAIR\_SPEC, keySpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    
    ret = OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec("NID\_sm2", sm2CommonSpec);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }
    
    ret = OH\_CryptoAsymKeySpec\_SetCommonParamsSpec(\*keySpec, \*sm2CommonSpec);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*sm2CommonSpec);
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }
    
    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_PK\_X\_DATABLOB, &params->pkXData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*sm2CommonSpec);
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }
    
    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_PK\_Y\_DATABLOB, &params->pkYData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*sm2CommonSpec);
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }
    
    ret = OH\_CryptoAsymKeySpec\_SetParam(\*keySpec, CRYPTO\_ECC\_SK\_DATABLOB, &params->skData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(\*sm2CommonSpec);
        OH\_CryptoAsymKeySpec\_Destroy(\*keySpec);
        return ret;
    }
    
    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode GenerateSm2KeyPair(OH\_CryptoAsymKeySpec \*keySpec,
    OH\_CryptoAsymKeyGeneratorWithSpec \*\*generatorSpec, OH\_CryptoKeyPair \*\*keyPair)
{
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGeneratorWithSpec\_Create(keySpec, generatorSpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    
    ret = OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair(\*generatorSpec, keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(\*generatorSpec);
        return ret;
    }
    
    return CRYPTO\_SUCCESS;
}

static OH\_Crypto\_ErrCode ValidateSm2KeyPair(OH\_CryptoKeyPair \*keyPair)
{
    Crypto\_DataBlob dataPkX = {.data = nullptr, .len = 0};
    Crypto\_DataBlob dataPkY = {.data = nullptr, .len = 0};
    Crypto\_DataBlob dataSk = {.data = nullptr, .len = 0};
    OH\_Crypto\_ErrCode ret = GetEccKeyParams(keyPair, &dataPkX, &dataPkY, &dataSk);
    if (ret != CRYPTO\_SUCCESS) {
        FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);
        return ret;
    }
    FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);
    return CRYPTO\_SUCCESS;
}

OH\_Crypto\_ErrCode doTestSm2GenKeyPairBySpec()
{
    Sm2Params params = {};
    PrepareSm2Params(&params);
    
    OH\_CryptoAsymKeySpec \*keySpec = nullptr;
    OH\_CryptoAsymKeySpec \*sm2CommonSpec = nullptr;
    OH\_Crypto\_ErrCode ret = CreateSm2KeySpec(&params, &keySpec, &sm2CommonSpec);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    
    OH\_CryptoAsymKeyGeneratorWithSpec \*generatorSpec = nullptr;
    OH\_CryptoKeyPair \*keyPair = nullptr;
    ret = GenerateSm2KeyPair(keySpec, &generatorSpec, &keyPair);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeySpec\_Destroy(sm2CommonSpec);
        OH\_CryptoAsymKeySpec\_Destroy(keySpec);
        return ret;
    }
    
    ret = ValidateSm2KeyPair(keyPair);
    
    OH\_CryptoKeyPair\_Destroy(keyPair);
    OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(generatorSpec);
    OH\_CryptoAsymKeySpec\_Destroy(sm2CommonSpec);
    OH\_CryptoAsymKeySpec\_Destroy(keySpec);
    return ret;
}
