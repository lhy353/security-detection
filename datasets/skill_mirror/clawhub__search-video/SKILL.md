---
name: search-video
version: 1.0.9
description: 'Video search tool: queries Pixabay video API for stock clips, returning URLs and metadata for footage sourcing.'
metadata:
  {
    'openclaw': { 'systemPrompt': 'When invoking this skill, call the search-video tool.' },
  }
---

# search-video

Video search tool: queries Pixabay video API for stock clips, returning URLs and metadata for footage sourcing.

## Trigger Keywords

- search-video
- pixabay video
- video search

## Usage

Invoke the `search-video` tool with a structured input object.

```ts
{
  query: string;
  videoType?: "all" | "film" | "animation";
  category?: string;
  minDuration?: number;
  maxDuration?: number;
  page?: number;
  perPage?: number;
}
```

## Notes

- Pixabay performs best with English keywords.
- Surface the best preview or source URLs plus short metadata.
- If no result is found, suggest a broader keyword.

## Example

```ts
search-video({
  query: "technology background",
  videoType: "film",
  minDuration: 5,
  perPage: 6,
})
```
