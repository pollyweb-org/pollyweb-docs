# 🈯 TRANSLATE 📃 script

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`TRANSLATE`](<🈯 TRANSLATE ⌘ cmd.md>) command.

## Flow

![alt text](<🈯 TRANSLATE ⚙️ uml.png>)

## How to call

```yaml
- RUN|.TRANSLATE:
    From: en-us
    To: pt-br
    Domains: 
      - any-domain.dom
    Schemas: 
      - any-authority.dom/ANY-SCHEMA
    Text: Any ((not translatable)) text
```

## Script

```yaml
📃 .SHARE:

# Assert inputs
- ASSERT|$.Inputs:
    Texts: From, To, Text
    Lists: Domains, Schemas

# Default the languages
- DEFAULT|$.Inputs:
    From: $.Script.Language
    To: $.Chat.Language

- IF|

# Return the data
- RETURN:
    $translations
```

Uses||
|-|-
|