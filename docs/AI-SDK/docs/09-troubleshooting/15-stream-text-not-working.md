---
title: streamText fails silently
description: Troubleshooting errors related to the streamText function not working.
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/09-troubleshooting/15-stream-text-not-working.mdx"
---

# `streamText` is not working

## Issue

I am using [`streamText`](/docs/reference/ai-sdk-core/stream-text) function, and it does not work.
It does not throw any errors and the stream is only containing error parts.

## Background

`streamText` immediately starts streaming to enable sending data without waiting for the model.
Errors become part of the stream and are not thrown to prevent e.g. servers from crashing.

## Solution

To log errors, you can provide an `onError` callback that is triggered when an error occurs.

```tsx highlight="6-8"
import { streamText } from 'ai';
__PROVIDER_IMPORT__;

const result = streamText({
  model: __MODEL__,
  prompt: 'Invent a new holiday and describe its traditions.',
  onError({ error }) {
    console.error(error); // your error logging logic here
  },
});
```
