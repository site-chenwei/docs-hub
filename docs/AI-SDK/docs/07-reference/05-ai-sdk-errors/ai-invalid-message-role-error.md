---
title: AI_InvalidMessageRoleError
description: Learn how to fix AI_InvalidMessageRoleError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-invalid-message-role-error.mdx"
---

# AI_InvalidMessageRoleError

This error occurs when an invalid message role is provided.

## Properties

- `role`: The invalid role value
- `message`: The error message (optional, auto-generated from `role`)

## Checking for this Error

You can check if an error is an instance of `AI_InvalidMessageRoleError` using:

```typescript
import { InvalidMessageRoleError } from 'ai';

if (InvalidMessageRoleError.isInstance(error)) {
  // Handle the error
}
```
