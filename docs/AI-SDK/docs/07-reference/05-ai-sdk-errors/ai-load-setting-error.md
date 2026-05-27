---
title: AI_LoadSettingError
description: Learn how to fix AI_LoadSettingError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-load-setting-error.mdx"
---

# AI_LoadSettingError

This error occurs when a setting is not loaded successfully.

## Properties

- `message`: The error message

## Checking for this Error

You can check if an error is an instance of `AI_LoadSettingError` using:

```typescript
import { LoadSettingError } from 'ai';

if (LoadSettingError.isInstance(error)) {
  // Handle the error
}
```
