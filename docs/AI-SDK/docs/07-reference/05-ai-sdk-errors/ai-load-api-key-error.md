---
title: AI_LoadAPIKeyError
description: Learn how to fix AI_LoadAPIKeyError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-load-api-key-error.mdx"
---

# AI_LoadAPIKeyError

This error occurs when API key is not loaded successfully.

## Properties

- `message`: The error message

## Checking for this Error

You can check if an error is an instance of `AI_LoadAPIKeyError` using:

```typescript
import { LoadAPIKeyError } from 'ai';

if (LoadAPIKeyError.isInstance(error)) {
  // Handle the error
}
```
