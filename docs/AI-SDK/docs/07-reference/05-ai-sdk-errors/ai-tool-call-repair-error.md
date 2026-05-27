---
title: ToolCallRepairError
description: Learn how to fix AI SDK ToolCallRepairError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-tool-call-repair-error.mdx"
---

# ToolCallRepairError

This error occurs when there is a failure while attempting to repair an invalid tool call.
This typically happens when the AI attempts to fix either
a `NoSuchToolError` or `InvalidToolInputError`.

## Properties

- `originalError`: The original error that triggered the repair attempt (either `NoSuchToolError` or `InvalidToolInputError`)
- `message`: The error message
- `cause`: The underlying error that caused the repair to fail

## Checking for this Error

You can check if an error is an instance of `ToolCallRepairError` using:

```typescript
import { ToolCallRepairError } from 'ai';

if (ToolCallRepairError.isInstance(error)) {
  // Handle the error
}
```
