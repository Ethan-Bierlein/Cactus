---
title: Markdown Style Guide
site_area: Docs
layout: default
permalink: /Docs/Contrib/MarkdownStyleGuide/
---

## File Naming Convention:

- Use a `CamelCaseName`
- First letter capitalized
- The extension should *always* be `.md`

### Example:

- `Markdown.md`
- `TacoTuesday.md`

## Basic Syntax:

- Use `**Bold**` for **Bold Text**
- Use `*Italics*` for *Italic Text* (**not** `_My Text_`)
- Include the punctuation in the bold/italic tag if the tag ends at the end of the sentence (Bad: `I like **cheese**.`; Good: `I like **cheese.**`)
- Avoid using horizontal rules
- If you need to, use the `-` character and make it *exactly* 80 characters long
- Use inline links (`[GitHub](http://github.com)`)
- Always include `http://` or `https://`
- Make the link bold to make it obvious that it is a link
- If a bold/italic tag is for the all of the link's text, put the tag outside of the link (Bad: `[**GitHub**](http://github.com)`; Good: `**[GitHub](http://github.com)**`)

## Headings:

- Use "ATX" style (`#` or `###`) with **no closing tags**
- Do not skip a heading level--instead, go from `H1` (`#`) directly to `H2` to `H3` and so on
- There should only be one `H1` heading--the title of the document
- There should be only one space between the heading symbol (the `#`) and the title
- Each heading should end with a colon (`:`)
- Do not use bold or italic text in place of heading, nor use bold or italics in a heading tag
- Leave a blank line before and after

### Example:

```markdown
# A Very Important Document:

## Introduction:

## Description of Problem:

## Proposed Solution:

### Execution:

### Cost:

## Conclusion:
```

## Whitespace/Newlines:

- No trailing whitespace
- No elements should be indented--except *some* code blocks (see "Code"), second level or lower list elements (see "Lists"), or anything inside a code block
- Do not use HTML elements such as `<br />` to do a newline; instead, leave a blank line between different paragraphs
- Do not have two or more consecutive blank lines in the source file
- Leave one blank line at the very end of the document

## Code:

- Use the ` ``` ` notation for a block of code whenever possible instead of the four space indentation
- Always use a "language tag" or equivalent to tell the interpreter how to highlight the syntax
- With GitHub Markdown, you can write the language on the opening line (see example below)
- Leave a blank line before and after

### Example:

<!--Note: I had to break this rule below because I can't have backticks in backticks :)-->

````c++
int sum(int x, int y) {
  return x + y;
}
```

## Lists:

- Unordered lists should use the `-` character
- Keep each line short for readability
- Do not indent level one list items; indent all lower levels by two spaces per level
- Have one space after the `-` character
- Leave a blank line before and after each list

### Example:

```markdown
- First Element
- Second Element
- Third Element
- Another First Element
```

## Tables:

- Don't use trailing or leading pipes
- Use a space before and after each pipe
- The width of a column is dependent on the largest item in it

### Example:

```markdown
Employee ID | Name         | Favorite Beverage
----------- | ------------ | -----------------
1           | Bobby Tables | Water
2           | Matthew      | Dr. Pepper
3           | No Name      | Snapple Tea
4           | A Person     | N/A
```

## Comments:

- Avoid unneeded comments
- Add comments to explain anything that is unusual and should be noted by any editor of the file
- Use the standard HTML format for comments: `<!--My note here!-->`

## Other:

- Only use **one** space between each sentence
