---
title: Streaming Not Working When Deployed
description: Troubleshooting streaming issues in deployed apps.
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/09-troubleshooting/06-streaming-not-working-when-deployed.mdx"
---

# Streaming Not Working When Deployed

## Issue

Streaming with the AI SDK works in my local development environment.
However, when deploying, streaming does not work in the deployed app.
Instead of streaming, only the full response is returned after a while.

## Cause

The causes of this issue are varied and depend on the deployment environment.

## Solution

You can try the following:

- add `'Transfer-Encoding': 'chunked'` and/or `Connection: 'keep-alive'` headers

  ```tsx
  return result.toUIMessageStreamResponse({
    headers: {
      'Transfer-Encoding': 'chunked',
      Connection: 'keep-alive',
    },
  });
  ```
