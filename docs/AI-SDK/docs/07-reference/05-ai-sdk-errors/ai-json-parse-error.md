---
title: AI_JSONParseError
description: Learn how to fix AI_JSONParseError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-json-parse-error.mdx"
---

# AI_JSONParseError

This error occurs when JSON fails to parse.

## Properties

- `text`: The text value that could not be parsed
- `cause`: The underlying parsing error (required in constructor)

## Checking for this Error

You can check if an error is an instance of `AI_JSONParseError` using:

```typescript
import { JSONParseError } from 'ai';

if (JSONParseError.isInstance(error)) {
  // Handle the error
}
```
