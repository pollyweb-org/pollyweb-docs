# 🕸 Translate 📃 handler

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Translate@Graph` 🅰️ method](<🕸 Translate 📃 handler.md>).

## Script

```yaml
📃 Translate@Graph:

# Verify the message
- VERIFY|$.Msg

- DEFAULT|$.Msg:
    Language: en-us
    Source: en-us

# Assert required fields
- ASSERT|$.Msg:
    AllOf: Language
    AnyOf: Domain, Domains, Schema, Schemas, Text
    Texts: Language, Text, Source, Domain, Schema
    Lists: Domains, Schemas

# Process Domain(s) translation
- IF|$.Msg.Domain:
    - SEND >> $about:
        Subject: About@Graph
        Domain: $.Msg.Domain
```