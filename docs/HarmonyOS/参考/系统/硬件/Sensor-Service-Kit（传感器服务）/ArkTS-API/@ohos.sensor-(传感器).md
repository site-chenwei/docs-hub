---
title: "@ohos.sensor (传感器)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Sensor Service Kit（传感器服务）"
  - "ArkTS API"
  - "@ohos.sensor (传感器)"
captured_at: "2026-04-17T01:48:34.175Z"
---

# @ohos.sensor (传感器)

sensor模块提供了获取传感器数据的能力，包括获取传感器属性列表，订阅传感器数据，以及一些通用的传感器算法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/H67uvAW2SSW_UqAegtuRDg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=A0A6E2788739E0CF6BF5D33AA380EA63C7781B8C4EC9A50FBBF05A981C132292)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。订阅前可使用[getSingleSensor](#sensorgetsinglesensor9)接口获取该传感器的信息，获取该传感器信息成功时可正常订阅传感器，异常情况详见[getSingleSensor](#sensorgetsinglesensor9)错误码说明，具体使用方法可参考[指南开发步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sensor-guidelines#开发步骤)；订阅传感器数据时确保on订阅和off取消订阅成对出现。

#### 导入模块

```ts
import { sensor } from '@kit.SensorServiceKit';
```

#### sensor.on

#### \[h2\]ACCELEROMETER9+

on(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options): void

订阅加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ACCELEROMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]FUSION\_PRESSURE22+

on(type: SensorId.FUSION\_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void

订阅融合压力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).FUSION\_PRESSURE | 是 | 传感器类型，该值固定为SensorId.FUSION\_PRESSURE |
| callback | Callback<[FusionPressureResponse](#fusionpressureresponse22)\> | 是 | 回调函数，异步上报的传感器数据固定为FusionPressureResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.FUSION_PRESSURE, (data: sensor.FusionPressureResponse) => {
    console.info('Succeeded in invoking on. fusionPressure: ' + data.fusionPressure);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.FUSION_PRESSURE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ACCELEROMETER\_UNCALIBRATED9+

on(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void

订阅未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerUncalibratedResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ACCELEROMETER_UNCALIBRATED);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]AMBIENT\_LIGHT9+

on(type: SensorId.AMBIENT\_LIGHT, callback: Callback<LightResponse>, options?: Options): void

订阅环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](#lightresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为LightResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.AMBIENT_LIGHT, (data: sensor.LightResponse) => {
    console.info('Succeeded in getting the ambient light intensity: ' + data.intensity);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.AMBIENT_LIGHT);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]AMBIENT\_TEMPERATURE9+

on(type: SensorId.AMBIENT\_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>, options?: Options): void

订阅温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为AmbientTemperatureResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
    console.info('Succeeded in invoking on. Temperature: ' + data.temperature);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.AMBIENT_TEMPERATURE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]BAROMETER9+

on(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>, options?: Options): void

订阅气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为BarometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.BAROMETER, (data: sensor.BarometerResponse) => {
    console.info('Succeeded in invoking on. Atmospheric pressure: ' + data.pressure);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.BAROMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GRAVITY9+

on(type: SensorId.GRAVITY, callback: Callback<GravityResponse>, options?: Options): void

订阅重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| callback | Callback<[GravityResponse](#gravityresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为GravityResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GRAVITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GYROSCOPE9+

on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void

订阅校准的陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GYROSCOPE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GYROSCOPE\_UNCALIBRATED9+

on(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>, options?: Options): void

订阅未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeUncalibratedResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GYROSCOPE_UNCALIBRATED);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HALL9+

on(type: SensorId.HALL, callback: Callback<HallResponse>, options?: Options): void

订阅霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| callback | Callback<[HallResponse](#hallresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为HallResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，默认值为200000000ns。当霍尔事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.HALL, (data: sensor.HallResponse) => {
    console.info('Succeeded in invoking on. Hall status: ' + data.status);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HALL);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HEART\_RATE9+

on(type: SensorId.HEART\_RATE, callback: Callback<HeartRateResponse>, options?: Options): void

订阅心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为HeartRateResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.HEART_RATE, (data: sensor.HeartRateResponse) => {
    console.info('Succeeded in invoking on. Heart rate: ' + data.heartRate);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HEART_RATE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HUMIDITY9+

on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>, options?: Options): void

订阅湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为HumidityResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
    console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HUMIDITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]LINEAR\_ACCELEROMETER9+

on(type: SensorId.LINEAR\_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>, options?: Options): void

订阅线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELEROMETER。 |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为LinearAccelerometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.LINEAR_ACCELEROMETER, (data: sensor.LinearAccelerometerResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.LINEAR_ACCELEROMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]MAGNETIC\_FIELD9+

on(type: SensorId.MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>, options?: Options): void

订阅地磁传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.MAGNETIC_FIELD);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED9+

on(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void

订阅未校准地磁传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldUncalibratedResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ORIENTATION9+

on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void

订阅方向传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/LqPQ-qhaQUy2wfBghssjnA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=7E5479E8A84EE9CFA070988D80C829E6B6144993D7813EB5A91670252CA26A90)

调用本接口的应用或服务可以通过提示用户使用8字校准法来提高应用获取的方向传感器的精度，此传感器理论误差正负5度，具体的精度根据不同的驱动及算法实现可能存在差异。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为OrientationResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
    console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
    console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
    console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ORIENTATION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PEDOMETER9+

on(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void

订阅计步器传感器数据。计步传感器数据上报有一定延迟，延迟时间由具体的实现产品决定。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为PedometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.PEDOMETER, (data: sensor.PedometerResponse) => {
    console.info('Succeeded in invoking on. Step count: ' + data.steps);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.PEDOMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PEDOMETER\_DETECTION9+

on(type: SensorId.PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void

订阅计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为PedometerDetectionResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
    console.info('Succeeded in invoking on. Pedometer scalar: ' + data.scalar);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.PEDOMETER_DETECTION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PROXIMITY9+

on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void

订阅接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为ProximityResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，默认值为200000000ns。当接近光事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.PROXIMITY, (data: sensor.ProximityResponse) => {
    console.info('Succeeded in invoking on. Distance: ' + data.distance);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.PROXIMITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ROTATION\_VECTOR9+

on(type: SensorId.ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>, options?: Options): void

订阅旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为RotationVectorResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. Scalar quantity: ' + data.w);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ROTATION_VECTOR);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]SIGNIFICANT\_MOTION9+

on(type: SensorId.SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void

订阅有效运动传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为SignificantMotionResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
    console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.SIGNIFICANT_MOTION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]WEAR\_DETECTION9+

on(type: SensorId.WEAR\_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options): void

订阅佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为WearDetectionResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
    console.info('Succeeded in invoking on. Wear status: ' + data.value);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.WEAR_DETECTION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]sensorStatusChange19+

on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>): void

监听传感器上线下线状态的变化，callback返回传感器状态事件数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'sensorStatusChange' | 是 | 固定传入'sensorStatusChange',状态监听固定参数。 |
| callback | Callback<[SensorStatusEvent](#sensorstatusevent19)\> | 是 | 回调函数，异步上报的传感器事件数据SensorStatusEvent。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on('sensorStatusChange', (data: sensor.SensorStatusEvent) => {
    console.info('sensorStatusChange : ' + JSON.stringify(data));
  });
  setTimeout(() => {
    sensor.off('sensorStatusChange');
  }, 5000);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.once9+

#### \[h2\]ACCELEROMETER9+

once(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>): void

获取一次加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ACCELEROMETER\_UNCALIBRATED9+

once(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void

获取一次未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为AccelerometerUncalibratedResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]AMBIENT\_LIGHT9+

once(type: SensorId.AMBIENT\_LIGHT, callback: Callback<LightResponse>): void

获取一次环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](#lightresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为LightResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.AMBIENT_LIGHT, (data: sensor.LightResponse) => {
    console.info('Succeeded in invoking once. the ambient light intensity: ' + data.intensity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]AMBIENT\_TEMPERATURE9+

once(type: SensorId.AMBIENT\_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void

获取一次温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为AmbientTemperatureResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
    console.info('Succeeded in invoking once. Temperature: ' + data.temperature);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]BAROMETER9+

once(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>): void

获取一次气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为BarometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.BAROMETER, (data: sensor.BarometerResponse) => {
    console.info('Succeeded in invoking once. Atmospheric pressure: ' + data.pressure);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GRAVITY9+

once(type: SensorId.GRAVITY, callback: Callback<GravityResponse>): void

获取一次重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| callback | Callback<[GravityResponse](#gravityresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为GravityResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GYROSCOPE9+

once(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>): void

获取一次陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GYROSCOPE\_UNCALIBRATED9+

once(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void

获取一次未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为GyroscopeUncalibratedResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HALL9+

once(type: SensorId.HALL, callback: Callback<HallResponse>): void

获取一次霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| callback | Callback<[HallResponse](#hallresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为HallResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.HALL, (data: sensor.HallResponse) => {
    console.info('Succeeded in invoking once. Status: ' + data.status);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HEART\_RATE9+

once(type: SensorId.HEART\_RATE, callback: Callback<HeartRateResponse>): void

获取一次心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为HeartRateResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.HEART_RATE, (data: sensor.HeartRateResponse) => {
    console.info('Succeeded in invoking once. Heart rate: ' + data.heartRate);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HUMIDITY9+

once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>): void

获取一次湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为HumidityResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
    console.info('Succeeded in invoking once. Humidity: ' + data.humidity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]LINEAR\_ACCELEROMETER9+

once(type: SensorId.LINEAR\_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>): void

获取一次线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELEROMETER。 |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为LinearAccelerometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.LINEAR_ACCELEROMETER, (data: sensor.LinearAccelerometerResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]MAGNETIC\_FIELD9+

once(type: SensorId.MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>): void

获取一次磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED9+

once(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>): void

获取一次未经校准的磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为MagneticFieldUncalibratedResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ORIENTATION9+

once(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>): void

获取一次方向传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为OrientationResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
    console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
    console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
    console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PEDOMETER9+

once(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>): void

获取一次计步器传感器数据。计步传感器数据上报有一定延迟，延迟时间由具体的实现产品决定。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为PedometerResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.PEDOMETER, (data: sensor.PedometerResponse) => {
    console.info('Succeeded in invoking once. Step count: ' + data.steps);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PEDOMETER\_DETECTION9+

once(type: SensorId.PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>): void

获取一次计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为PedometerDetectionResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
    console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PROXIMITY9+

once(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>): void

获取一次接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为ProximityResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.PROXIMITY, (data: sensor.ProximityResponse) => {
    console.info('Succeeded in invoking once. Distance: ' + data.distance);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ROTATION\_VECTOR9+

once(type: SensorId.ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>): void

获取一次旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为RotationVectorResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. Scalar quantity: ' + data.w);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]SIGNIFICANT\_MOTION9+

once(type: SensorId.SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>): void

获取一次有效运动传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为SignificantMotionResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
    console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]WEAR\_DETECTION9+

once(type: SensorId.WEAR\_DETECTION, callback: Callback<WearDetectionResponse>): void

获取一次佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | 是 | 回调函数，异步上报的传感器数据固定为WearDetectionResponse。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
    console.info('Succeeded in invoking once. Wear status: ' + data.value);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.off

#### \[h2\]ACCELEROMETER9+

off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void

取消订阅加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ACCELEROMETER, callback1);
  sensor.on(sensor.SensorId.ACCELEROMETER, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.ACCELEROMETER, callback1);
  // 取消SensorId.ACCELEROMETER类型的所有回调
  sensor.off(sensor.SensorId.ACCELEROMETER);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ACCELEROMETER19+

off(type: SensorId.ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void

取消订阅加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.AccelerometerResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类别
const sensorType = sensor.SensorId.ACCELEROMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]ACCELEROMETER\_UNCALIBRATED9+

off(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void

取消订阅未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, callback1);
  sensor.on(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.ACCELEROMETER_UNCALIBRATED, callback1);
  // 取消注册SensorId.ACCELEROMETER_UNCALIBRATED类型的所有回调
  sensor.off(sensor.SensorId.ACCELEROMETER_UNCALIBRATED);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]FUSION\_PRESSURE22+

off(type: SensorId.FUSION\_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void

取消订阅融合压力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).FUSION\_PRESSURE | 是 | 传感器类型，该值固定为SensorId.FUSION\_PRESSURE。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[FusionPressureResponse](#fusionpressureresponse22)\> | 否 | 取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.FusionPressureResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.FUSION_PRESSURE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]ACCELEROMETER\_UNCALIBRATED19+

off(type: SensorId.ACCELEROMETER\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerUncalibratedResponse>): void

取消订阅未校准加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.ACCELEROMETER\_UNCALIBRATED。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.AccelerometerUncalibratedResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.ACCELEROMETER_UNCALIBRATED;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]AMBIENT\_LIGHT9+

off(type: SensorId.AMBIENT\_LIGHT, callback?: Callback<LightResponse>): void

取消订阅环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](#lightresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.AMBIENT_LIGHT, callback1);
  sensor.on(sensor.SensorId.AMBIENT_LIGHT, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.AMBIENT_LIGHT, callback1);
  // 取消注册SensorId.AMBIENT_LIGHT
  sensor.off(sensor.SensorId.AMBIENT_LIGHT);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]AMBIENT\_LIGHT19+

off(type: SensorId.AMBIENT\_LIGHT, sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void

取消订阅环境光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_LIGHT。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[LightResponse](#lightresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.LightResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.AMBIENT_LIGHT;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]AMBIENT\_TEMPERATURE9+

off(type: SensorId.AMBIENT\_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void

取消订阅温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.AMBIENT_TEMPERATURE, callback1);
  sensor.on(sensor.SensorId.AMBIENT_TEMPERATURE, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.AMBIENT_TEMPERATURE, callback1);
  // 取消注册SensorId.AMBIENT_TEMPERATURE的所有回调
  sensor.off(sensor.SensorId.AMBIENT_TEMPERATURE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]AMBIENT\_TEMPERATURE19+

off(type: SensorId.AMBIENT\_TEMPERATURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<AmbientTemperatureResponse>): void

取消订阅温度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | 是 | 传感器类型，该值固定为SensorId.AMBIENT\_TEMPERATURE。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.AmbientTemperatureResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.AMBIENT_TEMPERATURE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]BAROMETER9+

off(type: SensorId.BAROMETER, callback?: Callback<BarometerResponse>): void

取消订阅气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
    console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
    console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
    sensor.on(sensor.SensorId.BAROMETER, callback1);
    sensor.on(sensor.SensorId.BAROMETER, callback2);
    // 仅取消callback1的注册
    sensor.off(sensor.SensorId.BAROMETER, callback1);
    // 取消注册SensorId.BAROMETER的所有回调
    sensor.off(sensor.SensorId.BAROMETER);
} catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]BAROMETER19+

off(type: SensorId.BAROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<BarometerResponse>): void

取消订阅气压计传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | 是 | 传感器类型，该值固定为SensorId.BAROMETER。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.BarometerResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.BAROMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]GRAVITY9+

off(type: SensorId.GRAVITY, callback?: Callback<GravityResponse>): void

取消订阅重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| callback | Callback<[GravityResponse](#gravityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.GRAVITY, callback1);
  sensor.on(sensor.SensorId.GRAVITY, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.GRAVITY, callback1);
  // 取消注册SensorId.GRAVITY的所有回调
  sensor.off(sensor.SensorId.GRAVITY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GRAVITY19+

off(type: SensorId.GRAVITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<GravityResponse>): void

取消订阅重力传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | 是 | 传感器类型，该值固定为SensorId.GRAVITY。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[GravityResponse](#gravityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.GravityResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.GRAVITY;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]GYROSCOPE9+

off(type: SensorId.GYROSCOPE, callback?: Callback<GyroscopeResponse>): void

取消订阅陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.GYROSCOPE, callback1);
  sensor.on(sensor.SensorId.GYROSCOPE, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.GYROSCOPE, callback1);
  // 取消注册SensorId.GYROSCOPE的所有回调
  sensor.off(sensor.SensorId.GYROSCOPE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GYROSCOPE19+

off(type: SensorId.GYROSCOPE, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeResponse>): void

取消订阅陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.GyroscopeResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.GYROSCOPE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]GYROSCOPE\_UNCALIBRATED9+

off(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void

取消订阅未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.GYROSCOPE_UNCALIBRATED, callback1);
  sensor.on(sensor.SensorId.GYROSCOPE_UNCALIBRATED, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.GYROSCOPE_UNCALIBRATED, callback1);
  // 取消注册SensorId.GYROSCOPE_UNCALIBRATED的所有回调
  sensor.off(sensor.SensorId.GYROSCOPE_UNCALIBRATED);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]GYROSCOPE\_UNCALIBRATED19+

off(type: SensorId.GYROSCOPE\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeUncalibratedResponse>): void

取消订阅未校准陀螺仪传感器数据。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.GYROSCOPE\_UNCALIBRATED。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.GyroscopeUncalibratedResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.GYROSCOPE_UNCALIBRATED;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]HALL9+

off(type: SensorId.HALL, callback?: Callback<HallResponse>): void

取消订阅霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| callback | Callback<[HallResponse](#hallresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.HALL, callback1);
  sensor.on(sensor.SensorId.HALL, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.HALL, callback1);
  // 取消注册SensorId.HALL的所有回调
  sensor.off(sensor.SensorId.HALL);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HALL19+

off(type: SensorId.HALL, sensorInfoParam?: SensorInfoParam, callback?: Callback<HallResponse>): void

取消订阅霍尔传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | 是 | 传感器类型，该值固定为SensorId.HALL。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[HallResponse](#hallresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.HallResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.HALL;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]HEART\_RATE9+

off(type: SensorId.HEART\_RATE, callback?: Callback<HeartRateResponse>): void

取消订阅心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.HEART_RATE, callback1);
  sensor.on(sensor.SensorId.HEART_RATE, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.HEART_RATE, callback1);
  // 取消注册SensorId.HEART_RATE的所有回调
  sensor.off(sensor.SensorId.HEART_RATE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HEART\_RATE19+

off(type: SensorId.HEART\_RATE, sensorInfoParam?: SensorInfoParam, callback?: Callback<HeartRateResponse>): void

取消订阅心率传感器数据。

**需要权限**：ohos.permission.READ\_HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | 是 | 传感器类型，该值固定为SensorId.HEART\_RATE。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.HeartRateResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.HEART_RATE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]HUMIDITY9+

off(type: SensorId.HUMIDITY, callback?: Callback<HumidityResponse>): void

取消订阅湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.HUMIDITY, callback1);
  sensor.on(sensor.SensorId.HUMIDITY, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.HUMIDITY, callback1);
  // 取消注册SensorId.HUMIDITY的所有回调
  sensor.off(sensor.SensorId.HUMIDITY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]HUMIDITY19+

off(type: SensorId.HUMIDITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<HumidityResponse>): void

取消订阅湿度传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | 是 | 传感器类型，该值固定为SensorId.HUMIDITY。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.HumidityResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.HUMIDITY;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]LINEAR\_ACCELEROMETER9+

off(type: SensorId.LINEAR\_ACCELEROMETER, callback?: Callback<LinearAccelerometerResponse>): void

取消订阅线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.LINEAR_ACCELEROMETER, callback1);
  sensor.on(sensor.SensorId.LINEAR_ACCELEROMETER, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.LINEAR_ACCELEROMETER, callback1);
  // 取消注册SensorId.LINEAR_ACCELEROMETER的所有回调
  sensor.off(sensor.SensorId.LINEAR_ACCELEROMETER);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]LINEAR\_ACCELEROMETER19+

off(type: SensorId.LINEAR\_ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void

取消订阅线性加速度传感器数据。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | 是 | 传感器类型，该值固定为SensorId.LINEAR\_ACCELERATION。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.LinearAccelerometerResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.LINEAR_ACCELEROMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]MAGNETIC\_FIELD9+

off(type: SensorId.MAGNETIC\_FIELD, callback?: Callback<MagneticFieldResponse>): void

取消订阅磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.MAGNETIC_FIELD, callback1);
  sensor.on(sensor.SensorId.MAGNETIC_FIELD, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.MAGNETIC_FIELD, callback1);
  // 取消注册SensorId.MAGNETIC_FIELD的所有回调
  sensor.off(sensor.SensorId.MAGNETIC_FIELD);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]MAGNETIC\_FIELD19+

off(type: SensorId.MAGNETIC\_FIELD, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void

取消订阅磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.MagneticFieldResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.MAGNETIC_FIELD;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED9+

off(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void

取消订阅未校准的磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback1);
  sensor.on(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback1);
  // 取消注册SensorId.MAGNETIC_FIELD_UNCALIBRATED的所有回调
  sensor.off(sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED19+

off(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldUncalibratedResponse>): void

取消订阅未校准的磁场传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 传感器类型，该值固定为SensorId.MAGNETIC\_FIELD\_UNCALIBRATED。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.MagneticFieldUncalibratedResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.MAGNETIC_FIELD_UNCALIBRATED;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]ORIENTATION9+

off(type: SensorId.ORIENTATION, callback?: Callback<OrientationResponse>): void

取消订阅方向传感器数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ORIENTATION, callback1);
  sensor.on(sensor.SensorId.ORIENTATION, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.ORIENTATION, callback1);
  // 取消注册SensorId.ORIENTATION的所有回调
  sensor.off(sensor.SensorId.ORIENTATION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ORIENTATION19+

off(type: SensorId.ORIENTATION, sensorInfoParam?: SensorInfoParam, callback?: Callback<OrientationResponse>): void

取消订阅方向传感器数据。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | 是 | 传感器类型，该值固定为SensorId.ORIENTATION。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.OrientationResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.ORIENTATION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]PEDOMETER9+

off(type: SensorId.PEDOMETER, callback?: Callback<PedometerResponse>): void

取消订阅计步器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.PEDOMETER, callback1);
  sensor.on(sensor.SensorId.PEDOMETER, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.PEDOMETER, callback1);
  // 取消注册SensorId.PEDOMETER的所有回调
  sensor.off(sensor.SensorId.PEDOMETER);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PEDOMETER19+

off(type: SensorId.PEDOMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerResponse>): void

取消订阅计步器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | 是 | 传感器类型，该值固定为SensorId.PEDOMETER。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.PedometerResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.PEDOMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]PEDOMETER\_DETECTION9+

off(type: SensorId.PEDOMETER\_DETECTION, callback?: Callback<PedometerDetectionResponse>): void

取消订阅计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.PEDOMETER_DETECTION, callback1);
  sensor.on(sensor.SensorId.PEDOMETER_DETECTION, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.PEDOMETER_DETECTION, callback1);
  // 取消注册SensorId.PEDOMETER_DETECTION的所有回调
  sensor.off(sensor.SensorId.PEDOMETER_DETECTION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PEDOMETER\_DETECTION19+

off(type: SensorId.PEDOMETER\_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerDetectionResponse>): void

取消订阅计步检测器传感器数据。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | 是 | 传感器类型，该值固定为SensorId.PEDOMETER\_DETECTION。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.PedometerDetectionResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.PEDOMETER_DETECTION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]PROXIMITY9+

off(type: SensorId.PROXIMITY, callback?: Callback<ProximityResponse>): void

取消订阅接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.PROXIMITY, callback1);
  sensor.on(sensor.SensorId.PROXIMITY, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.PROXIMITY, callback1);
  // 取消注册SensorId.PROXIMITY的所有回调
  sensor.off(sensor.SensorId.PROXIMITY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]PROXIMITY19+

off(type: SensorId.PROXIMITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void

取消订阅接近光传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | 是 | 传感器类型，该值固定为SensorId.PROXIMITY。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.ProximityResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.PROXIMITY;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]ROTATION\_VECTOR9+

off(type: SensorId.ROTATION\_VECTOR, callback?: Callback<RotationVectorResponse>): void

取消订阅旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.ROTATION_VECTOR, callback1);
  sensor.on(sensor.SensorId.ROTATION_VECTOR, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.ROTATION_VECTOR, callback1);
  // 取消注册SensorId.ROTATION_VECTOR的所有回调
  sensor.off(sensor.SensorId.ROTATION_VECTOR);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]ROTATION\_VECTOR19+

off(type: SensorId.ROTATION\_VECTOR, sensorInfoParam?: SensorInfoParam, callback?: Callback<RotationVectorResponse>): void

取消订阅旋转矢量传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | 是 | 传感器类型，该值固定为SensorId.ROTATION\_VECTOR。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.RotationVectorResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.ROTATION_VECTOR;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]SIGNIFICANT\_MOTION9+

off(type: SensorId.SIGNIFICANT\_MOTION, callback?: Callback<SignificantMotionResponse>): void

取消订阅有效运动传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.SIGNIFICANT_MOTION, callback1);
  sensor.on(sensor.SensorId.SIGNIFICANT_MOTION, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.SIGNIFICANT_MOTION, callback1);
  // 取消注册SensorId.SIGNIFICANT_MOTION的所有回调
  sensor.off(sensor.SensorId.SIGNIFICANT_MOTION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]SIGNIFICANT\_MOTION19+

off(type: SensorId.SIGNIFICANT\_MOTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<SignificantMotionResponse>): void

取消订阅有效运动传感器数据。

**系统能力**:SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | 是 | 传感器类型，该值固定为SensorId.SIGNIFICANT\_MOTION。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.SignificantMotionResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.SIGNIFICANT_MOTION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]WEAR\_DETECTION9+

off(type: SensorId.WEAR\_DETECTION, callback?: Callback<WearDetectionResponse>): void

取消订阅佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.on(sensor.SensorId.WEAR_DETECTION, callback1);
  sensor.on(sensor.SensorId.WEAR_DETECTION, callback2);
  // 仅取消callback1的注册
  sensor.off(sensor.SensorId.WEAR_DETECTION, callback1);
  // 取消注册SensorId.WEAR_DETECTION的所有回调
  sensor.off(sensor.SensorId.WEAR_DETECTION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
}
```

#### \[h2\]WEAR\_DETECTION19+

off(type: SensorId.WEAR\_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void

取消订阅佩戴检测传感器数据。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | 是 | 传感器类型，该值固定为SensorId.WEAR\_DETECTION。 |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | 否 | 传感器传入设置参数，可指定deviceId、sensorIndex |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// 传感器回调
const sensorCallback = (response: sensor.WearDetectionResponse) => {
  console.info(`callback response: ${JSON.stringify(response)}`);
}
// 传感器监听类型
const sensorType = sensor.SensorId.WEAR_DETECTION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    // 查询所有的传感器
    const sensorList: sensor.Sensor[] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // 根据实际业务逻辑获取目标传感器。
    const targetSensor = sensorList
      // 按需过滤deviceId为1、sensorId为2的所有传感器。此处示例仅做展示，开发者需要自行调整筛选逻辑。
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // 可能存在的多个同类型传感器，选择sensorIndex为0的传感器。
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // 订阅传感器事件
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // 使用try catch对可能出现的异常进行捕获
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}`);
    ret = Ret.Failed;
  }
  return ret;
}
```

#### \[h2\]sensorStatusChange19+

off(type: 'sensorStatusChange', callback?: Callback<SensorStatusEvent>): void

取消监听传感器变化。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'sensorStatusChange' | 是 | 固定传入'sensorStatusChange',状态监听固定参数。 |
| callback | Callback<[SensorStatusEvent](#sensorstatusevent19)\> | 否 | sensor.on传入的回调函数，不传则取消所有监听。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  const statusChangeCallback = (data: sensor.SensorStatusEvent) => {
    console.info('sensorStatusChange : ' + JSON.stringify(data));
  }
  const statusChangeCallback2 = (data: sensor.SensorStatusEvent) => {
    console.info('sensorStatusChange2 : ' + JSON.stringify(data));
  }
  // 注册两个设备上线消息监听回调
  sensor.on('sensorStatusChange', statusChangeCallback);
  sensor.on('sensorStatusChange', statusChangeCallback2);
  
  // 3秒后注销第一个监听
  setTimeout(() => {
    sensor.off('sensorStatusChange', statusChangeCallback);
  }, 3000);
  // 5秒后注销所有监听
  setTimeout(() => {
    sensor.off('sensorStatusChange');
  }, 5000);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSensorListByDeviceSync19+

getSensorListByDeviceSync(deviceId?: number): Array<Sensor>

同步获取设备的所有传感器信息。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 否 | 设备ID，默认为查询本地设备，默认值为-1，表示本地设备，设备ID需通过[getSensorList](#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](#sensorstatuschange19)获取。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Array<[Sensor](#sensor9)\> | 传感器属性列表。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const deviceId = 1;
  // 第一个参数deviceId 非必填
  const sensorList: sensor.Sensor[] = sensor.getSensorListByDeviceSync(deviceId);
  console.info(`sensorList length: ${sensorList.length}`);
  console.info(`sensorList: ${JSON.stringify(sensorList)}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSingleSensorByDeviceSync19+

getSingleSensorByDeviceSync(type: SensorId, deviceId?: number): Array<Sensor>

同步获取指定设备和类型的传感器信息。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | 是 | 指定传感器类型。 |
| deviceId | number | 否 | 设备ID，默认为查询本地设备，默认值为-1，表示本地设备，设备ID需通过[getSensorList](#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](#sensorstatuschange19)获取。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Array<[Sensor](#sensor9)\> | 传感器属性列表。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const deviceId = 1;
  // 第二个参数deviceId 非必填
  const sensorList: sensor.Sensor[] = sensor.getSingleSensorByDeviceSync(sensor.SensorId.ACCELEROMETER, deviceId);
  console.info(`sensorList length: ${sensorList.length}`);
  console.info(`sensorList Json: ${JSON.stringify(sensorList)}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getGeomagneticInfo9+

getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void

获取某时刻地球上特定位置的地磁场信息，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | 是 | 地理位置，包括经度、纬度和海拔高度。 |
| timeMillis | number | 是 | 获取磁偏角的时间，unix时间戳，单位毫秒。 |
| callback | AsyncCallback<[GeomagneticResponse](#geomagneticresponse)\> | 是 | 回调函数，异步返回地磁场信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000,
      (err: BusinessError, data: sensor.GeomagneticResponse) => {
    if (err) {
      console.error(`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in getting geomagneticInfo x" + data.x);
    console.info("Succeeded in getting geomagneticInfo y" + data.y);
    console.info("Succeeded in getting geomagneticInfo z" + data.z);
    console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
    console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
    console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
    console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getGeomagneticInfo9+

getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>

获取某时刻地球上特定位置的地磁场信息，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | 是 | 地理位置，包括经度、纬度和海拔高度。 |
| timeMillis | number | 是 | 获取磁偏角的时间，unix时间戳，单位毫秒。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[GeomagneticResponse](#geomagneticresponse)\> | Promise对象，使用异步方式返回地磁场信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  const promise = sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
  promise.then((data: sensor.GeomagneticResponse) => {
    console.info("Succeeded in getting geomagneticInfo x" + data.x);
    console.info("Succeeded in getting geomagneticInfo y" + data.y);
    console.info("Succeeded in getting geomagneticInfo z" + data.z);
    console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
    console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
    console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
    console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
  }, (err: BusinessError) => {
    console.error(`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getDeviceAltitude9+

getDeviceAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void

根据气压值获取海拔高度，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| seaPressure | number | 是 | 海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 指定的气压值，单位为hPa。 |
| callback | AsyncCallback<number> | 是 | 回调函数，异步返回指定的气压值对应的海拔高度，单位为米。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let seaPressure = 1013.2;
  let currentPressure = 1500.0;
  sensor.getDeviceAltitude(seaPressure, currentPressure, (err: BusinessError, data: number) => {
    if (err) {
      console.error(`Failed to get altitude. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in getting altitude: ' + data);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get altitude. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getDeviceAltitude9+

getDeviceAltitude(seaPressure: number, currentPressure: number): Promise<number>

根据气压值获取海拔高度，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| seaPressure | number | 是 | 海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 指定的气压值，单位为hPa。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，使用异步方式返回指定的气压值对应的海拔高度，单位为米。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let seaPressure = 1013.2;
  let currentPressure = 1500.0;
  const promise = sensor.getDeviceAltitude(seaPressure, currentPressure);
  promise.then((data: number) => {
    console.info('Succeeded in getting sensor_getDeviceAltitude_Promise', data);
  }, (err: BusinessError) => {
    console.error(`Failed to get altitude. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get altitude. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getInclination9+

getInclination(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void

根据倾斜矩阵计算地磁倾角，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | 是 | 倾斜矩阵。 |
| callback | AsyncCallback<number> | 是 | 回调函数，异步返回地磁倾角，单位为弧度。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  // inclinationMatrix可以为3*3，或者4*4
  let inclinationMatrix = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ]
  sensor.getInclination(inclinationMatrix, (err: BusinessError, data: number) => {
    if (err) {
      console.error(`Failed to get inclination. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in getting inclination: ' + data);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get inclination. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getInclination9+

getInclination(inclinationMatrix: Array<number>): Promise<number>

根据倾斜矩阵计算地磁倾角，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | 是 | 倾斜矩阵。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，使用异步方式返回地磁倾斜角，单位为弧度。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  // inclinationMatrix可以为3*3，或者4*4
  let inclinationMatrix = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ]
  const promise = sensor.getInclination(inclinationMatrix);
  promise.then((data: number) => {
    console.info('Succeeded in getting inclination: ' + data);
  }, (err: BusinessError) => {
    console.error(`Failed to get inclination. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get inclination. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getAngleVariation9+

getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

计算两个旋转矩阵之间的角度变化，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | 是 | 当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 相对旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  // 旋转矩阵可以为3*3，或者4*4
  let currentRotationMatrix = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ];
  let preRotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  sensor.getAngleVariation(currentRotationMatrix, preRotationMatrix, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(`Failed to get angle variation. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    if (data.length < 3) {
      console.error("Failed to get angle variation, length" + data.length);
      return;
    }
    console.info("Z: " + data[0]);
    console.info("X: " + data[1]);
    console.info("Y: " + data[2]);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get angle variation. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getAngleVariation9+

getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>

得到两个旋转矩阵之间的角度变化，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | 是 | 当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 相对旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | Promise对象，使用异步方式返回绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  // 旋转矩阵可以为3*3，或者4*4
  let currentRotationMatrix = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ];
  let preRotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  const promise = sensor.getAngleVariation(currentRotationMatrix, preRotationMatrix);
  promise.then((data: Array<number>) => {
    if (data.length < 3) {
      console.error("Failed to get angle variation, length" + data.length);
      return;
    }
    console.info("Z: " + data[0]);
    console.info("X: " + data[1]);
    console.info("Y: " + data[2]);
  }, (err: BusinessError) => {
    console.error(`Failed to get angle variation. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get angle variation. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getRotationMatrix9+

getRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转矢量获取旋转矩阵，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回3\*3旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
  sensor.getRotationMatrix(rotationVector, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getRotationMatrix9+

getRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>

根据旋转矢量获取旋转矩阵，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | Promise对象，使用异步方式返回旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
  const promise = sensor.getRotationMatrix(rotationVector);
  promise.then((data: Array<number>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
    }
  }, (err: BusinessError) => {
    console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.transformRotationMatrix9+

transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void

根据指定坐标系映射旋转矩阵，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | 是 | 旋转矩阵。 |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | 是 | 指定坐标系方向。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回映射后的旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let rotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 }, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(`Failed to transform rotationMatrix. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + '] = ' + data[i]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.transformRotationMatrix9+

transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>

根据指定坐标系映射旋转矩阵，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | 是 | 旋转矩阵。 |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | 是 | 指定坐标系方向。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | Promise对象，使用异步方式返回转换后的旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例** ：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let rotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  const promise = sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 });
  promise.then((data: Array<number>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
    }
  }, (err: BusinessError) => {
    console.error(`Failed to transform rotationMatrix. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getQuaternion9+

getQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转向量计算归一化四元数，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回归一化四元数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
  sensor.getQuaternion(rotationVector, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(`Failed to get quaternion. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get quaternion. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getQuaternion9+

getQuaternion(rotationVector: Array<number>): Promise<Array<number>>

根据旋转向量计算归一化四元数，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | Promise，使用异步方式对象返归一化回四元数。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
    let rotationVector = [0.20046076, 0.21907, 0.73978853, 0.60376877];
    const promise = sensor.getQuaternion(rotationVector);
    promise.then((data: Array<number>) => {
        for (let i = 0; i < data.length; i++) {
            console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
        }
    }, (err: BusinessError) => {
        console.error(`Failed to get quaternion. Code: ${err.code}, message: ${err.message}`);
    });
} catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to get quaternion. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getOrientation9+

getOrientation(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转矩阵计算设备方向，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | 是 | 旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，异步返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let preRotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  sensor.getOrientation(preRotationMatrix, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(`Failed to get orientation. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    if (data.length < 3) {
      console.error("Failed to get orientation, length" + data.length);
    }
    console.info("Succeeded in getting data. Z: " + data[0]);
    console.info("Succeeded in getting data. X: " + data[1]);
    console.info("Succeeded in getting data. Y: " + data[2]);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get orientation. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getOrientation9+

getOrientation(rotationMatrix: Array<number>): Promise<Array<number>>

根据旋转矩阵计算设备的方向，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | 是 | 旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | Promise对象，使用异步方式返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let preRotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  const promise = sensor.getOrientation(preRotationMatrix);
  promise.then((data: Array<number>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + data[i]);
    }
  }, (err: BusinessError) => {
    console.error(`Failed to getOrientation. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to getOrientation Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getRotationMatrix9+

getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void

根据重力矢量和地磁矢量计算旋转矩阵，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | 是 | 重力矢量。 |
| geomagnetic | Array<number> | 是 | 地磁矢量。 |
| callback | AsyncCallback<[RotationMatrixResponse](#rotationmatrixresponse)\> | 是 | 回调函数，异步返回旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let gravity = [-0.27775216, 0.5351276, 9.788099];
  let geomagnetic = [210.87253, -78.6096, -111.44444];
  sensor.getRotationMatrix(gravity, geomagnetic, (err: BusinessError, data: sensor.RotationMatrixResponse) => {
    if (err) {
      console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in getting rotationMatrix' + JSON.stringify(data));
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getRotationMatrix9+

getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>

根据重力矢量和地磁矢量计算旋转矩阵，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | 是 | 重力向量。 |
| geomagnetic | Array<number> | 是 | 地磁矢量。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RotationMatrixResponse](#rotationmatrixresponse)\> | Promise对象，使用异步方式返回旋转矩阵。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let gravity = [-0.27775216, 0.5351276, 9.788099];
  let geomagnetic = [210.87253, -78.6096, -111.44444];
  const promise = sensor.getRotationMatrix(gravity, geomagnetic);
  promise.then((data: sensor.RotationMatrixResponse) => {
    console.info('Succeeded in getting rotationMatrix' + JSON.stringify(data));
  }, (err: BusinessError) => {
    console.error(`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSensorList9+

getSensorList(callback: AsyncCallback<Array<Sensor>>): void

获取设备上的所有传感器信息，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Sensor](#sensor9)\>> | 是 | 回调函数，异步返回传感器属性列表。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSensorList((err: BusinessError, data: Array<sensor.Sensor>) => {
    if (err) {
      console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + JSON.stringify(data[i]));
    }
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSensorList9+

getSensorList(): Promise<Array<Sensor>>

获取设备上的所有传感器信息，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[Sensor](#sensor9)\>> | Promise对象，使用异步方式返回传感器属性列表。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSensorList().then((data: Array<sensor.Sensor>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + JSON.stringify(data[i]));
    }
  }, (err: BusinessError) => {
    console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSensorListSync12+

getSensorListSync(): Array<Sensor>

获取设备上的所有传感器信息，使用同步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Array<[Sensor](#sensor9)\> | 使用同步方式返回传感器属性列表。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let ret = sensor.getSensorListSync()
  for (let i = 0; i < ret.length; i++) {
    console.info('Succeeded in getting sensor: ' + JSON.stringify(ret[i]));
  }
} catch(error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSingleSensor9+

getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void

获取指定传感器类型的属性信息，使用Callback异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | 是 | 指定传感器类型。 |
| callback | AsyncCallback<[Sensor](#sensor9)\> | 是 | 回调函数，异步返回指定传感器的属性信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER, (err: BusinessError, data: sensor.Sensor) => {
    if (err) {
      console.error(`Failed to get singleSensor. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
      console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
      console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
      console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    }, { interval: 100000000 });
    setTimeout(() => {
      sensor.off(sensor.SensorId.ACCELEROMETER);
    }, 500);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get singleSensor. Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSingleSensor9+

getSingleSensor(type: SensorId): Promise<Sensor>

获取指定类型的传感器信息，使用Promise异步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | 是 | 传感器类型。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Sensor](#sensor9)\> | 使用异步方式返回传感器信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER).then((data: sensor.Sensor) => {
    console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
  }, (err: BusinessError) => {
    console.error(`Failed to get singleSensor . Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

#### sensor.getSingleSensorSync12+

getSingleSensorSync(type: SensorId): Sensor

获取指定类型的传感器信息，使用同步方式返回结果。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | 是 | 传感器类型。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Sensor | 使用同步方式返回传感器信息。 |

**错误码**：

以下错误码的详细介绍请参见[传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。错误码和错误信息会以异常的形式抛出，调用接口时需要使用try catch对可能出现的异常进行捕获操作。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let ret = sensor.getSingleSensorSync(sensor.SensorId.ACCELEROMETER);
  console.info('Succeeded in getting sensor: ' + JSON.stringify(ret));
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

#### SensorId9+

表示当前支持订阅或取消订阅的传感器类型。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ACCELEROMETER | 1 | 
加速度传感器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| GYROSCOPE | 2 | 

陀螺仪传感器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| AMBIENT\_LIGHT | 5 | 环境光传感器。 |
| MAGNETIC\_FIELD | 6 | 磁场传感器。 |
| BAROMETER | 8 | 气压计传感器。 |
| HALL | 10 | 霍尔传感器。 |
| PROXIMITY | 12 | 接近光传感器。 |
| HUMIDITY | 13 | 湿度传感器。 |
| ORIENTATION | 256 | 

方向传感器。

**元服务API**：从API version 11开始，该接口在支持元服务中使用。

 |
| GRAVITY | 257 | 重力传感器。 |
| LINEAR\_ACCELEROMETER | 258 | 线性加速度传感器。 |
| ROTATION\_VECTOR | 259 | 旋转矢量传感器。 |
| AMBIENT\_TEMPERATURE | 260 | 环境温度传感器。 |
| MAGNETIC\_FIELD\_UNCALIBRATED | 261 | 未校准磁场传感器。 |
| GYROSCOPE\_UNCALIBRATED | 263 | 未校准陀螺仪传感器。 |
| SIGNIFICANT\_MOTION | 264 | 有效运动传感器。 |
| PEDOMETER\_DETECTION | 265 | 计步检测传感器。 |
| PEDOMETER | 266 | 计步传感器。 |
| HEART\_RATE | 278 | 心率传感器。 |
| WEAR\_DETECTION | 280 | 佩戴检测传感器。 |
| ACCELEROMETER\_UNCALIBRATED | 281 | 未校准加速度计传感器。 |
| FUSION\_PRESSURE22+ | 283 | 

融合压力传感器。

仅智能表有该传感器

 |

#### SensorInfoParam19+

传感器传入设置参数，多传感器情况下通过deviceId、sensorIndex控制指定传感器。

**系统能力**：SystemCapability.Sensors.Sensor

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | number | 否 | 是 | 
设备ID：默认值为-1，表示本地设备，设备ID需通过[getSensorList](#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](#sensorstatuschange19)获取。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

 |
| sensorIndex | number | 否 | 是 | 

传感器索引：默认值为0，为设备上的默认传感器，其它传感器ID需通过[getSensorList](#sensorgetsensorlist9)查询或者监听设备上下线接口[sensorStatusChange](#sensorstatuschange19)获取。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

 |

#### SensorStatusEvent19+

设备状态变化事件数据。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| timestamp | number | 否 | 否 | 事件发生的时间戳，单位ms。 |
| sensorId | number | 否 | 否 | 传感器ID。 |
| sensorIndex | number | 否 | 否 | 传感器索引。 |
| isSensorOnline | boolean | 否 | 否 | 传感器上线或者下线，true为上线，false为下线。 |
| deviceId | number | 否 | 否 | 设备ID。 |
| deviceName | string | 否 | 否 | 设备名称。 |

#### SensorAccuracy11+

传感器数据的精度。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ACCURACY\_UNRELIABLE | 0 | 传感器数据不可信。 |
| ACCURACY\_LOW | 1 | 传感器低挡位精度。 |
| ACCURACY\_MEDIUM | 2 | 传感器中挡位精度。 |
| ACCURACY\_HIGH | 3 | 传感器高挡位精度。 |

#### Response

传感器数据的时间戳。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| timestamp | number | 否 | 否 | 传感器数据上报的时间戳。从设备开机开始计时到上报数据的时间，单位 : ns。 |
| accuracy11+ | [SensorAccuracy](#sensoraccuracy11)11+ | 否 | 否 | 传感器数据上报的精度挡位值。 |

#### Sensor9+

指示传感器信息。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| sensorName | string | 否 | 否 | 传感器名称。 |
| vendorName | string | 否 | 否 | 传感器供应商。 |
| firmwareVersion | string | 否 | 否 | 传感器固件版本。 |
| hardwareVersion | string | 否 | 否 | 传感器硬件版本。 |
| sensorId | number | 否 | 否 | 传感器类型id。 |
| maxRange | number | 否 | 否 | 传感器测量范围的最大值。 |
| minSamplePeriod | number | 否 | 否 | 允许的最小采样周期。 |
| maxSamplePeriod | number | 否 | 否 | 允许的最大采样周期。 |
| precision | number | 否 | 否 | 传感器精度。 |
| power | number | 否 | 否 | 传感器功率的估计值，单位：mA。 |
| sensorIndex19+ | number | 否 | 是 | 传感器索引。 |
| deviceId19+ | number | 否 | 是 | 设备ID。 |
| deviceName19+ | string | 否 | 是 | 设备名称。 |
| isLocalSensor19+ | boolean | 否 | 是 | 是否本地传感器，true为本地传感器，false为非本地传感器。 |
| isMockSensor23+ | boolean | 否 | 是 | 是否mock传感器，true为mock传感器，false为非mock传感器。 |

#### AccelerometerResponse

加速度传感器数据，继承于[Response](#response)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 施加在设备x轴的加速度，单位 : m/s²；取值为实际上报物理量。 |
| y | number | 否 | 否 | 施加在设备y轴的加速度，单位 : m/s²；取值为实际上报物理量。 |
| z | number | 否 | 否 | 施加在设备z轴的加速度，单位 : m/s²；取值为实际上报物理量。 |

#### LinearAccelerometerResponse

线性加速度传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 施加在设备x轴的线性加速度，单位 : m/s²。 |
| y | number | 否 | 否 | 施加在设备y轴的线性加速度，单位 : m/s²。 |
| z | number | 否 | 否 | 施加在设备z轴的线性加速度，单位 : m/s²。 |

#### AccelerometerUncalibratedResponse

未校准加速度计传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 施加在设备x轴未校准的加速度，单位 : m/s²。 |
| y | number | 否 | 否 | 施加在设备y轴未校准的加速度，单位 : m/s²。 |
| z | number | 否 | 否 | 施加在设备z轴未校准的加速度，单位 : m/s²。 |
| biasX | number | 否 | 否 | 施加在设备x轴未校准的加速度偏量，单位 : m/s²。 |
| biasY | number | 否 | 否 | 施加在设备y轴未校准的加速度偏量，单位 : m/s²。 |
| biasZ | number | 否 | 否 | 施加在设备z轴未校准的加速度偏量，单位 : m/s²。 |

#### FusionPressureResponse22+

融合压力传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| fusionPressure | number | 否 | 否 | 施加在融合压力传感器上的压力值百分比，单位 : % |

#### GravityResponse

重力传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 施加在设备x轴的重力加速度，单位 : m/s²。 |
| y | number | 否 | 否 | 施加在设备y轴的重力加速度，单位 : m/s²。 |
| z | number | 否 | 否 | 施加在设备z轴的重力加速度，单位 : m/s²。 |

#### OrientationResponse

方向传感器数据，继承于[Response](#response)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| alpha | number | 否 | 否 | 设备围绕Z轴的旋转角度，单位：度；取值范围为0-360度。 |
| beta | number | 否 | 否 | 设备围绕X轴的旋转角度，单位：度；取值范围为0-±180度。 |
| gamma | number | 否 | 否 | 设备围绕Y轴的旋转角度，单位：度；取值范围为0-±90度。 |

#### RotationVectorResponse

旋转矢量传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 旋转矢量x轴分量。 |
| y | number | 否 | 否 | 旋转矢量y轴分量。 |
| z | number | 否 | 否 | 旋转矢量z轴分量。 |
| w | number | 否 | 否 | 标量，描述设备相对于某个参考方向的旋转状态，单位：弧度。 |

#### GyroscopeResponse

陀螺仪传感器数据，继承于[Response](#response)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 设备x轴的旋转角速度，单位rad/s；取值为实际上报物理量。 |
| y | number | 否 | 否 | 设备y轴的旋转角速度，单位rad/s；取值为实际上报物理量。 |
| z | number | 否 | 否 | 设备z轴的旋转角速度，单位rad/s；取值为实际上报物理量。 |

#### GyroscopeUncalibratedResponse

未校准陀螺仪传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 设备x轴未校准的旋转角速度，单位rad/s。 |
| y | number | 否 | 否 | 设备y轴未校准的旋转角速度，单位rad/s。 |
| z | number | 否 | 否 | 设备z轴未校准的旋转角速度，单位rad/s。 |
| biasX | number | 否 | 否 | 设备x轴未校准的旋转角速度偏量，单位rad/s。 |
| biasY | number | 否 | 否 | 设备y轴未校准的旋转角速度偏量，单位rad/s。 |
| biasZ | number | 否 | 否 | 设备z轴未校准的旋转角速度偏量，单位rad/s。 |

#### SignificantMotionResponse

有效运动传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| scalar | number | 否 | 否 | 表示剧烈运动程度。测量三个物理轴（x、y 和 z）上，设备是否存在大幅度运动；若存在大幅度运动则数据上报为1。 |

#### ProximityResponse

接近光传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| distance | number | 否 | 否 | 可见物体与设备显示器的接近程度。0表示接近，大于0表示远离。 |

#### LightResponse

环境光传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| intensity | number | 否 | 否 | 光强（单位：勒克斯）。 |
| colorTemperature12+ | number | 否 | 是 | 色温（单位：开尔文），可选参数，如果该参数不支持则返回固定值（固定值由传感器自定义），支持则返回正常数值。 |
| infraredLuminance12+ | number | 否 | 是 | 红外亮度（单位：cd/m²），可选参数，如果该参数不支持则返回固定值（固定值由传感器自定义），支持则返回正常数值。 |

#### HallResponse

霍尔传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| status | number | 否 | 否 | 显示霍尔状态。测量设备周围是否存在磁力吸引，0表示没有，大于0表示有。 |

#### MagneticFieldResponse

磁场传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | x轴环境磁场强度，单位 : μT。 |
| y | number | 否 | 否 | y轴环境磁场强度，单位 : μT。 |
| z | number | 否 | 否 | z轴环境磁场强度，单位 : μT。 |

#### MagneticFieldUncalibratedResponse

未校准磁场传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | x轴未校准环境磁场强度，单位 : μT。 |
| y | number | 否 | 否 | y轴未校准环境磁场强度，单位 : μT。 |
| z | number | 否 | 否 | z轴未校准环境磁场强度，单位 : μT。 |
| biasX | number | 否 | 否 | x轴未校准环境磁场强度偏量，单位 : μT。 |
| biasY | number | 否 | 否 | y轴未校准环境磁场强度偏量，单位 : μT。 |
| biasZ | number | 否 | 否 | z轴未校准环境磁场强度偏量，单位 : μT。 |

#### PedometerResponse

计步传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| steps | number | 否 | 否 | 用户的行走步数。 |

#### HumidityResponse

湿度传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| humidity | number | 否 | 否 | 湿度值。测量环境的相对湿度，以百分比 (%) 表示。 |

#### PedometerDetectionResponse

计步检测传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| scalar | number | 否 | 否 | 计步器检测。检测用户的计步动作，如果取值为1则代表用户产生了计步行走的动作，取值为0则代表用户没有发生运动。 |

#### AmbientTemperatureResponse

温度传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| temperature | number | 否 | 否 | 环境温度（单位：摄氏度）。 |

#### BarometerResponse

气压计传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| pressure | number | 否 | 否 | 压力值（单位：百帕）。 |

#### HeartRateResponse

心率传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| heartRate | number | 否 | 否 | 心率值。测量用户的心率数值，单位：bpm。 |

#### WearDetectionResponse

佩戴检测传感器数据，继承于[Response](#response)。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| value | number | 否 | 否 | 表示设备是否被穿戴（1表示已穿戴，0表示未穿戴）。 |

#### Options

设置传感器上报频率。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| interval | number|[SensorFrequency](#sensorfrequency11)11+ | 否 | 是 | 表示传感器的上报频率，默认值为200000000ns。该属性有最小值和最大值的限制，由硬件支持的上报频率决定，当设置频率大于最大值时以最大值上报数据，小于最小值时以最小值上报数据。 |
| sensorInfoParam19+ | [SensorInfoParam](#sensorinfoparam19) | 否 | 是 | 
传感器传入设置参数，可指定deviceId、sensorIndex。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

 |

#### SensorFrequency11+

type SensorFrequency = 'game' | 'ui' | 'normal'

传感器上报频率模式。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Sensors.Sensor

| 类型 | 说明 |
| :-- | :-- |
| 'game' | 用于指定传感器上报频率，频率值为20000000ns，该频率被设置在硬件支持的频率范围内时会生效，值固定为'game'字符串。 |
| 'ui' | 用于指定传感器上报频率，频率值为60000000ns，该频率被设置在硬件支持的频率范围内时会生效，值固定为'ui'字符串。 |
| 'normal' | 用于指定传感器上报频率，频率值为200000000ns，该频率被设置在硬件支持的频率范围内时会生效，值固定为'normal'字符串。 |

#### RotationMatrixResponse

设置旋转矩阵响应对象。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| rotation | Array<number> | 否 | 否 | 旋转矩阵。 |
| inclination | Array<number> | 否 | 否 | 倾斜矩阵。 |

#### CoordinatesOptions

设置坐标选项对象。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | x坐标方向。 |
| y | number | 否 | 否 | y坐标方向。 |

#### GeomagneticResponse

设置地磁响应对象。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 地磁场的北分量，单位nT。 |
| y | number | 否 | 否 | 地磁场的东分量，单位nT。 |
| z | number | 否 | 否 | 地磁场的垂直分量，单位nT。 |
| geomagneticDip | number | 否 | 否 | 地磁倾角，即地球磁场线与水平面的夹角，单位度（°）。 |
| deflectionAngle | number | 否 | 否 | 地磁偏角，即地磁北方向与正北方向在水平面上的角度，单位度（°）。 |
| levelIntensity | number | 否 | 否 | 地磁场的水平强度，单位nT。 |
| totalIntensity | number | 否 | 否 | 地磁场的总强度，单位nT。 |

#### LocationOptions

指示地理位置。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| latitude | number | 否 | 否 | 纬度，单位度（°）。 |
| longitude | number | 否 | 否 | 经度，单位度（°）。 |
| altitude | number | 否 | 否 | 海拔高度，单位m。 |

#### sensor.on(deprecated)

#### \[h2\]ACCELEROMETER(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback: Callback<AccelerometerResponse>,options?: Options): void

监听加速度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/W9h_tWkcTTGIx6F-VsBlHQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=71266607D1C9A7B2B29D3BCF475BC17782675F847D4E89219354165FCC953B8E)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ACCELEROMETER](#accelerometer9)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | 是 | 要订阅的加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | 是 | 注册加速度传感器的回调函数，上报的数据类型为AccelerometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);
```

#### \[h2\]LINEAR\_ACCELERATION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION,callback:Callback<LinearAccelerometerResponse>, options?: Options): void

监听线性加速度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/LpZtYWJ9SkK0S34fLxCJXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=BC879BC32DEE1CF9BF01FFC123B4039715636C6D0611B313A2E1764358DFE110)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.LINEAR\_ACCELEROMETER](#linear_accelerometer9)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 是 | 要订阅的线性加速度传感器类型为SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | 是 | 注册线性加速度传感器的回调函数，上报的数据类型为LinearAccelerometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

#### \[h2\]ACCELEROMETER\_UNCALIBRATED(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED,callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void

监听未校准加速度计传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/B8BgnWIjSESokIJZ35wTSQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=3CB9C869ECAF61E1047EEA5EF54C27970F354B8F20759E16132385289E605544)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ACCELEROMETER\_UNCALIBRATED](#accelerometer_uncalibrated9)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 是 | 要订阅的未校准加速度计传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | 是 | 注册未校准加速度计传感器的回调函数，上报的数据类型为AccelerometerUncalibratedResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
},
  { interval: 100000000 }
);
```

#### \[h2\]GRAVITY(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback: Callback<GravityResponse>,options?: Options): void

监听重力传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/dwdpWTxnTeWqn2bdtvr1PA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=BDD193B2D4BE8E7DAD5D6515C627787207C966598CE53322E2043F33BD84B3C6)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.GRAVITY](#gravity9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | 是 | 要订阅的重力传感器类型为SENSOR\_TYPE\_ID\_GRAVITY。 |
| callback | Callback<[GravityResponse](#gravityresponse)\> | 是 | 注册重力传感器的回调函数，上报的数据类型为GravityResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_GRAVITY, (data: sensor.GravityResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);
```

#### \[h2\]GYROSCOPE(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void

监听陀螺仪传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/2-lScCxwRqmxUfYBeilEnQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=C54B7D3983B0E1B7DEA2336BCB2D021059C446626C65F96ED24574095B43FAD7)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.GYROSCOPE](#gyroscope9)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | 是 | 要订阅的陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | 是 | 注册陀螺仪传感器的回调函数，上报的数据类型为GyroscopeResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE, (data: sensor.GyroscopeResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);
```

#### \[h2\]GYROSCOPE\_UNCALIBRATED(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED,callback:Callback<GyroscopeUncalibratedResponse>, options?: Options): void

监听未校准陀螺仪传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/C24lB8mjQKK8-qNqa7acXg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=0348ACB53A932AF1365FFEF3AE70A7309B4411FFB3918CFAA4532D7CCADFFAB5)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.GYROSCOPE\_UNCALIBRATED](#gyroscope_uncalibrated9)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 是 | 要订阅的未校准陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | 是 | 注册未校准陀螺仪传感器的回调函数，上报的数据类型为GyroscopeUncalibratedResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
},
  { interval: 100000000 }
);
```

#### \[h2\]SIGNIFICANT\_MOTION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void

监听有效运动传感器数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/gYK8atHnSCC8cyjwKeAMMQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=64469811C6CE0DE804677EBA52A0331A530D9FF80E58D3289F1BBD522EFAB0B3)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.SIGNIFICANT\_MOTION](#significant_motion9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 是 | 要订阅的有效运动传感器类型为SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | 是 | 注册有效运动传感器的回调函数，上报的数据类型为SignificantMotionResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
  console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
},
  { interval: 100000000 }
);
```

#### \[h2\]PEDOMETER\_DETECTION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void

监听计步检测传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/lsXEBnI2QPyyewQIUpQo0Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=FB071C9DDA88232DB31BB1765ABBEC09C5FAA1E6C0769660B97FCB443C28A7C6)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.PEDOMETER\_DETECTION](#pedometer_detection9)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 是 | 要订阅的计步检测传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | 是 | 注册计步检测传感器的回调函数，上报的数据类型为PedometerDetectionResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
  console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
},
  { interval: 100000000 }
);
```

#### \[h2\]PEDOMETER(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void

监听计步传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/BLWAYMmbQzi1m4O9LsG03A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=E999A9E73634ED26B4222D415B202A6A7644C7F86F5A92324D7690781C44F3F7)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.PEDOMETER](#pedometer9)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | 是 | 要订阅的计步传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER。 |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | 是 | 注册计步传感器的回调函数，上报的数据类型为PedometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER, (data: sensor.PedometerResponse) => {
  console.info('Succeeded in invoking on. Steps: ' + data.steps);
},
  { interval: 100000000 }
);
```

#### \[h2\]AMBIENT\_TEMPERATURE(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE,callback:Callback<AmbientTemperatureResponse>, options?: Options): void

监听环境温度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/w5jTWeXhR8K1rsCaw81YjA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=29A3019186008EA1FD413E2D65FBF3F8208F87AD841B7C89641B23E251DC57F4)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.AMBIENT\_TEMPERATURE](#ambient_temperature9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 是 | 要订阅的环境温度传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | 是 | 注册环境温度传感器的回调函数，上报的数据类型为AmbientTemperatureResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
  console.info('Succeeded in invoking on. Temperature: ' + data.temperature);
},
  { interval: 100000000 }
);
```

#### \[h2\]MAGNETIC\_FIELD(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>,options?: Options): void

监听磁场传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/IxK1BAyGSTix8-F2_yc5VA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=0EB572C0A376990472DD4F2586A0FF8DE840FFACE33008D52EF430A5F7F8D041)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.MAGNETIC\_FIELD](#magnetic_field9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 是 | 要订阅的磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | 是 | 注册磁场传感器的回调函数，上报的数据类型为MagneticFieldResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);
```

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED,callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void

监听未校准磁场传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/jbEAT07qRzGnQnHZRzAbcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=138181C05EEB8B525A9853FC52CF4D388C62929E51245BE84C2D708DB64E9E83)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.MAGNETIC\_FIELD\_UNCALIBRATED](#magnetic_field_uncalibrated9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 要订阅的未校准磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | 是 | 注册未校准磁场传感器的回调函数，上报的数据类型为MagneticFieldUncalibratedResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
},
  { interval: 100000000 }
);
```

#### \[h2\]PROXIMITY(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback: Callback<ProximityResponse>,options?: Options): void

监听接近光传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/y14Awtb_RWueT6v6WjLrXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=A93FAE8B4A5B1076DA316AE62FEB7A8AD24917B3BFEFAD4E51AE73645CA4FA65)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.PROXIMITY](#proximity9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | 是 | 要订阅的接近光传感器类型为SENSOR\_TYPE\_ID\_PROXIMITY。 |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | 是 | 注册接近光传感器的回调函数，上报的数据类型为ProximityResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，默认值为200000000ns。当接近光事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_PROXIMITY, (data: sensor.ProximityResponse) => {
  console.info('Succeeded in invoking on. Distance: ' + data.distance);
},
  { interval: 100000000 }
);
```

#### \[h2\]HUMIDITY(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback: Callback<HumidityResponse>,options?: Options): void

监听湿度传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/KeR7bua6ScGea3IqF4trCQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=0B2C0A41936F03FE29395DBCA51D67B3B9D80880C125EB1FCCD82207B5CE98DA)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.HUMIDITY](#humidity9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | 是 | 要订阅的湿度传感器类型为SENSOR\_TYPE\_ID\_HUMIDITY。 |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | 是 | 注册湿度传感器的回调函数，上报的数据类型为HumidityResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_HUMIDITY, (data: sensor.HumidityResponse) => {
  console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
},
  { interval: 100000000 }
);
```

#### \[h2\]BAROMETER(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback: Callback<BarometerResponse>,options?: Options): void

监听气压计传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/rRSpYkbsS_e_Qmifrl6l7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=66AD8CFCE9EFC5F7D5227183F6918D428FCB2AB10ABB87A1EA04834B0B942B5C)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.BAROMETER](#barometer9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | 是 | 要订阅的气压计传感器类型为SENSOR\_TYPE\_ID\_BAROMETER。 |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | 是 | 注册气压计传感器的回调函数，上报的数据类型为BarometerResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_BAROMETER, (data: sensor.BarometerResponse) => {
  console.info('Succeeded in invoking on. Atmospheric pressure: ' + data.pressure);
},
  { interval: 100000000 }
);
```

#### \[h2\]HALL(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback: Callback<HallResponse>, options?: Options): void

监听霍尔传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/0M0T5dZXSHuDZ4_Xs6fKSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2E45E9D515724DE32BE735C512FF485ACCE45579F4706BAAA5180996C36DFE87)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.HALL](#hall9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | 是 | 要订阅的霍尔传感器类型为SENSOR\_TYPE\_ID\_HALL。 |
| callback | Callback<[HallResponse](#hallresponse)\> | 是 | 注册霍尔传感器的回调函数，上报的数据类型为 HallResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，默认值为200000000ns。当霍尔事件被触发的很频繁时，该参数用于限定事件上报的频率。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_HALL, (data: sensor.HallResponse) => {
  console.info('Succeeded in invoking on. Status: ' + data.status);
},
  { interval: 100000000 }
);
```

#### \[h2\]AMBIENT\_LIGHT(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback: Callback<LightResponse>, options?: Options): void

监听环境光传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/P2JCO36wQUqI88kU2Pm2wg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=ABDC138AE303A05B6227EF0E47FFACCC30EE00C438038FD9B4529F9187E2047A)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.AMBIENT\_LIGHT](#ambient_light9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 是 | 要订阅的环境光传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](#lightresponse)\> | 是 | 注册环境光传感器的回调函数，上报的数据类型为LightResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, (data: sensor.LightResponse) => {
  console.info('Succeeded in invoking on. Illumination: ' + data.intensity);
},
  { interval: 100000000 }
);
```

#### \[h2\]ORIENTATION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void

监听方向传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/npkLKGhaTUCfrR4uwUhy9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=8E62EEC3FF5C07AD36845C2E11FEABACF1E7E7700F61BD4255B603FDAE86D43C)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ORIENTATION](#orientation9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | 是 | 要订阅的方向传感器类型为SENSOR\_TYPE\_ID\_ORIENTATION。 |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | 是 | 注册方向传感器的回调函数，上报的数据类型为OrientationResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ORIENTATION, (data: sensor.OrientationResponse) => {
  console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
  console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
  console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
},
  { interval: 100000000 }
);
```

#### \[h2\]HEART\_RATE(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback: Callback<HeartRateResponse>, options?: Options): void

监听心率传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/50giYSuLTZ-CFCDnW5G6FQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=4DBFC9473E422F604D5D55E69A67D1C1FD6E3FD7DA15982A2A73EB7DA9E8C238)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.HEART\_RATE](#heart_rate9)9+代替。

**需要权限**：ohos.permission.HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | 是 | 要订阅的心率传感器类型为SENSOR\_TYPE\_ID\_HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | 是 | 注册心率传感器的回调函数，上报的数据类型为HeartRateResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

#### \[h2\]ROTATION\_VECTOR(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR,callback: Callback<RotationVectorResponse>,options?: Options): void

监听旋转矢量传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/nU005p6oRpqRJzdwqHa4Aw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=E15D1CD3B1477BDE5F104253E9194E649A03216C714BB15ABBDE9FB57A7C411F)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.ROTATION\_VECTOR](#rotation_vector9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 是 | 要订阅的旋转矢量传感器类型为SENSOR\_TYPE\_ID\_ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | 是 | 注册旋转矢量传感器的回调函数，上报的数据类型为RotationVectorResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. Scalar quantity: ' + data.w);
},
  { interval: 100000000 }
);
```

#### \[h2\]WEAR\_DETECTION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback: Callback<WearDetectionResponse>,options?: Options): void

监听所佩戴的检测传感器的数据变化。如果多次调用该接口，仅最后一次调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/bUEtHgr3SlGSx5GfdXd1mQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=A9EB3EFF4409C390C95657FBF204FE815B925230AF000DE1439E67EFB38DAFE2)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.on.WEAR\_DETECTION](#wear_detection9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 是 | 要订阅的佩戴检测传感器类型为SENSOR\_TYPE\_ID\_WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | 是 | 注册佩戴检测传感器的回调函数，上报的数据类型为WearDetectionResponse。 |
| options | [Options](#options) | 否 | 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
  console.info('Succeeded in invoking on. Wear status: ' + data.value);
},
  { interval: 100000000 }
);
```

#### sensor.once(deprecated)

#### \[h2\]ACCELEROMETER(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void

监听加速度传感器的数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/fMEsr6p2TBO2eQ93c86J_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=477E276005DB73A837906952AD2AE974FFF1BC0B4919CFD0835A646F6E3B043F)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ACCELEROMETER](#accelerometer9-1)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | 是 | 加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | 是 | 注册一次加速度传感器的回调函数，上报的数据类型为AccelerometerResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
});
```

#### \[h2\]LINEAR\_ACCELERATION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION,callback:Callback<LinearAccelerometerResponse>): void

监听线性加速度传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Bfa6Acf7S_yjPOsNSr_w7g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=09844A201CE23CD7C599D29712BDA45B2D0A0E475AC79900FFDDF7284AB53809)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.LINEAR\_ACCELEROMETER](#linear_accelerometer9-1)9+代替。

**需要权限**：ohos.permission.ACCELERATION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 是 | 线性加速度传感器类型为SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | 是 | 注册一次线性加速度传感器的回调函数，上报的数据类型为LinearAccelerometerResponse。 |

#### \[h2\]ACCELEROMETER\_UNCALIBRATED(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED,callback: Callback<AccelerometerUncalibratedResponse>): void

监听未校准加速度传感器的数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/A3kB49ikTOylESkbDO65kg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=EBDF74D609858C5D5764A0AD049000AAE007EF66B5D089944E5863C7DED60C92)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ACCELEROMETER\_UNCALIBRATED](#accelerometer_uncalibrated9-1)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 是 | 未校准加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | 是 | 注册一次未校准加速度传感器的回调函数，上报的数据类型为AccelerometerUncalibratedResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
});
```

#### \[h2\]GRAVITY(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback: Callback<GravityResponse>): void

监听重力传感器的数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1dE9uTWHQhOlIgdLNdj6Yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2D5A7E42D4A999934847DFD8A3759BFE1B6870ADAD73F8DC6760F47EE6A1EAB2)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.GRAVITY](#gravity9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | 是 | 重力传感器类型为SENSOR\_TYPE\_ID\_GRAVITY。 |
| callback | Callback<[GravityResponse](#gravityresponse)\> | 是 | 注册一次重力传感器的回调函数，上报的数据类型为GravityResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_GRAVITY, (data: sensor.GravityResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
```

#### \[h2\]GYROSCOPE(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback: Callback<GyroscopeResponse>): void

监听陀螺仪传感器的数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ZVMJj7OtTqud8XBWG_KBPQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=784530F6D94537A8C1137967EBB49DD9E4F437184FDE5731B10F89B8320EF9AA)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.GYROSCOPE](#gyroscope9-1)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | 是 | 陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | 是 | 注册一次陀螺仪传感器的回调函数，上报的数据类型为GyroscopeResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE, (data: sensor.GyroscopeResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
});
```

#### \[h2\]GYROSCOPE\_UNCALIBRATED(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED,callback: Callback<GyroscopeUncalibratedResponse>): void

监听未校准陀螺仪传感器的数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/sXc81GuoQKiqgW63yeLN6g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2B9AD71BA09BF688C8E2FB07A44BD191806976C43D06308AFCFB96C1C6242077)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.GYROSCOPE\_UNCALIBRATED](#gyroscope_uncalibrated9-1)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 是 | 未校准陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | 是 | 注册一次未校准陀螺仪传感器的回调函数，上报的数据类型为GyroscopeUncalibratedResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
});
```

#### \[h2\]SIGNIFICANT\_MOTION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION,callback: Callback<SignificantMotionResponse>): void

监听有效运动传感器的数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/sp_FI-ZbRx-GrnapAxXphw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=E8D96ACF2EC3C08FD16AAB1186BDE7D3A3C0526F1C2A61180286F65168168CCA)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.SIGNIFICANT\_MOTION](#significant_motion9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 是 | 有效运动传感器类型为SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | 是 | 注册一次有效运动传感器的回调函数，上报的数据类型为SignificantMotionResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
  console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
});
```

#### \[h2\]PEDOMETER\_DETECTION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION,callback: Callback<PedometerDetectionResponse>): void

监听计步检测传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Ip2IDs-dSHmhAjb-kFqdQw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=A675B9EDA84BC7234660010D06BD772227301D928C106AFA56BAFDC55483C52D)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.PEDOMETER\_DETECTION](#pedometer_detection9-1)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 是 | 计步检测传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | 是 | 注册一次计步检测传感器的回调函数，上报的数据类型为PedometerDetectionResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
  console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
});
```

#### \[h2\]PEDOMETER(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback: Callback<PedometerResponse>): void

监听计步器传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/WhTOXXkZR0GBYSt671IgYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=9C336C1154DE7FA1726AB3B2D77141D65E3504ABC75765D0F0605C70E048B702)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.PEDOMETER](#pedometer9-1)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | 是 | 计步传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER。 |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | 是 | 注册一次计步传感器的回调函数，上报的数据类型为PedometerResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER, (data: sensor.PedometerResponse) => {
  console.info('Succeeded in invoking once. Steps: ' + data.steps);
});
```

#### \[h2\]AMBIENT\_TEMPERATURE(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE,callback: Callback<AmbientTemperatureResponse>): void

监听环境温度传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/G_OJZIIVQAubcDMJLTxP9w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=CA2DAAFD76422C6D8799197B787D4DC7C0EF8B69AF8AB9971D22A7A4A747952E)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.AMBIENT\_TEMPERATURE](#ambient_temperature9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 是 | 环境温度传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | 是 | 注册一次环境温度传感器的回调函数，上报的数据类型为AmbientTemperatureResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
  console.info('Succeeded in invoking once. Temperature: ' + data.temperature);
});
```

#### \[h2\]MAGNETIC\_FIELD(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>): void

监听磁场传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/EoNxNvipQq2ZjpOlIZfPVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=B9CA5ACB473CB4C598F2F57677ED901AD112D4EAC61C7CDA94191A408958B1D4)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.MAGNETIC\_FIELD](#magnetic_field9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 是 | 磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | 是 | 注册一次磁场传感器的回调函数，上报的数据类型为MagneticFieldResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
});
```

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED,callback: Callback<MagneticFieldUncalibratedResponse>): void

监听未校准磁场传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/5QvT13NRQsO140V7m1udJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=FBC301A325A9F255578E3C70CDCFEAF0FA2FE1A2C05A520DB4160C1547A570FE)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.MAGNETIC\_FIELD\_UNCALIBRATED](#magnetic_field_uncalibrated9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 未校准磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | 是 | 注册一次未校准磁场传感器的回调函数，上报的数据类型为MagneticFieldUncalibratedResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
});
```

#### \[h2\]PROXIMITY(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback: Callback<ProximityResponse>): void

监听接近光传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/NCk5FjqFQrSgO3T13MT0KQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=0C2C073B5DEE4F9E2C2D04877973AF01AB9A8B4E512719A11526A63C255E615B)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.PROXIMITY](#proximity9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | 是 | 接近光传感器类型为SENSOR\_TYPE\_ID\_PROXIMITY。 |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | 是 | 注册一次接近光传感器的回调函数，上报的数据类型为ProximityResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PROXIMITY, (data: sensor.ProximityResponse) => {
  console.info('Succeeded in invoking once. Distance: ' + data.distance);
}
);
```

#### \[h2\]HUMIDITY(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback: Callback<HumidityResponse>): void

监听湿度传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/n2aiiDLvTo2fxHIEkVsisw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=9E6A5A296EDEAC1248407BF2CB74F778F0FF1E6DD7FDFFBEB4D2C35065EB0B88)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.HUMIDITY](#humidity9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | 是 | 湿度传感器类型为SENSOR\_TYPE\_ID\_HUMIDITY。 |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | 是 | 注册一次湿度传感器的回调函数，上报的数据类型为HumidityResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_HUMIDITY, (data: sensor.HumidityResponse) => {
  console.info('Succeeded in invoking once. Humidity: ' + data.humidity);
});
```

#### \[h2\]BAROMETER(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback: Callback<BarometerResponse>): void

监听气压计传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/s70C2PoDS1GDH-Cv0Y_lnA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=D3E62F7BBB9D8492A5F4FFC7BE25674146CD241CEA69E28210D29F9B9D867A06)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.BAROMETER](#barometer9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | 是 | 气压计传感器类型为SENSOR\_TYPE\_ID\_BAROMETER。 |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | 是 | 注册一次气压计传感器的回调函数，上报的数据类型为BarometerResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_BAROMETER, (data: sensor.BarometerResponse) => {
  console.info('Succeeded in invoking once. Atmospheric pressure: ' + data.pressure);
});
```

#### \[h2\]HALL(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback: Callback<HallResponse>): void

监听霍尔传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/v7D7bgAhS_OlEknnxrLsuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=623602900BABABE5C05C24FA68F4CD5881E97D3EF537894CCD9D8F7E3A3D685F)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.HALL](#hall9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | 是 | 霍尔传感器类型为SENSOR\_TYPE\_ID\_HALL。 |
| callback | Callback<[HallResponse](#hallresponse)\> | 是 | 注册一次霍尔传感器的回调函数，上报的数据类型为HallResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_HALL, (data: sensor.HallResponse) => {
  console.info('Succeeded in invoking once. Status: ' + data.status);
});
```

#### \[h2\]AMBIENT\_LIGHT(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback: Callback<LightResponse>): void

监听环境光传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qBoOfrdeQ4aDNpC4S0185Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=E408A7FCD5F0B570BAD723D47BCA785808AAA61507CE8AD02BADA0449A31EEA4)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.AMBIENT\_LIGHT](#ambient_light9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 是 | 环境光传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](#lightresponse)\> | 是 | 注册一次环境光传感器的回调函数，上报的数据类型为LightResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, (data: sensor.LightResponse) => {
  console.info('Succeeded in invoking once. invoking once. Illumination: ' + data.intensity);
});
```

#### \[h2\]ORIENTATION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback: Callback<OrientationResponse>): void

监听方向传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Iuj9ArwMRXORIT02ksMK4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=ACA28DBFA76F040F25AAD959FFEB272A43F3EB7EB94C271230EF1CE322AB115F)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ORIENTATION](#orientation9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | 是 | 方向传感器类型为SENSOR\_TYPE\_ID\_ORIENTATION。 |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | 是 | 注册一次方向传感器的回调函数，上报的数据类型为OrientationResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ORIENTATION, (data: sensor.OrientationResponse) => {
  console.info('Succeeded in invoking the device rotating at an angle around the X axis: ' + data.beta);
  console.info('Succeeded in invoking the device rotating at an angle around the Y axis: ' + data.gamma);
  console.info('Succeeded in invoking the device rotating at an angle around the Z axis: ' + data.alpha);
});
```

#### \[h2\]ROTATION\_VECTOR(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>): void

监听旋转矢量传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/5UXInFVZQcqvQ0b5AogLMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=A970F7023308037E1404837987185DF0F5F5EE9BAE25FC1C07E9C1E44E668FF3)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.ROTATION\_VECTOR](#rotation_vector9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 是 | 旋转矢量传感器类型为SENSOR\_TYPE\_ID\_ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | 是 | 注册一次旋转矢量传感器的回调函数，上报的数据类型为RotationVectorResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, (data: sensor.RotationVectorResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking once. Scalar quantity: ' + data.w);
});
```

#### \[h2\]HEART\_RATE(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback: Callback<HeartRateResponse>): void

监听心率传感器数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/U3o4zhhqRXerOL0eJ4kFJw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=DFA27282ADEB2372F461ED3740F9FDFFB405CEAD3BA2830F1A7FDE1B78D38C86)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.HEART\_RATE](#heart_rate9-1)9+代替。

**需要权限**：ohos.permission.HEART\_RATE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | 是 | 心率传感器类型为SENSOR\_TYPE\_ID\_HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | 是 | 注册一次心率传感器的回调函数，上报的数据类型为HeartRateResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_HEART_RATE, (data: sensor.HeartRateResponse) => {
  console.info("Succeeded in invoking once. Heart rate: " + data.heartRate);
});
```

#### \[h2\]WEAR\_DETECTION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback: Callback<WearDetectionResponse>): void

监听所佩戴的检测传感器的数据变化一次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/3PWDdsIpRmipApe7NfF7zA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=4D6C43ACA6655B86A559A158723DB811F437A89ABBC7E4D5326A3D61C3F23C15)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.once.WEAR\_DETECTION](#wear_detection9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 是 | 佩戴检测传感器类型为SENSOR\_TYPE\_ID\_WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | 是 | 注册一次穿戴检测传感器的回调函数，上报的数据类型为WearDetectionResponse。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, (data: sensor.WearDetectionResponse) => {
  console.info("Succeeded in invoking once. Wear status: " + data.value);
});
```

#### sensor.off(deprecated)

#### \[h2\]ACCELEROMETER(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kP5pa9JmQ--VsGvqAFiuEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=B7AB34D5CF8476718F551CAB1FDB4D2B53114F0EEF88C8E1AFF5E1848E14B212)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ACCELEROMETER9+](#accelerometer9-2)代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | 是 | 要取消订阅的加速度传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER。 |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.AccelerometerResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback);
```

#### \[h2\]ACCELEROMETER\_UNCALIBRATED(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/jn5NoGEjQtqHe4VN8EkyXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2A860830E34FEA955652587AE57A16163A2C0C0B1218BA19AF8BFB9F8F349FEF)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ACCELEROMETER\_UNCALIBRATED](#accelerometer_uncalibrated9-2)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 是 | 要取消订阅的未校准加速度计传感器类型为SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED。 |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.AccelerometerUncalibratedResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking off. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking off. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking off. Z-coordinate bias: ' + data.biasZ);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, callback);
```

#### \[h2\]AMBIENT\_LIGHT(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback?: Callback<LightResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4_3ADa-cTuKDptbQwUjQvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=FDB6B9C90627C66AA9DC6117A6C9F001AE7B13B404F9A071F557C888DE294D9F)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.AMBIENT\_LIGHT](#ambient_light9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 是 | 要取消订阅的环境光传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT。 |
| callback | Callback<[LightResponse](#lightresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.LightResponse) {
  console.info('Succeeded in invoking off. Illumination: ' + data.intensity);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback);
```

#### \[h2\]AMBIENT\_TEMPERATURE(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/wlIFQyRkQceqeAVfmS82DA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2BC3469A61119BD43799DCA5D9B1486E4299FB03202EBF710BA9A843D083742F)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.AMBIENT\_TEMPERATURE](#ambient_temperature9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 是 | 要取消订阅的环境温度传感器类型为SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE。 |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.AmbientTemperatureResponse) {
  console.info('Succeeded in invoking off. Temperature: ' + data.temperature);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback);
```

#### \[h2\]BAROMETER(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback?: Callback<BarometerResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/KFRX3ntARuaS29p6CIhJbg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=EE113E6B9440F7449B2CE60B8C99C7E5A422EDDCBE06AB58FC6D4664F1098326)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.BAROMETER](#barometer9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | 是 | 要取消订阅的气压计传感器类型为SENSOR\_TYPE\_ID\_BAROMETER。 |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.BarometerResponse) {
  console.info('Succeeded in invoking off. Atmospheric pressure: ' + data.pressure);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_BAROMETER, callback);
```

#### \[h2\]GRAVITY(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback?: Callback<GravityResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/PWz6N2EARuS7CZuJ7VuLBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=EAC40A00A6743A6CFAF1ED8AE404D7315273554F5488556FB4F8438E664088D3)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.GRAVITY](#gravity9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | 是 | 要取消订阅的重力传感器类型为SENSOR\_TYPE\_ID\_GRAVITY。 |
| callback | Callback<[GravityResponse](#gravityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GravityResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GRAVITY, callback);
```

#### \[h2\]GYROSCOPE(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback?: Callback<GyroscopeResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/nY9jEIfhQhme-A-aunDulw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=CC3E85259F9FB8A6374021D9E6FDAB2A8F6F7C334D155B1CE42903294932EF74)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.GYROSCOPE](#gyroscope9-2)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | 是 | 要取消订阅的陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE。 |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GyroscopeResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback);
```

#### \[h2\]GYROSCOPE\_UNCALIBRATED(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/6ideA4EtT8uEkax01dgkqg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2EC3CA1A85C139AB48EEB4427E5625F13553BA36C4B6680D6ADA98D1D6711AE1)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.GYROSCOPE\_UNCALIBRATED](#gyroscope_uncalibrated9-2)9+代替。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 是 | 要取消订阅的未校准陀螺仪传感器类型为SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED。 |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GyroscopeUncalibratedResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback);
```

#### \[h2\]HALL(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback?: Callback<HallResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/b5nW9hq6QeCPCCHxQq-SLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=11AFDF831B8547341A4655BE0DCFF8EE4AE0B4CD8A087273F82F68C02731A3FF)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.HALL](#hall9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | 是 | 要取消订阅的霍尔传感器类型为SENSOR\_TYPE\_ID\_HALL。 |
| callback | Callback<[HallResponse](#hallresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HallResponse) {
  console.info('Succeeded in invoking off. Status: ' + data.status);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HALL, callback);
```

#### \[h2\]HEART\_RATE(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback?: Callback<HeartRateResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/vRJUY7KaQlyv91DAUm3uxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=EF1B8DF9CE71EAC236D96F068FA6B887747B10094EC9D6CC55C3882CB471DB6D)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.HEART\_RATE](#heart_rate9-2)9+代替。

**需要权限**：ohos.permission.HEALTH\_DATA

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | 是 | 要取消订阅的心率传感器类型为SENSOR\_TYPE\_ID\_HEART\_RATE。 |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HeartRateResponse) {
  console.info('Succeeded in invoking off. Heart rate: ' + data.heartRate);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HEART_RATE, callback);
```

#### \[h2\]HUMIDITY(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback?: Callback<HumidityResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/xwSTLwpwQ1ujMnobI47p9w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=167C92F184EFE61B8AA15A78DCDC911D1E9B48C432783D4355C8F2C12F5AA9D2)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.HUMIDITY](#humidity9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | 是 | 要取消订阅的湿度传感器类型为SENSOR\_TYPE\_ID\_HUMIDITY。 |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HumidityResponse) {
  console.info('Succeeded in invoking off. Humidity: ' + data.humidity);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HUMIDITY, callback);
```

#### \[h2\]LINEAR\_ACCELERATION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION, callback?: Callback<LinearAccelerometerResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/_5g4IK-xQzWQiMaVQLEHRg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=C59A44848F0BF63EC510ED7FF6190573B1603E11B01B79877A18C3D9E5976114)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.LINEAR\_ACCELEROMETER](#linear_accelerometer9-2)9+代替。

**需要权限**：ohos.permission.ACCELEROMETER

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 是 | 要取消订阅的线性加速度传感器类型为SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION。 |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.LinearAccelerometerResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback);
```

#### \[h2\]MAGNETIC\_FIELD(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback?: Callback<MagneticFieldResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/k43xSGwXRL67OqdavKrSPA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=617DA33FC9D41F0BAD8AE1276B32E78B43D72A107B5A1C881671E45EDB94AFFF)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.MAGNETIC\_FIELD](#magnetic_field9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 是 | 要取消订阅的磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD。 |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.MagneticFieldResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback);
```

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/pBEPEDTlTNWB6UuOQguJ3Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=1DA2B5428729C96BEDA8BBF95D8FE5FE5C0DD63F46D629C4FF38242B547DAF86)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.MAGNETIC\_FIELD\_UNCALIBRATED](#magnetic_field_uncalibrated9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 是 | 要取消订阅的未校准磁场传感器类型为SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED。 |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.MagneticFieldUncalibratedResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking off. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking off. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking off. Z-coordinate bias: ' + data.biasZ);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, callback);
```

#### \[h2\]ORIENTATION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback?: Callback<OrientationResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/q_U81_FxTROlWHMVKOsGFA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=22AF8AF517B10C841CFA4B200046BE449DA3CFF49BE8ADB3121CCFB205011E7C)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ORIENTATION](#orientation9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | 是 | 要取消订阅的方向传感器类型为SENSOR\_TYPE\_ID\_ORIENTATION。 |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.OrientationResponse) {
  console.info('Succeeded in invoking off. The device rotates at an angle around the X axis: ' + data.beta);
  console.info('Succeeded in invoking off. The device rotates at an angle around the Y axis: ' + data.gamma);
  console.info('Succeeded in invoking off. The device rotates at an angle around the Z axis: ' + data.alpha);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ORIENTATION, callback);
```

#### \[h2\]PEDOMETER(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback?: Callback<PedometerResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/v-IzkGchTD-vseBWrNflew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=E602C9CE8D740353911D796533D71DDCC7771A8CBE4407E33D95FE75D4C2C4B5)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.PEDOMETER](#pedometer9-2)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | 是 | 要取消订阅的计步传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER。 |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.PedometerResponse) {
  console.info('Succeeded in invoking off. Steps: ' + data.steps);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER, callback);
```

#### \[h2\]PEDOMETER\_DETECTION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, callback?: Callback<PedometerDetectionResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/EtqnE_pATY6iUf0rDuxw_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=BC3EC7F1FE1311E3605F037DBBCD88DCF56086619C816DB3FA94D462E1225C53)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.PEDOMETER\_DETECTION](#pedometer_detection9-2)9+代替。

**需要权限**：ohos.permission.ACTIVITY\_MOTION

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 是 | 要取消订阅的计步检测传感器类型为SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION。 |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.PedometerDetectionResponse) {
  console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback);
```

#### \[h2\]PROXIMITY(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback?: Callback<ProximityResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/TsQ6XrMXSAy8_Vpt5DmksQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=5648EEDFDCF6BCC0B69BC9C161F01FC7D64D1C5A3C13665E2A423CBAB0892053)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.PROXIMITY](#proximity9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | 是 | 要取消订阅的接近光传感器类型为SENSOR\_TYPE\_ID\_PROXIMITY。 |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.ProximityResponse) {
  console.info('Succeeded in invoking off. Distance: ' + data.distance);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PROXIMITY, callback);
```

#### \[h2\]ROTATION\_VECTOR(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, callback?: Callback<RotationVectorResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/jX3dQBKASjK7e3iSKRxxiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=B680ECE11C104E425F2EDC3236F31346968AB58A5C78FA4F325AF93A6EAD18B6)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.ROTATION\_VECTOR](#rotation_vector9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 是 | 要取消订阅的旋转矢量传感器类型为SENSOR\_TYPE\_ID\_ROTATION\_VECTOR。 |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.RotationVectorResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking off. Scalar quantity: ' + data.w);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, callback);
```

#### \[h2\]SIGNIFICANT\_MOTION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, callback?: Callback<SignificantMotionResponse>): void

取消订阅有效运动传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/TohTortDTIyJPCr45yBGlQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=D83655A5F84B99E6CE14DE71AFAC0754186B746F81E79864D917CC3DAAC18A47)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.SIGNIFICANT\_MOTION](#significant_motion9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 是 | 要取消订阅的有效运动传感器类型为SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION。 |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.SignificantMotionResponse) {
  console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback);
```

#### \[h2\]WEAR\_DETECTION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback?: Callback<WearDetectionResponse>): void

取消订阅传感器数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/wyL5ZDD0R-Gnaat7V8NDdg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=B46CF70C1560602ED7F81D6979D2A9C5763326AE5BE5E64F63CF2DD8D321D21C)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.off.WEAR\_DETECTION](#wear_detection9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 是 | 要取消订阅的佩戴检测传感器类型为SENSOR\_TYPE\_ID\_WEAR\_DETECTION。 |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | 否 | 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';

function accCallback(data: sensor.WearDetectionResponse) {
  console.info('Succeeded in invoking off. Wear status: ' + data.value);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, accCallback);
```

#### sensor.transformCoordinateSystem(deprecated)

transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void

旋转提供的旋转矩阵，使其可以以不同的方式表示坐标系，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/wQhV1pj9TVWwcrohRnRQ6g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=E27BFF5ED338494ECF67769B9566AFACCB7708805C04A92BB10167D315C79C51)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.transformRotationMatrix](#sensortransformrotationmatrix9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | 是 | 表示旋转矩阵。 |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | 是 | 表示坐标系方向。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回转换后的旋转矩阵。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.transformCoordinateSystem([1, 0, 0, 0, 1, 0, 0, 0, 1], { x: 2, y: 3 },
                                 (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info("Succeeded in starting Operation. Data obtained: " + data);
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting transformCoordinateSystem data[ " + i + "] = " + data[i]);
  }
})
```

#### sensor.transformCoordinateSystem(deprecated)

transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>

旋转提供的旋转矩阵，使其可以以不同的方式表示坐标系，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/huHBPHG9TYygCpgHGm9iMQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=9C6CB233434780BDE790541B493931C79D59E31F11F30D50120093C4CAC66E3D)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.transformRotationMatrix](#sensortransformrotationmatrix9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | 是 | 表示旋转矩阵。 |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | 是 | 表示坐标系方向。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | 使用异步方式返回转换后的旋转矩阵。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.transformCoordinateSystem([1, 0, 0, 0, 1, 0, 0, 0, 1], { x: 2, y: 3 });
promise.then((data: Array<number>) => {
  console.info("Succeeded in starting Operation");
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting transformCoordinateSystem data[ " + i + "] = " + data[i]);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to operate.`);
})
```

#### sensor.getGeomagneticField(deprecated)

getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void

获取地球上特定位置的地磁场，使用callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/IasVG4fQTKCWgbaqAprCHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=8A3294489A677093C029CB531714BE7DD5C76C1C643F8C7501B8455A1D49F2C0)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getGeomagneticInfo](#sensorgetgeomagneticinfo9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | 是 | 地理位置。 |
| timeMillis | number | 是 | 表示获取磁偏角的时间，单位为毫秒。 |
| callback | AsyncCallback<[GeomagneticResponse](#geomagneticresponse)\> | 是 | 异步返回磁场信息。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000,
                           (err: BusinessError, data: sensor.GeomagneticResponse) => {
  if (err) {
    console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting sensor_getGeomagneticField_callback x: ' + data.x + ',y: ' + data.y + ',z: ' +
  data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
  ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
});
```

#### sensor.getGeomagneticField(deprecated)

getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>

获取地球上特定位置的地磁场，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ZFvNjhsKSii5_EhTRUIRNA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=9C34300B307545661D3CB2D643114C3E1E3B9FBA98245A1FCED74A38198A66C2)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getGeomagneticInfo](#sensorgetgeomagneticinfo9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | 是 | 地理位置。 |
| timeMillis | number | 是 | 表示获取磁偏角的时间，单位为毫秒。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[GeomagneticResponse](#geomagneticresponse)\> | 使用异步方式返回磁场信息。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
promise.then((data: sensor.GeomagneticResponse) => {
  console.info('Succeeded in getting sensor_getGeomagneticField_promise x: ' + data.x + ',y: ' + data.y + ',z: ' +
  data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
  ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
}).catch((reason: BusinessError) => {
  console.error(`Failed to operate.`);
})
```

#### sensor.getAltitude(deprecated)

getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void

根据气压值获取设备所在的海拔高度，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/lIbiDCQNR8G7iJMXlw4Y3g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=04A7CD1330627403B014D48BE9B40FB753B5A37B8C17C1EAA1675B5565C581C1)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getDeviceAltitude](#sensorgetdevicealtitude9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| seaPressure | number | 是 | 表示海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 表示设备所在高度的气压值，单位为hPa。 |
| callback | AsyncCallback<number> | 是 | 异步返回设备所在的海拔高度，单位为米。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getAltitude(0, 200, (err: BusinessError, data: number) => {
  if (err) {
    console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info("Succeeded in getting getAltitude interface get data: " + data);
});
```

#### sensor.getAltitude(deprecated)

getAltitude(seaPressure: number, currentPressure: number): Promise<number>

根据气压值获取设备所在的海拔高度，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/cwNq0tFIQGCxOvVQ6x1-bA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=C6D4F850E9839AF72FA038256161C59D6637BD64409B50290D4077922D367A7D)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getDeviceAltitude](#sensorgetdevicealtitude9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| seaPressure | number | 是 | 表示海平面气压值，单位为hPa。 |
| currentPressure | number | 是 | 表示设备所在高度的气压值，单位为hPa。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 使用异步方式返回设备所在的海拔高度（单位：米）。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getAltitude(0, 200);
promise.then((data: number) => {
  console.info('Succeeded in getting sensor_getAltitude_Promise success', data);
}).catch((err: BusinessError) => {
  console.error(`Failed to operate.`);
})
```

#### sensor.getGeomagneticDip(deprecated)

getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void

根据倾斜矩阵计算地磁倾斜角，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/uNQRPB8MSpmiphtr9JNuQA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2C3AE95BDB513689C21A1C08A74892E435E9AF53F5D5CCF85C1A12DCBADC0493)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getInclination](#sensorgetinclination9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | 是 | 表示倾斜矩阵。 |
| callback | AsyncCallback<number> | 是 | 异步返回地磁倾斜角，单位为弧度。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getGeomagneticDip([1, 0, 0, 0, 1, 0, 0, 0, 1], (err: BusinessError, data: number) => {
  if (err) {
    console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info("Succeeded in getting getGeomagneticDip interface get data: " + data);
})
```

#### sensor.getGeomagneticDip(deprecated)

getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>

根据倾斜矩阵计算地磁倾斜角，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/2PhqiDFFTSyenM3K8_jFVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=5C9061274C890A22F9A73F0D7188213D888B6BC8E1F866D6E7D24A6C920E5F96)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getInclination](#sensorgetinclination9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | 是 | 表示倾斜矩阵。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 使用异步方式返回地磁倾斜角，单位为弧度。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getGeomagneticDip([1, 0, 0, 0, 1, 0, 0, 0, 1]);
promise.then((data: number) => {
  console.info('Succeeded in get GeomagneticDip_promise', data);
}).catch((err: BusinessError) => {
  console.error(`Failed to operate.`);
})
```

#### sensor. getAngleModify(deprecated)

getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

获取两个旋转矩阵之间的角度变化，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/yqPekaSXQW2BiTmgfICHHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=45B0B2B17FF859FA5A927FB0F22BFC38C42183E62A0B93A3C70826363BB912FE)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getAngleVariation](#sensorgetanglevariation9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | 是 | 表示当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回z、x、y轴方向的旋转角度变化，单位度（°）。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getAngleModify([1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0.87, -0.50, 0, 0.50, 0.87],
                      (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info("data[" + i + "]: " + data[i]);
  }
})
```

#### sensor. getAngleModify(deprecated)

getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>

获取两个旋转矩阵之间的角度变化，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/hnQMfKr0QPeB1RMxRCio9A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=A86AA6AF6F6C8F41DCB7727D15C45BF503E41C6FC67763EED4FC94F075801096)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getAngleVariation](#sensorgetanglevariation9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | 是 | 表示当前旋转矩阵。 |
| preRotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | 使用异步方式返回z、x、y轴方向的旋转角度变化，单位度（°）。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getAngleModify([1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0.87, -0.50, 0, 0.50, 0.87]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting AngleModify_promise.');
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting data[" + i + "]: " + data[i]);
  }
}).catch((reason: BusinessError) => {
  let e: BusinessError = reason as BusinessError;
  console.info("Succeeded in getting promise::catch", e);
})
```

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

将旋转矢量转换为旋转矩阵，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/PxwfAjqxRweHX7rC7pGTlg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=2BDCFD5609E1BD90EE2B528336C60ED359473769098E1326FD111D0111E66D7C)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](#sensorgetrotationmatrix9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回旋转矩阵。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.createRotationMatrix([0.20046076, 0.21907, 0.73978853, 0.60376877],
                            (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting data[" + i + "]: " + data[i]);
  }
})
```

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>

将旋转矢量转换为旋转矩阵，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/NaXiucvsTFCNG_gpDMYj1Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=A9708999E8ECBC07D3FBCEE81C570CB7EC0816067A82E2D299FE9B4E8E75F7AF)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](#sensorgetrotationmatrix9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | 使用异步方式返回旋转矩阵。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.createRotationMatrix([0.20046076, 0.21907, 0.73978853, 0.60376877]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting createRotationMatrix_promise');
  for (let i = 0; i < data.length; i++) {
    console.info("data[" + i + "]: " + data[i]);
  }
}).catch((reason: BusinessError) => {
  console.info("Succeeded in getting promise::catch", reason);
})
```

#### sensor.createQuaternion(deprecated)

createQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

将旋转矢量转换为四元数，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/CtcEgM7DSye8hom4Vq9-Xg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=663CB80B08BC9B253593B2841C6B26E6463542399B99E47A9A42283C2C76A208)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getQuaternion](#sensorgetquaternion9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回四元数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.createQuaternion([0.20046076, 0.21907, 0.73978853, 0.60376877],
                        (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting data[" + i + "]: " + data[i]);
  }
})
```

#### sensor.createQuaternion(deprecated)

createQuaternion(rotationVector: Array<number>): Promise<Array<number>>

将旋转矢量转换为四元数，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/z3If4C-BTp6x3EYYoXue_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=F3ECCC51D1A0F1FAC347959AE846DD0E3D43D26590C662FB00819AFD43B6082F)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getQuaternion](#sensorgetquaternion9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | 是 | 表示旋转矢量。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | 使用异步方式返回四元数。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.createQuaternion([0.20046076, 0.21907, 0.73978853, 0.60376877]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting createQuaternion_promise');
  for (let i = 0; i < data.length; i++) {
    console.info("data[" + i + "]: " + data[i]);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to get promise.`);
})
```

#### sensor.getDirection(deprecated)

getDirection(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

根据旋转矩阵计算设备的方向，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/tKr20HjmRPG2-xrGbQdJlg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=F8D4BBAD85BDE837CAE4F5D0496E6E954C331EE6CD8010D31F688FAE71966C37)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getOrientation](#sensorgetorientation9)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |
| callback | AsyncCallback<Array<number>> | 是 | 异步返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getDirection([1, 0, 0, 0, 1, 0, 0, 0, 1], (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info("Succeeded in getting getDirection interface get data: " + data);
  for (let i = 1; i < data.length; i++) {
    console.info("Succeeded in getting sensor_getDirection_callback" + data[i]);
  }
})
```

#### sensor.getDirection(deprecated)

getDirection(rotationMatrix: Array<number>): Promise<Array<number>>

根据旋转矩阵计算设备的方向，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/4nf6MbdYQkyS2qaOEESb_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=4D193C87BAAA77A5E28A8826AA0D1233877692B584A8A4FE9F6077E80A7E920D)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getOrientation](#sensorgetorientation9-1)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | 是 | 表示旋转矩阵。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<number>> | 使用异步方式返回围绕z、x、y轴方向的旋转角度，单位度（°）。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getDirection([1, 0, 0, 0, 1, 0, 0, 0, 1]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting sensor_getAltitude_Promise', data);
  for (let i = 1; i < data.length; i++) {
    console.info("Succeeded in getting sensor_getDirection_promise" + data[i]);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to get promise.`);
})
```

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void

根据重力矢量和地磁矢量计算旋转矩阵，使用Callback异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/d7qGAkYZT_CTDnTMUe_XOA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=9F3C10C76B29389B1C94A764EF58CA898A8687F033972075AC9428B405BEAF35)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](#sensorgetrotationmatrix9-2)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | 是 | 表示重力向量。 |
| geomagnetic | Array<number> | 是 | 表示地磁矢量。 |
| callback | AsyncCallback<[RotationMatrixResponse](#rotationmatrixresponse)\> | 是 | 异步返回旋转矩阵。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.createRotationMatrix([-0.27775216, 0.5351276, 9.788099], [210.87253, -78.6096, -111.44444],
                            (err: BusinessError, data: sensor.RotationMatrixResponse) => {
  if (err) {
    console.error(`Failed to get create rotationMatrix. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(JSON.stringify(data));
})
```

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>

根据重力矢量和地磁矢量计算旋转矩阵，使用Promise异步方式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/PbTadEQZS9Sv8bUV9wLZTg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=DB8C433C85A02D3C41A8EB302D37765DE4A29530C3C0B12E79D109F2A03F299B)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[sensor.getRotationMatrix](#sensorgetrotationmatrix9-3)9+代替。

**系统能力**：SystemCapability.Sensors.Sensor

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | 是 | 表示重力向量。 |
| geomagnetic | Array<number> | 是 | 表示地磁矢量。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RotationMatrixResponse](#rotationmatrixresponse)\> | 使用异步方式返回旋转矩阵。 |

**示例**：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.createRotationMatrix([-0.27775216, 0.5351276, 9.788099], [210.87253, -78.6096, -111.44444]);
promise.then((data: sensor.RotationMatrixResponse) => {
  console.info(JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to get promise.`);
})
```

#### SensorType(deprecated)

表示要订阅或取消订阅的传感器类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/6B-ZdhFlRGGZkDtEkkvvXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=FAB5179F6F700D674C405987F0BF8A682A93812CA6A00A713B3D3E75839ADB1B)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[SensorId](#sensorid9)代替。

**系统能力**：SystemCapability.Sensors.Sensor

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SENSOR\_TYPE\_ID\_ACCELEROMETER | 1 | 加速度传感器。 |
| SENSOR\_TYPE\_ID\_GYROSCOPE | 2 | 陀螺仪传感器。 |
| SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 5 | 环境光传感器。 |
| SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 6 | 磁场传感器。 |
| SENSOR\_TYPE\_ID\_BAROMETER | 8 | 气压计传感器。 |
| SENSOR\_TYPE\_ID\_HALL | 10 | 霍尔传感器。 |
| SENSOR\_TYPE\_ID\_PROXIMITY | 12 | 接近光传感器。 |
| SENSOR\_TYPE\_ID\_HUMIDITY | 13 | 湿度传感器。 |
| SENSOR\_TYPE\_ID\_ORIENTATION | 256 | 方向传感器。 |
| SENSOR\_TYPE\_ID\_GRAVITY | 257 | 重力传感器。 |
| SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 258 | 线性加速度传感器。 |
| SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 259 | 旋转矢量传感器。 |
| SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 260 | 环境温度传感器。 |
| SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 261 | 未校准磁场传感器。 |
| SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 263 | 未校准陀螺仪传感器。 |
| SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 264 | 有效运动传感器。 |
| SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 265 | 计步检测传感器。 |
| SENSOR\_TYPE\_ID\_PEDOMETER | 266 | 计步传感器。 |
| SENSOR\_TYPE\_ID\_HEART\_RATE | 278 | 心率传感器。 |
| SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 280 | 佩戴检测传感器。 |
| SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 281 | 未校准加速度计传感器。 |
