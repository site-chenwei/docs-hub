---
title: Generate Text
description: Learn how to generate text using the AI SDK and Node
tags: ['node']
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/cookbook/05-node/10-generate-text.mdx"
---

# Generate Text

The most basic LLM use case is generating text based on a prompt.
For example, you may want to generate a response to a question or summarize a body of text.
The `generateText` function can be used to generate text based on the input prompt.

```ts file='index.ts'
import { generateText } from 'ai';

const result = await generateText({
  model: 'openai/gpt-4o',
  prompt: 'Why is the sky blue?',
});

console.log(result);
```
