---
title: AI_MessageConversionError
description: Learn how to fix AI_MessageConversionError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-message-conversion-error.mdx"
---

# AI_MessageConversionError

This error occurs when message conversion fails.

## Properties

- `originalMessage`: The original message that failed conversion
- `message`: The error message

## Checking for this Error

You can check if an error is an instance of `AI_MessageConversionError` using:

```typescript
import { MessageConversionError } from 'ai';

if (MessageConversionError.isInstance(error)) {
  // Handle the error
}
```
