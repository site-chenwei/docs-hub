---
title: Model is not assignable to type "LanguageModelV1"
description: Troubleshooting errors related to incompatible models.
source_url: "https://github.com/vercel/ai/blob/ai%406.0.191/content/docs/09-troubleshooting/30-model-is-not-assignable-to-type.mdx"
---

# Model is not assignable to type "LanguageModelV1"

## Issue

I have updated the AI SDK and now I get the following error: `Type 'SomeModel' is not assignable to type 'LanguageModelV1'.`

<Note>Similar errors can occur with `EmbeddingModelV3` as well.</Note>

## Background

Sometimes new features are being added to the model specification.
This can cause incompatibilities with older provider versions.

## Solution

Update your provider packages and the AI SDK to the latest version.
