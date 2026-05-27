---
title: generateId
description: Generate a unique identifier (API Reference)
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/01-ai-sdk-core/90-generate-id.mdx"
---

# `generateId()`

Generates a unique identifier.

This is the same id generator used by the AI SDK.

```ts
import { generateId } from 'ai';

const id = generateId();
```

## Import

<Snippet text={`import { generateId } from "ai"`} prompt={false} />

## API Signature

### Returns

A string representing the generated ID.

## See also

- [`createIdGenerator()`](/docs/reference/ai-sdk-core/create-id-generator)
