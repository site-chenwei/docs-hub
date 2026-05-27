---
title: AI_NoTranscriptGeneratedError
description: Learn how to fix AI_NoTranscriptGeneratedError
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/05-ai-sdk-errors/ai-no-transcript-generated-error.mdx"
---

# AI_NoTranscriptGeneratedError

This error occurs when no transcript could be generated from the input.

## Properties

- `responses`: Array of transcription model response metadata (required in constructor)

## Checking for this Error

You can check if an error is an instance of `AI_NoTranscriptGeneratedError` using:

```typescript
import { NoTranscriptGeneratedError } from 'ai';

if (NoTranscriptGeneratedError.isInstance(error)) {
  // Handle the error
}
```
