---
title: getAIState
description: Reference for the getAIState function from the AI SDK RSC
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/07-reference/03-ai-sdk-rsc/06-get-ai-state.mdx"
---

# `getAIState`

<Note type="warning">
  AI SDK RSC is currently experimental. We recommend using [AI SDK
  UI](/docs/ai-sdk-ui/overview) for production. For guidance on migrating from
  RSC to UI, see our [migration guide](/docs/ai-sdk-rsc/migrating-to-ui).
</Note>

Get the current AI state.

## Import

<Snippet text={`import { getAIState } from "@ai-sdk/rsc"`} prompt={false} />

## API Signature

### Parameters

<PropertiesTable
  content={[
    {
      name: 'key',
      type: 'string',
      isOptional: true,
      description:
        "Returns the value of the specified key in the AI state, if it's an object.",
    },
  ]}
/>

### Returns

The AI state.

## Examples

<ExampleLinks
  examples={[
    {
      title:
        'Learn to render a React component during a tool call made by a language model in Next.js',
      link: '/examples/next-app/tools/render-interface-during-tool-call',
    },
  ]}
/>
