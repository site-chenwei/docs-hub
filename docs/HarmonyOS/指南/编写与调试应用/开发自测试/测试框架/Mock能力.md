---
title: "Mock能力"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-test-mock"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "开发自测试"
  - "测试框架"
  - "Mock能力"
captured_at: "2026-04-17T01:36:50.042Z"
---

# Mock能力

在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用Mock能力，对这些接口或对象进行模拟。当前Instrument Test和Local Test均支持对模块进行Mock，对于调用系统模块API或外部依赖模块，使用import mock，对于本地模块，使用hamock/hypium插件包的mock接口或者import mock。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/QBKdLnnZQ8iAD8yvVM47pg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=2DA82794AEB0AD1557E4298C8F713BB79B8ACE313FD45B6CC40DCE13B9BDCC1E)

仅API 11及以上版本的Stage模型工程支持。

#### 系统模块/依赖模块Mock

通过import mock对系统模块API或依赖模块的方法进行Mock，在mock-config.json5配置文件中定义目标模块和Mock实现代码文件的映射关系，运行时import目标模块都将指向Mock实现代码。以系统API bluetoothManager为例，具体实现如下。

1.  在src/mock目录下新建一个ArkTS文件，例如bluetooth\_manager.mock.ets，在这个文件内定义目标模块的Mock实现。
    
    // src/mock/bluetooth\_manager.mock.ets
    enum BluetoothState {
      /\*\* Indicates the local Bluetooth is off \*/
      STATE\_OFF = 0,
      /\*\* Indicates the local Bluetooth is turning on \*/
      STATE\_TURNING\_ON = 1,
      /\*\* Indicates the local Bluetooth is on, and ready for use \*/
      STATE\_ON = 2,
      /\*\* Indicates the local Bluetooth is turning off \*/
      STATE\_TURNING\_OFF = 3,
      /\*\* Indicates the local Bluetooth is turning LE mode on \*/
      STATE\_BLE\_TURNING\_ON = 4,
      /\*\* Indicates the local Bluetooth is in LE only mode \*/
      STATE\_BLE\_ON = 5,
      /\*\* Indicates the local Bluetooth is turning off LE only mode \*/
      STATE\_BLE\_TURNING\_OFF = 6
    }
    interface BluetoothInfo {
      state: number
    }
    const MockBluetoothManager: Record<string, Object> = {
      'getBluetoothInfo': () => {
        return { state : BluetoothState.STATE\_BLE\_TURNING\_ON } as BluetoothInfo;
      },
    };
    export default MockBluetoothManager;
    
2.  在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的映射关系。
    
    "@ohos.enterprise.bluetoothManager": {  // 待替换的模块名
      "source": "src/mock/bluetooth\_manager.mock.ets"  // Mock代码的路径，相对于模块根目录
    }
    
3.  在测试文件中编写如下代码。
    
    // bluetoothManager.test.ets
    import { describe, it, expect } from '@ohos/hypium';
    import { bluetoothManager } from '@kit.MDMKit';
    
    export default function mock\_system\_api() {   
      describe('mock\_system\_api', () => {
        /\* mock系统API \*/
        it('mock\_system\_api', 0, () => {
          let bluetoothInfo = bluetoothManager.getBluetoothInfo({
            bundleName: "com.example.myapplication"
          })
          expect(bluetoothInfo.state).assertEqual(4)
        });
      });
    }
    
4.  如果测试文件是手动创建的，需要将用例类mock\_system\_api添加到List.test.ets文件中。
    
    import mock\_system\_api from './bluetoothManager.test';
    
    export default function testsuite() {
      mock\_system\_api();
    }
    
5.  执行测试，用例通过。

#### 本地模块Mock

有两种方式可以对本地模块进行Mock，一是使用hamock/hypium插件包的mock接口，二是使用import mock。

#### \[h2\]使用hamock/hypium插件包的mock接口

以下例子通过mock接口模拟本地模块的某个方法，关于Mock的更多说明可以参考[mock能力](https://gitcode.com/openharmony/testfwk_arkxtest#mock能力)。

1.  在src/main/ets目录下新建一个ArkTS文件，例如ClassForMock.ets，并在其中导出一个类。
    
    export class ClassForMock {
      constructor() {
      }
      method\_1(arg: string) {
        return '888888';
      }
      method\_2(arg: string) {
        return '999999';
      }
    }
    
2.  在测试文件中编写如下代码。
    
    // afterReturnTest.test.ets
    import { describe, expect, it, MockKit, when } from '@ohos/hypium';
    import { ClassForMock } from '../../../main/ets/ClassForMock';
    
    export default function afterReturnTest() {
      describe('afterReturnTest', () => {
        it('afterReturnTest', 0, () => {
          console.info("it begin");
          // 1.创建一个mock能力的对象MockKit
          let mocker: MockKit = new MockKit();
          // 2.定义类ClassForMock，里面两个函数，然后创建一个对象classForMock
          let classForMock: ClassForMock = new ClassForMock();
          // 3.进行mock操作,比如需要对ClassForMock类的method\_1函数进行mock
          let mockFunc: Function = mocker.mockFunc(classForMock, classForMock.method\_1);
          // 4.期望classForMock.method\_1函数被mock后, 以'test'为入参时调用函数返回结果'1'
          when(mockFunc)('test').afterReturn('1');
          // 5.对mock后的函数进行断言，看是否符合预期
          // 执行成功案例，参数为'test'
          expect(classForMock.method\_1('test')).assertEqual('1'); // 执行通过
        })
      })
    }
    
3.  如果测试文件是手动创建的，需要将用例类afterReturnTest添加到List.test.ets文件中。
    
    import afterReturnTest from './afterReturnTest.test';
    
    export default function testsuite() {
      afterReturnTest();
    }
    
4.  执行测试，用例通过。

#### \[h2\]使用import mock

使用import mock对本地模块进行Mock，操作步骤和系统模块/依赖模块的Mock类似，在mock-config.json5配置文件中定义目标模块和Mock实现代码文件的映射关系，运行时import目标模块都将指向Mock实现代码。以下例子对本地模块entry/src/main/ets/common/calc.ets中的sum函数进行Mock。

1.  在src/mock目录下新建一个common目录并创建一个ArkTS文件，例如calc.mock.ets，在这个文件内定义目标模块的Mock实现。
    
    // src/mock/common/calc.mock.ets
    export function sum() {
      return "this is mock sum";
    }
    
    calc.ets的原始实现如下：
    
    // src/main/ets/common/calc.ets
    export function sum() {
      return 1;
    }
    
2.  在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的映射关系。
    
    {
      "common/calc.ets": { // 本地模块只支持ets/xxx的相对路径，并需明确文件后缀
        "source": "src/mock/common/calc.mock.ets"  // Mock代码的路径，相对于模块根目录
      },
    }
    
3.  在测试文件中编写如下代码。
    
    // test\_mock\_local\_method.test.ets
    import { describe, it, expect } from '@ohos/hypium'
    import { sum } from '../../../main/ets/common/calc';
    
    export default function test\_mock\_local\_method() {
      describe('test\_mock\_local\_method', () \=\> {
        it("test\_mock\_local\_method", 0, () \=\> {
          expect(sum()).assertEqual("this is mock sum")
        })
      })
    }
    
4.  如果测试文件是手动创建的，需要将用例类test\_mock\_local\_method添加到List.test.ets文件中。
    
    import test\_mock\_local\_method from './test\_mock\_local\_method.test';
    
    export default function testsuite() {
      test\_mock\_local\_method();
    }
    
5.  执行测试，用例通过。
