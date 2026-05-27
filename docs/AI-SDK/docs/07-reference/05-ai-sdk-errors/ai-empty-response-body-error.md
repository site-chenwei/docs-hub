---
title: AI_EmptyResponseBodyError
description: Learn how to fix AI_EmptyResponseBodyError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-empty-response-body-error.mdx"
---

# AI_EmptyResponseBodyError

This error occurs when the server returns an empty response body.

## Properties

- `message`: The error message

## Checking for this Error

You can check if an error is an instance of `AI_EmptyResponseBodyError` using:

```typescript
import { EmptyResponseBodyError } from 'ai';

if (EmptyResponseBodyError.isInstance(error)) {
  // Handle the error
}
```
