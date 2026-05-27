---
title: AI_NoSuchModelError
description: Learn how to fix AI_NoSuchModelError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-no-such-model-error.mdx"
---

# AI_NoSuchModelError

This error occurs when a model ID is not found.

## Properties

- `modelId`: The ID of the model that was not found
- `modelType`: The type of model (`'languageModel'`, `'embeddingModel'`, `'imageModel'`, `'transcriptionModel'`, `'speechModel'`, or `'rerankingModel'`)
- `message`: The error message (optional, auto-generated from `modelId` and `modelType`)

## Checking for this Error

You can check if an error is an instance of `AI_NoSuchModelError` using:

```typescript
import { NoSuchModelError } from 'ai';

if (NoSuchModelError.isInstance(error)) {
  // Handle the error
}
```
