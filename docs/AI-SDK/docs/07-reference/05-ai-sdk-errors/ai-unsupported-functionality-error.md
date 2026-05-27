---
title: AI_UnsupportedFunctionalityError
description: Learn how to fix AI_UnsupportedFunctionalityError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-unsupported-functionality-error.mdx"
---

# AI_UnsupportedFunctionalityError

This error occurs when functionality is not supported.

## Properties

- `functionality`: The name of the unsupported functionality
- `message`: The error message (optional, auto-generated from `functionality`)

## Checking for this Error

You can check if an error is an instance of `AI_UnsupportedFunctionalityError` using:

```typescript
import { UnsupportedFunctionalityError } from 'ai';

if (UnsupportedFunctionalityError.isInstance(error)) {
  // Handle the error
}
```
