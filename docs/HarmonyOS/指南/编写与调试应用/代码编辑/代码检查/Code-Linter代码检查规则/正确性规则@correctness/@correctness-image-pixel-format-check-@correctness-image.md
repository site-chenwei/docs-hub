---
title: "@correctness/image"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-pixel-format-check"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "正确性规则@correctness"
  - "@correctness/image-pixel-format-check"
captured_at: "2026-04-17T01:36:48.336Z"
---

# @correctness/image-pixel-format-check

在使用Image组件[createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8)接口时，建议不要选择RGB\_565档位，避免出现色阶问题。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@correctness/image-pixel-format-check": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

import image from '@ohos.multimedia.image';
const DEFAULT\_IMAGE\_WIDTH\_HEIGHT: number = 600;
const DEFAULT\_IMAGE\_BUFFER\_SIZE: number = DEFAULT\_IMAGE\_WIDTH\_HEIGHT \* DEFAULT\_IMAGE\_WIDTH\_HEIGHT \* 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT\_IMAGE\_BUFFER\_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA\_8888,
      size: { height: DEFAULT\_IMAGE\_WIDTH\_HEIGHT, width: DEFAULT\_IMAGE\_WIDTH\_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT\_IMAGE\_BUFFER\_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA\_8888,
      size: { height: DEFAULT\_IMAGE\_WIDTH\_HEIGHT, width: DEFAULT\_IMAGE\_WIDTH\_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width \* height \* 4);
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGBA\_8888,
      size: { height: height, width: width }
    })
  }
  
}

#### 反例

import image from '@ohos.multimedia.image';
const DEFAULT\_IMAGE\_WIDTH\_HEIGHT: number = 600;
const DEFAULT\_IMAGE\_BUFFER\_SIZE: number = DEFAULT\_IMAGE\_WIDTH\_HEIGHT \* DEFAULT\_IMAGE\_WIDTH\_HEIGHT \* 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT\_IMAGE\_BUFFER\_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB\_565,
      size: { height: DEFAULT\_IMAGE\_WIDTH\_HEIGHT, width: DEFAULT\_IMAGE\_WIDTH\_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT\_IMAGE\_BUFFER\_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB\_565,
      size: { height: DEFAULT\_IMAGE\_WIDTH\_HEIGHT, width: DEFAULT\_IMAGE\_WIDTH\_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width \* height \* 4);
    // warning
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGB\_565,
      size: { height: height, width: width }
    })
  }
}

#### 规则集

plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
