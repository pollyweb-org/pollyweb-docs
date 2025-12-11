# 🕸 Translate 📃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Translate@Graph` 📨 msg](<🕸 Translate 📃 handler.md>).

<br/>

## Script

```yaml
📃 Translate@Graph:

# Verify the message
- VERIFY $.Msg

# Default the language to american english
- DEFAULT $.Msg:
    Language: en-us
    Source: en-us

# Assert required fields
- ASSERT $.Msg:
    AllOf: Language
    AnyOf: Domain, Domains, Schema, Schemas, Text
    Texts: Language, Text, Source, Domain, Schema
    Lists: Domains, Schemas

# Process Domain(s) translation
- IF $.Msg.Domain:
    - SEND >> $about:
        Header:
            To: .Hosted.Domain
            Subject: About@Graph
        Body:
            Domain: $.Msg.Domain.Require
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)