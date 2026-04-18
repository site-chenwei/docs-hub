---
title: "如何实现ArkTS与C/C++的HashMap转换"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-67"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "如何实现ArkTS与C/C++的HashMap转换"
captured_at: "2026-04-17T02:03:02.365Z"
---

# 如何实现ArkTS与C/C++的HashMap转换

**问题详情：**

如何实现将ArkTS的HashMap转换至Native侧。

**解决措施：**

-   方案一：传递数组。
    
    将HashMap的key、value作为数组取出，将两个数组传递至Native侧并组装成Map。
    
    ArkTS侧传递数组。
    
    let hashMap: HashMap<string, number> = new HashMap();
    hashMap.set("Abc", 123);
    hashMap.set("Bcd", 234);
    hashMap.set("Cde", 345);
    
    let keysArray: Array<string> = Array.from(hashMap.keys());
    let valuesArray: Array<number> = Array.from(hashMap.values());
    testNapi.tsPutMap(keysArray, valuesArray, hashMap.length);
    
    在Native侧组装Map。
    
    // Convert value to string and return
    std::string HashMap::value2String(napi\_env env, napi\_value value) {
        size\_t stringSize = 0;
        napi\_get\_value\_string\_utf8(env, value, nullptr, 0, &stringSize); // 获取字符串长度
        std::string valueString;
        valueString.resize(stringSize + 1);
        napi\_get\_value\_string\_utf8(env, value, &valueString\[0\], stringSize + 1, &stringSize); // 根据长度转换成字符串
        return valueString;
    }
    napi\_value HashMap::TsPutMap(napi\_env env, napi\_callback\_info info) {
        std::map<std::string, int> myMap;
        size\_t argc = 3;
        napi\_value args\[3\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_value mapKey = args\[0\]; // key
        napi\_value mapVal = args\[1\]; // value
        napi\_value mapNum = args\[2\]; // length
    
    
        uint32\_t mapCNum = 0;
        napi\_get\_value\_uint32(env, mapNum, &mapCNum);
        for (uint32\_t i = 0; i < mapCNum; i++) {
            napi\_value keyNIndex, valNIndex;
            napi\_get\_element(env, mapKey, i, &keyNIndex);
            napi\_get\_element(env, mapVal, i, &valNIndex);
            std::string keyIndex = value2String(env, keyNIndex);
            int valIndex = 0;
            napi\_get\_value\_int32(env, valNIndex, &valIndex);
            myMap\[keyIndex\] = valIndex;
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "Pure", "%{public}s %{public}d", keyIndex.c\_str(), myMap\[keyIndex\]);
        }
        return nullptr;
    }
    
-   方案二：传递JSON。
    
    将HashMap转换为Json数据传至Native侧，在Native侧反序列化用Map承接。
    
    ArkTS侧转JSON。
    
    1.  JSON.stringify不支持对HashMap操作，需要先将其转成Record
        
        map2rec(map: HashMap<string, ESObject>): Record<string, ESObject> {
          // Map to Record
          let Rec: Record<string, ESObject> = {}
          map.forEach((value: ESObject, key: string) => {
            if (value instanceof HashMap) {
              //Value may be HashMap
              let vRec: Record<string, ESObject> = this.map2rec(value)
              value = vRec
            }
            Rec\[key\] = value
          })
          return Rec
        }
        
    2.  然后使用JSON.stringify序列化
        
        let myRec: Record<string, ESObject> = this.map2rec(hashMap);
        let str: string = JSON.stringify(myRec);
        testNapi.mapJson(str);
        
    
    Native侧反序列化。
    
    C++没有直接反序列化的接口，需要使用三方库，本demo采用lycium交叉编译工具编译json三方库。
    
    napi\_value HashMap::MapJson(napi\_env env, napi\_callback\_info info) {
    
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        std::string jsonStr = value2String(env, args\[0\]);
    
        std::map<std::string, int> myMap = nlohmann::json::parse(jsonStr.c\_str());
    
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "Pure", "%{public}d %{public}d %{public}d", myMap\["Abc"\], myMap\["Bcd"\],
                     myMap\["Cde"\]);
    
        return nullptr;
    }
